from __future__ import annotations

from pathlib import Path
from typing import Any

from .io import load_yaml


class AgentRegistry:
    def __init__(self, path: str | Path = "agents.yaml") -> None:
        self.path = Path(path)
        self.data = load_yaml(self.path)
        self.agents = {a["id"]: a for a in self.data.get("agents", []) if "id" in a}

    def list_agents(self) -> list[dict[str, Any]]:
        return list(self.agents.values())

    def get(self, agent_id: str) -> dict[str, Any]:
        try:
            return self.agents[agent_id]
        except KeyError as exc:
            available = ", ".join(sorted(self.agents))
            raise KeyError(f"Unknown agent '{agent_id}'. Available agents: {available}") from exc

    def route(self, request_type: str) -> str:
        lowered = request_type.lower()
        rules = {
            "compliance": "legal_compliance",
            "audit": "legal_compliance",
            "soc": "legal_compliance",
            "incident": "incident_report",
            "threat": "threat_intelligence",
            "ioc": "threat_intelligence",
            "detection": "detection_matcher",
            "proposal": "business_proposal",
            "sow": "business_proposal",
            "portfolio": "portfolio_documentation",
            "readme": "portfolio_documentation",
            "knowledge": "knowledge_base",
            "curation": "knowledge_curator",
            "executive": "executive_assistant",
            "schedule": "executive_assistant",
        }
        for key, agent_id in rules.items():
            if key in lowered:
                return agent_id
        return "orchestrator"
