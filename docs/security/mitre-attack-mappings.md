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
identifier appears in any Domain 03 source authority for this standard.** The
v5.0–v6.6 transmission set and the v17.0–v17.2 volume set were searched in full for
ATT&CK naming and for technique- and tactic-shaped tokens; neither returned a
match.

ATT&CK does appear elsewhere in the repository, and this standard records those
occurrences rather than claiming they do not exist. None is a Domain 03 source
authority, and none carries transcription provenance:

- as a framework named for future integration alongside ISO 27001 and NIST CSF
  2.0 (`docs/history/00_MASTER_CORPUS.md`;
  `docs/history/07_HISTORICAL_ARTIFACT_RECORDS.md`), and as an outstanding
  compliance-mapping recommendation (v4.16);
- as an optional vulnerability-record field named "MITRE ATT&CK technique
  mapping", with no identifiers enumerated (v4.17, v4.17.1);
- as literal technique identifiers used as illustrative fixtures in the v3
  Enterprise Edition detection-matcher appendices.

The third category is the one that matters here: those identifiers are sample
data in a superseded prototype, carry no recorded source, and are therefore
unusable as provenance. They are not promoted into any governed mapping record.

**Transcription performed 2026-08-03 (ATT&CK v19).** Technique identifiers now
appearing in this standard were transcribed from `attack.mitre.org` on that date
and ratified by the Program Owner; see section 9 for the transcription record.
The statement above remains true of the *source authorities* — the identifiers
come from MITRE, not from the corpus, which is exactly what this section
requires.

Consequences:

1. This standard defines mapping **method**, not a technique catalogue.
2. No technique identifier shall be written into any governed EAODS artifact
   until it is transcribed from published MITRE ATT&CK content by a named human
   reviewer and recorded with that provenance. Preserved historical sources are
   not rewritten to satisfy this rule; they are simply not cited as provenance.
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

THR-0001 (compromised service identity) is mapped below. Behavior names are taken
from the corpus behavioral and hunt vocabularies; technique identifiers were
transcribed from ATT&CK v19 on 2026-08-03 (section 9). The example asserts no
coverage state above C1: no validation evidence exists in the sources for these
behaviors, and a transcribed identifier does not by itself advance coverage.

| THR-0001 scenario | Behavior name | ATT&CK technique | Hunt playbook | Mitigating control |
|---|---|---|---|---|
| Credential theft and replay | Credential abuse | `T1078` Valid Accounts · `T1550.001` Application Access Token | Identity Abuse Hunt | EAODS-CTRL-000184 · PAT-0001 |
| Scope escalation | Privilege escalation | `T1078` Valid Accounts | Privilege Escalation Hunt | PAT-0001 |
| Identity authority compromise | Anomalous authentication | `T1528` Steal Application Access Token · `T1550` Use Alternate Authentication Material | Identity Abuse Hunt | PAT-0004 · RUN-0001 |
| Revocation lag | Anomalous authentication | `T1078.004` Cloud Accounts | Identity Abuse Hunt | EAODS-CTRL-000184 |

THR-0003 (assurance evidence tampering) is mapped on the same terms:

| THR-0003 scenario | Behavior name | ATT&CK technique | Mitigating control |
|---|---|---|---|
| Evidence deletion | Evidence tampering | `T1070.004` File Deletion | EAODS-CTRL-000184 · PAT-0003 |
| Evidence record alteration | Evidence tampering | `T1565.001` Stored Data Manipulation | PAT-0003 |
| Evidence ordering defeat | Evidence tampering | `T1070.006` Timestomp | PAT-0003 |
| Broad indicator suppression | Evidence tampering | `T1070` Indicator Removal | PAT-0003 · RUN-0003 |

**THR-0002 (LLM instruction injection) remains `unassigned`.** No ATT&CK
Enterprise technique describes instruction injection against a language model,
and mapping it to an adjacent technique would be the inference section 3
prohibits. MITRE ATLAS appears to cover this class of threat; adopting any
`AML.*` identifier requires registering ATLAS as a distinct framework with its
own identifier prefix under STD-0001 first. That is open work, not a gap in this
mapping.

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

## 14. Transcription record

Identifiers in this standard were transcribed under the section 3 rule.

| Field | Value |
|---|---|
| Source | `https://attack.mitre.org/techniques/<ID>/` and `https://attack.mitre.org/tactics/enterprise/` |
| ATT&CK release | **v19** (current from 2026-04-28) |
| Transcribed | 2026-08-03 |
| Method | Direct retrieval of each technique page; identifier, name, tactic assignment, and technique version taken from the page metadata |
| Ratified by | Program Owner |

| Technique | Name (as published) | Tactic(s) as published in v19 | Technique version |
|---|---|---|---|
| `T1078` | Valid Accounts | Stealth (TA0005) · Persistence (TA0003) · Privilege Escalation (TA0004) · Initial Access (TA0001) | 3.0 |
| `T1078.004` | Cloud Accounts | sub-technique of T1078 | — |
| `T1550` | Use Alternate Authentication Material | Lateral Movement (TA0008) | 2.0 |
| `T1550.001` | Application Access Token | sub-technique of T1550 | — |
| `T1528` | Steal Application Access Token | Credential Access (TA0006) | 1.5 |
| `T1070` | Indicator Removal | Stealth (TA0005) | 3.0 |
| `T1070.004` | File Deletion | sub-technique of T1070 | — |
| `T1070.006` | Timestomp | sub-technique of T1070 | — |
| `T1565` | Data Manipulation | Impact (TA0040) | 1.1 |
| `T1565.001` | Stored Data Manipulation | sub-technique of T1565 | — |

**Vocabulary note.** In ATT&CK v19, `TA0005` is named **Stealth**, and
**Defense Impairment (`TA0112`)** was created 2026-04-14. Material predating v19
— including older EAODS drafts and most external writing — refers to `TA0005` as
"Defense Evasion". Reviewers reconciling this standard against pre-v19 material
should treat "Defense Evasion" and "Stealth" as the same tactic identifier and
check whether a behavior belongs under `TA0112` instead. Tactic names are not
stable across ATT&CK releases; **identifiers are**, which is why the identifier
is the mapped value and the name is carried only for readability.

**Re-transcription trigger.** A new ATT&CK release requires re-checking every row
above; a name change alone does not invalidate a mapping, but a technique
deprecation or re-identification does.

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
| `docs/history/00_MASTER_CORPUS.md` · `docs/history/07_HISTORICAL_ARTIFACT_RECORDS.md` · `history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v4.6-v4.21-longgap/EAODS-v4.16-alpha-cybersecurity-core-domain-alignment-matrix.md` | ATT&CK named as a framework for future integration alongside ISO 27001 and NIST CSF 2.0, and as an outstanding compliance-mapping recommendation — the framework-level occurrences recorded in section 3 |
| `history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v4.6-v4.21-longgap/EAODS-v4.17-alpha-enterprise-threat-vulnerability-management-standard.md` · `.../units/v4.17.1-v4.28/EAODS-v4.17.1-alpha-vulnerability-intake-and-triage-workflow.md` | "MITRE ATT&CK technique mapping" as an optional vulnerability-record field with no identifiers enumerated — the field-level occurrences recorded in section 3 |
| `history/original-sources/EAODS_v3_Enterprise_Edition/Source-Code-Appendices/detection_matcher_agent.py` · `.../Volume-05-Security-Agents/detection-matcher-agent_handbook_v3.md` | The only literal technique identifiers in the repository, present as prototype fixture data without recorded provenance — the occurrences section 3 excludes from use |
