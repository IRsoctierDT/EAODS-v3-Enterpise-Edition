from pathlib import Path

from eaods.artifact_factory import (
    ArtifactContext,
    generate_sop,
    generate_policy,
    generate_case_study,
    generate_client_deliverable,
    generate_portfolio_page,
    generate_evidence_binder,
    generate_release_bundle,
    generate_all_artifacts,
)


def test_generate_individual_artifacts(tmp_path):
    ctx = ArtifactContext(title="Test Artifact", purpose="Test purpose", scope="Test scope")
    funcs = [
        generate_sop,
        generate_policy,
        generate_case_study,
        generate_client_deliverable,
        generate_portfolio_page,
        generate_evidence_binder,
        generate_release_bundle,
    ]
    for func in funcs:
        path = func(ctx, tmp_path)
        assert path.exists()
        text = path.read_text(encoding="utf-8")
        assert "QA Checklist" in text
        assert "Human Review Gate" in text


def test_generate_all_artifacts(tmp_path):
    outputs = generate_all_artifacts("Full Artifact Set", output_root=tmp_path)
    assert len(outputs) == 7
    for path in outputs.values():
        assert Path(path).exists()
