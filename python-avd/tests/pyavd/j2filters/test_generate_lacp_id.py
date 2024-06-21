# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest
from pyavd.j2filters import generate_lacp_id

ESI_SHORT_VALID_INPUT = [
    ("0404:0202:0101", "0404.0202.0101"),
    ("000:000:0303:0202:0101", "000.000.0303.0202.0101"),
    ("", ""),
]

ESI_SHORT_INVALID_INPUT = [
    (10, "'int' object has no attribute 'replace'"),
    (None, "'NoneType' object has no attribute 'replace'"),
    ({}, "'dict' object has no attribute 'replace'"),
    ([], "'list' object has no attribute 'replace'"),
]


class TestGenerateLacpIdFilter:

    @pytest.mark.parametrize("esi_short, lacp_id", ESI_SHORT_VALID_INPUT)
    def test_generate_lacp_id_valid(self, esi_short, lacp_id):
        resp = generate_lacp_id(esi_short)
        assert resp == lacp_id

    @pytest.mark.parametrize("esi_short, error_msg", ESI_SHORT_INVALID_INPUT)
    def test_generate_lacp_id_invalid(self, esi_short, error_msg):
        with pytest.raises(AttributeError) as exc_info:
            generate_lacp_id(esi_short)
        assert str(exc_info.value) == error_msg
