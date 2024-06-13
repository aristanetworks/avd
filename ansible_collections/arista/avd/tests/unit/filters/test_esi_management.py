# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.arista.avd.plugins.filter.generate_lacp_id import generate_lacp_id

ESI_SHORT_1 = "0404:0202:0101"


class TestEsiManagementFilter:

    def test_lacp_id(self):
        assert ESI_SHORT_1 is not None and ESI_SHORT_1 != ""
        resp = generate_lacp_id(ESI_SHORT_1)
        assert ":" not in resp
        assert "." in resp
