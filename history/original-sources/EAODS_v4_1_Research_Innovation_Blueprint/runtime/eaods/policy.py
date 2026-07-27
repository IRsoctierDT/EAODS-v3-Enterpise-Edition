from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class PolicyDecision:
    decision: str
    reason: str
    required_actions: list[str] = field(default_factory=list)


def evaluate_action(action: dict[str, Any]) -> PolicyDecision:
    risk_tier = int(action.get("risk_tier", 1))
    approval_status = bool(action.get("approval_status", False))
    evidence = action.get("evidence", [])
    text = str(action).lower()

    if any(k in text for k in ["api_key", "password=", "secret=", "token="]):
        return PolicyDecision("deny", "Potential secret exposure detected.", ["Remove secrets", "Rotate exposed credential if real"])

    if risk_tier >= 5:
        return PolicyDecision("require_qualified_review", "Tier 5 regulated or high-impact decision.", ["Qualified human review"])

    if risk_tier >= 2 and not approval_status:
        return PolicyDecision("require_approval", "Risk tier requires human approval.", ["Obtain approval"])

    if action.get("requires_evidence") and not evidence:
        return PolicyDecision("require_evidence", "Required evidence is missing.", ["Attach evidence record"])

    return PolicyDecision("allow_with_logging", "Action may proceed with logging.", ["Record action in workflow history"])
