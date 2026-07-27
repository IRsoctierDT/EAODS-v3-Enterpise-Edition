#!/usr/bin/env bash
set -euo pipefail

if [[ ! -d .git ]]; then
  echo "Run this script from the root of the EAODS-v3 repository." >&2
  exit 1
fi

git checkout main
git pull --ff-only
git checkout -b fix/complete-volume-09-integration

rm -f APPLY.md
mkdir -p architecture/adr docs/governance
cp "/mnt/data/EAODS-v3-pr10-integration/architecture/adr/ADR-0002-eaods-enterprise-reference-operating-model.md"    architecture/adr/ADR-0002-eaods-enterprise-reference-operating-model.md
cp "/mnt/data/EAODS-v3-pr10-integration/docs/governance/ROADMAP.md" docs/governance/ROADMAP.md

python scripts/validate_front_matter.py
mkdocs build --strict

git add -A
git commit -m "fix(docs): complete Volume 9 integration and formalize EAODS direction"
git push -u origin fix/complete-volume-09-integration

gh pr create   --base main   --head fix/complete-volume-09-integration   --title "fix(docs): complete Volume 9 integration and formalize EAODS direction"   --body "Removes the temporary APPLY.md helper, marks Volume 9 complete, expands the active roadmap, and adds ADR-0002 establishing EAODS as an Enterprise Reference Operating Model guided by the Volume 10 vision."
