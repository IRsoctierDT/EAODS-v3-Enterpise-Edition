---
title: EAODS Unified Migration Manifest
document_id: EAODS-MIG-MAN-001
version: 1.2.0-reconstructed
status: active
reconstructed: true
governing_architecture: Volume 10
---

# EAODS Unified Migration Manifest

| ID | Scope | Target | Mandatory controls | Acceptance gate | State |
|---|---|---|---|---|---|
| MIG-001 | v17.0 | Govern/Design controls and threat models | Provenance, owners, canonical IDs | No orphaned requirements | blocked-source |
| MIG-002 | v17.1 | Architecture patterns and diagrams | Name/ID crosswalk, interfaces, rationale | EARB review for conflicts | blocked-source |
| MIG-003 | v17.2 | Runbooks and governance procedures | Separate policy, decision rights, and executable procedures | Runbook and traceability validation | blocked-source |
| MIG-004 | Volumes 1–7 | `docs/frameworks/EAODS-v17.3/volume-01…07` | Accepted reconstructions (EAODS-HIST-V173-001); no synthesized bodies | Every unit migrated, superseded, or excepted | migrated 2026-08-03 |
| MIG-014 | Volume 12 | `docs/frameworks/EAODS-v17.3/volume-12-metrics-kpis-kris.md` | Accepted reconstruction (EAODS-HIST-V173-001) | Front matter, nav, and traceability gates pass | migrated 2026-08-03 |
| MIG-005 | Volume 8 | Canonical volume registry | Front matter and graph metadata | CI and link validation | path-unresolved |
| MIG-006 | Volume 9 | Resilience/HA/DR volume | Registration, cross-links, control coverage | Traceability validation | substantially-complete |
| MIG-007 | Volume 10 | Governing EPOC/SRE architecture | North-star marker and controlled change process | No silent contradiction | governing |
| MIG-008 | Volume 11 | Control catalog and compliance framework | Stable control IDs and standards links | Terminology/control validation | canonical-validation |
| MIG-009 | Ten agent precursors | Agent handbooks/specifications | Exact filename preservation; evidence-based mapping only | All ten recovered, superseded, or excepted | source-recovered |
| MIG-010 | v3 and v3.2.0-alpha packages | Current repository artifact map | Version provenance and checksums | No package artifact orphaned | source-recovered |
| MIG-011 | v4.6/v4.7/Orchestrator drafts | Current governance/operations artifacts | Reconstruction notice and scope approval | Original recovered or reconstruction approved | v4.7-outstanding |
| MIG-012 | Proposed Volumes 11–13 | Historical roadmap crosswalk | Proposal/canonical distinction | Canonical Volume 11 remains unchanged | partially-mapped |
| MIG-013 | Hardening/commercial backlog | Authoritative roadmap | Evidence-backed implementation status | Each item classified | pending-reconciliation |

## Unit migration procedure

1. Acquire bytes or record the source as evidence-limited.
2. Calculate checksum and preserve original filename.
3. Register title, version, date, owner, source authority, and evidence grade.
4. Normalize front matter in a derivative—not by overwriting the original.
5. Map deprecated terms and identifiers.
6. Link controls, architecture patterns, runbooks, threats, owners, and evidence.
7. Validate against Volume 10, Volume 11, ADR-0002, and repository schemas.
8. Obtain required review.
9. Record final disposition and close or update the related exception.
