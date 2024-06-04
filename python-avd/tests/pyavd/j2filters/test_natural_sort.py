# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest
from jinja2.runtime import Undefined
from natsort import os_sorted
from pyavd.j2filters.natural_sort import convert
from pyavd.j2filters.natural_sort import natural_sort as _natural_sort

STRINGS_VALID = ["100", "200", "ABC"]
ITEMS_TO_NATURAL_SORT = [None, [], {}, "", ["1,2,3,4", "11,2,3,4", "5.6.7.8"], {"a1": 123, "a2": 2, "a10": 333, "a11": 4456}]


class TestNaturalSortFilter:
    @pytest.mark.parametrize("STRING_VALID", STRINGS_VALID)
    def test_convert_function(self, STRING_VALID):
        resp = convert(STRING_VALID)
        if STRING_VALID.isdigit():
            assert resp == int(STRING_VALID)
        else:
            assert resp == STRING_VALID.lower()

    @pytest.mark.parametrize("ITEM_TO_NATURAL_SORT", ITEMS_TO_NATURAL_SORT)
    def test_natural_sort(self, ITEM_TO_NATURAL_SORT):
        resp = _natural_sort(ITEM_TO_NATURAL_SORT)
        if ITEM_TO_NATURAL_SORT is None or isinstance(ITEM_TO_NATURAL_SORT, Undefined):
            resp == []
        else:
            resp_natsort = os_sorted(ITEM_TO_NATURAL_SORT)
            assert resp == resp_natsort
