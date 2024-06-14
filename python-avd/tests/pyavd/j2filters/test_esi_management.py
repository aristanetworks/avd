# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest
from pyavd.j2filters.generate_esi import generate_esi
from pyavd.j2filters.generate_route_target import generate_route_target

ESI_TO_RT_TEST_CASES = [
    # (<esi_short>, <route_target>)
    ("0303:0202:0101", "03:03:02:02:01:01"),
    (None, None),
    ("ESI_SHORT", "ES:I_:SH:OR"),
    ("", ""),
    ("3", ""),
]

DEFAULT_ESI_PREFIX = "0000:0000:"
GENERATE_ESI_TEST_CASES = [
    # (<esi_short>, <esi_prefix>, <esi>)
    ("0303:0202:0101", "", "0000:0000:0303:0202:0101"),  # without prefix
    ("0303:0202:0101", "1111:1111:", "1111:1111:0303:0202:0101"),  # with prefix
]


class TestEsiManagementFilter:
    @pytest.mark.parametrize("esi_short, route_target", ESI_TO_RT_TEST_CASES)
    def test_generate_route_target(self, esi_short, route_target):
        resp = generate_route_target(esi_short)
        assert resp == route_target

    @pytest.mark.parametrize("esi_short, esi_prefix, esi", GENERATE_ESI_TEST_CASES)
    def test_generate_esi(self, esi_short, esi_prefix, esi):
        esi_prefix = esi_prefix or DEFAULT_ESI_PREFIX
        resp = generate_esi(esi_short, esi_prefix)
        assert resp == esi
