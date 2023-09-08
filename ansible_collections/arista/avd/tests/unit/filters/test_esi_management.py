# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.arista.avd.plugins.filter.generate_esi import generate_esi
from ansible_collections.arista.avd.plugins.filter.generate_lacp_id import generate_lacp_id
from ansible_collections.arista.avd.plugins.filter.generate_route_target import generate_route_target
from ansible_collections.arista.avd.tests.unit.filters.filter_utils import convert_esi_short_to_route_target_format

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

    def test_generate_route_target(self):
        route_target_format_esi = convert_esi_short_to_route_target_format(ESI_SHORT)
        resp = generate_route_target(ESI_SHORT)
        assert resp == route_target_format_esi
        resp1 = generate_route_target(None)
        assert resp1 is None
