from __future__ import annotations

from pathlib import Path
from typing import Any
import json
import re


DEFAULT_CHECKS = {
    "yaml_completeness": lambda t: t.strip().startswith("---") and t.count("---") >= 2,
    "mission_clarity": lambda t: "## Mission" in t or "# Mission" in t,
    "scope_boundaries": lambda t: "## Scope" in t or "# Scope" in t,
    "workflow_specificity": lambda t: "Workflow" in t and ("mermaid" in t or "1." in t),
    "governance_controls": lambda t: "Governance" in t or "Approval" in t,
    "risk_analysis": lambda t: "Risk" in t,
    "human_approval_gates": lambda t: "Human Approval" in t or "approval gate" in t.lower(),
    "evidence_discipline": lambda t: "Evidence" in t or "source" in t.lower(),
    "qa_checklist": lambda t: "QA Checklist" in t or "Quality Assurance" in t,
    "case_study_depth": lambda t: len(re.findall(r"Case Study", t, flags=re.I)) >= 5,
    "agent_integration": lambda t: "Integration" in t or "Handoff" in t,
    "reusability": lambda t: "Template" in t or "SOP" in t or "reusable" in t.lower(),
    "publishing_readiness": lambda t: "version:" in t and "classification:" in t,
}


def score_markdown(path: str | Path, schema_path: str | Path = "scorecard.schema.json") -> dict[str, Any]:
    path = Path(path)
    schema = json.loads(Path(schema_path).read_text(encoding="utf-8"))
    text = path.read_text(encoding="utf-8", errors="ignore")

    criteria = schema.get("criteria", [])
    details = []
    total = 0

    for c in criteria:
        name = c["name"]
        weight = int(c["weight"])
        passed = DEFAULT_CHECKS.get(name, lambda t: False)(text)
        earned = weight if passed else 0
        total += earned
        details.append({"criterion": name, "weight": weight, "passed": passed, "earned": earned})

    failures = []
    lower = text.lower()
    if "password=" in lower or "api_key=" in lower or "secret=" in lower or "token=" in lower:
        failures.append("secret exposure")
    if "## scope" not in lower and "# scope" not in lower:
        failures.append("no scope statement")
    if "qa checklist" not in lower and "quality assurance" not in lower:
        failures.append("missing QA process")

    return {
        "file": str(path),
        "score": total,
        "minimum_publication_score": schema.get("minimum_publication_score", 85),
        "publication_candidate": total >= schema.get("minimum_publication_score", 85) and not failures,
        "mandatory_failures": failures,
        "details": details,
    }
