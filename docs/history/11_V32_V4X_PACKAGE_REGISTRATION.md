---
title: EAODS v3.2 and v4.x Package Registration
document_id: EAODS-HIST-PKG-001
version: 1.0.0
status: registered
owner: Ivan Rozenblad
governing_architecture: Volume 10
---

# EAODS v3.2 and v4.x Package Registration

This record registers seven recovered EAODS release packages supplied by the
Program Owner on 2026-07-26, plus one conversation-derived evidence excerpt.
Originals are preserved byte-exact under `history/source-archives/` (archives)
and `history/original-sources/` (extracted trees); per-file SHA-256 digests are
appended to `history/migration/checksums.sha256`.

## Registered packages

| Package | Files | Notable contents |
|---|---|---|
| `EAODS_v3_2_Enhanced_Operator_Edition` | 15 | v3.2 manifest, AGENTS.md, evaluation rubric, QA pipeline, security guardrails, competitive strategy, templates, docs-QA workflow |
| `EAODS_v4_Runtime_Alpha_Scaffold` | 28+ | First runtime scaffold: `runtime/eaods/` Python modules, agents registry, scorecard schema, v3.2.0-alpha and v4.0.0-alpha release notes |
| `EAODS_v4_1_Research_Innovation_Blueprint` | 28+ | Prompt-injection firewall design, agent constitution, AgentOps metrics dashboard spec, v4.1 release notes |
| `EAODS_v4_2_Runtime_Governance_Implementation` | 28+ | Runtime governance implementation, v4.2 release notes |
| `EAODS_v4_3_Artifact_Factory` | 28+ | Artifact factory line, v4.3 release notes |
| `EAODS_v4_4_GitHub_Publishing_Automation` | 28+ | Publishing automation, generated repository map and mkdocs config, v4.4 release notes |
| `EAODS_v4_5_RAG_Knowledge_Memory` | 28+ | RAG and knowledge-memory subsystem, v4.5 release notes |

Across the extracted trees, 110 Python runtime source files are preserved.

## Exception dispositions established by this registration

### EXC-007 — v3.2.0-alpha (closed)

Two findings resolve this exception under the closure rule:

1. **Bodies recovered.** The v3.2.0-alpha release notes
   (`Release-Notes/v3.2.0-alpha.md`, generated 2026-07-07T19:30Z) and the
   v3.2 Enhanced Operator Edition package contents are recovered and
   integrity-registered.
2. **No Git artifact ever existed.** Both GitHub repositories
   (`IRsoctierDT/EAODS`, `IRsoctierDT/EAODS-v3-Enterprise-Edition`) were
   checked on 2026-07-26: no tags and no releases exist in either. The
   v3.2.0-alpha release existed as package artifacts, not as a Git tag/commit.

### EXC-009 — v4.6 Executive Control Tower (pending-review)

A complete conversation-derived transmission of the v4.6-alpha specification is
retained at
`history/original-sources/conversation-evidence/EAODS_v4_6_ECT_full_transmission_2026-07-26.md`
(all sections, field tables, and the Human Review Gate; every item on the
document's own QA checklist is present). An earlier partial excerpt of the
same specification
(front matter, purpose, objectives, dashboard architecture, health rules, risk
queue, evidence formula, recommendations engine, workflow, case study, QA
checklist) is retained at
`history/original-sources/conversation-evidence/EAODS_v4_6_ECT_conversation_excerpt_2026-07-26.md`.
The original file bytes remain unrecovered, so the transmission is registered
as evidence rather than as the canonical artifact; it is sufficient for an
owner-approved bounded reconstruction, which has not yet been requested. An
unlabeled appended pipeline fragment (workflow-to-executive-approval) is
retained with it as candidate v4.7 evidence (EXC-010). The v4.6 dependency
chain (v4.1–v4.5) is now fully recovered, corroborating the excerpt's
`depends_on` declarations.

### Unchanged

EXC-001–004 (v17.0–17.2 corpora, v17.3 Volumes 1–7) and EXC-010 (v4.7
Governance Metrics Standard) remain open — none of the supplied packages
contain that material.

## Historical note

The recovered release notes document the intended lineage: v3 Enterprise
Edition handbooks merged with v3.2 control-plane enhancements into
v3.2.0-alpha, followed by the v4.x runtime line (scaffold → research blueprint
→ runtime governance → artifact factory → publishing automation → RAG/knowledge
memory) that the v4.6 Executive Control Tower was specified to sit above.
