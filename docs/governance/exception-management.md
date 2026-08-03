---
title: EAODS Exception Management and Exception Register
document_id: EAODS-GOV-EXC-001
version: 1.0.0
status: proposed
owner: Enterprise Governance Office
review_gate: Enterprise Governance Board and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - EAODS-ARCH-GOV-001
  - EAODS-ARCH-EOM-001
  - EAODS-MIG-EXC-001
  - EAODS-GOV-RISK-001
  - ADR-0002
  - STD-0002
  - docs/history/05_EXCEPTION_QUEUE.md
  - history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v4.17.1-v4.28/EAODS-v4.20-alpha-enterprise-security-exceptions-and-risk-acceptance-standard.md
---

# EAODS Exception Management and Exception Register

## 1. Purpose

This document defines how EAODS raises, classifies, decides, time-bounds, reviews, and closes an exception, and how the resulting records are held in an exception register. An exception is an approved, recorded, time-bound deviation from an approved architecture, standard, policy, or control, together with the residual risk that deviation carries and the compensating controls that bound it.

It exists because a governed operating model must be able to say what it is not currently doing, and why, without that admission disappearing into a backlog. Any decision not to remediate a validated issue within the expected timeframe shall be documented, approved, time-bound, reviewed, and visible to executive stakeholders. The Enterprise Operating Model already names exception management as one of the mechanisms by which historical content is retained under control (EAODS-ARCH-EOM-001), and the Architecture Governance Model already reserves architectural deviation approval to a named board (EAODS-ARCH-GOV-001). This document supplies the lifecycle, record schema, and register those two statements assume.

## 2. Core principle

Risk may be accepted by accountable leadership. Risk may not be ignored, buried, or silently deferred.

Risk acceptance is a governance action, not a technical closure shortcut. A deviation that has not been through its approval authority is a defect, not an exception.

## 3. Scope and governing authority

This document governs exceptions arising from:

- vulnerability remediation deferrals;
- accepted security findings;
- penetration test findings not immediately remediated;
- compensating-control decisions;
- scan exceptions;
- cloud configuration exceptions;
- endpoint and server hardening exceptions;
- identity and access exceptions;
- AI-agent governance exceptions;
- publication risk exceptions;
- compliance-impacting exceptions;
- migration, provenance, and supersession gaps in the historical corpus.

EAODS v17.3 Volume 10 is the operational north star. ADR-0002 reserves material change to the four-pillar operating model for board review and Program Owner approval, which is why an exception that would in effect amend the operating model is not grantable at council level and escalates under Section 12. STD-0002 requires that every stated relationship between governed objects be a registered, validated edge, which is why an exception record names the artifact it deviates from rather than describing it in prose.

**Naming reconciliation.** The v4.20-alpha standard names the top approval authority for critical risk acceptance the Executive Governance Committee; the approved sibling documents name the same body the Enterprise Governance Board (EGB). These refer to one body, and this document uses Enterprise Governance Board throughout. Likewise, the v4.20-alpha roles of Asset Owner and Business Owner are read against the governance architecture as the accountable Domain Owner or Platform Owner for the asset in question. No new body and no new authority is created by this reconciliation.

## 3.1 Boundary with the risk register

This document and **EAODS-GOV-RISK-001 (Risk Management and Risk Register)** are
built from the same source and govern overlapping records. A control or standard
deviation is raised as an exception here; the residual risk it leaves is rated
and accepted under EAODS-GOV-RISK-001 §8. One event commonly produces one record
in each register, cross-referenced by identifier.

This document governs **exception lifecycle and closure**, including the four
closure branches of §11.2, which apply to risk-acceptance records as well.
EAODS-GOV-RISK-001 governs **risk rating and acceptance authority**. Neither
document overrides the other within the other's scope.

## 4. Prohibited uses

Exceptions shall not be used to:

- hide unresolved critical vulnerabilities;
- bypass executive review;
- avoid remediation due to convenience;
- suppress findings without evidence;
- mark untested fixes as complete;
- excuse unauthorized scanning;
- override legal or regulatory obligations;
- permanently accept risk without review.

An exception request that meets any of these descriptions is rejected at classification and does not enter the register.

## 5. Exception lifecycle

The lifecycle has six stages. Each stage has an entry condition, a named accountability, required evidence, and an exit condition; a request that cannot satisfy the exit condition of its stage is escalated under Section 12 rather than advanced or silently dropped.

| Stage | Entry condition | Accountability | Required evidence | Exit condition |
|---|---|---|---|---|
| Raise | A validated finding, or a deviation from an approved artifact, cannot be resolved on schedule | Requesting owner, with the accountable asset or artifact owner | Related finding and asset references; risk description; business and technical justification | A complete request exists with all Section 7 fields populated, status Requested |
| Classify | Request is complete | Security Reviewer for security exceptions; Document or Domain Owner otherwise | Exception type per Section 6; risk level; remediation feasibility review | Type and risk level assigned, determining the approval authority and the maximum review interval |
| Decide | Type and risk level assigned | Approval authority for that risk level, per Section 6 | Risk analysis (Section 8); validated compensating controls (Section 9); residual risk statement | Disposition recorded: approve, reject, or revise. Rejected and Needs Revision are terminal or returning states, not grants |
| Time-bound | Disposition is approve | Approval authority | Approval date; expiration date; review frequency; revocation conditions | Status Active, with an expiration date on or before the maximum interval for its risk level |
| Review | Scheduled review date, or a revocation condition fires | Implementation owner, reporting to the approval authority | Evidence that compensating controls remain implemented and effective; unchanged risk analysis inputs | Renew, revoke, or proceed to closure. A renewal restarts the time-bound stage and does not extend the original grant |
| Close | A closure branch in Section 11 is satisfied and evidenced | Accepting authority named in the closure record | Closure evidence package per Section 11 | Status Closed, with branch, authority, and date recorded. Any supersession clause is stated in the record |

The status model that carries these stages is: Requested → Under Review → (Rejected | Needs Revision) → Approved → Active → (Expired | Revoked | Renewed) → Closed. Expiry is not a closure branch. An expired exception automatically returns to open-risk status and the underlying risk is unaccepted from that moment.

## 6. Classification and decision authority

### 6.1 Exception types

| Type | Description |
|---|---|
| Remediation Deferral | Fix is delayed beyond normal SLA |
| Risk Acceptance | Business owner accepts residual risk |
| Compensating Control Exception | Alternative control reduces but does not eliminate risk |
| Scope Exception | Asset or system excluded from scan or assessment |
| Policy Exception | Temporary deviation from approved EAODS policy |
| Technical Constraint Exception | Remediation blocked by architecture, vendor, or compatibility issue |
| Business Continuity Exception | Temporary risk accepted to preserve critical operations |

### 6.2 Approval authority by risk level

| Risk level | Minimum approver |
|---|---|
| Low | Asset Owner |
| Medium | Business Owner and Security Reviewer |
| High | Executive Sponsor and Security Lead |
| Critical | Enterprise Governance Board |
| Regulated or legal impact | Enterprise Governance Board with Legal and Compliance review |

No one may approve risk acceptance for an asset, system, or business process they do not own or govern. Consultation does not transfer authority. Where an exception deviates from an approved architecture, standard, or pattern, the Enterprise Architecture Review Board is the approving authority for the architectural deviation itself, and the risk acceptance authority above applies to the residual risk it leaves behind.

## 7. Exception record schema

Every register entry carries the following fields. This section defines fields and their lifecycle position; it does not allocate or illustrate identifiers, which are minted only by the registering authority at the Raise stage.

| Field | Required | Set at |
|---|---|---|
| Exception identifier | Yes | Raise |
| Related finding reference | Yes | Raise |
| Asset or artifact reference | Yes | Raise |
| Asset or artifact owner | Yes | Raise |
| Exception type | Yes | Classify |
| Risk level | Yes | Classify |
| Risk description | Yes | Raise |
| Business justification | Yes | Raise |
| Technical justification | Yes | Raise |
| Residual risk statement | Yes | Decide |
| Compensating controls, each with implementation status and evidence reference | Yes | Decide |
| Approver and approving role | Yes | Decide |
| Approval date | Yes | Time-bound |
| Expiration date | Yes | Time-bound |
| Review frequency | Yes | Time-bound |
| Revocation conditions | Yes | Time-bound |
| Evidence references | Yes | Raise, extended at each review |
| Status | Yes | Maintained across all stages |

The historical migration register (EAODS-MIG-EXC-001) demonstrates the minimal operating projection of this schema for a register whose exceptions are documentary rather than technical: identifier, exception statement, owner, required resolution, and state, with the register itself carrying the default owner and the next review date in its front matter. The full schema and the minimal projection are the same record; the projection omits fields that do not apply rather than leaving them empty.

## 8. Required risk analysis

Each request shall evaluate technical severity, operational priority, affected asset criticality, exposure level, data classification, exploitability, known exploited status, business dependency, remediation complexity, available compensating controls, regulatory or contractual impact, and expected remediation timeline. Where vulnerability scoring applies, the analysis references the AI-assisted vulnerability prioritization scoring model that the v4.20-alpha standard extends (v4.17.2).

The analysis is an input to the Decide stage and is re-run at each Review stage. A renewal decided against a stale analysis is not a renewal; it is an unreviewed extension, and Section 12 escalation applies.

## 9. Compensating controls

Compensating controls shall be specific, implemented, testable, monitored, documented, mapped to the accepted risk, and reviewed before approval. Representative controls include network segmentation, web application firewall rules, endpoint detection controls, MFA enforcement, restricted access, additional logging, temporary service isolation, configuration guardrails, rate limiting, and manual monitoring.

Unimplemented future controls do not qualify as compensating controls. A planned control is part of the remediation plan, not part of the basis for approval. Compensating-control failure is both a revocation condition and a mandatory escalation trigger.

## 10. Expiry and renewal

Every exception shall have an expiration date, and shall be renewed, remediated, or revoked before it.

| Risk level | Maximum review interval |
|---|---|
| Low | 12 months |
| Medium | 6 months |
| High | 90 days |
| Critical | 30 days |
| Active exploitation context | Continuous executive review |

Renewal is a fresh decision by the same authority, on a re-run risk analysis and re-validated compensating controls, producing a new expiration date. A high-risk exception renewed more than once escalates. Expired exceptions automatically return to open-risk status, and the register shall show them as expired rather than removing them.

## 11. Closure and the four-branch closure rule

### 11.1 The worked precedent

The historical migration exception queue (EAODS-MIG-EXC-001) is the worked precedent for closure in EAODS. It ran eighteen exceptions — the full EXC-001 through EXC-018 range — to a closed state, under a single explicit closure rule, with an accountable owner and a date on every closure. Fifteen of the eighteen name a closure branch explicitly; **EXC-011, EXC-012, and EXC-013 close on verification-and-approval language that predates this standard**. They are recorded here as pre-rule closures, grandfathered rather than reopened; the branch rule in §11.2 applies prospectively. Owners across the queue were the Program Owner, the Architecture Owner, and the Repository Owner, with the Program Owner as the register default.

The queue closed an exception only when one of four conditions held:

1. the original is recovered and integrity-registered;
2. an evidence-bounded reconstruction is formally accepted;
3. the unit is formally superseded with owner, authority, and effective date; or
4. authoritative evidence establishes that the reference never became an artifact.

The corpus recovery registration (EAODS-HIST-CORPUS-001) shows branch 2 executed at scale: seventy conversation-derived transmissions were formally accepted by the Program Owner on 2026-07-30, closing EXC-001, EXC-002, EXC-003, EXC-015, EXC-016, and EXC-017. Its acceptance record is the model closure evidence package — accepting authority, acceptance date, scope, precondition, basis, and supersession — and its precondition was an independent completeness and contamination verification of all seventy units before acceptance was granted. Its supersession clause states that original file bytes supersede the accepted units if recovered, so a branch 2 closure remains reversible on new evidence without reopening the governance question.

Other closures in the queue exercised the other branches: originals recovered and integrity-registered (branch 1), a title conflict resolved by an approved supersession crosswalk row (branch 3), and a package whose release tag was confirmed never to have been created (branch 4).

### 11.2 The generalized enterprise rule

EAODS adopts the four branches as standing enterprise practice. An exception of any type closes only when one of the following is satisfied and evidenced, and the register records which:

| Branch | Standing formulation | Closure evidence required |
|---|---|---|
| Remediation | The deviation is removed and the remediated state is verified and registered | Remediation record; verification or retest result; integrity registration of the resulting state |
| Accepted substitute | An evidence-bounded substitute for the required state is formally accepted by the accountable authority | Accepting authority, acceptance date, scope, precondition satisfied, basis, and supersession clause |
| Supersession | The requirement deviated from is formally superseded | Supersession record naming owner, approving authority, and effective date; the superseded item is preserved, not deleted |
| Nullity | Authoritative evidence establishes that the premise of the exception never held | The evidence establishing non-existence or invalidity, and the authority accepting it |

Three properties travel with the rule. Closure is branch-labelled: a record that says "closed" without naming its branch is incomplete. Closure is authority-bound: the accepting authority is named in the record, at the level Section 6 requires for the risk. And branch 2 closure carries a supersession clause, so an acceptance made on the best available evidence is explicitly reversible if better evidence appears.

Expiry, revocation, and rejection are not closure branches. They return the underlying risk to open status and, where the risk persists, require a new request rather than a closure entry.

## 12. Mandatory escalation

Escalation follows the fixed path already established for governance: operational issue → Domain Owner → Governance Manager → Architecture, AI, or Risk Council → Enterprise Governance Board → Executive Leadership.

Escalation is mandatory when a critical finding is proposed for acceptance; a high-risk exception is renewed more than once; compensating controls fail; active exploitation emerges; the asset becomes internet-facing; the asset begins handling more sensitive data; ownership changes; remediation is delayed beyond the accepted expiration date; exception evidence is incomplete; or the exception conflicts with regulatory obligations.

An exception whose residual risk exceeds approved enterprise tolerance is not granted at council level; it escalates on this path with its rationale, risk analysis, and the unresolved point stated.

## 13. Register operation, reporting, and retention

The exception register is the authoritative list of every exception in any state. It carries a document owner, a default owner for entries that do not name one, and a next review date, and it retains closed entries with their closure branch, authority, date, and any supersession clause intact.

Executive Control Tower reporting shall display active exceptions, exceptions by risk level, exceptions nearing expiration, expired exceptions, repeated renewals, accepted critical risks, exception owners, compensating-control failures, and business units carrying residual risk. Accepted risk shall be visible, not buried.

Knowledge Memory shall retain exception history, accepted-risk rationale, compensating-control evidence, renewal decisions, remediation outcomes, recurring exception patterns, and asset-level residual-risk history, so that repeated risk acceptance patterns and weak remediation discipline become detectable rather than anecdotal.

The Artifact Factory may generate the risk acceptance memo, exception request form, compensating-control validation checklist, executive residual-risk summary, renewal review packet, expired exception report, remediation deferral justification, and board-level risk register extract from these records.

## 14. Human review gate

Approval of this document requires confirmation by the Enterprise Governance Board and the Program Owner that:

- no governance body, approval authority, risk level, review interval, or escalation trigger has been introduced beyond those in the cited sources, and the Section 3 naming reconciliation creates no new body;
- the core principle is stated without weakening: risk may be accepted by accountable leadership, and may not be ignored, buried, or silently deferred;
- every grant is time-bound, and expiry returns the underlying risk to open status rather than closing it;
- compensating controls are implemented before approval, never planned;
- the four-branch closure rule is applied as generalized in Section 11.2, with branch, authority, date, and any supersession clause recorded;
- closed entries are preserved in the register rather than removed.

Because this document defines approval authority, exception eligibility, expiration rules, compensating-control requirements, escalation conditions, and executive reporting, its adoption additionally passes security governance review, risk management review, and legal or compliance review where applicable, before adoption.

## 15. Sources and traceability

| Source (repo-relative path) | Contribution |
|---|---|
| history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v4.17.1-v4.28/EAODS-v4.20-alpha-enterprise-security-exceptions-and-risk-acceptance-standard.md (v4.20-alpha, draft transmission) | Purpose statement and the documented-approved-time-bound-reviewed-visible requirement (Section 1); core principle and the governance-action-not-shortcut formulation (Section 2); scope list (Section 3); prohibited uses (Section 4); risk acceptance workflow and exception status model underlying the six-stage lifecycle (Section 5); exception type table and risk acceptance authority matrix (Section 6); exception record requirements and request template fields (Section 7); required risk analysis factors and the v4.17.2 scoring reference (Section 8); compensating-control requirements, examples, and the unimplemented-controls exclusion (Section 9); expiration and maximum review interval table, renewal-or-remediate-or-revoke rule, and expired-returns-to-open-risk rule (Sections 5, 10); mandatory escalation conditions (Section 12); Executive Control Tower display set, Knowledge Memory retention set, and Artifact Factory output set (Section 13); human review gate scope (Section 14) |
| docs/history/05_EXCEPTION_QUEUE.md (EAODS-MIG-EXC-001) | The worked precedent: eighteen exceptions EXC-001 through EXC-018 run to closed state (Section 11.1); the four-branch closure rule generalized in Section 11.2; branch-labelled closure statements naming owner and date; owner roles exercised across the queue and the register default owner (Section 11.1); minimal register projection of the record schema — identifier, exception, owner, required resolution, state — plus register-level default owner and next review date (Sections 7, 13); branch 1, branch 3, and branch 4 closures cited in Section 11.1; the supersede-if-recovered clause attached to accepted reconstructions (Section 11) |
| docs/history/16_COMPLETE_CORPUS_RECOVERY_REGISTRATION.md (EAODS-HIST-CORPUS-001) | Branch 2 executed at scale: seventy transmissions formally accepted by the Program Owner on 2026-07-30, closing EXC-001, EXC-002, EXC-003, EXC-015, EXC-016, EXC-017 (Section 11.1); the acceptance record fields — accepting authority, acceptance date, scope, precondition, basis, supersession — adopted as the branch 2 closure evidence package (Sections 11.1, 11.2); independent completeness and contamination verification as a precondition of acceptance (Section 11.1); original bytes supersede if recovered, as the reversibility property of acceptance closure (Section 11.2) |
| docs/architecture/architecture-governance-model.md (EAODS-ARCH-GOV-001) | House style — front matter fields, numbered sections, naming-reconciliation paragraph, staged lifecycle table, human review gate and sources-and-traceability formatting; exception defined as an approved, recorded, time-bound deviation and the deviation-without-board-review-is-a-defect formulation (Sections 1, 2); EARB authority over architectural deviations and exceptions (Section 6.2); residual risk, risk acceptance oversight, and the not-granted-at-council-level rule (Section 12); fixed escalation path and escalate-rather-than-reject-silently rule (Sections 5, 12); decision record fields including implementation owner and review date (Section 7); preservation of superseded records (Section 11.2) |
| docs/architecture/ENTERPRISE_OPERATING_MODEL.md (EAODS-ARCH-EOM-001) | Exception management as a named mechanism of controlled historical lineage, alongside provenance, checksums, and supersession records (Sections 1, 11); Volume 10 as operational north star and named owners for governed artifacts (Section 3) |
| architecture/adr/ADR-0002-eaods-enterprise-reference-operating-model.md | Reservation of material operating-model change to board review plus Program Owner approval, applied as the limit on what an exception may grant (Section 3) |
| docs/standards/cross-artifact-traceability.md (STD-0002) | Requirement that stated relationships between governed objects be registered, validated edges, applied to the artifact reference field of the exception record (Sections 3, 7) |
