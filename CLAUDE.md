# CLAUDE.md

@AGENTS.md

The canonical operating manual for this repository is `AGENTS.md` (imported above).
Claude Code–specific notes:

- Use the local toolchain at `.venv/bin/` for all quality gates before pushing.
- Use `gh` for PR creation and merge; merge only after the required `validate` check
  is green, and never bypass a human approval gate listed in AGENTS.md §6.
- Begin every session by re-verifying repository state (`git fetch`, roadmap, open
  PRs) — do not trust prior-session summaries.
