from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import json
import re
import shutil

from .io import load_yaml, write_text
from .evidence import list_evidence, evidence_summary


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "artifact"


@dataclass
class ArtifactContext:
    title: str
    owner: str = "Ivan Rozenblad"
    version: str = "4.3.0-alpha"
    classification: str = "Internal / Portfolio / Commercialization Candidate"
    purpose: str = ""
    scope: str = ""
    audience: str = ""
    workflow_id: str = ""
    agent_id: str = ""
    assumptions: list[str] | None = None
    risks: list[str] | None = None
    evidence: list[dict[str, Any]] | None = None

    def to_frontmatter(self, artifact_type: str) -> str:
        generated = datetime.now(timezone.utc).isoformat()
        assumptions = self.assumptions or []
        risks = self.risks or []
        fm = f"""---
title: "{self.title}"
artifact_type: "{artifact_type}"
version: "{self.version}"
owner: "{self.owner}"
generated: "{generated}"
classification: "{self.classification}"
workflow_id: "{self.workflow_id}"
agent_id: "{self.agent_id}"
audience: "{self.audience}"
assumptions:
"""
        for item in assumptions:
            fm += f'  - "{item}"\n'
        fm += "risks:\n"
        for item in risks:
            fm += f'  - "{item}"\n'
        fm += "---\n"
        return fm


def context_from_workflow(workflow_path: str | Path | None = None, **kwargs: Any) -> ArtifactContext:
    data: dict[str, Any] = {}
    if workflow_path:
        path = Path(workflow_path)
        if path.exists():
            data = load_yaml(path)

    title = kwargs.get("title") or data.get("title") or "EAODS Artifact"
    goal = data.get("goal", "")
    assumptions = data.get("assumptions", []) or []
    risks_raw = data.get("risks", []) or []
    risks: list[str] = []
    for risk in risks_raw:
        if isinstance(risk, dict):
            risks.append(risk.get("risk_statement") or risk.get("statement") or str(risk))
        else:
            risks.append(str(risk))

    return ArtifactContext(
        title=title,
        purpose=kwargs.get("purpose") or goal,
        scope=kwargs.get("scope") or data.get("scope", ""),
        audience=kwargs.get("audience") or data.get("audience", ""),
        workflow_id=data.get("workflow_id", ""),
        agent_id=kwargs.get("agent_id") or (data.get("required_agents", [""])[0] if data.get("required_agents") else ""),
        assumptions=assumptions,
        risks=risks,
        evidence=kwargs.get("evidence"),
    )


def evidence_section(records: list[dict[str, Any]] | None) -> str:
    if not records:
        return "## Evidence References\n\nNo evidence records attached.\n"
    md = "## Evidence References\n\n| Evidence ID | Title | Type | Sensitivity | Source |\n|---|---|---|---|---|\n"
    for r in records:
        source = r.get("source_path") or r.get("source_url") or ""
        md += f"| {r.get('evidence_id','')} | {r.get('title','')} | {r.get('evidence_type','')} | {r.get('sensitivity','')} | {source} |\n"
    return md


def qa_section() -> str:
    return """## QA Checklist

- [ ] YAML metadata complete.
- [ ] Purpose and scope are clear.
- [ ] Assumptions are identified.
- [ ] Risks are identified.
- [ ] Evidence is attached or explicitly absent.
- [ ] Human approval gate is identified.
- [ ] Artifact is safe for its intended audience.
- [ ] Artifact is stored in the correct repository location.

## Human Review Gate

This artifact should be reviewed by the accountable human owner before external publication, client delivery, regulated use, or high-impact operational action.
"""


def generate_sop(context: ArtifactContext, output_dir: str | Path = "artifacts/sops") -> Path:
    md = context.to_frontmatter("SOP")
    md += f"""# {context.title} — Standard Operating Procedure

## Purpose

{context.purpose or "Define a repeatable operating procedure for this workflow."}

## Scope

{context.scope or "This SOP applies to the defined EAODS workflow and related artifacts."}

## Roles and Responsibilities

| Role | Responsibility |
|---|---|
| Owner | Accountable for procedure outcome |
| Operator | Performs the procedure |
| Reviewer | Validates quality and approval requirements |
| Orchestrator | Routes workflow and enforces gates |

## Procedure

1. Intake the request.
2. Confirm scope and audience.
3. Identify required evidence.
4. Assign responsible agent or owner.
5. Execute the procedure.
6. Document risks, assumptions, and outputs.
7. Perform QA review.
8. Route to human approval where required.
9. Publish or archive the artifact.
10. Record lessons learned.

## Records and Evidence

Procedure records should include workflow state, evidence records, approval notes, and final artifacts.

{evidence_section(context.evidence)}
{qa_section()}
"""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{slugify(context.title)}_sop.md"
    write_text(path, md)
    return path


def generate_policy(context: ArtifactContext, output_dir: str | Path = "artifacts/policies") -> Path:
    md = context.to_frontmatter("Policy")
    md += f"""# {context.title} — Policy

## Policy Statement

The organization shall manage this area using documented scope, accountable ownership, risk-based review, evidence retention, and human approval for high-impact decisions.

## Purpose

{context.purpose or "Establish governance requirements for this domain."}

## Scope

{context.scope or "This policy applies to workflows, artifacts, agents, and human operators within the relevant EAODS domain."}

## Requirements

1. All work must be scoped.
2. All material assumptions must be documented.
3. High-impact actions require human approval.
4. Evidence must be retained when used to support decisions.
5. Artifacts must pass QA before publication.
6. Sensitive data must be minimized.
7. Exceptions must be documented.

## Exceptions

Exceptions require owner approval, documented rationale, and review date.

## Monitoring and Enforcement

Compliance should be reviewed through artifact scoring, evidence ledger completeness, dashboard metrics, and periodic governance review.

{evidence_section(context.evidence)}
{qa_section()}
"""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{slugify(context.title)}_policy.md"
    write_text(path, md)
    return path


def generate_case_study(context: ArtifactContext, output_dir: str | Path = "artifacts/case_studies") -> Path:
    md = context.to_frontmatter("Case Study")
    md += f"""# {context.title} — Enterprise Case Study

## Executive Scenario

{context.purpose or "A workflow required structured agent-supported execution and governance."}

## Business Context

This case demonstrates how EAODS converts an operational need into a governed workflow with evidence, risk handling, QA, approval gates, and reusable documentation.

## Stakeholders

- Owner
- Operator
- Reviewer
- Affected business or technical stakeholder
- Documentation maintainer

## Objectives

- Define scope.
- Identify evidence.
- Execute the workflow.
- Produce a reusable artifact.
- Preserve lessons learned.

## Workflow

```mermaid
flowchart TD
    A[Request] --> B[Scope]
    B --> C[Evidence]
    C --> D[Execution]
    D --> E[Risk Review]
    E --> F[QA]
    F --> G[Human Review]
    G --> H[Publish]
    H --> I[Archive]
```

## Risks and Controls

| Risk | Control |
|---|---|
| Incomplete evidence | Evidence ledger and assumptions log |
| Unapproved high-impact action | Human approval gate |
| Poor reuse | Template and case-study conversion |
| Sensitive disclosure | Audience review and redaction |

## Deliverables

- Workflow summary
- Evidence list
- Risk notes
- Final artifact
- Lessons learned
- Improvement backlog

{evidence_section(context.evidence)}
{qa_section()}
"""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{slugify(context.title)}_case_study.md"
    write_text(path, md)
    return path


def generate_client_deliverable(context: ArtifactContext, output_dir: str | Path = "artifacts/client_deliverables") -> Path:
    md = context.to_frontmatter("Client Deliverable")
    md += f"""# {context.title} — Client Deliverable

## Executive Summary

{context.purpose or "This deliverable summarizes the work performed, findings, recommendations, and next steps in a client-safe format."}

## Scope of Work

{context.scope or "Scope should be confirmed before external delivery."}

## Assumptions

"""
    for item in context.assumptions or ["No assumptions documented."]:
        md += f"- {item}\n"
    md += """
## Findings

- Finding 1: To be completed.
- Finding 2: To be completed.
- Finding 3: To be completed.

## Recommendations

| Priority | Recommendation | Owner | Timeline |
|---|---|---|---|
| High | Confirm and remediate priority issue | Client / Owner | 30 days |
| Medium | Improve documentation and evidence | Owner | 90 days |
| Low | Monitor and review periodically | Owner | Ongoing |

## Limitations

This deliverable is based on the provided information and does not replace qualified legal, financial, compliance, or security review where such review is required.

{qa_section()}
"""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{slugify(context.title)}_client_deliverable.md"
    write_text(path, md)
    return path


def generate_portfolio_page(context: ArtifactContext, output_dir: str | Path = "artifacts/portfolio") -> Path:
    md = context.to_frontmatter("Portfolio Page")
    md += f"""# {context.title} — Portfolio Page

## Project Overview

{context.purpose or "This project demonstrates structured AI-assisted enterprise workflow design and documentation."}

## Problem

The work required a repeatable system for turning requests into governed, reusable, high-quality artifacts.

## Solution

EAODS was used to structure scope, evidence, workflow, risk, QA, and publication readiness.

## Tools and Concepts

- Python
- Markdown
- YAML
- Agent registry
- Workflow state
- Evidence ledger
- Policy engine
- Prompt-injection firewall
- Artifact factory

## Outcomes

- Generated reusable artifact.
- Preserved evidence and assumptions.
- Improved documentation quality.
- Created portfolio-ready proof of work.

## Skills Demonstrated

- AI systems design
- Cybersecurity governance
- Documentation engineering
- Risk management
- Python automation
- Repository organization

{qa_section()}
"""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{slugify(context.title)}_portfolio_page.md"
    write_text(path, md)
    return path


def generate_evidence_binder(context: ArtifactContext, output_dir: str | Path = "artifacts/evidence_binders") -> Path:
    md = context.to_frontmatter("Evidence Binder")
    md += f"""# {context.title} — Evidence Binder

## Binder Purpose

This binder organizes evidence supporting the workflow, artifact, decision, or release.

## Evidence Summary

"""
    if context.evidence:
        md += evidence_section(context.evidence)
    else:
        md += "No evidence records were attached.\n"
    md += """

## Decision Support

| Decision | Evidence | Approval |
|---|---|---|
| Proceed with artifact review | Evidence ledger records | Owner review required |

## Binder QA

- [ ] Evidence is relevant.
- [ ] Evidence sensitivity is correctly classified.
- [ ] Source paths or URLs are recorded.
- [ ] Hashes are present where source files exist.
- [ ] Binder is suitable for intended audience.
"""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{slugify(context.title)}_evidence_binder.md"
    write_text(path, md)
    return path


def generate_release_bundle(context: ArtifactContext, output_dir: str | Path = "artifacts/release_bundles") -> Path:
    md = context.to_frontmatter("Release Bundle")
    md += f"""# {context.title} — Release Bundle

## Release Summary

{context.purpose or "This release bundle summarizes artifacts prepared for review, publication, or archival."}

## Included Artifacts

- SOP
- Policy
- Case study
- Client-safe deliverable
- Portfolio page
- Evidence binder

## Release Checklist

- [ ] All artifacts generated.
- [ ] QA complete.
- [ ] Evidence reviewed.
- [ ] Sensitive data removed.
- [ ] Human approval obtained.
- [ ] Version assigned.
- [ ] Release notes prepared.
- [ ] Archive location confirmed.

## Release Decision

- [ ] Approved
- [ ] Approved with changes
- [ ] Rejected

{qa_section()}
"""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{slugify(context.title)}_release_bundle.md"
    write_text(path, md)
    return path


def generate_all_artifacts(
    title: str,
    workflow_path: str | Path | None = None,
    evidence_ledger: str | Path | None = None,
    output_root: str | Path = "artifacts",
) -> dict[str, str]:
    evidence = list_evidence(evidence_ledger) if evidence_ledger and Path(evidence_ledger).exists() else []
    ctx = context_from_workflow(workflow_path, title=title, evidence=evidence)
    root = Path(output_root)

    outputs = {
        "sop": generate_sop(ctx, root / "sops"),
        "policy": generate_policy(ctx, root / "policies"),
        "case_study": generate_case_study(ctx, root / "case_studies"),
        "client_deliverable": generate_client_deliverable(ctx, root / "client_deliverables"),
        "portfolio_page": generate_portfolio_page(ctx, root / "portfolio"),
        "evidence_binder": generate_evidence_binder(ctx, root / "evidence_binders"),
        "release_bundle": generate_release_bundle(ctx, root / "release_bundles"),
    }
    return {k: str(v) for k, v in outputs.items()}
