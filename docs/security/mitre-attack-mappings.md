---
title: EAODS MITRE ATT&CK Mapping Standard
document_id: EAODS-SEC-ATTACK-001
version: 1.0.0
status: proposed
owner: Enterprise Cyber Command
review_gate: Security Architecture Review Board and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - THR-0001
  - PAT-0001
  - PAT-0003
  - RUN-0003
  - STD-0001
  - STD-0002
  - ADR-0002
  - EAODS-CTRL-000184
  - history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v5.0-v6.6/EAODS-v6.4-alpha-enterprise-security-detection-engineering-analytics-and-adversary-emulation-architecture-standard.md
  - history/original-sources/conversation-evidence/v17.0-v17.2-volumes/EAODS-v17.0.1-alpha-enterprise-cyber-defense-digital-resilience-framework-volume.md
  - history/original-sources/conversation-evidence/v17.0-v17.2-volumes/EAODS-v17.0.10-alpha-enterprise-cyber-defense-digital-resilience-framework-volume.md
---

# EAODS MITRE ATT&CK Mapping Standard

## 1. Purpose

This standard defines how EAODS relates adversary behavior to enterprise defensive
objects, and how the resulting coverage is measured, evidenced, and reported.

It exists because the historical corpus consistently requires detections to be
"threat-informed" and "mapped to enterprise controls and risks" (v6.4) and requires
detection entities to maintain governed relationships with "attack techniques"
(v17.0.1, v17.0.2) — but nowhere defines the mapping object, the relationship
semantics, or the arithmetic behind the word *coverage*. This standard supplies
those definitions without asserting technique content the corpus does not contain.

## 2. Scope

Applies to every governed detection, hunt, adversary-simulation exercise, threat
model, and control that claims alignment to adversary behavior in this repository.
It governs the mapping records themselves and does not restate detection
engineering procedure.

## 3. Evidentiary position on technique identifiers

The following statement is normative and must be preserved through revision.

**No MITRE ATT&CK technique identifier, sub-technique identifier, or tactic
identifier appears in any EAODS source unit reviewed for this standard.** The
v5.0–v6.6 transmission set and the v17.0–v17.2 volume set were searched in full for
ATT&CK naming and for technique- and tactic-shaped tokens; neither returned a
match. MITRE ATT&CK is named in the corpus only as a framework the Volume 10
planning record intended to integrate alongside ISO 27001 and NIST CSF 2.0
(`docs/history/00_MASTER_CORPUS.md`).

Consequences:

1. This standard defines mapping **method**, not a technique catalogue.
2. No technique identifier shall be written into any EAODS artifact until it is
   transcribed from published MITRE ATT&CK content by a named human reviewer and
   recorded with that provenance.
3. A mapping record with no technique identifier is valid and complete under this
   standard. Its technique field carries the state `unassigned`, never a guess.
4. Inventing, inferring, or pattern-matching a technique identifier is a defect of
   the same class as an unregistered identifier under STD-0002.

## 4. What maps to what

The mapping graph has one behavior node type and four defensive node types. The
behavior node is the unit of mapping; ATT&CK is one of the vocabularies that may
label it, not the node itself.

| Node | Meaning | Source of the concept |
|---|---|---|
| Adversary behavior | A named observable action — credential abuse, privilege escalation, lateral movement, persistence, anomalous authentication, data access anomaly | Behavioral Detection Framework, v17.0.1 |
| Detection | Certified detection content with owner, telemetry sources, and validation status | Canonical Detection Record, v17.0.1; Detection Object Model, v6.4 |
| Hunt | Hypothesis-driven proactive investigation of a behavior | Canonical Hunt Record, v17.0.3 |
| Validation exercise | Authorized purple-team or adversary-simulation activity | Canonical Validation Exercise Record, v17.0.10 |
| Control / threat model | Enterprise control or registered threat scenario | THR-0001; EAODS-CTRL-000184 |

Relationship semantics reuse the registered edge types of STD-0002. No new edge
type is introduced by this standard:

| Relationship | Edge type | Reading |
|---|---|---|
| Detection → behavior | `mitigates` | The detection reduces exposure to the behavior |
| Validation exercise → detection | `applies_to` | The exercise tests that detection under representative conditions |
| Hunt → behavior | `applies_to` | The hunt investigates the behavior against enterprise telemetry |
| Detection → control | `implements` | The detection realizes a detective control |
| Coverage report → assurance | `emits_evidence_to` | Coverage state is assurance evidence, not commentary |
| Mapping record → this standard | `governed_by` | Mapping records are subordinate to EAODS-SEC-ATTACK-001 |

## 5. Mapping record

Every mapping is a governed record. Its fields are drawn from the detection,
hunt, and exercise schemas already present in the corpus; this standard adds only
the technique-labelling fields and their state discipline.

| Field | Required | Origin |
|---|---|---|
| `behavior_name` | Yes | Behavioral Detection Framework, v17.0.1 |
| `behavior_description` | Yes | Hypothesis Engineering Framework, v17.0.3 |
| `attack_technique_id` | Yes, may be `unassigned` | This standard, section 3 |
| `attack_source_provenance` | Yes when an id is present | This standard, section 3 |
| `detection_id` | Yes when a detection exists | Canonical Detection Record, v17.0.1 |
| `telemetry_sources` | Yes | Enterprise Telemetry Fabric, v17.0.1 |
| `owner` | Yes | Detection Object Model, v6.4 |
| `validation_status` | Yes | Detection Object Model, v6.4 |
| `coverage_state` | Yes | This standard, section 6 |
| `related_controls` | Yes | Detection Object Model, v6.4 |
| `related_risks` | Yes | Detection Object Model, v6.4 |
| `last_validated` | Yes at coverage state C4 or above | Detection Certification Framework, v17.0.1 |

Identifier discipline: mapping records cite detections, hunts, and exercises by
identifier only after the relevant prefix is registered under STD-0001. At the time
of writing, no detection, hunt, or exercise prefix is registered; mapping records
shall therefore carry object references as registry-pending until Engineering
Governance registers the prefixes. Registration precedes use, without exception.

## 6. Coverage model

Coverage is a state per behavior, not a percentage of a technique list. The ladder
below composes stages that the corpus already defines; each state is the literal
completion of a named source construct, which is what makes the state auditable.

| State | Name | Entry condition | Governing source construct |
|---|---|---|---|
| C0 | Unmapped | No mapping record exists for the behavior | — |
| C1 | Mapped | Mapping record exists with owner and description | Mapping record, section 5 |
| C2 | Instrumented | Required telemetry sources exist and pass the telemetry quality framework | Telemetry Quality Framework, v17.0.1 |
| C3 | Detected | A certified detection is deployed against the behavior | Detection Certification Framework, v17.0.1 |
| C4 | Validated | A purple-team or adversary-simulation exercise verified the detection | Detection Verification Framework, v17.0.10 |
| C5 | Continuously verified | Registered with Continuous Assurance and subject to recertification | Continuous Control Assurance, v17.0.10; DQ-5, v6.4 |

Three rules bind the ladder:

1. **States are not skippable.** A behavior cannot reach C3 while its telemetry
   fails quality validation; the corpus is explicit that material telemetry
   degradation triggers engineering review rather than silent progression.
2. **States decay.** Control degradation triggers reassessment (v17.0.10); a
   behavior whose detection loses certification or whose telemetry source degrades
   returns to the highest state it can still evidence.
3. **Only C4 and C5 may be reported as assurance.** C1–C3 are engineering progress.
   Reporting an untested detection as coverage is the failure mode this standard
   exists to prevent — validation exists "to improve defensive capability, not to
   demonstrate offensive sophistication" (v17.2.4).

## 7. Coverage measurement

Coverage is measured across the registered behavior set, reported as counts by
state, and never as a single composite score. The metrics below are those the
corpus already names; this standard adds no new metric.

| Metric | Definition under this standard | Source |
|---|---|---|
| Telemetry coverage | Behaviors at C2 or above | v17.0.1 detection effectiveness metrics |
| Detection coverage | Behaviors at C3 or above | v6.4 detection coverage by capability |
| Validated control coverage | Behaviors at C4 or above | v17.0.10 enterprise validation metrics |
| Adversary coverage | Behaviors at C4 or above attributable to a profiled adversary | v17.0.3 enterprise hunt metrics |
| Coverage gaps | Behaviors at C0 or C1 | v6.4 Executive Control Tower integration |
| Detection verification success | Share of C4 attempts that verified on first exercise | v17.0.10 |

Coverage arithmetic is honest only if the denominator is stated. Every coverage
figure published from this repository shall name the behavior set it was computed
over and the date of the underlying validation evidence. A coverage figure without
a named denominator is not a measurement and shall not pass review.

## 8. Worked application — THR-0001

THR-0001 (compromised service identity) is mapped below to demonstrate the record
shape. Behavior names are taken from the corpus behavioral and hunt vocabularies;
technique identifiers are `unassigned` because, per section 3, no source supplies
one. The example asserts no coverage state above C1: no validation evidence exists
in the sources for these behaviors.

| THR-0001 scenario | Behavior name | ATT&CK technique | Hunt playbook | Mitigating control |
|---|---|---|---|---|
| Credential theft and replay | Credential abuse | `unassigned` | Identity Abuse Hunt | EAODS-CTRL-000184 · PAT-0001 |
| Scope escalation | Privilege escalation | `unassigned` | Privilege Escalation Hunt | PAT-0001 |
| Identity authority compromise | Anomalous authentication | `unassigned` | Identity Abuse Hunt | PAT-0004 · RUN-0001 |
| Revocation lag | Anomalous authentication | `unassigned` | Identity Abuse Hunt | EAODS-CTRL-000184 |

Hunt playbook names are the literal portfolio entries of v17.2.3. Control and
pattern citations are the mitigations THR-0001 already records; this standard
restates them as edges and adds nothing.

## 9. Mapping lifecycle

```text
Threat model or intelligence requirement
   ▼  behavior named, mapping record created          (C1)
   ▼  telemetry validated                             (C2)
   ▼  detection engineered, reviewed, certified       (C3)
   ▼  adversary simulation or purple-team validation  (C4)
   ▼  Continuous Assurance registration               (C5)
```

The sequence is the corpus detection lifecycle and validation lifecycle joined at
the point both already reference: validation findings become governed engineering
inputs. Every transition produces evidence; no transition is self-attested by the
team that owns the detection.

## 10. Evidence and assurance integration

Coverage state changes are assurance evidence and follow PAT-0003. Exercise
records, telemetry quality results, and certification decisions are the evidence
objects; the coverage report is a derived view over them, never a hand-maintained
list. Unresolved validation findings and behaviors that decay below their reported
state are compliance deviations and are handled under RUN-0003, with Enterprise
Cyber Command escalation consistent with the assurance hooks THR-0001 defines.

## 11. AI assistance boundaries

AI assistance may draft mapping records, propose behavior groupings, summarize
exercise evidence, and identify candidate coverage gaps. Consistent with the
operating model's AI boundaries and the corpus validation rules, AI shall not
assign a technique identifier, advance a coverage state, authorize or expand a
validation exercise, or certify a detection. Every mapping record entering C3 or
above carries a named human approver.

## 12. Prohibited practices

1. Writing a technique identifier that was not transcribed from published MITRE
   ATT&CK content with recorded provenance.
2. Publishing a coverage percentage without its behavior-set denominator and
   evidence date.
3. Reporting C1–C3 states as validated coverage in executive material.
4. Minting detection, hunt, or exercise identifiers before STD-0001 registration.
5. Retiring a mapping record; records are retained with a retired status, as
   STD-0001 requires of all governed objects.

## 13. Human review gate

Approval requires confirmation that the evidentiary position in section 3 remains
accurate against the sources; that no technique identifier appears without recorded
provenance; that the coverage ladder still maps state-for-state to named source
constructs; that every metric in section 7 remains traceable to a source unit; and
that identifier discipline under STD-0001 and STD-0002 is intact. Material change
to the coverage model requires Security Architecture Review Board and Program Owner
approval.

## 14. Sources and traceability

| Source (repo-relative) | Contribution |
|---|---|
| `history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v5.0-v6.6/EAODS-v6.4-alpha-enterprise-security-detection-engineering-analytics-and-adversary-emulation-architecture-standard.md` | Detection Object Model fields (owner, validation status, related controls, related risks); threat-informed and mapped-to-controls principles; detection coverage by capability and coverage gaps as reported measures; DQ-5 "Continuously Verified" quality level |
| `history/original-sources/conversation-evidence/v17.0-v17.2-volumes/EAODS-v17.0.1-alpha-enterprise-cyber-defense-digital-resilience-framework-volume.md` | Behavioral Detection Framework behavior vocabulary; Canonical Detection Record fields; Telemetry Quality Framework as the C2 gate; Detection Certification Framework as the C3 gate; knowledge-graph relationship to attack techniques; detection effectiveness metric names |
| `history/original-sources/conversation-evidence/v17.0-v17.2-volumes/EAODS-v17.0.2-alpha-enterprise-cyber-defense-digital-resilience-framework-volume.md` | Adversary Knowledge Management (adversary profiles carry preferred techniques); intelligence knowledge graph edge to attack techniques, establishing the behavior node as the mapping unit |
| `history/original-sources/conversation-evidence/v17.0-v17.2-volumes/EAODS-v17.0.3-alpha-enterprise-cyber-defense-digital-resilience-framework-volume.md` | Canonical Hunt Record; hypothesis engineering fields; adversary emulation validating detection coverage; adversary coverage as an enterprise hunt metric |
| `history/original-sources/conversation-evidence/v17.0-v17.2-volumes/EAODS-v17.0.10-alpha-enterprise-cyber-defense-digital-resilience-framework-volume.md` | Canonical Validation Exercise Record; Detection Verification Framework as the C4 gate; Continuous Control Assurance and degradation-triggered reassessment as the C5 gate and decay rule; validated control coverage and detection verification success metrics |
| `history/original-sources/conversation-evidence/v17.0-v17.2-volumes/EAODS-v17.2.3-alpha-enterprise-domain-03-operations-manual-executive-playbook-vo.md` | Threat Hunting Playbook Portfolio names used in section 8; detection change governance and peer approval expectations |
| `history/original-sources/conversation-evidence/v17.0-v17.2-volumes/EAODS-v17.2.4-alpha-enterprise-domain-03-operations-manual-executive-playbook-vo.md` | Validation principles (authorized, controlled, measurable, evidence-driven); the purpose statement constraining coverage reporting; adversary emulation scenario vocabulary; AI validation boundaries |
| `docs/threat-models/THR-0001-compromised-service-identity.md` | Scenario set, mitigation and control citations, and assurance hooks used in the worked application and section 10 |
| `docs/architecture/ENTERPRISE_OPERATING_MODEL.md` | House structure; Domain 03 cross-pillar position; AI operating boundaries; traceability-to-controls-and-evidence requirement |
| `docs/standards/canonical-terminology-and-identifiers.md` | STD-0001 identifier format, registration-before-use, stability, and retention rules applied in sections 5 and 12 |
| `docs/standards/cross-artifact-traceability.md` | STD-0002 registered edge types reused in section 4; the no-unregistered-identifier rule underwriting section 3 |
| `docs/history/00_MASTER_CORPUS.md` | The corpus's only literal reference to MITRE ATT&CK — as a framework intended for integration alongside ISO 27001 and NIST CSF 2.0 — evidencing section 3 |
