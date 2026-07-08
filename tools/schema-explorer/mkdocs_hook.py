# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
MkDocs hook for the AVD Schema Explorer.

Responsibilities:

1. **Markdown authoring interface.** Register a ``schema-explorer`` SuperFences
   formatter so docs authors can embed scoped explorers with Markdown fenced
   blocks instead of raw HTML.

2. **Asset publishing.** Copy the pre-built explorer (static assets + SQLite)
   from ``tools/schema-explorer/build/`` into
   ``<site_dir>/_assets/schema-explorer/``. The destination sits under
   ``_assets/`` because the explorer is embedded into arbitrary docs pages and
   the SPA assets are a shared site-wide resource.

3. **Global asset injection.** Append only the SPA's own ``style.css`` and
   ``app.js`` to ``extra_css`` / ``extra_javascript`` so every docs page gets
   the embed loader. Runtime dependencies are lazy-loaded only when an explorer
   mounts, so Material's chrome on plain docs pages is unaffected.

4. **Standalone route.** Copy the SPA ``index.html`` so the full-page experience
   stays reachable at ``/_assets/schema-explorer/index.html``.
"""

from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
from pathlib import Path
from types import ModuleType
from typing import Any

HERE = Path(__file__).resolve().parent
BUILD_DIR = HERE / "build"
STATIC_DIR = HERE / "static"
GENERATE_SCRIPT = HERE / "generate.py"
# Repo root is two levels up from tools/schema-explorer/.
AVD_ROOT = HERE.parents[1]
SCHEMA_INPUTS = (
    AVD_ROOT / "python-avd" / "pyavd" / "_eos_designs" / "schema" / "eos_designs.schema.yml",
    AVD_ROOT / "python-avd" / "pyavd" / "_eos_cli_config_gen" / "schema" / "eos_cli_config_gen.schema.yml",
)
FORMATTER_SCRIPT = AVD_ROOT / "tools" / "schema_explorer_markdown.py"
FORMATTER_MODULE = "_avd_schema_explorer_markdown"
ASSET_SUBPATH = "_assets/schema-explorer"
# Only the SPA's own style.css + app.js are registered globally. Bootstrap
# CSS/JS + Bootstrap Icons + sql.js are lazy-loaded by app.js at runtime
# when (and only when) the page actually hosts a <schema-explorer> embed
# or the standalone SPA — otherwise Bootstrap's body-level rules (link
# underlines, heading sizes, line-height) would leak into Material's chrome
# on every docs page even those without an embed.
CSS_FILES = (f"{ASSET_SUBPATH}/css/style.css",)
JS_FILES = (f"{ASSET_SUBPATH}/js/app.js",)


def _iter_static_files() -> tuple[Path, ...]:
    """Return all static SPA files that affect the generated build tree."""
    if not STATIC_DIR.is_dir():
        return ()
    return tuple(path for path in STATIC_DIR.rglob("*") if path.is_file())


def _load_formatter() -> Any:
    """Load the Markdown formatter from a local file path."""
    module = sys.modules.get(FORMATTER_MODULE)
    if not isinstance(module, ModuleType):
        spec = importlib.util.spec_from_file_location(FORMATTER_MODULE, FORMATTER_SCRIPT)
        if spec is None or spec.loader is None:
            msg = f"Unable to load Schema Explorer Markdown formatter from {FORMATTER_SCRIPT}"
            raise RuntimeError(msg)
        module = importlib.util.module_from_spec(spec)
        sys.modules[FORMATTER_MODULE] = module
        spec.loader.exec_module(module)
    return module.schema_explorer_fence_format


def _ensure_markdown_fence(config: dict[str, Any]) -> None:
    """Register the ``schema-explorer`` SuperFences formatter."""
    markdown_extensions = list(config.get("markdown_extensions") or [])
    if "pymdownx.superfences" not in markdown_extensions:
        markdown_extensions.append("pymdownx.superfences")

    mdx_configs = dict(config.get("mdx_configs") or {})
    fence_config = dict(mdx_configs.get("pymdownx.superfences") or {})
    custom_fences = list(fence_config.get("custom_fences") or [])

    if not any(fence.get("name") == "schema-explorer" for fence in custom_fences if isinstance(fence, dict)):
        custom_fences.append(
            {
                "name": "schema-explorer",
                "class": "schema-explorer",
                "format": _load_formatter(),
            },
        )

    fence_config["custom_fences"] = custom_fences
    mdx_configs["pymdownx.superfences"] = fence_config
    config["markdown_extensions"] = markdown_extensions
    config["mdx_configs"] = mdx_configs


def _copy_static_assets() -> None:
    """Copy the latest static SPA assets into the build directory."""
    if not STATIC_DIR.is_dir():
        msg = f"Static asset dir not found: {STATIC_DIR}"
        raise FileNotFoundError(msg)
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    for entry in STATIC_DIR.iterdir():
        target = BUILD_DIR / entry.name
        if entry.is_dir():
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(entry, target)
        else:
            shutil.copy2(entry, target)


def _database_is_current(sqlite_marker: Path) -> bool:
    """Return True when the generated SQLite is newer than build inputs."""
    if not sqlite_marker.is_file():
        return False
    sqlite_mtime = sqlite_marker.stat().st_mtime
    input_paths = (GENERATE_SCRIPT, *SCHEMA_INPUTS, *_iter_static_files())
    return all(path.is_file() and path.stat().st_mtime <= sqlite_mtime for path in input_paths)


def _ensure_build() -> None:
    """
    Build the Schema Explorer if ``build/`` is missing.

    Hosts that do not run ``make schema-explorer-build`` first, such as the
    ReadTheDocs build pipeline, would otherwise end up with missing
    ``_assets/schema-explorer/*`` URLs. Running the generator on demand from the
    hook makes the SPA self-publishing for any host that can run ``mkdocs build``.
    """
    sqlite_marker = BUILD_DIR / "data" / "schema.sqlite"
    if _database_is_current(sqlite_marker):
        _copy_static_assets()
        return
    reason = "missing" if not sqlite_marker.is_file() else "stale"
    print(f"[schema-explorer] build/ {reason} — running generate.py")
    subprocess.check_call(  # noqa: S603
        [
            sys.executable,
            str(GENERATE_SCRIPT),
            "--avd-root",
            str(AVD_ROOT),
            "--site-dir",
            str(BUILD_DIR),
        ],
    )


def on_config(config: dict[str, Any], **kwargs: Any) -> dict[str, Any]:  # noqa: ARG001
    """Register the Markdown fence, build the SPA, then register CSS/JS."""
    _ensure_markdown_fence(config)
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


EXPECTED_BUILD_FILES = ("index.html",)
EXPECTED_BUILD_DIRS = ("css", "js", "vendor")
EXPECTED_DATA_FILES = ("schema.sqlite",)


def _copy_expected_build_artifacts(dest: Path) -> None:
    """Copy only the expected Schema Explorer build artifacts."""
    dest.mkdir(parents=True, exist_ok=True)
    for filename in EXPECTED_BUILD_FILES:
        source = BUILD_DIR / filename
        if not source.is_file():
            msg = f"Required Schema Explorer build file missing: {source}"
            raise FileNotFoundError(msg)
        shutil.copy2(source, dest / filename)

    for dirname in EXPECTED_BUILD_DIRS:
        source = BUILD_DIR / dirname
        if not source.is_dir():
            msg = f"Required Schema Explorer build directory missing: {source}"
            raise FileNotFoundError(msg)
        shutil.copytree(source, dest / dirname)

    data_source = BUILD_DIR / "data"
    data_dest = dest / "data"
    data_dest.mkdir(parents=True, exist_ok=True)
    for filename in EXPECTED_DATA_FILES:
        source = data_source / filename
        if not source.is_file():
            msg = f"Required Schema Explorer data file missing: {source}"
            raise FileNotFoundError(msg)
        shutil.copy2(source, data_dest / filename)


def on_post_build(config: dict[str, Any], **kwargs: Any) -> None:  # noqa: ARG001
    """Copy the built Schema Explorer into the generated site."""
    if not BUILD_DIR.is_dir():
        return
    dest = Path(config["site_dir"]) / ASSET_SUBPATH
    if dest.exists():
        shutil.rmtree(dest)
    _copy_expected_build_artifacts(dest)
