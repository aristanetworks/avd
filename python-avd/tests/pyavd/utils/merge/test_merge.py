# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path

import pytest
import yaml

from pyavd._utils import merge

script_dir = Path(__file__).parent
with Path(script_dir, "acl1.yml").open(encoding="utf-8") as data_file:
    acl1 = yaml.load(data_file, Loader=yaml.SafeLoader)
with Path(script_dir, "acl2.yml").open(encoding="utf-8") as data_file:
    acl2 = yaml.load(data_file, Loader=yaml.SafeLoader)
with Path(script_dir, "acl_merged.yml").open(encoding="utf-8") as data_file:
    acl_merged = yaml.load(data_file, Loader=yaml.SafeLoader)


class TestMerge:
    @pytest.mark.parametrize("schema_name", ["eos_config", "eos_cli_config_gen"])
    def test_merge_of_lists_with_primary_keys(self, schema_name: str) -> None:
        merge_result = {}
        merge(merge_result, acl1, acl2, schema_name=schema_name)
        assert merge_result == acl_merged

    @pytest.mark.parametrize("schema_name", [None, "eos_config"])
    def test_list_merge_replace(self, schema_name: str | None) -> None:
        """
        Testing with list_merge="replace" with or without schema.

        Expecting acl2 as result since we only have lists in the input.
        """
        merge_result = {}
        merge(merge_result, acl1, acl2, list_merge="replace", schema_name=schema_name)
        assert merge_result == acl2

    def test_unsupported_schema_name_raises(self) -> None:
        with pytest.raises(ValueError, match="Unsupported schema name 'invalid_schema'"):
            merge({}, acl1, acl2, schema_name="invalid_schema")
