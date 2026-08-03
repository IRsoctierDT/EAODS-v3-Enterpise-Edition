---
title: EAODS AI Risk Management Guidance
document_id: EAODS-SEC-AIRISK-001
version: 1.0.0
status: proposed
owner: AI Governance Council
review_gate: Security Architecture Review Board and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - THR-0001
  - THR-0002
  - PAT-0001
  - PAT-0003
  - RUN-0003
  - EAODS-CTRL-000184
  - docs/frameworks/EAODS-v17.3/volume-05-automation-fabric-agent-runtime.md
  - history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v7.0-v8.3
---

# EAODS AI Risk Management Guidance

## 1. Purpose and scope

This guidance consolidates the EAODS position on managing risk arising from AI models, prompts, tools, and agents operating inside Cybersecurity Domain 03. It draws four historical standards into one operative document — model governance and validation (v7.4), trust, safety and human oversight (v7.5), agent identity and trust fabric (v7.6), and evaluation, benchmarking and red teaming (v7.9) — reconciled against the Automation Fabric of EAODS v17.3 Volume 5 and the approved threat model THR-0002.

Scope covers every AI capability that informs or executes enterprise work: registered models, production prompts and system instructions, authorized tools, persistent agent memory, and the agent identities that invoke them. Non-AI service identities are out of scope and remain governed by THR-0001 and PAT-0001; this document reuses those identity controls rather than restating them.

The operating premise is unchanged from the Enterprise Operating Model: governance precedes automation, AI assistance operates through least privilege and observable approval gates, and automation is an engineering capability governed by policy rather than an independent decision-making authority.

## 2. Risk management principles

1. Every production model, prompt, tool, and agent is a uniquely identifiable, owned enterprise asset.
2. Risk classification precedes validation; validation depth and approval authority follow from the assigned tier.
3. Model output is data, never authorization — every action is re-authorized against the invoking agent's approved capabilities.
4. Human accountability is non-delegable and cannot be discharged by an automated approval.
5. Trust is recalculated throughout execution, not established once at authentication.
6. No AI security capability enters production without documented assurance evidence.
7. Evidence is generated as a by-product of operation, not assembled after the fact.

## 3. AI risk taxonomy

The taxonomy below normalizes the risk surfaces named across the source standards into the categories used for classification, control selection, and assurance reporting.

| Risk category | What can go wrong | Primary source of control |
|---|---|---|
| Model risk | Functional error, degraded accuracy, unexplainable output, unfair or inconsistent outcomes | Model governance lifecycle (Section 4) |
| Drift and regression risk | Prediction, data, or concept drift; benchmark degradation; undetected regression on revision | Continuous monitoring and regression testing (Sections 8, 9) |
| Instruction and content risk | Direct injection, indirect prompt manipulation, instruction hierarchy violation, context manipulation | THR-0002 mitigations; prompt governance (Section 6) |
| Retrieval and knowledge risk | Retrieval poisoning, unauthorized data disclosure, ungoverned persistent memory | Governed corpus intake, memory governance (Section 6) |
| Tool and workflow risk | Tool misuse, workflow abuse, execution beyond approved boundaries | Tool Gateway and capability allowlists (Section 6) |
| Identity and privilege risk | Anonymous execution, excessive capability, privilege escalation attempts, credential compromise, cross-agent laundering | Trust Fabric controls (Section 5) |
| Autonomy and oversight risk | Autonomous action beyond approved authority; material decisions taken without human accountability | Autonomy classification and oversight gates (Section 7) |
| Assurance risk | Unvalidated deployment, irreproducible evaluation, incomplete evidence | Assurance Laboratory requirements (Section 9) |

## 4. Model risk classification and lifecycle

Every production model is registered in the enterprise Model Registry, the authoritative inventory. Registration records the model identifier, name, version, owner, business purpose, deployment scope, risk classification, status, and approval date.

| Tier | Description |
|---|---|
| MR-0 | Experimental |
| MR-1 | Internal Advisory |
| MR-2 | Operational Support |
| MR-3 | Business Decision Support |
| MR-4 | High-Impact Operational |
| MR-5 | Mission-Critical / Executive Decision Support |

Risk tier determines validation depth and approval authority. The governed lifecycle is registration, risk classification, validation and evaluation, governance approval, production deployment, continuous monitoring, retirement. Security review precedes validation and risk review precedes governance approval; no production deployment bypasses governance approval.

Validation covers functional validation, security assessment, adversarial testing, robustness evaluation, performance benchmarking, explainability assessment, governance review, and production readiness review. Minimum evaluation dimensions are accuracy, reliability, robustness, explainability, security, privacy, fairness, and operational efficiency. Each production model maintains a baseline benchmark, a production benchmark, acceptable variance thresholds, evaluation history, and regression history; benchmark approval is a precondition of production deployment.

Retirement removes the deployment, assesses dependencies, preserves and archives evidence, validates any replacement, and obtains governance approval. Historical model records remain immutable.

## 5. Agent identity and trust fabric controls

Every autonomous or semi-autonomous agent is a first-class enterprise identity governed with the rigor applied to privileged human identities. Agent identity is unique, non-transferable, cryptographically verifiable, continuously authenticated, least privileged, policy governed, auditable, and lifecycle managed. Anonymous or unmanaged autonomous execution is prohibited.

The identity lifecycle is registration, verification, credential issuance, capability assignment, production operation, continuous validation, credential rotation, retirement. Credentials declare issuing authority, validity period, rotation interval, revocation status, associated agent, and cryptographic profile; long-lived credentials are minimized in favor of short-lived, automatically rotated credentials, consistent with EAODS-CTRL-000184 and PAT-0001.

Authorization is capability-based: permissions are assigned as discrete capabilities — the source capability classes are telemetry read, evidence write, workflow execute, detection analysis, incident assistance, policy evaluation, report generation and recovery coordination, cited there as examples rather than as a closed set — rather than unrestricted administrative access. Capability inheritance is explicitly documented and approved, and delegated authority never exceeds the authority of the originating identity, carrying a defined maximum duration, approval authority, monitoring requirement, and automatic expiration.

| Trust level | Description |
|---|---|
| T0 | Untrusted |
| T1 | Registered |
| T2 | Authenticated |
| T3 | Policy Validated |
| T4 | Operationally Trusted |
| T5 | Executive Certified |

Trust evaluation considers credential validity, runtime integrity, behavioral history, policy compliance, workload attestation, execution context, security events, and evidence completeness, and is recalculated throughout execution. Before privileged execution, agents attest to approved software version, runtime integrity, approved configuration, verified identity, policy compliance, and security baseline; failed attestation prevents privileged execution. Federated agent communication requires mutual authentication, cryptographic identity verification, capability validation, policy evaluation, transaction auditing, and session lifecycle governance — implicit trust between enterprise domains is prohibited. Revocation is supported for compromise, retirement, policy violation, operational suspension, ownership transfer, and governance decision, and propagates immediately across the Trust Fabric.

Identity risk scoring weighs privilege level, trust history, anomalous behavior, credential age, capability sensitivity, operational exposure, and policy violations; elevated scores trigger additional policy evaluation. Runtime records such as the canonical agent metadata for AGENT-00128 in Volume 5 bind an agent to its class, required tools, approval level, and policy profile.

## 6. Runtime safety controls

| Control area | Requirement |
|---|---|
| Runtime policy enforcement | Tool invocations are evaluated through the enterprise policy decision point before execution |
| Capability allowlists | Execution is bounded to explicitly approved capabilities and operations |
| Tool authorization | Each tool declares identifier, authorized operations, required permissions, approval authority, risk classification, and audit requirements; tools never inherit unrestricted agent permissions |
| Prompt governance | Each production prompt or system instruction carries a unique identifier, approved owner, version history, authorized use cases, prohibited behaviors, validation evidence, rollback version, and retirement criteria; unauthorized modification is prohibited |
| Memory governance | Persistent memory complies with data minimization, retention, provenance, access control, lifecycle governance, auditability, and deletion procedures; updates generate evidence records |
| Runtime isolation | Identity isolation, permission isolation, resource quotas, network segmentation, execution monitoring, and secure termination per execution environment |
| Output validation | Model output is validated before it influences a privileged action |
| Monitoring and anomaly detection | Runtime monitoring, anomaly detection, rollback capability, escalation workflows, and immutable audit logging |

Every production model additionally declares its operational boundaries, prohibited uses, approved workflows, escalation criteria, human intervention points, and policy constraints.

## 7. Human oversight gates

Autonomy is classified before deployment, and higher autonomy requires progressively stronger governance controls.

| Level | Description |
|---|---|
| AT-0 | Human execution only |
| AT-1 | AI recommendations |
| AT-2 | Human-approved automation |
| AT-3 | Limited autonomous execution |
| AT-4 | Conditional autonomous operation |
| AT-5 | Enterprise-approved autonomous workflows with continuous oversight |

Human approval is mandatory and non-delegable for policy publication, model promotion, risk acceptance, regulatory communications, executive reporting, destructive operational actions, and modification of AI trust policy. Model governance adds mandatory human approval for mission-critical deployments, major model revisions, risk tier changes, executive-facing models, regulatory-impacting models, and safety-critical operational models. The Automation Fabric enforces approval points for strategic decisions, privilege elevation, production infrastructure changes, permanent configuration changes, external communications, and regulatory reporting; automation pauses execution pending required approval.

The safety event lifecycle is observation, evaluation, risk assessment, policy decision, execution or intervention, evidence collection, continuous monitoring. Safety incidents record incident identifier, affected models, affected agents, trust impact, containment actions, corrective actions, approval authority, and closure evidence.

## 8. Continuous monitoring

Continuous monitoring evaluates response quality, latency, error rate, drift, resource utilization, policy violations, operational availability, and governance compliance. Drift detection covers prediction drift, data drift, concept drift, performance degradation, confidence degradation, and operational anomalies. Significant drift initiates governance review.

Trust posture is measured through policy compliance rate, human intervention frequency, authorization success rate, safety event rate, model confidence, evidence completeness, governance exceptions, and audit findings. Automation telemetry records workflow execution, agent interactions, tool invocations, policy evaluations, approval events, runtime exceptions, and performance metrics. Out-of-scope action requests are treated as high-signal security telemetry, emitted as evidence under PAT-0003 and evaluated under RUN-0003.

## 9. Evaluation and red-teaming requirements

The Assurance Laboratory provides independent, reproducible, evidence-backed, statistically sound, policy-governed, technology-neutral, and auditable evaluation. Evaluation capability domains are functional, performance, security, safety, robustness, explainability, operational, and governance evaluation. Benchmarks are version controlled and declare benchmark identifier, business objective, evaluation domain, acceptance criteria, scoring methodology, owner, version, and evidence requirements; the benchmark lifecycle is proposal, design, validation, approval, execution, evidence review, publication, revision.

AI red teams evaluate resistance to prompt injection, indirect prompt manipulation, retrieval poisoning, tool misuse, privilege escalation attempts, instruction hierarchy violations, adversarial inputs, context manipulation, unauthorized data disclosure, and workflow abuse. Each exercise has documented objectives, scope, authorization, and evidence. Operational simulations cover normal workloads, degraded infrastructure, identity compromise, malicious user behavior, excessive workload conditions, policy conflicts, dependency failures, and recovery validation, and never impact production systems.

Every production model revision undergoes functional, security, and policy regression, plus benchmark, latency, resource, retrieval, and explainability comparison. Deployment is blocked if mandatory regression criteria are not satisfied. Each evaluation records evaluation identifier, evaluated artifact, benchmark version, environment description, evaluator identity, execution timestamp, quantitative results, qualitative observations, and approval decision.

Reported evaluation metrics are benchmark pass rate, regression stability, safety evaluation score, security evaluation score, retrieval precision, retrieval recall, operational readiness score, and evaluation reproducibility rate. Continuous evaluation monitors model drift, benchmark degradation, policy deviations, runtime anomalies, retrieval quality, operational performance, evaluation coverage, and assurance maturity; significant degradation triggers governance review.

## 10. Assurance levels and deployment eligibility

Two independent ladders are maintained. Trust assurance levels — TA-0 Experimental, TA-1 Reviewed, TA-2 Validated, TA-3 Governed, TA-4 Continuously Assured, TA-5 Executive Certified — determine operational deployment eligibility. Assurance maturity levels — AA-0 Experimental, AA-1 Validated, AA-2 Operational, AA-3 Governed, AA-4 Continuously Assured, AA-5 Executive Certified — are assessed independently for each AI capability. Domain 03 security capabilities do not enter production without documented assurance evidence.

## 11. Residual risk

Injection that steers an agent *within* its authorized scopes is not blocked by authorization and remains the standing residual identified in THR-0002; it is addressed by human review of consequential outputs and assurance-side anomaly detection, which is why production decisions remain under human governance. Two further residuals follow from the source standards: drift is detected rather than prevented, so a model may operate degraded between monitoring intervals and governance review; and trust recalculation depends on the completeness of the evidence fed to it, so gaps in evidence generation degrade trust decisions silently. Both are tracked as governance exceptions and reported in the trust metrics of Section 8.

## 12. Human review gate

Changes affecting risk classification, validation methodology, approval authority, autonomy classification, human oversight requirements, capability authorization, trust evaluation, red team procedures, regression acceptance criteria, drift thresholds, or AI safety constraints require Security Architecture Review Board review and Program Owner approval before publication. Approval confirms that AI authority remains bounded, human accountability remains non-delegable, evaluation evidence remains reproducible, and every AI-initiated action remains attributable to a verified enterprise identity.

## 13. Sources and traceability

| Source (repo-relative) | Contribution |
|---|---|
| `history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v7.0-v8.3/EAODS-v7.4-alpha-enterprise-ai-model-governance-validation-evaluation-and-risk-management-standard.md` | Model registry attributes, MR-0–MR-5 risk tiers, validation requirements, evaluation dimensions, benchmark governance, drift categories, approval workflow, monitoring scope, retirement, AI safety requirements (Sections 3, 4, 7, 8) |
| `history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v7.0-v8.3/EAODS-v7.5-alpha-enterprise-ai-trust-safety-human-oversight-and-responsible-ai-governance-standard.md` | Trust principles, AT-0–AT-5 autonomy classification, human oversight matrix, AI safety controls, prompt and tool authorization governance, memory governance, safety event lifecycle, trust metrics, TA-0–TA-5 assurance levels, safety incident fields (Sections 2, 6, 7, 8, 10) |
| `history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v7.0-v8.3/EAODS-v7.6-alpha-enterprise-ai-agent-identity-credential-capability-and-trust-fabric-standard.md` | Agent identity principles and lifecycle, credential governance attributes, capability-based authorization classes, T0–T5 trust levels, continuous trust evaluation, federation, runtime attestation, delegation, revocation triggers, identity risk scoring (Sections 2, 3, 5) |
| `history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v7.0-v8.3/EAODS-v7.9-alpha-enterprise-ai-evaluation-benchmarking-red-teaming-and-assurance-laboratory-standard.md` | Evaluation principles and capability domains, benchmark catalog attributes and lifecycle, red team scope, operational simulation scenarios, regression testing, evaluation evidence fields, AA-0–AA-5 maturity model, evaluation metrics, continuous evaluation (Sections 3, 9, 10) |
| `docs/threat-models/THR-0002-llm-instruction-injection.md` | Instruction and content risk category, output-as-data rule, cross-agent laundering, assurance hooks via PAT-0003 and RUN-0003, standing residual risk (Sections 2, 3, 8, 11) |
| `docs/frameworks/EAODS-v17.3/volume-05-automation-fabric-agent-runtime.md` | Automation-as-governed-capability premise, Tool Gateway duties, runtime isolation, AI safety controls, observability telemetry, human-in-the-loop approval points, canonical agent metadata AGENT-00128 (Sections 1, 5, 6, 7, 8) |
| `docs/threat-models/THR-0001-compromised-service-identity.md` | Scope boundary for non-AI service identity; short-lived credential and revocation posture referenced via EAODS-CTRL-000184 and PAT-0001 (Sections 1, 5) |
| `docs/architecture/ENTERPRISE_OPERATING_MODEL.md` | House style, AI operating boundaries, governance-precedes-automation principle, human review gate framing (Sections 1, 2, 12) |
