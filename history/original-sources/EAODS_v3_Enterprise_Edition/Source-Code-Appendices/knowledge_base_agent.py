"""Knowledge Base Agent — grounds analysis in the curated cybersecurity corpus.

Given a query (or a SOC/MITRE result), this agent retrieves the most relevant
references from the local ``knowledge-base/`` corpus so incident reports can cite
authoritative framework context (MITRE ATT&CK, OWASP, NIST CSF, CIS, etc.).

Two retrieval modes (DESIGN.md §5):
- **lexical** (default) — a deterministic, dependency-free term-overlap score. No
  network, fully reproducible, CI-safe. This is what the agent pipeline uses.
- **semantic** — embeds the query and corpus chunks via the local ``OllamaEmbedder``
  (loopback-only, fail-closed) and ranks by cosine similarity. If Ollama is
  unreachable it **falls back to lexical**, so callers never break.

Other guarantees:
- **Trusted, confined corpus.** Documents are loaded through ``rag.ingest.ingest()``,
  which enforces an extension allow-list, rejects symlinks, and confines reads to the
  corpus root (path-traversal safe).
- **Fails soft.** A missing or unreadable corpus yields no references rather than an
  error, so the agent pipeline degrades gracefully.
"""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Literal

from rag.embeddings import OllamaEmbedder
from rag.ingest import Chunk, Embedder, ingest
from rag.retrieve import _cosine

from agents.tools.validation import ValidationError

RetrievalMode = Literal["lexical", "semantic"]

# Default location of the curated corpus, relative to the working directory.
DEFAULT_KB_ROOT = Path("knowledge-base")

# Tokenizer: lowercase alphanumeric words of length >= 3 (drops noise like "a", "of").
_TOKEN_RE = re.compile(r"[a-z0-9]{3,}")

# Common words that would otherwise inflate overlap scores without adding signal.
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
    }
)


def _tokenize(text: str) -> set[str]:
    """Return the set of meaningful lowercase tokens in ``text``."""
    return {tok for tok in _TOKEN_RE.findall(text.lower()) if tok not in _STOPWORDS}


@dataclass(frozen=True)
class KnowledgeReference:
    """A single retrieved knowledge-base reference with provenance."""

    source: str
    score: float
    snippet: str


class KnowledgeBaseAgent:
    """Retrieve relevant references from the local cybersecurity knowledge base."""

    def __init__(
        self,
        kb_root: Path | str = DEFAULT_KB_ROOT,
        *,
        snippet_chars: int = 160,
        mode: RetrievalMode = "lexical",
        embedder: Embedder | None = None,
    ) -> None:
        self.kb_root = Path(kb_root)
        self.snippet_chars = snippet_chars
        self.mode = mode
        # Injectable for tests; constructed lazily for semantic mode otherwise.
        self.embedder = embedder

    def retrieve(self, query: str, k: int = 3) -> list[KnowledgeReference]:
        """Return the top-``k`` knowledge-base documents most relevant to ``query``.

        Results are aggregated to one reference per source document, ranked by the
        document's best-scoring chunk, with a clean snippet drawn from the document's
        opening. Only positive-scoring documents are returned. In ``semantic`` mode,
        an unreachable embedder falls back to ``lexical`` so callers never break.
        """
        if k <= 0:
            raise ValidationError("k must be positive")
        if not query.strip():
            return []

        try:
            chunks = ingest(self.kb_root)
        except ValidationError:
            # Missing/unreadable corpus: fail soft with no references.
            return []
        if not chunks:
            return []

        openings = self._openings(chunks)

        if self.mode == "semantic":
            try:
                scores = self._semantic_scores(query, chunks)
                return self._aggregate(scores, openings, k)
            except ValidationError:
                # Ollama unreachable / fails closed -> graceful lexical fallback.
                pass

        return self._aggregate(self._lexical_scores(query, chunks), openings, k)

    def _openings(self, chunks: list[Chunk]) -> dict[str, str]:
        """Map each source to a clean snippet drawn from its opening chunk."""
        return {
            c.source: " ".join(c.text.split())[: self.snippet_chars] for c in chunks if c.index == 0
        }

    @staticmethod
    def _lexical_scores(query: str, chunks: list[Chunk]) -> dict[str, float]:
        """Best per-source term-overlap score (fraction of query terms present)."""
        query_terms = _tokenize(query)
        if not query_terms:
            return {}
        best: dict[str, float] = {}
        for chunk in chunks:
            chunk_terms = _tokenize(chunk.text)
            if not chunk_terms:
                continue
            score = len(query_terms & chunk_terms) / len(query_terms)
            if score > best.get(chunk.source, 0.0):
                best[chunk.source] = score
        return best

    def _semantic_scores(self, query: str, chunks: list[Chunk]) -> dict[str, float]:
        """Best per-source cosine similarity using the local embedder."""
        embedder = self.embedder or OllamaEmbedder()
        vectors = embedder.embed([query, *(c.text for c in chunks)])
        query_vec = vectors[0]
        best: dict[str, float] = {}
        for chunk, vec in zip(chunks, vectors[1:], strict=True):
            score = _cosine(query_vec, vec)
            if score > best.get(chunk.source, 0.0):
                best[chunk.source] = score
        return best

    @staticmethod
    def _aggregate(
        scores: dict[str, float], openings: dict[str, str], k: int
    ) -> list[KnowledgeReference]:
        """Build positive-scoring references, ranked high-first (stable by source)."""
        refs = [
            KnowledgeReference(source=source, score=score, snippet=openings.get(source, ""))
            for source, score in scores.items()
            if score > 0.0
        ]
        refs.sort(key=lambda ref: (-ref.score, ref.source))
        return refs[:k]

    def reference_for_event(
        self,
        soc_result: dict[str, Any],
        mitre_result: dict[str, Any] | None = None,
        k: int = 3,
    ) -> list[dict[str, Any]]:
        """Build a query from a SOC (+ optional MITRE) result and retrieve references.

        Returns plain dicts (via ``asdict``) so the output composes cleanly with the
        rest of the agent pipeline's JSON-serializable results.
        """
        parts: list[str] = []
        for key in ("event_type", "summary"):
            value = soc_result.get(key)
            if isinstance(value, str):
                parts.append(value)
        if mitre_result is not None:
            for key in ("tactic", "technique"):
                value = mitre_result.get(key)
                if isinstance(value, str):
                    parts.append(value)

        query = " ".join(parts)
        return [asdict(ref) for ref in self.retrieve(query, k=k)]


if __name__ == "__main__":
    agent = KnowledgeBaseAgent()
    for ref in agent.retrieve("brute force authentication failure credential access", k=3):
        print(f"[{ref.score:.2f}] {ref.source}: {ref.snippet}")
