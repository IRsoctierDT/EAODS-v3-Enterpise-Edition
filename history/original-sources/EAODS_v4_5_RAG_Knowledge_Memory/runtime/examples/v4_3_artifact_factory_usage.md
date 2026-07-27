---
title: "EAODS v4.3 Artifact Factory Usage"
version: "4.3.0-alpha"
---

# EAODS v4.3 Artifact Factory Usage

From the `runtime/` directory:

```bash
python -m eaods.cli artifact sop --title "SOC 2 Readiness"
python -m eaods.cli artifact policy --title "AI Governance"
python -m eaods.cli artifact case-study --title "Cloud Credential Exposure"
python -m eaods.cli artifact client --title "Client Security Assessment"
python -m eaods.cli artifact portfolio --title "EAODS Runtime Project"
python -m eaods.cli artifact binder --title "SOC 2 Evidence Binder"
python -m eaods.cli artifact release-bundle --title "EAODS v4.3 Release"
python -m eaods.cli artifact all --title "SOC 2 Readiness Program"
```

Generate from workflow state:

```bash
python -m eaods.cli new-workflow --title "SOC 2 Readiness Program" --goal "Build governed SOC 2 readiness package"
python -m eaods.cli artifact all --title "SOC 2 Readiness Program" --workflow workflows/workflow_state.yaml
```
