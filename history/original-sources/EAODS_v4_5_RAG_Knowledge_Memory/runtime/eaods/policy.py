from __future__ import annotations

from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any
import json

try:
    from .io import load_yaml
except ImportError:  # pragma: no cover
    from io import load_yaml  # type: ignore


@dataclass
class PolicyDecision:
    decision: str
    reason: str
    risk_tier: int
    required_actions: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


SECRET_PATTERNS = ["api_key", "password=", "secret=", "token=", "private_key"]


def evaluate_action(action: dict[str, Any]) -> PolicyDecision:
    risk_tier = int(action.get("risk_tier", 1))
    approval_status = bool(action.get("approval_status", False))
    evidence = action.get("evidence", [])
    text = str(action).lower()

    if any(k in text for k in SECRET_PATTERNS):
        return PolicyDecision(
            "deny",
            "Potential secret exposure detected.",
            risk_tier,
            ["Remove secrets", "Rotate exposed credential if real", "Re-run scan"],
        )

    if risk_tier >= 5:
        return PolicyDecision(
            "require_qualified_review",
            "Tier 5 regulated or high-impact decision.",
            risk_tier,
            ["Qualified human review", "Document authority and assumptions"],
        )

    if risk_tier >= 2 and not approval_status:
        return PolicyDecision(
            "require_approval",
            "Risk tier requires human approval.",
            risk_tier,
            ["Obtain approval", "Record approval in evidence ledger"],
        )

    if action.get("requires_evidence") and not evidence:
        return PolicyDecision(
            "require_evidence",
            "Required evidence is missing.",
            risk_tier,
            ["Attach evidence record"],
        )

    return PolicyDecision(
        "allow_with_logging",
        "Action may proceed with logging.",
        risk_tier,
        ["Record action in workflow history"],
    )


def load_action(path: str | Path) -> dict[str, Any]:
    path = Path(path)
    if path.suffix.lower() == ".json":
        return json.loads(path.read_text(encoding="utf-8"))
    return load_yaml(path)
