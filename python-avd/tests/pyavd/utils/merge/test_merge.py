# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path
from unittest.mock import patch

import yaml

from pyavd._utils import merge

script_dir = Path(__file__).parent
with Path(script_dir, "access_lists.schema.yml").open(encoding="utf-8") as schema_file:
    acl_schema = yaml.load(schema_file, Loader=yaml.SafeLoader)
with Path(script_dir, "acl1.yml").open(encoding="utf-8") as data_file:
    acl1 = yaml.load(data_file, Loader=yaml.SafeLoader)
with Path(script_dir, "acl2.yml").open(encoding="utf-8") as data_file:
    acl2 = yaml.load(data_file, Loader=yaml.SafeLoader)
with Path(script_dir, "acl_merged.yml").open(encoding="utf-8") as data_file:
    acl_merged = yaml.load(data_file, Loader=yaml.SafeLoader)


class TestMerge:
    def test_merge_of_lists_with_primary_keys(self) -> None:
        merge_result = {}
        merge(merge_result, acl1, acl2, schema_name="eos_config")
        assert merge_result == acl_merged

    def test_merge_of_lists_with_schema_name_uses_indexed_paths(self) -> None:
        merge_result = {}

        def get_list_primary_key(schema_name: str, data_path: list[str]) -> str | None:
            assert schema_name == "eos_config"
            primary_keys = {
                ("access_lists",): "name",
                ("access_lists", "1", "sequence_numbers"): "sequence",
            }
            return primary_keys.get(tuple(data_path))

        with (
            patch("pyavd._schema.store.init_store"),
            patch("pyavd_utils.schema_store.get_list_primary_key", side_effect=get_list_primary_key),
        ):
            merge(merge_result, acl1, acl2, schema_name="eos_config")

        assert merge_result == acl_merged

    def test_list_merge_replace(self) -> None:
        """
        Testing with list_merge="replace" with or without schema.

        Expecting acl2 as result since we only have lists in the input.
        """
        merge_result = {}
        merge(merge_result, acl1, acl2, list_merge="replace", schema_name="eos_config")
        assert merge_result == acl2
