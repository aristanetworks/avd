from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.arista.avd.plugins.filter.default import default, FilterModule
import pytest
from jinja2.runtime import Undefined


PRIMARY_VALUE_LIST = [1, 'ABC', None, Undefined, {}, {"key": "value"}, [1, 2]]
DEFAULT_VALUE_LIST = [["default"], [None, 1], [
    None, "abc"], [None, None, "2"], [{"key": "value"}]]

f = FilterModule()


class TestDefaultFilter():
    @pytest.mark.parametrize("PRIMARY_VALUE", PRIMARY_VALUE_LIST)
    @pytest.mark.parametrize("DEFAULT_VALUE", DEFAULT_VALUE_LIST)
    def test_default(self, PRIMARY_VALUE, DEFAULT_VALUE):
        resp = default(PRIMARY_VALUE, *DEFAULT_VALUE)
        if isinstance(PRIMARY_VALUE, Undefined) or PRIMARY_VALUE is None and len(DEFAULT_VALUE_LIST) >= 1:
            for i in DEFAULT_VALUE:
                if isinstance(i, Undefined) or i is None or i == '':
                    continue
                assert i == resp
        else:
            assert resp == PRIMARY_VALUE

    def test_default_filter(self):
        resp = f.filters()
        assert isinstance(resp, dict)
        assert 'default' in resp.keys()
