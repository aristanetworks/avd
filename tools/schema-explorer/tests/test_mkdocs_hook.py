# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Tests for allowlisted Schema Explorer artifact publishing."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from types import ModuleType

AVD_ROOT = Path(__file__).resolve().parents[3]
HOOK_PATH = AVD_ROOT / "tools" / "schema-explorer" / "mkdocs_hook.py"


def _load_hook_module() -> ModuleType:
    spec = importlib.util.spec_from_file_location("schema_explorer_mkdocs_hook_under_test", HOOK_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _write_minimal_build_tree(build_dir: Path) -> None:
    build_dir.mkdir(parents=True, exist_ok=True)
    (build_dir / "index.html").write_text("<html></html>", encoding="utf-8")
    (build_dir / "css").mkdir()
    (build_dir / "css" / "style.css").write_text("/* test */", encoding="utf-8")
    (build_dir / "js").mkdir()
    (build_dir / "js" / "app.js").write_text("// test", encoding="utf-8")
    (build_dir / "vendor").mkdir()
    (build_dir / "vendor" / "placeholder.txt").write_text("vendor", encoding="utf-8")
    (build_dir / "data").mkdir()
    (build_dir / "data" / "schema.sqlite").write_bytes(b"SQLite format 3\x00")
    (build_dir / "unexpected-extra.txt").write_text("must not publish", encoding="utf-8")


def test_copy_expected_build_artifacts_publishes_allowlist_only(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    module = _load_hook_module()
    build_dir = tmp_path / "build"
    dest_dir = tmp_path / "site" / "_assets" / "schema-explorer"
    _write_minimal_build_tree(build_dir)
    monkeypatch.setattr(module, "BUILD_DIR", build_dir)

    module._copy_expected_build_artifacts(dest_dir)

    assert (dest_dir / "index.html").is_file()
    assert (dest_dir / "data" / "schema.sqlite").is_file()
    assert (dest_dir / "js" / "app.js").is_file()
    assert not (dest_dir / "unexpected-extra.txt").exists()


def test_copy_expected_build_artifacts_fails_when_required_sqlite_missing(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    module = _load_hook_module()
    build_dir = tmp_path / "build"
    dest_dir = tmp_path / "dest"
    _write_minimal_build_tree(build_dir)
    (build_dir / "data" / "schema.sqlite").unlink()
    monkeypatch.setattr(module, "BUILD_DIR", build_dir)

    with pytest.raises(FileNotFoundError, match=r"schema\.sqlite"):
        module._copy_expected_build_artifacts(dest_dir)
