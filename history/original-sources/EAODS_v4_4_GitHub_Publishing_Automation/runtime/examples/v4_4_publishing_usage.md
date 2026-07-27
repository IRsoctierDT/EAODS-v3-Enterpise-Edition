---
title: "EAODS v4.4 Publishing Automation Usage"
version: "4.4.0-alpha"
---

# EAODS v4.4 Publishing Automation Usage

From the `runtime/` directory or repository root as appropriate:

```bash
python -m eaods.cli publish map --root ..
python -m eaods.cli publish mkdocs --root ..
python -m eaods.cli publish changelog --root ..
python -m eaods.cli publish score-all --root ..
python -m eaods.cli publish issue --title "Expand Orchestrator Handbook" --body "Add v4.4 publishing integration."
python -m eaods.cli publish pr --title "docs: add publishing automation" --summary "Adds repository map, changelog, release candidate, and bundle automation."
python -m eaods.cli publish release-candidate --root .. --version v4.4.0-alpha
python -m eaods.cli publish bundles --root .. --version v4.4.0-alpha
```
