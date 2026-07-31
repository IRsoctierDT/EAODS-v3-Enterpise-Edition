---
title: EAODS Canonical Historical Mapping Matrix
document_id: EAODS-MIG-MAP-001
version: 1.2.0-reconstructed
status: active
reconstructed: true
---

# EAODS Canonical Historical Mapping Matrix

| Historical source/concept | Canonical destination | Pillar | Mapping rule | Conflict disposition |
|---|---|---|---|---|
| v17.0 cyber defense/resilience | Control catalog and threat-model library | Govern / Design | Decompose into controls, threats, relationships | Volume 10 constraints and canonical IDs prevail |
| v17.1 reference architecture | Architecture pattern library | Design | Preserve rationale and interfaces | Material conflict requires EARB/ADR |
| v17.2 operations/executive playbook | Runbooks and governance procedures | Operate / Govern | Separate procedure from policy and authority | Current operating model prevails |
| v17.3 implementation guidance | Reference implementations | Build / Operate | Link implementation to controls and evidence | Implementation cannot redefine architecture |
| Volumes 1–7 | Unit-specific volume destinations | All | Migrate recovered text only | Missing text remains exceptioned |
| Volume 9 | Resilience, HA, and DR | Design / Operate | Preserve integration and verify traceability | Volume 10 governs operations |
| Volume 10 | EPOC, SRE, operational engineering | Operate | Governing interpretation | Deviation requires ADR/EARB |
| Volume 11 | Control catalog and compliance | Govern / Design | Preserve canonical control IDs | Canonical taxonomy prevails |
| Python agent sources | Agent handbooks and `agents.yaml` | Build / Operate | Map only with content evidence | Filename alone is insufficient |
| Enterprise Orchestrator Handbook | Agent governance and trust boundaries | Govern / Operate / Build | Map duties to roles, controls, and human gates | Least privilege and human review mandatory |
| Executive Control Tower v4.6 | Decision rights and executive observability | Govern / Operate | Metadata now; content only when recovered | Do not infer metrics or controls |
| Metrics Standard v4.7 | Evidence and metrics schemas | Govern / Operate | Require owners, source authority, reproducibility | Reject unowned/unverifiable measures |
| July 6 Volume 10 plan | Volume 10 coverage/provenance | Operate / Govern | Coverage checklist, not canonical substitute | Approved Volume 10 text prevails |
| Proposed Volume 11 AI Governance Runtime | Future AI-governance runtime artifacts | Govern / Build | Historical proposed title only | Cannot overwrite canonical Volume 11 |
| Proposed Volumes 12–13 | Future roadmap concepts | Govern / Design / Operate | Preserve without assigning current status | No inferred numbering/completion |

## Required deprecated-name crosswalk

Each recovered source must add a row containing:

| Original name/ID | Canonical name/ID | Relationship | Authority | Effective date | Review state |
|---|---|---|---|---|---|
| Ten Python agent sources (SRC-010, filenames per EAODS-HIST-ART-001) | EAODS v3 Enterprise Edition agent handbooks (`history/original-sources/EAODS_v3_Enterprise_Edition/Volume-02…08`) | replaced-by | EAODS-HIST-ENT-001 | 2026-07-26 | registered |
| Ten Markdown agent conversions (SRC-011) | EAODS v3 Enterprise Edition agent handbooks | merged-into | EAODS-HIST-ENT-001 | 2026-07-26 | registered |
| EAODS v3 Enterprise Edition, 29-file package (SRC-012) | Current governed repository model (ADR-0002); archival tree under `history/original-sources/EAODS_v3_Enterprise_Edition/` | superseded-by | EAODS-HIST-ENT-001 | 2026-07-26 | registered |
| EAODS v3.2.0-alpha packages (SRC-013) | Current repository governance assets (AGENTS.md, workflows, templates); archival trees under `history/original-sources/` | superseded-by | EAODS-HIST-PKG-001 | 2026-07-26 | registered |
| EAODS v4.x runtime packages v4.0–v4.5, 110 Python sources (SRC-025) | Current governed repository model (ADR-0002); archival trees under `history/original-sources/EAODS_v4_*` | superseded-by | EAODS-HIST-PKG-001 | 2026-07-26 | registered |
| Transmission `EOADS-v17.1-v28.md` (SRC-028; label is owner shorthand for v4.17.1–v4.28) | Unit files `…/EAODS_AI_Operator_Suite_transmissions/units/v4.17.1-v4.28/` | split-into | EAODS-HIST-AIO-001 | 2026-07-27 | registered |
| Transmission `EAODS-v5-alpha-v6.7-alpha.md` (SRC-029) | Unit files `…/units/v5.0-v6.6/` | split-into | EAODS-HIST-AIO-001 | 2026-07-27 | registered |
| Transmission `EAODS-v7-alpha-v8.5-alpha.md` (SRC-030) | Unit files `…/units/v7.0-v8.3/` | split-into | EAODS-HIST-AIO-001 | 2026-07-27 | registered |
| v17.3 Volume 1–7 transmissions (SRC-005; EAODS-HIST-V173-001) | Future `docs/frameworks/EAODS-v17.3/volume-01…07` canonical files | implements | EAODS-HIST-V173-001; Program Owner acceptance 2026-07-30 | 2026-07-30 | accepted |
| v17.3 Volume 12 transmission (SRC-031; EAODS-HIST-V173-001) | Future `docs/frameworks/EAODS-v17.3/volume-12` canonical file | implements | EAODS-HIST-V173-001; Program Owner acceptance 2026-07-30 | 2026-07-30 | accepted |
| “Volume 11 — Enterprise AI Governance Runtime” (July 6 planning taxonomy; CON-001, EXC-012) | v17.3 Volume 11 — Enterprise Reference Control Catalog, Engineering Standards & Architecture Compliance (`17.3.10-alpha`) | superseded-by | 00_MASTER_CORPUS §5; CON-001 | 2026-07-21 | submitted-for-approval (EXC-012, Architecture Owner) |

Permitted relationships are `renamed-to`, `replaced-by`, `split-into`, `merged-into`, `implements`, `governed-by`, and `superseded-by`.
