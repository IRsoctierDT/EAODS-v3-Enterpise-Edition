---
title: EAODS Enterprise Capability Model
document_id: EAODS-ARCH-CAP-001
version: 1.0.0
status: proposed
owner: Enterprise Architecture Owner
review_gate: Enterprise Architecture Review Board and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - EAODS-ARCH-EOM-001
  - ADR-0002
  - history/original-sources/conversation-evidence/v6.7-v16-band (EAODS v13.0.0-v13.0.5 volume units)
  - history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v4.17.1-v4.28/EAODS-v4.27-alpha-enterprise-cybersecurity-reference-architecture-and-capability-model.md
---

# EAODS Enterprise Capability Model

## 1. Purpose

This document consolidates the EAODS capability map into a single governed reference. It normalizes two source layers: the v13.0 Enterprise Operating Model and Capability Framework (Volumes 1-6), which defines the enterprise capability architecture, and the v4.27 Enterprise Cybersecurity Reference Architecture and Capability Model, which defines the cybersecurity capability domains and shared services.

Capabilities are organized under the four enduring pillars of the Enterprise Operating Model (EAODS-ARCH-EOM-001): Govern, Design, Operate, Build. Every capability is traced to the source volume that defines it.

## 2. Model structure and source key

Per v13.0 Volume 1, capabilities are organized into four levels:

| Level | Description |
|-------|-------------|
| L1 | Enterprise Domain |
| L2 | Business Capability |
| L3 | Operational Capability |
| L4 | Implemented Service |

The tables in sections 4-7 present L2 capabilities grouped by pillar. Source keys used throughout:

| Key | Defining volume |
|-----|-----------------|
| v13 V1 | v13.0.0 — Enterprise Capability Architecture, Business Capability Map and Federated Operating Model |
| v13 V2 | v13.0.1 — Portfolio Governance, Investment Management, Roadmapping and Value Streams |
| v13 V3 | v13.0.2 — Organizational Design, Decision Rights, Federated Governance and Accountability |
| v13 V4 | v13.0.3 — Enterprise Engineering System, Architecture Lifecycle, Standards and Design Authority |
| v13 V5 | v13.0.4 — Architecture Repository, Digital Twin, CMDB and Knowledge Federation |
| v13 V6 | v13.0.5 — Observability, Operational Intelligence, Telemetry Fabric and Decision Intelligence |
| v4.27 | Enterprise Cybersecurity Reference Architecture and Capability Model |

## 3. Capability stack

The v4.27 reference stack orders capability layers from strategy to improvement; a downstream capability shall not weaken controls established by an upstream dependency:

Business Strategy → Enterprise Governance → Risk and Compliance → Security Architecture → Identity and Trust Services → Infrastructure Security → Application Security → AI Security Services → Security Operations → Incident Response → Continuous Improvement.

The v4.27 dependency model summarizes the same ordering as: Governance → Identity → Infrastructure → Applications → AI Services → Security Operations → Executive Reporting.

## 4. Govern tier

| Capability | Scope | Defined by |
|------------|-------|------------|
| Policy and standards governance | Policy governance, standards management | v4.27 Domain 1 |
| Architecture governance | Architecture review authority; approval precedes funding | v4.27 Domain 1; v13 V2 |
| Risk governance | Risk governance and portfolio risk categories with accountable owners | v4.27 Domain 1; v13 V2 |
| Decision management | Decision rights classes, decision lifecycle, decision register | v4.27 Domain 1; v13 V3 |
| Portfolio governance and investment management | Investment lifecycle, capability-level funding, prioritization, roadmapping | v13 V2 |
| Value stream management | Required value streams (Strategy-to-Execution, Detect-to-Respond, Incident-to-Recovery, and peers) | v13 V2 |
| Federated governance and organizational design | Governance tiers G1-G6, governance bodies, charters, escalation levels E1-E5 | v13 V3 |
| Capability ownership and accountability | Executive, Business, Technical, Governance, Operational, Performance owners; enterprise RACI | v13 V1; v13 V3 |
| AI governance | AI Governance Council decision authority; AI engineering approvals | v13 V3; v13 V4 |
| Executive reporting | Executive metrics and Executive Control Tower visualization | v4.27 Domain 1; v13 V1 |

Governance dependencies named in v4.27: Executive Governance Board, Security Architecture Review Board, Enterprise Risk Council.

## 5. Design tier

| Capability | Scope | Defined by |
|------------|-------|------------|
| Enterprise architecture | Target-state definition; EADM phases A-I | v13 V4 |
| Solution architecture | Capability realization | v13 V4 |
| Security architecture | Defensive architecture; reference trust zones and trust-boundary design | v13 V1; v4.27 |
| Architecture decision management | ADR governance: immutable approved records, required attributes, security assessment | v13 V4; v4.27 |
| Technical standards lifecycle | Standard scope, mandatory controls, exception process, review cadence | v13 V4 |
| Engineering pattern library | Approved reusable patterns (Zero Trust Service Communication, Secure API Gateway, RAG, Detection-as-Code, Evidence-as-Code, and peers) | v13 V4 |
| Technology lifecycle governance | Evaluate / Trial / Adopt / Maintain / Restrict / Retire classifications | v13 V4 |
| Threat modeling | Integrated into secure engineering activities | v13 V4; v4.27 |

Every transition between v4.27 trust zones (External Networks through Management Zone) requires explicit authentication, authorization, logging, and policy evaluation.

## 6. Operate tier

| Capability | Scope | Defined by |
|------------|-------|------------|
| Identity and trust services | Identity lifecycle, authentication, authorization, federation, PAM, certificates, secrets | v4.27 Domain 2 |
| Infrastructure security | Network, endpoint, server, cloud, storage security; platform hardening | v4.27 Domain 3 |
| Threat management | Threat intelligence, vulnerability management, threat hunting, exposure management, adversary simulation | v4.27 Domain 6 |
| Security operations | Detection engineering, SIEM, SOAR, digital forensics, case management, security automation; AI Security Operations Center | v4.27 Domain 7; v13 V1 |
| Incident command and recovery | Incident response, business continuity, disaster recovery, crisis management, cyber recovery | v4.27 Domain 8; v13 V1 |
| Security assurance | Continuous validation of controls and posture | v13 V1 |
| Configuration intelligence | Architecture repository, CMDB, Digital Twin governance, discovery, reconciliation, drift detection | v13 V5 |
| Enterprise observability | Telemetry fabric, correlation engine, AI runtime observability, operational health scoring | v13 V6 |
| Decision intelligence | Insight generation, prioritization, explainable recommendations; no automatic authorization of high-impact actions | v13 V6 |
| KPI/KRI computation | Version-controlled calculation of service KPIs, operational KRIs, governance indicators | v13 V6 |

Domain 03 asset intelligence (v13 V5) evaluates security posture through relationship-aware intelligence — attack surface, identity trust paths, detection coverage, recovery dependencies — rather than isolated inventories.

## 7. Build tier

| Capability | Scope | Defined by |
|------------|-------|------------|
| Platform engineering | Shared platforms | v13 V4 |
| Application engineering | Business services | v13 V4 |
| AI engineering | Models, agents, orchestration; model selection, prompt standards, agent manifests, evaluation | v13 V4 |
| Data engineering | Information architecture | v13 V4 |
| Reliability engineering | Operational resilience | v13 V4 |
| Security engineering (Domain 03) | Identity engineering, detection engineering, AI runtime protection, cryptographic implementation, forensic readiness | v13 V1; v13 V4 |
| Application security | Secure SDLC, dependency security, CI/CD security, API security, software supply chain, release integrity | v4.27 Domain 4 |
| AI security services | Prompt, model, retrieval, and memory governance; tool authorization; agent isolation; AI audit logging; AI safety controls | v4.27 Domain 5 |
| Engineering assurance | Conformance verification, non-conformity remediation, exception governance | v13 V4 |

Per v4.27, every AI-enabled capability shall support human approval gates for privileged actions, signed model provenance, prompt isolation, retrieval boundary enforcement, policy-aware tool execution, immutable audit logging, model version traceability, rollback, and explainable decision support.

## 8. Shared security services

v4.27 designates the following as enterprise shared capabilities:

| Service | Purpose |
|---------|---------|
| Identity Platform | Authentication and authorization |
| PKI | Certificate trust |
| Secrets Vault | Secret lifecycle |
| SIEM | Security monitoring |
| SOAR | Automated response |
| EDR/XDR | Endpoint protection |
| Threat Intelligence Platform | Threat enrichment |
| Configuration Repository | Baseline management |
| Artifact Repository | Trusted software distribution |
| AI Governance Platform | AI policy enforcement |

## 9. Cross-domain integration

The v4.27 integration matrix, retained unchanged:

| Capability | Primary integration |
|------------|---------------------|
| Identity | Infrastructure, AI, Applications |
| Threat Intelligence | SOC, Vulnerability Management |
| Configuration Management | Infrastructure, Cloud, Containers |
| AI Governance | SOC, Identity, Architecture |
| Risk Management | Governance, Metrics, Audit |
| Incident Response | SOC, Forensics, Executive Reporting |

Per v13 V1, cybersecurity integrates with every capability through architectural review, risk assessment, control mapping, continuous monitoring, threat intelligence, resilience planning, and incident coordination. Security is an enterprise capability, not an isolated department.

## 10. Capability maturity and health

v13 V1 defines the maturity scale: 1 Initial, 2 Managed, 3 Standardized, 4 Measured, 5 Optimized, 6 Adaptive Enterprise (continuous optimization supported by governed AI and enterprise telemetry).

Every capability reports maturity, operational health, strategic alignment, staffing readiness, automation maturity, cybersecurity posture, financial efficiency, and customer impact. No enterprise capability shall exist without documented ownership.

## 11. Human review gate

Changes to tier assignments, capability definitions, dependency ordering, shared-service designations, or source traceability require Enterprise Architecture Review Board and Program Owner approval. The review shall confirm that the four-pillar tiering remains consistent with EAODS-ARCH-EOM-001, that no capability loses its trace to a defining volume, and that the v4.27 rule — downstream capabilities do not weaken upstream controls — remains enforceable.

## Sources and traceability

- `history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v13.0.0-alpha-enterprise-operating-model-capability-framework-volume-1-ent.md` — L1-L4 hierarchy, Domain 03 capability map, ownership roles, maturity scale, capability health model, cross-domain integration (sections 2, 4, 6, 9, 10).
- `history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v13.0.1-alpha-enterprise-operating-model-capability-framework-volume-2-ent.md` — portfolio governance, investment lifecycle, value streams, EARB approval-before-funding, portfolio risk categories (section 4).
- `history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v13.0.2-alpha-enterprise-operating-model-capability-framework-volume-3-ent.md` — governance tiers, governance bodies, decision rights, escalation levels, RACI, AI Governance Council authority (section 4).
- `history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v13.0.3-alpha-enterprise-operating-model-capability-framework-volume-4-ent.md` — engineering capability model, EADM, ADR governance, standards lifecycle, pattern library, technology lifecycle, engineering assurance (sections 5, 7).
- `history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v13.0.4-alpha-enterprise-operating-model-capability-framework-volume-5-ent.md` — configuration intelligence, CMDB, Digital Twin, drift detection, Domain 03 asset intelligence (section 6).
- `history/original-sources/conversation-evidence/v6.7-v16-band/EAODS-v13.0.5-alpha-enterprise-operating-model-capability-framework-volume-6-ent.md` — telemetry fabric, correlation, observability, decision intelligence, KPI/KRI pipeline (section 6).
- `history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v4.17.1-v4.28/EAODS-v4.27-alpha-enterprise-cybersecurity-reference-architecture-and-capability-model.md` — capability stack, Domains 1-8, trust zones, shared security services, dependency model, integration matrix, AI-native architecture requirements (sections 3-9).
- `docs/architecture/ENTERPRISE_OPERATING_MODEL.md` (EAODS-ARCH-EOM-001) — Govern/Design/Operate/Build pillar definitions used as the tiering frame (sections 1, 11).
