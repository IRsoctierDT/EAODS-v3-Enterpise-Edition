from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import uuid

from .io import write_yaml


VALID_STATES = [
    "intake",
    "scoped",
    "planned",
    "assigned",
    "executing",
    "blocked",
    "qa_review",
    "human_review",
    "approved",
    "published",
    "archived",
    "improved",
]


@dataclass
class WorkflowState:
    title: str
    goal: str
    owner: str = "Ivan Rozenblad"
    workflow_id: str = field(default_factory=lambda: f"EAODS-WF-{uuid.uuid4().hex[:8].upper()}")
    version: str = "4.0.0-alpha"
    status: str = "intake"
    classification: str = "Internal / Portfolio / Commercialization Candidate"
    audience: str = ""
    sensitivity: str = "internal"
    required_agents: list[str] = field(default_factory=list)
    inputs: list[str] = field(default_factory=list)
    outputs: list[str] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)
    risks: list[dict[str, Any]] = field(default_factory=list)
    approval_gates: list[str] = field(default_factory=list)
    qa_checks: list[str] = field(default_factory=list)
    deliverables: list[str] = field(default_factory=list)
    archive_location: str = ""
    next_improvement: str = ""
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def transition(self, new_state: str) -> None:
        if new_state not in VALID_STATES:
            raise ValueError(f"Invalid state: {new_state}. Valid states: {', '.join(VALID_STATES)}")
        self.status = new_state

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def save(self, path: str | Path) -> None:
        write_yaml(path, self.to_dict())
