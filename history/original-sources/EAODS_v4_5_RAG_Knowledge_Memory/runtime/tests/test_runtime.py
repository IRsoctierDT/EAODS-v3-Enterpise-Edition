from pathlib import Path

from eaods.registry import AgentRegistry
from eaods.security import classify_action
from eaods.artifacts import generate_handbook
from eaods.scorer import score_markdown


def test_registry_loads_agents():
    registry = AgentRegistry("agents.yaml")
    assert "orchestrator" in registry.agents
    assert registry.route("SOC 2 compliance readiness") == "legal_compliance"


def test_security_classification():
    result = classify_action("deploy and publish production changes")
    assert result["tier"] >= 4
    assert result["human_approval_required"] is True


def test_generate_and_score_handbook(tmp_path):
    path = generate_handbook("orchestrator", tmp_path, "agents.yaml")
    assert path.exists()
    result = score_markdown(path, "scorecard.schema.json")
    assert result["score"] >= 70
