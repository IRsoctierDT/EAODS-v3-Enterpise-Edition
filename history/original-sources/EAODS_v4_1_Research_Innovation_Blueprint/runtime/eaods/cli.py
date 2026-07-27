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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="eaods", description="EAODS Runtime Alpha CLI")
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

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
