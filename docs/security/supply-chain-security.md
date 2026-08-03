---
title: EAODS Software Supply Chain Security Standard
document_id: EAODS-SEC-SUPPLY-001
version: 1.0.0
status: proposed
owner: Security Architecture Owner
review_gate: Security Architecture Review Board and Program Owner approval
governing_architecture: EAODS v17.3 Volume 10
related:
  - EAODS-ARCH-EOM-001
  - THR-0001
  - PAT-0001
  - PAT-0003
  - PAT-0004
  - RUN-0001
  - RUN-0003
  - EAODS-CTRL-000184
  - ADR-0002
  - STD-0001
  - STD-0002
  - docs/frameworks/EAODS-v17.3/volume-07-devsecops-gitops.md
  - docs/frameworks/EAODS-v17.3/volume-08-security-engineering.md
  - history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v7.0-v8.3/EAODS-v7.7-alpha-enterprise-ai-software-supply-chain-security-provenance-and-artifact-integrity-standard.md
---

# EAODS Software Supply Chain Security Standard

## 1. Purpose and scope

This standard governs the creation, verification, distribution, deployment, maintenance, and retirement of every executable artifact in EAODS.

Its scope extends supply chain governance beyond application code to AI models, prompts, workflows, agents, policies, datasets, evaluation assets, plugins, orchestration logic, configuration bundles, and deployment manifests. Where an artifact executes, informs an execution decision, or is deployed into a runtime environment, it is in scope.

The standard sets the obligations. Volume 7 supplies the delivery architecture that carries them out; Volume 8 supplies the cryptographic services on which signing and verification depend.

## 2. Position in the operating model

Supply-chain security is a named component of Cybersecurity Domain 03, which operates across all four enduring pillars of the operating model. This standard therefore expresses obligations in each pillar rather than in a single lifecycle stage:

| Pillar | Supply chain obligation |
|---|---|
| Govern | Ownership, dependency policy, risk classification, third-party approval, release attestation as governed evidence |
| Design | Artifact taxonomy, provenance schema, signing profiles, repository and Infrastructure-as-Code standards |
| Operate | Runtime verification, drift detection, dependency monitoring, integrity incident response |
| Build | Trusted build environments, quality gates, SBOM generation, artifact signing, GitOps promotion |

Only verified artifacts may participate in enterprise cybersecurity workflows. Trusted detection engineering, secure response automation, verified recovery artifacts, evidence integrity, and trusted AI agents all inherit their assurance from this standard.

## 3. Governing principles

1. Every enterprise artifact is uniquely identifiable.
2. Every enterprise artifact is cryptographically verifiable.
3. Artifacts are immutable after publication.
4. Releases are reproducible where technically feasible.
5. Artifacts are policy-governed, continuously monitored, fully attributable, and lifecycle managed.
6. Delivery remains declarative, version-controlled, and continuously validated.
7. Governance precedes automation; final production approval remains under human authority.

Unsigned production artifacts are prohibited. Manual modification of production build outputs is prohibited.

## 4. Artifact taxonomy

Every artifact class below is subject to the full obligations of this standard, and each instance carries a globally unique enterprise identifier registered under the canonical identifier standard.

| Artifact type | Description |
|---|---|
| Source Code | Application and infrastructure code |
| AI Model | Foundation, fine-tuned, or specialized model |
| AI Agent | Autonomous operational component |
| Prompt | Governed production prompt |
| Workflow | Orchestration definition |
| Policy | Enterprise policy object |
| Dataset | Approved training or evaluation dataset |
| Evaluation Suite | Benchmark and validation assets |
| Container Image | Runtime deployment artifact |
| Infrastructure Definition | Platform provisioning artifact |
| Configuration Bundle | Approved runtime configuration |

## 5. Supply chain reference architecture

The governed path from source to assurance is fixed. No artifact may enter a runtime environment by any other route.

```text id="supply-chain-architecture"
Source Repository
        │
        ▼
Build Pipeline
        │
        ▼
Security Validation
        │
        ▼
Artifact Signing
        │
        ▼
Artifact Registry
        │
        ▼
Deployment Approval
        │
        ▼
Runtime Verification
        │
        ▼
Continuous Assurance
```

The delivery architecture in Volume 7 instantiates this chain through a source control platform, a CI pipeline, a security validation stage, an immutable artifact registry, a GitOps controller, a runtime platform, and independent continuous assurance.

## 6. Artifact lifecycle

Artifacts progress through design, development, security validation, signing, publication, deployment, continuous verification, and retirement. Two stages are gates rather than steps:

- **Signing** — an artifact that has not been signed by an approved signing profile cannot be published to the registry.
- **Deployment approval** — promotion into production requires documented approval criteria and, for the production environment, executive-controlled approval.

Retirement is a governed stage, not an omission: retired artifacts are recorded, their deployment authorization is withdrawn, and their provenance records are preserved.

## 7. Artifact record and provenance requirements

Each production artifact maintains a governed record whose fields are canonical across the platform.

| Field | Meaning |
|---|---|
| Artifact identifier | Globally unique enterprise identifier |
| Artifact type | Class from the taxonomy in section 4 |
| Version | Published, immutable version designation |
| Owner | Accountable engineering or governance function |
| Status | Governance state (for example, approved) |
| Integrity status | Result of the most recent verification |
| Signature profile | Approved enterprise signing profile applied |
| Provenance reference | Link to the immutable provenance record |
| Deployment scope | Environments in which the artifact is authorized |

The provenance record for every production artifact captures the origin repository, the originating organization, the build pipeline identifier, the build timestamp, the approving authority, validation evidence, the dependency inventory, and deployment history. Provenance records are immutable after publication and independently verifiable.

## 8. Dependency governance and SBOM

SBOM generation is a required property of the enterprise delivery pipeline, declared alongside artifact signing and policy validation in the pipeline definition rather than left to individual teams.

Every production artifact maintains a governed dependency inventory covering direct dependencies, transitive dependencies, licensing information, maintenance status, known security advisories, and approval status. Dependencies undergo continuous monitoring for newly disclosed risks, and dependency validation is one of the mandatory engineering quality gates.

Repository dependency policy is declared per repository and enforced through platform policy, not through convention.

## 9. Build integrity

Enterprise build pipelines enforce:

- authenticated source retrieval;
- isolated build environments;
- approved toolchains;
- automated security validation;
- artifact signing;
- immutable build logs;
- reproducibility verification where applicable.

Every production promotion additionally validates successful compilation, automated testing, code quality, static analysis, dependency validation, security scanning, infrastructure validation, and deployment readiness. Pipeline failures block promotion until resolved or formally waived.

## 10. Repository and Infrastructure-as-Code governance

Every repository declares ownership, branching strategy, protected branches, review requirements, commit signing policy, release process, dependency policy, and archival procedures. These declarations are enforced through platform policy.

Infrastructure definitions remain declarative, undergo peer review, support deterministic deployment, include rollback capability, produce audit evidence, and maintain version history. Manual production infrastructure changes require documented exception approval.

GitOps governance closes the loop: Git is the authoritative desired state, deployments occur through approved controllers, production changes are traceable to reviewed commits, configuration drift is detected and reported, and reconciliation activities generate audit events. Emergency overrides require post-implementation review.

## 11. Integrity verification

Integrity validation occurs before publication, before deployment, during runtime, after restoration, and during periodic assurance reviews. Integrity failures prevent deployment pending investigation.

Runtime environments verify the artifact signature, the approved version, deployment authorization, configuration integrity, dependency integrity, workload identity, and policy compliance. Verification failures generate security events within the Enterprise Security Data Fabric. Verification after restoration is what makes recovery trustworthy: an artifact reinstated by governed recovery orchestration (PAT-0004, RUN-0001) re-enters service only after its integrity is re-established.

## 12. Release attestation

Every production release produces an attestation containing the release identifier, the artifact inventory, a validation summary, the approval authority, the provenance reference, the integrity status, and the deployment scope. All seven attributes are required; an incomplete attestation is not a release.

Release attestations become governed evidence objects and are handled under the assurance evidence pipeline (PAT-0003) with the same integrity expectations as any other evidence.

## 13. Third-party component governance

Third-party artifacts undergo supplier evaluation, security review, dependency analysis, license review, operational approval, and periodic reassessment before and during use. Unsupported or unmaintained components require documented risk acceptance before continued use; risk acceptance is a governance decision with a named owner and a review date, not a permanent exemption.

## 14. Supply chain risk classification

Supply chain controls increase proportionally with artifact criticality.

| Tier | Description |
|---|---|
| SC-0 | Experimental |
| SC-1 | Internal Development |
| SC-2 | Operational |
| SC-3 | Business-Critical |
| SC-4 | High-Impact Enterprise |
| SC-5 | Mission-Critical Infrastructure |

Classification is assigned at design time, recorded on the artifact record, and reassessed when deployment scope changes.

## 15. Threat alignment

| Threat | Supply chain relevance | Anchoring control |
|---|---|---|
| Compromised service identity (THR-0001) | Runtime verification depends on workload identity; an artifact verified against a stolen identity is not trustworthy | EAODS-CTRL-000184 · PAT-0001 |
| Unauthorized artifact modification | Immutability after publication, signature verification, and immutable build logs remove the silent-change path | Sections 9 and 11 |
| Dependency and third-party compromise | Governed dependency inventory, continuous advisory monitoring, supplier reassessment | Sections 8 and 13 |
| Deployment drift | GitOps reconciliation, drift detection, continuous integrity monitoring | Sections 10 and 16 |

Where a supply chain integrity failure is also a compliance deviation, response follows RUN-0003 with escalation to Enterprise Cyber Command.

## 16. Continuous assurance and reporting

Continuous assurance independently monitors artifact integrity, provenance completeness, dependency changes, signature validity, unauthorized modifications, deployment drift, and release compliance. Results integrate with the enterprise evidence framework.

Delivery telemetry contributes deployment duration, deployment success rate, rollback frequency, change failure rate, recovery time, approval latency, and artifact verification status.

Executive reporting covers artifact inventory, integrity verification status, supply chain risk distribution, dependency health, release compliance, verification failures, provenance completeness, and unauthorized artifact activity.

## 17. AI-assisted engineering boundaries

AI assistance may support code review recommendations, pipeline optimization, deployment planning, dependency analysis, infrastructure validation, and release documentation. AI agents operating in the delivery path are themselves in-scope artifacts under section 4, and remain least privileged, observable, auditable, bounded by policy, and traceable to owners, controls, and evidence. Final production approval remains under human governance.

## 18. Required outputs

Conformance to this standard is demonstrated through a governed set of artifacts:

- Enterprise Artifact Registry;
- Provenance Register;
- Dependency Governance Report;
- Build Integrity Assessment;
- Release Attestation Package;
- Runtime Verification Dashboard;
- Supply Chain Risk Register;
- Executive Supply Chain Security Summary.

Artifact entities in the enterprise knowledge graph maintain governed relationships with repositories, build pipelines, AI models, AI agents, prompts, workflows, deployment environments, evidence, policies, and release records.

## 19. Human review gate

Approval of this standard, and of any change affecting artifact signing requirements, provenance controls, build pipeline governance, dependency management policies, runtime verification procedures, release attestation standards, third-party component governance, or supply chain risk classification, requires Security Architecture Review Board and Program Owner approval.

The review confirms that:

- no production artifact path bypasses signing, provenance, or runtime verification;
- risk classification remains proportional to deployment scope;
- attestation evidence remains complete and tamper-evident;
- AI authority in the delivery path remains bounded;
- traceability to controls, threat models, and evidence remains enforceable.

## 20. Sources and traceability

| Source (repo-relative) | Contribution |
|---|---|
| `history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v7.0-v8.3/EAODS-v7.7-alpha-enterprise-ai-software-supply-chain-security-provenance-and-artifact-integrity-standard.md` | Primary source. Supply chain architecture chain, artifact taxonomy, artifact lifecycle, canonical artifact record fields, provenance requirements, dependency governance, build pipeline governance, integrity verification points, release attestation attributes, third-party governance, runtime verification checks, SC-0 to SC-5 risk classification, continuous assurance scope, Domain 03 integration, executive reporting set, knowledge graph relationships, required outputs, human review scope. |
| `docs/frameworks/EAODS-v17.3/volume-07-devsecops-gitops.md` | Delivery architecture stages, delivery pipeline properties including required artifact signing, SBOM generation and policy validation, repository governance requirements, Infrastructure-as-Code standards, GitOps governance, engineering quality gates, release promotion model, deployment observability metrics, AI-assisted engineering boundaries. |
| `docs/frameworks/EAODS-v17.3/volume-08-security-engineering.md` | Security engineering control plane, PKI and secrets platform, runtime protection and platform integrity as the cryptographic and integrity services underpinning signing and verification; assurance-to-Executive-Control-Tower reporting path. |
| `docs/architecture/ENTERPRISE_OPERATING_MODEL.md` | House style and structure; four-pillar framing; Domain 03 cross-domain placement including supply-chain security; AI operating boundaries; decision, traceability, and human review model; governing architecture reference. |
| `docs/threat-models/THR-0001-compromised-service-identity.md` | House style for threat and mitigation tables; workload identity dependency in runtime verification; registered identifiers EAODS-CTRL-000184, PAT-0001, PAT-0003, PAT-0004, RUN-0001, RUN-0003 and their roles in identity, evidence, recovery, and deviation response. |
| `history/original-sources/EAODS_AI_Operator_Suite_transmissions/units/v7.0-v8.3/` (directory listing) | Unit inventory scanned to confirm v7.7 as the supply-chain, provenance, and artifact-integrity unit within the v7.0–v8.3 band. |

No control, metric, technique identifier, or classification in this document originates outside the sources listed above.
