# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Tests for the Schema Explorer MkDocs SuperFences formatter."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

AVD_ROOT = Path(__file__).resolve().parents[3]
FORMATTER_PATH = AVD_ROOT / "tools" / "schema_explorer_markdown.py"


def _load_formatter_module():
    spec = importlib.util.spec_from_file_location("schema_explorer_markdown_under_test", FORMATTER_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_schema_explorer_fence_rejects_unknown_options() -> None:
    module = _load_formatter_module()
    with pytest.raises(ValueError, match="Unsupported schema-explorer option"):
        module.schema_explorer_fence_format("bad_option: true\n", "schema-explorer", "", {}, None)


@pytest.mark.parametrize(
    ("source", "expected_fragment"),
    [
        ("module: eos_designs\nview: reference\nchrome: compact\n", 'module="eos_designs"'),
        ("module: eos_cli_config_gen\nview: yaml\n", 'view="yaml"'),
    ],
)
def test_schema_explorer_fence_validates_allowed_options(source: str, expected_fragment: str) -> None:
    module = _load_formatter_module()
    html = module.schema_explorer_fence_format(source, "schema-explorer", "", {}, None)
    assert expected_fragment in html
    assert "<schema-explorer" in html


def test_schema_explorer_fence_escapes_attribute_values() -> None:
    module = _load_formatter_module()
    html = module.schema_explorer_fence_format("root: '\"><img src=x onerror=alert(1)>'\n", "schema-explorer", "", {}, None)
    assert '"><img' not in html
    assert "&quot;&gt;&lt;img" in html or "&lt;img" in html
