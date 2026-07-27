"""Executive Assistant Agent.

Supports planning and prioritization: it turns a list of tasks/notes (or freeform
text) into a prioritized plan with a suggested focus, surfaced blockers and open
questions, and a decision-log entry template.

Scope & guardrails (AGENTS.md §5):
- **Plans and structures only.** It never sends messages, schedules events, or takes
  any external action — those remain human decisions.
- **No fabrication.** Priorities are derived from explicit signals in the text; it
  does not invent tasks, dates, or decisions. The decision-log template is blank for
  the human to complete.
- Deterministic and network-free.
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from typing import Any, Literal

Priority = Literal["high", "medium", "low"]

# Urgency signals -> priority. Checked high-first.
_HIGH_TERMS: frozenset[str] = frozenset(
    {"urgent", "asap", "critical", "deadline", "today", "now", "blocker", "blocked", "immediately"}
)
_LOW_TERMS: frozenset[str] = frozenset(
    {"someday", "later", "eventually", "nice to have", "optional", "backlog", "low priority"}
)
_BLOCKER_TERMS: frozenset[str] = frozenset({"blocker", "blocked", "waiting on", "depends on"})

_PRIORITY_RANK: dict[str, int] = {"high": 0, "medium": 1, "low": 2}

_SPLIT = re.compile(r"[\n;]+")


@dataclass(frozen=True)
class PlanItem:
    """A single planned task with a derived priority."""

    task: str
    priority: Priority
    is_blocker: bool


@dataclass(frozen=True)
class ExecutivePlan:
    """A structured, non-actioned plan for human review."""

    agent: str
    items: list[dict[str, Any]]
    prioritized_order: list[str]
    suggested_focus: list[str]
    blockers: list[str]
    open_questions: list[str]
    decision_log_template: dict[str, str]
    assumptions: list[str]


class ExecutiveAssistantAgent:
    """Prioritize tasks/notes into a reviewable plan (no external actions)."""

    def __init__(self, name: str = "Executive Assistant Agent") -> None:
        self.name = name

    def plan(self, items: str | list[str], *, focus_count: int = 3) -> dict[str, Any]:
        """Return a prioritized plan from tasks/notes.

        Args:
            items: A freeform string (split on newlines/semicolons) or a list of
                task strings.
            focus_count: How many top-priority items to suggest as the focus.
        """
        tasks = self._normalize_items(items)
        if not tasks:
            raise ValueError("no tasks found in input.")

        plan_items = [self._classify(t) for t in tasks]
        # Stable sort by priority preserves input order within a priority band.
        ordered = sorted(plan_items, key=lambda it: _PRIORITY_RANK[it.priority])

        open_questions = [t for t in tasks if t.rstrip().endswith("?")]
        blockers = [it.task for it in plan_items if it.is_blocker]

        result = ExecutivePlan(
            agent=self.name,
            items=[asdict(it) for it in plan_items],
            prioritized_order=[it.task for it in ordered],
            suggested_focus=[it.task for it in ordered[:focus_count]],
            blockers=blockers,
            open_questions=open_questions,
            decision_log_template={
                "date": "TODO: YYYY-MM-DD",
                "decision": "TODO: what was decided",
                "rationale": "TODO: why",
                "owner": "TODO: who",
            },
            assumptions=[
                "Priorities are inferred from urgency keywords in the supplied text.",
                "No tasks, dates, or decisions were invented.",
                "No external actions taken — planning only; a human executes.",
            ],
        )
        return asdict(result)

    @staticmethod
    def _normalize_items(items: str | list[str]) -> list[str]:
        if isinstance(items, str):
            raw = _SPLIT.split(items)
        elif isinstance(items, list):
            raw = items
        else:
            raise ValueError("items must be a string or a list of strings.")
        cleaned: list[str] = []
        for entry in raw:
            if not isinstance(entry, str):
                raise ValueError("each task must be a string.")
            text = entry.strip().lstrip("-*•").strip()
            if text:
                cleaned.append(text)
        return cleaned

    @staticmethod
    def _classify(task: str) -> PlanItem:
        lowered = task.lower()
        is_blocker = any(term in lowered for term in _BLOCKER_TERMS)
        if is_blocker or any(term in lowered for term in _HIGH_TERMS):
            priority: Priority = "high"
        elif any(term in lowered for term in _LOW_TERMS):
            priority = "low"
        else:
            priority = "medium"
        return PlanItem(task=task, priority=priority, is_blocker=is_blocker)


if __name__ == "__main__":
    agent = ExecutiveAssistantAgent()
    sample = (
        "Patch the urgent auth vulnerability today\n"
        "Refactor the logging module someday\n"
        "Blocked on security review for the release\n"
        "Should we adopt the new framework?"
    )
    print(json.dumps(agent.plan(sample), indent=2))
