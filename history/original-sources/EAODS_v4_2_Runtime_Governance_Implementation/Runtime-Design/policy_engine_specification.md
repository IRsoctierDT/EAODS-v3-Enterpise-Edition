---
title: "EAODS Policy Engine Specification"
version: "4.1.0-alpha"
owner: "Ivan Rozenblad"
generated: "2026-07-07T19:36:27.504726+00:00"
classification: "Internal / Portfolio / Commercialization Candidate"
description: "Specification for a policy engine that controls agent actions, approvals, risk tiers, and release gates."
---

# EAODS Policy Engine Specification

## Purpose

The Policy Engine determines whether an agent action may proceed, requires human approval, must be modified, or must be blocked.

## Policy Inputs

```yaml
action:
  id:
  requested_by:
  agent_id:
  action_type:
  target:
  sensitivity:
  risk_tier:
  evidence:
  approval_status:
```

## Policy Decision Types

| Decision | Meaning |
|---|---|
| allow | Action may proceed |
| allow_with_logging | Action may proceed but must be logged |
| require_approval | Human approval required |
| require_evidence | Missing source/evidence blocks action |
| require_revision | Artifact fails quality or structure checks |
| deny | Action is unsafe or prohibited |

## Default Rules

1. Tier 0 actions may proceed with logging.
2. Tier 1 actions may proceed if no sensitive data is present.
3. Tier 2 actions require explicit approval.
4. Tier 3 actions require explicit approval and command review.
5. Tier 4 actions require strict approval and rollback planning.
6. Tier 5 actions require qualified human review.
7. Any action involving secrets defaults to deny unless a secure secret-management pattern is used.
8. Any legal or compliance conclusion must identify jurisdiction, authority, and assumptions.

## Future Implementation

The policy engine should become a Python module:

```text
runtime/eaods/policy.py
```

with unit tests for each risk tier and decision type.
