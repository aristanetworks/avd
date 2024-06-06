# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest
from pyavd.j2filters.natural_sort import convert, natural_sort


class TestNaturalSortFilter:
    @pytest.mark.parametrize("item_to_convert", ["100", "200", "ABC"])
    def test_convert_function(self, item_to_convert):
        resp = convert(item_to_convert)
        if item_to_convert.isdigit():
            assert resp == int(item_to_convert)
        else:
            assert resp == item_to_convert.lower()

    @pytest.mark.parametrize(
        "item_to_natural_sort, sort_key, sorted_list",
        [
            (None, None, []),  # test with None
            ([], None, []),  # test with blank list
            ({}, "", []),  # test with blank dict
            ("", None, []),  # test with blank string
            ("access_list", None, ["_", "a", "c", "c", "e", "i", "l", "s", "s", "s", "t"]),  # test with string
            (["1,2,3,4", "11,2,3,4", "5.6.7.8"], None, ["1,2,3,4", "5.6.7.8", "11,2,3,4"]),  # test with list of integers
            ({"a1": 123, "a10": 333, "a2": 2, "a11": 4456}, None, ["a1", "a2", "a10", "a11"]),  # test with dict
            (
                [
                    {"name": "ACL-10", "counters_per_entry": True},
                    {"name": "ACL-01", "counters_per_entry": True},
                    {"name": "ACL-05", "counters_per_entry": False},
                ],
                "name",
                [
                    {"name": "ACL-01", "counters_per_entry": True},
                    {"name": "ACL-05", "counters_per_entry": False},
                    {"name": "ACL-10", "counters_per_entry": True},
                ],  # test list of dict with "name" as sort_key
            ),
        ],
    )
    def test_natural_sort(self, item_to_natural_sort, sort_key, sorted_list):
        resp = natural_sort(item_to_natural_sort, sort_key)
        assert resp == sorted_list
