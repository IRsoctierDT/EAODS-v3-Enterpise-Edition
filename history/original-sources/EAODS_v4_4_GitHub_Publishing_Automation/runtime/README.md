---
title: "EAODS v4.4 GitHub and Publishing Automation"
version: "4.4.0-alpha"
owner: "Ivan Rozenblad"
generated: "2026-07-07T19:45:01.576085+00:00"
classification: "Internal / Portfolio / Commercialization Candidate"
---

# EAODS v4.4 GitHub and Publishing Automation

This release implements publishing automation.

## New Commands

```bash
python -m eaods.cli publish map --root ..
python -m eaods.cli publish mkdocs --root ..
python -m eaods.cli publish changelog --root ..
python -m eaods.cli publish score-all --root ..
python -m eaods.cli publish issue --title "Expand Orchestrator Handbook" --body "Add v4.4 publishing integration."
python -m eaods.cli publish pr --title "docs: add publishing automation" --summary "Adds repository map and release automation."
python -m eaods.cli publish release-candidate --root .. --version v4.4.0-alpha
python -m eaods.cli publish bundles --root .. --version v4.4.0-alpha
```

## New Runtime Module

- `runtime/eaods/publishing.py`

## Strategic Improvement

EAODS can now prepare repository maps, changelogs, MkDocs navigation files, GitHub issue/PR artifacts, release candidates, and public/private bundles.
