from __future__ import annotations

import argparse
import json
from pathlib import Path

from .registry import AgentRegistry
from .workflow import WorkflowState
from .security import classify_action
from .artifacts import generate_handbook
from .scorer import score_markdown
from .release import generate_release_notes
from .policy import evaluate_action, load_action
from .evidence import EvidenceRecord, add_evidence, list_evidence, evidence_summary
from .prompt_firewall import scan_file
from .dashboard import build_dashboard, build_dashboard_json
from .constitution import compile_constitution
from .artifact_factory import (
    context_from_workflow,
    generate_sop,
    generate_policy,
    generate_case_study,
    generate_client_deliverable,
    generate_portfolio_page,
    generate_evidence_binder,
    generate_release_bundle,
    generate_all_artifacts,
)


def cmd_agents(args: argparse.Namespace) -> None:
    registry = AgentRegistry(args.registry)
    for agent in registry.list_agents():
        print(f"{agent['id']}: {agent['name']} — {agent.get('role', '')}")


def cmd_route(args: argparse.Namespace) -> None:
    registry = AgentRegistry(args.registry)
    agent_id = registry.route(args.request)
    agent = registry.get(agent_id)
    print(json.dumps({"request": args.request, "agent_id": agent_id, "agent": agent}, indent=2))


def cmd_new_workflow(args: argparse.Namespace) -> None:
    registry = AgentRegistry(args.registry)
    required_agents = [registry.route(args.goal)]
    wf = WorkflowState(
        title=args.title,
        goal=args.goal,
        audience=args.audience or "",
        required_agents=required_agents,
        outputs=args.outputs or [],
        qa_checks=[
            "Scope is clear",
            "Assumptions are identified",
            "Risk tier is assigned",
            "Human approval gate applied where required",
            "Deliverable is archived",
        ],
    )
    path = Path(args.output)
    wf.save(path)
    print(f"Created workflow: {path}")


def cmd_classify(args: argparse.Namespace) -> None:
    print(json.dumps(classify_action(args.action), indent=2))


def cmd_generate(args: argparse.Namespace) -> None:
    path = generate_handbook(args.agent, args.output_dir, args.registry)
    print(f"Generated handbook: {path}")


def cmd_score(args: argparse.Namespace) -> None:
    result = score_markdown(args.file, args.schema)
    print(json.dumps(result, indent=2))


def cmd_release(args: argparse.Namespace) -> None:
    path = generate_release_notes(args.version, args.output_dir)
    print(f"Generated release notes: {path}")


def cmd_policy_check(args: argparse.Namespace) -> None:
    action = load_action(args.action)
    decision = evaluate_action(action)
    print(json.dumps(decision.to_dict(), indent=2))


def cmd_evidence_add(args: argparse.Namespace) -> None:
    record = EvidenceRecord(
        title=args.title,
        evidence_type=args.type,
        description=args.description or "",
        source_path=args.source_path or "",
        source_url=args.source_url or "",
        sensitivity=args.sensitivity,
        related_workflow=args.workflow or "",
        related_artifact=args.artifact or "",
    )
    result = add_evidence(args.ledger, record)
    print(json.dumps(result, indent=2))


def cmd_evidence_list(args: argparse.Namespace) -> None:
    records = list_evidence(args.ledger)
    print(json.dumps(records, indent=2))


def cmd_evidence_summary(args: argparse.Namespace) -> None:
    print(json.dumps(evidence_summary(args.ledger), indent=2))


def cmd_firewall_scan(args: argparse.Namespace) -> None:
    result = scan_file(args.file)
    print(json.dumps(result.to_dict(), indent=2))


def cmd_dashboard(args: argparse.Namespace) -> None:
    md_path = build_dashboard(args.workflow_dir, args.evidence_ledger, args.output)
    json_path = build_dashboard_json(args.workflow_dir, args.evidence_ledger, args.json_output)
    print(f"Generated dashboard: {md_path}")
    print(f"Generated dashboard JSON: {json_path}")


def cmd_constitution_compile(args: argparse.Namespace) -> None:
    paths = compile_constitution(args.source, args.output_dir)
    for p in paths:
        print(f"Wrote: {p}")


def _ctx_from_args(args: argparse.Namespace):
    evidence = list_evidence(args.evidence_ledger) if args.evidence_ledger and Path(args.evidence_ledger).exists() else []
    return context_from_workflow(
        args.workflow,
        title=args.title,
        purpose=args.purpose,
        scope=args.scope,
        audience=args.audience,
        evidence=evidence,
    )


def cmd_artifact_sop(args: argparse.Namespace) -> None:
    print(generate_sop(_ctx_from_args(args), args.output_dir))


def cmd_artifact_policy(args: argparse.Namespace) -> None:
    print(generate_policy(_ctx_from_args(args), args.output_dir))


def cmd_artifact_case_study(args: argparse.Namespace) -> None:
    print(generate_case_study(_ctx_from_args(args), args.output_dir))


def cmd_artifact_client(args: argparse.Namespace) -> None:
    print(generate_client_deliverable(_ctx_from_args(args), args.output_dir))


def cmd_artifact_portfolio(args: argparse.Namespace) -> None:
    print(generate_portfolio_page(_ctx_from_args(args), args.output_dir))


def cmd_artifact_binder(args: argparse.Namespace) -> None:
    print(generate_evidence_binder(_ctx_from_args(args), args.output_dir))


def cmd_artifact_release_bundle(args: argparse.Namespace) -> None:
    print(generate_release_bundle(_ctx_from_args(args), args.output_dir))


def cmd_artifact_all(args: argparse.Namespace) -> None:
    outputs = generate_all_artifacts(args.title, args.workflow, args.evidence_ledger, args.output_root)
    print(json.dumps(outputs, indent=2))


def add_artifact_common(p: argparse.ArgumentParser) -> None:
    p.add_argument("--title", required=True)
    p.add_argument("--workflow", default=None)
    p.add_argument("--purpose", default="")
    p.add_argument("--scope", default="")
    p.add_argument("--audience", default="")
    p.add_argument("--evidence-ledger", default="evidence/evidence_ledger.yaml")
    p.add_argument("--output-dir", default="artifacts")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="eaods", description="EAODS Artifact Factory CLI")
    parser.add_argument("--registry", default="agents.yaml", help="Path to agents.yaml")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("agents", help="List registered agents")
    p.set_defaults(func=cmd_agents)

    p = sub.add_parser("route", help="Route a request to a primary agent")
    p.add_argument("request")
    p.set_defaults(func=cmd_route)

    p = sub.add_parser("new-workflow", help="Create a workflow state YAML")
    p.add_argument("--title", required=True)
    p.add_argument("--goal", required=True)
    p.add_argument("--audience", default="")
    p.add_argument("--outputs", nargs="*", default=[])
    p.add_argument("--output", default="workflows/workflow_state.yaml")
    p.set_defaults(func=cmd_new_workflow)

    p = sub.add_parser("classify", help="Classify an action by EAODS risk tier")
    p.add_argument("action")
    p.set_defaults(func=cmd_classify)

    p = sub.add_parser("generate-handbook", help="Generate a runtime handbook for an agent")
    p.add_argument("agent")
    p.add_argument("--output-dir", default="artifacts")
    p.set_defaults(func=cmd_generate)

    p = sub.add_parser("score", help="Score a Markdown artifact")
    p.add_argument("file")
    p.add_argument("--schema", default="scorecard.schema.json")
    p.set_defaults(func=cmd_score)

    p = sub.add_parser("release-notes", help="Generate release notes")
    p.add_argument("version")
    p.add_argument("--output-dir", default="releases")
    p.set_defaults(func=cmd_release)

    p = sub.add_parser("policy-check", help="Evaluate an action YAML/JSON against EAODS policy")
    p.add_argument("action")
    p.set_defaults(func=cmd_policy_check)

    p = sub.add_parser("evidence", help="Manage EAODS evidence ledger")
    ev_sub = p.add_subparsers(dest="evidence_command", required=True)

    ev = ev_sub.add_parser("add", help="Add evidence record")
    ev.add_argument("--ledger", default="evidence/evidence_ledger.yaml")
    ev.add_argument("--title", required=True)
    ev.add_argument("--type", required=True)
    ev.add_argument("--description", default="")
    ev.add_argument("--source-path", default="")
    ev.add_argument("--source-url", default="")
    ev.add_argument("--sensitivity", default="internal")
    ev.add_argument("--workflow", default="")
    ev.add_argument("--artifact", default="")
    ev.set_defaults(func=cmd_evidence_add)

    ev = ev_sub.add_parser("list", help="List evidence records")
    ev.add_argument("--ledger", default="evidence/evidence_ledger.yaml")
    ev.set_defaults(func=cmd_evidence_list)

    ev = ev_sub.add_parser("summary", help="Summarize evidence ledger")
    ev.add_argument("--ledger", default="evidence/evidence_ledger.yaml")
    ev.set_defaults(func=cmd_evidence_summary)

    p = sub.add_parser("firewall", help="Prompt-injection firewall")
    fw_sub = p.add_subparsers(dest="firewall_command", required=True)
    fw = fw_sub.add_parser("scan", help="Scan file for prompt-injection risk")
    fw.add_argument("file")
    fw.set_defaults(func=cmd_firewall_scan)

    p = sub.add_parser("dashboard", help="Generate EAODS operator dashboard")
    p.add_argument("--workflow-dir", default="workflows")
    p.add_argument("--evidence-ledger", default="evidence/evidence_ledger.yaml")
    p.add_argument("--output", default="dashboards/eaods_dashboard.md")
    p.add_argument("--json-output", default="dashboards/eaods_dashboard.json")
    p.set_defaults(func=cmd_dashboard)

    p = sub.add_parser("constitution", help="Compile agent constitution into instruction files")
    c_sub = p.add_subparsers(dest="constitution_command", required=True)
    c = c_sub.add_parser("compile", help="Compile constitution")
    c.add_argument("--source", default="agent_constitution.yaml")
    c.add_argument("--output-dir", default=".")
    c.set_defaults(func=cmd_constitution_compile)

    p = sub.add_parser("artifact", help="Generate governed EAODS artifacts")
    a_sub = p.add_subparsers(dest="artifact_command", required=True)

    commands = [
        ("sop", "Generate SOP", cmd_artifact_sop),
        ("policy", "Generate policy", cmd_artifact_policy),
        ("case-study", "Generate case study", cmd_artifact_case_study),
        ("client", "Generate client-safe deliverable", cmd_artifact_client),
        ("portfolio", "Generate portfolio page", cmd_artifact_portfolio),
        ("binder", "Generate evidence binder", cmd_artifact_binder),
        ("release-bundle", "Generate release bundle", cmd_artifact_release_bundle),
    ]
    for name, help_text, func in commands:
        ap = a_sub.add_parser(name, help=help_text)
        add_artifact_common(ap)
        ap.set_defaults(func=func)

    ap = a_sub.add_parser("all", help="Generate all artifact types")
    ap.add_argument("--title", required=True)
    ap.add_argument("--workflow", default=None)
    ap.add_argument("--evidence-ledger", default="evidence/evidence_ledger.yaml")
    ap.add_argument("--output-root", default="artifacts")
    ap.set_defaults(func=cmd_artifact_all)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
