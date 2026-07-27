---
title: "EAODS v4.2 Runtime Governance Implementation"
version: "4.2.0-alpha"
owner: "Ivan Rozenblad"
generated: "2026-07-07T19:39:35.756688+00:00"
classification: "Internal / Portfolio / Commercialization Candidate"
---

# EAODS v4.2 Runtime Governance Implementation

This release implements the governance commands specified in the V4.1 research blueprint.

## New Commands

```bash
python -m eaods.cli policy-check examples/sample_action.yaml
python -m eaods.cli evidence add --title "Source" --type document --source-path ./README.md
python -m eaods.cli evidence list
python -m eaods.cli evidence summary
python -m eaods.cli firewall scan README.md
python -m eaods.cli dashboard
python -m eaods.cli constitution compile --source agent_constitution.yaml --output-dir .
```

## Existing Commands Preserved

```bash
python -m eaods.cli agents
python -m eaods.cli route "Build SOC 2 readiness package"
python -m eaods.cli classify "deploy production change"
python -m eaods.cli new-workflow --title "SOC 2 Readiness" --goal "Build SOC 2 readiness package"
python -m eaods.cli generate-handbook orchestrator
python -m eaods.cli score artifacts/orchestrator_handbook_runtime.md
python -m eaods.cli release-notes v4.2.0-alpha
```

## Implemented Modules

- `policy.py`
- `evidence.py`
- `prompt_firewall.py`
- `dashboard.py`
- `constitution.py`

## Security Boundary

This runtime still does not execute arbitrary shell commands, deploy infrastructure, access secrets, delete files, or contact external parties. It implements the governance layer first.
