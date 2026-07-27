---
title: "EAODS v4.5 RAG and Knowledge Memory"
version: "4.5.0-alpha"
owner: "Ivan Rozenblad"
generated: "2026-07-07T19:47:01.380516+00:00"
classification: "Internal / Portfolio / Commercialization Candidate"
---

# EAODS v4.5 RAG and Knowledge Memory

This release implements the first knowledge memory layer.

## New Commands

```bash
python -m eaods.cli knowledge inventory --root ..
python -m eaods.cli knowledge chunks --root ..
python -m eaods.cli knowledge stale --root ..
python -m eaods.cli knowledge qa --root ..
python -m eaods.cli knowledge graph --root ..
python -m eaods.cli knowledge memory-index --root ..
```

## New Runtime Module

- `runtime/eaods/knowledge.py`

## New Knowledge Outputs

- document registry
- chunk manifest
- staleness report
- retrieval QA set
- knowledge graph export
- memory index

## Strategic Improvement

EAODS now has a durable, structured knowledge memory layer for RAG, retrieval QA, and source governance.
