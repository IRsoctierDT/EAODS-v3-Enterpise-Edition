---
title: "EAODS GitHub and Publishing Automation Design"
version: "4.4.0-alpha"
owner: "Ivan Rozenblad"
generated: "2026-07-07T19:45:01.576085+00:00"
classification: "Internal / Portfolio / Commercialization Candidate"
description: "Design for repository mapping, changelog generation, release candidate packaging, MkDocs navigation, GitHub issue/PR automation, and public/private bundle separation."
---

# EAODS GitHub and Publishing Automation Design

## Purpose

EAODS v4.4 adds the publishing layer. The system can now prepare repository-ready documentation assets, score them, package release candidates, and separate public-safe material from private/internal material.

## Publishing Workflow

```mermaid
flowchart TD
    A[Repository Files] --> B[Repository Map]
    B --> C[Batch Artifact Scoring]
    C --> D[Changelog Generation]
    D --> E[Release Candidate Builder]
    E --> F[Public / Private Split]
    F --> G[MkDocs Navigation]
    G --> H[GitHub Issue and PR Templates]
    H --> I[Release Review]
    I --> J[Publish or Archive]
```

## Publishing Rules

1. Public bundles must exclude sensitive source appendices unless explicitly approved.
2. Private bundles may include internal governance, working notes, and source appendices.
3. Release candidates must include a manifest.
4. Artifact scoring should be run before release.
5. Files below release threshold should be listed as review-required.
6. GitHub issue and PR text should be generated from workflow state when possible.
7. MkDocs navigation should be generated from Markdown inventory.

## Strategic Improvement

EAODS now has the ability to move from local generation to controlled release operations.
