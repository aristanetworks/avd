# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
# Testing the legacy pickled schema store.
# Only used by schema-based merging at the end of eos_designs_structured_config Ansible role
from pyavd._schema.store import create_store


def test_create_schema_store() -> None:
    store = create_store()
    keys = set(store.keys())
    assert keys.issuperset(("eos_designs", "eos_cli_config_gen", "cv_deploy"))
    assert isinstance(store["eos_designs"], dict)
    assert "keys" in store["eos_designs"]
    assert isinstance(store["eos_designs"]["keys"], dict)
    assert "fabric_name" in store["eos_designs"]["keys"]
    assert isinstance(store["eos_designs"]["keys"]["fabric_name"], dict)
    assert "required" in store["eos_designs"]["keys"]["fabric_name"]
    assert isinstance(store["eos_designs"]["keys"]["fabric_name"]["required"], bool)
    assert store["eos_designs"]["keys"]["fabric_name"]["required"]
