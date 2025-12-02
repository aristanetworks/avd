# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ipaddress import IPv4Address, IPv4Interface, ip_address
from typing import TYPE_CHECKING

from anta.input_models.path_selection import DpsPath
from anta.tests.path_selection import VerifySpecificPath

from pyavd._anta.logs import LogMessage
from pyavd.j2filters import natural_sort

from ._base_classes import AntaTestInputFactory

if TYPE_CHECKING:
    from collections.abc import Iterator

    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen


class VerifySpecificPathInputFactory(AntaTestInputFactory[VerifySpecificPath.Input]):
    """
    Input factory class for the `VerifySpecificPath` test.

    This factory generates test inputs for verifying DPS paths telemetry state of an IPv4 peer.

    It collects the peer and destination address from static peers, source address for local interfaces and path name from path groups.
    """

    def create(self) -> Iterator[VerifySpecificPath.Input]:
        """Generate the inputs for the `VerifySpecificPath` test."""
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
                source_ip = self._get_interface_ip(interface.name)
                if not source_ip:
                    continue

                for static_peer in path_group.static_peers:
                    all_dps_paths.extend(self._create_dps_paths(path_group.name, source_ip, static_peer))

        if not all_dps_paths:
            self.logger_adapter.debug(LogMessage.NO_INPUTS_GENERATED)
            return

        yield VerifySpecificPath.Input(paths=natural_sort(all_dps_paths, sort_key="peer"))

    def _get_interface_ip(self, interface_name: str) -> IPv4Address | None:
        """
        Retrieve and validate the IPv4 address of a path group local interface.

        Return None if the interface is not found, is DHCP, or is not IPv4.
        """
        if interface_name.startswith("Ethernet") and interface_name in self.structured_config.ethernet_interfaces:
            ip_str = self.structured_config.ethernet_interfaces[interface_name].ip_address
        elif interface_name.startswith("Port-Channel") and interface_name in self.structured_config.port_channel_interfaces:
            ip_str = self.structured_config.port_channel_interfaces[interface_name].ip_address
        else:
            ip_str = None

        if ip_str is None:
            self.logger_adapter.debug(LogMessage.INTERFACE_NO_IP, interface=interface_name)
            return None

        if ip_str == "dhcp":
            self.logger_adapter.debug(LogMessage.INTERFACE_USING_DHCP, interface=interface_name)
            return None

        return IPv4Interface(ip_str).ip

    def _create_dps_paths(
        self, path_group_name: str, source_ip: IPv4Address, static_peer: EosCliConfigGen.RouterPathSelection.PathGroupsItem.StaticPeersItem
    ) -> Iterator[DpsPath]:
        """Yield DpsPath objects for a specific peer if valid."""
        peer_ip = ip_address(static_peer.router_ip)

        if not isinstance(peer_ip, IPv4Address):
            self.logger_adapter.debug(LogMessage.PATH_GROUP_IPV6_STATIC_PEER, peer=static_peer.router_ip, path_group=path_group_name)
            return

        for destination_address in static_peer.ipv4_addresses:
            yield DpsPath(
                peer=peer_ip,
                path_group=path_group_name,
                source_address=source_ip,
                destination_address=IPv4Address(destination_address),
            )
