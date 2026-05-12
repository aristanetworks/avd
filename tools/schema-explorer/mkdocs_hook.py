# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
MkDocs hook: copy the pre-built Schema Explorer (static assets + SQLite) from
``tools/schema-explorer/build/`` into ``<site_dir>/docs/schema-explorer/`` so
the generated artifact never lives under the source-controlled ``docs/``.

The destination uses ``docs/schema-explorer/`` (matching the rest of the
site's URL space, which is rooted under ``docs/`` because ``mkdocs.yml`` has
``docs_dir: .``) so wrapper pages and the template-override variant can
reference paths like ``docs/schema-explorer/index.html`` without changing.

Build the artifact first with ``make schema-explorer-build`` (or via the
docs container's entrypoint). If the build directory is missing, the hook
is a no-op so a bare ``mkdocs build`` still succeeds — the explorer just
won't be present in the output.
"""

from __future__ import annotations

import shutil
from pathlib import Path

BUILD_DIR = Path(__file__).resolve().parent / "build"


def on_post_build(config, **kwargs):  # noqa: ARG001
    if not BUILD_DIR.is_dir():
        return
    dest = Path(config["site_dir"]) / "docs" / "schema-explorer"
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(BUILD_DIR, dest)
