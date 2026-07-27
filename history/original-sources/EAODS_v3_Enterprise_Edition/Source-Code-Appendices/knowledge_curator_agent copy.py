"""Knowledge Curator Agent.

Organizes raw notes, transcripts, or research text into a **retrieval-ready
knowledge entry**: a suggested title, knowledge-base category, tags, summary, key
points, a slugified filename, and a clean Markdown body ready for ingestion into
``knowledge-base/`` (and thus retrievable by the Knowledge Base Agent).

Scope & guardrails (DESIGN.md §5; AGENTS.md §5):
- **Structures, does not publish.** It returns a proposed entry; it does **not**
  write into the corpus. Adding curated content to the knowledge base is a separate,
  human-reviewed step (the corpus is a trusted source — see `rag/ingest.py`).
- **No fabrication.** It reorganizes and summarizes the supplied text only; it does
  not invent facts, sources, or citations. A "verify sources" note is included.
- Deterministic and network-free.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from dataclasses import asdict, dataclass
from typing import Any

# Map salient keywords -> knowledge-base category (mirrors knowledge-base/ folders).
_CATEGORY_RULES: list[tuple[str, frozenset[str]]] = [
    ("mitre", frozenset({"mitre", "att&ck", "attack", "tactic", "technique", "adversary"})),
    ("owasp", frozenset({"owasp", "injection", "xss", "web application", "broken access"})),
    ("nist", frozenset({"nist", "csf", "cybersecurity framework", "govern", "identify"})),
    ("cis", frozenset({"cis", "controls", "safeguard", "benchmark"})),
    ("security-plus", frozenset({"security+", "comptia", "exam", "certification", "domain"})),
    (
        "cybersecurity",
        frozenset({"soc", "incident", "detection", "log", "alert", "triage", "siem"}),
    ),
]

_TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9+#-]{2,}")
_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")
_SLUG_STRIP = re.compile(r"[^a-z0-9]+")

_STOPWORDS: frozenset[str] = frozenset(
    {
        "the",
        "and",
        "for",
        "with",
        "that",
        "this",
        "from",
        "are",
        "was",
        "were",
        "has",
        "have",
        "may",
        "any",
        "into",
        "use",
        "used",
        "uses",
        "per",
        "via",
        "not",
        "you",
        "your",
        "our",
        "their",
        "its",
        "can",
        "will",
        "they",
        "them",
        "but",
        "all",
        "also",
        "such",
        "which",
        "when",
        "then",
        "than",
        "what",
    }
)


def _tokenize(text: str) -> list[str]:
    return [t for t in _TOKEN_RE.findall(text.lower()) if t not in _STOPWORDS]


def _slugify(text: str, *, max_len: int = 60) -> str:
    slug = _SLUG_STRIP.sub("-", text.lower()).strip("-")
    return slug[:max_len].rstrip("-") or "untitled"


@dataclass(frozen=True)
class CuratedEntry:
    """A retrieval-ready knowledge entry proposed for human review."""

    agent: str
    title: str
    suggested_category: str
    suggested_filename: str
    tags: list[str]
    summary: str
    key_points: list[str]
    markdown: str
    assumptions: list[str]


class KnowledgeCuratorAgent:
    """Turn raw text into a structured, retrieval-ready knowledge entry."""

    def __init__(self, name: str = "Knowledge Curator Agent") -> None:
        self.name = name

    def curate(
        self,
        text: str,
        *,
        title: str | None = None,
        category: str | None = None,
    ) -> dict[str, Any]:
        """Return a proposed knowledge-base entry built from raw ``text``.

        Args:
            text: Raw notes, transcript, or research text to organize.
            title: Optional title; otherwise derived from the content.
            category: Optional KB category override; otherwise auto-suggested.
        """
        if not isinstance(text, str):
            raise ValueError("text must be a string.")
        cleaned = text.strip()
        if not cleaned:
            raise ValueError("text cannot be empty.")

        resolved_title = title.strip() if title and title.strip() else self._derive_title(cleaned)
        tokens = _tokenize(cleaned)
        resolved_category = (
            category.strip()
            if category and category.strip()
            else self._suggest_category(cleaned.lower())
        )
        tags = self._extract_tags(tokens)
        summary = self._summarize(cleaned)
        key_points = self._key_points(cleaned)

        markdown = self._render_markdown(resolved_title, summary, key_points, tags)

        result = CuratedEntry(
            agent=self.name,
            title=resolved_title,
            suggested_category=resolved_category,
            suggested_filename=f"{_slugify(resolved_title)}.md",
            tags=tags,
            summary=summary,
            key_points=key_points,
            markdown=markdown,
            assumptions=[
                "Entry reorganizes only the supplied text; no facts were added.",
                "Category and tags are heuristic and should be confirmed.",
                "Not yet added to the corpus — placement is a human-reviewed step.",
            ],
        )
        return asdict(result)

    @staticmethod
    def _derive_title(text: str, *, limit: int = 80) -> str:
        first_line = next((ln.strip() for ln in text.splitlines() if ln.strip()), "")
        first_line = first_line.lstrip("#").strip()
        if not first_line:
            return "Untitled Note"
        # Prefer the first sentence so notes/transcripts get a clean, short title.
        candidate = (_SENTENCE_SPLIT.split(first_line)[0].strip() or first_line).rstrip(".!?")
        return candidate if len(candidate) <= limit else candidate[: limit - 1].rstrip() + "…"

    @staticmethod
    def _suggest_category(lowered: str) -> str:
        for category, keywords in _CATEGORY_RULES:
            if any(kw in lowered for kw in keywords):
                return category
        return "general"

    @staticmethod
    def _extract_tags(tokens: list[str], *, top: int = 6) -> list[str]:
        counts = Counter(tokens)
        return [tok for tok, _ in counts.most_common(top)]

    @staticmethod
    def _summarize(text: str, *, limit: int = 240) -> str:
        sentences = _SENTENCE_SPLIT.split(" ".join(text.split()))
        summary = sentences[0] if sentences else ""
        return summary if len(summary) <= limit else summary[: limit - 1].rstrip() + "…"

    @staticmethod
    def _key_points(text: str, *, top: int = 5) -> list[str]:
        # Prefer existing bullet lines; otherwise fall back to leading sentences.
        bullets = [
            ln.strip().lstrip("-*•").strip()
            for ln in text.splitlines()
            if ln.strip().startswith(("-", "*", "•"))
        ]
        if bullets:
            return bullets[:top]
        sentences = [s.strip() for s in _SENTENCE_SPLIT.split(" ".join(text.split())) if s.strip()]
        return sentences[:top]

    @staticmethod
    def _render_markdown(title: str, summary: str, key_points: list[str], tags: list[str]) -> str:
        lines = [f"# {title}", ""]
        if summary:
            lines += ["## Summary", summary, ""]
        if key_points:
            lines += ["## Key Points", *[f"- {p}" for p in key_points], ""]
        if tags:
            lines += ["## Tags", ", ".join(tags), ""]
        lines += [
            "> Curated from supplied notes. Verify all facts and add authoritative",
            "> sources before relying on this entry.",
            "",
        ]
        return "\n".join(lines)


if __name__ == "__main__":
    agent = KnowledgeCuratorAgent()
    sample = (
        "SOC alert triage notes. The analyst classifies the event, scores severity, "
        "and extracts indicators.\n- Preserve evidence\n- Correlate timestamps\n"
        "- Escalate high-risk incidents to a human."
    )
    print(json.dumps(agent.curate(sample), indent=2))
