# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os

import pytest
import yaml

from ansible_collections.arista.avd.plugins.plugin_utils.merge import merge
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschema import AvdSchema

script_dir = os.path.dirname(__file__)
with open(f"{script_dir}/access_lists.schema.yml", "r", encoding="utf-8") as schema_file:
    acl_schema = yaml.load(schema_file, Loader=yaml.SafeLoader)
with open(f"{script_dir}/acl1.yml", "r", encoding="utf-8") as data_file:
    acl1 = yaml.load(data_file, Loader=yaml.SafeLoader)
with open(f"{script_dir}/acl2.yml", "r", encoding="utf-8") as data_file:
    acl2 = yaml.load(data_file, Loader=yaml.SafeLoader)
with open(f"{script_dir}/acl_merged.yml", "r", encoding="utf-8") as data_file:
    acl_merged = yaml.load(data_file, Loader=yaml.SafeLoader)


class TestMerge:
    def test_merge_of_lists_with_primary_keys(self):
        merge_result = {}
        schema = AvdSchema(acl_schema)
        merge(merge_result, acl1, acl2, schema=schema)
        # print(yaml.dump(merge_result, indent=2))
        assert merge_result == acl_merged

    @pytest.mark.parametrize("schema", [None, AvdSchema(acl_schema)])
    def test_list_merge_replace(self, schema):
        """
        Testing with list_merge="replace" with or without schema.
        Expecting acl2 as result since we only have lists in the input.
        """
        merge_result = {}
        merge(merge_result, acl1, acl2, list_merge="replace", schema=schema)
        # print(yaml.dump(merge_result, indent=2))
        assert merge_result == acl2
