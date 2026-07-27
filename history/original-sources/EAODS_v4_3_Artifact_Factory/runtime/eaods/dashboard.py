from __future__ import annotations

from pathlib import Path
from typing import Any
import json

from .io import load_yaml, write_text
from .evidence import evidence_summary


def load_workflows(workflow_dir: str | Path) -> list[dict[str, Any]]:
    root = Path(workflow_dir)
    if not root.exists():
        return []
    records = []
    for p in root.glob("*.yaml"):
        try:
            data = load_yaml(p)
            data["_path"] = str(p)
            records.append(data)
        except Exception:
            continue
    return records


def build_dashboard(
    workflow_dir: str | Path = "workflows",
    evidence_ledger: str | Path = "evidence/evidence_ledger.yaml",
    output_path: str | Path = "dashboards/eaods_dashboard.md",
) -> Path:
    workflows = load_workflows(workflow_dir)
    statuses: dict[str, int] = {}
    high_risk = 0
    approval_queue = 0

    for wf in workflows:
        status = wf.get("status", "unknown")
        statuses[status] = statuses.get(status, 0) + 1
        for risk in wf.get("risks", []) or []:
            rating = str(risk.get("rating", "")).lower() if isinstance(risk, dict) else ""
            if rating in {"high", "critical"}:
                high_risk += 1
        if status in {"human_review", "blocked"} or wf.get("approval_gates"):
            approval_queue += 1

    ev = evidence_summary(evidence_ledger)

    md = f"""---
title: "EAODS Operator Dashboard"
version: "4.2.0-alpha"
---

# EAODS Operator Dashboard

## Workflow Metrics

| Metric | Value |
|---|---:|
| Workflow Count | {len(workflows)} |
| Approval Queue | {approval_queue} |
| High/Critical Risk Items | {high_risk} |
| Evidence Records | {ev['total_records']} |

## Workflow Status

| Status | Count |
|---|---:|
"""
    for status, count in sorted(statuses.items()):
        md += f"| {status} | {count} |\n"

    md += """

## Evidence by Type

| Type | Count |
|---|---:|
"""
    for typ, count in sorted(ev["by_type"].items()):
        md += f"| {typ} | {count} |\n"

    md += """

## Evidence by Sensitivity

| Sensitivity | Count |
|---|---:|
"""
    for sensitivity, count in sorted(ev["by_sensitivity"].items()):
        md += f"| {sensitivity} | {count} |\n"

    path = Path(output_path)
    write_text(path, md)
    return path


def build_dashboard_json(
    workflow_dir: str | Path = "workflows",
    evidence_ledger: str | Path = "evidence/evidence_ledger.yaml",
    output_path: str | Path = "dashboards/eaods_dashboard.json",
) -> Path:
    workflows = load_workflows(workflow_dir)
    ev = evidence_summary(evidence_ledger)
    payload = {
        "workflow_count": len(workflows),
        "evidence": ev,
        "statuses": {},
    }
    for wf in workflows:
        status = wf.get("status", "unknown")
        payload["statuses"][status] = payload["statuses"].get(status, 0) + 1

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path
