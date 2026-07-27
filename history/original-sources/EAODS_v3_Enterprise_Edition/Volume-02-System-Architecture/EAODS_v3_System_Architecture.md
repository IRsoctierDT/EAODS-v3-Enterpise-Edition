---
title: "EAODS v3 System Architecture Overview"
version: "3.0"
owner: "Ivan Rozenblad"
generated: "2026-07-06T21:02:37.224733+00:00"
description: "Reference architecture for the Enterprise AI Operator Documentation Suite and its agent ecosystem."
---

# EAODS v3 System Architecture Overview

## Architecture Intent

The EAODS platform treats each agent as a governed capability inside a larger operating system. The Orchestrator coordinates task routing. Knowledge agents manage source integrity. Security agents assess and report threats. Business agents convert operational work into client-ready outputs. Compliance agents enforce evidence, policy, audit, and risk discipline.

## Logical Architecture

```mermaid
flowchart LR
    User[User / Operator] --> ORCH[Orchestrator Agent]
    ORCH --> KB[Knowledge Base Agent]
    ORCH --> KC[Knowledge Curator Agent]
    ORCH --> EA[Executive Assistant Agent]
    ORCH --> LC[Legal Compliance Agent]
    ORCH --> TI[Threat Intelligence Agent]
    ORCH --> DM[Detection Matcher Agent]
    ORCH --> IR[Incident Report Agent]
    ORCH --> BP[Business Proposal Agent]
    ORCH --> PD[Portfolio Documentation Agent]
    KB <--> KC
    TI --> DM
    DM --> IR
    LC --> IR
    BP --> PD
```

## Trust Boundaries

```mermaid
flowchart TD
    A[Public Information] --> B[Research Staging]
    C[Private User Context] --> D[Protected Context Zone]
    E[Uploaded Files] --> F[Evidence Review Zone]
    B --> G[Agent Analysis]
    D --> G
    F --> G
    G --> H[Human Review Gate]
    H --> I[Published Deliverable]
```

## Operating Model

1. Intake receives the request.
2. Orchestrator identifies required agents.
3. Knowledge Base retrieves existing evidence.
4. Knowledge Curator validates source quality.
5. Specialist agents perform analysis.
6. Compliance or security agents review risk where applicable.
7. Executive Assistant converts outputs into actions and follow-ups.
8. Portfolio Documentation Agent preserves the result as reusable evidence.
