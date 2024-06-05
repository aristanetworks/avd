# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

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
        "item_to_natural_sort, expected_output",
        [
            (None, []),
            ([], []),
            ({}, []),
            ("", []),
            (["1,2,3,4", "11,2,3,4", "5.6.7.8"], ["1,2,3,4", "5.6.7.8", "11,2,3,4"]),
            ({"a1": 123, "a10": 333, "a2": 2, "a11": 4456}, ["a1", "a2", "a10", "a11"]),
        ],
    )
    def test_natural_sort(self, item_to_natural_sort, expected_output):
        resp = natural_sort(item_to_natural_sort)
        assert resp == expected_output
