from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass
class FirewallFinding:
    category: str
    pattern: str
    severity: str


@dataclass
class FirewallResult:
    allowed: bool
    risk_score: int
    findings: list[FirewallFinding] = field(default_factory=list)


PATTERNS = {
    "instruction_override": [r"ignore (all )?(previous|prior) instructions", r"system prompt", r"developer message"],
    "tool_abuse": [r"\bcurl\b", r"\bbash\b", r"\bchmod\b", r"\bnc\b", r"reverse shell"],
    "secret_access": [r"print.*token", r"dump.*credential", r"read.*env", r"api[_-]?key"],
    "exfiltration": [r"webhook", r"upload.*http", r"dns lookup", r"send.*url"],
    "encoding": [r"base64", r"eval\(", r"decode\("],
    "destructive": [r"rm -rf", r"format disk", r"delete all"],
}


def scan_text(text: str) -> FirewallResult:
    findings: list[FirewallFinding] = []
    lower = text.lower()

    for category, patterns in PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, lower):
                severity = "high" if category in {"tool_abuse", "secret_access", "exfiltration", "destructive"} else "moderate"
                findings.append(FirewallFinding(category, pattern, severity))

    score = sum(25 if f.severity == "high" else 10 for f in findings)
    return FirewallResult(allowed=score < 25, risk_score=score, findings=findings)
