---
title: EAODS Incident Command and Major Incident Management
document_id: EAODS-OPS-IC-001
version: 1.0.0
status: proposed
owner: Enterprise Platform Operations Center
review_gate: Platform Engineering Leadership and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - EAODS-ARCH-EOM-001
  - STD-0001
  - STD-0002
  - PAT-0003
  - PAT-0004
  - RUN-0001
  - RUN-0002
  - RUN-0003
  - docs/frameworks/EAODS-v17.3/volume-10-platform-operations.md
  - docs/architecture/architecture-governance-model.md
  - history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v5.0-v6.6/EAODS-v6.6-alpha-enterprise-incident-command-crisis-management-and-cyber-recovery-governance-standard.md
---

# EAODS Incident Command and Major Incident Management

## 1. Purpose

This document defines how an EAODS platform incident is classified, declared, commanded, communicated, recovered, and reviewed. It establishes the command posts and their responsibilities, the severity scale and the criteria that move an event up it, the authority attached to each material incident decision, the reporting obligations that run to executive leadership and external parties, and the post-incident review that converts an incident into governance improvement.

It exists because Volume 10 makes the Enterprise Platform Operations Center (EPOC) the operational authority for platform health, reliability, performance, and continuous improvement, and names incident command among the operational capabilities the operating model expects it to run (EAODS-ARCH-EOM-001). Volume 10 defines who operates the platform; the runbook library defines exactly what is executed under defined conditions. Neither states how command is constituted when an event exceeds a single runbook. This document supplies that layer and nothing below it: procedures already governed by RUN-0001, RUN-0002, and RUN-0003 are referenced, not restated.

## 2. Scope and governing authority

This model applies to any operational event affecting a production platform service that carries a canonical service ownership record under Volume 10, from a routine security event through an enterprise crisis. It governs the command structure, not the engineering procedure.

Authority is layered. EAODS v17.3 Volume 10 is the operational north star and the governing architecture for this document. The v6.6-alpha Enterprise Incident Command, Crisis Management and Cyber Recovery Governance Standard supplies the command architecture, incident classification, command posts, authority matrix, crisis lifecycle, recovery governance, situation reporting, external coordination, exercise framework, and AI boundaries applied here. RUN-0001, RUN-0002, and RUN-0003 remain the executable procedures and are unchanged by this document.

**Command reconciliation.** The v6.6 standard establishes the Enterprise Cyber Incident Command System (ECICS) as a cyber incident command structure under Domain 03. Volume 10 draws the boundary directly: the Enterprise Cyber Command directs cybersecurity operations, while the EPOC governs the operational engineering of the platform itself. This document therefore applies the ECICS command structure to platform incidents under EPOC ownership, and hands direction to the Enterprise Cyber Command where a cyber cause is suspected or confirmed — the transfer point already written into RUN-0001 ("suspected cyber cause → Enterprise Cyber Command before further recovery steps") and RUN-0003 (trust-boundary exposure escalates immediately and is treated as a potential security event). No second command system is created by this reconciliation, and no authority is moved from the Enterprise Cyber Command.

**Naming.** The v6.6 standard names the architecture authority in its review gate the Security Architecture Review Board. Consistent with the approved architecture governance model, this document uses **Enterprise Architecture Review Board (EARB)** for that body. The reconciliation creates no new body.

## 3. Principles

Incident management under this model is risk-driven, command-oriented, evidence-based, policy-governed, transparent, repeatable, continuously measurable, and business-aligned. Platform operations remain service-oriented, measurable, observable, automation-assisted, continuously improving, evidence-driven, resilient, and constitutionally governed, and operational decisions prioritize long-term platform stability over short-term convenience.

Applied to an active incident, these principles carry four standing obligations:

1. Every material decision has exactly one named approving authority (Section 6).
2. Every command post is filled, or its responsibilities are explicitly assumed by a filled post and recorded.
3. Evidence is preserved as the incident runs, not reconstructed after it closes.
4. Human authority remains accountable for declaration, recovery authorization, and external communication (Section 11).

## 4. Severity classification

| Level | Description |
|---|---|
| IC-0 | Security event |
| IC-1 | Minor incident |
| IC-2 | Department incident |
| IC-3 | Enterprise incident |
| IC-4 | Major business disruption |
| IC-5 | Enterprise crisis |

Classification is assigned at declaration and reassessed at every situation report. Escalation criteria are operational impact, regulatory obligations, business criticality, customer impact, safety implications, and executive visibility. A level is set by the highest criterion met, not by an average across them.

Two Volume 10 inputs qualify the assessment. The affected service's reliability classification and availability target, recorded in its canonical service ownership record (the canonical example being `SVC-00387`), establish business criticality without re-deriving it during the incident. Where the deviation is a control failure, the registered control (the canonical example being `EAODS-CTRL-000184`) and its evidence requirement establish the regulatory dimension, and RUN-0003 governs the response.

Severity is a command signal, not a routing table. A single-service condition already covered by an approved runbook is handled by that runbook (Section 9); classification determines who commands, who is briefed, and at what cadence.

## 5. Command posts and responsibilities

| Post | Responsible for |
|---|---|
| Incident Commander | Overall incident direction; operational prioritization; executive coordination; resource allocation; strategic decision tracking |
| Operations Section lead | Containment; eradication; technical response; recovery execution |
| Planning Section lead | Situational awareness; action plans; dependency analysis; forecast development |
| Communications Section lead | Executive briefings; stakeholder coordination; regulatory communication support; internal status updates |
| Recovery Coordinator | Restoration sequencing; validation; resilience verification; transition to normal operations |

The command architecture runs from Executive Leadership through the Cyber Executive Steering Group to the Incident Commander, who directs the Operations, Planning, and Communications Sections; recovery coordination sits beneath the sections, and its output feeds the Enterprise Knowledge Graph and the Executive Control Tower.

### 5.1 Record-keeping duty

The sources read for this document — the v6.6-alpha standard, Volume 10, and RUN-0001 through RUN-0003 — define no separate scribe or note-taker post. The record-keeping obligations those sources do impose (the incident command log, the executive situation report, and the crisis decision register described in Section 10) are therefore assigned to filled posts rather than to a new role: the Planning Section maintains the command log and the decision register as an extension of situational awareness, and the Communications Section owns the situation report as an extension of executive briefing. An incident that cannot staff those duties within the filled posts escalates the staffing gap to the Incident Commander, who reallocates resources under Section 5.

### 5.2 Relationship to service ownership

Command posts are incident-scoped; service ownership is permanent. Volume 10 requires every production service to identify a business owner, an engineering owner, an operational owner, an executive sponsor, a recovery authority, an architecture authority, and an assurance owner, continuously documented. Command posts engage those owners rather than replacing them: the Recovery Coordinator works with the service owner on production recovery, the Incident Commander works with the business owner on enterprise service isolation, and the recovery authority and operational owner hold the two human approval gates written into RUN-0001. Where a service's ownership record is incomplete, that gap is itself an incident finding and is carried into the post-incident review.

## 6. Command authority matrix

Every material decision carries exactly one approval authority. Consultation does not transfer authority.

| Decision | Approval authority | Executable procedure |
|---|---|---|
| Routine containment | Incident Commander | — |
| Enterprise service isolation | Incident Commander with the business owner | — |
| Entry into recovery | Recovery authority named in the service ownership record | RUN-0001 step 2 |
| Production recovery | Recovery Coordinator with the service owner | RUN-0001 |
| Business resumption | Operational owner | RUN-0001 step 6 |
| Regulatory notification authorization | Executive Leadership, with Legal review | — |
| Enterprise crisis declaration | Executive Leadership | — |
| Risk acceptance during recovery | Enterprise Governance Board, or its delegated authority | — |

Entries marked "—" are commanded directly under this model and have no separate runbook in the current library.

## 7. Declaration, activation, and escalation

The crisis lifecycle proceeds in a fixed order: detection → incident declaration → command activation → operational stabilization → business recovery → service validation → lessons learned → governance improvement. The enterprise workflow that surrounds it runs security detection → incident assessment → command activation → operational response → recovery execution → business validation → post-incident review → governance enhancement.

| Stage | Entry condition | Authority | Required output |
|---|---|---|---|
| Detection and assessment | Telemetry, monitoring, or a runbook trigger reports a condition | Reporting party with the service's operational owner | Confirmed condition, affected service, and initial impact |
| Incident declaration | Assessment establishes an incident rather than an event | Incident Commander; Executive Leadership for an enterprise crisis | Severity level (Section 4) and an opened command log |
| Command activation | Declaration recorded | Incident Commander | Command posts filled or their duties explicitly assumed (Section 5.1) |
| Operational stabilization | Command active | Operations Section, under the Incident Commander | Containment achieved and impact no longer expanding |
| Business recovery | Stabilization confirmed and recovery authorized | Recovery Coordinator, per Section 6 and RUN-0001 | Restoration executed in dependency order |
| Service validation | Recovery executed | Operational owner, per RUN-0001 step 6 | Dependent services healthy; objectives met or the miss documented |
| Lessons learned | Service validated | Incident Commander with the EPOC | Post-incident review (Section 12) |
| Governance improvement | Review complete | Owning authority for each corrective action | Corrective actions with assigned ownership |

Escalation follows the enterprise path already governed by the architecture governance model: operational issue → Domain Owner → Governance Manager → Architecture, AI, or Risk Council → Enterprise Governance Board → Executive Leadership. Two incident-specific triggers sit on top of it and are mandatory: a suspected cyber cause transfers direction to the Enterprise Cyber Command before further recovery steps (RUN-0001), and a preventive-control failure on a Tier 1 service escalates to the Enterprise Cyber Command and the executive sponsor (RUN-0003). A critical security incident requiring executive direction is a mandatory escalation to Executive Leadership.

## 8. Communications

### 8.1 Executive situation reporting

Every major incident maintains structured situation reports. Each report contains: incident identifier; executive summary; affected services; current operational status; decisions made; outstanding risks; recovery progress; next planned actions. The Communications Section owns the report; the Incident Commander approves it before release.

The incident identifier field is required by the report, but this document does not mint one. STD-0001 requires an identifier prefix to be registered in `standards/vocabulary/object-identifiers.yaml` before any artifact mints an identifier with it, and the prefixes registered there today do not include one for incidents. Registration of an incident prefix is a prerequisite to first use of this field, and is a change to the identifier registry rather than to this document.

### 8.2 External and regulatory coordination

Where applicable, incident governance follows documented workflows for regulatory notifications, customer communications, third-party coordination, cyber insurance engagement, law enforcement liaison, and contractual notification obligations. All external communications follow enterprise approval workflows, and regulatory notification is authorized by Executive Leadership with Legal review (Section 6).

### 8.3 Executive Control Tower

Executive dashboards display active incident command status, incident severity distribution, containment progress, recovery progress, business service availability, unresolved executive decisions, corrective action status, and resilience trends. These are reporting views over the registers in Section 10; they are not a separate record.

## 9. Recovery coordination

Recovery activities define restoration priority, service dependencies, minimum viable operation, validation criteria, rollback procedures, recovery evidence, and residual risk. Business-critical services maintain documented recovery objectives consistent with enterprise continuity requirements.

The Recovery Coordinator sequences recovery against those definitions; the execution itself is the runbook's. RUN-0001 is the executable procedure for governed recovery orchestration (PAT-0004), and this model supplies only the command layer above it. The interface is fixed:

| Condition | Governing runbook | What this model contributes |
|---|---|---|
| Tier 1 service fails or degrades beyond its availability target | [RUN-0001](../runbooks/RUN-0001-service-recovery-execution.md) | Declaration and severity (Sections 4, 7); recovery authorization and business resumption authorities (Section 6); situation reporting during execution (Section 8.1) |
| Service error budget reaches zero in the measurement window | [RUN-0002](../runbooks/RUN-0002-error-budget-exhaustion-response.md) | Severity assignment where exhaustion coincides with an active incident; recurrence findings carried into post-incident review (Section 12) |
| Continuous compliance detects a material deviation | [RUN-0003](../runbooks/RUN-0003-compliance-deviation-response.md) | Regulatory dimension of classification (Section 4); mandatory escalation on trust-boundary exposure (Section 7) |

Where a condition is covered by an approved runbook, that runbook is executed or the deviation is recorded. This model neither shortens a runbook's human approval gates nor authorizes bypassing one; an incident that appears to require a bypass is an escalation under Section 7.

## 10. Incident registers and evidence

Four registers are maintained for the duration of an incident and retained after it. Each is defined here by its record fields and lifecycle; none is populated with sample identifiers, and none may mint an identifier-shaped token before its prefix is registered under STD-0001.

| Register | Record fields | Lifecycle |
|---|---|---|
| Incident command log | Time-ordered entries covering incident identifier, severity at time of entry, affected services, actions taken, and the post that took them | Opened at declaration; appended throughout; closed at service validation; retained as evidence |
| Executive situation report | The eight fields in Section 8.1 | Issued from command activation at a cadence set by severity; final report issued at service validation |
| Crisis decision register | Decision, approving authority per Section 6, time, and the outstanding risk the decision accepted or resolved | Opened at declaration; one entry per material decision; closed with the incident; unresolved executive decisions surface in the Executive Control Tower |
| Corrective action register | Action, assigned owner, originating finding, and status | Opened at post-incident review; entries close only on the owning authority's confirmation; open entries surface in executive reporting |

Two further outputs are produced rather than maintained: a recovery validation report at service validation, and a post-incident governance assessment at review close. Recovery evidence produced under RUN-0001 — recovery timeline, per-step validation results, and objective attainment — is emitted to Continuous Assurance under PAT-0003 before the incident record closes; RUN-0002 and RUN-0003 emit their own evidence on the same path.

Incident command objects maintain governed relationships in the Enterprise Knowledge Graph with incidents, services, assets, responders, executive decisions, evidence, recovery activities, corrective actions, risks, and controls. Those relationships are registered edges under STD-0002 and are subject to its enforcement rules; an edge is added when this or another artifact states the relationship.

## 11. AI-assisted incident support

AI may assist with timeline generation, dependency analysis, action tracking, executive briefing preparation, evidence correlation, resource recommendations, and post-incident documentation.

AI shall not independently declare an incident, authorize recovery, or approve external communications. This boundary is absolute and is not relaxed by severity, time pressure, or unavailability of a command post; where a post cannot be filled, Section 5.1 applies. AI assistance operating within an incident remains least privileged, observable, auditable, bounded by policy, and traceable to owners, controls, and evidence.

## 12. Post-incident review

Post-incident review is a stage of the lifecycle, not an optional follow-up: service validation is followed by lessons learned and then governance improvement (Section 7). The review is convened by the Incident Commander with the EPOC and produces the post-incident governance assessment.

The review examines, at minimum:

- the classification assigned and whether the escalation criteria in Section 4 were correctly applied;
- the decisions in the crisis decision register against the authorities in Section 6;
- recovery performance against the service's documented recovery objectives, and any objective miss with its documented cause (RUN-0001);
- evidence completeness on the Continuous Assurance path (PAT-0003);
- ownership gaps found during the incident (Section 5.2);
- recurrence: whether this incident repeats a prior one, and whether an existing corrective action failed to prevent it.

Every finding becomes a corrective action with an assigned owner. Reliability engineering under Volume 10 reduces incident recurrence, and reliability initiatives are prioritized using measurable operational data, so recurrence findings from this review are inputs to that prioritization rather than a parallel backlog. Recurrence within two measurement windows for an error-budget condition already triggers operational governance review of the SLO and the service architecture under RUN-0002.

## 13. Readiness validation and cadence

Enterprise exercises validate the command structure, escalation procedures, communications, technical recovery, executive decision making, evidence collection, and policy compliance. Exercise outcomes produce corrective actions with assigned ownership, recorded in the same register as incident-derived actions (Section 10).

| Cycle | Cadence | Source authority |
|---|---|---|
| Incident command standard review | Semi-annual, with quarterly tabletop validation | v6.6-alpha standard |
| Operations review | Weekly | Volume 10 |
| Reliability review | Monthly | Volume 10 |
| Operational excellence certification | Annual | Volume 10 |

## 14. Human review gate

Approval of this document requires confirmation by Platform Engineering Leadership and the Program Owner that:

- no command post, severity level, authority, escalation trigger, register, or cadence has been introduced beyond those in the cited sources;
- the command reconciliation in Section 2 creates no second command system and moves no authority from the Enterprise Cyber Command;
- the runbook interface in Section 9 links to RUN-0001, RUN-0002, and RUN-0003 without restating, weakening, or bypassing their human approval gates;
- the AI boundary in Section 11 is stated without conditions or exceptions;
- no identifier is minted by this document ahead of its prefix registration under STD-0001.

Because this document addresses incident command authority, crisis escalation criteria, executive reporting, recovery governance, regulatory communication workflows, AI-assisted crisis support, and cyber recovery decision processes, any change to it additionally passes the multi-role review carried by the v6.6-alpha standard: the Enterprise Governance Board, Executive Leadership, the Enterprise Architecture Review Board, Security Operations Leadership, Business Continuity Management, Legal, and Internal Audit.

## 15. Sources and traceability

| Source (repo-relative path) | Contribution |
|---|---|
| history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v5.0-v6.6/EAODS-v6.6-alpha-enterprise-incident-command-crisis-management-and-cyber-recovery-governance-standard.md | ECICS command architecture and reporting chain (Sections 2, 5); guiding principles (Section 3); IC-0 to IC-5 classification and escalation criteria (Section 4); command post responsibilities for Incident Commander, Operations, Planning, Communications, and Recovery Coordinator (Section 5); absence of a distinct scribe post in the material read (Section 5.1); command authority matrix (Section 6); crisis lifecycle and enterprise workflow (Section 7); situation report fields (Section 8.1); regulatory and external coordination workflows (Section 8.2); Executive Control Tower display set (Section 8.3); recovery governance definitions (Section 9); Artifact Factory outputs read as the register set, and Knowledge Graph relationship set (Section 10); AI-assisted crisis support boundaries (Section 11); tabletop exercise framework and semi-annual/quarterly cycle (Section 13); multi-role review gate (Section 14) |
| docs/frameworks/EAODS-v17.3/volume-10-platform-operations.md | Governing architecture; EPOC as operational authority and the Enterprise Cyber Command boundary used in the Section 2 reconciliation; engineering principles (Section 3); canonical service ownership record and reliability classification as classification inputs, including `SVC-00387` (Section 4); seven-role service ownership framework (Section 5.2); reliability engineering model and recurrence reduction (Section 12); operations, reliability, and certification cadences (Section 13) |
| docs/runbooks/RUN-0001-service-recovery-execution.md | Recovery authority and operational owner approval gates (Sections 5.2, 6, 7); cyber-cause transfer to Enterprise Cyber Command (Sections 2, 7); recovery objective attainment and documented miss (Sections 7, 12); recovery evidence emitted to Continuous Assurance under PAT-0003 (Section 10); identification of RUN-0001 as the executable procedure for PAT-0004 governed recovery orchestration, and the runbook interface row (Section 9) |
| docs/runbooks/RUN-0002-error-budget-exhaustion-response.md | Error-budget exhaustion trigger and recurrence-within-two-windows escalation to operational governance (Sections 9, 12) |
| docs/runbooks/RUN-0003-compliance-deviation-response.md | Material compliance deviation trigger; trust-boundary escalation to Enterprise Cyber Command; preventive-control failure on a Tier 1 service escalating to executive sponsor; registered control `EAODS-CTRL-000184` as the regulatory dimension of classification (Sections 4, 7, 9) |
| docs/standards/canonical-terminology-and-identifiers.md (STD-0001) | Requirement that an identifier prefix be registered before first use, applied to the incident identifier field and to the registers (Sections 8.1, 10) |
| docs/standards/cross-artifact-traceability.md (STD-0002) | Registered, typed edges and enforcement rules applied to incident command relationships (Section 10) |
| docs/architecture/ENTERPRISE_OPERATING_MODEL.md (EAODS-ARCH-EOM-001) | Incident command as a defined Volume 10 operational capability (Section 1); AI operating boundaries restated for incident support (Section 11) |
| docs/architecture/architecture-governance-model.md (EAODS-ARCH-GOV-001) | House style — front matter, numbered sections, reconciliation and human-review-gate conventions, sources-and-traceability format; EARB naming reconciliation (Section 2); enterprise escalation path and mandatory escalation for critical security incidents (Section 7); single-approval-authority rule (Sections 3, 6) |
