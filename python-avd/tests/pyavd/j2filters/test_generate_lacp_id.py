# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest
from pyavd.j2filters.generate_lacp_id import generate_lacp_id

ESI_SHORT_INPUT = [
    ("0404:0202:0101", "0404.0202.0101"),
    ("000:000:0303:0202:0101", "000.000.0303.0202.0101"),
    ("", ""),
    (10, None),
    (None, None),
]


class TestGenerateLacpIdFilter:

    @pytest.mark.parametrize("esi_short, lacp_id", ESI_SHORT_INPUT)
    def test_generate_lacp_id(self, esi_short, lacp_id):
        resp = generate_lacp_id(esi_short)
        assert resp == lacp_id
