from __future__ import annotations

from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from pathlib import Path
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

    def to_dict(self):
        return asdict(self)


def add_evidence(ledger_path: str | Path, record: EvidenceRecord) -> None:
    path = Path(ledger_path)
    if path.exists():
        data = load_yaml(path)
    else:
        data = {"evidence": []}
    data.setdefault("evidence", []).append(record.to_dict())
    write_yaml(path, data)
