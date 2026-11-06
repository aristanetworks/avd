# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""AVD-owned SQLite import, publication, and asset integration contracts."""

from __future__ import annotations

import importlib.util
import json
import sqlite3
from contextlib import closing
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parents[3]
GENERATE_PATH = REPO_ROOT / "tools" / "schema-explorer" / "generate.py"
SPEC = importlib.util.spec_from_file_location("schema_explorer_generate", GENERATE_PATH)
assert SPEC is not None
assert SPEC.loader is not None
GENERATE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GENERATE)


@pytest.fixture
def source_root(tmp_path: Path) -> Path:
    """Supply minimal named sources to exercise the real JSONL-to-SQLite pipeline."""
    root = tmp_path / "avd"
    for relative in GENERATE.SCHEMA_SOURCE_FILES.values():
        source = root / relative
        source.parent.mkdir(parents=True)
        source.write_text(
            json.dumps({"type": "dict", "keys": {"value": {"type": "bool", "default": False}}}),
            encoding="UTF-8",
        )
    return root


def test_build_imports_jsonl_with_browser_layout(source_root: Path, tmp_path: Path) -> None:
    out = tmp_path / "data" / "schema.sqlite"
    assert GENERATE.build(source_root, out) == dict.fromkeys(GENERATE.SCHEMA_IDS, 1)
    with closing(sqlite3.connect(out)) as connection:
        assert connection.execute("PRAGMA integrity_check").fetchone() == ("ok",)
        assert connection.execute("SELECT id, module, key_path, default_value, required, parent_path, depth FROM schema_vars ORDER BY id").fetchall() == [
            (1, "eos_designs", "value", "false", 0, "", 1),
            (2, "eos_cli_config_gen", "value", "false", 0, "", 1),
        ]
        assert connection.execute("SELECT module, var_count FROM schema_meta ORDER BY rowid").fetchall() == [(name, 1) for name in GENERATE.SCHEMA_IDS]
        assert all(isinstance(row[0], int) for row in connection.execute("SELECT loaded_at FROM schema_meta"))
        columns = [row[1] for row in connection.execute("PRAGMA table_info(schema_vars)")]
        assert columns == [
            "id",
            "module",
            "key_path",
            "var_type",
            "description",
            "default_value",
            "required",
            "primary_key",
            "unique_key",
            "parent_path",
            "depth",
            "doc_table",
            "deprecated",
            "removed",
            "cross_ref",
            "constraints",
        ]
        indexes = {row[1]: row[2] for row in connection.execute("PRAGMA index_list(schema_vars)")}
        assert indexes == {"idx_schema_unique": 1, "idx_schema_search": 0, "idx_schema_parent": 0, "idx_schema_doc_table": 0}


def test_build_replaces_database_without_cleaning_siblings(source_root: Path, tmp_path: Path) -> None:
    directory = tmp_path / "data"
    directory.mkdir()
    out = directory / "schema.sqlite"
    out.write_bytes(b"old database")
    sibling = directory / "preserved.txt"
    sibling.write_bytes(b"keep")
    GENERATE.build(source_root, out)
    with closing(sqlite3.connect(out)) as connection:
        assert connection.execute("SELECT COUNT(*) FROM schema_vars").fetchone() == (2,)
    assert sibling.read_bytes() == b"keep"
    assert set(directory.iterdir()) == {out, sibling}


def test_schema_failure_preserves_database(source_root: Path, tmp_path: Path) -> None:
    source = source_root / GENERATE.SCHEMA_SOURCE_FILES["eos_designs"]
    source.write_text(json.dumps({"type": "dict", "keys": {"broken": {"type": "dict", "$ref": "absent#"}}}), encoding="UTF-8")
    out = tmp_path / "schema.sqlite"
    out.write_bytes(b"old database")
    with pytest.raises(RuntimeError, match="absent"):
        GENERATE.build(source_root, out)
    assert out.read_bytes() == b"old database"
    assert not list(tmp_path.glob(".schema-explorer-*"))


def test_sqlite_failure_preserves_database(source_root: Path, tmp_path: Path) -> None:
    source = source_root / GENERATE.SCHEMA_SOURCE_FILES["eos_designs"]
    # Deliberately colliding Explorer paths reach the database's unique index.
    # This exercises import failure without adding instrumentation to production.
    source.write_text(
        json.dumps({"type": "dict", "keys": {"<selector.key>": {"type": "str"}}, "dynamic_keys": {"selector.key": {"type": "str"}}}),
        encoding="UTF-8",
    )
    out = tmp_path / "schema.sqlite"
    out.write_bytes(b"old database")
    with pytest.raises(sqlite3.IntegrityError):
        GENERATE.build(source_root, out)
    assert out.read_bytes() == b"old database"
    assert not list(tmp_path.glob(".schema-explorer-*"))


def test_static_assets_copy_is_independent_of_database(tmp_path: Path) -> None:
    database = tmp_path / "data" / "schema.sqlite"
    database.parent.mkdir()
    database.write_bytes(b"database")
    GENERATE._copy_static_assets(tmp_path)
    assert (tmp_path / "index.html").read_bytes() == (GENERATE.STATIC_DIR / "index.html").read_bytes()
    assert (tmp_path / "js" / "app.js").read_bytes() == (GENERATE.STATIC_DIR / "js" / "app.js").read_bytes()
    assert database.read_bytes() == b"database"
