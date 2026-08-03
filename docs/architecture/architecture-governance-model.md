---
title: EAODS Architecture Governance Model
document_id: EAODS-ARCH-GOV-001
version: 1.0.0
status: proposed
owner: Enterprise Architecture Review Board
review_gate: Enterprise Architecture Review Board and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - EAODS-ARCH-EOM-001
  - EAODS-ARCH-PRIN-001
  - ADR-0001
  - ADR-0002
  - history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v4.17.1-v4.28/EAODS-v4.26-alpha-enterprise-governance-operating-model-and-decision-authority-framework.md
---

# EAODS Architecture Governance Model

## 1. Purpose

This document defines how architecture decisions are made, reviewed, recorded, superseded, and escalated in EAODS Enterprise Edition. It establishes the charter and composition of the Enterprise Architecture Review Board, the decision authorities that surround it, the lifecycle of an architecture decision record, the review gates a change must pass, the handling of approved deviations, and the cadence at which governance operates. It exists because the Enterprise Reference Operating Model requires that architecture decisions be explicit and reviewable (ADR-0002, EAODS-ARCH-EOM-001), and because a reference operating model without named decision rights reproduces the failure the governance framework was written to prevent: unclear decision ownership, inconsistent escalation paths, and no executive visibility into unresolved issues.

## 2. Scope and governing authority

This model governs every artifact class that the operating model integrates: the ADR catalog, standards, the control catalog, threat models, runbooks, architecture patterns, the migration corpus, the knowledge graph, reference implementations, and GitHub governance workflows.

Authority is layered. EAODS v17.3 Volume 10 is the operational north star. ADR-0002 is the accepted decision that constitutes the four-pillar operating model and reserves material change to it for board review and Program Owner approval. ADR-0001 fixes the repository structure within which architecture decisions live, placing them under `architecture/adr/`. The v4.26 Enterprise Governance Operating Model and Decision Authority Framework supplies the governance bodies, decision classification, RACI assignments, escalation path, and cadence that this document applies to architecture work.

**Naming reconciliation.** The v4.26 framework names the architecture authority the Security Architecture Review Board (SARB); ADR-0002 names it the EAODS Enterprise Architecture Board; the approved sibling documents record the gate as "Enterprise Architecture Review Board and Program Owner approval". These refer to one body. This document uses **Enterprise Architecture Review Board (EARB)** throughout, and the responsibilities, outputs, decision authority, and cadence assigned to the SARB in v4.26 are the responsibilities, outputs, decision authority, and cadence of the EARB here. No new body is created by this reconciliation.

## 3. Governance objectives

The governance operating model applied to architecture shall:

- establish clear accountability;
- eliminate decision ambiguity;
- standardize governance workflows;
- provide executive oversight;
- accelerate risk-informed decision making;
- ensure policy consistency;
- improve cross-functional collaboration;
- support enterprise scalability.

## 4. Governance architecture

Authority descends from Executive Leadership through the Enterprise Governance Board, which sits above three peer councils — the Enterprise Architecture Review Board, the AI Governance Council, and the Enterprise Risk Council — and from those councils through Domain Owners, Platform Owners, and Operational Teams.

| Body | Charter position | Architecture-relevant responsibilities |
|------|-----------------|----------------------------------------|
| Executive Leadership | Strategic oversight | Approves strategic investment; receives mandatory escalations |
| Enterprise Governance Board (EGB) | Highest decision-making authority for EAODS governance | Approves enterprise strategy and new governance standards; resolves cross-domain conflicts; reviews enterprise risk posture; oversees EAODS maturity progression |
| Enterprise Architecture Review Board (EARB) | Architecture authority | Reviews security architecture; approves architectural deviations; validates security patterns; reviews technical standards; assesses technology risks |
| AI Governance Council (AIGC) | AI authority | Governs AI systems and model usage; approves AI tooling, deployment standards, model lifecycle policies, AI governance controls, and AI risk treatment strategies; oversees prompt governance; evaluates autonomous capabilities |
| Enterprise Risk Council | Risk authority | Enterprise and residual risk review; risk acceptance oversight; KRI monitoring; executive risk reporting |
| Change Advisory Board (CAB) | Change coordination | Coordinates production security changes, emergency changes, configuration governance, release approvals, and deployment scheduling; security representatives participate in reviews affecting critical assets |
| Domain Owners | Domain implementation | Own operational decisions within a domain; responsible for risk acceptance review and compliance assessment inputs |
| Platform Owners | Technical execution | Implement approved architecture within platform scope |
| Program Owner | Final approval for operating-model change | Approves changes that materially alter the four-pillar model, canonical terminology, metadata structure, or cross-volume architecture |

## 5. Enterprise Architecture Review Board: charter and composition

### 5.1 Charter

The EARB is the standing authority for technical architecture decisions in EAODS. It reviews security architecture, approves architectural deviations, validates security patterns, reviews technical standards, and assesses technology risks. Its outputs are architecture decisions, approved reference architectures, technology guidance, and architectural exceptions.

The board does not hold unilateral authority over the operating model itself. Under ADR-0002, changes that materially alter the four-pillar model, canonical terminology, metadata structure, or cross-volume architecture require EARB review **and** final approval by the Program Owner.

### 5.2 Composition

The board is composed from the enterprise governance role catalog. Each seat contributes the responsibility recorded against that role.

| Seat | Responsibility contributed |
|------|---------------------------|
| Enterprise Architect | Architecture governance |
| Chief Information Security Officer | Enterprise security leadership |
| Security Governance Manager | Standards lifecycle |
| Domain Owner | Domain implementation |
| Platform Owner | Technical execution |
| Risk Manager | Risk governance |
| Compliance Lead | Regulatory oversight |
| Operations Manager | Operational delivery |
| Internal Audit | Independent assurance |
| Executive Sponsor | Strategic oversight |

Architecture governance accountability rests with the Enterprise Architect. Internal Audit participates as independent assurance and is not an approving authority for the decisions it reviews.

## 6. Decision authorities

Every decision carries exactly one approval authority. Consultation does not transfer authority.

| Decision type | Approval authority |
|---------------|--------------------|
| Editorial | Document Owner |
| Operational | Domain Owner |
| Technical architecture | Enterprise Architecture Review Board |
| AI governance | AI Governance Council |
| Enterprise risk | Enterprise Risk Council |
| Enterprise policy | Enterprise Governance Board |
| Strategic investment | Executive Leadership |

Two overlays apply to architecture work specifically:

1. A technical architecture decision that materially alters the four-pillar model, canonical terminology, metadata structure, or cross-volume architecture is not final on EARB approval alone; it additionally requires Program Owner approval (ADR-0002).
2. A technical architecture decision that changes AI authority, autonomous capability, or model usage is consulted with the AI Governance Council, whose own approvals remain its authority rather than the board's.

## 7. Accountability matrix

The enterprise RACI assignments applied to architecture governance, with the architecture seat read as the EARB per Section 2:

| Activity | EGB | EARB | AIGC | Domain Owner | Operations |
|----------|-----|------|------|--------------|------------|
| Policy approval | A | C | C | I | I |
| Architecture approval | I | A | C | C | I |
| AI governance decisions | C | C | A | I | I |
| Operational implementation | I | C | C | A | R |
| Risk acceptance review | A | C | C | R | I |
| Compliance assessment | C | C | C | R | A |

Legend: R — Responsible; A — Accountable; C — Consulted; I — Informed.

## 8. Architecture decision record lifecycle

Architecture decisions are recorded as ADRs under `architecture/adr/` and move through four states.

| Stage | Entry condition | Authority | Required evidence | Exit condition |
|-------|----------------|-----------|-------------------|----------------|
| Propose | A material architectural change is identified | Proposer, with the accountable Domain or Platform Owner | Documented rationale; impact analysis; traceability to controls and standards | A complete draft record exists at the next sequential number after the highest accepted ADR |
| Review | Draft record is complete | EARB, consulting AIGC, Enterprise Risk Council, CAB, and Internal Audit as the subject requires | Alternatives considered; supporting evidence; affected standards | Board disposition recorded: accept, revise, reject, or escalate |
| Accept | Board disposition is accept, and Program Owner approval is obtained where the operating model is affected | EARB and, where applicable, Program Owner | Decision log entry with all fields in Section 13 | Record status set to Accepted with date and decision owner; decision retained in Knowledge Memory |
| Supersede | A later accepted decision replaces the earlier one | EARB, under the same gates as acceptance | Supersession record naming the superseding decision | Superseding record names the earlier decision in its `supersedes` field; the earlier record is preserved, not deleted |

### 8.1 Record structure

Accepted records in this repository carry the following front matter and body structure, as established by ADR-0001 and ADR-0002:

| Field or section | Purpose |
|------------------|---------|
| `title` | Decision identifier and one-line statement |
| `status` | Accepted, or superseded once replaced |
| `date` | Date of acceptance |
| `decision_owner` | Named accountable owner of the decision |
| `scope` | Boundary of what the decision governs |
| `supersedes` | Earlier record replaced, or null |
| `related` | Adjacent records and governing volumes |
| Context | Problem, structural risk, and direction |
| Decision | The normative statement |
| Required contribution model | Obligations placed on downstream artifacts |
| Traceability model | Position in the business-objective-to-evidence chain |
| Consequences | Positive outcomes and costs, stated separately |
| Governance | Which changes to this decision require board review and Program Owner approval |

Not every section applies to every decision; ADR-0001 demonstrates the minimal form, ADR-0002 the full form. Sections that do not apply are omitted rather than left empty.

A superseded decision remains in the repository with its provenance intact. Historical content is preserved through controlled migration, provenance, checksums, supersession records, and exception management, and never silently redefines current architecture: current approved repository artifacts and ADRs take precedence over historical drafts.

## 9. Review gates

No material architectural change is approved without, in order: documented rationale; impact analysis; traceability to controls and standards; human architecture review; and Program Owner approval where the operating model is affected.

| Change type | Gate | Approving authority |
|-------------|------|---------------------|
| Editorial correction to a governed artifact | Document owner review | Document Owner |
| New or amended technical standard | EARB review against principles, controls, and traceability | EARB |
| New or amended ADR | Section 8 lifecycle, in full | EARB; Program Owner where the operating model is affected |
| Change to the four-pillar model, canonical terminology, metadata structure, or cross-volume architecture | EARB review plus operating-model confirmation | EARB and Program Owner |
| Change to governance authority, board charters, decision rights, RACI assignments, escalation procedures, executive reporting, or cross-domain oversight | Multi-role governance review by Executive Leadership, Enterprise Architecture, Security Governance, Internal Audit, and Legal/Compliance where applicable | Executive Leadership |
| New reference implementation | Demonstration of control enforcement, secure architecture, operational ownership, measurable outcomes, traceable evidence, and human review gates | EARB |
| Production security change, emergency change, or release affecting critical assets | CAB review with security representation | CAB |

Confirmation at the operating-model gate requires that the four-pillar model remains intact, Volume 10 remains the operational north star, cybersecurity remains cross-domain, AI authority remains bounded, traceability requirements remain enforceable, and historical content does not silently redefine current architecture.

## 10. Exception handling

An exception is an approved, recorded, time-bound deviation from an approved architecture, standard, or pattern. Approving architectural deviations and issuing architectural exceptions are explicit EARB responsibilities and explicit EARB outputs; a deviation that has not been through the board is a defect, not an exception.

Exceptions are recorded with the same fields required of any governance decision (Section 13), and additionally:

- the artifact deviated from, and the specific provision;
- the review date at which the exception is reassessed;
- the implementation owner accountable for remediation or renewal.

Where an exception carries residual risk, the Enterprise Risk Council performs residual risk evaluation and risk acceptance oversight, the Domain Owner is responsible for the submission, and the Enterprise Governance Board is accountable for the risk acceptance review. An exception whose residual risk exceeds approved enterprise tolerance is not granted at council level; it escalates under Section 11. Exception status is visible in executive reporting through overdue approvals, unresolved escalations, and standards awaiting review.

## 11. Escalation

Escalation follows a fixed path: operational issue → Domain Owner → Governance Manager → Architecture, AI, or Risk Council → Enterprise Governance Board → Executive Leadership.

Escalation is mandatory when:

- enterprise risk exceeds approved tolerance;
- regulatory obligations are affected;
- architectural conflicts cannot be resolved;
- AI governance issues impact safety or compliance;
- critical security incidents require executive direction.

A contribution that cannot satisfy its review gate is not rejected silently; it is escalated on this path with its rationale, impact analysis, and the unresolved point stated.

## 12. Governance cadences

| Forum | Frequency |
|-------|-----------|
| Executive Governance Board | Quarterly |
| Enterprise Architecture Review Board | Biweekly |
| AI Governance Council | Monthly |
| Enterprise Risk Council | Monthly |
| Change Advisory Board | Weekly |
| Domain Governance Review | Monthly |
| Executive Cybersecurity Review | Quarterly |

The governance operating model itself is reviewed annually, with a quarterly governance assessment between annual reviews.

## 13. Decision records, reporting, and retention

Every governance decision — including every ADR acceptance, supersession, and exception — records: decision identifier; meeting reference; participants; rationale; alternatives considered; supporting evidence; affected standards; implementation owner; review date; follow-up actions.

Executive reporting presents governance maturity score, board decision backlog, overdue approvals, unresolved escalations, standards awaiting review, ownership coverage, governance participation metrics, and enterprise decision timelines.

Knowledge Memory retains governance decisions, architectural rulings, AI governance determinations, recurring governance issues, board voting history, lessons learned, decision dependencies, and policy evolution history.

Standard governance artifacts generated from these records are the Governance Board Agenda, Governance Decision Register, Executive Briefing Package, RACI Matrix Workbook, Governance KPI Dashboard, Escalation Summary Report, Quarterly Governance Review, and Annual Governance Effectiveness Assessment.

## 14. Requirements on governed artifacts

Every EAODS standard and major artifact shall identify its governing authority, accountable owner, approval workflow, review cadence, and escalation path. Every major artifact shall additionally define, where applicable, stable identifiers, ownership, purpose and scope, dependencies, architecture relationships, governing controls, implementation guidance, operational workflows, evidence and assurance requirements, measurable outcomes, and human review gates. An artifact that names no governing authority and no accountable owner is not governed by this model and is not eligible for acceptance.

## 15. Human review gate

Approval of this governance model requires confirmation by the Enterprise Architecture Review Board and the Program Owner that:

- no governance body, decision authority, RACI assignment, cadence, or escalation trigger has been introduced beyond those in the cited sources;
- the EARB naming reconciliation in Section 2 creates no new body and transfers no authority;
- the four-pillar reservation in ADR-0002 — EARB review plus Program Owner approval — is stated without weakening;
- the ADR lifecycle preserves superseded records rather than deleting them;
- exception handling remains bounded by risk acceptance authority and mandatory escalation.

Because this document defines decision rights, board charters, RACI assignments, escalation procedures, and executive reporting, its adoption additionally passes the multi-role governance review in Section 9: Executive Leadership, Enterprise Architecture, Security Governance, Internal Audit, and Legal/Compliance where applicable.

## Sources and traceability

| Source (repo-relative path) | Contribution |
|-----------------------------|--------------|
| history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v4.17.1-v4.28/EAODS-v4.26-alpha-enterprise-governance-operating-model-and-decision-authority-framework.md (v4.26-alpha, conversation-derived evidence) | Governance objectives (Section 3); governance architecture, body charters and responsibilities (Section 4); SARB responsibilities and outputs read as the EARB charter, and the governance role catalog used for composition (Section 5); decision classification table (Section 6); enterprise RACI matrix (Section 7); multi-role human review gate (Sections 9, 15); architectural deviation and exception authority (Section 10); escalation path and mandatory triggers (Section 11); governance cadence table and annual-with-quarterly review cycle (Section 12); decision log fields, Executive Control Tower reporting, Knowledge Memory retention, and Artifact Factory outputs (Section 13); standing requirements on future standards (Section 14) |
| architecture/adr/ADR-0002-eaods-enterprise-reference-operating-model.md | Reservation of four-pillar, terminology, metadata, and cross-volume change to board review plus Program Owner approval (Sections 2, 5.1, 6, 9); Volume 10 as north star (Section 2); required contribution model (Section 14); full ADR record structure — context, decision, contribution model, traceability, consequences, governance — and the `status`, `date`, `decision_owner`, `scope`, `supersedes`, `related` fields (Section 8.1); structural-risk rationale for explicit decision ownership (Section 1) |
| architecture/adr/ADR-0001-repository-architecture.md | Placement of architecture decisions under `architecture/adr/` (Sections 2, 8); minimal accepted-record form and the baseline front-matter fields (Section 8.1) |
| docs/architecture/ENTERPRISE_OPERATING_MODEL.md (EAODS-ARCH-EOM-001) | Five-step decision and accountability requirements as the ordered review gate (Section 9); operating-model confirmation checklist (Section 9); governed artifact classes and integration points (Section 2); historical lineage, supersession records, and precedence of current artifacts (Section 8.2); reference implementation acceptance criteria (Section 9); principle that architecture decisions are explicit and reviewable (Section 1) |
| docs/architecture/architecture-principles.md (EAODS-ARCH-PRIN-001) | House style — front matter fields, numbered section structure, governed prose and table conventions, human review gate and sources-and-traceability formatting; the approved rendering of the review gate as "Enterprise Architecture Review Board and Program Owner approval" used in the Section 2 naming reconciliation; the escalation-not-silent-rejection formulation (Section 11) |
