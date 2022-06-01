from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.arista.avd.plugins.filter.natural_sort import FilterModule, convert, natural_sort as _natural_sort
from jinja2.runtime import Undefined
from ansible_collections.arista.avd.tests.unit.filters.filter_utils import natural_sort
import pytest

f = FilterModule()

STRINGS_VALID = ["100", "200", "ABC"]
ITEMS_TO_NATURAL_SORT = [None, [], {}, "", ["1,2,3,4", "11,2,3,4", "5.6.7.8"], {
    'a1': 123, 'a2': 2, 'a10': 333, 'a11': 4456}]


class TestNaturalSortFilter():
    @pytest.mark.parametrize("STRING_VALID", STRINGS_VALID)
    def test_convert_function(self, STRING_VALID):
        resp = convert(STRING_VALID)
        if STRING_VALID.isdigit():
            assert resp == int(STRING_VALID)
        else:
            assert resp == STRING_VALID.lower()

    @pytest.mark.parametrize("ITEM_TO_NATURAL_SORT", ITEMS_TO_NATURAL_SORT)
    def test_natural_sort_invalid(self, ITEM_TO_NATURAL_SORT):
        resp = _natural_sort(ITEM_TO_NATURAL_SORT)
        if ITEM_TO_NATURAL_SORT is None or isinstance(ITEM_TO_NATURAL_SORT, Undefined):
            resp == []
        else:
            resp_natsort = natural_sort(ITEM_TO_NATURAL_SORT)
            assert resp == resp_natsort

    def test_natural_sort_filter(self):
        resp = f.filters()
        assert isinstance(resp, dict)
        assert 'natural_sort' in resp.keys()
