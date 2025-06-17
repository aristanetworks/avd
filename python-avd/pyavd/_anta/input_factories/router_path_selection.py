# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ipaddress import ip_interface

from anta.input_models.path_selection import DpsPath
from anta.tests.path_selection import VerifySpecificPath

from pyavd._anta.logs import LogMessage
from pyavd.j2filters import natural_sort

from ._base_classes import AntaTestInputFactory


class VerifySpecificPathInputFactory(AntaTestInputFactory):
    """
    Input factory class for the `VerifySpecificPath` test.

    This factory generates test inputs for verifying DPS paths telemetry state of an IPv4 peer.

    It collects the peer and destination address from static peers, source address for local interfaces and path name from path groups.
    """

    def create(self) -> list[VerifySpecificPath.Input] | None:
        """Create a list of inputs for the `VerifySpecificPath` test."""
        all_dps_paths: list[DpsPath] = []

        for path_group in self.structured_config.router_path_selection.path_groups:
            if not path_group.local_interfaces:
                self.logger_adapter.debug(LogMessage.PATH_GROUP_NO_LOCAL_INTERFACES, path_group=path_group.name)
                continue
            if not path_group.static_peers:
                self.logger_adapter.debug(LogMessage.PATH_GROUP_NO_STATIC_PEERS, path_group=path_group.name)
                continue

            for interface in path_group.local_interfaces:
                # Get the source IP address for the local interface
                if interface.name.startswith("Ethernet") and interface.name in self.structured_config.ethernet_interfaces:
                    ip_address = self.structured_config.ethernet_interfaces[interface.name].ip_address
                elif interface.name.startswith("Port-Channel") and interface.name in self.structured_config.port_channel_interfaces:
                    ip_address = self.structured_config.port_channel_interfaces[interface.name].ip_address
                else:
                    ip_address = None

                if ip_address is None:
                    self.logger_adapter.debug(LogMessage.INTERFACE_NO_IP, interface=interface)
                    continue

                if ip_address == "dhcp":
                    self.logger_adapter.debug(LogMessage.INTERFACE_USING_DHCP, interface=interface)
                    continue

                source_address = ip_interface(ip_address).ip
                for static_peer in path_group.static_peers:
                    for destination_address in static_peer.ipv4_addresses:
                        dps_path = DpsPath(
                            peer=static_peer.router_ip, path_group=path_group.name, source_address=source_address, destination_address=destination_address
                        )
                        all_dps_paths.append(dps_path)

        return [VerifySpecificPath.Input(paths=natural_sort(all_dps_paths, sort_key="peer"))] if all_dps_paths else None
