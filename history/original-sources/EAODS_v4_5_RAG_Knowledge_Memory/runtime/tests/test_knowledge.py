from pathlib import Path
import json

from eaods.knowledge import (
    inventory_documents,
    create_chunk_manifest,
    generate_staleness_report,
    generate_retrieval_qa,
    export_knowledge_graph,
    build_memory_index,
)


def test_knowledge_inventory_and_outputs(tmp_path):
    (tmp_path / "Docs").mkdir()
    (tmp_path / "Docs" / "test.md").write_text("""---
title: "Test Knowledge"
version: "1.0"
owner: "Tester"
classification: "Internal"
---

# Test Knowledge

## Mission

This document explains knowledge memory evidence retrieval and governance.

## QA Checklist

- [ ] Check evidence.

## Human Review

Approval gate required.
""", encoding="utf-8")

    reg = inventory_documents(tmp_path)
    assert reg.exists()
    data = json.loads(reg.read_text(encoding="utf-8"))
    assert len(data["documents"]) == 1
    assert data["documents"][0]["reliability_score"] >= 70

    chunks = create_chunk_manifest(tmp_path)
    assert chunks.exists()
    chunk_data = json.loads(chunks.read_text(encoding="utf-8"))
    assert len(chunk_data["chunks"]) >= 1

    stale = generate_staleness_report(tmp_path)
    assert stale.exists()

    qa = generate_retrieval_qa(tmp_path)
    assert qa.exists()

    graph = export_knowledge_graph(tmp_path)
    assert graph.exists()

    memory = build_memory_index(tmp_path)
    assert memory.exists()
    assert "Highest Reliability Documents" in memory.read_text(encoding="utf-8")
