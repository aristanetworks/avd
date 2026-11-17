# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""MkDocs rebuilds and publishes the explorer into its own output directory."""

from __future__ import annotations

import importlib.util
import json
import sqlite3
from contextlib import closing
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


def test_post_build_regenerates_explorer_in_site_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    source_root = tmp_path / "avd"
    site_dir = tmp_path / "site"
    monkeypatch.setattr(HOOK, "AVD_ROOT", source_root)
    schema_ids = ("eos_designs", "eos_cli_config_gen")
    sources = [source_root / "python-avd" / "pyavd" / f"_{schema_id}" / "schema" / f"{schema_id}.schema.yml" for schema_id in schema_ids]
    for source in sources:
        source.parent.mkdir(parents=True)
    site_dir.mkdir()
    page = site_dir / "index.html"
    page.write_text("MkDocs page", encoding="UTF-8")

    for key in ("before", "after"):
        for source in sources:
            source.write_text(json.dumps({"type": "dict", "keys": {key: {"type": "bool"}}}), encoding="UTF-8")
        HOOK.on_post_build({"site_dir": str(site_dir)})
        explorer = site_dir / HOOK.ASSET_SUBPATH
        with closing(sqlite3.connect(explorer / "data" / "schema.sqlite")) as connection:
            assert connection.execute("SELECT module, key_path FROM schema_vars ORDER BY id").fetchall() == [(schema_id, key) for schema_id in schema_ids]
        for relative in ("index.html", "css/style.css", "js/app.js", "vendor/sql.js/dist/sql-wasm.wasm"):
            assert (explorer / relative).is_file()
        assert page.read_text(encoding="UTF-8") == "MkDocs page"
