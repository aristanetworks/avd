# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

import pytest
from pyavd.j2filters import convert_dicts

DEFAULT_PRIMARY_KEY = "name"
NESTED_LIST_OF_DICT = {
    "TEST1": [{"type": "permit", "extcommunities": "65000:65000"}, {"type": "deny", "extcommunities": "65002:65002"}],
    "TEST2": [{"type": "deny", "extcommunities": "65001:65001"}],
}
NESTED_DICT = {"TEST1": {"action": "permit 1000:1000"}, "TEST2": {"action": "permit 2000:3000"}}
LIST_OF_STRING = ["Test1", "Test2", "Test3"]
LIST_OF_DICT = [{"type": "permit"}, {"extcommunities": "65000:65000"}]
DICT_WITH_STRING = {"dict": "test_string"}


class TestConvertDicts:
    @pytest.mark.parametrize(
        "test_dict, primary_key, secondary_key, converted_value",
        [
            (
                NESTED_DICT,
                "",
                "",
                [{"action": "permit 1000:1000", "name": "TEST1"}, {"action": "permit 2000:3000", "name": "TEST2"}],
            ),  # test_convert_dicts_with_nested_dict_default
            (
                NESTED_DICT,
                "id",
                "",
                [{"action": "permit 1000:1000", "id": "TEST1"}, {"action": "permit 2000:3000", "id": "TEST2"}],
            ),  # test_convert_dicts_with_nested_dict_primary_key
            (
                NESTED_DICT,
                "",
                "types",
                [{"name": "TEST1", "types": {"action": "permit 1000:1000"}}, {"name": "TEST2", "types": {"action": "permit 2000:3000"}}],
            ),  # test_convert_dicts_with_nested_dict_secondary_key
            (
                NESTED_DICT,
                "id",
                "types",
                [{"id": "TEST1", "types": {"action": "permit 1000:1000"}}, {"id": "TEST2", "types": {"action": "permit 2000:3000"}}],
            ),  # test_convert_dicts_with_listofdict_default
            (NESTED_LIST_OF_DICT, "", "", [{"name": "TEST1"}, {"name": "TEST2"}]),  # test_convert_dicts_with_listofdict_default
            (NESTED_LIST_OF_DICT, "test", "", [{"test": "TEST1"}, {"test": "TEST2"}]),  # test_convert_dicts_with_listofdict_primary_key
            (
                NESTED_LIST_OF_DICT,
                "",
                "types",
                [
                    {"name": "TEST1", "types": [{"type": "permit", "extcommunities": "65000:65000"}, {"type": "deny", "extcommunities": "65002:65002"}]},
                    {"name": "TEST2", "types": [{"type": "deny", "extcommunities": "65001:65001"}]},
                ],
            ),  # test_convert_dicts_with_listofdict_secondary_key
            (
                NESTED_LIST_OF_DICT,
                "id",
                "types",
                [
                    {"id": "TEST1", "types": [{"type": "permit", "extcommunities": "65000:65000"}, {"type": "deny", "extcommunities": "65002:65002"}]},
                    {"id": "TEST2", "types": [{"type": "deny", "extcommunities": "65001:65001"}]},
                ],
            ),  # test_convert_dicts_with_listofdict_primary_and_secondary_key
            (LIST_OF_STRING, "", "", [{"name": "Test1"}, {"name": "Test2"}, {"name": "Test3"}]),  # test_convert_dicts_with_list_default
            (LIST_OF_STRING, "test", "", [{"test": "Test1"}, {"test": "Test2"}, {"test": "Test3"}]),  # test_convert_dicts_with_list_primary_key
            (LIST_OF_STRING, "", "id", [{"name": "Test1"}, {"name": "Test2"}, {"name": "Test3"}]),  # test_convert_dicts_with_list_secondary_key
            (
                LIST_OF_STRING,
                "test",
                "types",
                [{"test": "Test1"}, {"test": "Test2"}, {"test": "Test3"}],
            ),  # test_convert_dicts_with_list_primary_and_secondary_key
            (DICT_WITH_STRING, "", "", [{"name": "dict"}]),  # test_convert_dicts_with_string_value_default
            (DICT_WITH_STRING, "test", "", [{"test": "dict"}]),  # test_convert_dicts_with_string_value_primary_key
            (DICT_WITH_STRING, "", "str", [{"name": "dict", "str": "test_string"}]),  # test_convert_dicts_with_string_value_secondary_key
            (DICT_WITH_STRING, "test", "str", [{"test": "dict", "str": "test_string"}]),  # test_convert_dicts_with_string_value_primary_key_and_secondary_key
            (LIST_OF_DICT, "", "", LIST_OF_DICT),  # test_convert_dicts_with_list_of_dict_default
            (LIST_OF_DICT, "test", "", LIST_OF_DICT),  # test_convert_dicts_with_list_of_dict_primary_key
            (
                LIST_OF_DICT,
                "",
                "id",
                [{"name": "type", "id": "permit"}, {"name": "extcommunities", "id": "65000:65000"}],
            ),  # test_convert_dicts_with_list_of_dict_secondary_key
            (LIST_OF_DICT, "test", "id", [{"test": "type", "id": "permit"}, {"test": "extcommunities", "id": "65000:65000"}]),
        ],
    )  # test_convert_dicts_with_list_of_dict_primary_key_and_secondary_key
    def test_convert_dicts(self, test_dict, primary_key, secondary_key, converted_value):
        primary_key = primary_key if primary_key else DEFAULT_PRIMARY_KEY
        secondary_key = secondary_key if secondary_key else None
        resp = convert_dicts(test_dict, primary_key, secondary_key)
        assert resp == converted_value
