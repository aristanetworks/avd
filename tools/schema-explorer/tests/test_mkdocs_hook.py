# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Cache invalidation belongs to the AVD documentation integration."""

from __future__ import annotations

import importlib.util
import subprocess
from pathlib import Path

import pytest

HOOK_PATH = Path(__file__).parents[1] / "mkdocs_hook.py"
SPEC = importlib.util.spec_from_file_location("schema_explorer_mkdocs_hook", HOOK_PATH)
assert SPEC is not None
assert SPEC.loader is not None
HOOK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(HOOK)


def test_cache_requires_matching_generator_version(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    sqlite_marker = tmp_path / "schema.sqlite"
    sqlite_marker.touch()
    monkeypatch.setattr(HOOK, "_schema_input_paths", lambda: ())
    monkeypatch.setattr(HOOK, "_iter_static_files", lambda: ())
    monkeypatch.setattr(HOOK, "version", lambda _package: "example-version")
    assert not HOOK._database_is_current(sqlite_marker)
    version_marker = sqlite_marker.with_suffix(".generator-version")
    version_marker.write_text("example-version", encoding="UTF-8")
    assert HOOK._database_is_current(sqlite_marker)
    version_marker.write_text("old-version", encoding="UTF-8")
    assert not HOOK._database_is_current(sqlite_marker)


def test_missing_database_is_not_current(tmp_path: Path) -> None:
    assert not HOOK._database_is_current(tmp_path / "absent.sqlite")


@pytest.mark.parametrize("returncode", [0, 1])
def test_regeneration_updates_marker_only_after_success(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, returncode: int) -> None:
    sqlite_marker = tmp_path / "data" / "schema.sqlite"
    sqlite_marker.parent.mkdir()
    sqlite_marker.write_bytes(b"old database")
    version_marker = sqlite_marker.with_suffix(".generator-version")
    version_marker.write_text("old-version", encoding="UTF-8")
    monkeypatch.setattr(HOOK, "BUILD_DIR", tmp_path)
    monkeypatch.setattr(HOOK, "_schema_input_paths", lambda: ())
    monkeypatch.setattr(HOOK, "_iter_static_files", lambda: ())
    monkeypatch.setattr(HOOK, "version", lambda _package: "new-version")

    def regenerate(command: list[str]) -> None:
        # Asset publication can fail after the database has been replaced.
        sqlite_marker.write_bytes(b"new database")
        if returncode:
            raise subprocess.CalledProcessError(returncode, command)

    monkeypatch.setattr(HOOK.subprocess, "check_call", regenerate)
    if returncode:
        with pytest.raises(subprocess.CalledProcessError):
            HOOK._ensure_build()
        assert not version_marker.exists()
        monkeypatch.setattr(HOOK, "version", lambda _package: "old-version")
        assert not HOOK._database_is_current(sqlite_marker)
    else:
        HOOK._ensure_build()
        assert version_marker.read_text(encoding="UTF-8") == "new-version"
        assert HOOK._database_is_current(sqlite_marker)
