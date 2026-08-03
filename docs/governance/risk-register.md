---
title: EAODS Risk Management and Risk Register
document_id: EAODS-GOV-RISK-001
version: 1.0.0
status: proposed
owner: Enterprise Governance Office
review_gate: Enterprise Governance Board and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - EAODS-ARCH-GOV-001
  - EAODS-ARCH-EOM-001
  - EAODS-SEC-AIRISK-001
  - ADR-0002
  - STD-0001
  - THR-0002
  - PAT-0003
  - RUN-0003
  - docs/architecture/architecture-governance-model.md
  - docs/security/ai-risk-management.md
  - history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v4.17.1-v4.28/EAODS-v4.20-alpha-enterprise-security-exceptions-and-risk-acceptance-standard.md
  - history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v10.0.0-alpha-enterprise-business-continuity-governance-crisis-communicati.md
---

# EAODS Risk Management and Risk Register

## 1. Purpose

This document defines how EAODS Enterprise Edition classifies risk, rates it, records it, treats it, accepts it, reviews it, and reports it. It establishes the risk taxonomy, the rating method, the fields every risk record carries, the treatment options available, the authority required to accept residual risk at each rating, the review cadence that keeps an accepted risk from becoming a permanent one, and the operation of the register itself.

It exists because the enterprise governance position is explicit: risk may be accepted by accountable leadership, but risk may not be ignored, buried, or silently deferred. Risk acceptance is a governance action, not a technical closure shortcut. Its purpose is to prevent unmanaged risk from being hidden inside remediation backlogs, operational constraints, or informal business decisions. Any decision not to remediate a validated issue within the expected timeframe shall be documented, approved, time-bound, reviewed, and visible to executive stakeholders.

## 2. Scope and governing authority

The register covers every risk that EAODS governs as an enterprise object, spanning three surfaces: security and control deviations, AI and automation risk, and business continuity risk.

Authority is layered. EAODS v17.3 Volume 10 is the operational north star. ADR-0002 constitutes the four-pillar operating model and reserves material change to it for board review and Program Owner approval. EAODS-ARCH-GOV-001 supplies the governance bodies, decision authorities, RACI assignments, escalation path, cadences, and decision-record fields that this document applies to risk work; it also establishes that an exception is an approved, recorded, time-bound deviation and that a deviation which has not been through the responsible board is a defect, not an exception. EAODS-SEC-AIRISK-001 governs risk arising from models, prompts, tools, and agents, and this document reuses its classifications rather than restating them.

The Enterprise Governance Office owns this document. Ownership of the document confers no approval authority over any individual risk decision; approval authority is exclusively as stated in Section 8.

**Naming reconciliation.** The v4.20 acceptance authority matrix names the top approver the Executive Governance Committee. EAODS-ARCH-GOV-001 names the highest decision-making authority for EAODS governance the Enterprise Governance Board, and assigns it accountability for risk acceptance review. These refer to one body. This document uses **Enterprise Governance Board (EGB)** throughout. No new body is created by this reconciliation and no authority is transferred by it.

## 3. Risk management principles

1. Risk may be accepted by accountable leadership; it may not be ignored, buried, or silently deferred.
2. Risk acceptance is a governance action, not a technical closure shortcut.
3. Risk classification precedes validation; validation depth and approval authority follow from the assigned tier.
4. Human accountability is non-delegable and cannot be discharged by an automated approval.
5. Accepted risk shall be visible, not buried.
6. Evidence is generated as a by-product of operation, not assembled after the fact.
7. Risk governance is risk-driven, evidence-based, policy-governed, role-accountable, communication-centric, continuously exercised, measurable, and continuously improved.
8. No one may approve risk acceptance for an asset, system, or business process they do not own or govern.

## 4. Risk taxonomy

The taxonomy has three branches. A risk record is classified into exactly one branch and one category within it; cross-branch effects are captured through record relationships (Section 12) rather than by duplicate classification.

### 4.1 AI and automation risk

| Category | What can go wrong |
|---|---|
| Model risk | Functional error, degraded accuracy, unexplainable output, unfair or inconsistent outcomes |
| Drift and regression risk | Prediction, data, or concept drift; benchmark degradation; undetected regression on revision |
| Instruction and content risk | Direct injection, indirect prompt manipulation, instruction hierarchy violation, context manipulation |
| Retrieval and knowledge risk | Retrieval poisoning, unauthorized data disclosure, ungoverned persistent memory |
| Tool and workflow risk | Tool misuse, workflow abuse, execution beyond approved boundaries |
| Identity and privilege risk | Anonymous execution, excessive capability, privilege escalation attempts, credential compromise, cross-agent laundering |
| Autonomy and oversight risk | Autonomous action beyond approved authority; material decisions taken without human accountability |
| Assurance risk | Unvalidated deployment, irreproducible evaluation, incomplete evidence |

### 4.2 Security and control-deviation risk

Risk in this branch arises wherever a validated security issue is not remediated on the expected schedule, or an approved control is not applied as written. The governed surfaces are vulnerability remediation deferrals; accepted security findings; penetration test findings not immediately remediated; compensating-control decisions; scan exceptions; cloud configuration exceptions; endpoint and server hardening exceptions; identity and access exceptions; AI-agent governance exceptions; publication risk exceptions; and compliance-impacting exceptions.

### 4.3 Continuity and crisis risk

Risk in this branch is risk to essential operations. It is organized by the continuity capability domains: crisis governance, business continuity, communications, cyber operations under Domain 03, recovery, legal and regulatory obligations, human resources and workforce continuity, and vendor coordination.

## 5. Rating method

### 5.1 Enterprise risk levels

Every risk record carries one enterprise risk level. The level drives acceptance authority (Section 8) and review interval (Section 9).

| Level | Meaning in the register |
|---|---|
| Low | Residual exposure the asset owner may carry |
| Medium | Residual exposure requiring business ownership and security review |
| High | Residual exposure requiring executive sponsorship and security leadership |
| Critical | Residual exposure requiring enterprise governance decision |
| Regulated / legal impact | Any level where regulatory or contractual obligations are engaged; treated as an overlay that raises authority, not as a separate severity |
| Active exploitation context | Overlay applied when exploitation is observed; forces continuous executive review |

### 5.2 Required risk analysis

A rating is not asserted; it is supported. Each request to record, defer, or accept a risk shall evaluate: technical severity; operational priority; affected asset criticality; exposure level; data classification; exploitability; known exploited status; business dependency; remediation complexity; available compensating controls; regulatory or contractual impact; and expected remediation timeline.

### 5.3 Classification ladders that feed the rating

Where the risk concerns an already-classified enterprise object, the object's own classification is recorded on the risk and constrains the rating and the approval path rather than being re-derived.

| Ladder | Range | What it determines |
|---|---|---|
| Model risk tier | MR-0 experimental through MR-5 mission-critical / executive decision support | Validation depth and approval authority for the model |
| Autonomy classification | AT-0 human execution only through AT-5 enterprise-approved autonomous workflows with continuous oversight | Strength of governance controls and oversight gates |
| Agent trust level | T0 untrusted through T5 executive certified | Whether privileged execution is permitted |
| Trust assurance level | TA-0 experimental through TA-5 executive certified | Operational deployment eligibility |
| Continuity classification | BC0 non-essential through BC4 mission essential | Recovery priority and communication requirements |

### 5.4 Scoring boundary

The sources read for this document (Section 16) define risk levels, overlay conditions, factor sets, and classification ladders; they do not define a single numeric enterprise scoring formula. The v4.20 standard defers vulnerability scoring to the AI-assisted vulnerability prioritization scoring model it extends, which was not among the sources read here. Identity risk scoring for agent identities weighs privilege level, trust history, anomalous behavior, credential age, capability sensitivity, operational exposure, and policy violations, and elevated scores trigger additional policy evaluation. Where a scoring model applies, the risk record cites it by identifier rather than restating it.

## 6. Risk record schema

Identifiers for risk records are allocated under the registered-prefix discipline of STD-0001. No identifier is minted in this document; the fields below describe what a record carries, not any specific record. Every record names an asset owner and, once treated, an implementation owner accountable for remediation or renewal; a record that names no accountable owner is not a governed risk and is not eligible for acceptance.

### 6.1 Core fields

| Field | Required | Purpose |
|---|:---:|---|
| Risk or exception identifier | ✓ | Stable handle for the record |
| Related finding identifier | ✓ | The validated finding the risk derives from |
| Asset identifier | ✓ | The governed object exposed |
| Asset owner | ✓ | Named accountable owner of that object |
| Exception or treatment type | ✓ | Classification from Section 7 |
| Risk level | ✓ | Rating from Section 5.1, with overlays applied |
| Risk description | ✓ | What can go wrong, in the taxonomy terms of Section 4 |
| Business justification | ✓ | Why the business cannot absorb immediate remediation |
| Technical justification | ✓ | Why the technical remediation cannot proceed on schedule |
| Residual risk statement | ✓ | What exposure remains after treatment |
| Compensating controls | ✓ | Control name, implementation status, and evidence reference for each |
| Approver and approver role | ✓ | The individual exercising the authority in Section 8, and the authority exercised |
| Approval date and expiration date | ✓ | When the acceptance took effect, and when it lapses absent renewal, remediation, or revocation |
| Review frequency | ✓ | Interval from Section 9 |
| Evidence references | ✓ | Links to scanner output, advisories, test results, and impact statements |
| Revocation conditions | ✓ | Conditions that terminate the acceptance before expiration |
| Status | ✓ | State from Section 10 |

### 6.2 Decision fields

Because risk acceptance is a governance decision, an accepted record additionally carries the fields required of every governance decision: decision identifier; meeting reference; participants; rationale; alternatives considered; supporting evidence; affected standards; implementation owner; review date; and follow-up actions.

### 6.3 Conditional fields

| Applies when | Additional fields |
|---|---|
| The risk concerns an AI model, prompt, tool, or agent | Affected models; affected agents; trust impact; containment actions; corrective actions; approval authority; closure evidence |
| The risk affects an essential business function | Critical business function; executive owner; recovery objectives; communication strategy; dependency inventory; alternate operating procedures; validation schedule; maximum tolerable disruption |

## 7. Treatment options

Remediation on schedule is the default and requires no register entry beyond closure evidence. Every other outcome is a governed deviation and is recorded.

| Treatment | Description |
|---|---|
| Remediation deferral | Fix is delayed beyond normal service-level expectation |
| Risk acceptance | Business owner accepts residual risk |
| Compensating control exception | Alternative control reduces but does not eliminate risk |
| Scope exception | Asset or system excluded from scan or assessment |
| Policy exception | Temporary deviation from approved EAODS policy |
| Technical constraint exception | Remediation blocked by architecture, vendor, or compatibility issue |
| Business continuity exception | Temporary risk accepted to preserve critical operations |

### 7.1 Compensating control requirements

A compensating control shall be specific, implemented, testable, monitored, documented, mapped to the accepted risk, and reviewed before approval. Unimplemented future controls do not qualify as compensating controls. Control forms named in the source include network segmentation, web application firewall rules, endpoint detection controls, multi-factor authentication enforcement, restricted access, additional logging, temporary service isolation, configuration guardrails, rate limiting, and manual monitoring.

### 7.2 Prohibited uses

A register entry shall not be used to hide unresolved critical vulnerabilities; bypass executive review; avoid remediation due to convenience; suppress findings without evidence; mark untested fixes as complete; excuse unauthorized scanning; override legal or regulatory obligations; or permanently accept risk without review.

## 8. Acceptance authority thresholds

Every acceptance carries exactly one approval authority. Consultation does not transfer authority, and human approval for risk acceptance is mandatory and non-delegable.

| Risk level | Minimum approver |
|---|---|
| Low | Asset Owner |
| Medium | Business Owner and Security Reviewer |
| High | Executive Sponsor and Security Lead |
| Critical | Enterprise Governance Board |
| Regulated or legal impact | Enterprise Governance Board with Legal and Compliance review |

Two overlays apply. The Enterprise Risk Council performs enterprise and residual risk review, risk acceptance oversight, and key risk indicator monitoring; the Domain Owner is responsible for the submission; the EGB is accountable for the risk acceptance review. Risk treatment strategies for AI systems are approved by the AI Governance Council, whose approvals remain its own authority rather than the EGB's.

No one may approve risk acceptance for an asset, system, or business process they do not own or govern. A residual risk that exceeds approved enterprise tolerance is not granted at council level; it escalates under Section 11.

## 9. Review cadence and expiration

Every accepted risk has an expiration date. Before expiration it shall be renewed, remediated, or revoked. An expired record automatically returns to open-risk status.

| Risk level | Maximum review interval |
|---|---|
| Low | 12 months |
| Medium | 6 months |
| High | 90 days |
| Critical | 30 days |
| Active exploitation context | Continuous executive review |

Register operation runs against the governance cadences already in force: Enterprise Risk Council monthly, Change Advisory Board weekly, Enterprise Governance Board quarterly, and Executive Cybersecurity Review quarterly. The exception and risk acceptance standard itself carries a quarterly review cycle; continuity plans carry a semi-annual review with an annual enterprise continuity exercise.

## 10. Register lifecycle

A record moves through: Requested; Under Review; then either Rejected or Needs Revision, or forward to Approved; then Active; then either Expired, Revoked, or Renewed; and finally Closed by Remediation.

The operating sequence behind those states is fixed. A validated finding cannot be remediated on schedule; remediation feasibility is reviewed; a request is created with evidence attached; risk analysis is performed against Section 5.2; compensating controls are reviewed and validated; the residual risk statement is documented; the approval authority of Section 8 is confirmed and the decision recorded; executive reporting is updated; periodic review is scheduled at the Section 9 interval; and the record ends in expiration, renewal, remediation, or revocation. A record that cannot satisfy its gate is not closed silently; it escalates under Section 11 with its rationale, impact analysis, and the unresolved point stated.

## 11. Escalation

Escalation follows the fixed governance path: operational issue, Domain Owner, Governance Manager, the Architecture, AI, or Risk Council as the subject requires, Enterprise Governance Board, Executive Leadership.

Escalation is mandatory when a critical finding is proposed for acceptance; a high-risk record is renewed more than once; compensating controls fail; active exploitation emerges; the asset becomes internet-facing; the asset begins handling more sensitive data; ownership changes; remediation is delayed beyond the accepted expiration date; record evidence is incomplete; or the record conflicts with regulatory obligations.

Escalation is likewise mandatory under the enterprise triggers: enterprise risk exceeds approved tolerance; regulatory obligations are affected; architectural conflicts cannot be resolved; AI governance issues impact safety or compliance; or critical security incidents require executive direction.

## 12. Register operation

### 12.1 Executive visibility

Executive reporting shall present active records; records by risk level; records nearing expiration; expired records; repeated renewals; accepted critical risks; record owners; compensating-control failures; and business units carrying residual risk. Governance reporting adds overdue approvals, unresolved escalations, and ownership coverage.

### 12.2 Retention and relationships

Knowledge Memory retains record history; accepted-risk rationale; compensating-control evidence; renewal decisions; remediation outcomes; recurring exception patterns; and asset-level residual-risk history. This retention is what allows EAODS to identify repeated risk acceptance patterns and weak remediation discipline, which is the register's principal analytic purpose beyond individual records. Register entries maintain governed relationships with business services, continuity plans, executive decisions, incidents, communications, dependencies, recovery procedures, evidence, corrective actions, and resilience metrics.

### 12.3 Derived artifacts

Generated outputs include the risk acceptance memo, exception request form, compensating-control validation checklist, executive residual-risk summary, renewal review packet, expired exception report, remediation deferral justification, and board-level risk register extract. Continuity-side outputs include the Business Impact Assessment Register and the Executive Decision Log.

## 13. Continuity and crisis interface

During a disruptive event the register is an input to executive decision support rather than a parallel process. Executive decision support packages include current operational status, business impact assessment, dependency analysis, regulatory considerations, risk assessment, response options, recommended actions, and supporting evidence. Executive situation reports carry a required Risks attribute alongside report identifier, event summary, operational status, executive decisions, outstanding actions, and next review time. AI-generated recommendations are decision support and remain subject to organizational approval policies, and public communications are approved according to organizational governance before release.

## 14. Known limitations

Three limitations are inherited from the sources and are tracked as governance exceptions rather than treated as solved. Drift is detected rather than prevented, so a model may operate degraded between monitoring intervals and governance review. Trust recalculation depends on the completeness of the evidence fed to it, so gaps in evidence generation degrade trust decisions silently. Instruction injection that steers an agent within its authorized scopes is not blocked by authorization and remains the standing residual identified in THR-0002, addressed by human review of consequential outputs and assurance-side anomaly detection under PAT-0003 and RUN-0003.

## 15. Human review gate

Approval of this document requires confirmation by the Enterprise Governance Board and the Program Owner that:

- no governance body, approval authority, risk level, review interval, or escalation trigger has been introduced beyond those in the cited sources;
- the EGB naming reconciliation in Section 2 creates no new body and transfers no authority;
- acceptance authority remains bound to ownership, and human approval of risk acceptance remains non-delegable;
- every accepted risk remains time-bound, reviewable, revocable, and visible in executive reporting;
- no sample risk identifiers have been minted by this document.

Changes affecting approval authority, exception eligibility, expiration rules, compensating-control requirements, escalation conditions, or executive reporting shall additionally undergo security governance review, risk management review, and legal or compliance review where applicable before adoption.

## 16. Sources and traceability

| Source (repo-relative path) | Contribution |
|---|---|
| `history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v4.17.1-v4.28/EAODS-v4.20-alpha-enterprise-security-exceptions-and-risk-acceptance-standard.md` | Core principle that risk may be accepted but not ignored, buried, or silently deferred, and that acceptance is a governance action (Sections 1, 3); governed deviation surfaces (Section 4.2); enterprise risk levels and the required risk analysis factor set (Sections 5.1, 5.2); deferral of vulnerability scoring to the prioritization scoring model it extends (Section 5.4); exception record field requirements and request template keys (Section 6.1); treatment and exception types (Section 7); compensating-control requirements, qualifying control forms, and the exclusion of unimplemented future controls (Section 7.1); prohibited uses (Section 7.2); risk acceptance authority matrix and the ownership rule for approvers (Section 8); expiration rules and maximum review intervals, quarterly standard review cycle (Section 9); exception status model and risk acceptance workflow (Section 10); mandatory escalation conditions (Section 11); Executive Control Tower display set, Knowledge Memory retention set, and Artifact Factory outputs (Sections 12.1, 12.2, 12.3); human review gate scope (Section 15) |
| `history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v10.0.0-alpha-enterprise-business-continuity-governance-crisis-communicati.md` (conversation-derived evidence, not canonical bytes) | Continuity governing principles applied to risk governance (Section 3); continuity capability domains as the continuity risk branch (Section 4.3); BC0–BC4 continuity classification and its effect on recovery priority and communication requirements (Section 5.3); mandatory continuity plan attributes as conditional record fields (Section 6.3); Knowledge Graph relationship set (Section 12.2); Business Impact Assessment Register and Executive Decision Log outputs (Section 12.3); executive decision support package contents, situation report attributes including the required Risks attribute, AI recommendations as decision support, and public communication approval (Section 13); semi-annual continuity review with annual enterprise continuity exercise (Section 9) |
| `docs/security/ai-risk-management.md` (EAODS-SEC-AIRISK-001) | AI risk taxonomy categories (Section 4.1); MR-0–MR-5 model risk tiers, AT-0–AT-5 autonomy classification, T0–T5 trust levels, TA-0–TA-5 assurance levels (Section 5.3); identity risk scoring factors (Section 5.4); risk-classification-precedes-validation, non-delegable human accountability, and evidence-as-by-product principles (Section 3); mandatory non-delegable human approval for risk acceptance (Section 8); safety incident fields reused as AI-conditional record fields (Section 6.3); drift, evidence-completeness, and in-scope injection residuals with their THR-0002, PAT-0003, and RUN-0003 anchors (Section 14) |
| `docs/architecture/architecture-governance-model.md` (EAODS-ARCH-GOV-001) | Layered authority and the definition of an exception as an approved, recorded, time-bound deviation, with an unreviewed deviation treated as a defect (Section 2); Enterprise Governance Board as highest governance authority, Enterprise Risk Council duties, AI Governance Council approval of AI risk treatment strategies, and the risk-acceptance RACI used for the Section 8 overlays; governance decision record fields (Section 6.2); escalation path and enterprise escalation triggers (Section 11); governance cadences (Section 9); overdue approvals, unresolved escalations, and ownership coverage in executive reporting (Section 12.1); escalation-not-silent-closure formulation (Section 10); house style for the naming reconciliation, human review gate, and sources table |
| `docs/architecture/ENTERPRISE_OPERATING_MODEL.md` (EAODS-ARCH-EOM-001) | House style — front matter fields, numbered sections, governed prose and table conventions; governance-precedes-automation and human-authority principles (Sections 1, 3); requirement that every major artifact has a named owner, used as the ownership rule (Section 6); ADR-0002 reservation of operating-model change to board review plus Program Owner approval (Section 2) |
