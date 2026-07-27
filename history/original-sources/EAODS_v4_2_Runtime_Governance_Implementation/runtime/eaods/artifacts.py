from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from .io import write_text
from .registry import AgentRegistry


def generate_handbook(agent_id: str, output_dir: str | Path = "artifacts", registry_path: str | Path = "agents.yaml") -> Path:
    registry = AgentRegistry(registry_path)
    agent = registry.get(agent_id)
    generated = datetime.now(timezone.utc).isoformat()

    title = f"{agent['name']} Handbook"
    approval_gates = agent.get("approval_gates", [])
    outputs = agent.get("outputs", [])

    md = f"""---
title: "{title}"
version: "4.0.0-alpha"
agent_id: "{agent_id}"
owner: "Ivan Rozenblad"
generated: "{generated}"
classification: "Internal / Portfolio / Commercialization Candidate"
role: "{agent.get('role', '')}"
status: "Runtime Generated Draft"
---

# {title}

## Executive Summary

This runtime-generated handbook establishes the operating specification for the **{agent['name']}**.

## Mission

Support EAODS workflows as: **{agent.get('role', '')}**.

## Scope

### In Scope

- Structured intake
- Workflow support
- Evidence management
- Risk-aware recommendations
- QA-ready documentation
- Human approval routing where required

### Out of Scope

- Unsupported legal conclusions
- Unapproved production changes
- Secret handling outside approved controls
- High-impact decisions without human approval

## Inputs

- User request
- workflow state
- source documents
- assumptions
- evidence references

## Outputs

"""
    for item in outputs:
        md += f"- {item}\n"

    md += """

## Approval Gates

"""
    if approval_gates:
        for gate in approval_gates:
            md += f"- {gate}\n"
    else:
        md += "- No special approval gate defined beyond standard EAODS QA.\n"

    md += """

## Standard Workflow

```mermaid
flowchart TD
    A[Intake] --> B[Scope]
    B --> C[Evidence]
    C --> D[Analysis]
    D --> E[Risk Review]
    E --> F[Draft]
    F --> G[QA]
    G --> H[Human Approval if Required]
    H --> I[Publish]
    I --> J[Archive]
```

## QA Checklist

- [ ] YAML metadata complete.
- [ ] Scope is clear.
- [ ] Assumptions are documented.
- [ ] Evidence is identified.
- [ ] Risks are assessed.
- [ ] Human approval gates are applied.
- [ ] Deliverables are reusable.
- [ ] Final artifact is ready for repository storage.

## Case Studies

### Case Study 1 — Standard Operational Request

A user requests a structured deliverable. The agent converts the request into a scoped workflow, identifies evidence, drafts the artifact, and routes it through QA.

### Case Study 2 — High-Impact Review

The workflow includes a sensitive recommendation. The agent identifies the approval gate and prevents publication until human review is complete.

### Case Study 3 — Documentation Reuse

A repeated workflow is converted into a template, SOP, or case study and stored in the EAODS knowledge base.

### Case Study 4 — Evidence Gap

The agent detects missing evidence and creates an assumptions log rather than overstating certainty.

### Case Study 5 — Cross-Agent Handoff

The agent produces an output consumed by another specialist agent and documents the handoff criteria.

## Improvement Backlog

- Add agent-specific tests.
- Add structured JSON output mode.
- Add evidence ID support.
- Add dashboard metrics.
- Add RAG ingestion metadata.
"""

    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{agent_id}_handbook_runtime.md"
    write_text(path, md)
    return path
