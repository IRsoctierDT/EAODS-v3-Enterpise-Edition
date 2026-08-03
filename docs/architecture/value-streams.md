---
title: EAODS Value Streams
document_id: EAODS-ARCH-VAL-001
version: 1.0.0
status: proposed
owner: Enterprise Architecture Owner
review_gate: Enterprise Architecture Review Board and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - EAODS-ARCH-BIZ-001
  - EAODS-ARCH-EOM-001
  - EAODS-ARCH-PRIN-001
  - ADR-0002
  - STD-0002
  - docs/frameworks/EAODS-v17.3/volume-10-platform-operations.md
  - history/original-sources/conversation-evidence/v6.7-v16-band (EAODS v13.0.0–13.0.5 alpha volume units)
  - history/original-sources/conversation-evidence/v6.7-v16-band (EAODS v15.0.0–15.0.5 alpha volume units)
---

# EAODS Value Streams

## 1. Purpose and scope

This document gives the full treatment of the EAODS value streams sketched in the business architecture (EAODS-ARCH-BIZ-001, Section 6). It defines, for each stream, the end-to-end stages, the accountable owners, the human gates that must be passed, the evidence each stage produces, and the metrics by which the stream is judged.

It expands rather than replaces the business architecture. The required value stream catalog is unchanged, the rule that each capability supports one or more value streams is unchanged, and value stream economics remain evaluated per stream and linked to the capabilities that serve it.

Four streams receive detailed treatment here because they carry the operational load of the repository: idea to governed change, incident to recovery, evidence to assurance, and knowledge to retrieval. Each is a working path across one or more of the required streams; none is a new stream.

## 2. Required value stream catalog

The required enterprise value streams (v13.0 Volume 2) and their coverage in this document:

| Required value stream | End-to-end outcome | Treated here as |
|-----------------------|--------------------|-----------------|
| Strategy-to-Execution | Strategic objectives become funded, delivered capability | Idea to governed change (Section 4) |
| Idea-to-Innovation | Proposals are evaluated and either adopted or closed | Idea to governed change (Section 4) |
| Demand-to-Delivery | Approved demand becomes a production service | Idea to governed change (Section 4) |
| Detect-to-Respond | Signals become classified, owned response | Incident to recovery (Section 5) |
| Incident-to-Recovery | Disruption becomes restored service and learning | Incident to recovery (Section 5) |
| Risk-to-Assurance | Risks and controls become verified assurance evidence | Evidence to assurance (Section 6) |
| Data-to-Decision | Enterprise data becomes explainable decision support | Knowledge to retrieval (Section 7) |
| Customer-to-Value | Customer demand becomes realized, measured value | Governed by EAODS-ARCH-BIZ-001; not elaborated here |

Value streams represent end-to-end organizational outcomes. They are not departmental processes, and no stream is owned by a single organizational unit.

## 3. Common anatomy of an EAODS value stream

Every stream in this document is described with the same five elements, so that streams can be compared, measured, and audited consistently.

| Element | Requirement |
|---------|-------------|
| Stages | Ordered, named steps with defined entry and exit conditions |
| Owners | Drawn from the six capability ownership roles — Executive, Business, Technical, Governance, Operational, Performance — plus the deciding authority for each gate |
| Gates | Human decision points classified under the decision rights framework: Strategic, Architectural, Cybersecurity, AI Governance, Operational, or Emergency |
| Evidence | Records produced at each stage and registered for Continuous Assurance |
| Metrics | Throughput, bottlenecks, waste, investment cost, operating cost, and value contribution, per the value stream economics model |

Three constraints apply to every stream. Cybersecurity review is mandatory for material enterprise changes, so Domain 03 participates in every stream rather than in a security stream of its own. Escalation follows the documented E1–E5 path from Team Lead to Board-Level Review, with thresholds documented before production operation. Every decision recorded in a stream carries its identifier, requesting authority, approving authority, affected capabilities, supporting evidence, associated risks, expected benefits, implementation owner, and review date.

## 4. Idea to governed change

This stream carries an idea from strategic demand through architecture and portfolio governance into a released, measured change. It composes the investment lifecycle (v13.0 Volume 2), the engineering lifecycle and Architecture Development Method (v13.0 Volume 4), the decision lifecycle (v13.0 Volume 3), and — where the decision is large enough to warrant it — governed simulation in the Decision Laboratory (v15.0 Volume 2).

| # | Stage | Primary owner | Gate |
|---|-------|---------------|------|
| 1 | Strategic demand and capability assessment | Business Owner | Capability alignment confirmed before a business case is opened |
| 2 | Business case development | Executive sponsor | Business case complete: strategic objective, capability alignment, business outcomes, architectural impact, cybersecurity impact, AI governance considerations, financial analysis, operational impact, measurable success criteria, retirement or exit strategy |
| 3 | Scenario evaluation (where strategic uncertainty warrants) | Scenario executive sponsor | Governance review of the scenario before modeling; no simulation modifies production |
| 4 | Architecture and security review | Enterprise Architecture Review Board with Domain 03 | Architectural (EARB) and Cybersecurity (Domain 03 Governance Board) decision classes; architecture approval is required before portfolio funding |
| 5 | Portfolio approval and funding authorization | Portfolio Management Board | Strategic decision class; investment maps upward to an approved capability |
| 6 | Architecture definition, engineering design, standards validation | Technical Owner | Applicable technical standards selected; exceptions carry justification, risk assessment, compensating controls, approval authority, and expiration date |
| 7 | Architecture decision record | Design authority | Every material engineering decision generates an ADR; approved ADRs are immutable and superseding decisions are referenced explicitly |
| 8 | Implementation and verification | Delivery organization | Security testing integrated into the delivery pipeline rather than deferred to release |
| 9 | Engineering conformance assessment | Engineering Assurance | Architecture alignment, standards compliance, security implementation, operational readiness, documentation, technical debt, interoperability, maintainability; non-conformities carry remediation plans and named owners |
| 10 | Operational transition | Operational Owner | Service ownership record complete before production operation (Section 5) |
| 11 | Benefit measurement and value validation | Performance Owner | Benefits measurable after implementation; double-counting of realized value prohibited |
| 12 | Portfolio reassessment | Portfolio Management Board | Investment continued, rebalanced, or retired on evidence |

Stages 1 through 5 are the governed funding path; stages 6 through 10 are the governed engineering path; stages 11 and 12 close the loop back into the portfolio. A change that cannot pass a gate is not abandoned silently — it is escalated on the E1–E5 path or recorded as a governed exception with an expiry date.

Stream metrics: engineering cycle time, ADR completion rate, standards adoption, architecture compliance, decision cycle time, exception frequency, investment delivery, and benefit realization rate.

## 5. Incident to recovery

This stream carries a signal from detection through response and restoration to institutionalized learning. Volume 10 is the governing authority: the Enterprise Platform Operations Center holds operational authority for platform health, reliability, performance, and continuous improvement.

| # | Stage | Primary owner | Gate |
|---|-------|---------------|------|
| 1 | Telemetry generation and platform monitoring | Enterprise Platform Operations Center | Telemetry normalized before enterprise consumption |
| 2 | Detection and correlation | Domain 03 with the correlation engine | Signals correlated to capability, service, identity, agent, control, and risk |
| 3 | Classification and escalation | Operational Owner | Documented escalation thresholds; E1–E5 path |
| 4 | Response under incident command | Incident Commander | Emergency decision class exercised only under approved emergency authority |
| 5 | Recovery and restoration | Recovery authority named in the service ownership record | Recovery sequencing follows the approved plan; recovery events recorded as security telemetry |
| 6 | Reliability evaluation | Site Reliability Engineering | Service level objectives derived from observed behavior, not aspiration |
| 7 | Error budget disposition | Enterprise Platform Operations Center | Exhausted error budgets trigger engineering review before additional production changes |
| 8 | Engineering prioritization and improvement | Platform Engineering | Reliability initiatives prioritized on measurable operational data |
| 9 | Retrospective and learning capture | Performance Owner | Validated lessons update enterprise standards, playbooks, and knowledge repositories |
| 10 | Continuous assurance evidence and executive reporting | Continuous Assurance with the Executive Control Tower | Operational evidence independently verified before executive reporting |

The stream cannot start without ownership already in place. Every production service identifies a business owner, an engineering owner, an operational owner, an executive sponsor, a recovery authority, an architecture authority, and an assurance owner, and that ownership remains continuously documented. The canonical service ownership record — for example SVC-00387 (AutomationFabric), operated by the Enterprise Platform Operations Center at a 99.95% availability target with an enforced error budget policy — is the form this takes.

Recovery readiness is rehearsed rather than assumed. The Enterprise Digital Twin models recovery scenarios and supports simulation without modifying production systems; predictive resilience models estimate operational recovery duration and are periodically recalibrated against observed outcomes. Early warning indicators — increasing incident frequency, deteriorating service health, declining control effectiveness, elevated identity anomalies, supplier instability, mission delays, governance exceptions — feed stage 3 before disruption becomes material.

Stream metrics: service availability, dependency health, error budget consumption, incident recurrence, recovery capability, operational toil, resilience improvement, and corrective action completion.

## 6. Evidence to assurance

This stream converts operational activity into independently verified assurance. Its premise, from the architecture principles, is that evidence precedes assertion: assurance is continuous and independent, not a periodic attestation.

| # | Stage | Primary owner | Gate |
|---|-------|---------------|------|
| 1 | Evidence generation at the point of work | Capability performing the activity | Telemetry lifecycle terminates in evidence; source attribution and collection timestamps preserved |
| 2 | Registration and correlation | Data and telemetry owners | Evidence linked through the Knowledge Graph to services, controls, risks, incidents, and executive objectives |
| 3 | Reconciliation | Configuration and architecture authorities | Architecture repository, CMDB, operational telemetry, Digital Twin, deployment pipelines, Knowledge Graph, and evidence records compared; material inconsistencies generate remediation workflows |
| 4 | Independent verification | Continuous Assurance | Control effectiveness, evidence completeness and quality, calculation consistency, treatment execution, benefit measurement integrity, and simulation and model traceability verified |
| 5 | Deviation handling | Governance Owner | Material deviations trigger governance review, executive review, corrective action planning, and where applicable recertification of affected autonomous capabilities |
| 6 | Executive reporting | Executive Control Tower | Reporting accuracy independently verified; observed evidence distinguished from analytical inference |
| 7 | Assurance-driven improvement | Performance Owner | Corrective actions tracked to completion and fed back into standards |

Assurance is not a separate reporting track bolted onto the other streams; it is the terminal stage of each of them. The closed-loop feedback architecture makes this explicit: telemetry becomes operational intelligence, intelligence becomes decision support, approved action becomes execution, execution generates evidence, evidence updates the Knowledge Graph, and Continuous Assurance verifies the result. Feedback remains human-governed for high-impact operational changes.

Stream metrics: evidence completeness, control effectiveness, reconciliation success rate, configuration accuracy, architecture drift, treatment completion, exception frequency, and corrective action completion.

## 7. Knowledge to retrieval

This stream makes enterprise knowledge findable, current, and safely usable — by humans and by governed AI. It spans knowledge federation and configuration intelligence (v13.0 Volume 5), telemetry and decision intelligence (v13.0 Volume 6), and the learning repositories that close the loop (v15.0 Volumes 2 and 6).

| # | Stage | Primary owner | Gate |
|---|-------|---------------|------|
| 1 | Discovery and capture | Source-system owners | Approved discovery mechanisms only; provenance and collection timestamps preserved |
| 2 | Classification and validation | Data and Knowledge domain | Records classified, security-classified, and version-controlled |
| 3 | Registration and federation | Knowledge Graph authority | Duplicate authoritative records prohibited; the Knowledge Graph is the authoritative semantic model |
| 4 | Relationship mapping | Architecture authority | Registered relationship types only; relationship integrity continuously validated |
| 5 | Retrieval and reasoning | AI governance and operations | Retrieval activity, prompt version, model version, tool invocations, policy decisions, confidence estimates, and human interventions all emit telemetry |
| 6 | Decision support | Decision Intelligence Platform | Recommendations are explained and carry supporting evidence; recommendations shall not automatically authorize high-impact actions |
| 7 | Learning capture | Performance Owner | Lessons validated before adoption; validated learning updates enterprise standards, playbooks, and knowledge repositories |
| 8 | Currency maintenance | Configuration and architecture authorities | Architecture drift and synchronization failures produce actionable alerts and documented reconciliation |

Retrieval quality is therefore a governance property, not a search feature. It depends on federation discipline upstream (one authoritative record per fact, with provenance) and on explainability downstream (reasoning legible to authorized reviewers). Where AI participates, the boundaries of Section 9 apply without exception.

Stream metrics: discovery coverage, configuration accuracy, topology completeness, synchronization latency, telemetry completeness, Digital Twin fidelity, learning adoption, and decision quality trends.

## 8. Cross-stream handoffs

Streams are only end-to-end because their handoffs are governed. The principal handoffs are:

| From | To | Handoff obligation |
|------|----|--------------------|
| Idea to governed change (stage 10) | Incident to recovery (stage 1) | Complete service ownership record, availability target, recovery objective, and telemetry instrumentation before production operation |
| Incident to recovery (stage 9) | Idea to governed change (stage 1) | Validated retrospective findings enter the demand path as capability improvements, not as informal fixes |
| All streams | Evidence to assurance | Every stage registers its evidence; unregistered activity is a non-conformity |
| Evidence to assurance (stage 5) | Idea to governed change (stage 4) | Material deviations re-enter architecture and governance review rather than being remediated locally |
| Knowledge to retrieval (stage 3) | All streams | The Knowledge Graph supplies the authoritative context every other stream reasons over |
| All streams | Portfolio governance | Value stream economics inform funding: business services are improved on evidence of stream performance rather than departmental output |

## 9. Human authority within streams

The streams are AI-assisted throughout and AI-authorized nowhere. Three boundaries are load-bearing and are restated here because they sit at stream gates rather than in any single system:

- decision support and analytical recommendations shall not automatically authorize high-impact actions;
- closed-loop operational feedback remains human-governed for high-impact changes;
- simulation and scenario work shall not directly modify production environments.

Emergency authority is the one place where a single role may act ahead of the standing gates: the Incident Commander decides under approved emergency authority, and the decision is recorded and reviewed like any other.

## 10. Stream measurement and cadence

Every stream is measured under the same governance. Each enterprise metric defines a metric owner, business purpose, calculation methodology, authoritative data source, reporting frequency, acceptable thresholds, escalation criteria, and evidence requirements; metric definitions are version-controlled and approved through governance. Stream health is reviewed on the executive operating cadence — weekly operational reviews, monthly performance governance, quarterly strategic reviews, and annual enterprise performance assessments — and each review generates documented decisions, assigned actions, and follow-up metrics.

Value stream economics are evaluated per stream: investment cost, operational cost, value contribution, throughput, bottlenecks, waste, and improvement opportunities, with performance linked to the enterprise capabilities that serve the stream.

## 11. Supporting repository artifacts

The streams above are realized by artifacts already governed in this repository. This mapping is indicative of where each stream's controls and procedures are documented; it introduces no new obligations.

| Stream | Supporting artifacts |
|--------|----------------------|
| Idea to governed change | ADR-0001, ADR-0002, STD-0001, STD-0002, PAT-0002 (error-budget-gated delivery) |
| Incident to recovery | RUN-0001 (service recovery execution), RUN-0002 (error budget exhaustion response), PAT-0004 (governed recovery orchestration) |
| Evidence to assurance | PAT-0003 (continuous assurance evidence pipeline), RUN-0003 (compliance deviation response), THR-0003 (assurance evidence tampering) |
| Knowledge to retrieval | STD-0002, THR-0002 (LLM instruction injection) |
| All streams | PAT-0001 (zero-trust service identity), THR-0001 (compromised service identity), EAODS-CTRL-000184 (Service Identity Verification) |

## 12. Human review gate

Approval of this value stream architecture requires confirmation by the Enterprise Architecture Review Board and the Program Owner that:

- the required value stream catalog and the capability-to-stream rule stated in EAODS-ARCH-BIZ-001 are reproduced without modification;
- every stage in every stream names an accountable owner and, where a decision is made, a deciding authority under the decision rights framework;
- architecture approval before portfolio funding, mandatory Domain 03 review of material changes, and error-budget gating of production change are stated as binding;
- AI participation in every stream remains advisory, with human authorization retained for high-impact actions;
- every stream terminates in registered evidence subject to independent Continuous Assurance verification;
- no capability, metric, governance body, or organizational structure is introduced beyond those in the cited sources.

## Sources and traceability

| Source (repo-relative path) | Contribution |
|-----------------------------|--------------|
| docs/architecture/business-architecture.md (EAODS-ARCH-BIZ-001) | Required value stream catalog and capability-to-stream rule expanded here (Sections 1, 2); six capability ownership roles, decision rights classes, governance bodies, E1–E5 escalation, decision record attributes (Section 3); value stream economics linkage (Sections 8, 10); executive operating cadence (Section 10) |
| docs/architecture/ENTERPRISE_OPERATING_MODEL.md (EAODS-ARCH-EOM-001) | House style; four-pillar and Volume 10 north-star framing; decision and accountability model behind stream gates; AI operating boundaries (Section 9); integration points reflected in Section 11 |
| docs/architecture/architecture-principles.md (EAODS-ARCH-PRIN-001) | Approved sibling structure and tone; evidence-precedes-assertion premise (Section 6); named ownership and human-gate requirements applied per stage |
| docs/frameworks/EAODS-v17.3/volume-10-platform-operations.md | Enterprise Platform Operations Center authority, service ownership framework and canonical record (SVC-00387), SLI/SLO/SLA and error budget governance, reliability engineering model, operational workflow from telemetry to executive reporting (Section 5) |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v13.0.0-alpha-enterprise-operating-model-capability-framework-volume-1-ent.md | Capability-centric premise, capability ownership roles, value-stream contribution rule, planning cycle context (Sections 3, 4) |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v13.0.1-alpha-enterprise-operating-model-capability-framework-volume-2-ent.md | Required value stream definitions (Section 2), investment lifecycle and business case requirements, EARB-before-funding gate, capability funding and portfolio reassessment (Section 4) |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v13.0.2-alpha-enterprise-operating-model-capability-framework-volume-3-ent.md | Decision rights classes including Emergency authority, decision lifecycle, decision record attributes, E1–E5 escalation, mandatory Domain 03 review (Sections 3, 4, 9) |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v13.0.3-alpha-enterprise-operating-model-capability-framework-volume-4-ent.md | Engineering lifecycle and Architecture Development Method, ADR governance and immutability, standards and exception process, conformance assessment criteria, pipeline-integrated security testing (Section 4) |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v13.0.4-alpha-enterprise-operating-model-capability-framework-volume-5-ent.md | Discovery provenance, configuration lifecycle, reconciliation scope, relationship model, knowledge federation and no-duplicate-authoritative-records rule, Digital Twin recovery modeling and simulation constraint, synchronization alerting (Sections 5, 6, 7) |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v13.0.5-alpha-enterprise-operating-model-capability-framework-volume-6-ent.md | Telemetry lifecycle terminating in evidence, correlation engine scope, AI runtime observability fields, Domain 03 detection-to-recovery telemetry, decision-support boundary, closed-loop feedback architecture (Sections 5, 6, 7, 9) |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v15.0.1-alpha-enterprise-intelligence-adaptive-organization-framework-volu.md | Decision Laboratory scenario lifecycle and governance review gate, no-production-modification constraint, enterprise learning repository, Continuous Assurance verification of simulation integrity (Sections 4, 6, 9) |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v15.0.2-alpha-enterprise-intelligence-adaptive-organization-framework-volu.md | Early warning indicators, predictive resilience estimation of recovery duration and model recalibration, Continuous Assurance evaluation scope including recertification trigger (Sections 5, 6) |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v15.0.4-alpha-enterprise-intelligence-adaptive-organization-framework-volu.md | Benefits realization requirements, prohibition on double-counting realized value, value stream economics factors, Continuous Assurance verification of benefit measurement integrity (Sections 4, 6, 10) |
| history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v15.0.5-alpha-enterprise-intelligence-adaptive-organization-framework-volu.md | KPI/KRI governance attributes and version control, organizational learning framework and validated-learning rule, executive operating cadence, Continuous Assurance verification of metric integrity (Sections 5, 6, 7, 10) |
| docs/frameworks/EAODS-v17.3/volume-11-control-catalog.md | Identifier and objective of EAODS-CTRL-000184 (Service Identity Verification) cited in Section 11 |
