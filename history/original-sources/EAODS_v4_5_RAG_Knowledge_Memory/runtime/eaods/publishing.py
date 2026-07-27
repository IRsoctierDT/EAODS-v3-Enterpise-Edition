from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import json
import re
import shutil
from zipfile import ZipFile

from .io import write_text, write_json, load_yaml
from .scorer import score_markdown


SENSITIVE_DIR_MARKERS = {
    "Source-Code-Appendices",
    "private",
    "internal",
    ".venv",
    "__pycache__",
}

SENSITIVE_FILE_PATTERNS = [
    "evidence_ledger.yaml",
    "approval_log.yaml",
    "decision_log.yaml",
]


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "item"


def markdown_title(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return path.stem.replace("_", " ").title()

    fm_match = re.search(r'^---\n(.*?)\n---', text, re.S)
    if fm_match:
        for line in fm_match.group(1).splitlines():
            if line.lower().startswith("title:"):
                return line.split(":", 1)[1].strip().strip('"').strip("'")

    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("_", " ").title()


def is_sensitive(path: Path) -> bool:
    parts = set(path.parts)
    if parts.intersection(SENSITIVE_DIR_MARKERS):
        return True
    lower = str(path).lower()
    if any(marker.lower() in lower for marker in SENSITIVE_DIR_MARKERS):
        return True
    if any(pattern.lower() in path.name.lower() for pattern in SENSITIVE_FILE_PATTERNS):
        return True
    text = ""
    if path.suffix.lower() in {".md", ".yaml", ".yml", ".txt", ".json", ".py"}:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore").lower()
        except Exception:
            text = ""
    secret_patterns = ["api_key=", "password=", "secret=", "token=", "private_key"]
    return any(pattern in text for pattern in secret_patterns)


def generate_repository_map(root: str | Path = ".", output: str | Path = "Repository_Map.md") -> Path:
    root = Path(root)
    files = sorted([p for p in root.rglob("*") if p.is_file() and ".git" not in p.parts])
    md = f"""---
title: "EAODS Repository Map"
version: "4.4.0-alpha"
generated: "{datetime.now(timezone.utc).isoformat()}"
---

# EAODS Repository Map

| Path | Type | Public Safe? |
|---|---|---|
"""
    for p in files:
        rel = p.relative_to(root)
        kind = p.suffix.lower().lstrip(".") or "file"
        md += f"| `{rel}` | {kind} | {'No' if is_sensitive(p) else 'Yes'} |\n"
    out = root / output
    write_text(out, md)
    return out


def generate_mkdocs_nav(root: str | Path = ".", output: str | Path = "mkdocs.generated.yml") -> Path:
    root = Path(root)
    markdown_files = sorted([
        p for p in root.rglob("*.md")
        if ".git" not in p.parts and "runtime" not in p.parts and p.name.lower() != "repository_map.md"
    ])
    nav = "site_name: Enterprise AI Operator Documentation Suite\n"
    nav += "site_description: EAODS generated documentation site\n"
    nav += "theme:\n  name: material\n"
    nav += "markdown_extensions:\n  - tables\n  - fenced_code\n  - admonition\n  - toc:\n      permalink: true\n"
    nav += "nav:\n"
    nav += "  - Home: README.md\n"
    grouped: dict[str, list[Path]] = {}
    for p in markdown_files:
        rel = p.relative_to(root)
        top = rel.parts[0] if len(rel.parts) > 1 else "Root"
        grouped.setdefault(top, []).append(p)

    for group, paths in sorted(grouped.items()):
        if group == "Root":
            continue
        nav += f"  - {group}:\n"
        for p in paths[:50]:
            rel = p.relative_to(root)
            title = markdown_title(p).replace('"', "'")
            nav += f"      - \"{title}\": \"{rel}\"\n"
    out = root / output
    write_text(out, nav)
    return out


def generate_changelog(root: str | Path = ".", output: str | Path = "CHANGELOG.md") -> Path:
    root = Path(root)
    release_notes = sorted((root / "Release-Notes").glob("*.md")) if (root / "Release-Notes").exists() else []
    md = "# Changelog\n\n"
    md += "All notable EAODS changes are summarized here.\n\n"
    if not release_notes:
        md += "No release notes found.\n"
    for note in release_notes:
        title = markdown_title(note)
        md += f"## {title}\n\n"
        text = note.read_text(encoding="utf-8", errors="ignore")
        lines = [line for line in text.splitlines() if line.startswith("- ")]
        if lines:
            for line in lines[:20]:
                md += f"{line}\n"
        else:
            md += f"- See `{note.relative_to(root)}`.\n"
        md += "\n"
    out = root / output
    write_text(out, md)
    return out


def batch_score(root: str | Path = ".", schema: str | Path = "runtime/scorecard.schema.json", output: str | Path = "runtime/dashboards/batch_scores.json") -> Path:
    root = Path(root)
    schema_path = root / schema
    results: list[dict[str, Any]] = []
    for p in root.rglob("*.md"):
        if ".git" in p.parts:
            continue
        try:
            result = score_markdown(p, schema_path)
            result["relative_path"] = str(p.relative_to(root))
            results.append(result)
        except Exception as exc:
            results.append({"relative_path": str(p.relative_to(root)), "error": str(exc)})
    out = root / output
    write_json(out, {"generated": datetime.now(timezone.utc).isoformat(), "results": results})
    return out


def generate_issue(title: str, body: str, output_dir: str | Path = "runtime/publishing/issues") -> Path:
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    md = f"""---
title: "{title}"
type: "github_issue"
generated: "{datetime.now(timezone.utc).isoformat()}"
---

# {title}

## Summary

{body}

## Acceptance Criteria

- [ ] Scope is clear.
- [ ] Artifact owner identified.
- [ ] QA completed.
- [ ] Human review gate applied where required.

## Labels

- documentation
- eaods
"""
    path = out / f"{slugify(title)}_issue.md"
    write_text(path, md)
    return path


def generate_pr(title: str, summary: str, output_dir: str | Path = "runtime/publishing/pull_requests") -> Path:
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    md = f"""# {title}

## Summary

{summary}

## Type of Change

- [ ] Documentation expansion
- [ ] Runtime update
- [ ] Governance update
- [ ] Security update
- [ ] Publishing update

## QA Checklist

- [ ] YAML front matter preserved.
- [ ] No secrets or private data added.
- [ ] Scope is clear.
- [ ] Human approval gates included where needed.
- [ ] Tests or scoring completed.
- [ ] Release notes updated.

## Risk Level

- [ ] Low
- [ ] Moderate
- [ ] High
- [ ] Critical
"""
    path = out / f"{slugify(title)}_pull_request.md"
    write_text(path, md)
    return path


def create_release_candidate(
    root: str | Path = ".",
    version: str = "v4.4.0-alpha",
    output_dir: str | Path = "runtime/artifacts/release_candidates",
) -> Path:
    root = Path(root)
    out = root / output_dir
    out.mkdir(parents=True, exist_ok=True)
    manifest = {
        "version": version,
        "generated": datetime.now(timezone.utc).isoformat(),
        "included_files": [],
        "review_required": [],
    }

    for p in root.rglob("*"):
        if not p.is_file() or ".git" in p.parts or out in p.parents:
            continue
        rel = p.relative_to(root)
        if "runtime/artifacts/release_candidates" in str(rel):
            continue
        manifest["included_files"].append(str(rel))
        if is_sensitive(p):
            manifest["review_required"].append(str(rel))

    manifest_path = out / f"{version}_manifest.json"
    write_json(manifest_path, manifest)

    zip_path = out / f"{version}_release_candidate.zip"
    with ZipFile(zip_path, "w") as z:
        for rel in manifest["included_files"]:
            p = root / rel
            if p.exists():
                z.write(p, rel)
        z.write(manifest_path, manifest_path.relative_to(root))
    return zip_path


def create_public_private_bundles(
    root: str | Path = ".",
    version: str = "v4.4.0-alpha",
    output_dir: str | Path = "runtime/artifacts",
) -> dict[str, str]:
    root = Path(root)
    out = root / output_dir
    out.mkdir(parents=True, exist_ok=True)

    public_zip = out / "public_bundle" / f"{version}_public_bundle.zip"
    private_zip = out / "private_bundle" / f"{version}_private_bundle.zip"
    public_zip.parent.mkdir(parents=True, exist_ok=True)
    private_zip.parent.mkdir(parents=True, exist_ok=True)

    with ZipFile(public_zip, "w") as pub, ZipFile(private_zip, "w") as priv:
        for p in root.rglob("*"):
            if not p.is_file() or ".git" in p.parts:
                continue
            rel = p.relative_to(root)
            if "runtime/artifacts/public_bundle" in str(rel) or "runtime/artifacts/private_bundle" in str(rel):
                continue
            if is_sensitive(p):
                priv.write(p, rel)
            else:
                pub.write(p, rel)
                priv.write(p, rel)

    return {"public_bundle": str(public_zip), "private_bundle": str(private_zip)}
