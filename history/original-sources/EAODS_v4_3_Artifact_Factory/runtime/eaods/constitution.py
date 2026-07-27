from __future__ import annotations

from pathlib import Path
from typing import Any

from .io import load_yaml, write_text


def compile_constitution(source_path: str | Path, output_dir: str | Path = ".") -> list[Path]:
    source = load_yaml(source_path)
    constitution = source.get("constitution", {})
    principles = constitution.get("principles", [])
    prohibited = constitution.get("prohibited", [])
    requirements = constitution.get("output_requirements", [])
    targets = source.get("targets", ["AGENTS.md"])

    body = "# EAODS Agent Constitution\n\n"
    body += "## Principles\n\n"
    for p in principles:
        body += f"- {p}\n"
    body += "\n## Prohibited Defaults\n\n"
    for p in prohibited:
        body += f"- {p}\n"
    body += "\n## Output Requirements\n\n"
    for r in requirements:
        body += f"- {r}\n"
    body += "\n## Human Approval Rule\n\nHigh-impact actions require human approval before execution or publication.\n"

    output_root = Path(output_dir)
    written: list[Path] = []
    for target in targets:
        path = output_root / target
        write_text(path, body)
        written.append(path)
    return written
