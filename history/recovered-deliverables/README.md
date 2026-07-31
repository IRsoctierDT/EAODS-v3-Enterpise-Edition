# Recovered Deliverable Archive

Fifteen original EAODS deliverable ZIPs, recovered on 2026-07-30 from a
ChatGPT-export attachment-recovery pass and preserved here verbatim. These are
the artifacts the project's conversation record describes being delivered
between 2026-07-06 and 2026-07-21; several contain work that never landed in
this repository.

| Delivered | Artifact | Contents |
|---|---|---|
| 2026-07-06 | `agent_markdown_files.zip` | The original 10 agent files reformatted to Markdown — the request that started EAODS |
| 2026-07-06 | `Enterprise_Agent_Documentation_v2.zip` | First documentation deliverable (10 files), pre-charter |
| 2026-07-06 | `EAODS_v3_Enterprise_Edition.zip` | First chartered EAODS deliverable — 29 files, 10 agent handbooks |
| 2026-07-07 | `EAODS_v3_2_Enhanced_Operator_Edition.zip` | AGENTS.md, evaluation rubric, scorecard schema, security guardrails, mkdocs.yml, docs-QA workflow |
| 2026-07-07 | `EAODS_v3_2_Alpha_Merged_Release.zip` | Merged release: Repository_Map.md, agents.yaml, PR/issue templates, v4 roadmap |
| 2026-07-07 | `EAODS_v4_Runtime_Alpha_Scaffold.zip` | The v4.0-alpha runtime (39 files): `runtime/eaods/` CLI, registry, workflow, security, artifacts, scorer, release modules, tests, CI |
| 2026-07-07 | `EAODS_v4_1_Research_Innovation_Blueprint.zip` | Policy engine spec, evidence ledger spec, prompt-injection firewall design, agent_constitution.yaml |
| 2026-07-07 | `EAODS_v4_2_Runtime_Governance_Implementation.zip` | Runtime governance layer (policy checks, evidence ledger) |
| 2026-07-07 | `EAODS_v4_3_Artifact_Factory.zip` | Artifact Factory |
| 2026-07-07 | `EAODS_v4_4_GitHub_Publishing_Automation.zip` | GitHub & publishing automation |
| 2026-07-07 | `EAODS_v4_5_RAG_Knowledge_Memory.zip` | RAG & knowledge memory layer |
| 2026-07-21 | `EAODS-v3-github-ready.zip` | Repository bootstrap scaffold |
| 2026-07-21 | `EAODS-v3-repository-upgrade.zip` | Repository governance/hardening package |
| 2026-07-21 | `EAODS-v3-volume-09-pr.zip` | Volume 9 PR package (landed as PR #9) |
| 2026-07-21 | `EAODS-v3-pr10-integration.zip` | PR #10 integration package, including ADR-0002 — the PR that never opened |

## Notes

- **The v4 runtime series (v4.0–v4.5) is the headline recovery**: the
  `runtime/eaods/*.py` control plane and its governance specs predate this
  repository and were otherwise unpreserved.
- `EAODS-v3-pr10-integration.zip` contains the intended PR #10 payload
  (ADR-0002 "EAODS as an Enterprise Reference Operating Model", roadmap
  update, `APPLY.md` removal) and can be applied if that work resumes.
- Documents inside these ZIPs carry generator-stamped front matter labeled
  `classification: "Internal / Portfolio / Commercialization Candidate"`;
  the label is historical metadata from the generation pipeline, preserved
  as-is for archival fidelity.
- Files are archival: do not edit the ZIPs; extract and adapt into `docs/`
  or `frameworks/` through the normal PR workflow instead.
