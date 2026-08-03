---
title: EAODS Accessibility Statement
document_id: EAODS-PUB-A11Y-001
version: 1.0.0
status: proposed
owner: Engineering Governance
review_gate: Engineering Governance and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - docs/standards/documentation-standards.md
  - mkdocs.yml
---

# EAODS Accessibility Statement

## 1. Purpose

This statement records the accessibility posture of the EAODS Enterprise
Edition documentation site, the checks performed, their measured results, and
the limits of what has been verified. It is written to the same evidentiary
standard as the rest of the corpus: every claim below is either measured or
declared unverified.

## 2. Target conformance

The site targets **WCAG 2.1 Level AA**. Conformance is claimed only for the
items measured in section 4. No third-party audit has been performed, and no
assistive-technology user testing has been conducted; both are recorded as
gaps in section 6.

## 3. Platform baseline

The site is built with MkDocs Material, which supplies the structural
accessibility baseline:

| Capability | Source |
|---|---|
| Semantic landmarks and heading structure | Theme templates |
| Keyboard-navigable navigation, search, and content | Theme behaviour |
| Skip-to-content link | Theme behaviour |
| Responsive reflow without horizontal scrolling | Theme layout |
| Visible focus indicators | Theme styles |
| Light and dark palettes meeting AA contrast for body text | Theme palette defaults |

The theme baseline is inherited, not independently re-verified by this project.

## 4. Content checks performed

Automated content audit across the **61 authored documentation pages**
(historical evidence trees excluded, as those are preserved verbatim and are
never rewritten to satisfy presentation conventions):

| Check | Requirement | Result |
|---|---|---|
| Images without alternative text | WCAG 1.1.1 | **0** — the corpus contains no raster images; diagrams are rendered as text or Mermaid |
| Heading-level jumps (e.g. `##` directly to `####`) | WCAG 1.3.1, 2.4.6 | **0 pages** |
| Tables lacking a header row | WCAG 1.3.1 | **0 of 218 tables** |
| Non-descriptive link text ("click here", "this link") | WCAG 2.4.4 | **0 occurrences** |
| Internal links and navigation targets resolving | Usability; WCAG 2.4.5 support | **All resolve** — enforced in CI by `scripts/validate_links.py` |

These checks run against authored content. The heading, table, and link checks
are structural and repeatable; the link check is enforced on every pull
request.

## 5. Design decisions that support access

- **Text-first diagrams.** Architecture and workflow diagrams are expressed as
  Mermaid or ASCII structures rather than images, so they remain available to
  screen readers and to text-only consumers.
- **Tabular data carries headers.** Every table declares a header row, so
  cell relationships survive linearization.
- **No colour-only meaning.** Status is conveyed in words (`complete`,
  `pending`, `excepted`), never by colour alone.
- **Stable, descriptive link text.** Links name their destination.

## 6. Known gaps

| Gap | Status |
|---|---|
| Independent third-party accessibility audit | Not performed |
| Assistive-technology user testing (screen reader, voice control) | Not performed |
| Automated axe/Lighthouse run against the rendered site | Not yet wired into CI |
| Mermaid diagram accessible descriptions | Rendered diagrams rely on surrounding prose; per-diagram text alternatives are not yet authored |
| PDF library accessibility (tagged PDFs) | Generated PDFs are not verified for tagging or reading order |

Closing these gaps is scoped as follow-on work under Documentation Excellence.

## 7. Feedback

Accessibility defects should be raised as repository issues using the bug
report template. Reports that identify a barrier to access are triaged at the
same priority as functional defects.

## 8. Sources and traceability

| Source (repo-relative) | Contribution |
|---|---|
| `mkdocs.yml` | Theme, palette, and navigation features constituting the platform baseline in section 3 |
| `scripts/validate_links.py` | The enforced link and navigation resolution check cited in section 4 |
| `docs/standards/canonical-terminology-and-identifiers.md` | Terminology discipline underlying the "no colour-only meaning" rule |
| Automated audit of `docs/**/*.md` (61 pages, excluding history trees) | The measured results in section 4 |
