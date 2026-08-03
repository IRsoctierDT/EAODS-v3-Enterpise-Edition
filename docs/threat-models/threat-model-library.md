---
title: EAODS Threat Model Library — Scope, Method and Register
document_id: EAODS-SEC-THR-001
version: 1.0.0
status: proposed
owner: Enterprise Cyber Command
review_gate: Security Architecture Review Board and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - THR-0001
  - THR-0002
  - THR-0003
  - PAT-0001
  - PAT-0003
  - PAT-0004
  - RUN-0001
  - RUN-0003
  - STD-0001
  - STD-0002
  - ADR-0002
  - EAODS-CTRL-000184
  - docs/threat-models/index.md
  - docs/architecture/ENTERPRISE_OPERATING_MODEL.md
  - history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v5.0-v6.6/EAODS-v6.3-alpha-enterprise-threat-intelligence-exposure-intelligence-and-attack-surface-management-architecture-standard.md
  - history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v5.0-v6.6/EAODS-v6.4-alpha-enterprise-security-detection-engineering-analytics-and-adversary-emulation-architecture-standard.md
---

# EAODS Threat Model Library — Scope, Method and Register

## 1. Purpose and standing

This document governs the threat-model library as a whole. It fixes the modeling method every entry must follow, publishes the register of approved entries together with a coverage analysis, and maintains the prioritized backlog of candidate models awaiting authoring.

Individual entries (`THR-` identifiers) state what an attacker achieves against one trust boundary and how the platform resists. This document states how those entries are produced, how completeness of the library is judged, and what is written next. The separation is deliberate: an entry can be correct while the library remains incomplete, and only a library-level artifact makes that incompleteness visible.

Threat modeling sits in the Design pillar of the Enterprise Operating Model as a Cybersecurity Domain 03 responsibility operating across all four pillars. Volume 10 remains the operational north star above this document, and Enterprise Cyber Command remains the accountable owner of every entry.

## 2. Scope and non-goals

In scope: the authoring method; the register of approved entries; coverage analysis against the Domain 03 source authorities; the candidate backlog and its prioritization. The following are permanently out of scope.

- **Offensive content.** Entries state what an attacker achieves and how the platform resists — never how to reproduce the attack. This is the lawful-lab scope already declared by the library index.
- **Detection logic.** Detections are governed enterprise assets with their own engineering lifecycle. A threat model states the detection *requirement*; the detection engineering function owns the content that satisfies it.
- **Live intelligence.** Campaign and indicator material belongs to the threat-intelligence register, whose objects carry confidence ratings and expiration dates. Threat models are durable boundary analyses and must not decay with an indicator.

## 3. Modeling method

### 3.1 Required entry structure

Every entry documents seven parts, in this order. The structure is not stylistic: each part exists so that a downstream function can consume the entry mechanically.

| Part | What it must establish | Consumed by |
|---|---|---|
| Scope and assets | The concrete assets and flows analyzed, named tightly enough to exclude neighbours | Exposure correlation from asset to business service |
| Trust boundary | The single claim that, if false, invalidates everything downstream of it | Architecture review; pattern selection |
| Threat actors | Who acts and from what starting position — external, insider, compromised workload, defective automation | Adversary emulation scenario design |
| Threat scenarios | Numbered and outcome-stated: what the attacker achieves | Detection requirements; playbook triggers |
| Mitigations | One row per scenario, each mapped to an implementing object by stable identifier | Control validation; coverage reporting |
| Residual risk | What remains after mitigation, stated plainly and owned | Risk acceptance; executive reporting |
| Assurance hooks | The evidence the platform emits that proves the mitigation is alive | Continuous Assurance; Executive Control Tower |

### 3.2 Scope discipline

A scope statement names assets and flows, not products. THR-0001 scopes service-to-service authentication and enumerates the issuance service and every service that trusts its verdicts — a boundary, not a vendor. Candidates whose scope cannot be stated without naming a specific implementation are usually detections or configuration standards in disguise, and are redirected accordingly.

Where a candidate originates in attack-surface discovery, the discovered assets must first be linked to enterprise asset identifiers in the Knowledge Graph, as the discovery architecture requires. An entry about assets the enterprise cannot name is not actionable.

### 3.3 Actor derivation

Actors are derived, not imagined. Each entry names the actor at the head of the exposure correlation chain — threat actor, campaign, technique, exploit, vulnerability, affected asset, business service, enterprise risk — and the business service at its foot. The middle of that chain is the intelligence register's work, not the threat model's.

Three actor classes recur across the register and are considered for every new entry: the external attacker holding stolen material, the compromised or defective internal workload, and the privileged insider concealing an outcome. Entries that name only external attackers are treated as incomplete at review.

### 3.4 Assumptions register

Every entry states the assumptions its mitigations depend on. This requirement exists because purple team activity is chartered to validate engineering assumptions and identify telemetry gaps — an assumption that is never written down cannot be validated, and its failure surfaces only as an incident. Assumptions take one of three forms.

1. **Control assumptions** — a named control is implemented and effective. Cite the control identifier; effectiveness then becomes a control-validation question rather than a threat-model claim.
2. **Telemetry assumptions** — a signal exists, is complete, and is time-synchronized. Security telemetry is required to be complete, attributable, normalized, time-synchronized, schema validated and policy governed; an entry may assume those properties but must say that it does, so a data-quality regression becomes visible as a threat-model regression.
3. **Governance assumptions** — a human gate holds. Human approval is mandatory before production configuration changes, privileged identity modifications, destructive operations, enterprise policy publication, risk acceptance, regulatory submissions and financial transactions. An entry relying on any of these must cite which gate it relies on.

A failed assumption is a review trigger, not a footnote: the entry returns to the review gate.

### 3.5 Mitigation mapping

Every mitigation row maps to an existing control, pattern or runbook by stable identifier under STD-0001, and the resulting `mitigates` edge is registered under STD-0002. A threat with no mapped mitigation is a finding, not a footnote: it opens a corrective workflow rather than being softened in prose.

Mitigation claims are bounded by the governance automation boundaries the platform already accepts. Automation may evaluate controls, validate configurations, identify compliance drift, generate reports, recommend remediation, route approvals and correlate evidence. It may not approve enterprise policy, accept organizational risk, authorize privileged access outside approved policy, suppress audit evidence or alter governance records. A mitigation that would require any of the latter is not a mitigation and cannot be recorded as one.

### 3.6 Evidence and assurance hooks

An entry is incomplete until it names the evidence that proves its mitigations are running. Evidence is a governed object carrying required fields — identifier, source system, timestamp, event type, related entity identifiers, classification, integrity hash, collection method, confidence score, lifecycle state, retention policy — and it never bypasses validation. Entries cite the evidence class, not a schema; the evidence framework owns the schema.

Executive reporting draws only on evidence rated at integrity-verified quality or higher unless an exception is explicitly approved. An assurance hook must therefore either name evidence capable of reaching that level or state plainly that the hook is currently advisory.

### 3.7 What entries must not assert

No entry asserts a MITRE ATT&CK technique identifier that no source authority in this repository carries. The Domain 03 units require detections and intelligence objects to maintain governed relationships to threats and techniques, but they do not enumerate technique identifiers, and nothing in the current corpus authorizes a specific citation. Technique mapping is added when the intelligence register supplies it, with provenance, and not before.

Entries likewise invent no metrics. Where a measure is needed, entries cite one the platform already requires — detection latency, false-positive rate, false-negative estimate, telemetry completeness, validation success rate, analyst acceptance rate, evidence completeness, unauthorized action attempts.

## 4. Register of approved entries

| ID | Entry | Trust boundary | Mitigation anchors | Standing residual risk |
|---|---|---|---|---|
| THR-0001 | Compromised Service Identity | Presented identity versus actual identity | EAODS-CTRL-000184 · PAT-0001 · PAT-0004 · RUN-0001 | A credential is valid between issuance and theft-detection; issuer compromise is the highest-impact scenario |
| THR-0002 | LLM Instruction Injection | Model output versus authorized instruction | PAT-0001 · PAT-0003 · RUN-0003 · EAODS-CTRL-000184 | Injection that steers an agent *within* its authorized scopes is not blocked by authorization |
| THR-0003 | Assurance Evidence Tampering | What happened versus what is reported | PAT-0003 · RUN-0003 · Volume 11 evidence requirement | A privileged actor controlling both an activity and its telemetry can hold a consistent false picture |

All three entries are owned by Enterprise Cyber Command and carry Approved status. Their `mitigates` edges are registered in the relationship graph, and THR-0001 additionally carries a `governed_by` edge to STD-0001. Entries added under this document inherit the same obligation.

## 5. Coverage analysis

### 5.1 Against the detection taxonomy

The detection engineering framework defines eight detection categories. Mapping the register against them shows where the library supports detection requirements today and where a detection engineer has no threat model to design against.

| Detection category | Register coverage | Assessment |
|---|---|---|
| Identity — authentication and privilege misuse | THR-0001 | Covered |
| AI — AI misuse and policy violations | THR-0002 | Covered |
| Insider threat — behavioural anomalies | THR-0003 | Partial; concealment only, not exfiltration or sabotage |
| Data protection — unauthorized access or exfiltration | THR-0002 (escalation scenario) | Partial; exfiltration appears as an outcome, never as a boundary |
| Endpoint — host compromise indicators | None | Gap |
| Network — lateral movement and communications | None | Gap |
| Cloud — cloud platform misuse | None | Gap |
| Application — business application abuse | None | Gap |

### 5.2 Against the intelligence domains and exposure lifecycle

The threat-intelligence architecture defines six intelligence domains: strategic, operational, tactical, technical, exposure and business. The register is boundary-derived and serves the tactical domain well, because each entry yields detection requirements directly. It does not serve the exposure domain at all, because no entry takes attack-surface discovery as its starting point, and it serves the technical domain only indirectly, because no entry is anchored to vulnerability or indicator material.

Against the exposure management lifecycle — discover, validate, prioritize, mobilize, remediate, verify, measure — the library contributes to *validate* and *prioritize* for the three boundaries it covers, and contributes nothing to *discover*. This is the clearest structural gap in the library and the reason the highest-priority backlog candidates are discovery-anchored.

### 5.3 Structural observations

1. **Every approved entry is a control-plane entry.** Identity issuance, agent authorization and assurance reporting are all platform-internal. The library holds no entry for the data plane the platform operates on.
2. **Detection dependency is undeclared.** All three entries name assurance hooks; none names the telemetry sources those hooks require. Under section 3.4 this is now a defect, and the three entries are scheduled for an assumptions-register amendment at their next review — not a re-authoring.
3. **No entry is exercise-derived.** Adversary emulation validates detection coverage, alert quality, analyst workflows, evidence generation, incident-response readiness and telemetry completeness, yet none of that has produced a library entry. Exercise findings currently terminate in the purple team findings register instead of feeding durable boundary analysis back into Design.

## 6. Candidate backlog

Candidates are named descriptively. No `THR-` identifier is assigned until an entry has been authored and has passed review, so that the register never contains reserved-but-empty numbers.

### 6.1 Prioritization method

Candidates are ranked by weighted scoring rather than by severity alone, using the exposure prioritization factors the platform already adopts: exploit availability, active exploitation, asset criticality, business dependency, control effectiveness, network accessibility, identity exposure, compensating controls and remediation complexity. Two library-specific factors are applied on top, both derived from section 5 — whether the candidate closes a taxonomy or lifecycle gap, and whether a detection engineer or playbook author is blocked without it.

AI-assisted analysis may cluster candidates and recommend sequencing, but those recommendations remain advisory until validated through enterprise governance. Bands below are advisory until the review gate confirms them.

### 6.2 Band 1 — author next

| Candidate threat model | Primary trust boundary | Derived from |
|---|---|---|
| Unmanaged External Attack Surface Exposure | Discovered internet-facing asset versus governed enterprise asset inventory | External attack surface management: internet-facing assets, exposed services, public cloud resources, DNS records, certificate inventories, third-party exposures, forgotten infrastructure, shadow IT |
| Detection Coverage Gap and Silent Detection Failure | Expected detection coverage versus actual detection coverage | Detection lifecycle performance monitoring; coverage-gap and telemetry-health reporting; false-negative estimate as a required metric |
| Detection Content Integrity in the Detection-as-Code Repository | Approved detection content versus deployed detection content | Detection-as-code standard: version control, peer review, validation status, and the revision-or-retirement stage of the detection lifecycle |
| Threat Intelligence Poisoning and Confidence Laundering | Unverified external intelligence versus operationally actionable intelligence | Intelligence source inventory and the rule that every source carries a confidence rating and provenance record; intelligence quality levels TI-0 through TI-5 |

Each Band 1 candidate closes a gap named in section 5 and has a blocked consumer today: attack-surface discovery has no boundary analysis to prioritize against, and detection engineering has no model describing the failure of detection itself.

### 6.3 Band 2 — scheduled

| Candidate threat model | Primary trust boundary | Derived from |
|---|---|---|
| Internal Attack Surface Drift and Legacy Trust Relationships | Intended internal topology versus actual internal topology | Internal attack surface management: unmanaged endpoints, privileged systems, administrative interfaces, legacy platforms, unsupported software, configuration drift, internal trust relationships, unauthorized services |
| Exposure Prioritization Manipulation | Computed remediation priority versus actual operational risk | Weighted exposure prioritization inputs, in particular asset criticality, business dependency, control effectiveness and compensating controls |
| AI-Assisted Detection Engineering Error Propagation | AI-generated detection content versus validated production content | AI assistance in rule generation, tuning suggestions and coverage-gap identification, bounded by mandatory human validation before production deployment |
| Security Telemetry Pipeline Integrity Loss | Emitted telemetry versus telemetry available for correlation | Canonical event model and event lifecycle; normalization, enrichment and time-synchronization requirements |
| Response Automation Abuse | Legitimate response trigger versus attacker-induced response trigger | Response authorization and the human-approval list covering account disablement, infrastructure modification, data deletion and destructive actions; rollback and compensating-control requirements |

The telemetry candidate deliberately abuts THR-0003 and must be scoped against it at authoring: THR-0003 owns the boundary from operations to assurance reporting, while this candidate owns the boundary from source emission to the correlation layer. If the two cannot be separated cleanly at review, the correct outcome is an amendment to THR-0003 rather than a new entry.

### 6.4 Band 3 — watchlist

| Candidate threat model | Primary trust boundary | Derived from |
|---|---|---|
| Adversary Emulation Scope Escape | Authorized exercise activity versus production incident | Requirement that emulation exercises be authorized and documented before execution; purple team validation of operational readiness |
| Break-Glass and Just-In-Time Privilege Abuse | Emergency access versus routine access | Break-glass governance and just-in-time privilege: justification, approval, expiration, monitoring, audit trail, mandatory post-event review |
| Policy Decision Evasion and Stale Policy Evaluation | Enforced decision versus published policy | Separation of decision and enforcement points; the rule that no runtime decision evaluates unpublished policies; policy version governance including supersession and rollback |
| Multi-Agent Delegation Bypass | Brokered task routing versus direct agent-to-agent delegation | Inter-agent communication model and the prohibition on direct agent-to-agent privilege delegation; the rule that agents may never elevate their own privileges |
| Incident Command and Crisis Communication Manipulation | Authorized command decision versus asserted command decision | Command authority matrix; executive situation reporting; the requirement that all external communications follow enterprise approval workflows |
| Recovery of Compromised State | Restored service versus trustworthy service | Recovery governance: restoration priority, validation criteria, rollback procedures, recovery evidence, residual risk |

Band 3 candidates are real but currently have either strong compensating governance or no blocked consumer. The multi-agent delegation candidate additionally overlaps the cross-agent laundering scenario of THR-0002 and may resolve as an amendment there.

## 7. Lifecycle of a library entry

1. **Intake** — from a boundary identified in architecture review, an exposure identified by attack-surface discovery, a gap identified by adversary emulation or purple team activity, or a corrective workflow opened because a mitigation had no mapped implementing object.
2. **Prioritization** — ranked under section 6.1 and placed in a band; bands are revisited whenever the coverage analysis is refreshed.
3. **Authoring** — written to the section 3.1 structure, with assumptions stated and every mitigation mapped by identifier.
4. **Identifier assignment** — the next `THR-` identifier is minted from the registry sequence at this point, never earlier.
5. **Validation** — documentation validation, identifier validation under STD-0001, and relationship validation under STD-0002; unmapped mitigations fail the gate.
6. **Review** — Enterprise Cyber Command review, then the gate named in this document's front matter for any change to the method or the coverage baseline.
7. **Maintenance** — re-review when a stated assumption fails, when a mapped mitigation changes, or when an exercise produces a finding against the modeled boundary.

## 8. Reporting

Library health is reported through the same channels as the rest of Domain 03: coverage by detection category, backlog depth and band distribution, the count of threats with unmapped mitigations, and the age of the coverage analysis. Consistent with platform reporting discipline these are computed from validated evidence rather than asserted, and a library holding an unmapped mitigation is reported as such rather than as complete.

## 9. Human review gate

Approval requires confirmation that: the method preserves the seven-part entry structure used by the approved register; no mitigation is claimed without a mapped identifier; no technique identifier or metric is asserted beyond the source authorities; candidate models carry descriptive names and no reserved identifiers; the coverage analysis states gaps plainly rather than minimizing them; and the library remains a defensive artifact with no offensive content.

## 10. Sources and traceability

Paths beginning `history/…` expand to `history/original-sources/EAODS_AI_Operator_Suite_transmissions/`.

| Source (repo-relative) | Contribution |
|---|---|
| `docs/threat-models/index.md` | Library scope and defensive posture; the seven-part entry structure; the mitigation-mapping rule and the "unmapped mitigation is a finding" principle; identifier-minting sequence and review gate |
| `docs/threat-models/THR-0001-compromised-service-identity.md` | Register row; scope-discipline exemplar in section 3.2; identity actor classes; mitigation anchors and residual-risk framing |
| `docs/threat-models/THR-0002-llm-instruction-injection.md` | Register row; the agent authorization boundary; cross-agent laundering overlap noted against the multi-agent delegation candidate |
| `docs/threat-models/THR-0003-assurance-evidence-tampering.md` | Register row; insider-concealment actor class; boundary demarcation against the telemetry pipeline candidate |
| `docs/architecture/ENTERPRISE_OPERATING_MODEL.md` | House style; threat modeling in the Design pillar and Domain 03 as cross-pillar; Volume 10 as operational north star; traceability and review-gate expectations |
| `history/…/units/v5.0-v6.6/EAODS-v6.3-alpha-…-threat-intelligence-exposure-intelligence-and-attack-surface-management-architecture-standard.md` | Exposure correlation chain used for actor derivation; external and internal attack-surface inventories; exposure prioritization factors and the weighted-scoring rule; intelligence quality levels; exposure management lifecycle; source confidence and provenance requirement; advisory status of AI-assisted analysis |
| `history/…/units/v5.0-v6.6/EAODS-v6.4-alpha-…-security-detection-engineering-analytics-and-adversary-emulation-architecture-standard.md` | Detection taxonomy used for the coverage analysis; detection lifecycle and detection-as-code governance; purple team validation of engineering assumptions; adversary emulation authorization requirement; detection performance metrics |
| `history/…/units/v5.0-v6.6/EAODS-v6.2-alpha-…-cybersecurity-data-architecture-telemetry-and-security-data-fabric-standard.md` | Telemetry property requirements underpinning telemetry assumptions; canonical event model and event lifecycle behind the telemetry pipeline candidate |
| `history/…/units/v5.0-v6.6/EAODS-v6.1-alpha-…-evidence-as-code-continuous-assurance-and-audit-automation-standard.md` | Evidence object fields and the no-bypass validation rule; the evidence quality threshold governing executive reporting |
| `history/…/units/v5.0-v6.6/EAODS-v6.0-alpha-…-control-as-code-policy-as-code-and-governance-automation-framework.md` | Governance automation boundaries constraining what may be recorded as a mitigation |
| `history/…/units/v5.0-v6.6/EAODS-v5.2-alpha-…-policy-decision-point-pdp-policy-enforcement-point-pep-and-authorization-architecture-standard.md` | Break-glass and just-in-time privilege candidate; policy publication and version governance behind the policy evasion candidate |
| `history/…/units/v5.0-v6.6/EAODS-v5.1-alpha-…-ai-agent-operating-framework-and-multi-agent-coordination-standard.md` | Human approval gates cited in governance assumptions; brokered routing and the delegation prohibition behind the multi-agent candidate |
| `history/…/units/v5.0-v6.6/EAODS-v6.5-alpha-…-security-response-automation-orchestration-and-playbook-architecture-standard.md` | Response authorization and the human-approval list behind the response automation abuse candidate; rollback and compensating-control requirements |
| `history/…/units/v5.0-v6.6/EAODS-v6.6-alpha-…-incident-command-crisis-management-and-cyber-recovery-governance-standard.md` | Command authority and external-communication approval behind the incident command candidate; recovery validation behind the recovery-of-compromised-state candidate |
| `standards/vocabulary/object-identifiers.yaml` · `standards/graph/relationships.yaml` | Registered `THR-` identifier format and the existing `mitigates` and `governed_by` edges cited in section 4 |
