# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ipaddress import IPv4Address, ip_interface
from typing import TYPE_CHECKING

from anta.input_models.security import IPSecPeer
from anta.tests.security import VerifyAPIHttpsSSL, VerifySpecificIPSecConn

from pyavd._anta.logs import LogMessage
from pyavd.j2filters import natural_sort

from ._base_classes import AntaTestInputFactory

if TYPE_CHECKING:
    from collections.abc import Iterator


class VerifyAPIHttpsSSLInputFactory(AntaTestInputFactory[VerifyAPIHttpsSSL.Input]):
    """
    Input factory class for the `VerifyAPIHttpsSSL` test.

    The test input `profile` is collected from the value of
    `management_api_http.https_ssl_profile` of the device structured config.
    """

    def create(self) -> Iterator[VerifyAPIHttpsSSL.Input]:
        """Generate the inputs for the `VerifyAPIHttpsSSL test."""
        if not (profile := self.structured_config.management_api_http.https_ssl_profile):
            self.logger_adapter.debug(LogMessage.NO_INPUTS_GENERATED)
            return

        yield VerifyAPIHttpsSSL.Input(profile=profile)


class VerifySpecificIPSecConnInputFactory(AntaTestInputFactory[VerifySpecificIPSecConn.Input]):
    """
    Input factory class for the `VerifySpecificIPSecConn` test.

    This factory generates test inputs for verifying IPsec connections.

    It collects `static_peers` IP addresses from the dynamic path selection
    `path_groups` to build the list of IPSec connections to verify.

    It deduplicates connections and always uses the default VRF.
    """

    def create(self) -> Iterator[VerifySpecificIPSecConn.Input]:
        """Generate the inputs for the `VerifySpecificIPSecConn` test."""
        ip_security_connections: list[IPSecPeer] = []

        added_peers: set[tuple[str, str]] = set()
        for path_group in self.structured_config.router_path_selection.path_groups:
            # Check if the path group has static peers
            if not path_group.static_peers:
                self.logger_adapter.debug(LogMessage.PATH_GROUP_NO_STATIC_PEERS, path_group=path_group.name)
                continue

            # Add static peers to the list of IP security connections
            for static_peer in path_group.static_peers:
                peer_ip = ip_interface(static_peer.router_ip).ip
                if (static_peer.router_ip, "default") not in added_peers:
                    if isinstance(peer_ip, IPv4Address):
                        ip_security_connections.append(
                            IPSecPeer(
                                peer=peer_ip,
                                vrf="default",
                            ),
                        )
                        added_peers.add((static_peer.router_ip, "default"))
                    else:
                        self.logger_adapter.debug(LogMessage.PATH_GROUP_IPV6_STATIC_PEER, peer=peer_ip, path_group=path_group.name)

        if not ip_security_connections:
            self.logger_adapter.debug(LogMessage.NO_INPUTS_GENERATED)
            return

        yield VerifySpecificIPSecConn.Input(ip_security_connections=natural_sort(ip_security_connections, sort_key="peer"))
