# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from anta.input_models.services import DnsServer
from anta.tests.services import VerifyDNSServers

from pyavd.j2filters import natural_sort

from ._base_classes import AntaTestInputFactory


class VerifyDNSServersInputFactory(AntaTestInputFactory):
    """
    Input factory class for the `VerifyDNSServers` test.

    The test inputs `dns_servers` are collected from the values of
    `ip_address`, `vrf` and `priority` of each item in `ip_name_servers`
    of the device structured config.
    """

    def create(self) -> list[VerifyDNSServers.Input] | None:
        """Create a list of inputs for the `VerifyDNSServers` test."""
        dns_servers = [
            DnsServer(server_address=dns_server.ip_address, vrf=dns_server.vrf, priority=dns_server.priority if dns_server.priority is not None else 0)
            for dns_server in self.structured_config.ip_name_servers
        ]
        return [VerifyDNSServers.Input(dns_servers=natural_sort(dns_servers, sort_key="server_address"))] if dns_servers else None
