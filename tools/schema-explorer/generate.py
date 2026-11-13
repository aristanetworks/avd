# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Build the SQLite-backed AVD Schema Explorer and publish its static assets.

pyavd-utils-gen interprets the combined source schemas and exports ordered field
occurrences as JSON Lines. This script owns the browser's SQLite format: tables,
indexes, row IDs, JSON-text columns, and generation timestamps. Static assets
remain independent of schema interpretation.

The standalone CLI writes under --site-dir. The MkDocs hook uses a cache outside
the repository and copies the bundle into the built site's _assets directory.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sqlite3
import sys
import tempfile
import time
from contextlib import closing
from pathlib import Path

from pyavd_utils_gen.schema_generation import generate_schema_explorer_jsonl_from_paths

SCHEMA_IDS = ("eos_designs", "eos_cli_config_gen")
SCHEMA_SOURCE_FILES = {
    "eos_cli_config_gen": Path("python-avd/pyavd/_eos_cli_config_gen/schema/eos_cli_config_gen.schema.yml"),
    "eos_designs": Path("python-avd/pyavd/_eos_designs/schema/eos_designs.schema.yml"),
}
HERE = Path(__file__).resolve().parent
STATIC_DIR = HERE / "static"


def _create_schema(conn: sqlite3.Connection) -> None:
    """Create the database contract consumed by the browser's SQL queries."""
    conn.execute("""
        CREATE TABLE schema_vars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            module TEXT NOT NULL,
            key_path TEXT NOT NULL,
            var_type TEXT,
            description TEXT,
            default_value TEXT,
            required INTEGER DEFAULT 0,
            primary_key INTEGER DEFAULT 0,
            unique_key INTEGER DEFAULT 0,
            parent_path TEXT,
            depth INTEGER DEFAULT 0,
            doc_table TEXT DEFAULT '',
            deprecated INTEGER DEFAULT 0,
            removed INTEGER DEFAULT 0,
            cross_ref TEXT,
            constraints TEXT
        )
    """)
    conn.execute("CREATE UNIQUE INDEX idx_schema_unique ON schema_vars(module, key_path)")
    conn.execute("CREATE INDEX idx_schema_search ON schema_vars(key_path, module)")
    conn.execute("CREATE INDEX idx_schema_parent ON schema_vars(module, parent_path)")
    conn.execute("CREATE INDEX idx_schema_doc_table ON schema_vars(module, doc_table)")
    conn.execute("""
        CREATE TABLE schema_meta (
            module TEXT NOT NULL,
            loaded_at INTEGER,
            var_count INTEGER,
            PRIMARY KEY (module)
        )
    """)


def _database_row(line: str) -> dict:
    """Encode JSON-valued columns as text; SQLite stores JSON booleans as integers."""
    row = json.loads(line)
    for column in ("default_value", "constraints"):
        value = row[column]
        row[column] = json.dumps(value) if value is not None else None
    return row


def build(avd_root: Path, out: Path) -> dict[str, int]:
    """
    Export schema occurrences and atomically publish the browser database.

    Only the requested database is replaced. Existing output remains available
    if schema generation or database construction fails, and sibling files are
    never cleaned. The SQLite connection is closed before replacement on Windows.
    """
    out.parent.mkdir(parents=True, exist_ok=True)
    sources = {schema_id: avd_root / source_path for schema_id, source_path in SCHEMA_SOURCE_FILES.items()}
    print(f"  exporting schemas from {avd_root}/python-avd")
    with tempfile.TemporaryDirectory(prefix=".schema-explorer-", dir=out.parent) as temporary_dir:
        temporary = Path(temporary_dir)
        jsonl = temporary / "schema.jsonl"
        counts = generate_schema_explorer_jsonl_from_paths(sources, list(SCHEMA_IDS), jsonl)
        tmp_out = temporary / "schema.sqlite"
        with closing(sqlite3.connect(tmp_out)) as conn, conn:
            _create_schema(conn)
            with jsonl.open(encoding="UTF-8") as stream:
                conn.executemany(
                    """INSERT INTO schema_vars
                           (module, key_path, var_type, description, default_value,
                            required, primary_key, unique_key, parent_path, depth, doc_table, deprecated,
                            removed, cross_ref, constraints)
                           VALUES (:module, :key_path, :var_type, :description,
                                   :default_value, :required, :primary_key, :unique_key, :parent_path, :depth,
                                   :doc_table, :deprecated, :removed, :cross_ref, :constraints)""",
                    (_database_row(line) for line in stream),
                )
            loaded_at = int(time.time())
            # Use the requested module order, independent of Python/Rust map iteration.
            conn.executemany(
                "INSERT INTO schema_meta (module, loaded_at, var_count) VALUES (?, ?, ?)",
                [(name, loaded_at, counts[name]) for name in SCHEMA_IDS],
            )
        tmp_out.replace(out)
    for module in SCHEMA_IDS:
        print(f"    {module}: {counts[module]} variables")
    return counts


def _copy_static_assets(site_dir: Path) -> None:
    """Copy index.html / css/ / js/ from static/ into site_dir."""
    if not STATIC_DIR.is_dir():
        msg = f"Static asset dir not found: {STATIC_DIR}"
        raise FileNotFoundError(msg)
    site_dir.mkdir(parents=True, exist_ok=True)
    for entry in STATIC_DIR.iterdir():
        target = site_dir / entry.name
        if entry.is_dir():
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(entry, target)
        else:
            shutil.copy2(entry, target)
    print(f"  copied static assets → {site_dir}")


def main() -> int:
    """Build the SQLite database and static assets for a standalone or MkDocs site."""
    parser = argparse.ArgumentParser(description=(__doc__ or "").strip().splitlines()[0])
    parser.add_argument("--avd-root", type=Path, required=True, help="Path to the avd repo root (the directory containing python-avd/)")
    parser.add_argument(
        "--site-dir",
        type=Path,
        required=True,
        help="Output directory for the built explorer. Static assets are copied here and SQLite is written under data/schema.sqlite.",
    )
    args = parser.parse_args()
    site_dir = args.site_dir.resolve()
    print("Building Schema Explorer")
    sqlite_out = site_dir / "data" / "schema.sqlite"
    counts = build(args.avd_root.resolve(), sqlite_out)
    _copy_static_assets(site_dir)
    total = sum(counts.values())
    print(f"Wrote {sqlite_out} ({total} variables across {len(counts)} modules)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
