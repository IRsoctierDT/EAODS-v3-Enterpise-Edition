---
title: EAODS v3 Enterprise Edition Source-Unit Registration
document_id: EAODS-HIST-ENT-001
version: 1.0.0
status: registered
owner: Ivan Rozenblad
governing_architecture: Volume 10
---

# EAODS v3 Enterprise Edition Source-Unit Registration

This record registers the recovered 29-file EAODS v3 Enterprise Edition source
corpus. The originals were supplied by the Program Owner on 2026-07-26 as the
archive `EAODS_v3_Enterprise_Edition.zip` (consolidated on 2026-07-06 from the
owner's local EAODS-v3 folders). Bytes are preserved unmodified.

## Integrity registration

- Archive: `history/source-archives/EAODS_v3_Enterprise_Edition.zip`
  (SHA-256 `e40a6e6e31bedeaccd491c581a2668f470511e2a9f0e6571f0ff443fa525f942`, 29 files, all units generated 2026-07-06T21:02Z).
- Extracted originals: `history/original-sources/EAODS_v3_Enterprise_Edition/`
  (exact filenames preserved, including ` copy.py` suffixes).
- Per-file SHA-256 digests: appended to `history/migration/checksums.sha256`.

## Unit reconciliation (29 of 29)

| Unit class | Count | Files |
|---|---|---|
| Foundation standard | 1 | `Volume-01-Enterprise-Standards/EAODS_v3_Foundation_Standard.md` |
| System architecture | 1 | `Volume-02-System-Architecture/EAODS_v3_System_Architecture.md` |
| Agent handbooks (Markdown conversions) | 10 | `orchestrator`, `portfolio-documentation`, `business-proposal`, `detection-matcher`, `incident-report`, `threat-intelligence`, `legal-compliance`, `executive-assistant`, `knowledge-base`, `knowledge-curator` (`*_handbook_v3.md`, Volumes 02–08) |
| Python agent sources | 10 | `Source-Code-Appendices/*.py` (`business_proposal`, `detection_matcher`, `executive_assistant`, `incident_report`, `knowledge_base`, `knowledge_curator`, `legal_compliance`, `orchestrator`, `portfolio_documentation`, `threat_intel`) |
| Governance templates | 5 | `Policies/Policy_Template.md`, `SOPs/SOP_Template.md`, `Templates/Control_Matrix_Template.md`, `Templates/Risk_Register_Template.md`, `Case-Studies/Enterprise_Case_Study_Framework.md` |
| Reference registry | 1 | `Reference-Library/Authoritative_Reference_Registry.md` |
| Collection README | 1 | `README.md` |

## Corpus dispositions established by this recovery

- SRC-010 (ten Python agent sources): bodies recovered; grade A.
- SRC-011 (ten Markdown agent conversions): bodies recovered; grade A.
- SRC-012 (EAODS v3 Enterprise Edition, 29-file composition): recovered in full; grade A.
- SRC-018 (Enterprise Orchestrator Agent Handbook, dated 2026-07-07): a candidate
  predecessor generated 2026-07-06 is recovered
  (`Volume-02-System-Architecture/orchestrator-agent_handbook_v3.md`); owner
  confirmation is required before it can stand in for the 2026-07-07 draft.

The Enterprise Edition `Volume-01` through `Volume-08` directories are an agent-handbook
taxonomy distinct from the v17.3 framework Volumes 1–7; this recovery does not close
that exception.

## Archive retention note

The consolidation snapshots `EAODS-v3-All-Folders-original.zip` (80 MB) and
`EAODS-v3-local-collection.zip` (40 MB) are repository-clone snapshots containing no
unique historical units beyond Git history and build artifacts. They remain retained
outside the repository by the owner; their SHA-256 digests are registered in
`history/migration/checksums.sha256`. The unique package evidence they accompanied is
committed under `history/source-archives/` and `history/original-sources/`.
