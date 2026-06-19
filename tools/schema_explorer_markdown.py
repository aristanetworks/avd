# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Markdown helpers for embedding the AVD Schema Explorer in MkDocs pages."""

from __future__ import annotations

from html import escape
from typing import Any

import yaml

_ALLOWED_ATTRIBUTES = frozenset({"release", "module", "root", "view", "height", "chrome"})
_ALLOWED_MODULES = frozenset({"eos_designs", "eos_cli_config_gen", "all"})
_ALLOWED_VIEWS = frozenset({"tree", "flat", "yaml"})
_ALLOWED_CHROME = frozenset({"compact", "none"})
_DEFAULTS = {
    "release": "devel",
    "module": "eos_designs",
    "view": "tree",
    "height": "600px",
    "chrome": "compact",
}


def _load_options(source: str) -> dict[str, str]:
    """Load and validate a schema-explorer fence body."""
    data = yaml.safe_load(source) if source.strip() else {}
    if data is None:
        data = {}
    if not isinstance(data, dict):
        msg = "schema-explorer fence content must be a YAML mapping"
        raise TypeError(msg)

    unknown = set(data) - _ALLOWED_ATTRIBUTES
    if unknown:
        allowed = ", ".join(sorted(_ALLOWED_ATTRIBUTES))
        unknown_values = ", ".join(sorted(str(key) for key in unknown))
        msg = f"Unsupported schema-explorer option(s): {unknown_values}. Allowed options: {allowed}"
        raise ValueError(msg)

    options = {**_DEFAULTS, **{str(key): str(value) for key, value in data.items() if value is not None}}
    if options["module"] not in _ALLOWED_MODULES:
        msg = "schema-explorer 'module' must be one of: " + ", ".join(sorted(_ALLOWED_MODULES))
        raise ValueError(msg)
    if options["view"] not in _ALLOWED_VIEWS:
        msg = "schema-explorer 'view' must be one of: " + ", ".join(sorted(_ALLOWED_VIEWS))
        raise ValueError(msg)
    if options["chrome"] not in _ALLOWED_CHROME:
        msg = "schema-explorer 'chrome' must be one of: " + ", ".join(sorted(_ALLOWED_CHROME))
        raise ValueError(msg)
    return options


def schema_explorer_fence_format(source: str, language: str, class_name: str, options: dict[str, Any], md: Any, **kwargs: Any) -> str:
    """Render a ``schema-explorer`` SuperFences block as a custom element."""
    del language, options, md, kwargs
    attrs = _load_options(source)
    html_attrs = " ".join(f'{name}="{escape(value, quote=True)}"' for name, value in attrs.items() if value)
    classes = "schema-explorer-markdown"
    if class_name:
        classes += f" {escape(class_name, quote=True)}"
    return f'<div class="{classes}"><schema-explorer {html_attrs}></schema-explorer></div>'
