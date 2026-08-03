---
title: EAODS Implementation Guide
document_id: EAODS-REF-IDX-001
version: 1.0.0
status: proposed
owner: Enterprise Architecture Review Board
review_gate: Enterprise Architecture Review Board and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - EAODS-ARCH-ERA-001
  - EAODS-ARCH-EOM-001
  - EAODS-ARCH-PRIN-001
  - ADR-0002
  - STD-0001
  - STD-0002
  - PAT-0001
  - EAODS-CTRL-000184
  - docs/reference-implementations/index.md
  - docs/frameworks/EAODS-v17.3/volume-01-reference-platform-architecture.md
  - docs/architecture/enterprise-reference-architecture.md
  - history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v8.6-v8.7/EAODS-v8.6-alpha-enterprise-reference-architecture-patterns-technology-profiles-and-deployment-topologies-standard.md
  - history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v8.6-v8.7/EAODS-v8.7-alpha-enterprise-configuration-management-baseline-security-and-drift-governance-standard.md
---

# EAODS Implementation Guide

## 1. Purpose

This guide states the order in which an adopting organization stands up EAODS. It answers four questions that the architecture documents state structurally but do not sequence: what must exist before any platform work begins, which deployment topology to select and on what basis, what to build in what order once the topology is fixed, and what evidence each phase must produce before the next phase is authorized.

The guide is technology-neutral. It prescribes sequence, entry conditions, and acceptance evidence — not vendors, products, or timelines. It introduces no architecture, control, or governance requirement that is not already stated in the sources listed in Section 16.

## 2. How this guide relates to its siblings

| Artifact | Supplies | This guide adds |
|---|---|---|
| EAODS-ARCH-EOM-001 (Enterprise Operating Model) | The four pillars, decision and accountability model, AI operating boundaries | The order in which the pillars are instantiated |
| EAODS-ARCH-PRIN-001 (Architecture Principles) | The normative principle catalog and conformance tests | The phase at which each test is first applied |
| EAODS-ARCH-ERA-001 (Enterprise Reference Architecture) | Canonical layers, platform domains, service model, trust zones, topologies A–E, conformance checklist | The adoption path through that structure |
| docs/reference-implementations/index.md | What a reference implementation must demonstrate and how one is contributed | Where reference implementation work sits in the sequence |

Where this guide and a governing artifact disagree, the governing artifact prevails. Current approved repository artifacts and ADRs take precedence over historical drafts.

## 3. Adoption prerequisites

Nothing in Phase 1 or later begins until the following exist. This is the operating-model principle *governance precedes automation* (P2) expressed as an entry condition: no capability is automated before its governing policy, ownership, and controls are defined.

1. A named Program Owner with approval authority over changes affecting the operating model.
2. A constituted Enterprise Architecture Review Board able to hold the human review gate.
3. A recorded decision to adopt the four-pillar model — Govern, Design, Operate, Build — as structural.
4. Acknowledgement that EAODS v17.3 Volume 10 is the operational north star.
5. An identifier registry under STD-0001, from which all object identifiers are minted; identifiers are cited, never invented.
6. Traceability metadata rules under STD-0002 applied to every artifact the programme will produce.

An organization that cannot satisfy items 1, 2, and 5 is not ready to select a topology; it is ready to run Phase 0 only.

## 4. Adoption sequence at a glance

| Phase | Objective | Exit gate |
|---|---|---|
| 0 | Minimum viable governance | Program Owner and Architecture Review Board accept the governance baseline |
| 1 | Architecture baseline and topology selection | Topology ADR approved; trust zones and boundaries documented |
| 2 | Platform foundation | Every stood-up service has a complete canonical service model and passes the security baseline |
| 3 | Operational services and Domain 03 capability | Domain 03 capability demonstrated, including under component failure |
| 4 | Configuration baselines and drift governance | No production configuration without an approved baseline; drift detection operating |
| 5 | Reference implementation and evidence closure | Implementation anchored to the object model by stable identifier; entry registered |
| 6 | Continuous assurance and continual improvement | Assurance signals reported and feeding the improvement loop |

Phases are sequential in their gates, not in all their work. Phase 6 activities begin as soon as Phase 2 produces its first governed evidence, but Phase 6 cannot be declared complete before the earlier gates close.

## 5. Phase 0 — Minimum viable governance

Minimum viable governance is the smallest set of governance objects that makes later phases reviewable. It comprises:

- **A decision mechanism.** Every significant architectural decision is recorded as an ADR carrying identifier, context, decision, alternatives considered, consequences, approval authority, and review date, plus implementation status and superseded decisions where applicable. The catalog begins with ADR-0001 and ADR-0002 already in the repository.
- **A decision path.** Material architectural changes require, in order: documented rationale; impact analysis; traceability to controls and standards; human architecture review; and Program Owner approval where the operating model is affected.
- **A traceability chain.** Business Objective → Enterprise Capability → Reference Architecture → Security or Governance Control → Engineering Standard → Reference Implementation → Operational Runbook → Operational Metric → Continuous Assurance Evidence. Every artifact produced from Phase 1 onward joins this chain.
- **Named ownership.** Services and major artifacts have named owners and measurable reliability objectives.
- **An Evidence Registry.** Immutable by design, retaining workflow evidence, approvals, audit logs, QA results, release records, and execution summaries.
- **A human review gate.** A gate is a required element of every major artifact, not an optional courtesy.
- **AI operating boundaries.** Where AI assistance is used in any later phase, it is least privileged, observable, auditable, bounded by policy, subject to human approval for material actions, and traceable to owners, controls, and evidence.

Phase 0 produces no platform. It produces the conditions under which a platform can be approved.

## 6. Phase 1 — Architecture baseline and topology selection

### 6.1 State the design in all three canonical views

A design declares its position in each of the reference architecture's three views: the enterprise logical architecture (Business Services through Infrastructure Platform), the canonical platform layers (Enterprise Governance through Infrastructure Layer), and the enterprise layer model (Executive Control Tower through External Systems). No execution bypasses the Governance and Policy Engine where governance controls are required.

### 6.2 Select the topology

Topology selection, and its rationale, is a mandatory architecture decision recorded as an ADR. Selection is driven by the recommended-use column, not by preference:

| Topology | Select when the organization is characterized by | Consequences to plan for |
|---|---|---|
| A — Centralized Enterprise | Single region, centralized governance, moderate operational scale | Centralized policy enforcement; unified Security Data Fabric; single Enterprise Knowledge Graph |
| B — Hybrid Enterprise | Regulated industry, mixed on-premises and cloud estate, gradual modernization | Distributed compute; centralized governance; federated identity; synchronized evidence repositories |
| C — Multi-Cloud Enterprise | Global footprint, workload portability, resilience requirements | Cloud-independent governance; shared policy architecture; federated Security Data Fabric |
| D — Sovereign Deployment | Jurisdiction-specific data residency, government workloads, regulated infrastructure | Jurisdictional isolation; localized governance; controlled federation |
| E — Air-Gapped Deployment | Highly sensitive environments, critical infrastructure, classified operational networks | Isolated trust domains; controlled synchronization; offline evidence validation |

The v17.3 platform expresses the same requirement in infrastructure terms — on-premises for regulated or isolated environments, public cloud for elastic deployments, hybrid for mixed infrastructure strategies, multi-region for geographic resilience, edge for distributed operational environments. The two framings are compatible: the topology fixes the governance and data-fabric shape, the infrastructure model fixes where compute runs. Every topology preserves the same governance model, and every topology preserves Domain 03 operational capability during component failures.

### 6.3 Place trust zones and boundaries

Position every component in the trust zone reference model — External, DMZ, Enterprise Services, AI Operations Zone, Security Operations Zone, Restricted Data Zone — and document every boundary crossing. Communication across trust zones is authenticated, authorized, encrypted, logged, and policy evaluated. Separately, document the platform trust boundaries between executive governance, management services, operational workloads, automation services, data services, and external integrations; these are reviewed whenever architecture changes occur.

### 6.4 Select structural styles and patterns

Available structural styles are layered architecture, event-driven architecture, service mesh, hub-and-spoke, federated architecture, Zero Trust architecture, CQRS, and digital twin. The governed pattern library PAT-0001 through PAT-0004 supplies the approved, control-traced patterns; adversary assumptions come from THR-0001 through THR-0003.

## 7. Phase 2 — Platform foundation stand-up order

Stand up capability profiles, not products. The order below follows the dependency order of the canonical platform layers.

| Order | Capability | Why it precedes what follows |
|---|---|---|
| 1 | Identity Platform (authentication and federation) | Every subsequent boundary crossing requires an authenticated identity; cross-boundary service identity follows PAT-0001 under EAODS-CTRL-000184 |
| 2 | Governance Platform / Policy Engine (policy enforcement, authorization decisions) | Authorization decisions are made by policy, not by callers; integrations authorize via the Enterprise PDP |
| 3 | Integration Platform and Event Platform (API and event routing, messaging and streaming) | Carries the versioned envelope on which traceability depends |
| 4 | Data Platform (operational data lifecycle, Security Data Fabric) | Each data category needs an authoritative system of record before operational services generate data |
| 5 | Observability Platform (metrics, logs, traces) | Observability is by design; no service reaches operational acceptance without emitting its signals |
| 6 | Automation Platform / Workflow Platform (workflow execution and orchestration) | Controlled automation is enabled only once governance, identity, and observability can bound it |
| 7 | Knowledge Platform (Enterprise Knowledge Graph) | Registers governed relationships among services, deployments, policies, controls, trust zones, assets, ADRs, metrics, and resilience assessments |
| 8 | Evidence Platform and Assurance Platform (immutable assurance records, validation and certification) | Closes the traceability chain that Phases 4–6 consume |

Three conditions apply to every service stood up in this phase:

- **Canonical service model complete.** Each service declares service_id, service_name, business_capability, service_owner, dependencies, api_contract, event_contract, availability_target, recovery_objective, security_classification, and review_cycle. SVC-00387 in Volume 10 is the reference service record for this model.
- **Communication envelope carried.** Every cross-layer request carries Request ID, Workflow ID, Version, Classification, Timestamp, and Origin Component. Integrations support mutual authentication, authorization via the Enterprise PDP, schema validation, message integrity, encryption in transit, audit logging, and retry governance. Direct service dependencies are minimized.
- **Security baseline met.** Authenticated administrative access, role-based authorization, encrypted communications, immutable audit logging, secure configuration management, vulnerability management integration, and continuous security validation.

Resilience is designed in this phase, not retrofitted: redundant critical services, automated health monitoring, controlled failover, backup validation, dependency mapping, and documented recovery procedures, with recovery objectives documented and tested. Geographically resilient designs additionally define primary region, secondary region, evidence replication strategy, identity continuity, policy synchronization, and recovery orchestration.

## 8. Phase 3 — Operational services and Domain 03 capability

With the platform foundation accepted, stand up the operational services layer — Detection Engineering, Intelligence, and Incident Response — and the AI-SOC reference deployment, whose core logical components are Detection Services, Threat Intelligence, Incident Command, Response Orchestration, Evidence Repository, AI Investigation Agents, Executive Dashboards, and Continuous Assurance Services.

The phase is complete when the deployment explicitly supports AI-assisted threat detection, exposure management, incident command, response automation, recovery orchestration, resilience engineering, and evidence preservation — and when that support has been demonstrated to survive component failure, which the topology is required to guarantee.

## 9. Phase 4 — Configuration baselines and drift governance

Configuration is a governed enterprise asset. The governance path runs Configuration Sources → Configuration Registry → Baseline Repository → Configuration Validation → Policy Evaluation → Deployment → Continuous Drift Detection → Evidence Repository → Executive Control Tower.

Register configuration items across the governed families: INF (infrastructure), NET (network), IDM (identity), SEC (security), AI (AI components), APP (applications), DAT (data services), OBS (observability), and GOV (governance services). Every configuration item defines a configuration identifier, owner, approved baseline, deployment scope, lifecycle status, business criticality, validation frequency, rollback reference, and evidence requirements.

The binding rule for this phase: **no production configuration exists without an approved baseline.** Approved baselines include hardened default settings, approved software versions, required security controls, logging requirements, monitoring configuration, cryptographic settings, network policy requirements, and recovery configuration; deviations require documented approval.

Drift is classified as authorized, temporary, unauthorized, security-critical, or operational-critical. Unauthorized and security-critical drift triggers immediate investigation. Every production configuration change carries a change identifier, configuration reference, business justification, risk assessment, approval authority, rollback plan, and validation results; emergency changes undergo retrospective governance review.

## 10. Phase 5 — Reference implementation and evidence closure

A reference implementation is the Build pillar made concrete: it demonstrates that EAODS objects are buildable rather than aspirational, and it must demonstrate control enforcement, secure architecture, operational ownership, measurable outcomes, traceable evidence, and human review gates.

The contribution sequence is fixed:

1. Anchor the design document to the EAODS object model, stating what it realizes, mitigates, and evidences — by stable identifier.
2. Keep the implementation's own governance — charter, review gates, quality checks — in its own repository. EAODS records the relationship, not the code.
3. Add the entry to the implementation index and the corresponding edges to the knowledge graph once the implementation reaches a reviewable state.
4. Pass documentation validation and the Enterprise Architecture Review Board human review gate.

As read on the version of docs/reference-implementations/index.md cited in Section 16, the index carries a single registered entry: the IANUA Agent Trust Broker, realizing PAT-0001 (Zero Trust Service Identity) and EAODS-CTRL-000184 (Service Identity Verification), and mitigating THR-0001 (Compromised Service Identity) and THR-0002 (LLM Instruction Injection). An adopting organization treats it as the worked example of the anchoring pattern, not as a required component.

## 11. Phase 6 — Continuous assurance and continual improvement

Continuous assurance monitors configuration changes, unauthorized modifications, baseline deviations, deployment failures, rollback frequency, policy violations, recurring drift patterns, and evidence completeness. Each configuration item maintains a baseline compliance score, policy compliance score, drift frequency, remediation timeliness, validation success rate, and operational stability index; those scores contribute to Enterprise Capability Maturity assessments.

Executive architecture dashboards display deployed topology, trust zone health, service dependencies, architecture compliance, resilience posture, geographic distribution, platform capacity, and architectural risks. Executive configuration dashboards report enterprise baseline compliance, configuration drift trends, unauthorized configuration changes, remediation status, configuration risk heat maps, validation success rates, configuration maturity, and operational integrity indicators.

Governance validation, evidence recording, quality assurance, and Executive Control Tower reporting occur within the architecture workflow rather than after it; artifacts reach publishing and archive only after evidence is recorded. Operational execution of the architecture is carried by RUN-0001 through RUN-0003.

## 12. Acceptance evidence by phase

Each phase closes on evidence, not on assertion. Evidence precedes assertion (P8).

| Phase | Acceptance evidence |
|---|---|
| 0 | ADR record of the operating-model adoption decision; named Program Owner and constituted review board; identifier registry established under STD-0001; traceability metadata rules applied under STD-0002 |
| 1 | Approved topology ADR with rationale; Deployment Topology Catalog; Trust Zone Diagrams; Technology Capability Matrix; Architecture Decision Register; Enterprise Reference Architecture Portfolio |
| 2 | Complete canonical service model per service; security baseline validation per component; documented and tested recovery objectives; Resilience Assessment Report; knowledge graph registration |
| 3 | Demonstrated Domain 03 capability including under component failure; incident, detection, and response evidence in the Evidence Registry |
| 4 | Enterprise Configuration Registry; Approved Baseline Catalog; Baseline Validation Report; Configuration Drift Report; Configuration Risk Register; Configuration Compliance Dashboard |
| 5 | Reference implementation design document anchored by stable identifier; index entry and knowledge graph edges; documentation validation result; review board approval |
| 6 | Executive Architecture Dashboard; Executive Configuration Health Summary; Annual Architecture Compliance Review; Annual Configuration Governance Assessment |

All of it lands in the Evidence Registry, which holds workflow evidence, approvals, audit logs, QA results, release records, and execution summaries.

## 13. Illustrative adoption scenarios

The following are **illustrative scenarios drawn from the case-study sections of the cited source documents**. They are worked examples used to show how the sequence applies to different starting conditions. They are not accounts of real deployments at real organizations, and no organization is identified.

**Scenario 1 — Consolidating independently evolved platforms (v17.3 Volume 1 case study).** A multinational enterprise consolidates several regional cybersecurity platforms into a single globally governed operating model. The stated challenge is inconsistent architectures, duplicated integrations, fragmented observability, and uneven operational governance arising from independent evolution. In sequence terms this is a Phase 1 problem before it is a Phase 2 problem: the reference platform supplies standardized layers, service boundaries, data ownership, communication models, and resilience patterns, and every capability aligns to the canonical architecture while remaining deployable across on-premises, cloud, and hybrid environments. The scenario's stated outcome is a unified engineering foundation with preserved architectural traceability.

**Scenario 2 — Topology selection under modernization pressure (v8.6 case study).** A multinational institution in a regulated sector modernizes legacy cybersecurity platforms while deploying AI-assisted security operations across regional data centres and cloud providers. The stated challenge is that different engineering teams propose inconsistent deployment models, producing divergent security controls, fragmented observability, and operational complexity. The scenario resolves at Phase 1: engineering teams select a hybrid topology with centralized governance, federated identity, and regional AI-SOC instances while maintaining enterprise-wide policy consistency. Its stated outcome is reduced architectural drift and consistent governance across distributed services.

**Scenario 3 — Configuration governance at agent scale (v8.7 case study).** A global enterprise operates many AI agents, security platforms, and hybrid infrastructure components, with multiple engineering teams maintaining configurations independently and unauthorized drift appearing across production. This is the Phase 4 case: centralized configuration item registration, secure baseline management, Configuration-as-Code governance, automated drift detection, continuous validation, and executive reporting, with configuration evidence linked to the knowledge graph. Its stated outcome is consistent configuration governance and measurable executive visibility into configuration health.

None of the three scenarios reports quantified results in its source, and none is reproduced here as one.

## 14. Sequencing constraints and common failure modes

| Constraint | Failure mode it prevents |
|---|---|
| No component bypasses governance controls | Automation approved before its governing policy exists |
| No modification of immutable audit records | Evidence that cannot support assurance |
| No publication of unapproved artifacts | Draft material acquiring apparent authority |
| No execution outside documented workflow context | Untraceable operations |
| No access to undocumented interfaces | Unreviewed boundary crossings |
| No production configuration without an approved baseline | Drift with no reference to detect it against |
| Identifiers minted only from the registry and cited, never invented | Broken traceability chains |
| Historical units are evidence, retained with provenance | Historical drafts silently redefining current architecture |

Exceptions to any of the above require documented architectural approval recorded as an ADR. A contribution that cannot satisfy the relevant tests is escalated through the decision and accountability model, not rejected silently.

Two ordering errors are worth naming explicitly, because both are structurally invited by the material. The first is treating Phase 2 as the start of adoption — standing up identity and integration before a topology ADR exists, which makes the topology an artefact of infrastructure choices rather than a governed decision. The second is deferring Phase 4 until after Phase 3 is in production, which leaves operational services running without approved baselines and therefore without a reference against which drift is detectable.

## 15. Human review gate

Approval of this guide requires confirmation by the Enterprise Architecture Review Board and the Program Owner that:

- the phase sequence introduces no requirement absent from its cited sources;
- topology selection remains a mandatory ADR-recorded architecture decision;
- the minimum viable governance set is stated as an entry condition, not a recommendation;
- acceptance evidence in Section 12 maps to artifacts the cited sources already require;
- the scenarios in Section 13 are identifiable as illustrative source case studies;
- historical v8.6 and v8.7 material is treated as conversation-derived evidence rather than current authority.

Changes affecting the phase sequence, topology selection criteria, minimum viable governance, or acceptance evidence re-enter this gate before publication.

## 16. Sources and traceability

| Source (repo-relative path) | Contribution |
|---|---|
| docs/architecture/enterprise-reference-architecture.md (EAODS-ARCH-ERA-001) | Three canonical views and no-bypass rule (Section 6.1); topologies A–E with recommended use and characteristics, and reconciliation with v17.3 deployment models (Section 6.2); trust zones and platform trust boundaries (Section 6.3); structural styles and pattern/threat library ranges (Sections 6.4, 11); capability profiles and stand-up dependencies (Section 7); canonical service model and SVC-00387 reference record (Section 7); communication envelope, integration requirements, and security baseline (Section 7); resilience and geographic resilience requirements (Section 7); Evidence Registry contents (Sections 5, 12); architectural constraints and exception rule (Section 14); workflow placement of validation, evidence, QA, and reporting (Section 11) |
| docs/frameworks/EAODS-v17.3/volume-01-reference-platform-architecture.md | Canonical platform layers and their order (Section 7); core platform domains (Section 7); canonical service model fields (Section 7); v17.3 deployment models and same-governance rule (Section 6.2); observability and data-architecture requirements (Sections 7, 12); platform security baseline and resilience architecture (Section 7); operational services layer (Section 8); engineering workflow stages informing phase gates (Section 4); Scenario 1 case study (Section 13) |
| history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v8.6-v8.7/EAODS-v8.6-alpha-enterprise-reference-architecture-patterns-technology-profiles-and-deployment-topologies-standard.md (conversation-derived evidence) | Topology selection criteria and characteristics (Section 6.2); trust zone reference model and cross-zone communication rule (Section 6.3); architecture pattern catalog and technology capability profiles (Sections 6.4, 7); AI-SOC reference deployment components (Section 8); Domain 03 integration requirements and failure-tolerance rule (Sections 6.2, 8); ADR required attributes (Section 5); high availability, geographic resilience, scalability, and secure integration patterns (Section 7); Artifact Factory outputs used as architecture acceptance evidence (Section 12); Executive Control Tower architecture dashboard content (Section 11); Scenario 2 case study (Section 13) |
| history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v8.6-v8.7/EAODS-v8.7-alpha-enterprise-configuration-management-baseline-security-and-drift-governance-standard.md (conversation-derived evidence) | Configuration governance path (Section 9); configuration item families and mandatory attributes (Section 9); approved-baseline rule and secure baseline contents (Sections 9, 14); drift classification and investigation trigger (Section 9); change authorization attributes (Section 9); continuous configuration assurance monitoring and compliance scoring (Section 11); Artifact Factory outputs used as configuration acceptance evidence (Section 12); executive configuration reporting content (Section 11); Scenario 3 case study (Section 13) |
| docs/reference-implementations/index.md | Reference implementation definition and Build-pillar framing (Section 10); four-step contribution sequence (Section 10); registered index entry and its realized/mitigated identifiers as read (Section 10) |
| docs/architecture/ENTERPRISE_OPERATING_MODEL.md (EAODS-ARCH-EOM-001) | House structure and front matter conventions; four pillars and Volume 10 north-star role (Section 3); decision and accountability model (Section 5); AI operating boundaries (Section 5); reference implementation requirements (Section 10); precedence of current artifacts over historical drafts (Sections 2, 14) |
| docs/architecture/architecture-principles.md (EAODS-ARCH-PRIN-001) | House section structure and tone; governance-precedes-automation entry condition (Section 3); named ownership and evidence-precedes-assertion framing (Sections 5, 12); ADR-0002 traceability chain (Section 5); escalation rather than silent rejection (Section 14); review-gate construction (Section 15) |
