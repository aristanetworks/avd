# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest
from pyavd.j2filters.generate_route_target import generate_route_target

ESI_SHORT = "0303:0202:0101"
ESI_SHORT_STR = "ESI_SHORT"
ESI_SHORT_NONE = None
ESI_SHORT_EMPTY_STR = ""
ESI_SHORT_SINGLE_DIGIT = "3"

class TestEsiManagementFilter:
    @pytest.mark.parametrize("esi_short, route_target", [(ESI_SHORT, "03:03:02:02:01:01"), (ESI_SHORT_NONE, None), (ESI_SHORT_STR, "ES:I_:SH:OR"), (ESI_SHORT_EMPTY_STR, ""), (ESI_SHORT_SINGLE_DIGIT, "")])
    def test_generate_route_target(self, esi_short, route_target):
        resp = generate_route_target(esi_short)
        assert resp == route_target
