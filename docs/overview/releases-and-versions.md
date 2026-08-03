---
title: EAODS Releases and Version Navigation
document_id: EAODS-PUB-VER-001
version: 1.0.0
status: proposed
owner: Engineering Governance
review_gate: Engineering Governance and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - docs/governance/standards-lifecycle.md
  - docs/history/00_MASTER_CORPUS.md
  - .github/workflows/release.yml
---

# EAODS Releases and Version Navigation

## 1. Purpose

This page explains how EAODS is versioned, how to reach a specific version of
the material, and what each release carries. It distinguishes three version
axes that are easy to conflate — repository releases, framework line versions,
and document versions.

## 2. The three version axes

| Axis | What it versions | Where it lives | Example |
|---|---|---|---|
| **Repository release** | A published snapshot of this repository | Git tags and GitHub Releases | `v1.0.0` |
| **Framework line** | The authored EAODS framework generation | Volume front matter and the corpus register | `v17.3` |
| **Document version** | An individual standard or volume | `version:` in each document's front matter | `17.3.9-alpha` |

Conflating these is the single most common source of confusion in the
historical record: the repository was named for the *suite* identity (`v3`)
while the framework line had advanced to `v17.3`. The distinction above is
normative going forward.

## 3. Framework line lineage

The authored lineage recovered and registered in the corpus:

| Line | Scope | Status |
|---|---|---|
| v3 – v3.2 | Enterprise documentation suite and operator edition | Historical, superseded |
| v4.0 – v4.5 | Runtime scaffold, governance, artifact factory, publishing, RAG | Historical, superseded |
| v4.6 – v4.28 | Control tower, governance metrics, and the security-standards series | Historical, superseded |
| v5.0 – v8.7 | Knowledge graph, control/evidence automation, AI security operations, configuration governance | Historical, superseded |
| v9 – v16 | Information model, continuity, AEOS, implementation playbooks, operating model, sovereign AI (incl. the Enterprise Digital Constitution) | Historical, superseded |
| v17.0 – v17.2 | Domain 03 cyber defence, reference architecture, operations manual | Historical, superseded |
| **v17.3** | **Domain 03 Reference Implementation & Platform Engineering Guide — Volumes 1–12** | **Current governed baseline** |

Superseded lines are preserved in full under `history/` with provenance and
checksums. They are historical evidence: they inform the current model but do
not govern it. Where a superseded document conflicts with the current
baseline, the current baseline prevails (ADR-0002).

## 4. Reaching a specific version

- **Current documentation** — this site always renders `main`, which carries
  the current governed baseline.
- **A published snapshot** — see the repository's Releases page. Each release
  attaches a source archive, an SPDX SBOM, and the framework PDF library.
- **A historical framework line** — browse `history/original-sources/` in the
  repository. Every unit carries a provenance header recording its source and
  extraction date.
- **A specific document version** — check the `version:` field in that
  document's front matter.

## 5. Version selector

This site currently publishes a single governed baseline, so no version
selector is rendered: a selector offering one choice would be decoration
rather than navigation. Once a second baseline is published, versioned
deployment is introduced and the selector becomes meaningful. Until then,
historical material is reached through section 4.

This is a deliberate choice, recorded here so its absence is not mistaken for
an oversight.

## 6. Release contents

Each tagged release publishes:

| Artifact | Description |
|---|---|
| `EAODS-<tag>.tar.gz` | Repository source archive, excluding build and environment directories |
| `EAODS-<tag>-sbom.spdx.json` | SPDX software bill of materials |
| `EAODS-<tag>-pdf-library.tar.gz` | PDF renderings of the v17.3 framework volumes |
| Release notes | Generated from the commit and pull-request history |

## 7. Versioning rules

1. Repository releases follow semantic versioning.
2. A framework line version is never renumbered once published; superseded
   lines retain their numbers.
3. Document versions advance under the standards lifecycle; a material change
   requires review before publication.
4. Identifiers minted under STD-0001 are never reused or renumbered across
   versions.

## 8. Sources and traceability

| Source (repo-relative) | Contribution |
|---|---|
| `docs/history/00_MASTER_CORPUS.md` | The reconstructed v17.x lineage and the suite-versus-framework version distinction in section 2 |
| `docs/history/16_COMPLETE_CORPUS_RECOVERY_REGISTRATION.md` | The registered v6.7–v16 and v17.0–v17.2 lines listed in section 3 |
| `docs/history/15_LONGGAP_AND_ORIGINAL_REPO_REGISTRATION.md` | The v4.6–v4.17 band and the continuous v4.x lineage in section 3 |
| `.github/workflows/release.yml` | The release artifact set in section 6 |
| `architecture/adr/ADR-0002-eaods-enterprise-reference-operating-model.md` | The precedence rule that current baseline governs over historical material |
| `docs/standards/canonical-terminology-and-identifiers.md` | Identifier stability rule cited in section 7 |
