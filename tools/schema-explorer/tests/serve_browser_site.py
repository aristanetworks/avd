# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Build a minimal real MkDocs site and serve it for browser integration tests."""

from __future__ import annotations

import functools
import http.server
import shutil
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
PAYLOAD = '<img src=x onerror="window.schemaExplorerXss=true">'


def main() -> None:
    """Exercise the actual MkDocs hook, formatter, asset publishing and database."""
    with tempfile.TemporaryDirectory(prefix="avd-schema-explorer-browser-") as directory:
        work = Path(directory)
        docs = work / "docs"
        docs.mkdir()
        (docs / "index.md").write_text(
            "# Browser integration fixture\n\n```schema-explorer\nmodule: eos_designs\nroot: fabric_name\n```\n",
        )
        (docs / "yaml.md").write_text(
            "# YAML embed fixture\n\n```schema-explorer\nmodule: eos_designs\nroot: fabric_name\nview: yaml\n```\n",
        )
        (docs / "plain.md").write_text("# Plain documentation page\n")
        logo = docs / "docs/_media/arista-avd-logo-white.png"
        logo.parent.mkdir(parents=True)
        shutil.copy2(ROOT / "docs/_media/arista-avd-logo-white.png", logo)
        config = work / "mkdocs.yml"
        config.write_text(
            yaml.safe_dump(
                {
                    "site_name": "Schema Explorer browser tests",
                    "theme": {"name": "material", "font": False},
                    "docs_dir": str(docs),
                    "site_dir": str(work / "site"),
                    "hooks": [str(ROOT / "tools/schema-explorer/mkdocs_hook.py")],
                    "markdown_extensions": ["pymdownx.superfences"],
                }
            )
        )
        subprocess.run([sys.executable, "-m", "mkdocs", "build", "--strict", "-f", str(config)], check=True)  # noqa: S603
        # Test escaping through the real SQLite -> sql.js -> DOM path, without
        # changing the production schema or the hook's reusable build cache.
        database = work / "site/_assets/schema-explorer/data/schema.sqlite"
        with sqlite3.connect(database) as connection:
            connection.execute("UPDATE schema_vars SET description = ? WHERE module = ? AND key_path = ?", (PAYLOAD, "eos_designs", "fabric_name"))
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(work / "site"))
        with http.server.ThreadingHTTPServer(("127.0.0.1", 8765), handler) as server:
            server.serve_forever()


if __name__ == "__main__":
    main()
