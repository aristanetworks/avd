# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest
from pyavd.j2filters import generate_route_target

ESI_TO_RT_TEST_CASES = [
    # (<esi_short>, <route_target>)
    ("0303:0202:0101", "03:03:02:02:01:01"),
    (None, None),
    ("ESI_SHORT", "ES:I_:SH:OR"),
    ("", ""),
    ("3", ""),
]


class TestGenerateRouteTargetFilter:
    @pytest.mark.parametrize("esi_short, route_target", ESI_TO_RT_TEST_CASES)
    def test_generate_route_target(self, esi_short, route_target):
        resp = generate_route_target(esi_short)
        assert resp == route_target
