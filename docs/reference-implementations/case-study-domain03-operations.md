---
title: Case Study — Domain 03 Detection and Response Operations
document_id: EAODS-REF-CS-002
version: 1.0.0
status: proposed
owner: Enterprise Architecture Review Board
review_gate: Enterprise Architecture Review Board and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - EAODS-ARCH-EOM-001
  - EAODS-OPS-IC-001
  - THR-0001
  - RUN-0001
  - RUN-0003
  - PAT-0001
  - PAT-0003
  - PAT-0004
  - EAODS-CTRL-000184
  - STD-0001
  - history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v5.0-v6.6/EAODS-v6.6-alpha-enterprise-incident-command-crisis-management-and-cyber-recovery-governance-standard.md
  - history/original-sources/conversation-evidence/v17.0-v17.2-volumes/EAODS-v17.0.4-alpha-enterprise-cyber-defense-digital-resilience-framework-volume.md
---

# Case Study — Domain 03 Detection and Response Operations

## 1. Purpose and standing

This document walks one Domain 03 event end to end — detection, qualification, incident command, containment, recovery, evidence, and review — to show how the repository's governed objects fit together in sequence rather than as a catalog. It is a teaching artifact for the **Operate** pillar, and it is anchored to the same objects a real response would use: THR-0001, RUN-0001, RUN-0003, PAT-0001, PAT-0003, PAT-0004, and the registered control EAODS-CTRL-000184.

It creates no procedure. Every executable step shown here belongs to an approved runbook, and every command decision belongs to the incident command model (EAODS-OPS-IC-001). Where this document appears to describe *how* something is done, it is quoting those objects, not extending them.

## 2. How this case study is to be read

**This is an illustrative scenario, not a deployment record.** No organization is named, no organization is described, and nothing here is a report of an event that occurred at any enterprise. The scenario is a composite built from the "Enterprise Case Study" sections that the EAODS corpus writes for itself — the sections in the v6.6-alpha incident command standard, v17.0 Volume 5 (incident response), v17.2 Volume 3 (incident response runbooks), and v17.0 Volume 2 (detection engineering). Those sections are themselves written as hypothetical enterprises for illustration, and this document inherits that status without narrowing it.

Three consequences follow, and reviewers should hold the document to them:

1. **No outcome is measured.** Section 13 reports only the qualitative outcomes the source case-study sections themselves state, attributed to those sections. No timing, rate, volume, or cost figure appears anywhere in this document, because none of the sources read supplies one for this scenario.
2. **No identifier is minted.** The incident, its evidence items, and its corrective actions are referred to by role, not by identifier. EAODS-OPS-IC-001 Section 8.1 records that no incident prefix is registered in the identifier registry today, and STD-0001 requires registration before first use; a case study is not an exemption from that rule.
3. **Only registered objects are cited.** The identifiers appearing below all exist in the repository object model. The canonical service ownership record `SVC-00387` and the registered control `EAODS-CTRL-000184` appear in their canonical-example role, exactly as EAODS-OPS-IC-001 Section 4 uses them.

## 3. Governing objects exercised

| Object | Role in this scenario |
|---|---|
| THR-0001 Compromised Service Identity | The threat model the scenario instantiates: credential theft and replay, scope escalation, issuer compromise, revocation lag |
| EAODS-CTRL-000184 Service Identity Verification (Preventive) | The registered control whose failure supplies the regulatory dimension of classification and the assurance evidence stream |
| PAT-0001 Zero Trust Service Identity | The design under attack: short-lived scoped credentials, per-call verification, fail-closed, central revocation |
| PAT-0004 Governed Recovery Orchestration | The recovery design: orchestrated, idempotent, integrity-validated between steps, human-authorized at entry and resumption |
| PAT-0003 Continuous Assurance Evidence Pipeline | The path every stage's evidence takes to independent assurance |
| RUN-0003 Compliance Deviation Response | The entry procedure when a registered control fails and a trust boundary is exposed |
| RUN-0001 Service Recovery Execution | The executable recovery procedure for the Tier 1 service |
| EAODS-OPS-IC-001 Incident Command | Severity scale, command posts, authority matrix, registers, escalation triggers |
| `SVC-00387` | Canonical service ownership record, read for reliability classification and named owners |

## 4. The illustrative scenario

A hypothetical multinational enterprise, described only as such, operates hybrid infrastructure across multiple cloud environments and manages a large population of enterprise identities. During a peak commercial period it experiences a coordinated compromise touching cloud identity infrastructure, privileged credentials, and cloud-hosted operational dashboards, with encryption activity affecting a dependent business application.

The composite is deliberate. The identity-infrastructure and peak-period framing is drawn from the v17.0 Volume 5 case study; the simultaneity of ransomware activity, privileged credential compromise, and suspicious dashboard access is drawn from the v17.2 Volume 3 case study; the disruption of authentication services alongside customer-facing applications is drawn from the v6.6-alpha case study; and the telemetry conditions in Section 5 are drawn from the v17.0 Volume 2 case study.

The challenge those sections state is not a technical one. Independent teams respond capably inside their specialties, but sequencing, executive communication, and recovery validation are inconsistent across them; technical responders, executive leadership, legal counsel, communications, and business continuity must coordinate while preserving evidence and meeting notification obligations. The scenario exists to show what the governed objects contribute to that problem.

In repository terms the enterprise is experiencing THR-0001: the trust boundary between a caller's presented identity and its actual identity is in doubt, and everything downstream of a successful verification inherits that doubt.

## 5. Stage 1 — Detection

Two independent detection paths open, and the scenario is more instructive because they open in parallel.

**Assurance-hook path.** THR-0001 emits issuance volume, verification failure rates, and revocation latency as evidence under PAT-0003. An anomaly on that stream triggers RUN-0003 with immediate Enterprise Cyber Command escalation — the escalation is written into the threat model, not decided in the moment.

**Behavioral-detection path.** The v17.0 Volume 2 behavioral detection framework evaluates identity misuse, privilege escalation, credential abuse, anomalous authentication, lateral movement, persistence, and data access anomalies, over a telemetry fabric that normalizes identity activity, cloud audit events, and endpoint events. Analytics preserve explainability for every generated alert, which is what makes the alert usable as an investigative starting point rather than a prompt to re-derive the finding by hand.

Both paths matter to the illustration: the assurance hook detects that a *control* is failing, the behavioral detection detects that an *adversary* is acting, and the incident is the same incident.

## 6. Stage 2 — Qualification, classification, and declaration

RUN-0003 governs the control-failure path: correlate the deviation to its control (`EAODS-CTRL-`) and implicated service (`SVC-`), then classify whether the deviation disables a preventive control or exposes a trust boundary. EAODS-CTRL-000184 is a Preventive control and the exposure is a trust boundary, so RUN-0003 step 3 applies: escalate immediately to Enterprise Cyber Command and treat the finding as a potential security event, not only a compliance finding.

Classification then follows EAODS-OPS-IC-001 Section 4, on the IC-0 to IC-5 scale, with the level set by the highest criterion met across operational impact, regulatory obligations, business criticality, customer impact, safety implications, and executive visibility. Two inputs are read rather than re-derived during the incident: the affected service's reliability classification and availability target from its ownership record (canonically `SVC-00387`), and the registered control with its evidence requirement.

For the illustration, the event is declared an enterprise incident at IC-3 by the Incident Commander, and a command log is opened. The level is a scenario choice made to exercise the command layer; it is not a rule, and the sources read state explicitly that severity is reassessed at every situation report as evidence develops.

Runbook selection follows the v17.2 Volume 3 architecture — detection, incident qualification, runbook selection, response execution, evidence preservation, recovery coordination, lessons learned. The scenario activates the Credential Compromise runbook as primary, with the Cloud Platform Compromise and Ransomware Response runbooks running against the dependent surfaces, all under one incident.

## 7. Stage 3 — Command activation

Command posts are filled per EAODS-OPS-IC-001 Section 5, or their duties are explicitly assumed by a filled post and recorded: Incident Commander, Operations Section lead, Planning Section lead, Communications Section lead, and Recovery Coordinator. Command posts are incident-scoped; the permanent owners named in the service ownership record are engaged, not replaced.

Because a cyber cause is confirmed rather than suspected, the transfer written into RUN-0001 and reconciled in EAODS-OPS-IC-001 Section 2 applies: the Enterprise Cyber Command directs, and no second command system is created by the platform operations side. The authority matrix governs from here — one named approving authority per material decision, with consultation transferring nothing:

| Decision in this scenario | Approval authority |
|---|---|
| Routine containment of affected workloads | Incident Commander |
| Isolation of an enterprise service | Incident Commander with the business owner |
| Entry into recovery of the identity authority | Recovery authority named in the ownership record (RUN-0001 step 2) |
| Business resumption | Operational owner (RUN-0001 step 6) |
| Regulatory notification authorization | Executive Leadership, with Legal review |
| Risk acceptance during recovery | Enterprise Governance Board or its delegated authority |

Structured executive situation reporting begins at command activation: incident identifier field, executive summary, affected services, current operational status, decisions made, outstanding risks, recovery progress, next planned actions. The Communications Section owns the report; the Incident Commander approves it before release.

## 8. Stage 4 — Containment and investigation

The Credential Compromise runbook sequence from v17.2 Volume 3 runs in order: validate identity exposure, assess privilege level, preserve authentication evidence, contain unauthorized access, review identity federation, restore trusted authentication, conduct post-event analysis. Note that evidence preservation precedes containment in that sequence — the v17.0 Volume 5 principle that operational speed shall not compromise evidence integrity or governance is enforced by the ordering, not by exhortation.

THR-0001's mitigation table is what containment actually leans on, and the scenario exercises each row:

| THR-0001 scenario | What contains it here | Implemented by |
|---|---|---|
| Credential theft and replay | Short credential lifetime bounds the replay window; per-call verification fails closed | EAODS-CTRL-000184 · PAT-0001 |
| Scope escalation | Allow-listed scopes per role limit what a stolen identity reaches; delegation is off by default | PAT-0001 |
| Revocation lag | Central revocation checked at verification; no long-lived verification caches to outlive the revocation | PAT-0001 · EAODS-CTRL-000184 |
| Issuer compromise | Issuer treated as Tier 1; recovery via governed orchestration rather than improvisation | PAT-0004 · RUN-0001 |

Investigation runs the v17.0 Volume 6 methodology — scoping, preservation, collection, examination, correlation, analysis, validation, reporting — with methodological deviations documented and approved. Each evidence item carries source system, acquisition method, acquisition authority, collector identity, integrity verification method, classification, and retention requirement; chain-of-custody records carry collection time, transfer events, storage location, access history, integrity validation, and disposition history, with custody transfers requiring authenticated authorization and immutable logging. Evidence modification is prohibited.

Residual risk is stated rather than resolved: THR-0001 records that a credential remains valid between issuance and theft-detection for its full lifetime, and that lifetime tuning trades availability against exposure. The scenario does not make that trade-off disappear.

## 9. Stage 5 — Recovery

The identity authority is Tier 1 under PAT-0001 precisely because every protected service trusts its verdicts, so its recovery is the scenario's critical path. RUN-0001 executes, unchanged and unshortened:

1. Confirm detection and classify impact across service, dependencies, and data exposure.
2. **Human approval gate — the recovery authority authorizes entry into recovery.**
3. Execute the orchestrated recovery sequence from the resilience control plane, in dependency order.
4. Validate integrity at each step before proceeding; halt and reassess on any validation failure.
5. Measure elapsed recovery against the service's RTO and data loss against its RPO.
6. **Human approval gate — the operational owner approves business resumption.**
7. Resume service and close the recovery window.

The Recovery Coordinator supplies the command layer above that procedure — restoration priority, service dependencies, minimum viable operation, validation criteria, rollback procedures, recovery evidence, and residual risk — while the execution stays the runbook's. PAT-0004 is the design being relied on: humans authorize entry and resumption, and the steps in between are orchestrated and idempotent rather than improvised. The pattern's own stated dependency applies here too — recovery sequencing is only as good as the dependency maps, and stale maps sequence the restore wrong.

Two constraints bind the illustration. First, EAODS-OPS-IC-001 Section 9 states that the command model neither shortens a runbook's human approval gates nor authorizes bypassing one; an incident that appears to require a bypass is an escalation, not a shortcut. Second, recovery concludes only after the defined validation criteria are met — dependent services reporting healthy, integrity checks passed in sequence, and objectives met or the miss documented with cause.

## 10. Stage 6 — Evidence and continuous assurance

Evidence is preserved as the incident runs, not reconstructed after it closes. Four registers are maintained and retained per EAODS-OPS-IC-001 Section 10: the incident command log, the executive situation report, the crisis decision register, and — opened at review — the corrective action register. A recovery validation report is produced at service validation and a post-incident governance assessment at review close.

Evidence flows to independent assurance on the PAT-0003 path, as a side effect of the work rather than as a separate reporting exercise:

| Producing activity | Evidence emitted |
|---|---|
| RUN-0001 recovery | Recovery timeline, per-step validation results, RTO/RPO attainment, before the incident record closes |
| RUN-0003 deviation handling | Detection record, severity classification, corrective workflow reference, re-validation result, closure decision |
| EAODS-CTRL-000184 operation | Issuance volume, verification failure rates, revocation latency, per the control's evidence requirement |

Continuous Assurance validates that evidence against the registered control and objectives, and the Executive Control Tower reports only from validated evidence. Assurance remains independent: it consumes evidence but is never the system that produces it. The knowledge-graph relationships this incident creates — to services, assets, responders, executive decisions, evidence, recovery activities, corrective actions, risks, and controls — are registered typed edges under STD-0002 rather than free-form links.

## 11. Stage 7 — Post-incident review and corrective actions

Review is a lifecycle stage, not a follow-up: service validation is followed by lessons learned and then governance improvement. The Incident Commander convenes it with the EPOC, and the review distinguishes systemic causes from individual errors.

For this scenario the review examines, at minimum: whether the IC-3 classification correctly applied the escalation criteria; the crisis decision register against the authority matrix; recovery performance against the service's documented objectives, with any miss and its cause; evidence completeness on the PAT-0003 path; ownership gaps found during the incident; and recurrence — whether an existing corrective action failed to prevent this event. Control effectiveness is assessed directly: did short credential lifetime, per-call verification, and central revocation behave as PAT-0001 and EAODS-CTRL-000184 specify?

Every finding becomes a corrective action carrying an accountable owner, an implementation milestone, measurable success criteria, verification evidence, and closure approval, with completion independently validated. Consistent with Section 2, this document assigns no identifiers to those actions.

## 12. AI-assisted support in this scenario

AI assistance appears at four points across the stages above, and each source read draws the same line in its own domain.

| Stage | Permitted assistance | Boundary as stated by the source |
|---|---|---|
| Detection engineering | Rule generation, telemetry analysis, enrichment and optimization suggestions | Production deployment requires human approval and validation (v17.0 Volume 2) |
| Incident operations | Event summarization, evidence correlation, timeline generation, response recommendation, briefing preparation | Containment actions affecting production environments require explicit human authorization (v17.0 Volume 5) |
| Investigation | Artifact classification, event correlation, timeline construction, evidence indexing, report drafting | Analytical conclusions affecting enterprise decisions require human review before publication (v17.0 Volume 6) |
| Crisis command | Timeline generation, dependency analysis, action tracking, executive briefing preparation | AI shall not independently declare an incident, authorize recovery, or approve external communications (v6.6-alpha) |

EAODS-OPS-IC-001 Section 11 states the crisis-command boundary as absolute and not relaxed by severity, time pressure, or an unfilled command post. This case study introduces no scenario condition that tests it, because no such condition would be legitimate.

## 13. Outcomes as stated by the source case studies

The source case-study sections state outcomes qualitatively, and this document repeats them as attributed claims about those sections rather than as results of a deployment.

- The v6.6-alpha section states coordinated crisis management, improved executive decision support, measurable recovery governance, stronger evidence preservation, consistent stakeholder communications, and structured organizational learning.
- The v17.0 Volume 5 section states a coordinated response that reduces recovery time, preserves forensic integrity, improves executive decision-making, and strengthens long-term cyber resilience through measurable organizational learning and governance improvements.
- The v17.2 Volume 3 section states consistent documentation, controlled escalation, validated recovery, improved executive visibility, and actionable post-incident improvements that strengthen Domain 03 operational maturity.

None of the sources read attaches a figure to any of these statements, and this document does not supply one.

## 14. Limits of this illustration

Stated narrowly, and scoped to the sources named in Section 17:

- The scenario is hypothetical. It reports no event, at no organization, and its severity level, runbook selection, and stage ordering are illustrative choices within the scales and sequences the sources define.
- It demonstrates the command and governance layer over Domain 03 operations. It is not a detection ruleset, a forensic procedure, or a recovery script; those live in the detection repositories, the forensic laboratory procedures, and RUN-0001 respectively.
- Of the objects in the repository's current runbook and threat-model libraries, this walkthrough exercises RUN-0001, RUN-0003, THR-0001, PAT-0001, PAT-0003, PAT-0004, and EAODS-CTRL-000184. RUN-0002, THR-0002, and THR-0003 are not exercised here; their absence reflects this scenario's scope and says nothing about their standing.
- The sources read for this document define no incident identifier prefix, no evidence identifier prefix, and no corrective action identifier prefix registered under STD-0001; registration is a change to the identifier registry, not to this document.

## 15. Human review gate

Approval requires confirmation by the Enterprise Architecture Review Board and the Program Owner that:

- the document is unambiguously labelled an illustrative scenario, names no organization, and presents no outcome as a measured result;
- no procedure, command post, authority, severity level, or escalation trigger appears beyond those in the cited sources, and no runbook gate is shortened, weakened, or bypassed;
- every identifier cited already exists in the repository object model, and no new identifier is minted;
- the AI boundaries in Section 12 are stated without conditions or exceptions;
- the traceability from THR-0001 through EAODS-CTRL-000184, PAT-0001, PAT-0004, RUN-0003, and RUN-0001 to PAT-0003 evidence is complete and correctly attributed.

## 16. Sources and traceability

| Source (repo-relative path) | Contribution |
|---|---|
| docs/threat-models/THR-0001-compromised-service-identity.md | Trust boundary and threat framing (Section 4); assurance-hook detection path and its RUN-0003 escalation (Section 5); mitigation table rows and residual-risk statement (Section 8); Tier 1 issuer recovery route (Section 9) |
| docs/runbooks/RUN-0001-service-recovery-execution.md | Recovery procedure, both human approval gates, and validation criteria (Section 9); cyber-cause transfer to Enterprise Cyber Command (Section 7); recovery evidence emitted to Continuous Assurance (Section 10) |
| docs/runbooks/RUN-0003-compliance-deviation-response.md | Control-to-service correlation and severity classification (Section 6); trust-boundary escalation as a potential security event (Section 6); deviation evidence set (Section 10) |
| docs/patterns/PAT-0001-zero-trust-service-identity.md | Short-lived scoped identity, per-call fail-closed verification, central revocation, allow-listed scopes; EAODS-CTRL-000184 as governing control; Tier 1 status of the identity authority (Sections 3, 8, 9) |
| docs/patterns/PAT-0004-governed-recovery-orchestration.md | Orchestrated, idempotent, integrity-validated recovery with human authorization at entry and resumption, and the dependency-map dependency (Section 9) |
| docs/patterns/PAT-0003-continuous-assurance-evidence-pipeline.md | Evidence as a side effect of operation, per-control evidence requirement, assurance independence, Executive Control Tower reporting from validated evidence (Section 10) |
| docs/operations/incident-command-model.md (EAODS-OPS-IC-001) | IC-0 to IC-5 scale and classification inputs including `SVC-00387` and `EAODS-CTRL-000184` (Section 6); command posts and incident-scoped ownership (Section 7); command authority matrix (Section 7); situation report fields (Section 7); registers and knowledge-graph edges (Section 10); no-bypass rule for runbook gates (Section 9); post-incident review scope (Section 11); absolute AI boundary (Section 12); unregistered incident prefix under STD-0001 (Sections 2, 14) |
| docs/architecture/ENTERPRISE_OPERATING_MODEL.md (EAODS-ARCH-EOM-001) | Operate-pillar framing and reference implementation expectations — control enforcement, operational ownership, traceable evidence, human review gates (Sections 1, 15) |
| docs/architecture/architecture-principles.md (EAODS-ARCH-PRIN-001) | House style — front matter, numbered sections, human-review-gate and sources-and-traceability conventions; evidence-precedes-assertion and named-ownership principles applied throughout |
| history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v5.0-v6.6/EAODS-v6.6-alpha-enterprise-incident-command-crisis-management-and-cyber-recovery-governance-standard.md | Case-study scenario elements — coordinated ransomware disrupting authentication services and customer-facing applications, and the executive-governance challenge (Section 4); recovery governance definitions used by the Recovery Coordinator (Section 9); AI crisis-support boundary (Section 12); stated outcomes (Section 13) |
| history/original-sources/conversation-evidence/v17.0-v17.2-volumes/EAODS-v17.0.4-alpha-enterprise-cyber-defense-digital-resilience-framework-volume.md | Case-study scenario elements — cloud identity infrastructure compromise during a peak commercial period and the multi-function coordination challenge (Section 4); evidence-integrity-over-speed principle and evidence governance fields (Section 8); AI containment-authorization boundary (Section 12); corrective action attributes (Section 11); stated outcomes (Section 13) |
| history/original-sources/conversation-evidence/v17.0-v17.2-volumes/EAODS-v17.2.2-alpha-enterprise-domain-03-operations-manual-executive-playbook-vo.md | Case-study scenario elements — simultaneous ransomware, privileged credential compromise, and suspicious dashboard access, with the sequencing and validation challenge (Section 4); runbook architecture and portfolio selection (Section 6); Credential Compromise execution sequence (Section 8); stated outcomes (Section 13) |
| history/original-sources/conversation-evidence/v17.0-v17.2-volumes/EAODS-v17.0.1-alpha-enterprise-cyber-defense-digital-resilience-framework-volume.md | Behavioral detection categories, telemetry fabric normalization scope, and alert explainability requirement (Section 5); AI detection-engineering boundary requiring human approval before production deployment (Section 12) |
| history/original-sources/conversation-evidence/v17.0-v17.2-volumes/EAODS-v17.0.5-alpha-enterprise-cyber-defense-digital-resilience-framework-volume.md | Investigation methodology, evidence governance fields, chain-of-custody record requirements, and prohibition on evidence modification (Section 8); AI forensic-analysis boundary (Section 12) |
| docs/standards/canonical-terminology-and-identifiers.md (STD-0001) | Requirement that an identifier prefix be registered before first use, applied to the incident, evidence, and corrective action fields (Sections 2, 11, 14) |
| docs/standards/cross-artifact-traceability.md (STD-0002) | Registered typed edges applied to the relationships this incident creates (Section 10) |
