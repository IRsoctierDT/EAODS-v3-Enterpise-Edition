---
title: EAODS Business Architecture
document_id: EAODS-ARCH-BIZ-001
version: 1.0.0
status: proposed
owner: Enterprise Architecture Owner
review_gate: Enterprise Architecture Review Board and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - EAODS-ARCH-EOM-001
  - EAODS-GOV-MAN-001
  - EAODS-ARCH-GOV-001
  - ADR-0002
  - history/original-sources/conversation-evidence/v6.7-v16-band (EAODS v13.0.0–13.0.5 alpha volume units)
  - history/original-sources/conversation-evidence/v6.7-v16-band (EAODS v15.0.0–15.0.5 alpha volume units)
---

# EAODS Business Architecture

## 1. Purpose and scope

This document defines the EAODS business architecture: the business capabilities, business services, operating model, decision rights, and organizational interfaces through which the enterprise is governed and run.

It normalizes the v13.0 Enterprise Operating Model & Capability Framework and the v15.0 Enterprise Intelligence & Adaptive Organization Framework volume units into a single governed reference. Technology, data, and platform concerns are out of scope and are addressed by companion architecture documents under the same review gate.

The organizing idea, stated in v13.0 Volume 1, is that the enterprise is organized around business capabilities — independently governed, measurable, composable, and continuously improved — rather than around technology. Technology, AI agents, cybersecurity, governance, operations, data, and executive leadership act as supporting capabilities, not isolated departments.

## 2. Business architecture principles

Every enterprise capability shall be:

1. business-owned;
2. architecture-governed;
3. security-enabled;
4. measurable;
5. interoperable;
6. continuously improved;
7. AI-assisted where appropriate;
8. operationally accountable.

Portfolio and governance decisions that shape the business architecture shall be strategy-driven, evidence-based, risk-informed, capability-centric, financially accountable, and transparently governed. Executive judgment remains the final decision authority.

## 3. Capability hierarchy

Capabilities are organized into four levels.

| Level | Description |
|-------|-------------|
| L1 | Enterprise Domain |
| L2 | Business Capability |
| L3 | Operational Capability |
| L4 | Implemented Service |

Business services are the L4 realization of capabilities: every operational service maps upward to an approved business capability, and no capability exists without documented ownership.

## 4. Enterprise domains (L1)

The recommended enterprise domains are:

- Executive Leadership
- Enterprise Governance
- Enterprise Risk
- Finance
- Human Capital
- Legal
- Enterprise Architecture
- Data & Knowledge
- Artificial Intelligence
- Technology Operations
- Cybersecurity (Domain 03)
- Business Operations
- Customer Services
- Innovation
- Strategy

Cybersecurity (Domain 03) is treated as an enterprise capability integrated across all others — through architectural review, risk assessment, control mapping, continuous monitoring, threat intelligence, resilience planning, and incident coordination — rather than as an isolated department.

## 5. Capability ownership model

Every capability shall define six named ownership roles:

| Role | Accountability |
|------|----------------|
| Executive Owner | Strategic outcomes and enterprise risk |
| Business Owner | Business value and capability direction |
| Technical Owner | Solution realization |
| Governance Owner | Policy and compliance |
| Operational Owner | Day-to-day service delivery |
| Performance Owner | Measurement and reporting |

Executive sponsors additionally carry responsibility for strategic outcomes, governance compliance, budget stewardship, capability maturity, organizational readiness, enterprise risk, performance reporting, and corrective-action sponsorship.

## 6. Business services and value streams

Capabilities deliver value through end-to-end value streams. The required value streams are:

- Strategy-to-Execution
- Demand-to-Delivery
- Detect-to-Respond
- Incident-to-Recovery
- Data-to-Decision
- Idea-to-Innovation
- Risk-to-Assurance
- Customer-to-Value

Each capability shall support one or more value streams. Value stream economics — investment cost, operating cost, value contribution, throughput, bottlenecks, and waste — are evaluated per stream and linked to the capabilities that serve it, so business services are funded and improved on evidence of stream performance rather than departmental output.

## 7. Operating model

The enterprise operates a federated operating model: enterprise policies and central governance at the core, capability governance boards in the middle tier, and local operational autonomy at the edge. Local execution may vary only within approved enterprise guardrails, and operational feedback flows back into governance improvement.

Funding follows the same structure. Capabilities — not projects — are the primary funding unit, each maintaining an annual operating budget, capital investment plan, innovation reserve, technical debt allocation, resilience allocation, and optimization budget. Every investment maps upward through the portfolio hierarchy (Enterprise Portfolio → Strategic Capability Portfolio → Program → Project → Operational Service) to an approved capability.

The v15.0 framework makes this operating model adaptive: organizational structure, governance efficiency, workflow effectiveness, capability utilization, automation maturity, executive decision latency, and operational bottlenecks are continuously evaluated, and operating-model changes are recommended from verified outcomes while preserving enterprise governance constraints.

## 8. Decision rights

Enterprise decisions are classified by authority.

| Decision class | Approval authority |
|----------------|--------------------|
| Editorial | Document Owner |
| Operational | Domain Owner |
| Technical architecture | Enterprise Architecture Review Board |
| AI governance | AI Governance Council |
| Enterprise risk | Enterprise Risk Council |
| Enterprise policy | Enterprise Governance Board |
| Strategic investment | Executive Leadership |

**Naming reconciliation.** The v13 source states a six-class model — Strategic,
Architectural, Cybersecurity, AI Governance, Operational, Emergency. The table
above is the approved seven-class taxonomy of EAODS-GOV-MAN-001 §6, which
governs. The source classes map onto it without creating a body or an authority:

| v13 source class | Approved class | Authority |
|---|---|---|
| Strategic | Strategic investment | Executive Leadership |
| Architectural | Technical architecture | Enterprise Architecture Review Board |
| **Cybersecurity** | Technical architecture | EARB, with Domain 03 review as a **consultation** — consultation confers no approval authority |
| AI Governance | AI governance | AI Governance Council |
| **Operational** | Operational | **Domain Owner** (the source's "Capability Owner" is read as Domain Owner) |
| **Emergency** | not a class | An authorization *path*, not a decision class: EAODS-GOV-CAB-001 §6.2 defers review sequence, never review substance. The Incident Commander acts under a time-bounded delegation from the Domain Owner, recorded as an Operational decision. |

No new governing body is created by this document and no authority is
transferred. The four overlays of EAODS-GOV-MAN-001 §6 apply cumulatively.

Governance authority is tiered from G1 (Board Governance) through G2 (Executive Leadership), G3 (Enterprise Governance Councils), G4 (Capability Governance Boards), G5 (Operational Management), to G6 (Delivery and Execution Teams). Each tier possesses explicitly documented authority and accountability.

Delegated authority shall be documented, time-bounded where appropriate, and periodically reviewed. Every capability maintains a RACI matrix spanning strategic planning, funding, architecture, engineering, cybersecurity, operations, compliance, executive reporting, and retirement.

Every enterprise decision records: identifier, requesting authority, approving authority, affected capabilities, supporting evidence, associated risks, expected benefits, implementation owner, and review date. Decisions follow a defined lifecycle — request, impact assessment, architecture review, risk assessment, governance approval, implementation, outcome measurement, and decision review — and are preserved in the enterprise decision register with links to supporting evidence and implementation outcomes.

## 9. Governance bodies

The minimum governance structure comprises:

- Executive Leadership Council
- Enterprise Governance Council
- Enterprise Architecture Review Board (EARB)
- Domain 03 Governance Board
- AI Governance Council
- Enterprise Risk Committee
- Change Advisory Board
- Data Governance Council
- Portfolio Management Board
- Operational Excellence Council

Each body maintains a charter, scope, authority, quorum requirements, voting procedures, review cadence, and decision register. Governance effectiveness is measured on decision cycle time, policy compliance, exception frequency, board attendance, implementation success, corrective-action completion, executive accountability, and Domain 03 participation.

## 10. Organizational interfaces

The principal cross-organizational interfaces are:

| Interface | Obligation |
|-----------|------------|
| EARB ↔ Portfolio governance | Architecture approval is required before portfolio funding |
| Domain 03 ↔ Portfolio and governance reviews | Domain 03 participates in decisions affecting enterprise risk, infrastructure, cloud, AI deployments, identity systems, and customer-facing services; cybersecurity review is mandatory for material enterprise changes |
| Capability boards ↔ Delivery organizations | Local autonomy operates within centrally approved guardrails |
| Strategic intelligence ↔ Executive planning | Strategic, risk, capability, value, and performance intelligence inform executive decisions; recommendations never automatically authorize high-impact actions |
| Escalation path | E1–E5 tier notation, mapped to the approved fixed path below |

Governance conflicts are resolved through documented issue statements, evidence review, stakeholder consultation, architectural evaluation, and executive arbitration when required, with resolutions preserved in the decision register.

**Escalation reconciliation.** E1–E5 is the v13 source's tier notation. The
binding path is the fixed one in EAODS-GOV-MAN-001 §9, EAODS-GOV-EXC-001 §12 and
EAODS-GOV-DEC-001 §13:

| Source tier | Approved step |
|---|---|
| E1 Team Lead | the operational issue as raised |
| E2 Capability Owner | Domain Owner |
| E3 Governance Board | Governance Manager, then the Architecture, AI, or Risk Council |
| E4 Executive Leadership | Enterprise Governance Board |
| E5 Board-Level Review | Executive Leadership |

Where the notations differ, the approved path governs.

## 11. Planning and operating cadence

Business planning follows a closed cycle: strategy, capability assessment, roadmap planning, investment approval, implementation, measurement, and continuous improvement. Roadmaps span 12, 24, 36, and 60 months with capability milestones, investment phases, dependency sequencing, retirement plans, and executive decision gates.

The v15.0 adaptive planning framework supplements this with rolling strategic planning, annual planning, quarterly adjustment, scenario-triggered replanning, and crisis adaptation. The executive operating rhythm comprises weekly operational reviews, monthly performance governance, quarterly strategic reviews, and annual enterprise performance assessments; each review generates documented decisions, assigned actions, and follow-up metrics.

## 12. Capability maturity and health

Capabilities are assessed on a six-level maturity scale: Initial, Managed, Standardized, Measured, Optimized, and Adaptive Enterprise — the last representing continuous optimization supported by governed AI and enterprise telemetry. (The v15.0 capability intelligence framework applies an equivalent CM-0 to CM-5 scale with documented, repeatable scoring across governance, people, process, technology, automation, security, resilience, operational performance, and evidence quality.)

Every capability reports maturity, operational health, strategic alignment, staffing readiness, automation maturity, cybersecurity posture, financial efficiency, and customer impact, and maintains a roadmap, investment plan, strategic objectives, KPIs, KRIs, technical debt register, and dependency map.

## 13. Enterprise intelligence functions

The v15.0 framework adds six business intelligence functions that keep the organization adaptive. Each operates as a governed capability with human decision authority retained:

| Function | Business contribution |
|----------|----------------------|
| Strategic Intelligence | Continuous strategy evaluation, scenario-oriented foresight, executive decision optimization |
| Decision Laboratory | Governed evaluation of strategic alternatives (wargaming, simulation) before resources are committed |
| Risk Intelligence | Unified enterprise risk model with appetite, tolerance, escalation thresholds, and documented risk acceptance authority |
| Capability Intelligence | Maturity measurement, transformation planning, investment prioritization, organizational readiness |
| Value Intelligence | Benefits realization, value attribution without double-counting, adaptive investment optimization |
| Performance Intelligence | KPI/KRI governance with named metric owners, organizational learning, benchmarking, operating-model adaptation |

Validated organizational learning — lessons from operations, incidents, transformations, and executive reviews — updates enterprise standards, playbooks, and knowledge repositories, closing the loop between execution and the operating model.

## 14. Human review gate

Adoption of this business architecture requires confirmation that: capability ownership is documented at all four levels; the federated operating model and its guardrails remain intact; decision rights, delegated authority, and escalation thresholds are explicit and auditable; Domain 03 participation in material decisions is preserved; intelligence functions inform but do not replace human decision authority; and all governance decisions remain traceable to evidence per the governing architecture.

## 15. Sources and traceability

| Source (repo-relative path) | Contribution |
|-----------------------------|--------------|
| docs/architecture/ENTERPRISE_OPERATING_MODEL.md | House style, four-pillar context, governing architecture, decision and accountability baseline |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v13.0.0-alpha-enterprise-operating-model-capability-framework-volume-1-ent.md | Capability-centric premise, principles, L1–L4 hierarchy, enterprise domains, ownership model, federated operating model, maturity levels, capability health, planning cycle |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v13.0.1-alpha-enterprise-operating-model-capability-framework-volume-2-ent.md | Portfolio principles and hierarchy, capability funding model, required value streams, roadmap horizons, EARB-before-funding interface, Domain 03 portfolio participation |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v13.0.2-alpha-enterprise-operating-model-capability-framework-volume-3-ent.md | Decision rights classes, governance tiers G1–G6, governance bodies and charter obligations, RACI scope, decision lifecycle and record attributes, escalation levels E1–E5, conflict resolution, governance metrics, executive accountability model |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v13.0.3-alpha-enterprise-operating-model-capability-framework-volume-4-ent.md | Business-capability-to-service traceability context (business architecture phase of the architecture method) |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v13.0.4-alpha-enterprise-operating-model-capability-framework-volume-5-ent.md | Business services as a governed configuration domain; service-to-capability relationship model context |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v13.0.5-alpha-enterprise-operating-model-capability-framework-volume-6-ent.md | Business/governance telemetry domains, capability health scoring, decision-support boundary (recommendations do not authorize high-impact actions) |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v15.0.0-alpha-enterprise-intelligence-adaptive-organization-framework-volu.md | Strategic Intelligence function, adaptive planning framework, executive decision model, human-directed principle |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v15.0.1-alpha-enterprise-intelligence-adaptive-organization-framework-volu.md | Decision Laboratory function, scenario governance, enterprise learning repository |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v15.0.2-alpha-enterprise-intelligence-adaptive-organization-framework-volu.md | Risk Intelligence function, risk appetite/tolerance and acceptance authority, escalation thresholds |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v15.0.3-alpha-enterprise-intelligence-adaptive-organization-framework-volu.md | Capability Intelligence function, CM-0–CM-5 maturity scale and assessment criteria, transformation planning, organizational readiness |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v15.0.4-alpha-enterprise-intelligence-adaptive-organization-framework-volu.md | Value Intelligence function, benefits realization framework, value attribution rule, value stream economics |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v15.0.5-alpha-enterprise-intelligence-adaptive-organization-framework-volu.md | Performance Intelligence function, KPI/KRI governance, adaptive operating model, organizational learning framework, executive operating cadence |
