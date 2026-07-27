"""Portfolio Documentation Agent.

Turns a description of lab/project work into a GitHub-ready Markdown document — a
README or a case study — following the project's documentation standard
(AGENTS.md §9). Returns a structured draft (sections + assembled Markdown +
suggested filename) for human review.

Scope & guardrails (AGENTS.md §5/§9):
- **Drafts only.** Returns Markdown; it never writes files or publishes. Placement
  and publishing are human-reviewed steps.
- **No fabrication.** It organizes the supplied description into the standard
  structure; it does not invent results, metrics, or sources. Placeholders are
  clearly marked for the author to fill.
- Deterministic and network-free.
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from typing import Any, Literal

DocType = Literal["readme", "case_study"]

# Case-study section order per AGENTS.md §9 documentation standard.
_CASE_STUDY_SECTIONS: tuple[str, ...] = (
    "Executive Summary",
    "Objectives",
    "Architecture / Process",
    "Implementation Steps",
    "Risks",
    "Cost Considerations",
    "Future Enhancements",
)

_README_SECTIONS: tuple[str, ...] = (
    "Overview",
    "Features",
    "Usage",
    "Skills Demonstrated",
    "Status",
)

_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")
_SLUG_STRIP = re.compile(r"[^a-z0-9]+")
_PLACEHOLDER = "_TODO: complete this section._"


def _slugify(text: str, *, max_len: int = 60) -> str:
    slug = _SLUG_STRIP.sub("-", text.lower()).strip("-")
    return slug[:max_len].rstrip("-") or "untitled"


@dataclass(frozen=True)
class DocumentationDraft:
    """A structured, GitHub-ready documentation draft for human review."""

    agent: str
    title: str
    doc_type: str
    suggested_filename: str
    summary: str
    sections: list[dict[str, str]]
    markdown: str
    assumptions: list[str]


class PortfolioDocumentationAgent:
    """Draft portfolio-ready README or case-study documents from a description."""

    def __init__(self, name: str = "Portfolio Documentation Agent") -> None:
        self.name = name

    def document(
        self,
        project_name: str,
        description: str,
        *,
        doc_type: DocType = "readme",
        skills: list[str] | None = None,
    ) -> dict[str, Any]:
        """Return a structured documentation draft for a project.

        Args:
            project_name: Human-readable project/work name (becomes the title).
            description: Plain-language description of the work.
            doc_type: "readme" (default) or "case_study" (AGENTS.md §9 structure).
            skills: Optional list of skills the work demonstrates.
        """
        if not isinstance(project_name, str) or not project_name.strip():
            raise ValueError("project_name must be a non-empty string.")
        if not isinstance(description, str) or not description.strip():
            raise ValueError("description must be a non-empty string.")
        if doc_type not in ("readme", "case_study"):
            raise ValueError("doc_type must be 'readme' or 'case_study'.")

        title = project_name.strip()
        desc = " ".join(description.split())
        summary = self._summarize(desc)
        sections = (
            self._case_study_sections(desc, summary)
            if doc_type == "case_study"
            else self._readme_sections(desc, summary, skills)
        )
        markdown = self._render(title, sections)

        result = DocumentationDraft(
            agent=self.name,
            title=title,
            doc_type=doc_type,
            suggested_filename=f"{_slugify(title)}.md",
            summary=summary,
            sections=sections,
            markdown=markdown,
            assumptions=[
                "Draft organizes only the supplied description; no results were invented.",
                "Sections marked TODO require the author to fill in specifics.",
                "Not written to disk — placement and publishing are human steps.",
            ],
        )
        return asdict(result)

    @staticmethod
    def _summarize(text: str, *, limit: int = 240) -> str:
        sentences = _SENTENCE_SPLIT.split(text)
        summary = sentences[0] if sentences else text
        return summary if len(summary) <= limit else summary[: limit - 1].rstrip() + "…"

    @staticmethod
    def _objectives(text: str, *, top: int = 4) -> list[str]:
        sentences = [s.strip() for s in _SENTENCE_SPLIT.split(text) if len(s.strip()) >= 8]
        return sentences[:top] or [text]

    def _case_study_sections(self, desc: str, summary: str) -> list[dict[str, str]]:
        objectives = "\n".join(f"- {o}" for o in self._objectives(desc))
        bodies = {
            "Executive Summary": summary,
            "Objectives": objectives,
            "Architecture / Process": _PLACEHOLDER,
            "Implementation Steps": _PLACEHOLDER,
            "Risks": _PLACEHOLDER,
            "Cost Considerations": _PLACEHOLDER,
            "Future Enhancements": _PLACEHOLDER,
        }
        return [{"heading": h, "body": bodies[h]} for h in _CASE_STUDY_SECTIONS]

    def _readme_sections(
        self, desc: str, summary: str, skills: list[str] | None
    ) -> list[dict[str, str]]:
        features = "\n".join(f"- {o}" for o in self._objectives(desc))
        skill_body = "\n".join(f"- {s}" for s in skills) if skills else _PLACEHOLDER
        bodies = {
            "Overview": summary,
            "Features": features,
            "Usage": _PLACEHOLDER,
            "Skills Demonstrated": skill_body,
            "Status": "Draft — pending author review.",
        }
        return [{"heading": h, "body": bodies[h]} for h in _README_SECTIONS]

    @staticmethod
    def _render(title: str, sections: list[dict[str, str]]) -> str:
        lines = [f"# {title}", ""]
        for section in sections:
            lines += [f"## {section['heading']}", section["body"], ""]
        lines += [
            "> Draft generated from a project description. Verify all claims and fill",
            "> any TODO sections before publishing.",
            "",
        ]
        return "\n".join(lines)


if __name__ == "__main__":
    agent = PortfolioDocumentationAgent()
    draft = agent.document(
        "SOC Analyst Agent v0.2",
        "Triages security logs, scores severity, maps to MITRE ATT&CK, and writes "
        "incident reports. Fully local and deterministic.",
        doc_type="case_study",
        skills=["Python", "Detection engineering", "RAG"],
    )
    print(json.dumps(draft, indent=2))
