⸻

title: “EAODS v4.18-alpha — Authorized Scanning Governance Standard”
version: “4.18.0-alpha”
owner: “Ivan Rozenblad”
suite: “Enterprise AI Operator Documentation Suite”
status: “Draft”
classification: “Internal / Portfolio / Commercialization Candidate”
extends:

* “EAODS v4.17.2 AI-Assisted Vulnerability Prioritization Scoring Model”
* “EAODS v4.17.1 Vulnerability Intake & Triage Workflow”
* “EAODS v4.17 Enterprise Threat & Vulnerability Management Standard”
* “EAODS v4.15 Enterprise Security Operations & Incident Response Standard”
* “EAODS v4.12 Enterprise Trust, Identity & Authorization Architecture Standard”
    architecture_domain: “Threat and Vulnerability Management”
    cybersecurity_domain:
    domain_id: “Domain 03”
    domain_name: “Threat and Vulnerability Management”
    control_domain: “Authorized Security Assessment”
    review_cycle: “Quarterly”

⸻

Authorized Scanning Governance Standard

Purpose

This standard defines the governance requirements for conducting authorized security scanning within the Enterprise AI Operator Documentation Suite.

Its purpose is to ensure that vulnerability scanning, host discovery, network exposure review, application scanning, cloud assessment, container scanning, and AI-assisted security analysis occur only within documented scope, with approved authorization, controlled intensity, evidence preservation, and executive accountability.

This standard is especially relevant to EAODS-supported tooling such as MCPScan, LAN scanning modules, vulnerability intake workflows, and AI-assisted security assessment agents.

⸻

Core Rule

No scan shall run without documented authorization, defined scope, approved intensity, and accountable ownership.

Scanning without authorization is not an EAODS workflow. It is a governance violation.

⸻

Scope

This standard applies to:

* host discovery;
* port scanning;
* service enumeration;
* vulnerability scanning;
* web application scanning;
* cloud configuration scanning;
* container image scanning;
* dependency scanning;
* secret scanning;
* endpoint configuration review;
* LAN exposure review;
* AI-assisted scanner interpretation;
* automated security assessment workflows.

This standard does not authorize exploitation, credential attacks, denial-of-service testing, persistence, lateral movement, destructive testing, or bypassing access controls.

⸻

Authorization Principles

All scans shall be:

* authorized in writing;
* scoped before execution;
* limited to approved assets;
* performed using approved methods;
* logged for auditability;
* minimally intrusive by default;
* reviewed according to risk;
* linked to evidence records;
* reported through governed channels.

⸻

Approved Scan Categories

Scan Type	Description	Default Risk
Passive Review	Reads existing configuration, logs, or metadata	Low
Host Discovery	Identifies live assets in approved scope	Low to Moderate
Port Scan	Identifies exposed services	Moderate
Service Enumeration	Collects service banners and protocol details	Moderate
Vulnerability Scan	Tests known vulnerability signatures	Moderate to High
Web Application Scan	Reviews web routes, headers, auth, inputs	Moderate to High
Cloud Configuration Scan	Reviews cloud posture and IAM exposure	Moderate
Container Scan	Reviews packages, image layers, secrets	Low to Moderate
Secret Scan	Searches for exposed credentials or keys	Moderate
Authenticated Scan	Uses credentials for deeper assessment	High

⸻

Prohibited Activities

Unless separately authorized under a formal penetration-testing standard, EAODS scanning workflows shall not perform:

* exploitation;
* password spraying;
* brute force attempts;
* denial-of-service testing;
* phishing;
* social engineering;
* persistence mechanisms;
* malware deployment;
* privilege escalation;
* lateral movement;
* data exfiltration;
* bypassing authentication;
* destructive payloads;
* unauthorized third-party scanning.

Any request for these activities must be routed to a separate approved assessment workflow with legal and executive authorization.

⸻

Required Authorization Record

Every scan shall have an authorization record.

Field	Required
Authorization ID	✓
Requestor	✓
Approver	✓
Business Justification	✓
Asset Owner	✓
Scope Definition	✓
Scan Type	✓
Allowed Tools	✓
Intensity Level	✓
Approved Time Window	✓
Exclusions	✓
Evidence Handling Rules	✓
Reporting Destination	✓
Expiration Date	✓
Emergency Contact	✓

Authorization expires automatically unless renewed.

⸻

Scope Definition Requirements

Scope shall be explicit.

Acceptable scope formats include:

Scope Type	Example
Asset ID	ASSET-001
Hostname	app01.internal.example
IP Address	10.0.10.25
CIDR Range	10.0.10.0/24
Cloud Account	AWS account ID, Azure subscription, GCP project
Repository	GitHub repository name
Container Image	Registry path and tag
Application URL	Approved internal or owned application endpoint

Wildcard scope is prohibited unless explicitly approved and justified.

⸻

Scan Intensity Levels

Level	Description	Examples
Level 0 — Passive	No active probing	Config review, log review
Level 1 — Light	Minimal non-intrusive discovery	Ping, DNS, metadata
Level 2 — Standard	Controlled port/service discovery	TCP connect scan, banner check
Level 3 — Authenticated Review	Credentialed configuration or vulnerability review	Authenticated scanner
Level 4 — High-Impact Assessment	Intrusive or production-sensitive testing	Requires special approval

EAODS default is Level 1 or Level 2 unless stronger authorization exists.

⸻

Authorization Workflow

Scan Request
        │
        ▼
Business Justification
        │
        ▼
Asset Ownership Verification
        │
        ▼
Scope Definition
        │
        ▼
Tool and Method Selection
        │
        ▼
Intensity Classification
        │
        ▼
Risk Review
        │
        ▼
Approval
        │
        ▼
Scheduled Execution
        │
        ▼
Telemetry and Evidence Collection
        │
        ▼
Finding Intake
        │
        ▼
Executive Reporting

⸻

Pre-Scan Checklist

Before execution, the operator shall confirm:

* Authorization record exists.
* Authorization has not expired.
* Asset owner is identified.
* Scope is explicit.
* Exclusions are documented.
* Tool is approved.
* Intensity level is approved.
* Time window is approved.
* Emergency contact is recorded.
* Evidence handling rules are defined.
* Logging is enabled.
* Stop conditions are understood.

⸻

Stop Conditions

Scanning shall stop immediately when:

* scope mismatch is detected;
* unexpected third-party systems are reached;
* production instability is observed;
* credentials or secrets are exposed;
* scanning causes service degradation;
* legal, compliance, or customer-impact concerns arise;
* asset owner revokes authorization;
* tool behavior exceeds approved intensity;
* sensitive data appears in scanner output.

Stop events shall be logged and escalated.

⸻

Evidence Handling

Scan evidence may include:

* tool name and version;
* scan configuration;
* authorization record;
* scope definition;
* timestamps;
* raw scanner output;
* normalized findings;
* screenshots;
* logs;
* packet or protocol summaries;
* operator notes;
* exception records.

Evidence must be classified according to EAODS Data Governance requirements.

⸻

Tool Governance

Approved scanning tools shall be registered with:

Field	Requirement
Tool Name	Required
Version	Required
Owner	Required
Approved Use Cases	Required
Supported Scan Types	Required
Default Intensity	Required
Output Format	Required
Evidence Handling Notes	Required
Known Risks	Required
Last Review Date	Required

Unregistered tools may not be used in governed EAODS scanning workflows.

⸻

MCPScan / LAN Scanning Governance

EAODS-supported LAN scanning shall follow stricter controls.

Required Controls

* LAN scanning disabled by default.
* Explicit operator intent required.
* Authorization attestation required.
* Scope validation required.
* Private-range default unless explicitly approved.
* No implicit target expansion.
* Connect-and-handshake probing only unless otherwise authorized.
* No remote filesystem reads.
* No credentialed access unless separately approved.
* Findings limited to exposure, service, and configuration observations.

Recommended Output Model

LAN scan outputs should favor:

* JSON audit records;
* structured reports;
* host:port exposure findings;
* scope attestation;
* scan configuration;
* evidence references.

SARIF may be used only where the representation supports non-file logical locations clearly.

⸻

Cloud and Container Scanning Governance

Cloud and container scanning shall preserve:

* account/project identity;
* registry source;
* image digest;
* repository reference;
* permission context;
* scan timestamp;
* tool version;
* configuration baseline;
* detected findings;
* remediation guidance.

Credential exposure, public storage exposure, overly permissive IAM, and exposed management interfaces require escalation.

⸻

AI-Assisted Scanning Interpretation

AI may assist with:

* finding summarization;
* duplicate detection;
* false-positive review;
* remediation explanation;
* prioritization support;
* report generation;
* executive summary drafting.

AI shall not:

* expand scan scope;
* authorize scans;
* perform intrusive testing without approval;
* suppress findings without evidence;
* close vulnerabilities without human review;
* recommend exploitation against unauthorized systems.

⸻

Scan Result Workflow

Scan Completed
        │
        ▼
Evidence Registration
        │
        ▼
Output Normalization
        │
        ▼
Duplicate Detection
        │
        ▼
Vulnerability Intake
        │
        ▼
Triage and Prioritization
        │
        ▼
Owner Assignment
        │
        ▼
Remediation Tracking
        │
        ▼
Retest or Rescan
        │
        ▼
Closure / Reporting

⸻

Governance Metrics

Metric	Target
Authorized Scan Coverage	100%
Scope Violation Events	0
Expired Authorization Usage	0
Stop Condition Compliance	100%
Evidence Attachment Rate	100%
Tool Registration Compliance	100%
Unauthorized Third-Party Contact	0
Scan-to-Finding Traceability	100%

⸻

Executive Control Tower Integration

The Executive Control Tower shall display:

* active scan authorizations;
* upcoming scan windows;
* scan activity by asset group;
* scan findings by priority;
* expired authorizations;
* scope violations;
* stop-condition events;
* unauthorized tool attempts;
* remediation impact.

⸻

Artifact Factory Outputs

The Artifact Factory may generate:

* scan authorization record;
* rules of engagement summary;
* scan evidence binder;
* scope attestation;
* scan result summary;
* executive exposure report;
* remediation task list;
* retest report;
* exception memo.

⸻

Enterprise Case Study

Scenario

A security engineering team wants to add LAN exposure scanning to a local AI-assisted security tool used in an internal lab and small-business assessment environment.

Challenge

The tool’s original promise was localhost-focused safety. LAN scanning introduces legal, ethical, technical, and operational risk because it may contact devices beyond the operator’s direct system.

EAODS Implementation

The Authorized Scanning Governance Standard requires LAN scanning to remain off by default. Operators must provide explicit intent, authorization attestation, scope boundaries, approved intensity, and evidence-handling rules. The scan is limited to private-range targets and least-intrusive connect-and-handshake probes. The output records host:port exposure findings without reading remote files or attempting exploitation.

Outcome

The team adds LAN assessment capability while preserving:

* authorization discipline;
* defensible scope control;
* minimal intrusiveness;
* evidence traceability;
* executive visibility;
* safe portfolio demonstration value.

⸻

QA Checklist

* YAML front matter validated.
* Authorization-first principle documented.
* Scope requirements defined.
* Approved scan categories included.
* Prohibited activities listed.
* Authorization record requirements complete.
* Scan intensity levels documented.
* Authorization workflow included.
* Pre-scan checklist included.
* Stop conditions defined.
* Evidence handling requirements included.
* Tool governance included.
* MCPScan / LAN scanning governance included.
* Cloud and container scanning governance included.
* AI-assisted interpretation limits documented.
* Scan result workflow included.
* Governance metrics defined.
* Executive Control Tower integration included.
* Enterprise case study completed.
* Ready for security architecture, governance, and legal review.

⸻

Human Review Gate

This standard governs authorized scanning activity across EAODS. Changes affecting scan authorization, scope validation, prohibited activities, intensity levels, LAN scanning, cloud scanning, evidence handling, AI-assisted interpretation, or third-party contact controls shall undergo security architecture review, governance validation, legal review where appropriate, and executive approval before adoption.





