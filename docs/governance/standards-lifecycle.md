---
title: EAODS Standards Lifecycle and Document Governance
document_id: EAODS-GOV-STD-001
version: 1.0.0
status: approved
owner: Engineering Governance
review_gate: Enterprise Governance Board and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - EAODS-ARCH-EOM-001
  - EAODS-ARCH-GOV-001
  - STD-0001
  - STD-0002
  - ADR-0001
  - ADR-0002
  - docs/standards/canonical-terminology-and-identifiers.md
  - docs/architecture/architecture-governance-model.md
  - standards/vocabulary/object-identifiers.yaml
  - standards/vocabulary/canonical-terms.yaml
  - CONTRIBUTING.md
---

# EAODS Standards Lifecycle and Document Governance

## 1. Purpose

This standard establishes the governance framework for creating, reviewing, approving, publishing, maintaining, superseding, archiving, and retiring every EAODS policy, standard, framework, architecture document, procedure, playbook, runbook, implementation guide, and technical work instruction. It exists so that every governance artifact remains authoritative, traceable, version-controlled, auditable, and continuously maintained across its whole life, rather than authoritative only on the day it is written.

It complements rather than duplicates STD-0001. STD-0001 governs *what an object is called and how it is identified*; this standard governs *how the document that defines the object moves from draft to retirement, and who approves each move*. An artifact that satisfies one and not the other is not publishable.

## 2. Scope and governing authority

This standard applies to every governance artifact in this repository and to the registers that track them. Authority is layered: EAODS v17.3 Volume 10 is the operational north star; the Enterprise Reference Operating Model (EAODS-ARCH-EOM-001) establishes that governance precedes automation and that every major artifact has a named owner; the Architecture Governance Model (EAODS-ARCH-GOV-001) supplies the governance bodies, decision authorities, escalation path, and cadences that this document applies to documentation work; STD-0001 supplies the identifier and terminology rules that gate publication; CONTRIBUTING.md supplies the mechanics by which a change reaches the repository.

**Naming reconciliation.** The v4.25 lifecycle standard names the minimum approval authority for a standard the "Security Governance Board" and for a framework the "Enterprise Architecture Board", and names the architecture approver "Chief Architect or Delegate". EAODS-ARCH-GOV-001 records the enterprise authority that approves new governance standards as the **Enterprise Governance Board (EGB)**, the architecture authority as the **Enterprise Architecture Review Board (EARB)**, and assigns architecture governance accountability to the **Enterprise Architect** seat. This document uses the EAODS-ARCH-GOV-001 names throughout. The reconciliation creates no new body and transfers no authority.

## 3. Documentation governance principles

Enterprise documentation shall be authoritative; version controlled; evidence based; reviewed regularly; approved through defined authority; traceable; reproducible; protected from unauthorized modification; and continuously improved.

## 4. Documentation hierarchy and artifact classification

Authority descends through the documentation hierarchy. A lower tier may implement a higher tier; it may not contradict it.

Enterprise Governance Charter → Enterprise Policies → Enterprise Standards → Enterprise Frameworks → Architecture Documents → Operational Procedures → Playbooks → Runbooks → Implementation Guides → Technical Work Instructions.

Every artifact declares exactly one classification.

| Classification | Purpose |
|---|---|
| Policy | Executive governance requirement |
| Standard | Mandatory implementation requirement |
| Framework | Organizational operating model |
| Architecture | Technical design guidance |
| Procedure | Required operational process |
| Playbook | Response workflow |
| Runbook | Step-by-step operational execution |
| Guideline | Recommended practice |
| Reference | Informational material |

Under STD-0001, enterprise standards are located in `docs/standards/` under the `STD` prefix and architecture decision records in `architecture/adr/` under the `ADR` prefix. The `THR`, `RUN`, and `PAT` prefixes were originally reserved pending establishment of their libraries. Those libraries are established — `docs/threat-models/`, `docs/runbooks/`, and `docs/patterns/` are populated — and all three prefixes are registered in `standards/vocabulary/object-identifiers.yaml` with an owning authority and a `defined_in` location. STD-0001 records this state directly, so artifacts of those classifications mint identifiers under this lifecycle in the ordinary way, with no divergence to reconcile.

## 5. Required document metadata

Two front-matter schemas are in force, and an artifact must use the one its
location requires. `scripts/validate_front_matter.py` enforces the framework
schema in CI over `docs/frameworks/` and `frameworks/`; documents elsewhere use
the governance schema. Authoring against the wrong one fails the build.

**Framework volumes** (`docs/frameworks/**`) — the nine keys CI requires, exactly:
`title`, `version`, `owner`, `suite`, `status`, `classification`, `purpose`,
`architecture_domain`, `review_cycle`.

**Governance-tier documents** (this document, and everything under
`docs/governance/`, `docs/security/`, `docs/architecture/`, `docs/operations/`,
`docs/standards/`) — the eight keys the approved set uses: `title`,
`document_id`, `version`, `status`, `owner`, `review_gate`,
`governing_architecture`, `related`.

`docs/standards/documentation-standards.md` is authoritative for both schemas.
The requirements below are the governance-level obligations each schema realizes;
where a requirement names a key, it names the key of the schema in force.

| Required field | Realization in this repository |
|---|---|
| Title | `title` |
| Version | `version`, under the semantics in Section 7 |
| Status | `status`, from the model in Section 6.1 |
| Owner | `owner` — a named accountable owner, never a queue |
| Domain | `governing_architecture`, naming the governing volume |
| Control Domain | Stated in the body where the artifact governs controls |
| Classification | The tier declared under Section 4 |
| Review Cycle | Section 8, stated in the body where it differs from the default |
| Effective Date | Date of approval, recorded in the approval record (Section 13) |
| Supersedes | `supersedes` on the record, plus the supersession record in Section 10 |
| Related Artifacts | `related`, citing registered identifiers and repository paths |
| Approval Authority | `review_gate` |
| Change History | Change records under Section 10, retained in version control |
| Human Review Gate | The closing numbered section of the artifact |

Approved documents additionally carry a `document_id` front-matter label. These labels are document-level names; they are not object identifiers under STD-0001, whose registered format is `^[A-Z][A-Z0-9-]*-[0-9]{4,6}$`. A `document_id` is therefore not a substitute for registering the objects a document defines. Whether document-level labels are brought under the identifier registry is a decision reserved to the Enterprise Governance Board; this standard does not decide it.

## 6. Lifecycle

### 6.1 Status model

| Status | Description |
|---|---|
| Proposed | Authored and published for review; the pre-review state used across the current baseline. Equivalent to Draft for the purposes of Section 6.2 gating. |
| Draft | Under development |
| Architecture Review | Technical review underway |
| Governance Review | Governance validation |
| Legal Review | Regulatory or legal assessment |
| Executive Approval | Pending executive authorization |
| Approved | Official enterprise standard |
| Active | Published and enforceable |
| Deprecated | Scheduled for retirement |
| Archived | Historical reference only |

### 6.2 Stages

The enterprise document lifecycle runs from business need through draft, technical review, governance review, legal review where applicable, executive approval, publication, operational use, and periodic review, to revision or retirement. The seven governed stages below are that sequence expressed as entry and exit conditions.

| Stage | Status values | Authority | Required evidence | Exit condition |
|---|---|---|---|---|
| Draft | Draft | Author, with the accountable owner named in `owner` | Business need or governance requirement recorded; classification declared; all Section 5 metadata present | A complete draft exists with no empty required metadata field |
| Review | Architecture Review; Governance Review; Legal Review where applicable | EARB for technical review; Engineering Governance for governance validation; Legal and Compliance where regulatory obligations are touched | Quality gates in Section 12; reviewer comments; affected standards; implementation impact; rollback considerations | Every applicable review recorded with an explicit disposition |
| Approve | Executive Approval, then Approved | The authority for the classification (Section 9), plus Program Owner approval where the operating model, canonical terminology, metadata structure, or cross-volume architecture is affected | Approval records; named approval authority; effective date | Status set to Approved with an effective date and a named approver |
| Publish | Active | Document owner, executing the contribution workflow | Publication readiness confirmed; YAML front matter preserved; documentation validation passed; no secrets; business and architecture impact and affected volumes explained in the pull request | Artifact is Active in the repository and entered in the standards catalog |
| Maintain | Active | Named owner | Periodic review record; a change record for every revision; cross-reference validation re-run | Review completed on cycle, with a decision to reaffirm, revise, supersede, or retire |
| Supersede | Superseding artifact Active; superseded artifact Deprecated, then Archived | The same authority that would approve the superseding artifact | Supersession record (Section 10); change impact assessment; dependency review | Both artifacts carry the supersession link, and the earlier artifact is preserved rather than deleted |
| Retire | Deprecated, then Archived | The approval authority for the classification | Retirement rationale; disposition of dependent artifacts; confirmation that no active artifact depends on the retired provisions | Artifact is Archived as historical reference only, and its identifier is retained with a retired status |

An artifact reaches Active only from Approved, and reaches Approved only through the reviews its classification requires. Publication and approval are distinct: the v1.0.0 baseline publishes its authored set at `status: proposed` with the board review gates open and disclosed (see `docs/governance/release-readiness-v1.0.0.md` §6). Publishing under review is permitted and recorded; representing a `proposed` artifact as Approved is not.

## 7. Version semantics

| Increment | Meaning | Gate consequence |
|---|---|---|
| Major (X.0) | Architectural or governance change | Full review path for the classification, including Program Owner approval where the operating model, terminology, or metadata structure is affected |
| Minor (X.Y) | New capabilities or substantive additions | Technical and governance review for the classification |
| Patch (X.Y.Z) | Editorial corrections or clarifications | Document owner review, provided no normative provision changes |

Maturity qualifiers apply to the release, not to the increment: **Alpha** denotes internal drafting, **Beta** review-ready, **Release Candidate** final validation, and **General Availability** an approved enterprise release. Historical EAODS units carry alpha versions and are held as provenance, not as current authority.

Two coupling rules apply. First, a change that alters a definition in the canonical terms registry requires Engineering Governance review and a registry version increment under STD-0001, independent of the document version. Second, an editorial patch that would change a normative provision is not an editorial patch; it is reclassified to the increment its content requires, and takes that increment's gate.

## 8. Review cycles and maintenance

The default review cycle is **annual at minimum, with a quarterly operational review**. This aligns with the governance cadence recorded in EAODS-ARCH-GOV-001, where the governance operating model is reviewed annually with a quarterly governance assessment between annual reviews, and where the EARB meets biweekly and the Enterprise Governance Board quarterly.

An artifact whose review date passes without a recorded review remains Active but is reported as overdue (Section 15). Maintenance is not optional upkeep: an artifact that cannot demonstrate a review within its cycle cannot be relied upon as evidence.

The sources read for this standard, listed in Section 17, do not fix a retention period for archived artifacts or a numeric turnaround time for any individual review stage; both remain to be set by the Enterprise Governance Board.

## 9. Ownership and approval authority

Every artifact carries exactly one approval authority for its classification. Consultation does not transfer authority.

| Artifact type | Minimum approval authority | Reconciled body (Section 2) |
|---|---|---|
| Policy | Executive Leadership | Executive Leadership |
| Standard | Security Governance Board | Enterprise Governance Board |
| Framework | Enterprise Architecture Board | Enterprise Architecture Review Board |
| Architecture | Chief Architect or Delegate | Enterprise Architect, or a named delegate |
| Procedure | Domain Owner | Domain Owner |
| Playbook | SOC / Operations Manager | Operations Manager |
| Runbook | Technical Service Owner | Technical Service Owner |

Standards lifecycle responsibility is contributed to the EARB by the Security Governance Manager seat, and the `STD` prefix is registered to Engineering Governance, which owns this standard. Every EAODS standard and major artifact shall identify its governing authority, accountable owner, approval workflow, review cadence, and escalation path; an artifact that names no governing authority and no accountable owner is not eligible for acceptance. Where a review gate cannot be satisfied, the contribution is escalated with its rationale, impact analysis, and the unresolved point stated, rather than rejected silently.

## 10. Change management, supersession, and retirement

Every revision shall record: reason for change; originating request; affected standards; implementation impact; rollback considerations; reviewer comments; approval records; and publication date.

A supersession is recorded as its own governance record. The record carries the following fields; no example identifiers are minted here, because identifiers are assigned only through the registries named in Section 11.

| Supersession record field | Content |
|---|---|
| Superseded artifact | Identifier and title of the artifact being replaced |
| Superseding artifact | Identifier and title of the replacement |
| Effective date | Date the replacement becomes enforceable |
| Reason | Why replacement rather than revision was required |
| Approval reference | Authority, decision record, and approval date |
| Impact assessment | Affected standards, controls, procedures, and dependent artifacts |
| Disposition | Status applied to the superseded artifact and where it is retained |
| Migration notes | Actions required of downstream owners, with the accountable owner named |

Superseded and retired artifacts are preserved, not deleted. Historical content is retained through controlled migration, provenance, checksums, supersession records, and exception management, and current approved repository artifacts and decision records take precedence over historical drafts. Retirement moves an artifact from Deprecated to Archived, where it is historical reference only; it does not release the artifact's identifier, which is retained with a retired status under STD-0001.

## 11. Relationship to STD-0001 registration rules

STD-0001 is a precondition of publication, not a parallel concern. Its registries — `standards/vocabulary/object-identifiers.yaml` for identifier prefixes and `standards/vocabulary/canonical-terms.yaml` for canonical terms — are the source of truth, and prose in any artifact that conflicts with a registry entry is a defect in the artifact.

The following STD-0001 rules bind specific stages of this lifecycle:

1. **Registration before use.** A prefix must exist in the identifier registry before any artifact mints an identifier with it. A draft that mints an unregistered identifier does not exit the Review stage.
2. **Registration before normative use.** A term used normatively must exist in the canonical terms registry. A pull request introducing an unregistered identifier prefix or an unregistered normative term shall not pass review.
3. **Format and fixed width.** Identifiers match `^[A-Z][A-Z0-9-]*-[0-9]{4,6}$`, with the zero-padding width fixed when the prefix is registered and new prefixes using six digits — for example the registered control identifier EAODS-CTRL-000184 at six digits and the platform service identifier SVC-00387 at five.
4. **One object, one identifier.** An object carries the same identifier across every volume, diagram, and record that references it, so a superseding document inherits the object's identifier rather than reissuing it.
5. **Stability across retirement.** Published identifiers are never reused, renumbered, or reassigned, and retired objects keep their identifier with a retired status. Retirement under Section 6.2 therefore never frees an identifier for reuse.
6. **No silent redefinition.** Changing a definition requires Engineering Governance review and a registry version increment, which is why Section 7 couples definitional change to the registry rather than to the document version alone.

Changes to STD-0001 or to either registry require review by the Enterprise Architecture Review Board and final approval by the program owner, per GOVERNANCE.md and ADR-0002 as recorded in STD-0001 itself. Artifacts already governed by these rules include ADR-0001, ADR-0002, STD-0001, and STD-0002.

## 12. Quality gates and publication readiness

Before publication, every artifact shall pass: structural validation; metadata validation; terminology review; technical review; governance review; cross-reference validation; formatting verification; and QA checklist completion.

The contribution mechanics that carry an artifact through those gates are fixed by CONTRIBUTING.md: short-lived branches named `docs/<topic>`, `feature/<capability>`, `fix/<issue>`, or `chore/<maintenance>`; pull requests that explain business and architecture impact, identify affected EAODS volumes, pass documentation validation, preserve YAML front matter, and avoid secrets; and Conventional Commits.

## 13. Lifecycle registers and records

Lifecycle state is tracked in registers generated from the governance record, not reconstructed by reading documents. The register set comprises the Governance Charter, Policy Register, Standards Catalog, Architecture Register, Document Review Package, Executive Approval Package, Change Impact Assessment, Publication Readiness Report, and Annual Governance Review Report.

Each Standards Catalog entry carries the fields below. The catalog assigns no identifiers of its own; it records the identifier the artifact already holds under STD-0001.

| Catalog field | Content |
|---|---|
| Identifier | The artifact's registered identifier, where the artifact defines a registered object |
| Title and classification | Name and Section 4 tier |
| Version and status | Current version and Section 6.1 status |
| Owner and approval authority | Named accountable owner and the authority that approved the current version |
| Effective date | Date the current version became enforceable |
| Review cycle and next review date | Cycle applied under Section 8 and the date the next review falls due |
| Supersedes and superseded by | Links in both directions, where they exist |
| Related artifacts | Parent policies, dependent standards, related controls, procedures, evidence requirements, exception records, metrics, risk register entries, and implementation artifacts |
| Change history reference | Pointer to the change and approval records for the artifact |

Those relationship fields are the traceability requirement stated directly: each artifact shall maintain references to its parent policies, dependent standards, related controls, operational procedures, evidence requirements, exception records, metrics, risk register entries, and implementation artifacts.

## 14. AI-assisted documentation governance

AI may assist with drafting standards, identifying duplicate content, consistency checking, cross-reference validation, terminology normalization, executive summary generation, and change impact analysis.

AI shall not independently approve governance documents or replace designated human approval authorities. This is the documentation expression of the enterprise AI operating boundaries: AI assistance is least privileged, observable, auditable, bounded by policy, subject to human approval for material actions, and traceable to owners, controls, and evidence. An AI-assisted draft enters the lifecycle at Draft and passes every gate that a human-authored draft passes.

## 15. Executive reporting and knowledge retention

Executive reporting on documentation health presents active governance documents, upcoming review deadlines, overdue reviews, document ownership, approval status, superseded artifacts, policy compliance mapping, documentation maturity, and publication trends.

Knowledge Memory preserves historical versions, approval decisions, review comments, publication history, supersession lineage, recurring revision themes, governance lessons learned, and document dependency relationships. Retention is what makes supersession safe: the replaced artifact stays legible after the replacement takes authority.

## 16. Human review gate

Changes affecting document hierarchy, lifecycle governance, approval authority, versioning policy, publication controls, metadata requirements, AI-assisted documentation governance, or traceability requirements shall undergo review by Enterprise Architecture, Security Governance, Internal Audit, Records Management, and Executive Leadership prior to approval and publication.

Approval of this standard requires confirmation by the Enterprise Governance Board and the Program Owner that:

- no governance body, approval authority, cadence, or lifecycle status has been introduced beyond those in the cited sources;
- the naming reconciliation in Section 2 creates no new body and transfers no authority;
- the STD-0001 registration rules in Section 11 are restated without weakening, and no identifier is minted by this document;
- superseded and retired artifacts are preserved with their identifiers retained under a retired status;
- AI assistance remains excluded from approval authority.

Because this standard defines metadata requirements and lifecycle governance, Program Owner approval applies in addition to Enterprise Governance Board approval.

## 17. Approval

Approved by the Program Owner on 2026-08-03, closing the Human governance
review gate of epic #26.

| Field | Value |
|---|---|
| Approving authority | Program Owner (Ivan Rozenblad) |
| Approval date | 2026-08-03 |
| Gate closed | Epic #26 — Human governance review |
| Basis | Independent four-lens defect review (34 candidates, 8 confirmed and fixed in PR #65) preceding sign-off |
| Status effect | `proposed` → `approved`; this document is enforceable governance |

Subsequent material change re-enters the lifecycle at Section 6 and requires
re-approval; it does not inherit this one.

## 18. Sources and traceability

| Source (repo-relative path) | Contribution |
|---|---|
| history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v4.17.1-v4.28/EAODS-v4.25-alpha-enterprise-cybersecurity-policy-governance-and-document-lifecycle-standard.md (v4.25-alpha, conversation-derived evidence) | Purpose and lifecycle coverage (Section 1); documentation governance principles (Section 3); documentation hierarchy and artifact classification table (Section 4); required metadata fields (Section 5); document status model and enterprise lifecycle sequence (Section 6); versioning policy and maturity qualifiers (Section 7); annual-minimum-with-quarterly-operational review cycle (Section 8); approval matrix (Section 9); change management fields and supersession lineage (Section 10); document quality gates (Section 12); Artifact Factory register set and traceability requirements (Section 13); AI-assisted documentation governance boundaries (Section 14); Executive Control Tower and Knowledge Memory items (Section 15); human review gate roles and triggers (Section 16) |
| docs/standards/canonical-terminology-and-identifiers.md (STD-0001) | Identifier format, registration-before-use, stability, one-object-one-identifier, and fixed-width rules; terminology registration and no-silent-redefinition rules; registry locations as source of truth; the review outcome for unregistered prefixes and terms; registered locations of `STD` and `ADR` artifacts, and the prefix-table reservation of `THR`, `RUN`, and `PAT`, quoted in Section 4 as written and reconciled there against the current registry (Sections 2, 4, 5, 7, 10, 11); the ADR-0002 and GOVERNANCE.md pointer for registry change approval (Section 11) |
| `standards/vocabulary/object-identifiers.yaml` | Current registration state of the `THR`, `RUN`, and `PAT` prefixes — owning authority and `defined_in` location for each — establishing that the three libraries are no longer forthcoming (Section 4); registry as source of truth for prefixes (Section 11) |
| CONTRIBUTING.md | Branch naming, pull-request content requirements, documentation validation, YAML front-matter preservation, secret avoidance, and Conventional Commits as the publication mechanics (Sections 6.2, 12) |
| docs/architecture/architecture-governance-model.md (EAODS-ARCH-GOV-001) | House style — front matter, numbered sections, naming-reconciliation pattern, stage tables, and sources-and-traceability formatting; governance body names used in the reconciliation and the approval matrix (Sections 2, 9); Enterprise Governance Board authority over new governance standards (Section 9); Security Governance Manager seat contributing standards lifecycle responsibility (Section 9); ADR-0002 Program Owner overlay for operating-model, terminology, and metadata change (Sections 6.2, 7, 16); governance cadences (Section 8); requirement that every artifact name governing authority, owner, workflow, cadence, and escalation path, and the escalate-rather-than-reject rule (Section 9); preservation of superseded records (Section 10) |
| docs/architecture/ENTERPRISE_OPERATING_MODEL.md (EAODS-ARCH-EOM-001) | House style and tone; governance-precedes-automation and named-owner principles (Sections 1, 2); Volume 10 as operational north star (Section 2); historical lineage through controlled migration, provenance, checksums, supersession records, and exception management, and precedence of current approved artifacts (Sections 7, 10); AI operating boundaries applied to documentation assistance (Section 14) |
