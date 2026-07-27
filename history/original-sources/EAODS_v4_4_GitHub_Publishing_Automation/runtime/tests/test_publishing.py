from pathlib import Path
from eaods.publishing import (
    generate_repository_map,
    generate_mkdocs_nav,
    generate_changelog,
    generate_issue,
    generate_pr,
    create_public_private_bundles,
)


def test_repository_map(tmp_path):
    (tmp_path / "README.md").write_text("# Test\n", encoding="utf-8")
    path = generate_repository_map(tmp_path)
    assert path.exists()
    assert "README.md" in path.read_text(encoding="utf-8")


def test_mkdocs_nav(tmp_path):
    (tmp_path / "README.md").write_text("# Home\n", encoding="utf-8")
    (tmp_path / "Docs").mkdir()
    (tmp_path / "Docs" / "a.md").write_text("---\ntitle: A Doc\n---\n# A\n", encoding="utf-8")
    path = generate_mkdocs_nav(tmp_path)
    assert path.exists()
    assert "A Doc" in path.read_text(encoding="utf-8")


def test_changelog(tmp_path):
    (tmp_path / "Release-Notes").mkdir()
    (tmp_path / "Release-Notes" / "v.md").write_text("# Version\n\n- Added test\n", encoding="utf-8")
    path = generate_changelog(tmp_path)
    assert path.exists()
    assert "Added test" in path.read_text(encoding="utf-8")


def test_issue_and_pr(tmp_path):
    issue = generate_issue("Test Issue", "Body", tmp_path)
    pr = generate_pr("Test PR", "Summary", tmp_path)
    assert issue.exists()
    assert pr.exists()


def test_public_private_bundles(tmp_path):
    (tmp_path / "public.md").write_text("# Public\n", encoding="utf-8")
    (tmp_path / "secret.md").write_text("api_key=abc", encoding="utf-8")
    result = create_public_private_bundles(tmp_path, "vtest", "artifacts")
    assert Path(result["public_bundle"]).exists()
    assert Path(result["private_bundle"]).exists()
