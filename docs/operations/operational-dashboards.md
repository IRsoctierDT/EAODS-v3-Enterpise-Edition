---
title: EAODS Operational Dashboard Specifications
document_id: EAODS-OPS-DASH-001
version: 1.0.0
status: proposed
owner: Enterprise Platform Operations Center
review_gate: Platform Engineering Leadership and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - EAODS-ARCH-EOM-001
  - EAODS-ARCH-GOV-001
  - ADR-0002
  - STD-0002
  - PAT-0002
  - PAT-0003
  - RUN-0002
  - SVC-00387
  - docs/frameworks/EAODS-v17.3/volume-10-platform-operations.md
  - docs/frameworks/EAODS-v17.3/volume-12-metrics-kpis-kris.md
  - history/original-sources/conversation-evidence/EAODS_v4_6_ECT_full_transmission_2026-07-26.md
---

# EAODS Operational Dashboard Specifications

## 1. Purpose

This document specifies the operational dashboards through which EAODS is observed: which panels exist, which measurements feed them, how often those measurements are expected to move, and what decision each panel is built to support. It exists because Volume 10 makes the Enterprise Platform Operations Center (EPOC) the operational authority for platform health and requires that leadership receive continuous, authoritative visibility into service health, while Volume 12 requires that every reported metric identify its authoritative source and calculation methodology. A dashboard that displays a number without a registered owner, source, and calculation is reporting, not measurement.

The specification separates dashboards by audience rather than by subsystem. The same underlying measurement can appear in more than one view; what changes between views is aggregation, refresh expectation, and the decision the view is answerable for.

## 2. Scope and governing authority

This specification covers three audiences: the Executive Control Tower, the EPOC operational floor, and the service owner. It governs panel composition and metric sourcing only. It does not define metrics; metric definition, approval, and retirement remain under the Volume 12 metric lifecycle and change control.

Authority is layered. EAODS v17.3 Volume 10 is the operational north star and places the Executive Control Tower above the EPOC in the reference architecture, with Continuous Assurance evidence flowing back to the Control Tower. Volume 12 supplies the measurement architecture — operational telemetry to the Enterprise Data Platform, through the metrics calculation engine, into the KPI catalog, KRI catalog, and engineering analytics, and onward to the Executive Control Tower and board reporting. The v4.6-alpha Executive Control Tower Specification supplies the Control Tower dashboard architecture, panel field tables, health rules, alert triggers, and the recommendations engine.

**Evidence class.** The v4.6 Control Tower transmission is conversation-derived evidence (grade B), retained verbatim and explicitly not promoted to a canonical artifact without owner-approved bounded reconstruction. This document is such a bounded reconstruction and is proposed, not accepted; panels traced solely to that transmission inherit its evidence class until the review gate in Section 12 is passed.

## 3. Audiences and decision rights

| Audience | View | Question the view answers | Accountable for the view |
|----------|------|---------------------------|--------------------------|
| Executive Control Tower | Enterprise summary and scorecard | Is the enterprise reliable, defensible, compliant, and ready to release? | Executive Control Tower, reporting to board reporting |
| EPOC operational | Operational floor | What is degrading, blocked, or unevidenced right now, and who owns it? | Enterprise Platform Operations Center |
| Service owner | Single-service drill-down | Is my service meeting its objectives, and may it take further change? | The service's engineering, operational, and business owners |

Aggregation ascends; authority does not. A service owner acting on a drill-down does not thereby exercise executive judgement, and an executive view that contradicts a service view is resolved by inspecting the metric's authoritative source, not by preferring the higher panel.

## 4. Panel register

Every panel admitted to any dashboard is recorded in the panel register. The register describes panels; the metric catalog described in Volume 12 remains the source of truth for the measurements themselves.

| Field | Content |
|-------|---------|
| Panel name | Canonical name of the panel as displayed |
| Audience | Executive Control Tower, EPOC operational, or service owner |
| Source metrics | The registered metrics rendered by the panel |
| Metric classification | KPI, KRI, KCI, KMI, diagnostic metric, or informational metric |
| Authoritative source | The system of record supplying the measurement |
| Measurement frequency | Frequency at which the underlying metric is measured |
| Reporting frequency | Frequency at which the panel is reported into governance |
| Business owner | Accountable owner of the reported outcome |
| Technical owner | Accountable owner of the calculation and feed |
| Calculation authority | Authority that owns the approved formula |
| Validation authority | Authority that verifies the measurement is correct |
| Confidence level | Confidence assigned to the panel's inputs |
| Executive dashboard flag | Whether the panel is promoted to executive reporting |
| Review frequency | Cadence at which the panel itself is reassessed |
| Retirement criteria | Conditions under which the panel is withdrawn |

Panels follow the Volume 12 metric lifecycle: definition, approval, implementation, validation, operational reporting, executive review, and continuous improvement. A panel is not displayed before validation. A withdrawn panel remains historically traceable, in the same way deprecated metrics do.

## 5. Executive Control Tower dashboard

The Control Tower provides a unified operational view suitable for engineering leadership, security teams, compliance officers, and executive stakeholders, and is responsible for continuous operational awareness rather than document generation. Its dashboard architecture comprises Executive Overview, Workflow Operations, Governance and Risk, Evidence Operations, Knowledge Memory, Artifact Factory, Publishing Operations, Repository Health, Agent Performance, and Executive Recommendations. Sections 5 and 6 assign those areas to the audience that acts on them.

### 5.1 Executive Overview

| Panel | Source metrics | Refresh expectation | Decision use |
|-------|----------------|---------------------|--------------|
| Workflow position | Active Workflows; Completed Workflows; Blocked Workflows | Continuous | Whether delivery is progressing or accumulating blockage awaiting approval or dependencies |
| Risk exposure | High-Risk Items (Tier 4–5 activities) | Continuous | Whether restricted and approval-required activity is within tolerance |
| Assurance coverage | Evidence Coverage; Documentation Coverage | Continuous | Whether claims made to the board are evidenced |
| Knowledge trust | Knowledge Reliability (average repository reliability score) | Continuous | Whether decisions resting on retrieved knowledge are safe to make |
| Release position | Release Readiness | Continuous | Whether a release may be approved |

### 5.2 Governance and risk queue

The risk queue presents count and status by tier: Tier 1 informational, Tier 2 monitor, Tier 3 review, Tier 4 executive approval required, Tier 5 restricted execution. The decision use is direct — Tier 4 rows are an executive approval work queue, and Tier 5 rows are an execution restriction that the panel exists to make undeniable.

### 5.3 Executive scorecard

The scorecard summarizes enterprise availability, cyber defense readiness, engineering maturity, compliance posture, operational resilience, strategic risks, platform investment effectiveness, and trend analysis. Historical trends accompany current-state reporting; a scorecard panel presenting a current value without its trend is incomplete.

The Engineering Health Index aggregates reliability, security, deployment quality, observability, operational maturity, automation quality, technical debt, and compliance status into a single executive-level indicator while preserving drill-down capability. The index is displayed only with its drill-down path intact, so that an executive reading a degraded index can reach the contributing service views in Section 7.

Enterprise availability is reported from the Platform Availability metric, whose canonical definition assigns the Enterprise Platform Operations Center as metric owner, the Enterprise Data Platform as authoritative source, hourly measurement, monthly reporting, a target of 99.95 percent, high confidence, and executive dashboard promotion. That definition is the worked example of every field the panel register requires.

### 5.4 Executive recommendations

The recommendations panel presents prioritized recommendations ranked by operational impact, governance risk, publication dependency, and executive priority. Its decision use is sequencing: it converts the state shown by the other panels into an ordered set of actions. AI-assisted analytics may support anomaly detection, trend identification, metric summarization, executive briefing generation, predictive analytics, and operational forecasting within this panel; executive decisions continue to rely upon validated enterprise evidence, and a recommendation is never itself the evidence.

## 6. EPOC operational dashboard

The EPOC dashboard is the working view for service operations, site reliability engineering, capacity engineering, platform performance, service ownership, operational analytics, platform optimization, and operational governance.

### 6.1 Workflow operations

Each workflow exposes Workflow ID, Owner, Assigned Agent, Current Phase (intake, planning, execution, QA, approval, published), Progress, Last Activity, Estimated Completion, and Blocking Issues. Refresh is continuous; Last Activity is itself the staleness signal the panel is read for. Decision use is assignment and unblocking: the panel identifies which workflows have an owner but no movement, and which are held at approval rather than in execution.

Workflow health is classified on the same panel:

| State | Conditions | Decision use |
|-------|-----------|--------------|
| Healthy | Progressing normally; evidence complete; approvals current | No action |
| Warning | Stalled longer than threshold; incomplete documentation; missing evidence | Operational follow-up by the workflow owner |
| Critical | High-risk activity without approval; failed QA; missing governance records | Immediate escalation; the condition is a governance failure, not a delay |

### 6.2 Evidence operations

| Panel | Source metrics | Refresh expectation | Decision use |
|-------|----------------|---------------------|--------------|
| Evidence production | Evidence records created; evidence attached per workflow | Continuous | Whether evidence is being emitted as activity runs (PAT-0003) |
| Evidence integrity | Hash verification status; missing source references | Continuous | Whether existing evidence can be trusted |
| Evidence currency | Evidence aging; evidence sensitivity distribution | Continuous | Whether evidence has decayed, and whether handling matches sensitivity |
| Evidence Health | Verified Evidence ÷ Required Evidence × 100, target at or above 95 percent | Continuous | Whether the assurance position supports the claims in Section 5.1 |

### 6.3 Knowledge Memory

The Control Tower consumes outputs from the Knowledge Memory subsystem: total indexed documents, canonical documents, duplicate documents, stale documents, average reliability score, retrieval QA success rate, knowledge graph nodes, knowledge graph relationships, and chunk inventory. Reliability is banded as excellent at 90 and above, good at 80 to 89, moderate at 70 to 79, and review required below 70. Decision use is remediation queueing — duplicates for reconciliation, stale documents for refresh, and any corpus falling into the review-required band for owner attention before its content is relied upon.

### 6.4 Artifact Factory and publishing operations

The Artifact Factory panel displays SOPs generated, policies generated, case studies generated, client deliverables, portfolio assets, evidence binders, and release bundles, with each artifact carrying QA score, review status, publication status, owner, and version. Publishing Operations monitors release candidates, pending releases, public bundles, private bundles, changelog generation, repository mapping status, and documentation completeness. The release readiness score combines documentation completeness, QA score, evidence completeness, approval status, and publication checklist completion; it is the same figure surfaced to the executive view in Section 5.1, and the decision it supports is whether the release threshold is met.

### 6.5 Repository health

Repository metrics comprise Markdown documents, YAML specifications, runtime modules, automated tests, documentation coverage, orphaned files, deprecated artifacts, and duplicate content. The repository maturity score sums documentation, governance, knowledge, testing, publishing, and automation to a maximum of 100. Decision use is prioritization of maintenance work against the weakest contributing component rather than against the aggregate.

### 6.6 Agent operations

Each registered agent reports Tasks Assigned, Completed Tasks, Average Completion Time, QA Pass Rate, Escalations, and Failure Rate. Agents requiring repeated intervention are automatically flagged for review. The panel's decision use is bounded: it informs workload rebalancing and review of agent behaviour, and it is the operational surface for the requirement that AI assistance remain observable and subject to human approval for material actions.

## 7. Service owner dashboard

The service owner view is the drill-down target for the Engineering Health Index and the operational floor alike. It is scoped to one production service.

| Panel | Source metrics | Refresh expectation | Decision use |
|-------|----------------|---------------------|--------------|
| Service Health Score | Availability; latency; error rate; deployment stability; dependency health; security posture; recovery readiness | Recalculated automatically using governed measurement logic | Whether the service is healthy, and which of the seven components is responsible when it is not |
| Service level position | SLI measured against SLO, and SLA where a business commitment applies | Per the registered measurement frequency of each SLI | Whether observed behaviour is meeting the objective derived from it |
| Error budget | Remaining error budget for the measurement window | Per the SLI measurement frequency | Whether further production change is permitted (PAT-0002) |
| Ownership | Business owner; engineering owner; operational owner; executive sponsor; recovery authority; architecture authority; assurance owner | On change | Who is called, and by what authority, when any panel above degrades |

Service level objectives are based on observed service behaviour rather than aspirational targets, so a service owner disputing an SLO panel disputes the observation window, not the ambition. An exhausted error budget triggers engineering review before additional production changes; the error budget panel is therefore a change gate rendered as a number, and the response procedure is RUN-0002.

Ownership is displayed from the canonical service ownership record, whose fields are demonstrated by SVC-00387: service identifier, service name, service owner, operations owner, executive sponsor, availability target, reliability classification, error budget policy, and continuous validation status. Ownership remains continuously documented; a service whose ownership panel is incomplete is not fully governed by Volume 10.

## 8. Refresh and reporting cadence

Refresh has two distinct meanings and both are recorded per panel. Measurement frequency is how often the underlying metric is calculated. Reporting frequency is how often the panel is carried into a governance forum.

| Class | Applies to | Basis |
|-------|-----------|-------|
| Continuous | Control Tower summary and EPOC operational panels | The Control Tower presents a real-time operational summary and maintains continuous operational awareness |
| Automatic recalculation | Service Health Score | Scores are recalculated automatically using governed measurement logic |
| Declared measurement frequency | All catalogued metrics | The measurement frequency field of the metric's canonical definition, hourly in the Platform Availability example |
| Declared reporting frequency | Executive scorecard and KPI panels | The reporting frequency field of the metric's canonical definition, monthly in the Platform Availability example |

No panel asserts a refresh interval that its registered metric does not support. Where a source does not state a frequency for a measurement, the panel inherits the frequency declared for that metric rather than asserting one of its own.

Reporting cadence follows the review cycles the governing volumes already declare: weekly operations review, monthly reliability review, quarterly capacity forecast, and annual operational excellence certification for platform operations; monthly executive metrics review, quarterly KPI and KRI assessment, and annual enterprise performance certification for the measurement framework.

## 9. Alerting

Alerts are the subset of panel states that must interrupt rather than wait to be read. Automatic alerts trigger when a Tier 5 activity lacks approval, when evidence is missing for regulated workflows, and when publication occurs before QA completion. The workflow critical state in Section 6.1 alerts on the same principle: high-risk activity without approval, failed QA, and missing governance records are governance failures and are routed as such.

Alerting does not create authority. An alert names the condition, the affected object, and the accountable owner from the panel register; disposition remains with the authority that owns the decision.

## 10. Data quality and confidence

Panel inputs are evaluated for completeness, accuracy, consistency, timeliness, lineage, provenance, and calculation reproducibility. Low-confidence metrics are clearly identified within executive reports; a panel does not silently render a low-confidence input as though it were high-confidence, and the confidence level field of the panel register is displayed rather than stored only.

Each Volume 12 measurement domain maintains an assigned measurement owner, and panels inherit that ownership: platform engineering for reliability and delivery, cybersecurity operations for defensive effectiveness, DevSecOps for secure software delivery, automation for AI operational performance, identity for trust and access health, security engineering for platform protection, governance for policy compliance, continuous assurance for validation effectiveness, executive operations for organizational performance, and enterprise risk for strategic risk posture.

## 11. Traceability

Every panel is traceable from displayed value to authoritative source: operational telemetry, the Enterprise Data Platform, the metrics calculation engine, the KPI or KRI catalog, and the Executive Control Tower. Panels, their source metrics, and their owning services are registered as nodes and edges under STD-0002 so the relationship between a degraded executive indicator and the services beneath it is machine-readable rather than inferred. Continuous Assurance independently verifies operational evidence, and the Control Tower reports from validated evidence.

## 12. Human review gate

Approval by Platform Engineering Leadership and the Program Owner requires confirmation that:

- no metric, panel, threshold, alert trigger, organizational unit, or capability has been introduced beyond those in the sources listed in Section 13;
- every panel names its source metrics, refresh expectation, and decision use;
- the panel register defines fields and lifecycle without asserting metric identifiers, which remain the property of the Volume 12 catalog under change control;
- executive aggregation preserves drill-down to the service views in Section 7;
- the error budget panel is stated as a change gate without weakening;
- the grade-B evidence class of the v4.6 Control Tower transmission is carried, not erased, by this reconstruction.

Because this document defines executive reporting content, its adoption is additionally subject to the review that governs executive reporting under the architecture governance model.

## 13. Sources and traceability

| Source (repo-relative path) | Contribution |
|-----------------------------|--------------|
| history/original-sources/conversation-evidence/EAODS_v4_6_ECT_full_transmission_2026-07-26.md (v4.6-alpha, conversation-derived evidence, grade B) | Control Tower purpose, audience, and executive objectives (Sections 1, 5); dashboard architecture areas (Section 5); Executive Overview primary KPI names (Section 5.1); risk tier queue and statuses (Section 5.2); recommendations engine and ranking factors (Section 5.4); workflow field table and health rules (Section 6.1); evidence metrics and Evidence Health formula with its 95 percent target (Section 6.2); Knowledge Memory metrics and reliability bands (Section 6.3); Artifact Factory and Publishing Operations metrics, release readiness composition (Section 6.4); repository health metrics and maturity score composition (Section 6.5); agent operations metric table and repeat-intervention flagging (Section 6.6); automatic alert triggers (Section 9); real-time and continuous-awareness basis for the continuous refresh class (Section 8); evidence-class caveat and non-promotion condition (Sections 2, 12) |
| docs/frameworks/EAODS-v17.3/volume-12-metrics-kpis-kris.md | Requirement that every metric identify authoritative source and calculation methodology (Section 1); enterprise measurement architecture from telemetry to board reporting (Sections 2, 11); canonical metric definition fields and the Platform Availability worked example — owner, authoritative source, hourly measurement, monthly reporting, 99.95 percent target, confidence, executive dashboard promotion (Sections 4, 5.3, 8); metric classification set (Section 4); metric lifecycle and historical traceability of deprecated items (Section 4); metric governance fields — business owner, technical owner, calculation authority, validation authority, reporting audience, review frequency, retirement criteria (Section 4); executive scorecard contents and trend requirement (Section 5.3); Engineering Health Index composition and drill-down preservation (Section 5.3); Service Health Score components and automatic recalculation (Section 7); AI-assisted analytics scope and the primacy of validated evidence (Section 5.4); data quality dimensions and low-confidence identification (Section 10); measurement domains and assigned measurement owners (Section 10); review cycle for the measurement framework (Section 8) |
| docs/frameworks/EAODS-v17.3/volume-10-platform-operations.md | EPOC as operational authority and the requirement for continuous executive visibility into service health (Sections 1, 2); reference architecture placing the Executive Control Tower above the EPOC with assurance evidence returning to it (Sections 2, 11); operational capability domains used to scope the EPOC dashboard (Section 6); service level framework — SLI, SLO, SLA, error budget — and the observed-behaviour basis for objectives (Section 7); error budget exhaustion as a change gate before further production change (Section 7); service ownership framework roles and the canonical service ownership record fields demonstrated by SVC-00387 (Section 7); Continuous Assurance independent verification of operational evidence (Section 11); platform operations review cycle (Section 8) |
| docs/architecture/ENTERPRISE_OPERATING_MODEL.md (EAODS-ARCH-EOM-001) | Volume 10 as operational north star and the operational elements it defines (Section 2); requirement that services have named owners and measurable reliability objectives, and that controls map to evidence, implementation, and operations (Sections 4, 7); AI operating boundaries — observable, auditable, bounded, human-approved for material actions — applied to the agent operations panel (Section 6.6) |
| docs/architecture/architecture-governance-model.md (EAODS-ARCH-GOV-001) | House style — front matter fields, numbered sections, governed prose and table conventions, human review gate and sources-and-traceability formatting; the principle that consultation does not transfer authority, applied to alerting and to audience decision rights (Sections 3, 9); the governance review that applies to executive reporting content (Section 12) |
