"""Legal/Compliance Research Agent.

Structures a legal or compliance inquiry into a reviewable intake: it classifies
the topic area, flags whether escalation to counsel is required, and produces a
*research checklist* of authority categories to verify — plus recommended next
steps and a mandatory disclaimer.

What this agent deliberately does NOT do (AGENTS.md §5, §9; governance rules):
- It does **not** provide legal advice or legal conclusions.
- It does **not** invent or assert statutes, case law, deadlines, or citations.
  The authority checklist names *categories to research and verify*, never a claim
  that a specific law applies to the user's facts.
- It does **not** send, file, or publish anything. Drafting only; humans act.

It is a drafting and triage aid whose output is meant to be handed to a qualified
attorney, not relied on directly.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from typing import Any

# Mandatory, non-removable disclaimer attached to every assessment.
DISCLAIMER = (
    "This is an automated, non-authoritative drafting and triage aid. It does not "
    "constitute legal advice, does not create an attorney-client relationship, and "
    "does not replace review by a qualified attorney licensed in the relevant "
    "jurisdiction. Verify every authority and deadline with primary sources."
)

# Topic classification: ordered keyword rules -> (topic_area, authority checklist).
# Checklist items are RESEARCH POINTERS ("verify whether ..."), never assertions
# that a given law governs the user's situation.
_TOPIC_RULES: list[tuple[str, frozenset[str], tuple[str, ...]]] = [
    (
        "data protection / privacy",
        frozenset({"privacy", "gdpr", "ccpa", "personal data", "pii", "data breach", "consent"}),
        (
            "Verify which data-protection regimes apply (e.g. GDPR, CCPA/CPRA, state laws) "
            "based on data subjects, processing location, and sector.",
            "Verify breach-notification obligations and their timelines for each applicable "
            "regime.",
            "Verify contractual data-processing obligations (DPAs, sub-processor terms).",
        ),
    ),
    (
        "contracts",
        frozenset({"contract", "agreement", "nda", "breach of contract", "clause", "terms"}),
        (
            "Verify the governing-law and jurisdiction clauses of the agreement.",
            "Verify notice, cure, and termination provisions and any applicable deadlines.",
            "Verify limitation-of-liability, indemnity, and dispute-resolution terms.",
        ),
    ),
    (
        "employment / labor",
        frozenset({"employment", "employee", "termination", "harassment", "wage", "labor"}),
        (
            "Verify applicable federal, state, and local employment statutes for the worksite.",
            "Verify any administrative filing prerequisites and their deadlines.",
            "Verify employee-handbook, contract, and collective-bargaining obligations.",
        ),
    ),
    (
        "intellectual property",
        frozenset({"copyright", "trademark", "patent", "infringement", "license", "trade secret"}),
        (
            "Verify which IP rights are implicated and their registration status.",
            "Verify ownership, assignment, and licensing chains.",
            "Verify any infringement-notice or filing deadlines.",
        ),
    ),
    (
        "regulatory / compliance",
        frozenset({"regulation", "compliance", "regulator", "audit", "sanction", "license"}),
        (
            "Verify which regulators and frameworks have jurisdiction over the activity.",
            "Verify reporting, registration, and recordkeeping obligations and timelines.",
            "Verify whether any safe harbors or exemptions apply.",
        ),
    ),
    (
        "litigation / dispute",
        frozenset({"lawsuit", "litigation", "subpoena", "court", "complaint", "dispute", "claim"}),
        (
            "Verify the controlling statute of limitations for each potential claim.",
            "Verify court rules, response deadlines, and service requirements.",
            "Verify preservation/litigation-hold obligations for relevant evidence.",
        ),
    ),
]

# Signals that the matter is time-sensitive or adversarial and needs a human now.
_ESCALATION_TERMS: frozenset[str] = frozenset(
    {
        "subpoena",
        "lawsuit",
        "litigation",
        "court",
        "deadline",
        "statute of limitations",
        "regulator",
        "breach",
        "sanction",
        "complaint",
        "summons",
        "injunction",
    }
)


@dataclass(frozen=True)
class LegalAssessment:
    """Structured, non-authoritative legal/compliance intake."""

    agent: str
    inquiry_summary: str
    topic_area: str
    jurisdiction: str
    authority_checklist: list[str]
    risk_flags: list[str]
    recommended_actions: list[str]
    escalation_required: bool
    disclaimer: str
    assumptions: list[str]


class LegalComplianceAgent:
    """Classify and structure a legal/compliance inquiry for attorney review."""

    def __init__(self, name: str = "Legal/Compliance Research Agent") -> None:
        self.name = name

    def assess_inquiry(self, text: str, *, jurisdiction: str | None = None) -> dict[str, Any]:
        """Return a structured, non-authoritative assessment of a legal inquiry.

        Args:
            text: Plain-language description of the legal/compliance question.
            jurisdiction: Optional jurisdiction hint. If omitted, the assessment
                records that jurisdiction is unspecified and must be confirmed.
        """
        if not isinstance(text, str):
            raise ValueError("text must be a string.")
        cleaned = text.strip()
        if not cleaned:
            raise ValueError("text cannot be empty.")

        lowered = cleaned.lower()
        topic_area, checklist = self._classify_topic(lowered)
        risk_flags = self._risk_flags(lowered)
        escalation_required = bool(risk_flags)

        result = LegalAssessment(
            agent=self.name,
            inquiry_summary=self._summarize(cleaned),
            topic_area=topic_area,
            jurisdiction=jurisdiction.strip()
            if jurisdiction and jurisdiction.strip()
            else "unspecified — confirm before relying on any authority",
            authority_checklist=list(checklist),
            risk_flags=risk_flags,
            recommended_actions=self._recommend_actions(topic_area, escalation_required),
            escalation_required=escalation_required,
            disclaimer=DISCLAIMER,
            assumptions=[
                "Assessment is based only on the supplied description.",
                "No primary legal sources were retrieved, verified, or cited.",
                "Topic classification is heuristic and may be incomplete.",
            ],
        )
        return asdict(result)

    @staticmethod
    def _classify_topic(lowered: str) -> tuple[str, tuple[str, ...]]:
        for topic_area, keywords, checklist in _TOPIC_RULES:
            if any(kw in lowered for kw in keywords):
                return topic_area, checklist
        return (
            "general / unclassified",
            (
                "Verify which area(s) of law the facts implicate.",
                "Verify the relevant jurisdiction(s) and governing authorities.",
                "Verify any applicable deadlines before taking action.",
            ),
        )

    @staticmethod
    def _risk_flags(lowered: str) -> list[str]:
        flags = [term for term in sorted(_ESCALATION_TERMS) if term in lowered]
        return flags

    @staticmethod
    def _summarize(text: str, *, limit: int = 200) -> str:
        collapsed = " ".join(text.split())
        return collapsed if len(collapsed) <= limit else collapsed[: limit - 1].rstrip() + "…"

    @staticmethod
    def _recommend_actions(topic_area: str, escalation_required: bool) -> list[str]:
        actions = [
            "Confirm the relevant jurisdiction(s) and effective dates.",
            "Research and verify each authority-checklist item against primary sources.",
            "Separate facts from assumptions before drafting any position.",
        ]
        if escalation_required:
            actions.insert(
                0,
                "Escalate to a qualified attorney promptly — time-sensitive or adversarial "
                "signals were detected.",
            )
        else:
            actions.append("Have a qualified attorney review before acting on the findings.")
        return actions


if __name__ == "__main__":
    agent = LegalComplianceAgent()
    sample = (
        "We received a subpoena requesting customer data and need to understand our "
        "privacy obligations and response deadline."
    )
    print(json.dumps(agent.assess_inquiry(sample), indent=2))
