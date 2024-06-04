# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest
from pyavd.j2filters.natural_sort import convert, natural_sort


class TestNaturalSortFilter:
    @pytest.mark.parametrize("STRING_VALID", ["100", "200", "ABC"])
    def test_convert_function(self, STRING_VALID):
        resp = convert(STRING_VALID)
        if STRING_VALID.isdigit():
            assert resp == int(STRING_VALID)
        else:
            assert resp == STRING_VALID.lower()

    @pytest.mark.parametrize(
        "ITEM_TO_NATURAL_SORT, EXPECTED_OUTPUT",
        [
            (None, []),
            ([], []),
            ({}, []),
            ("", []),
            (["1,2,3,4", "11,2,3,4", "5.6.7.8"], ["1,2,3,4", "5.6.7.8", "11,2,3,4"]),
            ({"a1": 123, "a10": 333, "a2": 2, "a11": 4456}, ["a1", "a2", "a10", "a11"]),
        ],
    )
    def test_natural_sort(self, ITEM_TO_NATURAL_SORT, EXPECTED_OUTPUT):
        resp = natural_sort(ITEM_TO_NATURAL_SORT)
        assert resp == EXPECTED_OUTPUT
