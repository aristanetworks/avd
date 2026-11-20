# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import importlib.util
from copy import deepcopy
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parents[3]
GENERATE_PATH = REPO_ROOT / "tools" / "schema-explorer" / "generate.py"
SPEC = importlib.util.spec_from_file_location("schema_explorer_generate", GENERATE_PATH)
assert SPEC is not None
assert SPEC.loader is not None
GENERATE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GENERATE)


def test_load_unresolved_store_from_yaml() -> None:
    store = GENERATE.load_unresolved_store(REPO_ROOT)

    assert set(store) == {"avd_meta_schema", "eos_designs", "eos_cli_config_gen"}
    login = store["eos_designs"]["keys"]["aaa_settings"]["keys"]["authentication"]["keys"]["login"]
    assert login["$ref"].startswith("eos_cli_config_gen#")


def test_neutralize_hidden_cross_schema_refs_keeps_visible_reuse() -> None:
    node = {
        "type": "dict",
        "$ref": "eos_cli_config_gen#/keys/aaa_authentication/keys/login",
        "documentation_options": {},
    }
    GENERATE.neutralize_hidden_cross_schema_refs(node, own_schema_id="eos_designs")
    assert node["$ref"] == "eos_cli_config_gen#/keys/aaa_authentication/keys/login"
    assert "_cross_ref" not in node


def test_neutralize_hidden_cross_schema_refs_strips_hide_keys() -> None:
    node = {
        "type": "dict",
        "documentation_options": {"hide_keys": True},
        "$ref": "eos_cli_config_gen#",
    }
    GENERATE.neutralize_hidden_cross_schema_refs(node, own_schema_id="eos_designs")
    assert node["_cross_ref"] == "eos_cli_config_gen#"
    assert "$ref" not in node


def test_neutralize_hidden_cross_schema_refs_leaves_same_schema_ref() -> None:
    node = {"$ref": "eos_designs#/$defs/node_type"}
    GENERATE.neutralize_hidden_cross_schema_refs(node, own_schema_id="eos_designs")
    assert node["$ref"] == "eos_designs#/$defs/node_type"


def test_neutralize_hidden_cross_schema_refs_ignores_non_dict() -> None:
    GENERATE.neutralize_hidden_cross_schema_refs([], own_schema_id="eos_designs")  # type: ignore[arg-type]


def test_neutralize_hidden_cross_schema_refs_hide_keys_same_schema() -> None:
    node = {
        "documentation_options": {"hide_keys": True},
        "$ref": "eos_designs#/$defs/node_type",
    }
    GENERATE.neutralize_hidden_cross_schema_refs(node, own_schema_id="eos_designs")
    assert node["$ref"] == "eos_designs#/$defs/node_type"
    assert "_cross_ref" not in node


def test_neutralize_hidden_cross_schema_refs_recurses_nested_containers() -> None:
    node = {
        "dynamic_keys": {
            "dyn": {
                "documentation_options": {"hide_keys": True},
                "$ref": "eos_cli_config_gen#/keys/foo",
            },
        },
        "items": {
            "documentation_options": {"hide_keys": True},
            "$ref": "eos_cli_config_gen#/keys/bar",
        },
        "$defs": {
            "inner": {
                "documentation_options": {"hide_keys": True},
                "$ref": "eos_cli_config_gen#",
            },
        },
    }
    GENERATE.neutralize_hidden_cross_schema_refs(node, own_schema_id="eos_designs")
    assert node["dynamic_keys"]["dyn"]["_cross_ref"] == "eos_cli_config_gen#/keys/foo"
    assert node["items"]["_cross_ref"] == "eos_cli_config_gen#/keys/bar"
    assert node["$defs"]["inner"]["_cross_ref"] == "eos_cli_config_gen#"


def test_hide_keys_structured_config_neutralized_in_yaml_store() -> None:
    store = deepcopy(GENERATE.load_unresolved_store(REPO_ROOT))
    GENERATE.neutralize_hidden_cross_schema_refs(store["eos_designs"], own_schema_id="eos_designs")
    structured = store["eos_designs"]["$defs"]["node_type"]["keys"]["defaults"]["keys"]["structured_config"]
    assert structured["_cross_ref"].startswith("eos_cli_config_gen")
    assert "$ref" not in structured


@pytest.mark.parametrize("schema_id", ["eos_designs", "eos_cli_config_gen"])
def test_load_resolved_store_expands_schema(schema_id: str) -> None:
    store = GENERATE._load_resolved_store(REPO_ROOT)

    assert store[schema_id]["$id"] == schema_id
