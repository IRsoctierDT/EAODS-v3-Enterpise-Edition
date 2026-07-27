---
title: "EAODS Runtime Alpha Scaffold"
version: "4.0.0-alpha"
owner: "Ivan Rozenblad"
generated: "2026-07-07T19:32:25.462059+00:00"
classification: "Internal / Portfolio / Commercialization Candidate"
---

# EAODS Runtime Alpha Scaffold

This runtime scaffold converts EAODS from a documentation-only suite into a minimal working operator framework.

## Included Runtime Components

- `eaods.cli` command-line interface
- `agents.yaml` agent registry
- workflow state generation
- risk-tier action classification
- runtime handbook generation
- Markdown artifact scoring
- release note generation
- pytest test suite
- GitHub Actions runtime test workflow

## Installation

```bash
cd runtime
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Commands

```bash
python -m eaods.cli agents
python -m eaods.cli route "Build SOC 2 readiness package"
python -m eaods.cli classify "deploy production change"
python -m eaods.cli new-workflow --title "SOC 2 Readiness" --goal "Build SOC 2 readiness package"
python -m eaods.cli generate-handbook orchestrator
python -m eaods.cli score artifacts/orchestrator_handbook_runtime.md
python -m eaods.cli release-notes v4.0.0-alpha
```

## Design Boundary

This alpha runtime does not autonomously execute system commands, deploy infrastructure, access secrets, or contact external parties. It creates the safe control-plane foundation first.

## Next Engineering Step

Add persistent workflow history, richer validation, and RAG ingestion metadata.
