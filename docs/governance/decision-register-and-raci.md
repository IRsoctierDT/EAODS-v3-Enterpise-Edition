---
title: EAODS Decision Register and RACI Model
document_id: EAODS-GOV-DEC-001
version: 1.0.0
status: approved
owner: Enterprise Governance Office
review_gate: Enterprise Governance Board and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - EAODS-ARCH-GOV-001
  - EAODS-ARCH-EOM-001
  - ADR-0001
  - ADR-0002
  - history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v4.17.1-v4.28/EAODS-v4.26-alpha-enterprise-governance-operating-model-and-decision-authority-framework.md
---

# EAODS Decision Register and RACI Model

## 1. Purpose

This document defines two of the standard governance artifacts that the EAODS governance operating model requires: the Governance Decision Register and the RACI Matrix Workbook. It specifies what the register records, the fields every register entry carries, the lifecycle an entry moves through, how architecture decision records relate to the register, how supersession is handled without loss of history, and how responsibility and accountability are assigned per governance activity across the four enduring pillars.

It exists because a governance operating model that names bodies and cadences but leaves decisions unrecorded reproduces the condition the v4.26 framework was written to correct: unclear decision ownership, escalation paths that vary between teams, and executive leadership without visibility into unresolved issues. The register is the evidence layer of that model; the RACI model is its assignment layer.

## 2. Scope and governing authority

This document governs the recording of every governance decision taken over the artifact classes that the operating model integrates: the ADR catalog, standards, the control catalog, threat models, runbooks, architecture patterns, the migration corpus, the knowledge graph, reference implementations, and GitHub governance workflows.

Authority is layered and is not restated here in competition with its sources. EAODS v17.3 Volume 10 is the operational north star. ADR-0002 constitutes the four-pillar operating model — Govern, Design, Operate, Build — and reserves material change to it for board review plus Program Owner approval. ADR-0001 places architecture decisions under `architecture/adr/`. The v4.26 Enterprise Governance Operating Model and Decision Authority Framework supplies the governance bodies, decision classification, RACI assignments, decision log requirements, escalation path, and cadence. EAODS-ARCH-GOV-001 applies that framework to architecture work, and this document adopts its reconciliations without amendment — in particular, the Security Architecture Review Board of v4.26 and the EAODS Enterprise Architecture Board of ADR-0002 are one body, referred to throughout as the Enterprise Architecture Review Board (EARB). No new governance body is created by this document.

The Enterprise Governance Office is the document owner of this register specification. Document ownership is the editorial authority defined in the decision classification; it confers no approval authority over the decisions the register records.

## 3. What the decision register records

The register records every governance decision, across all seven decision classes and their single approval authorities.

| Decision class | Approval authority | Recorded in the register |
|----------------|--------------------|--------------------------|
| Editorial | Document Owner | Yes |
| Operational | Domain Owner | Yes |
| Technical architecture | Enterprise Architecture Review Board | Yes, and additionally as an ADR where the decision is material |
| AI governance | AI Governance Council | Yes |
| Enterprise risk | Enterprise Risk Council | Yes |
| Enterprise policy | Enterprise Governance Board | Yes |
| Strategic investment | Executive Leadership | Yes |

Every decision carries exactly one approval authority. Consultation does not transfer authority, and a register entry that names more than one approving authority is incomplete rather than jointly approved. Two overlays qualify this without dividing it: a technical architecture decision that materially alters the four-pillar model, canonical terminology, metadata structure, or cross-volume architecture additionally requires Program Owner approval under ADR-0002, and a technical architecture decision touching AI authority, autonomous capability, or model usage is consulted with the AI Governance Council, whose own approvals remain its authority.

Three categories of entry are recorded in addition to ordinary decisions: ADR acceptances, supersessions, and exceptions. All three carry the full field set in Section 4.

## 4. Register record structure

Each register entry carries the decision log fields required of every governance decision, together with the traceability fields the operating model requires of governed artifacts. No entry is complete until every applicable field is populated; fields that do not apply are omitted rather than left empty.

| Field | Content | Source of the requirement |
|-------|---------|---------------------------|
| Decision identifier | Stable identifier for the decision, assigned at the point of record | v4.26 decision log; ADR-0002 stable identifiers |
| Meeting reference | The forum session at which the disposition was taken | v4.26 decision log |
| Participants | Seats present and voting at that session | v4.26 decision log |
| Decision class | One of the seven classes in Section 3 | v4.26 decision classification |
| Approval authority | The single body or role that approved, plus any Program Owner overlay applied | v4.26; ADR-0002 |
| Rationale | Documented reasoning for the decision | v4.26; EAODS-ARCH-EOM-001 |
| Alternatives considered | Options evaluated and not taken | v4.26 decision log |
| Supporting evidence | Impact analysis and traceability to controls and standards | v4.26; EAODS-ARCH-EOM-001 |
| Affected standards | Standards, controls, patterns, runbooks, or implementations changed | v4.26 decision log |
| Pillar affected | The pillar or pillars the decision strengthens | ADR-0002 contribution model |
| Implementation owner | The party accountable for carrying the decision into effect | v4.26 decision log |
| Review date | The date at which the decision is reassessed | v4.26 decision log |
| Follow-up actions | Obligations placed on downstream artifacts | v4.26 decision log; ADR-0002 |
| Supersession link | The earlier entry replaced, or the later entry that replaced this one | EAODS-ARCH-GOV-001; EAODS-ARCH-EOM-001 |

Identifier assignment is a register function. This specification defines the field and its stability requirement; it does not allocate identifier values and contains no example identifiers, so that no token in this document can be mistaken for an allocated record.

## 5. Register lifecycle

An entry moves through five states. The states align with the ADR lifecycle in EAODS-ARCH-GOV-001 and extend it to the non-architecture decision classes.

| State | Entry condition | Authority | Exit condition |
|-------|----------------|-----------|----------------|
| Proposed | A decision is required and the class in Section 3 is identified | Proposer, with the accountable Domain or Platform Owner | Rationale, impact analysis, and traceability to controls and standards are documented |
| Under review | The draft entry is complete | The approval authority for the class, consulting other councils as the subject requires | A disposition is recorded: approve, revise, reject, or escalate |
| Approved | Disposition is approve, and Program Owner approval is obtained where the operating model is affected | The approval authority, and the Program Owner where applicable | All Section 4 fields populated; implementation owner and review date set |
| In effect | The decision is being implemented | Implementation owner | Follow-up actions closed; the decision is retained in Knowledge Memory |
| Superseded | A later approved decision replaces this one | The same authority and gates that applied to the original approval | Supersession link recorded in both entries; the earlier entry preserved |

A proposal that cannot satisfy its review gate is not rejected silently. It is escalated on the path in Section 13 with its rationale, impact analysis, and the unresolved point stated.

## 6. Where architecture decision records fit

The ADR catalog is not a parallel register. It is the long-form expression of the technical architecture class, held under `architecture/adr/` per ADR-0001, and every ADR acceptance and supersession is also a register entry. The register carries the decision; the ADR carries the reasoning, the traceability model, and the consequences at the length the decision warrants.

| Register field | Expression in an accepted ADR |
|----------------|------------------------------|
| Decision identifier | The record identifier in `title`, and the record's path under `architecture/adr/` |
| Meeting reference | The EARB disposition recorded at the review stage |
| Participants | The board seats present at that review |
| Decision class | Technical architecture, with the Program Owner overlay where the operating model is affected |
| Rationale | The Context and Decision sections |
| Alternatives considered | Alternatives evaluated at the review stage |
| Supporting evidence | Impact analysis and the traceability model, from business objective through to continuous assurance evidence |
| Affected standards | The `related` field and the standards named in the review |
| Pillar affected | The pillar the contribution strengthens, per ADR-0002 |
| Implementation owner | `decision_owner`, where the accountable owner also carries the work; otherwise recorded separately in the register entry |
| Review date | Recorded in the register entry. The accepted-record structure documented in EAODS-ARCH-GOV-001 carries `date` as the date of acceptance and does not define a separate review-date field, so the register is the authoritative location for it |
| Follow-up actions | The required contribution model and the Governance section of the record |
| Supersession link | The `supersedes` field |

Minor decisions are recorded in the register alone. A decision is promoted to an ADR when it is a material architectural change — that is, when it requires documented rationale, impact analysis, traceability to controls and standards, human architecture review, and, where the operating model is affected, Program Owner approval.

## 7. Supersession and historical lineage

Supersession replaces the authority of a decision, never its record. A superseding entry names the earlier entry in its supersession link; the earlier entry is marked superseded and retained with its provenance intact. Records are not deleted from the register.

Historical EAODS content is retained through controlled migration, provenance, checksums, supersession records, and exception management. Current approved repository artifacts and ADRs take precedence over historical drafts, and no historical record silently redefines current architecture. A register entry sourced from historical material records that provenance in its supporting evidence field and remains subordinate to the current approved decision on the same subject.

## 8. Exceptions and risk acceptances in the register

An exception is an approved, recorded, time-bound deviation from an approved architecture, standard, or pattern. Approving architectural deviations and issuing architectural exceptions are explicit EARB responsibilities and explicit EARB outputs; a deviation that has not been through the board is a defect, not an exception, and does not become one by being entered in the register.

Exception entries carry the Section 4 fields and additionally name the artifact deviated from and the specific provision, the review date at which the exception is reassessed, and the implementation owner accountable for remediation or renewal.

Where an exception carries residual risk, the assignment follows the risk acceptance review row of the enterprise RACI matrix as reconciled in EAODS-ARCH-GOV-001: the Enterprise Risk Council performs residual risk evaluation and risk acceptance oversight, the Domain Owner is responsible for the submission, and the Enterprise Governance Board is accountable for the review. An exception whose residual risk exceeds approved enterprise tolerance is not granted at council level and escalates under Section 13.

## 9. The RACI model and its rules

Assignments use four values: **R** — Responsible; **A** — Accountable; **C** — Consulted; **I** — Informed.

Three rules bound their use in EAODS:

1. Exactly one body or role is Accountable for an activity. Where the enterprise matrix and the decision classification appear to differ, the classification names the approving authority and the matrix names the accountability for the governance activity around it; both hold, and neither is amended here.
2. Consulted status confers no approval authority and no veto. A council consulted on another council's decision retains authority only over its own decision class.
3. Internal Audit participates as independent assurance and is not an approving authority for the decisions it reviews.

The enterprise RACI matrix in the v4.26 framework names five columns — EGB, the architecture board, AIGC, Domain Owner, and Operations. The Change Advisory Board, Executive Leadership, Platform Owner, and Program Owner appear elsewhere in that framework and in ADR-0002 as authorities and coordinating bodies, but they are not columns in that matrix, and this document does not add them to it. Their involvement is stated in prose alongside the pillar tables rather than converted into assignments.

## 10. Enterprise RACI baseline

The following is the normative baseline. The pillar views in Section 11 reproduce rows from it and introduce no assignment that does not appear here.

| Activity | EGB | EARB | AIGC | Domain Owner | Operations |
|----------|-----|------|------|--------------|------------|
| Policy approval | A | C | C | I | I |
| Architecture approval | I | A | C | C | I |
| AI governance decisions | C | C | A | I | I |
| Operational implementation | I | C | C | A | R |
| Risk acceptance review | A | C | C | R | I |
| Compliance assessment | C | C | C | R | A |

## 11. RACI by pillar

Each governance activity is exercised within one or more of the four pillars. An activity that appears under two pillars is the same activity with the same assignment, viewed from two pillars, not a second assignment.

### 11.1 Govern

Govern defines policy, ownership, risk, controls, compliance, decision rights, and assurance. The activities exercised here are policy approval, risk acceptance review, and compliance assessment, together with the editorial decisions held by Document Owners.

| Activity | EGB | EARB | AIGC | Domain Owner | Operations |
|----------|-----|------|------|--------------|------------|
| Policy approval | A | C | C | I | I |
| Risk acceptance review | A | C | C | R | I |
| Compliance assessment | C | C | C | R | A |

Enterprise policy decisions are approved by the Enterprise Governance Board and enterprise risk decisions by the Enterprise Risk Council. Register entries in this pillar are the primary input to the governance maturity and ownership-coverage reporting in Section 14.

### 11.2 Design

Design defines reference architectures, patterns, interfaces, threat models, and engineering standards. The activities exercised here are architecture approval and, where a design determines AI authority or model usage, AI governance decisions.

| Activity | EGB | EARB | AIGC | Domain Owner | Operations |
|----------|-----|------|------|--------------|------------|
| Architecture approval | I | A | C | C | I |
| AI governance decisions | C | C | A | I | I |
| Risk acceptance review | A | C | C | R | I |

The EARB is accountable for architecture approval and produces architecture decisions, approved reference architectures, technology guidance, and architectural exceptions. Where the change materially alters the four-pillar model, canonical terminology, metadata structure, or cross-volume architecture, EARB approval is not final and the Program Owner approves in addition. Risk acceptance review appears in this pillar because architectural exceptions carrying residual risk are routed under Section 8; the assignment is unchanged.

### 11.3 Operate

Operate defines platform operations, SOC and NOC coordination, SRE, telemetry, incident command, resilience, and continual improvement. The activities exercised here are operational implementation and compliance assessment.

| Activity | EGB | EARB | AIGC | Domain Owner | Operations |
|----------|-----|------|------|--------------|------------|
| Operational implementation | I | C | C | A | R |
| Compliance assessment | C | C | C | R | A |

Compliance assessment appears in both Govern and Operate: the obligation is defined in Govern, while the enterprise matrix makes Operations accountable for the assessment itself. Production security changes, emergency changes, configuration governance, release approvals, and deployment scheduling are coordinated by the Change Advisory Board, with security representatives participating in reviews affecting critical assets; that coordination is recorded in the register as an operational decision under Domain Owner authority.

### 11.4 Build

Build defines reference implementations, automation, agents, secure delivery, validation, and engineering guidance. The activity exercised here is operational implementation, executed by delivery teams under the same assignment as in Operate.

| Activity | EGB | EARB | AIGC | Domain Owner | Operations |
|----------|-----|------|------|--------------|------------|
| Operational implementation | I | C | C | A | R |
| Architecture approval | I | A | C | C | I |

Architecture approval appears in this pillar because a new reference implementation passes an EARB gate: it must demonstrate control enforcement, secure architecture, operational ownership, measurable outcomes, traceable evidence, and human review gates before acceptance. Platform Owners hold technical execution within platform scope and are the usual implementation owners on Build entries.

## 12. Cross-pillar overlays

Two overlays apply to register entries in every pillar.

Cybersecurity Domain 03 operates across all four pillars and carries Zero Trust, identity and access governance, threat modeling, detection engineering, incident response, supply-chain security, AI security, continuous assurance, and standards alignment. A register entry touching any of these records the affected area in its supporting evidence.

AI agents and automation must be least privileged, observable, auditable, bounded by policy, subject to human approval for material actions, and traceable to owners, controls, and evidence. A register entry that grants, widens, or automates an authority exercised by an agent is an AI governance decision consulted with or approved by the AI Governance Council according to Section 3, and human authority remains accountable for material decisions.

## 13. Escalation of unresolved entries

Escalation follows a fixed path: operational issue → Domain Owner → Governance Manager → Architecture, AI, or Risk Council → Enterprise Governance Board → Executive Leadership. Each escalation step is itself a register entry, carrying the unresolved point and the evidence already assembled.

Escalation is mandatory when enterprise risk exceeds approved tolerance, regulatory obligations are affected, architectural conflicts cannot be resolved, AI governance issues impact safety or compliance, or critical security incidents require executive direction.

## 14. Cadence, reporting, and retention

Register entries are dispositioned at the forums on the established cadence: Executive Governance Board quarterly, Enterprise Architecture Review Board biweekly, AI Governance Council monthly, Enterprise Risk Council monthly, Change Advisory Board weekly, Domain Governance Review monthly, and Executive Cybersecurity Review quarterly. The governance operating model is reviewed annually, with a quarterly governance assessment between annual reviews.

Executive reporting draws directly on the register and presents governance maturity score, board decision backlog, overdue approvals, unresolved escalations, standards awaiting review, ownership coverage, governance participation metrics, and enterprise decision timelines. Each of these is a view over register entries rather than a separately maintained figure.

Knowledge Memory retains governance decisions, architectural rulings, AI governance determinations, recurring governance issues, board voting history, lessons learned, decision dependencies, and policy evolution history. The register is the source of record from which that retention is populated.

## 15. Conformance requirements

A register entry conforms when it names a single approval authority, populates every applicable Section 4 field, identifies the pillar it strengthens, links to its supporting evidence and affected standards, and names an implementation owner and a review date.

An artifact governed by a register entry conforms when it identifies its governing authority, accountable owner, approval workflow, review cadence, and escalation path. An artifact that names no governing authority and no accountable owner is not governed by this model and is not eligible for acceptance.

## 16. Human review gate

Approval of this document requires confirmation by the Enterprise Governance Board and the Program Owner that:

- no governance body, decision authority, RACI assignment, cadence, escalation trigger, or reporting metric has been introduced beyond those in the cited sources;
- the enterprise RACI baseline in Section 10 is reproduced without alteration, and the pillar views in Section 11 add no assignment absent from it;
- every decision retains exactly one approval authority, with the ADR-0002 Program Owner overlay stated without weakening;
- the register preserves superseded entries rather than deleting them, and historical content does not silently redefine current architecture;
- exception handling remains bounded by risk acceptance authority and mandatory escalation;
- no identifier values are allocated by this specification.

Because this document defines decision rights, RACI assignments, escalation procedures, and executive reporting, its adoption additionally passes multi-role governance review by Executive Leadership, Enterprise Architecture, Security Governance, Internal Audit, and Legal/Compliance where applicable.

## 17. Approval

Approved by the Program Owner on 2026-08-03, closing the Human governance
review gate of epic #26.

| Field | Value |
|---|---|
| Approving authority | Program Owner (Ivan Rozenblad) |
| Approval date | 2026-08-03 |
| Gate closed | Epic #26 — Human governance review |
| Basis | Independent four-lens defect review (34 candidates, 8 confirmed and fixed in PR #65) preceding sign-off |
| Status effect | `proposed` → `approved`; this document is enforceable governance |

Subsequent material change re-enters the lifecycle at Section 6 and requires
re-approval; it does not inherit this one.

## 18. Sources and traceability

| Source (repo-relative path) | Contribution |
|-----------------------------|--------------|
| history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v4.17.1-v4.28/EAODS-v4.26-alpha-enterprise-governance-operating-model-and-decision-authority-framework.md (v4.26-alpha, conversation-derived evidence) | Purpose and the failure condition the model corrects (Section 1); governance bodies, charters, responsibilities, and outputs, including SARB outputs read as EARB outputs and the CAB coordination scope (Sections 2, 8, 11.2, 11.3); decision classification and single approval authority (Section 3); decision log fields (Section 4); governance role catalog including Document Owner, Domain Owner, Platform Owner, Governance Manager, and Internal Audit (Sections 2, 9, 11.4); enterprise RACI matrix and legend (Sections 9, 10, 11); escalation path and mandatory triggers (Section 13); governance cadence table and annual-with-quarterly review cycle (Section 14); Executive Control Tower reporting fields (Section 14); Knowledge Memory retention set (Section 14); Artifact Factory outputs naming the Governance Decision Register and RACI Matrix Workbook (Section 1); standing requirements on governed artifacts (Section 15); multi-role human review gate (Section 16) |
| docs/architecture/architecture-governance-model.md (EAODS-ARCH-GOV-001) | EARB naming reconciliation adopted without amendment (Section 2); ADR lifecycle stages and their entry, authority, and exit conditions, extended to all decision classes (Section 5); accepted-record structure and front-matter fields used for the ADR-to-register field mapping, including `date` as the acceptance date (Section 6); preservation of superseded records with provenance intact (Section 7); exception definition, additional exception fields, and the residual-risk reconciliation of the risk acceptance review row (Sections 8, 11.2); escalation-not-silent-rejection formulation (Section 5); Internal Audit as non-approving assurance (Section 9); house style for numbered sections, governed prose, tables, human review gate, and this traceability table |
| docs/architecture/ENTERPRISE_OPERATING_MODEL.md (EAODS-ARCH-EOM-001) | Governed artifact classes and integration points defining register scope (Section 2); four-pillar definitions of Govern, Design, Operate, and Build used to allocate activities (Section 11); five-step decision and accountability requirements as the promotion test for ADRs (Sections 4, 6); historical lineage through controlled migration, provenance, checksums, supersession records, and exception management, and the precedence of current approved artifacts (Section 7); reference implementation acceptance criteria (Section 11.4); Cybersecurity Domain 03 as cross-pillar and the AI operating boundaries (Section 12); principle that human authority remains accountable for material decisions (Section 12); house style for front matter and section structure |
| architecture/adr/ADR-0002-eaods-enterprise-reference-operating-model.md | Constitution of the four-pillar model and the requirement that every contribution strengthen at least one pillar, giving the pillar-affected register field (Sections 2, 4, 11); reservation of four-pillar, terminology, metadata, and cross-volume change to board review plus Program Owner approval (Sections 3, 11.2); stable identifiers and the required contribution model behind the identifier and follow-up-action fields (Section 4); traceability model from business objective to continuous assurance evidence (Section 6); Volume 10 as the operational north star (Section 2) |
| architecture/adr/ADR-0001-repository-architecture.md | Placement of architecture decision records under `architecture/adr/`, fixing where the ADR expression of a register entry lives (Sections 2, 6) |
