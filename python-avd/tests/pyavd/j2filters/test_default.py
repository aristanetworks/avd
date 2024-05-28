# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest
from jinja2.runtime import Undefined
from pyavd.j2filters.default import default

PRIMARY_VALUE_LIST = [1, "ABC", None, Undefined, {}, {"key": "value"}, [1, 2]]
DEFAULT_VALUE_LIST = [["default"], [None, 1], [None, "abc"], [None, None, "2"], [{"key": "value"}]]


class TestDefaultFilter:
    @pytest.mark.parametrize("PRIMARY_VALUE", PRIMARY_VALUE_LIST)
    @pytest.mark.parametrize("DEFAULT_VALUE", DEFAULT_VALUE_LIST)
    def test_default(self, PRIMARY_VALUE, DEFAULT_VALUE):
        resp = default(PRIMARY_VALUE, *DEFAULT_VALUE)
        if isinstance(PRIMARY_VALUE, Undefined) or PRIMARY_VALUE is None and len(DEFAULT_VALUE_LIST) >= 1:
            for i in DEFAULT_VALUE:
                if isinstance(i, Undefined) or i is None or i == "":
                    continue
                assert i == resp
        else:
            assert resp == PRIMARY_VALUE
