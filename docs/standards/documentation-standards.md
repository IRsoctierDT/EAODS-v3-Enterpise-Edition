---
title: EAODS Documentation Standards and Style Guide
document_id: EAODS-DOC-STD-001
version: 1.0.0
status: proposed
owner: Engineering Governance
review_gate: Engineering Governance and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - EAODS-ARCH-EOM-001
  - EAODS-ARCH-PRIN-001
  - STD-0001
  - STD-0002
  - ADR-0002
  - CONTRIBUTING.md
  - scripts/validate_front_matter.py
  - docs/frameworks/EAODS-v17.3/volume-08-security-engineering.md
---

# EAODS Documentation Standards and Style Guide

## 1. Purpose and scope

This guide states how EAODS documents are authored so that they are consistent to read, mechanically validatable, and traceable to their governing authority. It covers required metadata, section structure, prose conventions, tables and diagrams, identifier and terminology usage, and the sources-and-traceability obligation.

Scope: all Markdown artifacts under `docs/` and `architecture/`, which are the trees scanned by the traceability validator (`scripts/validate_traceability.py`).

This guide is subordinate to the standards it applies. STD-0001 governs identifiers and canonical terminology; STD-0002 governs relationship metadata and CI enforcement; `CONTRIBUTING.md` governs branch, commit, and pull-request mechanics. Where this guide and one of those sources appear to diverge, the source governs and this guide is the defect.

## 2. Document classes and the applicable metadata schema

Two YAML front-matter schemas are in use. Which one applies is determined by where the document lives, because that is what the validators key on.

| Document class | Location | Front-matter schema | Enforced by |
|---|---|---|---|
| Framework volume | `docs/frameworks/**`, `frameworks/**` | Nine-field framework schema (Section 3) | `scripts/validate_front_matter.py` |
| Governance and architecture document | `docs/architecture/`, `docs/standards/`, and comparable governance trees | Eight-field governance schema (Section 4) | Human review gate |

A document may carry fields beyond its schema's required set; neither schema is closed. Volume 8 of EAODS v17.3, for example, adds `extends` and `constitutional_authority` alongside the nine required framework fields.

Two of the documents read for this guide — `docs/standards/canonical-terminology-and-identifiers.md` (STD-0001) and `docs/standards/cross-artifact-traceability.md` (STD-0002) — carry no YAML front matter at all and open directly with an H1 that states the identifier and title. That pattern is preserved for those existing standards; new governance-tier documents use the eight-field schema in Section 4.

## 3. Framework front-matter schema (nine required fields)

`scripts/validate_front_matter.py` walks `docs/frameworks` and `frameworks` recursively, and for every `.md` file it requires the following nine keys. A missing key, a file that does not begin with a `---` fence, or front matter that does not parse as a YAML mapping is a build failure reported per file.

| Field | Purpose | Example value (Volume 8) |
|---|---|---|
| `title` | Full volume title as it appears in the H1 | EAODS v17.3 — Volume 8: Enterprise Security Engineering, Cryptographic Services & Platform Protection Architecture |
| `version` | Volume version string | 17.3.7-alpha |
| `owner` | Accountable owner of the volume | Ivan Rozenblad |
| `suite` | Parent documentation suite | Enterprise AI Operator Documentation Suite (EAODS) v3 |
| `status` | Publication or maturity state | Enterprise Platform Engineering Guide |
| `classification` | Handling classification | Internal / Portfolio / Commercialization Candidate |
| `purpose` | One-line statement of what the volume defines | Canonical Security Engineering Architecture for Enterprise Platform Protection |
| `architecture_domain` | Domain the volume governs | Security Engineering & Cryptographic Infrastructure |
| `review_cycle` | Cadence and forums for scheduled review | Monthly Security Engineering Review, Quarterly Cryptographic Governance Assessment, Annual Enterprise Platform Security Certification |

Authoring rules for this schema:

- values are quoted strings; multi-valued fields such as `extends` are YAML sequences;
- `title` and the document H1 state the same thing, so a reader arriving from search and a reader arriving from the navigation see one title;
- the validator checks presence, not content, so the review gate is what confirms `owner`, `classification`, and `review_cycle` are truthful.

## 4. Governance front-matter schema (eight fields)

Governance-tier documents — the operating model, the principles catalog, and this guide — use the eight-field schema. It exists to give each document a stable identity, a named owner, an explicit approval gate, and declared relationships.

| Field | Purpose | Example value |
|---|---|---|
| `title` | Document title, restated as the H1 | EAODS Enterprise Operating Model |
| `document_id` | Stable document identity | EAODS-ARCH-EOM-001 |
| `version` | Semantic version of the document | 1.0.0 |
| `status` | Lifecycle state | proposed |
| `owner` | Accountable owner | Enterprise Architecture Owner |
| `review_gate` | The bodies whose approval the document requires | Enterprise Architecture Board and Program Owner approval |
| `governing_architecture` | The authority the document is subordinate to | EAODS v17.3 Volume 10 |
| `related` | Identifiers and repo-relative paths of connected artifacts | ADR-0002, STD-0001, STD-0002 |

Authoring rules for this schema:

- `related` entries are either registered identifiers or repo-relative paths; each entry names something that exists in the repository;
- `status` moves from proposed to approved only through the gate named in `review_gate`, per the decision and accountability model in the Enterprise Operating Model;
- `governing_architecture` is the document's link into the traceability chain and is never left implicit.

## 5. Structure, headings, and numbering

- **One H1 per document**, stating the title verbatim. Nothing precedes it except front matter.
- **Governance-tier documents number their `##` sections** — `## 1. Purpose`, `## 2. …` — in sentence case, as the operating model and the principles catalog do. Numbering makes cross-references stable ("Section 7") without minting identifiers.
- **Framework volumes and the existing STD documents use unnumbered `##` sections** in a fixed sequence. Volume 8 runs Purpose, Architecture, Enterprise workflow, Integration points, QA checklist, Human review gate; STD-0001 and STD-0002 run Purpose, Scope, authoritative sources, rules, workflow or validation, Integration points, QA checklist, Human review gate.
- **Heading levels are not skipped.** `###` appears only inside a `##` section, as in the four-pillar breakdown of the operating model.
- **Closing sections are mandatory.** Every document ends with a human review gate. Governance-tier documents then close with the sources-and-traceability table required by Section 9, which is the final section of the document.
- **QA checklists** are checkbox lists of verifiable conditions, one per line, phrased so that a reviewer can mark each true or false without interpretation.

## 6. Voice, tense, and normative language

- **Present tense for standing facts.** State what the architecture is, not what it will be: Volume 10 serves as the operational north star.
- **Past tense only for lineage.** Supersession, migration, and provenance statements are the legitimate use of past tense.
- **Third person throughout.** No first person, singular or plural. Obligations attach to a named actor — a role, a body, or an owner — never to an unnamed "we".
- **Normative verbs carry weight.** Use *must* or *shall* for obligations, *requires* for gate conditions, and plain indicative for description. Avoid *should* where an obligation is intended; the enforced rules of STD-0002 and the review sentence of STD-0001 are the models to follow.
- **Active voice for anything auditable.** Passive constructions hide the accountable party, which conflicts with the named-ownership principle.
- **Sentences are declarative and unadorned.** Superlatives, promotional phrasing, and unattributed quantities do not appear. A number appears only when a cited source states it.
- **Terminology is canonical, not stylistic.** Use the canonical term from the terms registry rather than a synonym chosen for variety; see Section 8.
- **Worked examples are labelled as illustrative.** A scenario used to explain a rule is introduced as an illustrative scenario drawn from the framework's own material. It is never presented as a deployment at a named organization, because the evidence-precedes-assertion principle forbids asserting an outcome the repository cannot evidence.

## 7. Tables and diagrams

Tables are the default structure for any enumerable set whose members share attributes: registries, registered prefixes, principle catalogs, edge types, field schemas, and mapping matrices.

- every table has a header row, and the first column carries the key — an identifier, a prefix, a field name, or a short label;
- cells are short phrases without terminal punctuation;
- columns are parallel in kind down the whole table, so a reader can scan one column alone.

Diagrams are optional and are authored as fenced `mermaid` blocks, `flowchart TD` for sequences and hierarchies and `flowchart LR` for chains, as used in the contribution workflow of STD-0001, the realized traceability chain of STD-0002, and the architecture and workflow diagrams of Volume 8. Node labels are short noun phrases.

A diagram never carries a normative statement alone. This mirrors the STD-0002 rule that the graph follows prose: the document text or a table states the relationship, and the diagram renders it. Neither of the architecture documents read for this guide — `ENTERPRISE_OPERATING_MODEL.md` and `architecture-principles.md` — contains a diagram, which confirms diagrams are a clarity aid rather than a structural requirement.

## 8. Identifiers and terminology

Identifier and terminology rules are set by STD-0001 and enforced under STD-0002. This guide adds no rules; it states the authoring consequences.

Identifier rules restated by reference to STD-0001:

1. format is `<PREFIX>-<zero-padded integer>` matching `^[A-Z][A-Z0-9-]*-[0-9]{4,6}$`;
2. a prefix is registered in `standards/vocabulary/object-identifiers.yaml` before any artifact mints an identifier with it;
3. published identifiers are never reused, renumbered, or reassigned;
4. one object carries one identifier everywhere it appears;
5. zero-padding width is fixed per prefix when the prefix is registered.

Width is a property of the prefix, not of the number, which is why ADR-0002, SVC-00387, and EAODS-CTRL-000184 are all well-formed at four, five, and six digits respectively.

The authoring consequence is strict: **do not write identifier-shaped tokens that do not exist.** `scripts/validate_traceability.py` scans every Markdown file under `docs/` and `architecture/` for tokens matching the identifier shape. A token whose prefix is unregistered fails CI outright. A token whose prefix is registered is recorded as a cited identifier and can then satisfy a relationship-graph endpoint, so an invented example silently becomes a legitimizing citation. Illustrative examples therefore use real, existing identifiers — as this section does — or name the bare prefix (`SVC`, `RUN`, `TERM`) with no digits.

Terminology rules restated by reference to STD-0001: one canonical name per concept, with aliases used only when quoting or preserving continuity; registration in `standards/vocabulary/canonical-terms.yaml` before normative use; no silent redefinition, since a changed definition requires Engineering Governance review and a registry version increment; and a volume may restate a definition for readability but may not contradict the registry. Prose that conflicts with a registry entry is a defect in the prose.

## 9. Sources and traceability requirement

Every governance-tier document ends with a numbered `## N. Sources and traceability` section containing a two-column table.

| Column | Content |
|---|---|
| Source (repo-relative path) | The path, POSIX-style and relative to the repository root, optionally followed by the source's identifier in parentheses |
| Contribution | What this specific source supplied, named down to the sections of the document it supports |

Requirements:

- **Derived content only.** Every factual claim in the document traces to a listed source. A claim that no listed source supports is removed, not softened.
- **Contribution is specific.** "Background" is not a contribution; "four enduring pillars (Section 2), traceability chain (Section 6)" is.
- **Evidence is labelled as evidence.** Conversation-derived and historical material is cited with its provenance and never treated as current authority, per the historical-lineage principle.
- **Relationships reach the graph.** Where a document states a relationship between governed objects, that relationship belongs in `standards/graph/relationships.yaml` using a registered edge type, so that prose and graph do not drift.
- **Absence claims are scoped.** A statement that something is not present names the specific artifacts examined, as Sections 2 and 7 of this guide do. Repository-wide negatives are not asserted from a partial reading.

## 10. Validation and the contribution workflow

| Check | Command | Failure condition |
|---|---|---|
| Framework front matter | `python scripts/validate_front_matter.py` | Missing required field, absent front-matter fence, or front matter that is not a YAML mapping |
| Cross-artifact traceability | `python scripts/validate_traceability.py` | Unregistered identifier prefix, unregistered edge type, or a graph endpoint cited nowhere |

Both run in the Documentation Quality workflow alongside the strict build, per STD-0002.

Pull requests follow `CONTRIBUTING.md`: short-lived branches named `docs/<topic>`, `feature/<capability>`, `fix/<issue>`, or `chore/<maintenance>`; Conventional Commits; and a description that explains business and architecture impact, identifies the affected EAODS volumes, passes documentation validation, preserves YAML front matter, and contains no secrets. A pull request that introduces an unregistered identifier prefix or an unregistered normative term does not pass review.

## 11. Authoring checklist

- [ ] Correct front-matter schema selected for the document's location (Section 2).
- [ ] All required fields present, with `owner` and gate fields truthful.
- [ ] Single H1 matching `title`; section numbering matches the document class.
- [ ] Human review gate section present; governance-tier documents close with sources and traceability.
- [ ] Present tense, third person, active voice, named actors for every obligation.
- [ ] Tables have header rows and parallel columns; diagrams restate prose rather than replace it.
- [ ] Every identifier cited exists and uses a registered prefix; no invented tokens.
- [ ] Every normative term matches the canonical terms registry.
- [ ] Every factual claim traces to a row in the sources table; absence claims name the artifacts examined.
- [ ] Both validators pass locally.

## 12. Human review gate

Approval of this guide requires confirmation by Engineering Governance and the Program Owner that:

- both front-matter schemas are stated as they are actually enforced, and the rule selecting between them matches the validator's search roots;
- the identifier and terminology rules restate STD-0001 without extending it, and the enforcement description matches STD-0002 and the traceability validator;
- the sources-and-traceability requirement matches the practice of the approved architecture documents;
- no new obligation is imposed on contributors beyond those already carried by STD-0001, STD-0002, and `CONTRIBUTING.md`.

Subsequent changes to this guide follow the same gate, and any change that alters an obligation rather than its wording requires a version increment.

## 13. Sources and traceability

| Source (repo-relative path) | Contribution |
|-----------------------------|--------------|
| scripts/validate_front_matter.py | The nine required framework fields, the `docs/frameworks` and `frameworks` search roots, and the parse conditions that constitute failure (Sections 2, 3, 10) |
| docs/frameworks/EAODS-v17.3/volume-08-security-engineering.md | Worked instance of the framework schema including the optional `extends` and `constitutional_authority` fields, the unnumbered section sequence for volumes, mermaid diagram usage, and the QA-checklist and review-gate closing pattern (Sections 2, 3, 5, 7) |
| docs/architecture/ENTERPRISE_OPERATING_MODEL.md (EAODS-ARCH-EOM-001) | Instance of the eight-field governance schema, numbered-section and `###` sub-section convention, status progression through the decision and accountability model, and named-ownership basis for the voice rules (Sections 4, 5, 6) |
| docs/architecture/architecture-principles.md (EAODS-ARCH-PRIN-001) | Second governance-schema instance, the two-column sources-and-traceability table format and its level of specificity, evidence-precedes-assertion and historical-lineage principles behind the labelling rules, and table conventions (Sections 5, 6, 7, 9) |
| docs/standards/canonical-terminology-and-identifiers.md (STD-0001) | Identifier format, registration, stability, one-object-one-ID and fixed-width rules; terminology rules and registry precedence; registry locations; the review sentence used as the normative-verb model; QA-checklist and mermaid workflow patterns (Sections 5, 6, 7, 8, 10) |
| docs/standards/cross-artifact-traceability.md (STD-0002) | Scanned trees, enforced rules and CI failure conditions, registered edge types, the graph-follows-prose rule applied to diagrams and to relationship recording, and the Documentation Quality workflow (Sections 1, 7, 9, 10) |
| scripts/validate_traceability.py | Behaviour of identifier-token scanning — unregistered prefixes fail, registered-prefix tokens are recorded as cited and can satisfy graph endpoints — which grounds the prohibition on invented identifier-shaped tokens (Sections 1, 8, 10) |
| CONTRIBUTING.md | Branch naming, Conventional Commits, and the pull-request expectations of impact explanation, affected-volume identification, documentation validation, front-matter preservation, and secret avoidance (Section 10) |
