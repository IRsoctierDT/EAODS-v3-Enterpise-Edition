from dataclasses import asdict, dataclass
from typing import Any, Literal

Confidence = Literal["low", "medium", "high"]


@dataclass(frozen=True)
class ThreatIntelResult:
    indicator: str
    indicator_type: str
    risk_level: str
    confidence: Confidence
    explanation: str
    recommended_actions: list[str]


class ThreatIntelAgent:
    def analyze_indicator(self, indicator: str) -> dict[str, Any]:
        cleaned = indicator.strip()

        if not cleaned:
            raise ValueError("indicator cannot be empty")

        if self._is_private_ip(cleaned):
            return asdict(
                ThreatIntelResult(
                    indicator=cleaned,
                    indicator_type="private_ip",
                    risk_level="context-dependent",
                    confidence="high",
                    explanation="Private IP addresses are internal and require local network context.",
                    recommended_actions=[
                        "Correlate with asset inventory.",
                        "Check authentication and firewall logs.",
                        "Determine whether the host behavior is expected.",
                    ],
                )
            )

        if self._is_ipv4(cleaned):
            return asdict(
                ThreatIntelResult(
                    indicator=cleaned,
                    indicator_type="public_ip",
                    risk_level="unknown",
                    confidence="medium",
                    explanation="Public IP requires external reputation enrichment before classification.",
                    recommended_actions=[
                        "Check threat intelligence feeds.",
                        "Review geolocation and ASN.",
                        "Correlate with IDS, firewall, and authentication events.",
                    ],
                )
            )

        if "." in cleaned:
            return asdict(
                ThreatIntelResult(
                    indicator=cleaned,
                    indicator_type="domain",
                    risk_level="unknown",
                    confidence="medium",
                    explanation="Domain requires DNS, WHOIS, and reputation review.",
                    recommended_actions=[
                        "Check DNS records.",
                        "Review domain age and registrar.",
                        "Search logs for related DNS queries.",
                    ],
                )
            )

        return asdict(
            ThreatIntelResult(
                indicator=cleaned,
                indicator_type="unknown",
                risk_level="unknown",
                confidence="low",
                explanation="Indicator type could not be confidently classified.",
                recommended_actions=[
                    "Review original evidence.",
                    "Add parsing rules if this indicator appears repeatedly.",
                ],
            )
        )

    @staticmethod
    def _is_ipv4(value: str) -> bool:
        parts = value.split(".")
        return len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)

    @classmethod
    def _is_private_ip(cls, value: str) -> bool:
        if not cls._is_ipv4(value):
            return False

        first, second, *_ = [int(part) for part in value.split(".")]

        return (
            first == 10 or (first == 172 and 16 <= second <= 31) or (first == 192 and second == 168)
        )


if __name__ == "__main__":
    agent = ThreatIntelAgent()
    print(agent.analyze_indicator("192.168.1.50"))
