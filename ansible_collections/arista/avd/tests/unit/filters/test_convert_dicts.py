# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.arista.avd.plugins.filter.convert_dicts import FilterModule, convert_dicts

nested_list_of_dict = {
    "TEST1": [{"type": "permit", "extcommunities": "65000:65000"}, {"type": "deny", "extcommunities": "65002:65002"}],
    "TEST2": [{"type": "deny", "extcommunities": "65001:65001"}],
}
nested_dict = {"TEST1": {"action": "permit 1000:1000"}, "TEST2": {"action": "permit 2000:3000"}}
list = ["Test1", "Test2", "Test3"]
list_of_dict = [{"type": "permit"}, {"extcommunities": "65000:65000"}]
dict_with_string = {"dict": "test_string"}

f = FilterModule()


class TestConvertDicts:
    def test_convert_dicts_with_nested_dict_default(self):
        resp = convert_dicts(nested_dict)
        assert resp == [{"action": "permit 1000:1000", "name": "TEST1"}, {"action": "permit 2000:3000", "name": "TEST2"}]

    def test_convert_dicts_with_nested_dict_primary_key(self):
        resp = convert_dicts(nested_dict, "id")
        assert resp == [{"action": "permit 1000:1000", "id": "TEST1"}, {"action": "permit 2000:3000", "id": "TEST2"}]

    def test_convert_dicts_with_nested_dict_secondary_key(self):
        resp = convert_dicts(nested_dict, secondary_key="types")
        assert resp == [{"name": "TEST1", "types": {"action": "permit 1000:1000"}}, {"name": "TEST2", "types": {"action": "permit 2000:3000"}}]

    def test_convert_dicts_with_nested_dict_primary_and_secondary_key(self):
        resp = convert_dicts(nested_dict, "id", "types")
        assert resp == [{"id": "TEST1", "types": {"action": "permit 1000:1000"}}, {"id": "TEST2", "types": {"action": "permit 2000:3000"}}]

    def test_convert_dicts_with_listofdict_default(self):
        resp = convert_dicts(nested_list_of_dict)
        assert resp == [{"name": "TEST1"}, {"name": "TEST2"}]

    def test_convert_dicts_with_listofdict_primary_key(self):
        resp = convert_dicts(nested_list_of_dict, "test")
        assert resp == [{"test": "TEST1"}, {"test": "TEST2"}]

    def test_convert_dicts_with_listofdict_secondary_key(self):
        resp = convert_dicts(nested_list_of_dict, secondary_key="types")
        assert resp == [
            {"name": "TEST1", "types": [{"type": "permit", "extcommunities": "65000:65000"}, {"type": "deny", "extcommunities": "65002:65002"}]},
            {"name": "TEST2", "types": [{"type": "deny", "extcommunities": "65001:65001"}]},
        ]

    def test_convert_dicts_with_listofdict_primary_and_secondary_key(self):
        resp = convert_dicts(nested_list_of_dict, "id", "types")
        assert resp == [
            {"id": "TEST1", "types": [{"type": "permit", "extcommunities": "65000:65000"}, {"type": "deny", "extcommunities": "65002:65002"}]},
            {"id": "TEST2", "types": [{"type": "deny", "extcommunities": "65001:65001"}]},
        ]

    def test_convert_dicts_with_list_default(self):
        resp = convert_dicts(list)
        assert resp == [{"name": "Test1"}, {"name": "Test2"}, {"name": "Test3"}]

    def test_convert_dicts_with_list_primary_key(self):
        resp = convert_dicts(list, "test")
        assert resp == [{"test": "Test1"}, {"test": "Test2"}, {"test": "Test3"}]

    def test_convert_dicts_with_list_secondary_key(self):
        resp = convert_dicts(list, secondary_key="id")
        assert resp == [{"name": "Test1"}, {"name": "Test2"}, {"name": "Test3"}]

    def test_convert_dicts_with_list_primary_and_secondary_key(self):
        resp = convert_dicts(list, "test", "types")
        assert resp == [{"test": "Test1"}, {"test": "Test2"}, {"test": "Test3"}]

    def test_convert_dicts_with_string_value_default(self):
        resp = convert_dicts(dict_with_string)
        assert resp == [{"name": "dict"}]

    def test_convert_dicts_with_string_value_primary_key(self):
        resp = convert_dicts(dict_with_string, "test")
        assert resp == [{"test": "dict"}]

    def test_convert_dicts_with_string_value_secondary_key(self):
        resp = convert_dicts(dict_with_string, secondary_key="str")
        assert resp == [{"name": "dict", "str": "test_string"}]

    def test_convert_dicts_with_string_value_primary_key_and_secondary_key(self):
        resp = convert_dicts(dict_with_string, "test", "str")
        assert resp == [{"test": "dict", "str": "test_string"}]

    def test_convert_dicts_with_list_of_dict_default(self):
        resp = convert_dicts(list_of_dict)
        assert resp == list_of_dict

    def test_convert_dicts_with_list_of_dict_primary_key(self):
        resp = convert_dicts(list_of_dict, "test")
        assert resp == list_of_dict

    def test_convert_dicts_with_list_of_dict_secondary_key(self):
        # We convert a list-of-dict input if primary_key is found in element and secondary_key is set
        resp = convert_dicts(list_of_dict, secondary_key="id")
        assert resp == [{"name": "type", "id": "permit"}, {"name": "extcommunities", "id": "65000:65000"}]

    def test_convert_dicts_with_list_of_dict_primary_key_and_secondary_key(self):
        # We convert a list-of-dict input if primary_key is found in element and secondary_key is set
        resp = convert_dicts(list_of_dict, "test", "id")
        assert resp == [{"test": "type", "id": "permit"}, {"test": "extcommunities", "id": "65000:65000"}]

    def test_convert_dicts_filter(self):
        resp = f.filters()
        assert isinstance(resp, dict)
        assert "convert_dicts" in resp.keys()
