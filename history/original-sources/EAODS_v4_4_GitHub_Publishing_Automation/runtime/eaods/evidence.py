from __future__ import annotations

from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import hashlib
import uuid

from .io import load_yaml, write_yaml


@dataclass
class EvidenceRecord:
    title: str
    evidence_type: str
    description: str = ""
    source_path: str = ""
    source_url: str = ""
    sensitivity: str = "internal"
    related_workflow: str = ""
    related_artifact: str = ""
    evidence_id: str = field(default_factory=lambda: f"EV-{uuid.uuid4().hex[:8].upper()}")
    collected_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    sha256: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def hash_file(path: str | Path) -> str:
    p = Path(path)
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def add_evidence(ledger_path: str | Path, record: EvidenceRecord) -> dict[str, Any]:
    path = Path(ledger_path)
    if record.source_path and Path(record.source_path).exists():
        record.sha256 = hash_file(record.source_path)

    if path.exists():
        data = load_yaml(path)
    else:
        data = {"evidence": []}

    data.setdefault("evidence", []).append(record.to_dict())
    write_yaml(path, data)
    return record.to_dict()


def list_evidence(ledger_path: str | Path) -> list[dict[str, Any]]:
    path = Path(ledger_path)
    if not path.exists():
        return []
    data = load_yaml(path)
    records = data.get("evidence", [])
    if not isinstance(records, list):
        return []
    return records


def evidence_summary(ledger_path: str | Path) -> dict[str, Any]:
    records = list_evidence(ledger_path)
    by_type: dict[str, int] = {}
    by_sensitivity: dict[str, int] = {}
    for r in records:
        by_type[r.get("evidence_type", "unknown")] = by_type.get(r.get("evidence_type", "unknown"), 0) + 1
        by_sensitivity[r.get("sensitivity", "unknown")] = by_sensitivity.get(r.get("sensitivity", "unknown"), 0) + 1

    return {
        "total_records": len(records),
        "by_type": by_type,
        "by_sensitivity": by_sensitivity,
    }
