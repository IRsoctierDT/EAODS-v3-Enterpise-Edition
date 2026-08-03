---
title: EAODS Documentation Quality Assurance Framework
document_id: EAODS-DOC-QA-001
version: 1.0.0
status: proposed
owner: Engineering Governance
review_gate: Engineering Governance and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - STD-0001
  - STD-0002
  - ADR-0002
  - EAODS-ARCH-EOM-001
  - EAODS-ARCH-PRIN-001
  - .github/workflows/docs-quality.yml
---

# EAODS Documentation Quality Assurance Framework

## 1. Purpose and scope

This framework describes how documentation quality is actually assured in the EAODS Enterprise Edition repository: an automated gate that runs on every pull request and every push to `main`, and the human review gates that automation is not capable of replacing.

It is descriptive of the implemented mechanism, not aspirational. Every check named here corresponds to a step in `.github/workflows/docs-quality.yml` and, where a script is invoked, to code under `scripts/`.

Scope: Markdown artifacts under `docs/` and `architecture/`, the MkDocs site configuration, the registries under `standards/`, and the workflow that validates them. Historical evidence preserved verbatim is treated specially, as described in Section 7.

## 2. Quality model

Two operating-model commitments shape the design. *Evidence precedes assertion* — a quality claim about the suite is only as good as the check that produces it. And *governance precedes automation* — automation enforces rules a governing standard has already defined rather than inventing them. Each check therefore enforces an already-governed rule:

| Layer | Enforces | Governing source |
|---|---|---|
| Strict site build | The published suite renders and its navigation resolves | `mkdocs.yml` |
| Front-matter validation | Framework volumes carry required governance metadata | `standards/metadata/document-front-matter.schema.yaml` |
| Traceability validation | Identifiers and relationship edges are registered and real | STD-0001, STD-0002 |
| Link and navigation validation | Internal references resolve to files that exist | Repository convention, enforced in CI |
| Secret-like file detection | No key-shaped material enters a public repository | `SECURITY.md`, `CONTRIBUTING.md` |
| Human review gates | Meaning, authority, and accuracy | GOVERNANCE.md, ADR-0002, STD-0002 |

Automation decides whether a claim is *well-formed*. Humans decide whether it is *true*.

## 3. The automated gate

The Documentation Quality workflow triggers on `pull_request` and on `push` to `main`. It runs one job, `validate`, on `ubuntu-latest`, with `permissions: contents: read` — the gate reads the repository and reports; it holds no write authority over it.

Environment setup, in order:

1. `actions/checkout@v7` with `fetch-depth: 0`. Full history is fetched because the MkDocs revision-date plugin resolves per-page dates from commit history; a shallow clone would leave it without that history.
2. `actions/setup-python@v7` pinned to Python `3.12`, with the pip cache keyed to `requirements-docs.txt`.
3. `pip install -r requirements-docs.txt`, which pins the toolchain: `mkdocs-material`, the git revision-date plugin, and `PyYAML` — the parser all three validators depend on.

Five checks then run as sequential steps. Any non-zero exit fails the step, fails the job, and blocks the change.

## 4. Check 1 — Strict documentation build

**Command.** `mkdocs build --strict`.

**What it enforces.** That the suite is buildable as a site, not merely readable as files. Strict mode promotes build warnings to errors, so conditions a normal build tolerates become gate failures: a `nav` entry naming a page that does not exist, an unparsable configuration, or Markdown the configured extension set cannot process. That extension set is part of the contract — `admonition`, `attr_list`, `tables`, `toc` with permalinks, `pymdownx.details`, and `pymdownx.superfences` are configured in `mkdocs.yml`, and content relying on anything outside it is a defect.

**Failure mode.** MkDocs exits non-zero. Because this is the first check, its failure masks the four that follow: a change that both breaks the build and cites an unregistered identifier reports only the build error on that run.

**Defect classes caught.** Unbuildable site, missing navigation target, malformed site configuration, unsupported Markdown construct.

## 5. Check 2 — Front-matter validation

**Command.** `python scripts/validate_front_matter.py`.

**Coverage.** The script searches `docs/frameworks` and `frameworks` — whichever exist — recursively for `*.md`. As written, it does not extend to `docs/architecture`, `docs/standards`, or the other documentation trees; front matter elsewhere in the suite is a convention this check does not police.

**What it enforces.** For each file in scope: the file begins with `---`, the front-matter block parses as YAML, the result is a mapping, and nine required keys are present — `title`, `version`, `owner`, `suite`, `status`, `classification`, `purpose`, `architecture_domain`, `review_cycle`. These are the nine keys declared in `standards/metadata/document-front-matter.schema.yaml`, so the schema and the validator are two statements of one rule.

**What it does not enforce.** Presence, not meaning. A required key whose value is empty, stale, or wrong satisfies the check; ownership accuracy and review-cycle plausibility are human-gate concerns.

**Failure mode.** Failures accumulate rather than short-circuit: one line per offending file — `missing <fields>`, missing front matter, or the parser exception — printed under a `Front matter validation failed:` header, exit 1. A clean run prints the count of framework documents validated.

**Defect classes caught.** Unowned or unclassified framework volumes, corrupted or absent front matter, YAML that does not parse.

## 6. Check 3 — Cross-artifact traceability validation

**Command.** `python scripts/validate_traceability.py`.

This check is the enforcement arm of STD-0002, which states the rule plainly: traceability is a checked property of the repository, not a documentation convention. Its inputs are `standards/vocabulary/object-identifiers.yaml` (node identity), `standards/vocabulary/canonical-terms.yaml` (term nodes), and `standards/graph/relationships.yaml` (directed, typed edges).

**Rule 1 — no unregistered identifiers.** The script scans every `*.md` under `docs/` and `architecture/` for identifier-shaped tokens: an uppercase, hyphen-segmented prefix followed by four to six digits. The pattern deliberately matches candidates whose prefix is *not* registered, so unregistered prefixes are caught rather than skipped. Any token whose prefix is absent from the registry is reported with its file and fails the run; tokens with registered prefixes join the set of cited identifiers.

A consequence authors must internalise: an invented example identifier is indistinguishable from a real one to this check. Documentation about identifiers illustrates itself with registered examples — `SVC-00387`, `EAODS-CTRL-000184`, `ADR-0002` — because a plausible but unregistered placeholder would fail the very gate the document describes.

**Rule 2 — no unregistered edge types.** Every edge must use a type declared in the graph file's own `edge_types` list: `implements`, `operationalizes`, `mitigates`, `applies_to`, `emits_evidence_to`, `governed_by`. New edge types require Engineering Governance review before use.

**Rule 3 — no dangling endpoints.** For every edge, subject and object must both use a registered prefix *and* exist in the known set — the union of registered canonical-term identifiers and identifiers actually cited in prose. This makes STD-0002's "graph follows prose" rule mechanical: an edge asserting a relationship between objects no artifact mentions is a dangling endpoint and fails. The graph cannot drift ahead of the documents, and cannot be quietly populated with objects that do not exist.

**Failure mode.** All violations accumulate under a `Traceability validation failed:` header, exit 1. A clean run prints counts of cited identifiers, graph edges, and registered prefixes — an integrity signal in its own right.

**Defect classes caught.** Invented identifier prefixes, typos in cited identifiers, relationship claims about non-existent objects, edge-vocabulary drift, registry and document divergence.

## 7. Check 4 — Internal link and navigation validation

**Command.** `python scripts/validate_links.py`.

**Coverage and exclusions.** Markdown under `docs/` and `architecture/`, excluding any path containing `original-sources`, `source-archives`, or `recovered-deliverables`. The script states the reason: historical evidence is preserved verbatim and is never rewritten to satisfy repository conventions. This is the operating model's historical-lineage rule expressed as a code path — preserved material is exempt from convention, not from governance.

**What it enforces.**

1. **Relative links and images resolve.** Link and image targets are extracted, external schemes (`http:`, `https:`, `mailto:`) and pure in-page anchors are skipped, and each remaining target is resolved relative to the referring file's directory, fragment stripped, and must exist on disk.
2. **Navigation targets exist.** `mkdocs.yml` is parsed permissively — Python-specific YAML tags are neutralised before loading so the nav can be read without executing them — and every non-external nav entry must exist under `docs/`.
3. **Orphan reporting.** Documents under `docs/` absent from the nav, excluding `history` paths, are listed. This is advisory: orphans print as a note after a passing run and do not fail the gate. A new page never added to `mkdocs.yml` therefore ships unreachable from site navigation unless a reviewer acts on the note.

**What it does not enforce.** Fragments are discarded before resolution, so a link to a heading that no longer exists still resolves as long as the file does. External URLs are not fetched.

**Failure mode.** Broken targets accumulate as `broken link -> <target>` and `nav target missing -> <target>` lines, exit 1. A clean run reports the number of internal targets resolved.

**Defect classes caught.** Link rot from moved or renamed files, navigation entries pointing at deleted pages, mistyped relative paths, missing images.

## 8. Check 5 — Prohibited secret-like file detection

**Command.** An inline `bash` step running `find` across the working tree for files named `.env` or carrying the extensions `.pem`, `.key`, `.p12`, or `.pfx`. Any match prints `Prohibited secret-like file detected.` and exits 1.

**What it enforces.** That key-shaped material does not enter a public repository by filename. It is a name-based check, not a content scan: within this workflow as written, no step inspects file contents, so a credential pasted into the body of a Markdown file is not what this step is designed to catch. That residue belongs to review and to the repository's separate security tooling.

**Defect classes caught.** Committed private keys, certificate bundles, and environment files.

## 9. Ordering, determinism, and the guarantee

The five checks run in fixed order and the job stops at the first failure. Two consequences follow. A failing run reports the earliest defect, not all defects, so re-running after each fix is expected. And the ordering is deliberate: the build proves the suite is coherent as a site before the validators make finer-grained assertions about its contents.

Determinism comes from pinning — a fixed Python version and pinned toolchain versions mean a passing run today and one next quarter are comparable evidence. A green gate certifies exactly this and nothing more: the suite builds strictly, framework front matter is structurally complete, every cited identifier and graph edge is registered and grounded, internal references resolve, and no secret-shaped files are present.

## 10. Coverage boundary

Scoped to the workflow and the three validator scripts read for this document, the automated gate does not evaluate: whether a document's assertions are factually correct; whether front-matter values are current; whether a cited identifier is the *right* identifier for the object discussed; whether a resolving link points at the *relevant* page; whether a document contains the narrative sections GOVERNANCE.md requires — purpose, enterprise workflow, integration points, QA checklist, and human review gate; or whether historical material has been positioned so that it silently redefines current authority. Each is a human-gate responsibility.

## 11. Human review gates

Automation checks form; the gates below check authority and meaning.

- Material architecture changes follow the decision and accountability model: documented rationale, impact analysis, traceability to controls and standards, human architecture review, and Program Owner approval where the operating model is affected.
- Changes to the edge-type vocabulary, to the relationship-graph structure, or to the traceability validator's rules require Enterprise Architecture Review Board review and final approval by the program owner, per STD-0002 and GOVERNANCE.md.
- Changes to STD-0001 or to either vocabulary registry carry the same gate. Because the registries are the source of truth, a registry edit can make previously failing prose pass — which is why registry changes are governed more tightly than the prose they authorise.
- The repository owner retains final publication authority.

| Reviewer question | Why automation cannot answer it |
|---|---|
| Is the asserted relationship true? | The validator confirms endpoints exist and the type is registered, not that the claim holds |
| Is the owner named in front matter still accountable? | Presence is checked; currency is not |
| Does this page belong in navigation? | Orphan status is reported, never enforced |
| Does historical content override current authority? | Preserved paths are excluded from convention checks by design |
| Does the artifact meet the required narrative structure? | No check reads section headings |

## 12. Defect classes by layer

| Defect class | Caught by | Signal |
|---|---|---|
| Site fails to build; nav names a missing page | Strict build | MkDocs error; job stops |
| Framework volume missing governance metadata | Front-matter validation | Per-file `missing <fields>` report |
| Unparsable or absent front matter | Front-matter validation | Parser exception in report |
| Unregistered identifier prefix cited in prose | Traceability validation | File and offending token named |
| Relationship edge with a non-existent endpoint | Traceability validation | Dangling-endpoint report |
| Unregistered edge type | Traceability validation | Edge-type report |
| Broken internal link or missing image | Link validation | `broken link ->` report |
| Nav entry pointing at a deleted page | Link validation | `nav target missing ->` report |
| Page unreachable from navigation | Link validation | Advisory note only; reviewer must act |
| Key or environment file committed | Secret-like file detection | Job fails with a single message |
| False, stale, or misattributed content | Human review gates | Reviewer judgement |

## 13. Illustrative scenarios

The following are illustrative walkthroughs of the validators' own failure branches as implemented in this repository. They are not reports of real deployments and describe no organization.

*Scenario A — the self-defeating example.* An author drafting a page about the identifier standard invents a placeholder identifier to illustrate the format. The traceability check matches the placeholder, finds its prefix absent from the registry, and fails the run. The fix is to illustrate with registered identifiers such as `STD-0001` or `PAT-0001`, or to register the prefix first — registration before use, enforced against the document that describes it.

*Scenario B — the graph that outran the prose.* A contributor adds an edge asserting that a runbook operationalizes a pattern, but the corresponding runbook page is not part of the same change. The prefix is registered, so rule 1 passes; the endpoint is cited nowhere in `docs/` or `architecture/`, so rule 3 fails with a dangling-endpoint report. The graph is prevented from claiming a relationship the suite cannot show.

*Scenario C — the invisible page.* A well-formed new standard is added but not listed in `mkdocs.yml`. The strict build succeeds, links resolve, and the gate passes with an orphan note in its output. Only a reviewer reading that note gets the page into navigation — the clearest case of automation reporting where it deliberately does not enforce.

## 14. QA checklist

- [ ] Front matter present and complete for framework volumes.
- [ ] Every cited identifier uses a prefix registered under STD-0001.
- [ ] Any new relationship is asserted in prose before it is added to the graph.
- [ ] All relative links and images resolve from the referring file.
- [ ] New pages are added to the `mkdocs.yml` navigation.
- [ ] No `.env`, `.pem`, `.key`, `.p12`, or `.pfx` files in the change.
- [ ] Purpose, integration points, QA checklist, and human review gate present.
- [ ] All five automated checks passing on the head commit.
- [ ] Human review gate completed.

## 15. Human review gate

Approval of this framework requires confirmation by Engineering Governance and the Program Owner that:

- every check described here matches the workflow and scripts as committed;
- no check is claimed to enforce more than its code enforces;
- the coverage boundary in Section 10 is stated accurately and scoped to the sources read;
- human gates are stated as mandatory, not advisory;
- registry changes remain governed more tightly than the prose they authorise.

## 16. Sources and traceability

| Source (repo-relative path) | Contribution |
|---|---|
| `.github/workflows/docs-quality.yml` | Trigger conditions, job permissions, checkout and Python setup, the five validation steps and their order (Sections 3–9); secret-like file patterns and failure message (Section 8) |
| `scripts/validate_front_matter.py` | Search roots and coverage scope, nine required keys, parse and mapping checks, accumulating failure report and exit behaviour (Section 5) |
| `scripts/validate_traceability.py` | Registry inputs, identifier-token scan, unregistered-prefix rule, edge-type and dangling-endpoint rules, known-set construction, failure and success output (Section 6) |
| `scripts/validate_links.py` | Document roots and preserved-evidence exclusions, link and image resolution behaviour, permissive `mkdocs.yml` nav parsing, advisory orphan reporting (Section 7) |
| `docs/standards/cross-artifact-traceability.md` (STD-0002) | Traceability as a checked property, graph model and edge-type meanings, enforced rules, "graph follows prose", review gate for vocabulary and validator changes (Sections 2, 6, 11) |
| `docs/standards/canonical-terminology-and-identifiers.md` (STD-0001) | Identifier format and registration-before-use rule, registry authority, review gate for registry changes (Sections 6, 11) |
| `standards/vocabulary/object-identifiers.yaml` | Registered prefixes and canonical example identifiers cited in Section 6 |
| `standards/graph/relationships.yaml` | Edge-type vocabulary and edge structure validated in Section 6 |
| `standards/metadata/document-front-matter.schema.yaml` | Required front-matter keys mirrored by the validator (Sections 2, 5) |
| `mkdocs.yml` | Strict-build contract: navigation tree and configured Markdown extensions (Section 4) |
| `requirements-docs.txt` | Pinned documentation toolchain underpinning determinism (Sections 3, 9) |
| `GOVERNANCE.md` | Publication authority, required artifact sections, human review requirement (Sections 10, 11) |
| `SECURITY.md` | Prohibition on committing passwords, tokens, private keys, certificates, and sensitive data, which the secret-like file check partially enforces (Sections 2, 8) |
| `CONTRIBUTING.md` | Pull-request obligation to pass documentation validation, preserve YAML front matter, and avoid secrets (Sections 2, 8) |
| `docs/architecture/ENTERPRISE_OPERATING_MODEL.md` (EAODS-ARCH-EOM-001) | Decision and accountability model, historical lineage handling, house structure and review-gate form (Sections 2, 7, 11) |
| `docs/architecture/architecture-principles.md` (EAODS-ARCH-PRIN-001) | Governance-precedes-automation and evidence-precedes-assertion principles, human-gate doctrine, sources-table convention (Sections 2, 11, 16) |
