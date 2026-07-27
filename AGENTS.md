# EAODS Agent Operating Manual

This is the operating manual for any AI coding agent (Claude Code, Codex, Gemini CLI,
Copilot, or other) working in this repository. It is vendor-neutral and version-controlled:
the rules here are repository policy, not suggestions.

## 1. What this repository is

EAODS Enterprise Edition is an **Enterprise Reference Operating Model** — a governed
documentation and architecture system, not an application codebase. The authoritative
statements of intent are:

- [docs/architecture/ENTERPRISE_OPERATING_MODEL.md](docs/architecture/ENTERPRISE_OPERATING_MODEL.md) — the operating model and four pillars (Govern, Design, Operate, Build).
- [architecture/adr/ADR-0002-eaods-enterprise-reference-operating-model.md](architecture/adr/ADR-0002-eaods-enterprise-reference-operating-model.md) — the governing architecture decision.
- [docs/governance/ROADMAP.md](docs/governance/ROADMAP.md) — the **single source of truth** for what is done and what is next. The root `ROADMAP.md` is only a pointer to it.
- [docs/history/](docs/history/) — the Unified Historical Corpus; its exception queue
  (`05_EXCEPTION_QUEUE.md`) is the authoritative work-list for the historical migration.

## 2. Ground rules

1. **Verify state fresh, every session.** Never act on a prior session's summary of
   repository state. Read the roadmap, list branches and PRs, and inspect files before
   selecting work. Stale-memory reports have previously described blockers and pending
   work that did not exist.
2. **One increment per branch/PR.** Select the single highest-value open item; do not
   bundle unrelated changes.
3. **Never synthesize historical content.** Corpus rules apply: missing historical
   artifacts are recovered, formally superseded, or excepted — never invented from
   titles. Exceptions close only under the closure rule in `05_EXCEPTION_QUEUE.md`.
4. **Register identifiers before use.** Object-ID prefixes and terms are governed by
   STD-0001 (`standards/vocabulary/`). New prefixes must be registered there first;
   the traceability validator enforces this.
5. **No secrets.** Never commit `.env`, keys, certificates, or credential material.
   CI fails the build if secret-like files are present.

## 3. Increment workflow

1. Inspect: `git fetch`, read `docs/governance/ROADMAP.md`, check open PRs and branches.
2. Select the next open roadmap item (or exception-queue item for the migration line).
3. Branch from up-to-date `main`: `docs/<topic>`, `feature/<capability>`, `fix/<issue>`,
   or `chore/<maintenance>`.
4. Implement the complete increment, including nav (`mkdocs.yml`), `CHANGELOG.md`, and
   roadmap checkbox updates that belong to it.
5. Run all quality gates locally (section 4). Fix failures before pushing.
6. Push the branch and open a PR to `main`. The PR body must state business and
   architecture impact, affected EAODS volumes/artifacts, and validation results.
7. Stop at human gates (section 6). Otherwise, merge only after the required `validate`
   check is green.

## 4. Quality gates

Run from the repository root (a `.venv` with the toolchain exists; install with
`pip install -r requirements-docs.txt` if needed):

```bash
.venv/bin/mkdocs build --strict
.venv/bin/python scripts/validate_front_matter.py
.venv/bin/python scripts/validate_traceability.py
```

All three must pass with no warnings. These same gates run in CI
(`.github/workflows/docs-quality.yml`) as the required `validate` status check on `main`.

## 5. Branch, commit, and PR conventions

- `main` is protected: required `validate` check, strict up-to-date requirement, linear
  history, no force pushes, no direct commits. All changes land by PR.
- Use Conventional Commits (`docs:`, `feat:`, `fix:`, `chore:`), scoped where useful,
  e.g. `docs(history): …`, `docs(governance): …`.
- Portal pages need YAML front matter; framework volumes under `docs/frameworks/` have
  a required field set enforced by `scripts/validate_front_matter.py`.
- New portal pages must be added to `mkdocs.yml` nav.

## 6. Human approval gates — stop and ask

Do **not** proceed autonomously on:

- Closing a historical exception without recovery evidence that satisfies the closure rule.
- Approving supersession of a historical artifact (owner/authority/effective-date decision).
- Publishing releases or tags.
- Changing branch protection, CI required checks, or repository settings.
- Deleting content or history.

## 7. Repository map

| Path | Purpose |
|---|---|
| `docs/` | MkDocs portal content (frameworks, standards, patterns, runbooks, threat models, history, governance) |
| `architecture/adr/` | Architecture decision records |
| `standards/vocabulary/` | Machine-readable ID and terminology registries (STD-0001) |
| `standards/graph/` | Traceability knowledge graph (STD-0002) |
| `history/migration/` | Recovered-source evidence: checksums, inventory, chronology |
| `scripts/` | CI validators |
| `site/` | Build output — never edit or commit changes here |
