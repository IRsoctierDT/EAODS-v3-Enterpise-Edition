---
title: MITRE ATT&CK Technique Transcription Worksheet
document_id: EAODS-SEC-ATTACK-WS-001
version: 1.0.0
status: completed — ratified 2026-08-03
owner: Enterprise Cyber Command
review_gate: Security Architecture Review Board — named reviewer transcription and ratification
governing_architecture: EAODS v17.3 Volume 10
related:
  - docs/security/mitre-attack-mappings.md
  - docs/threat-models/threat-model-library.md
  - docs/threat-models/THR-0001-compromised-service-identity.md
  - docs/threat-models/THR-0002-llm-instruction-injection.md
  - docs/threat-models/THR-0003-assurance-evidence-tampering.md
---

# MITRE ATT&CK Technique Transcription Worksheet

## 1. What this document is, and is not

`EAODS-SEC-ATTACK-001` §3 states that no technique identifier may be written
into a governed EAODS artifact until it is **transcribed from published MITRE
ATT&CK content by a named human reviewer and recorded with that provenance**.

This worksheet exists to make that reviewer's job ratification rather than
research. It carries candidate identifiers retrieved from `attack.mitre.org`
with their retrieval provenance, so a reviewer can confirm or reject each row
against the authoritative source.

**It is not a governed mapping record.** Nothing here is promoted into
`mitre-attack-mappings.md`, the threat-model library, or any detection or
control record until the ratification column is completed and this document's
status changes. Until then, every governed mapping remains `unassigned`, which
§3 explicitly declares a valid and complete state.

## 2. Retrieval provenance

| Field | Value |
|---|---|
| Source | `https://attack.mitre.org/techniques/<ID>/` (per-row) |
| Retrieved | 2026-08-03 |
| Retrieved by | Direct retrieval from attack.mitre.org, 2026-08-03; ratified by the Program Owner |
| ATT&CK release | **v19**, current from 2026-04-28 (recorded at ratification) |

## 3. A correction, retained as the instructive part of this record

The first draft of this worksheet asserted:

> During retrieval, the fetch summarised the tactic for `T1078` and `T1070` as
> "Stealth". ATT&CK has no tactic by that name; `TA0005` is **Defense Evasion**.
> The summarisation layer paraphrased a controlled value.

**That assertion was wrong, and the retrieval was right.** Verification against
`attack.mitre.org/tactics/TA0005/` and the Enterprise tactics index confirms
that in **ATT&CK v19** (current from 2026-04-28) `TA0005` is named **Stealth**,
and that **Defense Impairment (`TA0112`)** was created 2026-04-14.

The error came from checking retrieved data against prior knowledge of a
*previous* ATT&CK release rather than against the authoritative source. It is
retained here rather than quietly deleted, because it is the most useful thing
this worksheet produced:

1. **A plausible-sounding correction can be the defect.** The "paraphrase" story
   was coherent, and it was false.
2. **Controlled vocabularies drift; identifiers do not.** `TA0005` has been
   stable while its name changed. The mapping standard therefore treats the
   identifier as the mapped value and the name as readability only.
3. **Verification must terminate at the authoritative source**, not at a
   confident recollection of it.

## 4. Candidate transcriptions — THR-0001 Compromised Service Identity

| Technique ID | Technique name (as displayed) | Relevance to the threat model | Confidence | Ratified? |
|---|---|---|---|---|
| `T1078` | Valid Accounts | Abuse of existing service credentials for access, persistence, or escalation | Verbatim from source | ☑ |
| `T1078.004` | Cloud Accounts | Sub-technique — cloud service identity abuse | Verbatim from source | ☑ |
| `T1550` | Use Alternate Authentication Material | Use of tokens, hashes, or tickets in place of credentials | Verbatim from source | ☑ |
| `T1550.001` | Application Access Token | Sub-technique — direct match to service-token misuse | Verbatim from source | ☑ |
| `T1528` | Steal Application Access Token | Theft of tokens from workloads, CI/CD, and metadata services | Verbatim from source | ☑ |

## 5. Candidate transcriptions — THR-0003 Assurance Evidence Tampering

| Technique ID | Technique name (as displayed) | Relevance to the threat model | Confidence | Ratified? |
|---|---|---|---|---|
| `T1070` | Indicator Removal | Deletion or modification of artifacts to reduce evidence of activity | Verbatim from source | ☑ |
| `T1070.004` | File Deletion | Sub-technique — removal of evidence files | Verbatim from source | ☑ |
| `T1070.006` | Timestomp | Sub-technique — timestamp manipulation defeating evidence ordering | Verbatim from source | ☑ |
| `T1565` | Data Manipulation | Insertion, deletion, or alteration of data, threatening integrity | Verbatim from source | ☑ |
| `T1565.001` | Stored Data Manipulation | Sub-technique — alteration of data at rest, including evidence stores | Verbatim from source | ☑ |

## 6. THR-0002 LLM Instruction Injection — no ATT&CK candidate proposed

No ATT&CK Enterprise technique was identified that describes instruction
injection against a language model. This is recorded as a finding, not a gap
to be filled by approximation: mapping this threat model to a loosely adjacent
ATT&CK technique would be exactly the inference §3 prohibits.

MITRE **ATLAS** — a separate knowledge base for adversarial threats to
AI-enabled systems — appears to carry a relevant technique. A secondary source
indicates `AML.T0051` "LLM Prompt Injection" with sub-techniques. **This was
not confirmed against the authoritative ATLAS site**, which did not resolve at
the URLs attempted during retrieval.

Recommendation for the reviewer: treat ATLAS as a distinct framework requiring
its own registered identifier prefix and its own mapping section in
`EAODS-SEC-ATTACK-001` before any `AML.*` identifier is used. Do not record
`AML.T0051` on the strength of the secondary source alone.

## 7. Ratification procedure

1. Open the authoritative page for each candidate at `attack.mitre.org`.
2. Confirm the identifier and name match this worksheet exactly.
3. Record the ATT&CK release version in section 2.
4. Add tactic assignments from the authoritative page — they are absent here by
   design (section 3).
5. Tick the ratification column, and record the reviewer's name and date below.
6. Only then promote ratified rows into the governed mapping records, carrying
   the transcription provenance with them.
7. Reject any row that does not match; a rejected row is evidence, not an error.

| Reviewer | Date | Rows ratified | Rows rejected |
|---|---|---|---|
| Program Owner | 2026-08-03 | 10 | 0 |

Ratified rows are published in `EAODS-SEC-ATTACK-001` §8, with the full
transcription record — tactic assignments and technique versions as published in
v19 — in that standard's transcription-record section. THR-0002 remains
deliberately unmapped (section 6).

## 8. Sources and traceability

| Source (repo-relative or URL) | Contribution |
|---|---|
| `docs/security/mitre-attack-mappings.md` | §3 evidentiary position and the transcription rule this worksheet serves |
| `docs/threat-models/THR-0001-compromised-service-identity.md` | Threat model scoped in section 4 |
| `docs/threat-models/THR-0002-llm-instruction-injection.md` | Threat model addressed in section 6 |
| `docs/threat-models/THR-0003-assurance-evidence-tampering.md` | Threat model scoped in section 5 |
| `https://attack.mitre.org/techniques/T1078/` · `T1550/` · `T1528/` · `T1070/` · `T1565/` | Candidate technique identifiers and names, retrieved 2026-08-03 |
