# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._errors import AristaAvdInvalidInputsError, AristaAvdMissingVariableError
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from pyavd._eos_designs.eos_designs_facts.schema.protocol import EosDesignsFactsProtocol

    from . import AvdStructuredConfigOverlayProtocol


class UtilsMixin(Protocol):
    """
    Mixin Class with internal functions.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def _evpn_route_clients(self: AvdStructuredConfigOverlayProtocol) -> dict[str, dict[str, str | None]]:
        if not self.shared_utils.overlay_evpn:
            return {}

        if self.shared_utils.evpn_role != "server":
            return {}

        evpn_route_clients = {}

        for avd_peer in self.facts.evpn_route_server_clients:
            peer_facts = self.shared_utils.get_peer_facts(avd_peer)
            if (
                self.shared_utils.hostname in peer_facts.evpn_route_servers
                and peer_facts.evpn_role in ["server", "client"]
                and avd_peer not in self._evpn_route_servers
            ):
                self._append_peer(evpn_route_clients, avd_peer, peer_facts)

        return evpn_route_clients

    @cached_property
    def _evpn_route_servers(self: AvdStructuredConfigOverlayProtocol) -> dict[str, dict[str, str | None]]:
        if not self.shared_utils.overlay_evpn:
            return {}

        evpn_route_servers = {}

        for route_server in natural_sort(self.facts.evpn_route_servers):
            peer_facts = self.shared_utils.get_peer_facts(route_server)
            if peer_facts.evpn_role != "server":
                continue

            self._append_peer(evpn_route_servers, route_server, peer_facts)

        return evpn_route_servers

    # The next three should probably be moved to facts
    @cached_property
    def _is_mpls_server(self: AvdStructuredConfigOverlayProtocol) -> bool:
        return self.shared_utils.mpls_overlay_role == "server" or (self.shared_utils.evpn_role == "server" and self.shared_utils.overlay_evpn_mpls)

    def _is_peer_mpls_client(self: AvdStructuredConfigOverlayProtocol, peer_facts: EosDesignsFactsProtocol) -> bool:
        return peer_facts.mpls_overlay_role == "client" or (peer_facts.evpn_role == "client" and peer_facts.overlay.evpn_mpls)

    def _is_peer_mpls_server(self: AvdStructuredConfigOverlayProtocol, peer_facts: EosDesignsFactsProtocol) -> bool:
        return peer_facts.mpls_overlay_role == "server" or (peer_facts.evpn_role == "server" and peer_facts.overlay.evpn_mpls)

    @cached_property
    def _mpls_route_reflectors(self: AvdStructuredConfigOverlayProtocol) -> dict:
        if not (self.shared_utils.mpls_overlay_role == "client" or (self.shared_utils.evpn_role == "client" and self.shared_utils.overlay_evpn_mpls)):
            return {}

        mpls_route_reflectors = {}

        for route_reflector in natural_sort(self.facts.mpls_route_reflectors):
            if route_reflector == self.shared_utils.hostname:
                continue

            peer_facts = self.shared_utils.get_peer_facts(route_reflector)
            if not self._is_peer_mpls_server(peer_facts):
                continue

            self._append_peer(mpls_route_reflectors, route_reflector, peer_facts)

        return mpls_route_reflectors

    def _append_peer(self: AvdStructuredConfigOverlayProtocol, peers_dict: dict, peer_name: str, peer_facts: EosDesignsFactsProtocol) -> None:
        """
        Retrieve bgp_as and "overlay.peering_address" from peer_facts and append a new peer to peers_dict.

        {
            peer_name: {
                "bgp_as": bgp_as,
                "ip_address": overlay.peering_address,
                "overlay_peering_interface": "Loopback0"
            }
        }.
        """
        bgp_as = peer_facts.bgp_as
        if not (ip_address := peer_facts.overlay.peering_address):
            msg = f"switch.overlay.peering_address for {peer_name} is required."
            raise AristaAvdInvalidInputsError(msg)
        peers_dict[peer_name] = {
            "bgp_as": str(bgp_as) if bgp_as is not None else None,
            "ip_address": ip_address,
            "overlay_peering_interface": "Loopback0",
        }

    @cached_property
    def _is_wan_server_with_peers(self: AvdStructuredConfigOverlayProtocol) -> bool:
        return self.shared_utils.is_wan_server and len(self.shared_utils.filtered_wan_route_servers) > 0

    def _stun_server_profile_name(self: AvdStructuredConfigOverlayProtocol, wan_route_server_name: str, path_group_name: str, interface_name: str) -> str:
        """
        Return a string to use as the name of the stun server_profile.

        `/` are not allowed, `.` are allowed so
        Ethernet1/1.1 is transformed into Ethernet1_1.1
        """
        sanitized_interface_name = self.shared_utils.sanitize_interface_name(interface_name)
        return f"{path_group_name}-{wan_route_server_name}-{sanitized_interface_name}"

    @cached_property
    def _stun_server_profiles(self: AvdStructuredConfigOverlayProtocol) -> dict[str, EosCliConfigGen.Stun.Client.ServerProfiles]:
        """Return a dictionary of _stun_server_profiles with ip_address per local path_group."""
        stun_server_profiles: dict[str, EosCliConfigGen.Stun.Client.ServerProfiles] = {}
        for wan_route_server in self.shared_utils.filtered_wan_route_servers:
            for path_group in wan_route_server.path_groups:
                stun_server_profiles.setdefault(path_group.name, EosCliConfigGen.Stun.Client.ServerProfiles()).extend(
                    EosCliConfigGen.Stun.Client.ServerProfilesItem(
                        name=self._stun_server_profile_name(wan_route_server.hostname, path_group.name, interface.name),
                        ip_address=interface.public_ip,
                        ssl_profile=self.shared_utils.wan_stun_dtls_profile_name,
                    )
                    for interface in path_group.interfaces
                )
        return stun_server_profiles

    def _wan_ha_peer_vtep_ip(self: AvdStructuredConfigOverlayProtocol) -> str:
        peer_facts = self.shared_utils.get_peer_facts(self.shared_utils.wan_ha_peer)
        if not peer_facts.vtep_ip:
            msg = f"'vtep_ip' for host {self.shared_utils.wan_ha_peer}"
            raise AristaAvdMissingVariableError(msg)
        return peer_facts.vtep_ip
