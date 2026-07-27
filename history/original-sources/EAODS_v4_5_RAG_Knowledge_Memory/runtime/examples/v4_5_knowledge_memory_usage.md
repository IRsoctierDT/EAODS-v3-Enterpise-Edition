---
title: "EAODS v4.5 RAG and Knowledge Memory Usage"
version: "4.5.0-alpha"
---

# EAODS v4.5 RAG and Knowledge Memory Usage

From the `runtime/` directory or repository root as appropriate:

```bash
python -m eaods.cli knowledge inventory --root ..
python -m eaods.cli knowledge chunks --root ..
python -m eaods.cli knowledge stale --root ..
python -m eaods.cli knowledge qa --root ..
python -m eaods.cli knowledge graph --root ..
python -m eaods.cli knowledge memory-index --root ..
```

To include chunk text inside the manifest:

```bash
python -m eaods.cli knowledge chunks --root .. --include-text
```

Recommended sequence:

```bash
python -m eaods.cli knowledge inventory --root ..
python -m eaods.cli knowledge chunks --root ..
python -m eaods.cli knowledge stale --root ..
python -m eaods.cli knowledge qa --root ..
python -m eaods.cli knowledge graph --root ..
python -m eaods.cli knowledge memory-index --root ..
```
