# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest

from ansible_collections.arista.avd.plugins.filter.list_compress import AnsibleFilterError, FilterModule, list_compress

LIST_TO_COMPRESS_INVALID_VALUES = ["1-3", {"key": "value"}, 33]
LIST_TO_COMPRESS_VALID_VALUES = [[1, 2, 3, 4], [1, 2, 3, 7, 8]]
EXPECTED_RESULT_VALID_VALUES = ["1-4", "1-3,7-8"]


f = FilterModule()


class TestListCompressFilter:
    @pytest.mark.parametrize("LIST_TO_COMPRESS_INVALID", LIST_TO_COMPRESS_INVALID_VALUES)
    def test_list_compress_invalid(self, LIST_TO_COMPRESS_INVALID):
        with pytest.raises(AnsibleFilterError) as exc_info:
            list_compress(LIST_TO_COMPRESS_INVALID)
        assert str(exc_info.value) == f"value must be of type list, got {type(LIST_TO_COMPRESS_INVALID)}"

    @pytest.mark.parametrize("LIST_TO_COMPRESS_VALID", LIST_TO_COMPRESS_VALID_VALUES)
    def test_list_compress_valid(self, LIST_TO_COMPRESS_VALID):
        resp = list_compress(LIST_TO_COMPRESS_VALID)
        assert resp in EXPECTED_RESULT_VALID_VALUES

    def test_list_compress_filter(self):
        resp = f.filters()
        assert isinstance(resp, dict)
        assert "list_compress" in resp.keys()
