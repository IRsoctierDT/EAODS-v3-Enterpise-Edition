from __future__ import annotations


RISK_TIERS = {
    0: "Read-only documentation review",
    1: "Create or edit non-sensitive documentation",
    2: "Modify code, config, tests, or CI files",
    3: "Run local commands, install dependencies, or change repo state",
    4: "Access secrets, deploy, delete, publish, or contact external parties",
    5: "Legal, financial, medical, or regulated decision",
}


def classify_action(action: str) -> dict[str, object]:
    text = action.lower()
    tier = 1

    if any(k in text for k in ["read", "review", "summarize"]):
        tier = 0
    if any(k in text for k in ["edit code", "modify code", "config", "ci", "test"]):
        tier = max(tier, 2)
    if any(k in text for k in ["run command", "install", "execute", "shell", "terminal"]):
        tier = max(tier, 3)
    if any(k in text for k in ["deploy", "delete", "secret", "token", "publish", "send email"]):
        tier = max(tier, 4)
    if any(k in text for k in ["legal", "compliance conclusion", "medical", "financial commitment", "regulated"]):
        tier = max(tier, 5)

    return {
        "tier": tier,
        "description": RISK_TIERS[tier],
        "human_approval_required": tier >= 2,
    }
