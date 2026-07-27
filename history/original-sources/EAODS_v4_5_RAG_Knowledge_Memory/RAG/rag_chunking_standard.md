---
title: "EAODS RAG Chunking Standard"
version: "4.5.0-alpha"
owner: "Ivan Rozenblad"
generated: "2026-07-07T19:47:01.380516+00:00"
classification: "Internal / Portfolio / Commercialization Candidate"
description: "Standard for chunking EAODS documents into retrieval-ready knowledge units."
---

# EAODS RAG Chunking Standard

## Chunking Objectives

Chunks should be:

- source-linked,
- stable,
- non-overly-large,
- semantically meaningful,
- hashable,
- safe to retrieve,
- tied to document metadata.

## Recommended Chunk Size

- Target: 500–1,200 words
- Minimum: 100 words
- Maximum: 1,500 words

## Required Chunk Metadata

```yaml
chunk_id:
document_id:
source_path:
title:
section_heading:
chunk_index:
sha256:
word_count:
classification:
topics:
created_at:
```

## Retrieval Rule

Agents should prefer canonical, current, high-reliability chunks over stale, duplicate, or low-confidence chunks.
