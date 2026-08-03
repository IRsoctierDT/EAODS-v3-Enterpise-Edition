"""Validate internal documentation links and mkdocs navigation targets.

Checks:
1. Every relative Markdown link and image target in docs/ and architecture/
   resolves to a file that exists.
2. Every mkdocs.yml nav entry points at a file that exists under docs/.
3. Every docs/ Markdown file is reachable from the mkdocs nav (orphan report).

Historical evidence under history/ and docs/history/original-sources is
excluded: those files are preserved verbatim and are never rewritten to
satisfy repository conventions.

Exit code 0 on success, 1 with a failure report otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

DOC_ROOTS = (Path("docs"), Path("architecture"))
EXCLUDED_PARTS = {"original-sources", "source-archives", "recovered-deliverables"}
LINK = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)]+)\)")
IMAGE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
EXTERNAL = re.compile(r"^(https?:|mailto:|#)")


def is_excluded(path: Path) -> bool:
    return bool(EXCLUDED_PARTS.intersection(path.parts))


def markdown_files() -> list[Path]:
    files: list[Path] = []
    for root in DOC_ROOTS:
        if root.exists():
            files.extend(p for p in root.rglob("*.md") if not is_excluded(p))
    return sorted(files)


def nav_targets(node, out: list[str]) -> None:
    if isinstance(node, dict):
        for value in node.values():
            nav_targets(value, out)
    elif isinstance(node, list):
        for item in node:
            nav_targets(item, out)
    elif isinstance(node, str):
        out.append(node)


def main() -> int:
    failures: list[str] = []
    checked = 0

    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for pattern in (LINK, IMAGE):
            for target in pattern.findall(text):
                target = target.split(" ")[0].strip()
                if not target or EXTERNAL.match(target):
                    continue
                checked += 1
                resolved = (path.parent / target.split("#")[0]).resolve()
                if not resolved.exists():
                    failures.append(f"{path}: broken link -> {target}")

    mkdocs = Path("mkdocs.yml")
    nav_files: list[str] = []
    if mkdocs.exists():
        # mkdocs.yml uses python-specific tags; parse permissively.
        raw = yaml.safe_load(
            re.sub(r"!!python/name:[^\s]+", "null", mkdocs.read_text(encoding="utf-8"))
        )
        nav_targets(raw.get("nav", []), nav_files)
        for target in nav_files:
            if EXTERNAL.match(target):
                continue
            checked += 1
            if not (Path("docs") / target).exists():
                failures.append(f"mkdocs.yml: nav target missing -> {target}")

    navigable = {(Path("docs") / t).resolve() for t in nav_files}
    orphans = [
        p for p in markdown_files()
        if p.parts[0] == "docs" and p.resolve() not in navigable
        and "history" not in p.parts
    ]

    if failures:
        print("Link validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Link validation passed: {checked} internal targets resolved.")
    if orphans:
        print(f"Note: {len(orphans)} documents are not in the mkdocs nav:")
        for orphan in orphans:
            print(f"- {orphan}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
