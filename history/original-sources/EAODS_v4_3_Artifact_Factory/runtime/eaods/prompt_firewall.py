from __future__ import annotations

import re
from dataclasses import dataclass, asdict, field
from pathlib import Path
from typing import Any


@dataclass
class FirewallFinding:
    category: str
    pattern: str
    severity: str
    excerpt: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class FirewallResult:
    allowed: bool
    risk_score: int
    findings: list[FirewallFinding] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "allowed": self.allowed,
            "risk_score": self.risk_score,
            "findings": [f.to_dict() for f in self.findings],
        }


PATTERNS = {
    "instruction_override": [r"ignore (all )?(previous|prior) instructions", r"system prompt", r"developer message"],
    "tool_abuse": [r"\bcurl\b", r"\bbash\b", r"\bchmod\b", r"\bnc\b", r"reverse shell", r"powershell"],
    "secret_access": [r"print.*token", r"dump.*credential", r"read.*env", r"api[_-]?key", r"private[_-]?key"],
    "exfiltration": [r"webhook", r"upload.*http", r"dns lookup", r"send.*url", r"post.*credentials"],
    "encoding": [r"base64", r"eval\(", r"decode\(", r"fromhex"],
    "destructive": [r"rm -rf", r"format disk", r"delete all", r"wipe"],
}


def _excerpt(text: str, match: re.Match[str], window: int = 60) -> str:
    start = max(0, match.start() - window)
    end = min(len(text), match.end() + window)
    return text[start:end].replace("\n", " ")


def scan_text(text: str) -> FirewallResult:
    findings: list[FirewallFinding] = []
    lower = text.lower()

    for category, patterns in PATTERNS.items():
        for pattern in patterns:
            for match in re.finditer(pattern, lower):
                severity = "high" if category in {"tool_abuse", "secret_access", "exfiltration", "destructive"} else "moderate"
                findings.append(FirewallFinding(category, pattern, severity, _excerpt(text, match)))

    score = sum(25 if f.severity == "high" else 10 for f in findings)
    return FirewallResult(allowed=score < 25, risk_score=score, findings=findings)


def scan_file(path: str | Path) -> FirewallResult:
    text = Path(path).read_text(encoding="utf-8", errors="ignore")
    return scan_text(text)
