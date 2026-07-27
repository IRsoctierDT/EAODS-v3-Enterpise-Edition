---
title: "EAODS v4.2 Runtime Governance Usage"
version: "4.2.0-alpha"
---

# EAODS v4.2 Runtime Governance Usage

From the `runtime/` directory:

```bash
python -m eaods.cli policy-check examples/sample_action.yaml
python -m eaods.cli evidence add --title "Architecture Research" --type document --source-path ../Research/agentic_ai_market_and_architecture_research_2026.md
python -m eaods.cli evidence summary
python -m eaods.cli firewall scan ../README.md
python -m eaods.cli dashboard
python -m eaods.cli constitution compile --source agent_constitution.yaml --output-dir .
pytest
```
