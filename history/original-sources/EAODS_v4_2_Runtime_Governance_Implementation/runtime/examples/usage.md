---
title: "EAODS Runtime Alpha Usage"
version: "4.0.0-alpha"
---

# EAODS Runtime Alpha Usage

From the `runtime/` directory:

```bash
python -m eaods.cli agents
python -m eaods.cli route "Build SOC 2 readiness package"
python -m eaods.cli classify "publish sensitive client report"
python -m eaods.cli new-workflow --title "SOC 2 Readiness" --goal "Build SOC 2 readiness package"
python -m eaods.cli generate-handbook orchestrator
python -m eaods.cli score artifacts/orchestrator_handbook_runtime.md
python -m eaods.cli release-notes v4.0.0-alpha
```
