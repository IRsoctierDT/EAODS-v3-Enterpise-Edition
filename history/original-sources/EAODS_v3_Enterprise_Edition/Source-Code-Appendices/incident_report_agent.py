from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

from agents.mitre_mapper_agent import MitreMapperAgent
from agents.soc_analyst_agent import SocAnalystAgent
from agents.tools.llm import Generator
from agents.tools.validation import ValidationError

_NARRATIVE_SYSTEM = (
    "You are a SOC analyst assistant. In 2-3 sentences, summarize ONLY the facts "
    "provided. Do not invent hosts, accounts, IPs, or conclusions not present in the "
    "input. Be precise and defensive."
)


def _md_cell(text: str) -> str:
    """Escape pipe and newline characters so they don't break a Markdown table cell."""
    return text.replace("|", "\\|").replace("\r\n", " ").replace("\n", " ").replace("\r", " ")


def _build_narrative(soc: dict, mitre: dict, generator: Generator | None) -> str:
    """Return an AI-generated narrative, or a clear note when it is off/unavailable.

    Opt-in and fail-soft: with no generator the deterministic report is unchanged;
    if the local model errors, the section records that rather than failing the report.
    """
    if generator is None:
        return "_AI narrative not enabled (no local model configured)._"
    facts = (
        f"event_type={soc.get('event_type')}; severity={soc.get('severity')} "
        f"({soc.get('severity_score')}/100); indicators={soc.get('indicators')}; "
        f"mitre={mitre.get('technique_id')} {mitre.get('technique')}."
    )
    # Prefer grammar-constrained JSON when the backend supports it (e.g. llama.cpp),
    # so the narrative is structured and parseable rather than free text.
    generate_json = getattr(generator, "generate_json", None)
    try:
        if callable(generate_json):
            return _render_structured(generate_json(facts, system=_NARRATIVE_SYSTEM))
        return generator.generate(facts, system=_NARRATIVE_SYSTEM).strip()
    except ValidationError as exc:
        return f"_AI narrative unavailable (generator error: {exc})._"


def _render_structured(data: dict) -> str:
    """Render a grammar-constrained narrative object as Markdown bullets."""
    fields = [
        ("Summary", "summary"),
        ("Assessment", "assessment"),
        ("Recommended next step", "recommended_next_step"),
    ]
    lines = [f"- **{label}:** {_md_cell(str(data[key]))}" for label, key in fields if data.get(key)]
    return "\n".join(lines) or "_AI narrative returned no content._"


class IncidentReportAgent:
    def __init__(self) -> None:
        self.soc_agent = SocAnalystAgent()
        self.mitre_mapper = MitreMapperAgent()

    def generate_report(
        self,
        log_text: str,
        output_path: str,
        *,
        soc_result: dict | None = None,
        mitre_result: dict | None = None,
        kb_references: list[dict] | None = None,
        detection_matches: list[dict] | None = None,
        generator: Generator | None = None,
    ) -> Path:
        """Write a markdown incident report.

        Pass pre-computed ``soc_result`` and ``mitre_result`` to avoid
        re-running analysis when the orchestrator has already done it.
        ``kb_references`` (from the Knowledge Base Agent) adds cited framework
        context; ``detection_matches`` (from the Detection Matcher Agent) lists
        the Sigma rules that cover the event's technique. When either is omitted,
        the report notes that none were attached.
        """
        if soc_result is None:
            soc_result = self.soc_agent.analyze_log(log_text)
        if mitre_result is None:
            mitre_result = self.mitre_mapper.map_event(
                soc_result["event_type"],
                log_text,
            )

        target = Path(output_path)
        target.parent.mkdir(parents=True, exist_ok=True)

        indicators = soc_result.get("indicators", [])
        narrative = _build_narrative(soc_result, mitre_result, generator)

        report = f"""# Incident Report

## Generated
{datetime.now(UTC).isoformat()}

## Summary
{soc_result["summary"]}

## Analyst Narrative (AI-generated)
{narrative}

## Severity
{soc_result["severity"]}

## Event Type
{soc_result["event_type"]}

## MITRE ATT&CK Mapping

- **Tactic:** {mitre_result["tactic"]}
- **Technique:** {mitre_result["technique"]}
- **Technique ID:** {mitre_result["technique_id"]}
- **Confidence:** {mitre_result["confidence"]}

### MITRE Evidence
{chr(10).join(f"- {e}" for e in mitre_result["evidence"])}

### MITRE Investigation Steps
{chr(10).join(f"- {s}" for s in mitre_result["recommended_investigation"])}

## Evidence

| Field | Value | Significance |
|-------|-------|--------------|
{chr(10).join(f"| {_md_cell(e['field'])} | {_md_cell(e['value'])} | {_md_cell(e['significance'])} |" for e in soc_result.get("evidence", [])) or "| — | — | No structured evidence captured. |"}

## Severity Score

**{soc_result.get("severity_score", "N/A")} / 100**

## Indicators
{chr(10).join(f"- `{i}`" for i in indicators) if indicators else "- None detected"}

## Recommended Actions
{chr(10).join(f"- {a}" for a in soc_result["recommended_actions"])}

## Knowledge Base References
{chr(10).join(f"- **{_md_cell(r['source'])}** (relevance {r['score']:.2f}) — {_md_cell(r['snippet'])}" for r in kb_references) if kb_references else "- None captured"}

## Detection Coverage
{chr(10).join(f"- **{_md_cell(d['title'])}** [{d['level']}] — `{d['file']}` ({d['technique']})" for d in detection_matches) if detection_matches else "- No Sigma rule covers this technique yet"}

## Assumptions
{chr(10).join(f"- {a}" for a in soc_result["assumptions"])}
"""

        target.write_text(report, encoding="utf-8")
        return target


if __name__ == "__main__":
    agent = IncidentReportAgent()
    agent.generate_report(
        "Failed password for root from 10.0.0.5 port 22 ssh2",
        "reports/markdown/sample_incident_report.md",
    )
    print("Generated reports/markdown/sample_incident_report.md")
