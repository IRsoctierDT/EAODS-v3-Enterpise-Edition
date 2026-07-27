from __future__ import annotations

from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import hashlib
import json
import re
import uuid

from .io import write_json, write_text, write_yaml


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: str | Path) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def markdown_title(text: str, path: Path) -> str:
    fm = re.search(r"^---\n(.*?)\n---", text, re.S)
    if fm:
        for line in fm.group(1).splitlines():
            if line.lower().startswith("title:"):
                return line.split(":", 1)[1].strip().strip('"').strip("'")
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("_", " ").title()


def extract_frontmatter(text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    fm = re.search(r"^---\n(.*?)\n---", text, re.S)
    if not fm:
        return result
    for line in fm.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def extract_topics(text: str, limit: int = 8) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9_-]{3,}", text.lower())
    stop = {
        "this", "that", "with", "from", "have", "will", "should", "agent", "eaods",
        "workflow", "document", "section", "generated", "classification", "internal",
        "portfolio", "commercialization", "candidate", "version", "owner"
    }
    counts: dict[str, int] = {}
    for word in words:
        if word in stop:
            continue
        counts[word] = counts.get(word, 0) + 1
    return [w for w, _ in sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:limit]]


@dataclass
class DocumentRecord:
    document_id: str
    source_path: str
    title: str
    sha256: str
    word_count: int
    classification: str = "unknown"
    version: str = ""
    generated: str = ""
    reliability_score: int = 50
    stale: bool = False
    topics: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ChunkRecord:
    chunk_id: str
    document_id: str
    source_path: str
    title: str
    section_heading: str
    chunk_index: int
    sha256: str
    word_count: int
    classification: str
    topics: list[str]
    text: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def reliability_score_for(path: Path, text: str, frontmatter: dict[str, str]) -> int:
    score = 50
    lower = text.lower()

    if frontmatter:
        score += 10
    if "version" in frontmatter:
        score += 5
    if "generated" in frontmatter:
        score += 5
    if "owner" in frontmatter:
        score += 5
    if "qa checklist" in lower or "quality assurance" in lower:
        score += 10
    if "evidence" in lower:
        score += 5
    if "human review" in lower or "approval gate" in lower:
        score += 5
    if "source-code-appendices" in str(path).lower():
        score -= 10
    if any(x in lower for x in ["draft", "placeholder", "to be completed"]):
        score -= 10
    if any(x in lower for x in ["api_key=", "password=", "secret=", "token="]):
        score = 0

    return max(0, min(100, score))


def is_stale(path: Path, text: str, frontmatter: dict[str, str]) -> bool:
    lower = text.lower()
    if any(x in lower for x in ["deprecated", "superseded", "archived", "obsolete"]):
        return True
    # Alpha docs are not stale by default; this flags only explicit stale/deprecated language.
    return False


def inventory_documents(root: str | Path = ".", output: str | Path = "runtime/knowledge/registries/document_registry.json") -> Path:
    root = Path(root)
    records: list[dict[str, Any]] = []

    for p in sorted(root.rglob("*.md")):
        if ".git" in p.parts or "__pycache__" in p.parts:
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        fm = extract_frontmatter(text)
        title = markdown_title(text, p)
        record = DocumentRecord(
            document_id=f"DOC-{uuid.uuid5(uuid.NAMESPACE_URL, str(p.relative_to(root))).hex[:10].upper()}",
            source_path=str(p.relative_to(root)),
            title=title,
            sha256=sha256_text(text),
            word_count=len(text.split()),
            classification=fm.get("classification", "unknown"),
            version=fm.get("version", ""),
            generated=fm.get("generated", ""),
            reliability_score=reliability_score_for(p, text, fm),
            stale=is_stale(p, text, fm),
            topics=extract_topics(text),
        )
        records.append(record.to_dict())

    out = root / output
    write_json(out, {"generated": datetime.now(timezone.utc).isoformat(), "documents": records})
    return out


def split_markdown_sections(text: str) -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    current_heading = "Preamble"
    current_lines: list[str] = []

    for line in text.splitlines():
        if line.startswith("#"):
            if current_lines:
                sections.append((current_heading, "\n".join(current_lines).strip()))
                current_lines = []
            current_heading = line.lstrip("#").strip() or "Untitled Section"
        current_lines.append(line)

    if current_lines:
        sections.append((current_heading, "\n".join(current_lines).strip()))
    return sections


def chunk_text(section_text: str, max_words: int = 1000) -> list[str]:
    words = section_text.split()
    if not words:
        return []
    chunks = []
    for i in range(0, len(words), max_words):
        chunks.append(" ".join(words[i:i + max_words]))
    return chunks


def create_chunk_manifest(
    root: str | Path = ".",
    registry_path: str | Path = "runtime/knowledge/registries/document_registry.json",
    output: str | Path = "runtime/knowledge/chunks/chunk_manifest.json",
    include_text: bool = False,
) -> Path:
    root = Path(root)
    reg_path = root / registry_path
    if not reg_path.exists():
        inventory_documents(root, registry_path)
    registry = json.loads(reg_path.read_text(encoding="utf-8"))
    chunks: list[dict[str, Any]] = []

    for doc in registry.get("documents", []):
        source = root / doc["source_path"]
        if not source.exists():
            continue
        text = source.read_text(encoding="utf-8", errors="ignore")
        for section_heading, section_text in split_markdown_sections(text):
            for idx, chunk in enumerate(chunk_text(section_text)):
                rec = ChunkRecord(
                    chunk_id=f"CHK-{uuid.uuid5(uuid.NAMESPACE_URL, doc['source_path'] + section_heading + str(idx)).hex[:12].upper()}",
                    document_id=doc["document_id"],
                    source_path=doc["source_path"],
                    title=doc["title"],
                    section_heading=section_heading,
                    chunk_index=idx,
                    sha256=sha256_text(chunk),
                    word_count=len(chunk.split()),
                    classification=doc.get("classification", "unknown"),
                    topics=extract_topics(chunk),
                    text=chunk if include_text else "",
                )
                chunks.append(rec.to_dict())

    out = root / output
    write_json(out, {"generated": datetime.now(timezone.utc).isoformat(), "chunks": chunks})
    return out


def generate_staleness_report(
    root: str | Path = ".",
    registry_path: str | Path = "runtime/knowledge/registries/document_registry.json",
    output: str | Path = "runtime/knowledge/registries/staleness_report.md",
) -> Path:
    root = Path(root)
    reg_path = root / registry_path
    if not reg_path.exists():
        inventory_documents(root, registry_path)
    registry = json.loads(reg_path.read_text(encoding="utf-8"))

    md = """---
title: "EAODS Staleness Report"
version: "4.5.0-alpha"
---

# EAODS Staleness Report

| Document | Stale? | Reliability | Topics |
|---|---:|---:|---|
"""
    for doc in registry.get("documents", []):
        md += f"| `{doc['source_path']}` | {doc.get('stale', False)} | {doc.get('reliability_score', 0)} | {', '.join(doc.get('topics', [])[:5])} |\n"

    out = root / output
    write_text(out, md)
    return out


def generate_retrieval_qa(
    root: str | Path = ".",
    registry_path: str | Path = "runtime/knowledge/registries/document_registry.json",
    output: str | Path = "runtime/knowledge/retrieval_qa/retrieval_qa.json",
) -> Path:
    root = Path(root)
    reg_path = root / registry_path
    if not reg_path.exists():
        inventory_documents(root, registry_path)
    registry = json.loads(reg_path.read_text(encoding="utf-8"))

    qa = []
    for doc in registry.get("documents", [])[:100]:
        topics = doc.get("topics", [])
        topic = topics[0] if topics else doc["title"]
        qa.append({
            "question": f"Which EAODS document explains {topic}?",
            "expected_source": doc["source_path"],
            "expected_document_id": doc["document_id"],
            "minimum_reliability_score": doc.get("reliability_score", 0),
        })

    out = root / output
    write_json(out, {"generated": datetime.now(timezone.utc).isoformat(), "retrieval_qa": qa})
    return out


def export_knowledge_graph(
    root: str | Path = ".",
    registry_path: str | Path = "runtime/knowledge/registries/document_registry.json",
    output: str | Path = "runtime/knowledge/graphs/knowledge_graph.json",
) -> Path:
    root = Path(root)
    reg_path = root / registry_path
    if not reg_path.exists():
        inventory_documents(root, registry_path)
    registry = json.loads(reg_path.read_text(encoding="utf-8"))

    nodes = []
    edges = []
    topic_nodes: set[str] = set()

    for doc in registry.get("documents", []):
        doc_id = doc["document_id"]
        nodes.append({
            "id": doc_id,
            "type": "document",
            "label": doc["title"],
            "path": doc["source_path"],
            "reliability_score": doc.get("reliability_score", 0),
        })
        for topic in doc.get("topics", [])[:5]:
            tid = f"TOPIC-{topic}"
            if tid not in topic_nodes:
                nodes.append({"id": tid, "type": "topic", "label": topic})
                topic_nodes.add(tid)
            edges.append({"source": doc_id, "target": tid, "relationship": "mentions"})

    out = root / output
    write_json(out, {"generated": datetime.now(timezone.utc).isoformat(), "nodes": nodes, "edges": edges})
    return out


def build_memory_index(root: str | Path = ".", output: str | Path = "runtime/knowledge/memory_index.md") -> Path:
    root = Path(root)
    registry_path = root / "runtime/knowledge/registries/document_registry.json"
    if not registry_path.exists():
        inventory_documents(root)
    registry = json.loads(registry_path.read_text(encoding="utf-8"))

    md = """---
title: "EAODS Memory Index"
version: "4.5.0-alpha"
---

# EAODS Memory Index

## Highest Reliability Documents

| Score | Document | Topics |
|---:|---|---|
"""
    docs = sorted(registry.get("documents", []), key=lambda d: d.get("reliability_score", 0), reverse=True)
    for doc in docs[:50]:
        md += f"| {doc.get('reliability_score', 0)} | `{doc['source_path']}` | {', '.join(doc.get('topics', [])[:5])} |\n"

    md += "\n## Documents Requiring Review\n\n| Score | Document | Reason |\n|---:|---|---|\n"
    for doc in docs:
        if doc.get("stale") or doc.get("reliability_score", 0) < 60:
            reason = "stale" if doc.get("stale") else "low reliability"
            md += f"| {doc.get('reliability_score', 0)} | `{doc['source_path']}` | {reason} |\n"

    out = root / output
    write_text(out, md)
    return out
