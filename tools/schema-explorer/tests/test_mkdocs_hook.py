# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Cache invalidation belongs to the AVD documentation integration."""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
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


def test_editable_extension_timestamp_invalidates_cache(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    extension = tmp_path / "bindings.so"
    extension.touch()
    sqlite_marker = tmp_path / "schema.sqlite"
    sqlite_marker.touch()
    sqlite_marker.with_suffix(".generator-version").write_text("example-version", encoding="UTF-8")
    monkeypatch.setattr(HOOK, "_schema_input_paths", lambda: (extension,))
    monkeypatch.setattr(HOOK, "_iter_static_files", lambda: ())
    monkeypatch.setattr(HOOK, "version", lambda _package: "example-version")
    assert HOOK._database_is_current(sqlite_marker)
    newer = sqlite_marker.stat().st_mtime + 10
    os.utime(extension, (newer, newer))
    assert not HOOK._database_is_current(sqlite_marker)


def test_missing_database_is_not_current(tmp_path: Path) -> None:
    assert not HOOK._database_is_current(tmp_path / "absent.sqlite")
