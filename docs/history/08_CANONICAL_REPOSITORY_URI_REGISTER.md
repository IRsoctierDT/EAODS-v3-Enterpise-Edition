---
title: EAODS Canonical Repository URI Register
document_id: EAODS-HIST-URI-001
version: 1.0.0
status: proposed
owner: Architecture Owner
review_gate: Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related_exception: EXC-011
---

# EAODS Canonical Repository URI Register

## Purpose

This register resolves canonical repository locations required for historical migration, architecture governance, and cross-artifact traceability.

## Canonical locations

| Artifact | Canonical repository path | Authority |
|---|---|---|
| ADR-0002 | `architecture/adr/ADR-0002-eaods-enterprise-reference-operating-model.md` | Accepted architecture decision |
| Canonical terminology and identifiers | `docs/standards/canonical-terminology-and-identifiers.md` | STD-0001 |
| Cross-artifact traceability | `docs/standards/cross-artifact-traceability.md` | STD-0002 |
| Authoritative roadmap | `docs/governance/ROADMAP.md` | Repository governance |
| Volume 10 North Star Charter | `docs/history/06_VOLUME_10_NORTH_STAR_CHARTER.md` | Historical migration governance |

## Human review gate

The Architecture Owner must verify each path exists and confirm that no historical artifact silently replaces a canonical repository artifact.

## QA requirements

- Front matter validation passes.
- Traceability validation passes.
- MkDocs strict build passes.
- All registered paths resolve.
- Program Owner approves closure of `EXC-011`.
