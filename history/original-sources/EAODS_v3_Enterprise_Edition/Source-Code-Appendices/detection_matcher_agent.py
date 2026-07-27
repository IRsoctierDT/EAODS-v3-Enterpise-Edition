"""Detection Matcher Agent — links triage to detection content.

Given a MITRE ATT&CK technique (the one the SOC Analyst / MITRE Mapper agents
emit), it returns the Sigma rules in ``detections/sigma/`` that cover that
technique. This closes the loop between *triage* (what happened) and *detection
engineering* (what alerts on it), using the shared ATT&CK vocabulary.

Design (DESIGN.md §5):
- **Read-only, network-free, deterministic.** It only reads the local Sigma
  corpus and matches on technique tags.
- **Fails soft.** A missing corpus — or PyYAML not being installed — yields no
  matches rather than an error, so the agent pipeline degrades gracefully and the
  package keeps a dependency-free core.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

try:  # PyYAML ships with the dev/dashboard extras; core stays import-safe without it.
    import yaml
except ModuleNotFoundError:  # pragma: no cover - yaml is present in dev/CI
    yaml = None

DEFAULT_SIGMA_DIR = Path("detections/sigma")

# Sigma severity order for ranking matches (most severe first).
_LEVEL_RANK: dict[str, int] = {
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
    "informational": 4,
}


@dataclass(frozen=True)
class DetectionMatch:
    """A Sigma rule that covers a given technique."""

    rule_id: str
    title: str
    level: str
    technique: str
    file: str


class DetectionMatcherAgent:
    """Map a MITRE technique to the Sigma rules that detect it."""

    def __init__(self, sigma_dir: Path | str = DEFAULT_SIGMA_DIR) -> None:
        self.sigma_dir = Path(sigma_dir)

    @staticmethod
    def _normalize(technique_id: str) -> str:
        """``"T1136.001"`` -> ``"t1136.001"`` to compare against Sigma tags."""
        return technique_id.strip().lower()

    def _load_rules(self) -> list[dict[str, Any]]:
        if yaml is None or not self.sigma_dir.is_dir():
            return []
        rules: list[dict[str, Any]] = []
        for path in sorted(self.sigma_dir.glob("*.yml")):
            try:
                parsed = yaml.safe_load(path.read_text(encoding="utf-8"))
            except yaml.YAMLError:
                continue
            if isinstance(parsed, dict):
                parsed["__file__"] = path.name
                rules.append(parsed)
        return rules

    def match_for_technique(self, technique_id: str) -> list[dict[str, Any]]:
        """Return Sigma rules whose ATT&CK tags include ``technique_id``.

        Matching is exact on the technique (e.g. ``T1110``). A rule tagged with a
        sub-technique (``t1136.001``) matches its parent query only if the parent
        id is supplied; callers pass whatever the MITRE Mapper emitted.
        """
        target = self._normalize(technique_id)
        if not target or target in {"unknown", "t"}:
            return []
        wanted = f"attack.{target}"

        matches: list[DetectionMatch] = []
        for rule in self._load_rules():
            tags = [str(t).lower() for t in rule.get("tags", [])]
            if wanted in tags:
                matches.append(
                    DetectionMatch(
                        rule_id=str(rule.get("id", "")),
                        title=str(rule.get("title", "")),
                        level=str(rule.get("level", "unknown")),
                        technique=technique_id.strip().upper(),
                        file=str(rule.get("__file__", "")),
                    )
                )
        # Most severe first; ties broken by title for a stable order.
        matches.sort(key=lambda m: (_LEVEL_RANK.get(m.level, 99), m.title))
        return [asdict(m) for m in matches]

    def match_for_event(self, mitre_result: dict[str, Any]) -> list[dict[str, Any]]:
        """Convenience: match using the ``technique_id`` from a MITRE result."""
        technique_id = mitre_result.get("technique_id")
        if not isinstance(technique_id, str):
            return []
        return self.match_for_technique(technique_id)


if __name__ == "__main__":
    import json

    agent = DetectionMatcherAgent()
    print(json.dumps(agent.match_for_technique("T1110"), indent=2))
