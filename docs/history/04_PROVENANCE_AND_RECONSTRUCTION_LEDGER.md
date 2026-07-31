---
title: EAODS Provenance and Reconstruction Ledger
document_id: EAODS-PROV-LED-001
version: 1.2.0-reconstructed
status: active
reconstructed: true
---

# EAODS Provenance and Reconstruction Ledger

| ID | Assertion | Basis | Confidence | Limitation |
|---|---|---:|---:|---|
| REC-001 | Release lineage spans v17.0–v17.3 | Canonical project record | 100% | Historical corpora not all present |
| REC-002 | v17.3 comprises Volumes 1–12 | Roadmap/project evidence; accepted transmissions (EAODS-HIST-V173-001) | 100% | Volumes 1–7 and 12 reconstructions accepted 2026-07-30; canonical repository filenames not yet assigned |
| REC-003 | Volume 10 is the architectural north star | Explicit user and project decision | 100% | Must remain encoded in canonical governance |
| REC-004 | Volume 10 is v17.3.9-alpha and extends Volumes 1–9 | Recovered project record | 100% | Full artifact is outside current workspace |
| REC-005 | Volume 11 is v17.3.10-alpha and extends Volumes 1–10 | Recovered project record | 100% | Full artifact is outside current workspace |
| REC-006 | Ten named Python sources were requested as YAML-front-mattered Markdown conversions | Direct July 6 transcript | 100% | Bodies and conversions recovered 2026-07-26 (EAODS-HIST-ENT-001; EXC-005 closed) |
| REC-007 | Early Enterprise Edition contained 29 files | Recovered archive (EAODS-HIST-ENT-001) | 100% | Recovered 2026-07-26; 29 of 29 units reconciled (EXC-006 closed) |
| REC-008 | v3.2.0-alpha included release/map/roadmap/registry/workflow artifacts | Recovered packages (EAODS-HIST-PKG-001) | 100% | Bodies recovered 2026-07-26; Git tag confirmed never created (EXC-007 closed) |
| REC-009 | July 6 Volume 10 plan included SRE, NOC/SOC/AIOC, incident command, telemetry, reliability, AI assistance, and human gates | Direct transcript | 100% | Planning scope is not proof of final coverage |
| REC-010 | July 6 Volumes 11–13 taxonomy conflicts with later canonical Volume 11 | Direct transcript plus later record | 100% | Requires explicit supersession, not renumbering |
| REC-011 | PR #10 was intended to complete Volume 9 integration and establish ADR-0002 | Direct transcript and later project record | 100% | Transcript includes obsolete failed attempt |
| REC-012 | v4.6, v4.7, and Orchestrator Handbook existed as drafts | Dated conversation/email records | 90% | v4.6 evidence-bounded reconstruction accepted 2026-07-26 (EAODS-HIST-V46-001; EXC-009 closed); Orchestrator 2026-07-06 unit accepted as standing record (EXC-008 closed); v4.7 body still absent (EXC-010 open) |
| REC-013 | PR #19 made `docs/governance/ROADMAP.md` authoritative | Verified project record | 100% | Repository path must be used as current authority |

## Conflict register

| ID | Conflict | Resolution |
|---|---|---|
| CON-001 | “Volume 11 — Enterprise AI Governance Runtime” versus canonical Volume 11 control catalog | Preserve the former as superseded planning taxonomy; do not renumber canonical content |
| CON-002 | Historical intent versus current implementation status | Mark intent as planned until repository evidence verifies completion |
| CON-003 | Reconstructed artifact versus recovered original | Preserve both; label reconstruction and link the original by checksum |

## Reconstruction declaration

This ledger records what is known, how it is known, and what remains unknown. A confidence score applies only to the stated assertion; it does not elevate an unavailable document body into recovered content.
