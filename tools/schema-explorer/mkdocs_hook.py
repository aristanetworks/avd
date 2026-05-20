# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
MkDocs hook for the AVD Schema Explorer.

Responsibilities:

1. **Asset publishing.** Copy the pre-built explorer (static assets + SQLite)
   from ``tools/schema-explorer/build/`` into ``<site_dir>/_assets/schema-explorer/``.
   The destination sits under ``_assets/`` (not ``docs/``) because the
   explorer is no longer a single full-page route — it is embedded into
   arbitrary docs pages via the ``<schema-explorer>`` custom HTML element,
   and the SPA assets are a shared site-wide resource.

2. **Global asset injection.** Append the SPA's CSS and JS to ``extra_css`` /
   ``extra_javascript`` so every docs page gets the loader. The loader
   short-circuits on pages that do not contain a ``<schema-explorer>``
   element, so the per-page cost is just the unfired script bytes.

3. **Standalone route.** The hook also copies the SPA ``index.html`` so the
   full-page experience stays reachable at ``/_assets/schema-explorer/index.html``.

Build the artifact first with ``make schema-explorer-build`` (or via the
docs container's entrypoint). If the build directory is missing, the hook
is a no-op so a bare ``mkdocs build`` still succeeds — the embeds just
render an empty placeholder.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
BUILD_DIR = HERE / "build"
GENERATE_SCRIPT = HERE / "generate.py"
# Repo root is two levels up from tools/schema-explorer/.
AVD_ROOT = HERE.parents[1]
DEFAULT_RELEASE = "devel"
ASSET_SUBPATH = "_assets/schema-explorer"
# The SPA was built on Bootstrap 5 + Bootstrap Icons. Inject them globally
# so embeds render with their existing markup on any docs page. Style scoping
# (so Bootstrap's body-level rules don't bleed into Material's typography)
# lives in tools/schema-explorer/static/css/style.css under .schema-embed
# / .schema-spa-host scopes.
CSS_FILES = (
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
    "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css",
    f"{ASSET_SUBPATH}/css/style.css",
)
JS_FILES = (
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js",
    "https://cdn.jsdelivr.net/npm/sql.js@1.10.3/dist/sql-wasm.js",
    f"{ASSET_SUBPATH}/js/app.js",
)


def _ensure_build() -> None:
    """
    Build the Schema Explorer if ``build/`` is missing.

    Hosts that don't run ``make schema-explorer-build`` first — e.g. the
    ReadTheDocs build pipeline, which only invokes ``mkdocs build`` — would
    otherwise end up with the hook copying nothing into ``site/`` and every
    ``_assets/schema-explorer/*`` URL returning 404. Running the generator
    on demand from the hook makes the SPA self-publishing: any host that
    can run ``mkdocs build`` gets the explorer for free.
    """
    sqlite_marker = BUILD_DIR / "data" / DEFAULT_RELEASE / "schema.sqlite"
    if sqlite_marker.is_file():
        return
    print(f"[schema-explorer] build/ missing — running generate.py for release={DEFAULT_RELEASE}")
    subprocess.check_call(  # noqa: S603
        [
            sys.executable,
            str(GENERATE_SCRIPT),
            "--avd-root",
            str(AVD_ROOT),
            "--release",
            DEFAULT_RELEASE,
            "--site-dir",
            str(BUILD_DIR),
        ],
    )


def on_config(config: dict[str, Any], **kwargs: Any) -> dict[str, Any]:  # noqa: ARG001
    """Build the SPA if needed, then register its CSS/JS globally."""
    _ensure_build()
    extra_css = list(config.get("extra_css") or [])
    extra_js = list(config.get("extra_javascript") or [])
    for href in CSS_FILES:
        if href not in extra_css:
            extra_css.append(href)
    for href in JS_FILES:
        if href not in extra_js:
            extra_js.append(href)
    config["extra_css"] = extra_css
    config["extra_javascript"] = extra_js
    return config


def on_post_build(config: dict[str, Any], **kwargs: Any) -> None:  # noqa: ARG001
    if not BUILD_DIR.is_dir():
        return
    dest = Path(config["site_dir"]) / ASSET_SUBPATH
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(BUILD_DIR, dest)
