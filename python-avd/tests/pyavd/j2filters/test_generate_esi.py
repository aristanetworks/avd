# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest
from pyavd.j2filters import generate_esi

DEFAULT_ESI_PREFIX = "0000:0000:"
GENERATE_ESI_TEST_CASES = [
    # (<esi_short>, <esi_prefix>, <esi>)
    ("0303:0202:0101", "", "0000:0000:0303:0202:0101"),  # without prefix
    ("0303:0202:0101", "1111:1111:", "1111:1111:0303:0202:0101"),  # with prefix
]


class TestGenerateEsiFilter:
    @pytest.mark.parametrize("esi_short, esi_prefix, esi", GENERATE_ESI_TEST_CASES)
    def test_generate_esi(self, esi_short, esi_prefix, esi):
        esi_prefix = esi_prefix or DEFAULT_ESI_PREFIX
        resp = generate_esi(esi_short, esi_prefix)
        assert resp == esi
