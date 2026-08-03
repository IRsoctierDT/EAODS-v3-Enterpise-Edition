---
title: EAODS Governance Manual
document_id: EAODS-GOV-MAN-001
version: 1.0.0
status: proposed
owner: Enterprise Governance Office
review_gate: Enterprise Governance Board and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - EAODS-ARCH-GOV-001
  - EAODS-ARCH-EOM-001
  - EAODS-GOV-V10-001
  - ADR-0001
  - ADR-0002
  - STD-0001
  - STD-0002
  - GOVERNANCE.md
  - history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v4.17.1-v4.28/EAODS-v4.26-alpha-enterprise-governance-operating-model-and-decision-authority-framework.md
---

# EAODS Governance Manual

## 1. Purpose

This manual is the consolidated statement of how EAODS Enterprise Edition is governed. It names the governing bodies and the authority each one holds, states the hierarchy by which a decision reaches a single approval authority, defines what may and may not be delegated down that hierarchy, fixes the escalation path and the conditions that make escalation mandatory, records the cadence at which each forum sits, and binds all of it to the four enduring pillars of the operating model.

It exists because EAODS is an Enterprise Reference Operating Model rather than a static documentation repository, and sustaining it requires organizational decision rights, governance forums, accountability, escalation paths, approval authorities, and operational oversight to be written down in one place. Where decision ownership is unclear and escalation paths differ between teams, executive leadership loses visibility into unresolved issues; this manual is the corrective.

## 2. Scope and relationship to adjacent documents

This manual governs the governance layer itself: bodies, authorities, delegation, escalation, cadence, decision records, and reporting. It applies across every artifact class the operating model integrates — the ADR catalog, standards, the control catalog, threat models, runbooks, architecture patterns, the migration corpus, the knowledge graph, reference implementations, and GitHub governance workflows.

Three boundaries keep this manual from duplicating or contradicting its siblings:

1. **The Enterprise Architecture Review Board charter is not restated here.** The EARB charter, composition, seat-by-seat responsibilities, review gates, ADR lifecycle, and exception handling are defined in `docs/architecture/architecture-governance-model.md` (EAODS-ARCH-GOV-001). This manual cites that document as the authority for architecture decision-making and does not re-derive it.
2. **The operating model is not restated here.** The four pillars, enterprise domains, AI operating boundaries, and success measures are defined in `docs/architecture/ENTERPRISE_OPERATING_MODEL.md` (EAODS-ARCH-EOM-001). Section 11 binds governance to those pillars; it does not redefine them.
3. **Repository-level obligations remain in force.** `GOVERNANCE.md` reserves final publication authority to the repository owner, requires documented human review for material architecture, security, governance, and commercialization changes, requires every normative framework artifact to carry YAML front matter, purpose, enterprise workflow, integration points, QA checklist, and a human review gate, and requires significant design decisions to be documented under `architecture/adr/`. Nothing in this manual relaxes those obligations.

EAODS v17.3 Volume 10 remains the operational north star. Current approved repository artifacts and ADRs take precedence over historical drafts.

## 3. Governance objectives

The governance operating model shall:

- establish clear accountability;
- eliminate decision ambiguity;
- standardize governance workflows;
- provide executive oversight;
- accelerate risk-informed decision making;
- ensure policy consistency;
- improve cross-functional collaboration;
- support enterprise scalability.

## 4. Governing bodies and their authorities

Authority descends from Executive Leadership through the Enterprise Governance Board, which sits above three peer councils — the Enterprise Architecture Review Board, the AI Governance Council, and the Enterprise Risk Council — and from those councils through Domain Owners, Platform Owners, and Operational Teams. The Change Advisory Board coordinates change across that descent rather than sitting within it.

| Body | Charter position | Authority held |
|------|-----------------|----------------|
| Executive Leadership | Strategic oversight | Approves strategic investment; approves changes to governance authority, board charters, decision rights, RACI assignments, escalation procedures, executive reporting, and cross-domain oversight; receives mandatory escalations |
| Enterprise Governance Board (EGB) | Highest decision-making authority for EAODS governance | Approves enterprise cybersecurity strategy and new governance standards; resolves cross-domain conflicts; reviews enterprise risk posture; authorizes strategic initiatives; oversees EAODS maturity progression; accountable for risk acceptance review |
| Enterprise Architecture Review Board (EARB) | Architecture authority | Reviews security architecture; approves architectural deviations; validates security patterns; reviews technical standards; assesses technology risks. Charter, composition, and lifecycle are held in EAODS-ARCH-GOV-001 |
| AI Governance Council (AIGC) | AI authority | Governs AI systems; reviews model usage; approves AI tooling, AI deployment standards, model lifecycle policies, AI governance controls, and AI risk treatment strategies; monitors AI operational risk; oversees prompt governance; evaluates autonomous capabilities |
| Enterprise Risk Council | Risk authority | Enterprise risk review; residual risk evaluation; risk acceptance oversight; KRI monitoring; executive risk reporting |
| Change Advisory Board (CAB) | Change coordination | Coordinates production security changes, emergency changes, configuration governance, release approvals, and deployment scheduling. Security representatives participate in reviews affecting critical assets |
| Domain Owners | Domain implementation | Own operational decisions within a domain; responsible for risk acceptance submissions and compliance assessment inputs |
| Platform Owners | Technical execution | Implement approved architecture within platform scope |
| Operational Teams | Delivery | Responsible for operational implementation and accountable for compliance assessment execution |
| Program Owner | Final approval for operating-model change | Approves changes that materially alter the four-pillar model, canonical terminology, metadata structure, or cross-volume architecture (ADR-0002) |
| Repository Owner | Publication authority | Retains final publication authority over the repository (`GOVERNANCE.md`) |

**Naming notes.** The v4.26 framework names the architecture authority the Security Architecture Review Board; EAODS-ARCH-GOV-001 reconciles that name to the Enterprise Architecture Review Board, and this manual follows that reconciliation. The same framework's cadence table renders the board-level forum as "Executive Governance Board" while its bodies section names the body "Enterprise Governance Board"; both renderings are preserved in Section 10, and no separate body is created by either. Neither note creates a body or transfers authority.

## 5. Governance roles

Bodies are staffed from a single enterprise role catalog. Each role carries one primary responsibility, and that responsibility travels with the role into whichever forum it sits on.

| Role | Primary responsibility |
|------|-----------------------|
| Executive Sponsor | Strategic oversight |
| Chief Information Security Officer | Enterprise security leadership |
| Enterprise Architect | Architecture governance |
| Security Governance Manager | Standards lifecycle |
| Domain Owner | Domain implementation |
| Platform Owner | Technical execution |
| Risk Manager | Risk governance |
| Compliance Lead | Regulatory oversight |
| Operations Manager | Operational delivery |
| Internal Audit | Independent assurance |

Internal Audit participates as independent assurance and is not an approving authority for the work it reviews.

## 6. Decision hierarchy

Every decision carries exactly one approval authority. Consultation informs a decision; it does not transfer authority for it.

| Decision type | Approval authority |
|---------------|--------------------|
| Editorial | Document Owner |
| Operational | Domain Owner |
| Technical architecture | Enterprise Architecture Review Board |
| AI governance | AI Governance Council |
| Enterprise risk | Enterprise Risk Council |
| Enterprise policy | Enterprise Governance Board |
| Strategic investment | Executive Leadership |

Four overlays sit above this table and are cumulative with it:

1. **Operating-model reservation.** A decision that materially alters the four-pillar model, canonical terminology, metadata structure, or cross-volume architecture is not final on council approval alone; it additionally requires Program Owner approval (ADR-0002).
2. **Governance-layer reservation.** A change to governance authority, board charters, decision rights, RACI assignments, escalation procedures, executive reporting, or cross-domain oversight passes multi-role review by Executive Leadership, Enterprise Architecture, Security Governance, Internal Audit, and Legal/Compliance where applicable, before approval and publication.
3. **AI consultation.** A decision that changes AI authority, autonomous capability, or model usage is consulted with the AI Governance Council; the council's own approvals remain its authority rather than the deciding body's.
4. **Publication.** Approval is not publication. Material architecture, security, governance, and commercialization changes require documented human review, and the repository owner retains final publication authority.

Material architectural changes reach their authority only after documented rationale, impact analysis, traceability to controls and standards, human architecture review, and Program Owner approval where the operating model is affected. The gate-by-gate application of that sequence is held in EAODS-ARCH-GOV-001.

## 7. Accountability matrix

| Activity | EGB | EARB | AIGC | Domain Owner | Operations |
|----------|-----|------|------|--------------|------------|
| Policy approval | A | C | C | I | I |
| Architecture approval | I | A | C | C | I |
| AI governance decisions | C | C | A | I | I |
| Operational implementation | I | C | C | A | R |
| Risk acceptance review | A | C | C | R | I |
| Compliance assessment | C | C | C | R | A |

Legend: R — Responsible; A — Accountable; C — Consulted; I — Informed.

## 8. Delegation

Delegation moves execution downward and leaves accountability where the matrix in Section 7 places it.

| From | To | What is delegated | What is retained |
|------|----|-------------------|------------------|
| Enterprise Governance Board | Councils | Domain-specific approval within the council's decision type | Enterprise policy approval, cross-domain conflict resolution, enterprise risk posture, maturity progression |
| Councils | Domain Owners | Operational decisions inside an approved architecture, standard, or control | Architecture, AI governance, and enterprise risk approval authority |
| Domain Owners | Platform Owners | Technical execution of approved architecture within platform scope | Domain implementation accountability and risk acceptance submissions |
| Platform Owners | Operational Teams | Operational implementation and delivery | Technical execution accountability |
| Human authority | AI agents and automation | Bounded, least-privileged, observable, auditable execution within policy | Approval of material actions; ownership; control and evidence traceability |

Four limits bound every delegation:

1. Human authority remains accountable for material decisions. Delegation to AI agents or automation never converts a material action into an unapproved one; such actions remain subject to human approval gates.
2. Delegated authority may not exceed the delegating body's own authority, and may not reach a decision type the hierarchy assigns elsewhere.
3. The reservations in Section 6 are not delegable. Operating-model change, governance-layer change, and publication authority stay with the Program Owner, Executive Leadership, and the repository owner respectively.
4. A delegated decision is still a governed decision: it is recorded under Section 12 with a named implementation owner, and it remains visible to the accountable body through executive reporting.

An artifact or activity that names no governing authority and no accountable owner is not delegated; it is ungoverned, and is not eligible for acceptance.

## 9. Escalation

Escalation follows a fixed path: operational issue → Domain Owner → Governance Manager → Architecture, AI, or Risk Council → Enterprise Governance Board → Executive Leadership.

Escalation is mandatory when:

- enterprise risk exceeds approved tolerance;
- regulatory obligations are affected;
- architectural conflicts cannot be resolved;
- AI governance issues impact safety or compliance;
- critical security incidents require executive direction.

A contribution that cannot satisfy its approval authority is not rejected silently. It moves up this path carrying its rationale, its impact analysis, and a plain statement of the unresolved point. Escalations that remain open are reported to Executive Leadership under Section 13 until they are closed.

## 10. Governance cadences

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

## 11. Binding to the four pillars

Governance is not a pillar beside the others; it is the authority layer each pillar reports into. The table states, for each pillar, what that pillar produces, which body holds approval, and what the pillar must show to be approved.

| Pillar | Pillar scope | Approval authority | Binding obligation |
|--------|-------------|--------------------|--------------------|
| Govern | Policy, ownership, risk, controls, compliance, decision rights, assurance | Enterprise Governance Board, with the Enterprise Risk Council for risk acceptance oversight | Policy and governance standards approved at board level; controls map to evidence, implementation, and operations |
| Design | Reference architectures, patterns, interfaces, threat models, engineering standards | Enterprise Architecture Review Board, per EAODS-ARCH-GOV-001 | Architecture decisions explicit, reviewable, and recorded as ADRs under `architecture/adr/`; standards reviewed against principles, controls, and traceability |
| Operate | Platform operations, SOC/NOC coordination, SRE, telemetry, incident command, resilience, continual improvement | Domain Owners, with CAB coordination for production and emergency change | Services carry named owners and measurable reliability objectives; operational workflows are measurable and reported |
| Build | Reference implementations, automation, agents, secure delivery, validation, engineering guidance | Enterprise Architecture Review Board, consulting the AI Governance Council where agents or model usage are involved | Reference implementations demonstrate control enforcement, secure architecture, operational ownership, measurable outcomes, traceable evidence, and human review gates |

Two properties cut across all four pillars and are governed at every gate rather than at one. Cybersecurity Domain 03 operates across all four pillars, spanning Zero Trust, identity and access governance, threat modeling, detection engineering, incident response, supply-chain security, AI security, continuous assurance, and standards alignment. AI authority is bounded everywhere it appears: agents and automation must be least privileged, observable, auditable, bounded by policy, subject to human approval for material actions, and traceable to owners, controls, and evidence.

Governance also binds the enterprise domains — governance and risk, enterprise architecture, Cybersecurity Domain 03, platform engineering, Site Reliability Engineering, AI governance and operations, data and telemetry, continuous assurance, and reference implementations — each of which reports into the pillar authority above through its Domain Owner.

## 12. Decision register

Governance decisions are held in a decision register. The register is a record structure, not an identifier scheme; identifiers are assigned by the register's owning body at the point of entry.

**Record fields.** Every governance decision — including every architecture decision acceptance, supersession, and exception — records: decision identifier; meeting reference; participants; rationale; alternatives considered; supporting evidence; affected standards; implementation owner; review date; follow-up actions.

**Record lifecycle.**

| Stage | Entry condition | Authority | Exit condition |
|-------|----------------|-----------|----------------|
| Raise | A decision is required and its type is classified under Section 6 | Proposer, with the accountable owner | Draft record complete with rationale, alternatives, and supporting evidence |
| Review | Draft record complete | The approval authority for that decision type, consulting others as the subject requires | Disposition recorded: approve, revise, reject, or escalate |
| Approve | Disposition is approve, and any Section 6 overlay is satisfied | Approval authority and, where applicable, Program Owner and Executive Leadership | Record entered with all fields, implementation owner named, review date set |
| Review-date reassessment | The recorded review date is reached | The body that approved the decision | Decision reaffirmed, amended under a new record, or superseded |
| Supersede | A later approved decision replaces an earlier one | Same authority, under the same overlays | Superseding record names the earlier decision; the earlier record is preserved, not deleted |

Architecture decisions run this lifecycle in the specific form defined by EAODS-ARCH-GOV-001, under `architecture/adr/`. Historical records are retained through controlled migration, provenance, checksums, supersession records, and exception management, and never silently redefine current architecture.

## 13. Executive reporting and knowledge retention

The Executive Control Tower presents governance maturity score, board decision backlog, overdue approvals, unresolved escalations, standards awaiting review, ownership coverage, governance participation metrics, and enterprise decision timelines.

Knowledge Memory retains governance decisions, architectural rulings, AI governance determinations, recurring governance issues, board voting history, lessons learned, decision dependencies, and policy evolution history.

The Artifact Factory generates the standard governance artifact set: Governance Board Agenda, Governance Decision Register, Executive Briefing Package, RACI Matrix Workbook, Governance KPI Dashboard, Escalation Summary Report, Quarterly Governance Review, and Annual Governance Effectiveness Assessment.

## 14. Requirements on governed artifacts

Every EAODS standard and major artifact shall identify its governing authority, accountable owner, approval workflow, review cadence, and escalation path. Every normative framework artifact shall additionally carry YAML front matter, purpose, enterprise workflow, integration points, a QA checklist, and a human review gate.

This governance framework integrates with the standards that precede it in the source lineage: v4.17–v4.22 for vulnerability management, configuration governance, and security operations; v4.23 for enterprise control ownership; v4.24 for KPI and KRI reporting; and v4.25 for document lifecycle governance. Within this repository it integrates with the ADR catalog, standards STD-0001 and STD-0002, the control catalog, threat models, runbooks, architecture patterns, the migration corpus, the knowledge graph, reference implementations, and GitHub governance workflows.

## 15. Human review gate

Approval of this manual requires confirmation by the Enterprise Governance Board and the Program Owner that:

- no governance body, role, decision authority, RACI assignment, cadence, escalation trigger, or reporting metric has been introduced beyond those in the cited sources;
- the EARB charter is referenced to EAODS-ARCH-GOV-001 and not restated, redefined, or extended here;
- the naming notes in Section 4 create no new body and transfer no authority;
- the reservations in Section 6 — Program Owner approval for operating-model change, multi-role review for governance-layer change, and repository-owner publication authority — are stated without weakening;
- delegation in Section 8 moves execution only, and leaves accountability and the non-delegable reservations intact;
- the pillar binding in Section 11 reports into the operating model rather than redefining it, and leaves Volume 10 as the operational north star;
- the decision register in Section 12 preserves superseded records rather than deleting them.

Because this document states governance authority, board charters, decision rights, RACI assignments, escalation procedures, executive reporting, and cross-domain oversight, its adoption additionally passes multi-role governance review by Executive Leadership, Enterprise Architecture, Security Governance, Internal Audit, and Legal/Compliance where applicable, before publication.

## 16. Sources and traceability

| Source (repo-relative path) | Contribution |
|-----------------------------|--------------|
| history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v4.17.1-v4.28/EAODS-v4.26-alpha-enterprise-governance-operating-model-and-decision-authority-framework.md (v4.26-alpha draft, conversation-derived evidence) | Purpose framing of governance as operating model rather than static repository (Section 1); governance objectives (Section 3); governance architecture descent and body charters, responsibilities, deliverables, decision authority, and CAB integration (Section 4); governance role catalog (Section 5); decision classification table (Section 6); enterprise RACI matrix (Section 7); escalation path and mandatory triggers (Section 9); governance cadence table and annual-with-quarterly review cycle (Section 10); decision log fields (Section 12); Executive Control Tower metrics, Knowledge Memory retention, and Artifact Factory outputs (Section 13); standing requirements on future standards and integration with v4.17–v4.25 (Section 14); multi-role human review gate for governance-layer change (Sections 6, 15) |
| docs/architecture/architecture-governance-model.md (EAODS-ARCH-GOV-001) | EARB charter, composition, review gates, ADR lifecycle, and exception handling, referenced rather than restated (Sections 2, 4, 6, 11, 12); SARB-to-EARB naming reconciliation adopted here (Section 4); the principle that consultation does not transfer authority and that exactly one approval authority attaches to each decision (Section 6); AI-consultation overlay (Section 6); escalation-not-silent-rejection formulation (Section 9); the ungoverned-artifact test (Section 8); house style for numbered sections, governed tables, human review gate, and this traceability table |
| docs/architecture/ENTERPRISE_OPERATING_MODEL.md (EAODS-ARCH-EOM-001) | Four-pillar scope statements and pillar binding (Section 11); enterprise domain list (Section 11); operating-model principles on human accountability, named owners with measurable reliability objectives, and controls mapping to evidence (Sections 8, 11); AI operating boundaries (Sections 8, 11); Cybersecurity Domain 03 cross-pillar span (Section 11); reference implementation acceptance criteria (Section 11); five-step material-change requirements (Section 6); Volume 10 as operational north star and precedence of current artifacts over historical drafts (Sections 2, 12); governed artifact classes and integration points (Sections 2, 14); historical lineage handling (Section 12); house style for front matter and section structure |
| GOVERNANCE.md | Repository owner's final publication authority and the separation of approval from publication (Sections 2, 4, 6, 8); documented human review for material architecture, security, governance, and commercialization changes (Sections 2, 6); required elements of every normative framework artifact (Sections 2, 14); placement of significant design decisions under `architecture/adr/` (Sections 2, 11, 12) |
| architecture/adr/ADR-0002-eaods-enterprise-reference-operating-model.md (cited via EAODS-ARCH-GOV-001 and EAODS-ARCH-EOM-001) | Reservation of four-pillar, canonical terminology, metadata structure, and cross-volume change to board review plus Program Owner approval (Sections 4, 6, 8, 15) |
| architecture/adr/ADR-0001-repository-architecture.md (cited via EAODS-ARCH-GOV-001) | Placement of architecture decision records under `architecture/adr/` (Sections 11, 12) |
