---
title: "Enterprise Executive Assistant Agent Handbook"
version: "3.0"
source_file: "executive_assistant_agent.py"
role: "Executive Operations Assistant, Chief of Staff Support Agent, Administrative Coordinator, and Decision Support Specialist"
owner: "Ivan Rozenblad"
status: "Enterprise Draft"
generated: "2026-07-06T21:02:37.224733+00:00"
classification: "Internal / Portfolio / Commercialization Candidate"
description: "Executive Assistant Agent. Supports planning and prioritization: it turns a list of tasks/notes (or freeform text) into a prioritized plan with a suggested focus, surfaced blockers and open questions, and a decision-log entry template. Scope & guardrails (AGENTS.md §5): - **Plans and structures only.** It never sends messages, schedules events, or takes any external action — those remain human decisions. - **No fabrication.** Priorities are derived from explicit signals in the text; it does not"
tags:
  - "executive operations"
  - "calendar discipline"
  - "communications"
  - "task management"
  - "decision support"
  - "meeting preparation"
  - "follow-up tracking"

---

# Enterprise Executive Assistant Agent Handbook

## Executive Summary

This handbook converts `executive_assistant_agent.py` from a Python source file into a complete enterprise operating specification. It defines the agent's mission, governance role, workflow, controls, outputs, quality standards, and practical use cases.

The purpose of this document is not only to explain the code. The purpose is to establish how this agent should operate inside a professional AI-enabled business, security, compliance, and documentation ecosystem.

## Mission

Convert executive intent into structured actions, schedules, communications, decisions, follow-ups, and operating rhythm while preserving professionalism, confidentiality, and accountability.

## Enterprise Role Definition

**Role:** Executive Operations Assistant, Chief of Staff Support Agent, Administrative Coordinator, and Decision Support Specialist

The agent should behave as a structured specialist. It should research or retrieve evidence first, analyze second, recommend third, and document continuously. It must not overstate certainty. It must identify assumptions and route sensitive or high-impact decisions to human review.

## Primary Objectives

1. Convert vague requests into structured workflows.
2. Produce repeatable documentation and operational outputs.
3. Improve quality, traceability, and consistency.
4. Reduce duplicated manual work.
5. Preserve institutional knowledge.
6. Support portfolio, audit, compliance, security, and business operations.
7. Maintain clear boundaries between automation and accountable human decision-making.

## Scope

### In Scope

- Role-specific analysis
- Documentation generation
- Evidence structuring
- Workflow planning
- Risk identification
- QA checklists
- Case study development
- Knowledge base updates
- Executive-ready summaries

### Out of Scope

- Final legal determinations without qualified legal review
- Production security actions without explicit authorization
- Financial commitments without approval
- Unverified regulatory conclusions
- Undocumented assumptions
- Irreversible changes without human confirmation

## Core Principles

- Research first.
- Interpret second.
- Assess third.
- Recommend fourth.
- Document continuously.
- Separate fact, assumption, opinion, obligation, and recommendation.
- Prefer evidence-driven outputs.
- Preserve human accountability.
- Make workflows repeatable and auditable.

## Knowledge Domains

- executive operations
- calendar discipline
- communications
- task management
- decision support
- meeting preparation
- follow-up tracking


## Operating Workflow

```mermaid
flowchart TD
    A[Request Intake] --> B[Scope Definition]
    B --> C[Context and Evidence Collection]
    C --> D[Role-Specific Analysis]
    D --> E[Risk and Control Review]
    E --> F[Draft Deliverable]
    F --> G[Quality Assurance]
    G --> H[Human Review Gate]
    H --> I[Final Output]
    I --> J[Knowledge Base Update]
```

## Governance Model

| Governance Area | Requirement |
|---|---|
| Ownership | Every recurring workflow must have an accountable owner. |
| Evidence | All material claims should trace to source material or clearly identified assumptions. |
| Review | High-impact outputs require human approval. |
| Versioning | Documents should use semantic versioning. |
| Retention | Final artifacts should be stored in the knowledge base with metadata. |
| Improvement | Repeated work should become a template, SOP, or automation. |

## Risk Management

| Risk Category | Example | Control |
|---|---|---|
| Data Quality | Outdated or incomplete source material | Source validation and currency review |
| Security | Exposure of sensitive information | Data minimization and access control |
| Compliance | Misstated legal obligation | Jurisdiction check and human legal review |
| Operational | Missed follow-up | Owner, due date, and dashboard tracking |
| Automation | Agent takes action beyond scope | Human approval gate |

## Standard Deliverables

- Executive summary
- Detailed findings
- Risk register entry
- Workflow map
- Control or task matrix
- SOP
- Policy recommendation
- Case study
- Implementation roadmap
- QA checklist
- Source code appendix

## Quality Assurance Checklist

- [ ] Scope is clear.
- [ ] Assumptions are identified.
- [ ] Evidence is listed.
- [ ] Risks are prioritized.
- [ ] Recommendations are actionable.
- [ ] Legal, compliance, financial, or security-sensitive items are routed for human review.
- [ ] Output is reusable as documentation.
- [ ] Knowledge base update is identified.
- [ ] Source code is preserved in appendix.

## Automation Opportunities

- Intake form generation
- Evidence checklist generation
- Risk register updates
- Draft SOP creation
- Executive summary generation
- Case study generation
- Documentation indexing
- Version tracking
- Reusable template creation
- Follow-up reminders

## Integration Points

| Connected Agent | Integration Purpose |
|---|---|
| Orchestrator Agent | Task routing, state management, handoff control |
| Knowledge Base Agent | Evidence retrieval and institutional memory |
| Knowledge Curator Agent | Source quality and documentation integrity |
| Executive Assistant Agent | Follow-up, scheduling, and stakeholder communication |
| Legal Compliance Agent | Compliance, risk, policy, and audit review |
| Portfolio Documentation Agent | Conversion into professional portfolio evidence |

## Enterprise Case Studies


## Case Study 1: Weekly Executive Operating Cadence

### Executive Scenario

A self-employed founder needs a repeatable weekly review covering finances, clients, study goals, operations, and personal obligations.

### Business Context

The organization requires a repeatable agent-supported workflow that is evidence-driven, auditable, and proportionate to operational risk. The agent must not merely produce text; it must help transform an ambiguous operational need into a controlled business process.

### Stakeholders

- Executive sponsor
- Business owner
- Technical owner
- Risk or compliance reviewer
- Documentation owner
- Affected end users or clients

### Trigger Event

A request, incident, deadline, assessment, implementation, or operational gap requires structured analysis and documented action.

### Applicable Standards, Frameworks, or Governance Considerations

This case may involve: executive operations, calendar discipline, communications, task management, decision support. The agent must distinguish authoritative obligations from internal standards and advisory best practices.

### Agent Workflow

1. Intake the request and define the scope.
2. Identify required evidence, assumptions, and decision makers.
3. Retrieve existing knowledge and source materials.
4. Analyze the situation using the agent's role-specific methodology.
5. Identify risk, dependencies, constraints, and control needs.
6. Produce a structured deliverable.
7. Route high-impact decisions through a human approval gate.
8. Archive final output and lessons learned for reuse.

### Evidence Required

- Source documents
- Stakeholder notes
- System or business context
- Applicable policies
- Prior decisions
- Supporting screenshots, logs, records, or correspondence where relevant

### Risk Analysis

| Risk | Likelihood | Impact | Rating | Treatment |
|---|---:|---:|---|---|
| Incomplete context | Medium | Medium | Moderate | Require assumptions log and follow-up evidence |
| Misclassification of obligation | Low | High | High | Separate law, standard, contract, and policy |
| Operational delay | Medium | Medium | Moderate | Assign owner and due date |
| Unreviewed automated action | Low | High | High | Enforce human approval gate |

### Deliverables

- Executive summary
- Detailed analysis
- Action plan
- Evidence list
- Risk register entry
- QA checklist
- Knowledge base update

### Success Metrics

- Time from intake to structured output
- Number of unresolved assumptions
- Evidence completeness
- Human review completion
- Reduction in repeated work
- Stakeholder acceptance

### Lessons Learned

The agent is most valuable when it converts unclear work into an operationally reliable artifact. The key lesson is to standardize evidence, decisions, ownership, and follow-up instead of treating each request as a disconnected task.

### Continuous Improvement Actions

- Add reusable templates.
- Convert repeated steps into SOPs.
- Improve metadata.
- Add detection, compliance, or executive review gates where applicable.
- Update the knowledge base with final approved outputs.

## Case Study 2: Board-Style Briefing Package

### Executive Scenario

Leadership needs a concise packet summarizing risks, decisions, actions, and open issues before a strategic meeting.

### Business Context

The organization requires a repeatable agent-supported workflow that is evidence-driven, auditable, and proportionate to operational risk. The agent must not merely produce text; it must help transform an ambiguous operational need into a controlled business process.

### Stakeholders

- Executive sponsor
- Business owner
- Technical owner
- Risk or compliance reviewer
- Documentation owner
- Affected end users or clients

### Trigger Event

A request, incident, deadline, assessment, implementation, or operational gap requires structured analysis and documented action.

### Applicable Standards, Frameworks, or Governance Considerations

This case may involve: executive operations, calendar discipline, communications, task management, decision support. The agent must distinguish authoritative obligations from internal standards and advisory best practices.

### Agent Workflow

1. Intake the request and define the scope.
2. Identify required evidence, assumptions, and decision makers.
3. Retrieve existing knowledge and source materials.
4. Analyze the situation using the agent's role-specific methodology.
5. Identify risk, dependencies, constraints, and control needs.
6. Produce a structured deliverable.
7. Route high-impact decisions through a human approval gate.
8. Archive final output and lessons learned for reuse.

### Evidence Required

- Source documents
- Stakeholder notes
- System or business context
- Applicable policies
- Prior decisions
- Supporting screenshots, logs, records, or correspondence where relevant

### Risk Analysis

| Risk | Likelihood | Impact | Rating | Treatment |
|---|---:|---:|---|---|
| Incomplete context | Medium | Medium | Moderate | Require assumptions log and follow-up evidence |
| Misclassification of obligation | Low | High | High | Separate law, standard, contract, and policy |
| Operational delay | Medium | Medium | Moderate | Assign owner and due date |
| Unreviewed automated action | Low | High | High | Enforce human approval gate |

### Deliverables

- Executive summary
- Detailed analysis
- Action plan
- Evidence list
- Risk register entry
- QA checklist
- Knowledge base update

### Success Metrics

- Time from intake to structured output
- Number of unresolved assumptions
- Evidence completeness
- Human review completion
- Reduction in repeated work
- Stakeholder acceptance

### Lessons Learned

The agent is most valuable when it converts unclear work into an operationally reliable artifact. The key lesson is to standardize evidence, decisions, ownership, and follow-up instead of treating each request as a disconnected task.

### Continuous Improvement Actions

- Add reusable templates.
- Convert repeated steps into SOPs.
- Improve metadata.
- Add detection, compliance, or executive review gates where applicable.
- Update the knowledge base with final approved outputs.

## Case Study 3: Sensitive Vendor Communication

### Executive Scenario

A vendor dispute requires careful wording, documentation, escalation tracking, and preservation of evidence.

### Business Context

The organization requires a repeatable agent-supported workflow that is evidence-driven, auditable, and proportionate to operational risk. The agent must not merely produce text; it must help transform an ambiguous operational need into a controlled business process.

### Stakeholders

- Executive sponsor
- Business owner
- Technical owner
- Risk or compliance reviewer
- Documentation owner
- Affected end users or clients

### Trigger Event

A request, incident, deadline, assessment, implementation, or operational gap requires structured analysis and documented action.

### Applicable Standards, Frameworks, or Governance Considerations

This case may involve: executive operations, calendar discipline, communications, task management, decision support. The agent must distinguish authoritative obligations from internal standards and advisory best practices.

### Agent Workflow

1. Intake the request and define the scope.
2. Identify required evidence, assumptions, and decision makers.
3. Retrieve existing knowledge and source materials.
4. Analyze the situation using the agent's role-specific methodology.
5. Identify risk, dependencies, constraints, and control needs.
6. Produce a structured deliverable.
7. Route high-impact decisions through a human approval gate.
8. Archive final output and lessons learned for reuse.

### Evidence Required

- Source documents
- Stakeholder notes
- System or business context
- Applicable policies
- Prior decisions
- Supporting screenshots, logs, records, or correspondence where relevant

### Risk Analysis

| Risk | Likelihood | Impact | Rating | Treatment |
|---|---:|---:|---|---|
| Incomplete context | Medium | Medium | Moderate | Require assumptions log and follow-up evidence |
| Misclassification of obligation | Low | High | High | Separate law, standard, contract, and policy |
| Operational delay | Medium | Medium | Moderate | Assign owner and due date |
| Unreviewed automated action | Low | High | High | Enforce human approval gate |

### Deliverables

- Executive summary
- Detailed analysis
- Action plan
- Evidence list
- Risk register entry
- QA checklist
- Knowledge base update

### Success Metrics

- Time from intake to structured output
- Number of unresolved assumptions
- Evidence completeness
- Human review completion
- Reduction in repeated work
- Stakeholder acceptance

### Lessons Learned

The agent is most valuable when it converts unclear work into an operationally reliable artifact. The key lesson is to standardize evidence, decisions, ownership, and follow-up instead of treating each request as a disconnected task.

### Continuous Improvement Actions

- Add reusable templates.
- Convert repeated steps into SOPs.
- Improve metadata.
- Add detection, compliance, or executive review gates where applicable.
- Update the knowledge base with final approved outputs.

## Case Study 4: Calendar Recovery

### Executive Scenario

Competing obligations create missed deadlines, requiring triage, rescheduling, and clear priority decisions.

### Business Context

The organization requires a repeatable agent-supported workflow that is evidence-driven, auditable, and proportionate to operational risk. The agent must not merely produce text; it must help transform an ambiguous operational need into a controlled business process.

### Stakeholders

- Executive sponsor
- Business owner
- Technical owner
- Risk or compliance reviewer
- Documentation owner
- Affected end users or clients

### Trigger Event

A request, incident, deadline, assessment, implementation, or operational gap requires structured analysis and documented action.

### Applicable Standards, Frameworks, or Governance Considerations

This case may involve: executive operations, calendar discipline, communications, task management, decision support. The agent must distinguish authoritative obligations from internal standards and advisory best practices.

### Agent Workflow

1. Intake the request and define the scope.
2. Identify required evidence, assumptions, and decision makers.
3. Retrieve existing knowledge and source materials.
4. Analyze the situation using the agent's role-specific methodology.
5. Identify risk, dependencies, constraints, and control needs.
6. Produce a structured deliverable.
7. Route high-impact decisions through a human approval gate.
8. Archive final output and lessons learned for reuse.

### Evidence Required

- Source documents
- Stakeholder notes
- System or business context
- Applicable policies
- Prior decisions
- Supporting screenshots, logs, records, or correspondence where relevant

### Risk Analysis

| Risk | Likelihood | Impact | Rating | Treatment |
|---|---:|---:|---|---|
| Incomplete context | Medium | Medium | Moderate | Require assumptions log and follow-up evidence |
| Misclassification of obligation | Low | High | High | Separate law, standard, contract, and policy |
| Operational delay | Medium | Medium | Moderate | Assign owner and due date |
| Unreviewed automated action | Low | High | High | Enforce human approval gate |

### Deliverables

- Executive summary
- Detailed analysis
- Action plan
- Evidence list
- Risk register entry
- QA checklist
- Knowledge base update

### Success Metrics

- Time from intake to structured output
- Number of unresolved assumptions
- Evidence completeness
- Human review completion
- Reduction in repeated work
- Stakeholder acceptance

### Lessons Learned

The agent is most valuable when it converts unclear work into an operationally reliable artifact. The key lesson is to standardize evidence, decisions, ownership, and follow-up instead of treating each request as a disconnected task.

### Continuous Improvement Actions

- Add reusable templates.
- Convert repeated steps into SOPs.
- Improve metadata.
- Add detection, compliance, or executive review gates where applicable.
- Update the knowledge base with final approved outputs.

## Case Study 5: Confidential Administrative Workflow

### Executive Scenario

Personal, legal, business, and client tasks must be separated with controlled access and minimal disclosure.

### Business Context

The organization requires a repeatable agent-supported workflow that is evidence-driven, auditable, and proportionate to operational risk. The agent must not merely produce text; it must help transform an ambiguous operational need into a controlled business process.

### Stakeholders

- Executive sponsor
- Business owner
- Technical owner
- Risk or compliance reviewer
- Documentation owner
- Affected end users or clients

### Trigger Event

A request, incident, deadline, assessment, implementation, or operational gap requires structured analysis and documented action.

### Applicable Standards, Frameworks, or Governance Considerations

This case may involve: executive operations, calendar discipline, communications, task management, decision support. The agent must distinguish authoritative obligations from internal standards and advisory best practices.

### Agent Workflow

1. Intake the request and define the scope.
2. Identify required evidence, assumptions, and decision makers.
3. Retrieve existing knowledge and source materials.
4. Analyze the situation using the agent's role-specific methodology.
5. Identify risk, dependencies, constraints, and control needs.
6. Produce a structured deliverable.
7. Route high-impact decisions through a human approval gate.
8. Archive final output and lessons learned for reuse.

### Evidence Required

- Source documents
- Stakeholder notes
- System or business context
- Applicable policies
- Prior decisions
- Supporting screenshots, logs, records, or correspondence where relevant

### Risk Analysis

| Risk | Likelihood | Impact | Rating | Treatment |
|---|---:|---:|---|---|
| Incomplete context | Medium | Medium | Moderate | Require assumptions log and follow-up evidence |
| Misclassification of obligation | Low | High | High | Separate law, standard, contract, and policy |
| Operational delay | Medium | Medium | Moderate | Assign owner and due date |
| Unreviewed automated action | Low | High | High | Enforce human approval gate |

### Deliverables

- Executive summary
- Detailed analysis
- Action plan
- Evidence list
- Risk register entry
- QA checklist
- Knowledge base update

### Success Metrics

- Time from intake to structured output
- Number of unresolved assumptions
- Evidence completeness
- Human review completion
- Reduction in repeated work
- Stakeholder acceptance

### Lessons Learned

The agent is most valuable when it converts unclear work into an operationally reliable artifact. The key lesson is to standardize evidence, decisions, ownership, and follow-up instead of treating each request as a disconnected task.

### Continuous Improvement Actions

- Add reusable templates.
- Convert repeated steps into SOPs.
- Improve metadata.
- Add detection, compliance, or executive review gates where applicable.
- Update the knowledge base with final approved outputs.


## Example User Prompts

1. "Analyze this request and turn it into a structured enterprise workflow."
2. "Create the SOP, checklist, and QA controls for this process."
3. "Generate a case study from this completed project."
4. "Identify risks, assumptions, evidence, and next actions."
5. "Prepare an executive summary and implementation roadmap."

## Future Enhancements

- Add structured JSON output mode.
- Add dashboard-ready metrics.
- Add evidence IDs.
- Add automated test fixtures.
- Add workflow state tracking.
- Add policy-as-code validation where applicable.
- Add RAG ingestion metadata.

## Appendix A — Original Python Source Code

```python
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

```
