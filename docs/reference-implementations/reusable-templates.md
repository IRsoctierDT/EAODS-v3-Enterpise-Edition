---
title: EAODS Reusable Implementation Templates
document_id: EAODS-REF-TPL-001
version: 1.0.0
status: proposed
owner: Enterprise Architecture Review Board
review_gate: Enterprise Architecture Review Board and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - EAODS-ARCH-EOM-001
  - EAODS-ARCH-PRIN-001
  - EAODS-ARCH-SOL-001
  - docs/frameworks/EAODS-v17.3/volume-10-platform-operations.md
  - docs/frameworks/EAODS-v17.3/volume-11-control-catalog.md
  - docs/frameworks/EAODS-v17.3/volume-12-metrics-kpis-kris.md
---

# EAODS Reusable Implementation Templates

## 1. Purpose

This document provides copy-ready record templates for adopters implementing EAODS. Where the solution architecture templates (EAODS-ARCH-SOL-001) describe how to design a solution, this document supplies the four record shapes that make a solution governable once it exists: the **service record**, the **control record**, the **metric/KPI definition**, and the **evidence record**. Each template reproduces a canonical record shape published in EAODS v17.3 Volumes 10, 11, and 12, expands it with attributes those volumes require elsewhere in their own text, and states field-by-field what an adopter must supply. Completed as a set, the four records carry a capability across the traceability chain from named ownership through governing control and measured outcome to registered assurance evidence.

## 2. How to use these templates

1. **Copy the fenced block, then complete every required field.** Angle-bracket tokens such as `<service-id>` are placeholders, not values.
2. **Do not reuse the worked-example identifiers from the volumes.** Volume 10 illustrates the service record with `SVC-00387`; Volume 11 illustrates the control record with `EAODS-CTRL-000184`. Cite those identifiers when referring to the canonical examples or to the governing control they name — never as the identifier of a new adopter record. EAODS-ARCH-SOL-001 states the minting rule for pattern identifiers: identifiers come from the object identifier registry and are never reused. Adopters issue service, control, metric, and evidence identifiers through their own registry under the same discipline.
3. **Optional blocks are optional in form, not in substance**, and completed records are governed artifacts. Where a block is marked optional the underlying obligation still applies, and the record must link to wherever it is satisfied. Volume 11 requires engineering controls to be version-controlled and independently reviewable; Volume 12 requires metric definitions to remain under change control.

## 3. Service record

Volume 10 publishes the canonical service ownership record. The block below is that record with placeholder values, followed by an optional ownership block whose field names render the seven roles named in the Volume 10 service ownership framework.

```yaml
service_id: <service-id>
service_name: <ServiceName>
service_owner: <engineering-owning-team>
operations_owner: <operational-owning-function>
executive_sponsor: <executive-sponsor>
availability_target: <availability-target>
reliability_classification: <tier>
error_budget_policy: <Enforced|Not enforced>
continuous_validation: <Enabled|Disabled>
```

```yaml
# Optional: full ownership declaration (Volume 10 service ownership framework)
ownership:
  business_owner: <business-owner>
  engineering_owner: <engineering-owner>
  operational_owner: <operational-owner>
  executive_sponsor: <executive-sponsor>
  recovery_authority: <recovery-authority>
  architecture_authority: <architecture-authority>
  assurance_owner: <assurance-owner>
```

| Field | Required | Guidance |
|---|---|---|
| `service_id`, `service_name` | Yes | Registry-issued identifier plus a name used consistently across telemetry, control mappings, and evidence. The canonical Volume 10 example is `SVC-00387`; do not copy it into a new record. |
| `service_owner`, `operations_owner` | Yes | The engineering function accountable for the service, and the function accountable for daily running — under Volume 10 the Enterprise Platform Operations Center or its delegate. |
| `executive_sponsor` | Yes | Named executive accountability, per the operating model requirement that every major artifact has an owner. |
| `availability_target` | Yes | Derived from the service level framework. Volume 10 requires objectives based on observed service behavior rather than aspirational targets. |
| `reliability_classification` | Yes | Reliability tier. Tier 1 and recovery-critical services additionally trigger PAT-0004 under EAODS-ARCH-SOL-001. |
| `error_budget_policy` | Yes | Whether error-budget governance is enforced. Volume 10: an exhausted error budget triggers engineering review before further production changes. Accompanying service level definitions use the Volume 10 four-part framework — SLI (measured operational indicator), SLO (expected operational objective), SLA (business commitment where applicable), error budget (controlled reliability risk). |
| `continuous_validation` | Yes | Whether the service is continuously validated and its evidence registered with Continuous Assurance. |
| `ownership.*` | Optional block, mandatory substance | Volume 10 requires every production service to identify all seven roles and to keep ownership continuously documented. |

## 4. Control record

Volume 11 publishes the canonical engineering control. The block below is that record with placeholder values.

```yaml
control_id: <control-id>
control_name: <Control Name>
control_domain: <control-domain>
control_classification: <Preventive|Detective|Corrective|Compensating|Directive>
constitutional_authority: "<governing constitutional reference>"
architecture_reference: "<governing EAODS volume or architecture artifact>"
objective: "<single-sentence statement of what must always be true>"
implementation_guidance: "<how an implementer satisfies the control>"
evidence_requirement: "<what evidence is produced and where it is registered>"
owner: <control-owning-function>
maturity_target: <Level1|Level2|Level3|Level4|Level5>
```

| Field | Required | Guidance |
|---|---|---|
| `control_id`, `control_name` | Yes | Registry-issued identifier and a stable name; renaming an approved control is a change-controlled event. The canonical Volume 11 example is `EAODS-CTRL-000184` (Service Identity Verification), cited by PAT-0001 as the governing control for cross-boundary service identity. |
| `control_domain` | Yes | One of the ten Volume 11 engineering control domains: Architecture governance, Identity and trust, Security engineering, DevSecOps, Data engineering, Automation, Observability, Resilience, Operations, Assurance. Each domain maintains an assigned governance owner. |
| `control_classification` | Yes | Volume 11 classification model. Multiple classifications may apply where justified. |
| `constitutional_authority`, `architecture_reference` | Yes | The governing authority the control derives from and the architecture artifact it implements against; no framework is approved without traceability to its governing authority. |
| `objective` | Yes | Testable outcome statement. Volume 11 requires controls to be risk-informed, measurable, and technology-neutral where practical. |
| `implementation_guidance`, `evidence_requirement` | Yes | Enough detail for an implementer to build to, kept vendor-neutral, plus the evidence produced and its registration point. Volume 11: compliance is determined through objective evidence rather than self-attestation. |
| `owner` | Yes | Responsible owner in the control traceability matrix. |
| `maturity_target` | Yes | Target level on the Volume 11 engineering maturity model (Level 1 Initial through Level 5 Optimizing). Each capability also maintains a current rating and improvement roadmap. |

### 4.1 Optional traceability block

Volume 11 requires every engineering control to trace to seven anchors and to keep that traceability machine-readable where feasible.

```yaml
traceability:
  constitutional_authority: <governing authority>
  architecture_domain: <architecture domain>
  platform_capability: <platform capability>
  implemented_by_service: <service-id>
  validation_evidence: <evidence-id>
  operational_metric: <metric-id>
  responsible_owner: <owner>
```

### 4.2 Optional exception block

Where an implementation cannot satisfy an approved control or pattern, EAODS-ARCH-SOL-001 requires a justified exception recorded under Volume 11 exception governance. Approved exceptions document business justification, associated risks, compensating controls, an expiration date, the approving authority, and a remediation plan; expired exceptions trigger mandatory review.

```yaml
exception:
  business_justification: "<why the control cannot be met as written>"
  associated_risks: "<risks accepted>"
  compensating_controls: "<control-ids or described mitigations>"
  expiration_date: <YYYY-MM-DD>
  approving_authority: <approving authority>
  remediation_plan: "<path back to conformance>"
```

## 5. Metric / KPI definition record

Volume 12 publishes the canonical metric definition. The block below is that record with placeholder values, followed by the governance and quality attributes Volume 12 requires of every enterprise metric.

```yaml
metric_id: <metric-id>
metric_name: <Metric Name>
metric_type: <KPI|KRI|KCI|KMI|Diagnostic Metric|Informational Metric>
metric_owner: <owning-function>
authoritative_source: <authoritative data source>
measurement_frequency: <measurement cadence>
reporting_frequency: <reporting cadence>
target: "<target value or threshold>"
calculation_method: <approved calculation reference>
confidence_level: <High|Medium|Low>
executive_dashboard: <Enabled|Disabled>
```

```yaml
# Required substance (Volume 12 metric governance and data quality)
governance:
  business_owner: <business owner>
  technical_owner: <technical owner>
  calculation_authority: <calculation authority>
  validation_authority: <validation authority>
  reporting_audience: <audience>
  review_frequency: <review cadence>
  retirement_criteria: "<conditions under which the metric is retired>"
data_quality:
  completeness: <assessment>
  accuracy: <assessment>
  consistency: <assessment>
  timeliness: <assessment>
  lineage: <lineage reference>
  provenance: <provenance reference>
  calculation_reproducibility: <assessment>
```

| Field | Required | Guidance |
|---|---|---|
| `metric_id`, `metric_name` | Yes | Registry-issued identifier and stable name. Do not reuse the worked example published in Volume 12. |
| `metric_type`, `metric_owner` | Yes | Volume 12 classification — metrics may belong to multiple reporting categories when justified — and the owning function; each measurement domain maintains an assigned measurement owner. |
| `authoritative_source`, `calculation_method` | Yes | Volume 12: every reported metric identifies its authoritative source and calculation methodology. Reference the approved formula; definitions remain under change control. |
| `measurement_frequency`, `reporting_frequency` | Yes | Distinguish collection cadence from executive reporting cadence. |
| `target` | Yes | For a service reliability metric, align with the `availability_target` in the service record of Section 3. |
| `confidence_level`, `executive_dashboard` | Yes | Volume 12 requires low-confidence metrics to be clearly identified within executive reports; the dashboard flag states whether the metric surfaces to the Executive Control Tower and executive scorecards. |
| `governance.*`, `data_quality.*` | Required substance | The seven governance attributes and seven quality dimensions Volume 12 requires of every enterprise metric. Deprecated metrics remain historically traceable. |

Metrics move through the Volume 12 lifecycle: Definition, Approval, Implementation, Validation, Operational Reporting, Executive Review, Continuous Improvement. A service-scoped metric set should be able to feed the Volume 12 Service Health Score components — availability, latency, error rate, deployment stability, dependency health, security posture, and recovery readiness.

## 6. Evidence record

Volume 10, Volume 11, Volume 12, and `docs/architecture/solution-architecture-templates.md`, as read for this document, state evidence obligations and evidence inputs but do not publish a single canonical evidence YAML in the way they publish the service, control, and metric records. The block below therefore composes the evidence attributes those four sources require; it is a convenience shape for adopters, not a fourth canonical record inherited from the volumes.

```yaml
evidence_id: <evidence-id>
evidence_name: <Evidence Name>
evidence_type: <control implementation|operational evidence|configuration state|automation validation|engineering documentation|runtime observation|audit finding>
supports_control: <control-id>
supports_metric: <metric-id>
produced_by_service: <service-id>
authoritative_source: <system of record>
collection_method: <automated|manual|hybrid>
registration: <assurance registration point>
validation_authority: <independent validation authority>
confidence_level: <High|Medium|Low>
provenance: "<origin, lineage, and integrity reference>"
retention: <retention period or policy reference>
review_frequency: <review cadence>
```

| Field | Required | Guidance |
|---|---|---|
| `evidence_type` | Yes | Drawn from the Volume 11 compliance assessment inputs: control implementation, operational evidence, configuration state, automation validation, engineering documentation, runtime observations, and audit findings. |
| `supports_control`, `supports_metric`, `produced_by_service` | At least one | These three links close the Volume 11 control traceability matrix (implemented service, validation evidence, operational metrics). |
| `authoritative_source` | Yes | The system of record. EAODS-ARCH-SOL-001 maps this to the Evidence Platform capability profile (immutable assurance records). |
| `collection_method`, `registration` | Yes | Prefer automated collection; Volume 11 continuous compliance monitors configuration drift, architecture deviations, failed validations, policy violations, control health, and engineering debt. Volume 11's canonical control requires evidence registered with Continuous Assurance. |
| `validation_authority`, `confidence_level` | Yes | Validation is independent of the producing team — Volume 11 determines compliance through objective evidence rather than self-attestation, and Volume 10 has Continuous Assurance verify operational evidence independently. Confidence stays consistent with any metric the evidence supports. |
| `provenance`, `retention`, `review_frequency` | Yes | The operating model retains historical content through provenance, checksums, and supersession records; set retention so that superseded evidence remains historically traceable rather than discarded. |

## 7. Joining the records into one traceable chain

Completed together, the four records produce the linkage the architecture principles require between control, implementation, operation, and assurance.

| From | Field | To | Effect |
|---|---|---|---|
| Control record | `traceability.implemented_by_service` | Service record `service_id` | The control names the service that implements it |
| Service record | `availability_target`, `error_budget_policy` | Metric record `target`, `metric_type` | Reliability objectives become measured, reported metrics |
| Control record | `traceability.operational_metric` | Metric record `metric_id` | Control effectiveness becomes observable (Volume 12 KCI classification) |
| Evidence record | `supports_control`, `produced_by_service`, `supports_metric` | All three records | Assurance evidence closes the loop back to control, service, and metric |
| Any record | `exception` block | Volume 11 exception governance | Non-conformance is governed, time-bounded, and remediated |

## 8. Adoption completeness checklist

Adapted from the QA checklists of Volumes 10, 11, and 12. Complete before submitting records to the review gate.

- [ ] Service record complete, including all seven ownership roles.
- [ ] Service level framework documented — SLI, SLO, SLA where applicable, error budget — with error-budget governance stated and enforceable.
- [ ] Control record complete, with domain, classification, maturity target, and all seven traceability anchors populated.
- [ ] Any exception recorded with justification, risks, compensating controls, expiry, approver, and remediation plan.
- [ ] Metric definition complete, with authoritative source, approved calculation method, governance attributes, and data quality attributes.
- [ ] Evidence record links to at least one control, metric, or service; names its registration and validation authority; and is registered with Continuous Assurance.
- [ ] YAML front matter validated on every governed document carrying these records, and the human review gate completed.

## 9. Illustrative adoption scenarios

The three scenarios below are the **illustrative case studies published in the volumes' own case-study sections**. They describe anonymous, hypothetical enterprises used to explain the framework. They are not real deployments, not customer references, and not measured results; the stated outcomes are the volumes' illustrative narrative, and adopters should read them as shape-of-problem indicators of which record set to complete first.

| Illustrative scenario (source volume) | Situation as described | Templates it exercises | Outcome as narrated in the source |
|---|---|---|---|
| Global retail enterprise running AI-assisted cybersecurity services across hybrid cloud (Volume 10 case study) | Detection performs well, but platform engineering issues, deployment instability, and unclear service ownership degrade reliability | Service record; metric record for observed-behavior SLOs | Reliability and deployment stability improve, operational debt declines, and leadership gains continuous visibility into service health |
| Multinational manufacturing enterprise expanding AI-assisted cyber operations across business units (Volume 11 case study) | Independent teams implement services with inconsistent controls, documentation, and architecture patterns | Control record, including traceability and exception blocks | Engineering consistency improves, architecture deviations decline, and compliance reporting becomes evidence-driven |
| Multinational technology enterprise operating AI-assisted security platforms across five regions (Volume 12 case study) | Executive leadership receives inconsistent reports from disconnected data sources | Metric record with governance and data quality blocks; evidence record | Executive reporting becomes evidence-based and operational trends become comparable over time |

## 10. Human review gate

Approval of this template set requires confirmation by the Enterprise Architecture Review Board and the Program Owner that:

- every template field traces to a canonical record shape or stated requirement in Volume 10, Volume 11, Volume 12, or EAODS-ARCH-SOL-001, and no template introduces a metric, control, organizational unit, or outcome absent from those sources;
- no worked-example identifier is presented as available for reuse, and identifier minting remains a registry function;
- the evidence record is presented as a composed convenience shape rather than an inherited canonical record, and the case-study material remains labelled as illustrative.

Changes to the canonical record shapes themselves are governed by the volumes that publish them and follow those volumes' own review gates.

## 11. Sources and traceability

| Source (repo-relative path) | Contribution |
|---|---|
| `docs/frameworks/EAODS-v17.3/volume-10-platform-operations.md` | Canonical service ownership record and its fields (Section 3); seven-role service ownership framework; SLI/SLO/SLA/error-budget service level framework with the observed-behavior and error-budget-review rules; Continuous Assurance independent verification of operational evidence (Section 6); QA checklist basis (Section 8); Volume 10 illustrative case study (Section 9) |
| `docs/frameworks/EAODS-v17.3/volume-11-control-catalog.md` | Canonical engineering control record and its fields (Section 4); ten engineering control domains and their governance owners; control classification model; engineering maturity model Levels 1–5; seven-anchor control traceability matrix (Section 4.1); architecture exception governance attributes (Section 4.2); compliance assessment inputs used as evidence types and the evidence-over-self-attestation rule (Section 6); continuous compliance monitoring scope; version control and independent reviewability of controls (Section 2); QA checklist basis (Section 8); Volume 11 illustrative case study (Section 9) |
| `docs/frameworks/EAODS-v17.3/volume-12-metrics-kpis-kris.md` | Canonical metric definition record and its fields (Section 5); metric classification set; seven metric governance attributes; seven data quality dimensions; metric lifecycle; Service Health Score components; change control over metric definitions; low-confidence reporting rule; historical traceability of deprecated metrics; QA checklist basis (Section 8); Volume 12 illustrative case study (Section 9) |
| `docs/architecture/solution-architecture-templates.md` (EAODS-ARCH-SOL-001) | Positioning of this document relative to solution design (Section 1); identifier registry minting and no-reuse rule (Section 2); PAT-0001 and EAODS-CTRL-000184 linkage for cross-boundary service identity (Section 4); PAT-0004 applicability to Tier 1 and recovery-critical services (Section 3); apply-or-exception rule referencing Volume 11 (Section 4.2); Evidence Platform capability profile as immutable assurance records (Section 6); required-field template convention and review gate framing |
| `docs/architecture/ENTERPRISE_OPERATING_MODEL.md` (EAODS-ARCH-EOM-001) | House front matter and numbered-section conventions; named ownership of every major artifact (Section 3); reference implementation requirements of control enforcement, ownership, measurable outcomes, traceable evidence, and human review gates (Sections 1, 7); provenance, checksum, and supersession discipline applied to evidence retention (Section 6) |
| `docs/architecture/architecture-principles.md` (EAODS-ARCH-PRIN-001) | House style for field-by-field guidance tables and review-gate sections; end-to-end traceability and evidence-precedes-assertion principles underpinning the joined record chain (Section 7); no-principle-absent-from-sources test adapted into the review gate (Section 10) |
