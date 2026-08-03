---
title: EAODS v4.6–v4.17 Band Recovery & Original Repository Registration
document_id: EAODS-HIST-GAP-001
version: 1.1.0
status: registered
owner: Ivan Rozenblad
governing_architecture: Volume 10
---

# EAODS v4.6–v4.17 Band Recovery & Original Repository Registration

This record registers the 2026-07-30 recovery batch supplied by the Program
Owner from local working directories and downloads. A 642-file SHA-256 sweep
found 601 exact duplicates of already-registered material; the genuinely new
recoveries are registered here.

## 1. The v4.6–v4.17 "long gap" transmission

`EAODS-v4.6-v17LONGGAP.md` (whole-file SHA-256 `310e240b…`) was found in the
owner's extracted `EAODS-v3-repository-upgrade` working directory at
`docs/frameworks/EAODS-v4.6-v17/` — a path absent from the registered zip of
the same package. It contains **twelve complete standards, v4.6 through
v4.17**, closing the previously unevidenced band between the v4.x runtime
packages and the v4.17.1–v4.28 suite transmissions. Units were split verbatim
under `…/units/v4.6-v4.21-longgap/` (manifest + SHA-256 digests registered):

| Version | Title |
|---|---|
| v4.6 | Executive Control Tower Specification *(content-distinct variant — see §2)* |
| v4.7 | Enterprise Governance & Operational Metrics Standard *(EXC-010)* |
| v4.8 | Enterprise Orchestration & Agent Lifecycle Standard |
| v4.9 | Enterprise Change Management & Configuration Governance Standard |
| v4.10 | Enterprise Reference Architecture Standard |
| v4.11 | Enterprise Data Governance & Information Lifecycle Standard |
| v4.12 | Enterprise Trust, Identity & Authorization Architecture Standard *(see §3)* |
| v4.13 | Enterprise Observability, Telemetry & Operational Assurance Standard |
| v4.14 | Enterprise Resilience, Continuity & Disaster Recovery Standard |
| v4.15 | Enterprise Security Operations & Incident Response Standard *(EXC-014)* |
| v4.16 | Cybersecurity Core Domain Alignment Matrix *(EXC-014)* |
| v4.17 | Enterprise Threat & Vulnerability Management Standard *(EXC-014)* |

Verification: all twelve units reviewed independently — complete,
untruncated, uncontaminated. The v4.15 and v4.16 units carry trailing
conversational appendices from the source stream (the owner's five-domain
taxonomy outline and build-planning prose, including one embedded chat-turn
fragment); these are preserved verbatim as transmission context, consistent
with prior registrations.

The v4.17 unit ends by proposing **v4.18–v4.21 under earlier titles**
(Penetration Testing & Authorized Assessment; Secure Configuration &
Hardening; Compliance Framework Mapping; AI-Assisted Cyber Risk
Prioritization) and handing off to v4.17.1. Those four titles were a
**proposed roadmap only** — no bodies existed under them; the delivered
v4.18–v4.21 standards in EAODS-HIST-AIO-001 carry the superseding titles.
The lineage v4.0→v4.5 → v4.6→v4.17 → v4.17.1→v4.28 → v5.x→v8.7 is now
continuous with recovered bodies at every step.

## 2. v4.6 variant disposition

The LONGGAP v4.6 and the accepted conversation transmission
(EAODS-HIST-V46-001, EXC-009) are **content-distinct variants** (~180
divergent lines each way; differing section structures). Per the v8.0
variant precedent, **both are preserved; no silent selection is made.**
Whether the LONGGAP file variant supersedes the accepted reconstruction under
the EXC-009 supersession clause is a Program Owner decision, recorded as
open question **Q-001** below.

## 3. v4.12 title note

EXC-014 cited a v4.12 "Cybersecurity Domain Taxonomy" from recovered
`extends:` chains. The recovered v4.12 body is titled "Enterprise Trust,
Identity & Authorization Architecture Standard" — matching the dated
2026-07-16 project record. The cited "Cybersecurity Domain Taxonomy" title
remains unmatched by any recovered body: either a mis-citation in a later
draft's `extends:` chain or a distinct unrecovered draft. Recorded as open
question **Q-002**; EXC-014's v4.12 component closes on the recovered body,
with the unmatched citation noted.

## 4. Original EAODS-v3 repository history

The owner's original `EAODS-v3` working clone was recovered intact,
containing **fourteen local branches whose commits do not exist in this
repository's history** (this repository was seeded from a snapshot). The
complete history is preserved as a git bundle in the owner's private archive
(`EAODS-v3-original-repo.bundle`, all refs, bundle verified), together with
the stash `On fix/complete-volume-09-integration: temporary PR10 recovery`
(an `APPLY.md` removal patch). Notable recovered facts:

- `fix/complete-volume-09-integration` exists **with commit `932b27d`** — the
  branch the 2026-07-22 record described as commit-less; the PR #10 story is
  now fully evidenced end to end (its intended payload was separately
  recovered as `EAODS-v3-pr10-integration.zip`).
- `fix/integrate-v17.3-volume-09` head `78e6a404` matches the recorded PR #9
  merge commit.
- Branch heads for volume-10-platform-operations, volume-11-control-catalog,
  traceability-knowledge-graph, and the docs/* series document the original
  authoring sequence.

## 5. Clone snapshot archives recovered

`EAODS-v3-All-Folders-original.zip` (83.6 MB) and
`EAODS-v3-local-collection.zip` (41.8 MB) — the archives that
09_ENTERPRISE_EDITION_RECONCILIATION records as retained outside the
repository — were recovered inside an early Enterprise-Edition snapshot zip
and **verified byte-exact against the digests already registered in
`history/migration/checksums.sha256`**. They remain outside this repository
per the standing retention decision; recovered copies are preserved in the
owner's private archive. The outer snapshot zip (126.5 MB, SHA-256
`e3bf2c8f…`) and the original Unified Historical Corpus package
(`EAODS_Unified_Historical_Corpus_1.0.0-reconstructed.tar.gz`) are likewise
preserved there.

## Exception dispositions established by this registration

- **EXC-010 (v4.7)** → **closed**: the complete v4.7 standard is recovered as
  a file artifact and integrity-registered (closure rule: original recovered
  and integrity-registered).
- **EXC-014 (v4.12, v4.15, v4.16, v4.17)** → **closed**: all four bodies
  recovered and integrity-registered; the v4.12 title discrepancy is recorded
  as Q-002 and does not reopen the exception.
- **EXC-009 (v4.6)** → remains closed; variant question recorded as Q-001.

## Open questions — resolved by Program Owner decision, 2026-07-30

| ID | Question | Decision |
|---|---|---|
| Q-001 | Does the LONGGAP v4.6 file variant supersede the accepted conversation reconstruction? | **Both retained as parallel variants** (the v8.0 precedent). The LONGGAP copy is a content-distinct draft, not the original bytes of the accepted transmission, so the EXC-009 supersession clause is not triggered; no silent selection is made. |
| Q-002 | Is the cited v4.12 "Cybersecurity Domain Taxonomy" a mis-citation or a distinct draft? | **Ruled a probable mis-citation.** The recovered v4.12 body matches the dated 2026-07-16 project record; no body, citation chain, or roadmap entry supports a distinct "Domain Taxonomy" draft. No new exception; reopens only if a body surfaces. |
