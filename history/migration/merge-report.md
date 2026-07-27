---
title: EAODS Enterprise Edition Consolidation Report
document_id: EAODS-MIG-RPT-001
version: 1.0.0
status: generated
owner: Ivan Rozenblad
human_review_required: true
---

# Consolidation Report

## Decision

The latest Git-tracked `EAODS-v3` repository is the canonical baseline. Earlier upgrade and pull-request packages are preserved as provenance sources. Files were not allowed to overwrite newer canonical content automatically.

## Source reconciliation

| Source | File | Canonical relationship |
|---|---|---|
| `EAODS-v3-repository-upgrade` | `.DS_Store` | different historical revision; preserved, canonical retained |
| `EAODS-v3-repository-upgrade` | `.github/CODEOWNERS` | identical to canonical |
| `EAODS-v3-repository-upgrade` | `.github/ISSUE_TEMPLATE/bug_report.yml` | identical to canonical |
| `EAODS-v3-repository-upgrade` | `.github/ISSUE_TEMPLATE/config.yml` | identical to canonical |
| `EAODS-v3-repository-upgrade` | `.github/ISSUE_TEMPLATE/feature_request.yml` | identical to canonical |
| `EAODS-v3-repository-upgrade` | `.github/dependabot.yml` | identical to canonical |
| `EAODS-v3-repository-upgrade` | `.github/workflows/docs-quality.yml` | different historical revision; preserved, canonical retained |
| `EAODS-v3-repository-upgrade` | `.github/workflows/pages.yml` | different historical revision; preserved, canonical retained |
| `EAODS-v3-repository-upgrade` | `.github/workflows/release.yml` | different historical revision; preserved, canonical retained |
| `EAODS-v3-repository-upgrade` | `MIGRATION.md` | identical to canonical |
| `EAODS-v3-repository-upgrade` | `docs/.DS_Store` | historical-only; preserved under original sources |
| `EAODS-v3-repository-upgrade` | `docs/frameworks/.DS_Store` | historical-only; preserved under original sources |
| `EAODS-v3-repository-upgrade` | `docs/frameworks/EAODS-v17.3/volume-08-security-engineering.md` | identical to canonical |
| `EAODS-v3-repository-upgrade` | `docs/governance/CONTRIBUTING.md` | identical to canonical |
| `EAODS-v3-repository-upgrade` | `docs/governance/GOVERNANCE.md` | identical to canonical |
| `EAODS-v3-repository-upgrade` | `docs/governance/ROADMAP.md` | different historical revision; preserved, canonical retained |
| `EAODS-v3-repository-upgrade` | `docs/governance/SECURITY.md` | identical to canonical |
| `EAODS-v3-repository-upgrade` | `mkdocs.yml` | different historical revision; preserved, canonical retained |
| `EAODS-v3-repository-upgrade` | `requirements-docs.txt` | different historical revision; preserved, canonical retained |
| `EAODS-v3-repository-upgrade` | `scripts/validate_front_matter.py` | identical to canonical |
| `EAODS-v3-volume-09-pr` | `APPLY.md` | historical-only; preserved under original sources |
| `EAODS-v3-volume-09-pr` | `docs/frameworks/EAODS-v17.3/volume-09-infrastructure-resilience.md` | identical to canonical |
| `EAODS-v3-pr10-integration` | `PATCH.sh` | historical-only; preserved under original sources |
| `EAODS-v3-pr10-integration` | `architecture/adr/ADR-0002-eaods-enterprise-reference-operating-model.md` | identical to canonical |
| `EAODS-v3-pr10-integration` | `docs/governance/ROADMAP.md` | different historical revision; preserved, canonical retained |

## Excluded from canonical working tree

Runtime/build artifacts (`.venv`, generated `site`, caches, bytecode, and `.DS_Store`) are excluded from the clean canonical tree. They remain recoverable inside `history/source-archives/EAODS-v3-All-Folders-original.zip`.

## Human review gate

- [ ] Confirm the canonical baseline is the July 23, 2026 Git repository state.
- [ ] Confirm historical-only files remain provenance artifacts unless separately promoted.
- [ ] Confirm runtime/build artifacts should remain archive-only.
- [ ] Approve publication or GitHub migration of this Enterprise Edition.
