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
from .artifact_factory import generate_all_artifacts
from .publishing import (
    generate_repository_map,
    generate_mkdocs_nav,
    generate_changelog,
    batch_score,
    generate_issue,
    generate_pr,
    create_release_candidate,
    create_public_private_bundles,
)


def cmd_agents(args):
    registry = AgentRegistry(args.registry)
    for agent in registry.list_agents():
        print(f"{agent['id']}: {agent['name']} — {agent.get('role', '')}")


def cmd_route(args):
    registry = AgentRegistry(args.registry)
    agent_id = registry.route(args.request)
    agent = registry.get(agent_id)
    print(json.dumps({"request": args.request, "agent_id": agent_id, "agent": agent}, indent=2))


def cmd_new_workflow(args):
    registry = AgentRegistry(args.registry)
    wf = WorkflowState(
        title=args.title,
        goal=args.goal,
        audience=args.audience or "",
        required_agents=[registry.route(args.goal)],
        outputs=args.outputs or [],
        qa_checks=[
            "Scope is clear",
            "Assumptions are identified",
            "Risk tier is assigned",
            "Human approval gate applied where required",
            "Deliverable is archived",
        ],
    )
    wf.save(args.output)
    print(f"Created workflow: {args.output}")


def cmd_classify(args):
    print(json.dumps(classify_action(args.action), indent=2))


def cmd_generate(args):
    print(f"Generated handbook: {generate_handbook(args.agent, args.output_dir, args.registry)}")


def cmd_score(args):
    print(json.dumps(score_markdown(args.file, args.schema), indent=2))


def cmd_release(args):
    print(f"Generated release notes: {generate_release_notes(args.version, args.output_dir)}")


def cmd_policy_check(args):
    print(json.dumps(evaluate_action(load_action(args.action)).to_dict(), indent=2))


def cmd_evidence_add(args):
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
    print(json.dumps(add_evidence(args.ledger, record), indent=2))


def cmd_evidence_list(args):
    print(json.dumps(list_evidence(args.ledger), indent=2))


def cmd_evidence_summary(args):
    print(json.dumps(evidence_summary(args.ledger), indent=2))


def cmd_firewall_scan(args):
    print(json.dumps(scan_file(args.file).to_dict(), indent=2))


def cmd_dashboard(args):
    md_path = build_dashboard(args.workflow_dir, args.evidence_ledger, args.output)
    json_path = build_dashboard_json(args.workflow_dir, args.evidence_ledger, args.json_output)
    print(f"Generated dashboard: {md_path}")
    print(f"Generated dashboard JSON: {json_path}")


def cmd_constitution_compile(args):
    for p in compile_constitution(args.source, args.output_dir):
        print(f"Wrote: {p}")


def cmd_artifact_all(args):
    print(json.dumps(generate_all_artifacts(args.title, args.workflow, args.evidence_ledger, args.output_root), indent=2))


def cmd_publish_map(args):
    print(generate_repository_map(args.root, args.output))


def cmd_publish_mkdocs(args):
    print(generate_mkdocs_nav(args.root, args.output))


def cmd_publish_changelog(args):
    print(generate_changelog(args.root, args.output))


def cmd_publish_score(args):
    print(batch_score(args.root, args.schema, args.output))


def cmd_publish_issue(args):
    print(generate_issue(args.title, args.body, args.output_dir))


def cmd_publish_pr(args):
    print(generate_pr(args.title, args.summary, args.output_dir))


def cmd_publish_release_candidate(args):
    print(create_release_candidate(args.root, args.version, args.output_dir))


def cmd_publish_bundles(args):
    print(json.dumps(create_public_private_bundles(args.root, args.version, args.output_dir), indent=2))


def build_parser():
    parser = argparse.ArgumentParser(prog="eaods", description="EAODS Publishing Automation CLI")
    parser.add_argument("--registry", default="agents.yaml", help="Path to agents.yaml")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("agents"); p.set_defaults(func=cmd_agents)
    p = sub.add_parser("route"); p.add_argument("request"); p.set_defaults(func=cmd_route)

    p = sub.add_parser("new-workflow")
    p.add_argument("--title", required=True)
    p.add_argument("--goal", required=True)
    p.add_argument("--audience", default="")
    p.add_argument("--outputs", nargs="*", default=[])
    p.add_argument("--output", default="workflows/workflow_state.yaml")
    p.set_defaults(func=cmd_new_workflow)

    p = sub.add_parser("classify"); p.add_argument("action"); p.set_defaults(func=cmd_classify)
    p = sub.add_parser("generate-handbook"); p.add_argument("agent"); p.add_argument("--output-dir", default="artifacts"); p.set_defaults(func=cmd_generate)
    p = sub.add_parser("score"); p.add_argument("file"); p.add_argument("--schema", default="scorecard.schema.json"); p.set_defaults(func=cmd_score)
    p = sub.add_parser("release-notes"); p.add_argument("version"); p.add_argument("--output-dir", default="releases"); p.set_defaults(func=cmd_release)
    p = sub.add_parser("policy-check"); p.add_argument("action"); p.set_defaults(func=cmd_policy_check)

    p = sub.add_parser("evidence")
    ev_sub = p.add_subparsers(dest="evidence_command", required=True)
    ev = ev_sub.add_parser("add")
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
    ev = ev_sub.add_parser("list"); ev.add_argument("--ledger", default="evidence/evidence_ledger.yaml"); ev.set_defaults(func=cmd_evidence_list)
    ev = ev_sub.add_parser("summary"); ev.add_argument("--ledger", default="evidence/evidence_ledger.yaml"); ev.set_defaults(func=cmd_evidence_summary)

    p = sub.add_parser("firewall")
    fw_sub = p.add_subparsers(dest="firewall_command", required=True)
    fw = fw_sub.add_parser("scan"); fw.add_argument("file"); fw.set_defaults(func=cmd_firewall_scan)

    p = sub.add_parser("dashboard")
    p.add_argument("--workflow-dir", default="workflows")
    p.add_argument("--evidence-ledger", default="evidence/evidence_ledger.yaml")
    p.add_argument("--output", default="dashboards/eaods_dashboard.md")
    p.add_argument("--json-output", default="dashboards/eaods_dashboard.json")
    p.set_defaults(func=cmd_dashboard)

    p = sub.add_parser("constitution")
    c_sub = p.add_subparsers(dest="constitution_command", required=True)
    c = c_sub.add_parser("compile")
    c.add_argument("--source", default="agent_constitution.yaml")
    c.add_argument("--output-dir", default=".")
    c.set_defaults(func=cmd_constitution_compile)

    p = sub.add_parser("artifact")
    a_sub = p.add_subparsers(dest="artifact_command", required=True)
    a = a_sub.add_parser("all")
    a.add_argument("--title", required=True)
    a.add_argument("--workflow", default=None)
    a.add_argument("--evidence-ledger", default="evidence/evidence_ledger.yaml")
    a.add_argument("--output-root", default="artifacts")
    a.set_defaults(func=cmd_artifact_all)

    p = sub.add_parser("publish", help="Publishing automation commands")
    pub = p.add_subparsers(dest="publish_command", required=True)

    q = pub.add_parser("map"); q.add_argument("--root", default="."); q.add_argument("--output", default="Repository_Map.generated.md"); q.set_defaults(func=cmd_publish_map)
    q = pub.add_parser("mkdocs"); q.add_argument("--root", default="."); q.add_argument("--output", default="mkdocs.generated.yml"); q.set_defaults(func=cmd_publish_mkdocs)
    q = pub.add_parser("changelog"); q.add_argument("--root", default="."); q.add_argument("--output", default="CHANGELOG.md"); q.set_defaults(func=cmd_publish_changelog)
    q = pub.add_parser("score-all"); q.add_argument("--root", default="."); q.add_argument("--schema", default="runtime/scorecard.schema.json"); q.add_argument("--output", default="runtime/dashboards/batch_scores.json"); q.set_defaults(func=cmd_publish_score)
    q = pub.add_parser("issue"); q.add_argument("--title", required=True); q.add_argument("--body", required=True); q.add_argument("--output-dir", default="runtime/publishing/issues"); q.set_defaults(func=cmd_publish_issue)
    q = pub.add_parser("pr"); q.add_argument("--title", required=True); q.add_argument("--summary", required=True); q.add_argument("--output-dir", default="runtime/publishing/pull_requests"); q.set_defaults(func=cmd_publish_pr)
    q = pub.add_parser("release-candidate"); q.add_argument("--root", default="."); q.add_argument("--version", default="v4.4.0-alpha"); q.add_argument("--output-dir", default="runtime/artifacts/release_candidates"); q.set_defaults(func=cmd_publish_release_candidate)
    q = pub.add_parser("bundles"); q.add_argument("--root", default="."); q.add_argument("--version", default="v4.4.0-alpha"); q.add_argument("--output-dir", default="runtime/artifacts"); q.set_defaults(func=cmd_publish_bundles)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
