---
title: EAODS v3 Enterprise Edition
document_id: EAODS-ENT-ROOT-001
version: 1.0.0-consolidated
status: review-required
owner: Ivan Rozenblad
governing_architecture: Volume 10
---

# EAODS v3 Enterprise Edition

This directory consolidates the latest Git-tracked EAODS-v3 repository with all supplied historical upgrade and integration packages. The clean working tree retains canonical source and documentation; all original supplied files remain preserved through the original collection archive and extracted provenance packages.

## Review entry points

- `history/migration/chronology.md`
- `history/migration/inventory.csv`
- `history/migration/duplicate-groups.json`
- `history/migration/merge-report.md`
- `history/source-archives/` (committed package evidence; the 80 MB / 40 MB clone snapshots `EAODS-v3-All-Folders-original.zip` and `EAODS-v3-local-collection.zip` are retained outside the repository with SHA-256 digests registered in `history/migration/checksums.sha256`)
- `history/original-sources/` (extracted originals, including the 29-unit Enterprise Edition corpus — see `10_ENTERPRISE_EDITION_SOURCE_UNITS.md`)

No historical revision was silently promoted over the latest canonical repository state.
