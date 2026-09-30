# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from copy import deepcopy

import pytest

from schema_tools.constants import SCHEMA_STORE_GZ_FILE
from schema_tools.store import (
    load_combined_store_from_gz,
    load_unresolved_store,
    neutralize_hidden_cross_schema_refs,
)


@pytest.mark.skipif(not SCHEMA_STORE_GZ_FILE.is_file(), reason="schemas.json.gz not built")
def test_load_combined_store_from_gz_includes_design_schemas() -> None:
    store = load_combined_store_from_gz()
    assert "eos_designs" in store
    assert "eos_cli_config_gen" in store
    login = store["eos_designs"]["keys"]["aaa_settings"]["keys"]["authentication"]["keys"]["login"]
    assert login["$ref"].startswith("eos_cli_config_gen#")


def test_neutralize_hidden_cross_schema_refs_keeps_visible_reuse() -> None:
    node = {
        "type": "dict",
        "$ref": "eos_cli_config_gen#/keys/aaa_authentication/keys/login",
        "documentation_options": {},
    }
    neutralize_hidden_cross_schema_refs(node, own_schema_id="eos_designs")
    assert node["$ref"] == "eos_cli_config_gen#/keys/aaa_authentication/keys/login"
    assert "_cross_ref" not in node


def test_neutralize_hidden_cross_schema_refs_strips_hide_keys() -> None:
    node = {
        "type": "dict",
        "documentation_options": {"hide_keys": True},
        "$ref": "eos_cli_config_gen#",
    }
    neutralize_hidden_cross_schema_refs(node, own_schema_id="eos_designs")
    assert node["_cross_ref"] == "eos_cli_config_gen#"
    assert "$ref" not in node


def test_neutralize_hidden_cross_schema_refs_leaves_same_schema_ref() -> None:
    node = {"$ref": "eos_designs#/$defs/node_type"}
    neutralize_hidden_cross_schema_refs(node, own_schema_id="eos_designs")
    assert node["$ref"] == "eos_designs#/$defs/node_type"


@pytest.mark.skipif(not SCHEMA_STORE_GZ_FILE.is_file(), reason="schemas.json.gz not built")
def test_load_unresolved_store_prefers_gz() -> None:
    store = load_unresolved_store()
    assert "eos_designs" in store
    login = store["eos_designs"]["keys"]["aaa_settings"]["keys"]["authentication"]["keys"]["login"]
    assert "$ref" in login


@pytest.mark.skipif(not SCHEMA_STORE_GZ_FILE.is_file(), reason="schemas.json.gz not built")
def test_hide_keys_structured_config_neutralized_in_gz_store() -> None:
    store = deepcopy(load_combined_store_from_gz())
    neutralize_hidden_cross_schema_refs(store["eos_designs"], own_schema_id="eos_designs")
    structured = store["eos_designs"]["$defs"]["node_type"]["keys"]["defaults"]["keys"]["structured_config"]
    assert structured.get("_cross_ref", "").startswith("eos_cli_config_gen")
    assert "$ref" not in structured
