# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.arista.avd.plugins.filter.generate_esi import generate_esi
from ansible_collections.arista.avd.plugins.filter.generate_lacp_id import generate_lacp_id

ESI_SHORT = "0303:0202:0101"
ESI_PREFIX = "1111:1111"
ESI_SHORT_1 = "0404:0202:0101"


class TestEsiManagementFilter:
    def test_generate_esi_without_prefix(self):
        resp = generate_esi(ESI_SHORT)
        assert resp == "0000:0000:" + ESI_SHORT

    def test_generate_esi_with_prefix(self):
        assert ESI_PREFIX is not None and ESI_PREFIX != ""
        resp = generate_esi(ESI_SHORT, ESI_PREFIX)
        assert resp == ESI_PREFIX + ESI_SHORT

    def test_lacp_id(self):
        assert ESI_SHORT_1 is not None and ESI_SHORT_1 != ""
        resp = generate_lacp_id(ESI_SHORT_1)
        assert ":" not in resp
        assert "." in resp
