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
    def test_merge_of_lists_with_primary_keys(self) -> None:
        merge_result = {}
        merge(merge_result, acl1, acl2, schema_name="eos_config")
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
