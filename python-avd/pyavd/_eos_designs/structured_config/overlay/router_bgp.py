# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from typing import TYPE_CHECKING, Literal, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import AvdStringFormatter, default, strip_empties_from_dict
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigOverlayProtocol


class RouterBgpMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def router_bgp(self: AvdStructuredConfigOverlayProtocol) -> None:
        """Set the structured config for router_bgp."""
        if self.shared_utils.overlay_cvx:
            return

        if self.shared_utils.overlay_dpath is True:
            self.structured_config.router_bgp.bgp.bestpath.d_path = True
        self._set_bgp_cluster_id()
        self._set_bgp_listen_ranges()
        self._set_peer_groups()
        self._set_address_family_evpn()
        self._set_address_family_ipv4()
        self._set_address_family_ipv4_sr_te()
        self._set_address_family_link_state()
        self._set_address_family_path_selection()
        self._set_address_family_rtc()
        self._set_address_family_vpn_ipvx(4)
        self._set_address_family_vpn_ipvx(6)
        self._set_neighbors()

    def _set_bgp_cluster_id(self: AvdStructuredConfigOverlayProtocol) -> None:
        if (
            self.shared_utils.overlay_routing_protocol == "ibgp"
            and (self.shared_utils.evpn_role == "server" or self.shared_utils.mpls_overlay_role == "server")
        ) or self.shared_utils.is_wan_server:
            self.structured_config.router_bgp.bgp_cluster_id = default(self.shared_utils.node_config.bgp_cluster_id, self.shared_utils.router_id)

    def _set_bgp_listen_ranges(self: AvdStructuredConfigOverlayProtocol) -> None:
        """Set listen-ranges. Currently only supported for WAN RR."""
        if not self.shared_utils.is_wan_server:
            return

        for prefix in self.shared_utils.wan_listen_ranges:
            self.structured_config.router_bgp.listen_ranges.append_new(
                prefix=prefix, peer_group=self.inputs.bgp_peer_groups.wan_overlay_peers.name, remote_as=self.shared_utils.bgp_as
            )

    def _generate_base_peer_group(
        self: AvdStructuredConfigOverlayProtocol,
        pg_type: str,
        pg_name: str,
        maximum_routes: int = 0,
        update_source: str = "Loopback0",
    ) -> EosCliConfigGen.RouterBgp.PeerGroupsItem:
        peer_group = getattr(self.inputs.bgp_peer_groups, pg_name)

        if peer_group.structured_config:
            self.custom_structured_configs.nested.router_bgp.peer_groups.obtain(peer_group.name)._deepmerge(
                peer_group.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
            )

        return EosCliConfigGen.RouterBgp.PeerGroupsItem(
            name=peer_group.name,
            type=pg_type,
            update_source=update_source,
            bfd=peer_group.bfd,
            password=peer_group.password,
            send_community="all",
            maximum_routes=maximum_routes,
        )

    def _set_peer_groups(self: AvdStructuredConfigOverlayProtocol) -> None:
        peer_groups = self.structured_config.router_bgp.peer_groups
        if self.shared_utils.overlay_routing_protocol == "ebgp":
            # EVPN OVERLAY peer group
            ebgp_overlay_peer_group = self._generate_base_peer_group("evpn", "evpn_overlay_peers")
            ebgp_overlay_peer_group.ebgp_multihop = self.inputs.evpn_ebgp_multihop

            if self.shared_utils.evpn_role == "server":
                ebgp_overlay_peer_group.next_hop_unchanged = True

            peer_groups.append(ebgp_overlay_peer_group)

            if self.shared_utils.node_config.evpn_gateway.evpn_l2.enabled or self.shared_utils.node_config.evpn_gateway.evpn_l3.enabled:
                evpn_overlay_core_peer_group = self._generate_base_peer_group("evpn", "evpn_overlay_core")
                evpn_overlay_core_peer_group.ebgp_multihop = self.inputs.evpn_ebgp_gateway_multihop
                peer_groups.append(evpn_overlay_core_peer_group)

        elif self.shared_utils.overlay_routing_protocol == "ibgp":
            if self.shared_utils.overlay_mpls is True:
                # MPLS OVERLAY peer group
                mpls_peer_group = self._generate_base_peer_group("mpls", "mpls_overlay_peers")
                mpls_peer_group.remote_as = self.shared_utils.bgp_as

                if self.shared_utils.mpls_overlay_role == "server" or (self.shared_utils.evpn_role == "server" and self.shared_utils.overlay_evpn_mpls is True):
                    mpls_peer_group.route_reflector_client = True

                peer_groups.append(mpls_peer_group)

            # TODO: AVD 6.0.0 remove the check for WAN routers.
            if self.shared_utils.overlay_evpn_vxlan is True and (not self.shared_utils.is_wan_router or self.inputs.wan_use_evpn_node_settings_for_lan):
                evpn_overlay_peer_group = self._generate_base_peer_group("evpn", "evpn_overlay_peers")
                evpn_overlay_peer_group.remote_as = self.shared_utils.bgp_as
                # EVPN OVERLAY peer group - also in EBGP..
                if self.shared_utils.evpn_role == "server":
                    evpn_overlay_peer_group.route_reflector_client = True
                peer_groups.append(evpn_overlay_peer_group)

            # RR Overlay peer group rendered either for MPLS route servers
            if self._is_mpls_server is True:
                rr_overlay_peer_group = self._generate_base_peer_group("mpls", "rr_overlay_peers")
                rr_overlay_peer_group.remote_as = self.shared_utils.bgp_as
                peer_groups.append(rr_overlay_peer_group)

        # Always render the WAN routers
        # TODO: probably should move from overlay
        if self.shared_utils.is_wan_router:
            # WAN OVERLAY peer group only is supported iBGP
            wan_overlay_peer_group = self._generate_base_peer_group("wan", "wan_overlay_peers", update_source=self.shared_utils.vtep_loopback)
            wan_overlay_peer_group._update(remote_as=self.shared_utils.bgp_as, ttl_maximum_hops=self.inputs.bgp_peer_groups.wan_overlay_peers.ttl_maximum_hops)
            if self.shared_utils.is_wan_server:
                wan_overlay_peer_group.route_reflector_client = True

            bfd_timers_item = self.inputs.bgp_peer_groups.wan_overlay_peers.bfd_timers
            wan_overlay_peer_group.bfd_timers._update(interval=bfd_timers_item.interval, min_rx=bfd_timers_item.min_rx, multiplier=bfd_timers_item.multiplier)
            peer_groups.append(wan_overlay_peer_group)

            if self._is_wan_server_with_peers:
                wan_rr_overlay_peer_group = self._generate_base_peer_group("wan", "wan_rr_overlay_peers", update_source=self.shared_utils.vtep_loopback)
                wan_rr_overlay_peer_group._update(
                    remote_as=self.shared_utils.bgp_as,
                    ttl_maximum_hops=self.inputs.bgp_peer_groups.wan_rr_overlay_peers.ttl_maximum_hops,
                    route_reflector_client=True,
                )

                bfd_timers_item = self.inputs.bgp_peer_groups.wan_rr_overlay_peers.bfd_timers
                # We have to apply the attributes individually to get the defaults from the input class.
                wan_rr_overlay_peer_group.bfd_timers._update(
                    interval=bfd_timers_item.interval, min_rx=bfd_timers_item.min_rx, multiplier=bfd_timers_item.multiplier
                )
                peer_groups.append(wan_rr_overlay_peer_group)

        # same for ebgp and ibgp
        if self.shared_utils.overlay_ipvpn_gateway is True:
            ipvpn_gateway_peer_group = self._generate_base_peer_group("mpls", "ipvpn_gateway_peers")
            ipvpn_gateway_peer_group._update(
                local_as=self.shared_utils.node_config.ipvpn_gateway.local_as, maximum_routes=self.shared_utils.node_config.ipvpn_gateway.maximum_routes
            )
            peer_groups.append(ipvpn_gateway_peer_group)

    def _set_address_family_ipv4(self: AvdStructuredConfigOverlayProtocol) -> None:
        """Deactivate the relevant peer_groups in address_family_ipv4."""
        peer_groups = self.structured_config.router_bgp.address_family_ipv4.peer_groups
        if self.shared_utils.is_wan_router:
            peer_groups.append_new(name=self.inputs.bgp_peer_groups.wan_overlay_peers.name, activate=False)
            if self._is_wan_server_with_peers:
                peer_groups.append_new(name=self.inputs.bgp_peer_groups.wan_rr_overlay_peers.name, activate=False)

        # TODO: no elif
        elif self.shared_utils.overlay_evpn_vxlan is True:
            peer_groups.append_new(name=self.inputs.bgp_peer_groups.evpn_overlay_peers.name, activate=False)

        if self.shared_utils.overlay_routing_protocol == "ebgp" and (
            self.shared_utils.node_config.evpn_gateway.evpn_l2.enabled or self.shared_utils.node_config.evpn_gateway.evpn_l3.enabled
        ):
            peer_groups.append_new(name=self.inputs.bgp_peer_groups.evpn_overlay_core.name, activate=False)

        if self.shared_utils.overlay_routing_protocol == "ibgp":
            if self.shared_utils.overlay_mpls is True:
                peer_groups.append_new(name=self.inputs.bgp_peer_groups.mpls_overlay_peers.name, activate=False)

            if self._is_mpls_server is True:
                peer_groups.append_new(name=self.inputs.bgp_peer_groups.rr_overlay_peers.name, activate=False)

        if self.shared_utils.overlay_ipvpn_gateway is True:
            peer_groups.append_new(name=self.inputs.bgp_peer_groups.ipvpn_gateway_peers.name, activate=False)

    def _set_address_family_evpn(self: AvdStructuredConfigOverlayProtocol) -> None:
        peer_groups = self.structured_config.router_bgp.address_family_evpn.peer_groups
        if self.shared_utils.is_wan_router:
            wan_overlay_peer_group = EosCliConfigGen.RouterBgp.AddressFamilyEvpn.PeerGroupsItem(
                name=self.inputs.bgp_peer_groups.wan_overlay_peers.name,
                activate=True,
                encapsulation=self.inputs.wan_encapsulation,
            )
            if self.shared_utils.wan_role != "server":
                wan_overlay_peer_group._update(
                    route_map_in="RM-EVPN-SOO-IN",
                    route_map_out="RM-EVPN-SOO-OUT",
                )
            peer_groups.append(wan_overlay_peer_group)

        if self.shared_utils.overlay_routing_protocol == "ebgp":
            if self.shared_utils.node_config.evpn_gateway.evpn_l2.enabled or self.shared_utils.node_config.evpn_gateway.evpn_l3.enabled:
                peer_groups.append_new(
                    name=self.inputs.bgp_peer_groups.evpn_overlay_core.name,
                    domain_remote=True,
                    activate=True,
                )

            if self.shared_utils.node_config.evpn_gateway.evpn_l3.enabled:
                self.structured_config.router_bgp.address_family_evpn.neighbor_default.next_hop_self_received_evpn_routes._update(
                    enable=True, inter_domain=self.shared_utils.node_config.evpn_gateway.evpn_l3.inter_domain
                )

        overlay_peer_group = EosCliConfigGen.RouterBgp.AddressFamilyEvpn.PeerGroupsItem()
        if self.shared_utils.overlay_evpn_vxlan is True:
            overlay_peer_group._update(name=self.inputs.bgp_peer_groups.evpn_overlay_peers.name, activate=True)

        if self.shared_utils.overlay_routing_protocol == "ibgp":
            # TODO: - assess this condition - both can't be true at the same time.
            if self.shared_utils.overlay_evpn_mpls is True and self.shared_utils.overlay_evpn_vxlan is not True:
                overlay_peer_group._update(name=self.inputs.bgp_peer_groups.mpls_overlay_peers.name, activate=True)
                self.structured_config.router_bgp.address_family_evpn.neighbor_default.encapsulation = "mpls"
                if self.shared_utils.overlay_ler is True:
                    self.structured_config.router_bgp.address_family_evpn.neighbor_default.next_hop_self_source_interface = "Loopback0"

                if self._is_mpls_server is True:
                    peer_groups.append_new(name=self.inputs.bgp_peer_groups.rr_overlay_peers.name, activate=True)

            # TODO: this is written for matching either evpn_mpls or evpn_vlxan based for iBGP see if we cannot make this better.
            if self.shared_utils.overlay_vtep is True and self.shared_utils.evpn_role != "server" and overlay_peer_group:
                overlay_peer_group._update(
                    route_map_in="RM-EVPN-SOO-IN",
                    route_map_out="RM-EVPN-SOO-OUT",
                )
        if overlay_peer_group:
            peer_groups.append(overlay_peer_group)

        # host flap detection & route pruning
        if self.shared_utils.overlay_vtep is True:
            if self.inputs.evpn_hostflap_detection:
                self.structured_config.router_bgp.address_family_evpn.evpn_hostflap_detection._update(
                    window=self.inputs.evpn_hostflap_detection.window,
                    threshold=self.inputs.evpn_hostflap_detection.threshold,
                    enabled=self.inputs.evpn_hostflap_detection.enabled,
                    expiry_timeout=self.inputs.evpn_hostflap_detection.expiry_timeout,
                )
            if self.inputs.evpn_import_pruning:
                self.structured_config.router_bgp.address_family_evpn.route.import_match_failure_action = "discard"

        if self.shared_utils.overlay_dpath is True:
            self.structured_config.router_bgp.address_family_evpn.domain_identifier = self.shared_utils.node_config.ipvpn_gateway.evpn_domain_id

        if self.shared_utils.is_wan_server:
            self.structured_config.router_bgp.address_family_evpn.next_hop.resolution_disabled = True

            if self._is_wan_server_with_peers:
                peer_groups.append_new(
                    name=self.inputs.bgp_peer_groups.wan_rr_overlay_peers.name,
                    activate=True,
                    encapsulation=self.inputs.wan_encapsulation,
                )

        # Activitating HA iBGP session for WAN HA
        if self.shared_utils.wan_ha:
            self.structured_config.router_bgp.address_family_evpn.neighbor_default.next_hop_self_received_evpn_routes.enable = True
            self.structured_config.router_bgp.address_family_evpn.neighbors.append_new(
                ip_address=self._wan_ha_peer_vtep_ip(),
                activate=True,
                encapsulation=self.inputs.wan_encapsulation,
            )

    def _set_address_family_ipv4_sr_te(self: AvdStructuredConfigOverlayProtocol) -> None:
        """Set the structured config for IPv4 SR-TE address family."""
        if not self.shared_utils.is_cv_pathfinder_router:
            return

        peer_groups = self.structured_config.router_bgp.address_family_ipv4_sr_te.peer_groups

        peer_groups.append_new(name=self.inputs.bgp_peer_groups.wan_overlay_peers.name, activate=True)

        if self._is_wan_server_with_peers:
            peer_groups.append_new(name=self.inputs.bgp_peer_groups.wan_rr_overlay_peers.name, activate=True)

    def _set_address_family_link_state(self: AvdStructuredConfigOverlayProtocol) -> None:
        """Set the structured config for link-state address family."""
        if not self.shared_utils.is_cv_pathfinder_router:
            return

        peer_groups = self.structured_config.router_bgp.address_family_link_state.peer_groups
        peer_group_obj = EosCliConfigGen.RouterBgp.AddressFamilyLinkState.PeerGroupsItem(name=self.inputs.bgp_peer_groups.wan_overlay_peers.name, activate=True)

        if self.shared_utils.is_cv_pathfinder_server:
            self.structured_config.router_bgp.address_family_link_state.path_selection.roles._update(consumer=True, propagator=True)
            peer_group_obj.missing_policy.direction_out_action = "deny"
        else:  # other roles are transit / edge
            self.structured_config.router_bgp.address_family_link_state.path_selection.roles.producer = True
        peer_groups.append(peer_group_obj)

        if self._is_wan_server_with_peers:
            peer_groups.append_new(name=self.inputs.bgp_peer_groups.wan_rr_overlay_peers.name, activate=True)

    def _set_address_family_path_selection(self: AvdStructuredConfigOverlayProtocol) -> None:
        if not self.shared_utils.is_wan_router:
            return

        peer_groups = self.structured_config.router_bgp.address_family_path_selection.peer_groups
        peer_groups.append_new(name=self.inputs.bgp_peer_groups.wan_overlay_peers.name, activate=True)

        self.structured_config.router_bgp.address_family_path_selection.bgp.additional_paths._update(receive=True, send="any")

        if self._is_wan_server_with_peers:
            peer_groups.append_new(name=self.inputs.bgp_peer_groups.wan_rr_overlay_peers.name, activate=True)

    def _set_address_family_rtc(self: AvdStructuredConfigOverlayProtocol) -> None:
        """
        Activate EVPN OVERLAY peer group and EVPN OVERLAY CORE peer group (if present) in address_family_rtc.

        if the evpn_role is server, enable default_route_target only
        """
        if not self.inputs.evpn_overlay_bgp_rtc:
            return
        peer_groups = self.structured_config.router_bgp.address_family_rtc.peer_groups
        peer_groups_evpn = EosCliConfigGen.RouterBgp.AddressFamilyRtc.PeerGroupsItem()
        if self.shared_utils.overlay_evpn_vxlan is True:
            peer_groups_evpn.name = self.inputs.bgp_peer_groups.evpn_overlay_peers.name
            peer_groups_evpn.activate = True

        if self.shared_utils.overlay_routing_protocol == "ebgp":
            if self.shared_utils.node_config.evpn_gateway.evpn_l2.enabled or self.shared_utils.node_config.evpn_gateway.evpn_l3.enabled:
                peer_group_obj = EosCliConfigGen.RouterBgp.AddressFamilyRtc.PeerGroupsItem(
                    name=self.inputs.bgp_peer_groups.evpn_overlay_core.name, activate=True
                )
                # TODO: (@Claus) told me to remove this
                if self.shared_utils.evpn_role == "server":
                    peer_group_obj.default_route_target.only = True
                peer_groups.append(peer_group_obj)

            # Transposing the Jinja2 logic: if the evpn_overlay_core peer group is not
            # configured then the default_route_target is applied in the evpn_overlay_peers peer group.
            elif self.shared_utils.evpn_role == "server":
                peer_groups_evpn.default_route_target.only = True

        if self.shared_utils.overlay_routing_protocol == "ibgp":
            if self.shared_utils.overlay_mpls is True:
                peer_group_obj = EosCliConfigGen.RouterBgp.AddressFamilyRtc.PeerGroupsItem(
                    name=self.inputs.bgp_peer_groups.mpls_overlay_peers.name, activate=True
                )
                if self.shared_utils.evpn_role == "server" or self.shared_utils.mpls_overlay_role == "server":
                    peer_group_obj.default_route_target.only = True
                peer_groups.append(peer_group_obj)

            if self.shared_utils.overlay_evpn_vxlan is True and (self.shared_utils.evpn_role == "server" or self.shared_utils.mpls_overlay_role == "server"):
                peer_groups_evpn.default_route_target.only = True
        if peer_groups_evpn:
            peer_groups.append(peer_groups_evpn)

    def _set_address_family_vpn_ipvx(self: AvdStructuredConfigOverlayProtocol, version: Literal[4, 6]) -> None:
        if (version == 4 and self.shared_utils.overlay_vpn_ipv4 is not True) or (version == 6 and self.shared_utils.overlay_vpn_ipv6 is not True):
            return

        af_vpn = self.structured_config.router_bgp.address_family_vpn_ipv4 if version == 4 else self.structured_config.router_bgp.address_family_vpn_ipv6

        if self.shared_utils.overlay_ler or self.shared_utils.overlay_ipvpn_gateway:
            af_vpn.neighbor_default_encapsulation_mpls_next_hop_self.source_interface = "Loopback0"

        if self.shared_utils.overlay_ipvpn_gateway:
            af_vpn.peer_groups.append_new(name=self.inputs.bgp_peer_groups.ipvpn_gateway_peers.name, activate=True)

        if self.shared_utils.overlay_routing_protocol == "ibgp":
            if self.shared_utils.overlay_mpls:
                af_vpn.peer_groups.append_new(name=self.inputs.bgp_peer_groups.mpls_overlay_peers.name, activate=True)

            if self.shared_utils.mpls_overlay_role == "server":
                af_vpn.peer_groups.append_new(name=self.inputs.bgp_peer_groups.rr_overlay_peers.name, activate=True)

        if self.shared_utils.overlay_dpath:
            af_vpn.domain_identifier = self.shared_utils.node_config.ipvpn_gateway.ipvpn_domain_id

    def _create_neighbor(
        self: AvdStructuredConfigOverlayProtocol,
        ip_address: str,
        name: str,
        peer_group: str,
        remote_as: str | None = None,
        overlay_peering_interface: str | None = None,
    ) -> EosCliConfigGen.RouterBgp.NeighborsItem:
        """Returns a BGP neighbor instance based on the given arguments."""
        neighbor = EosCliConfigGen.RouterBgp.NeighborsItem(
            ip_address=ip_address,
            peer_group=peer_group,
            peer=name,
            description=AvdStringFormatter().format(
                self.inputs.overlay_bgp_peer_description, **strip_empties_from_dict({"peer": name, "peer_interface": overlay_peering_interface})
            ),
        )

        if remote_as is not None:
            neighbor.remote_as = remote_as

        if self.inputs.shutdown_bgp_towards_undeployed_peers and name in self.facts.evpn_route_server_clients:
            peer_facts = self.shared_utils.get_peer_facts(name)
            if not peer_facts.is_deployed:
                neighbor.shutdown = True

        return neighbor

    def _set_neighbors(self: AvdStructuredConfigOverlayProtocol) -> None:
        neighbors = self.structured_config.router_bgp.neighbors
        if self.shared_utils.overlay_routing_protocol == "ebgp":
            for route_server, data in natural_sort(self._evpn_route_servers.items()):
                neighbor = self._create_neighbor(
                    data["ip_address"],
                    route_server,
                    self.inputs.bgp_peer_groups.evpn_overlay_peers.name,
                    remote_as=data["bgp_as"],
                    overlay_peering_interface=data.get("overlay_peering_interface"),
                )

                if self.inputs.evpn_prevent_readvertise_to_server:
                    neighbor.route_map_out = f"RM-EVPN-FILTER-AS{data['bgp_as']}"
                neighbors.append(neighbor)

            for route_client, data in natural_sort(self._evpn_route_clients.items()):
                neighbor = self._create_neighbor(
                    data["ip_address"],
                    route_client,
                    self.inputs.bgp_peer_groups.evpn_overlay_peers.name,
                    remote_as=data["bgp_as"],
                    overlay_peering_interface=data.get("overlay_peering_interface"),
                )
                neighbors.append(neighbor)

            self._set_evpn_gateway_remote_peers()

        if self.shared_utils.overlay_routing_protocol == "ibgp":
            if self.shared_utils.overlay_mpls is True:
                for route_reflector, data in natural_sort(self._mpls_route_reflectors.items()):
                    neighbor = self._create_neighbor(
                        data["ip_address"],
                        route_reflector,
                        self.inputs.bgp_peer_groups.mpls_overlay_peers.name,
                        overlay_peering_interface=data.get("overlay_peering_interface"),
                    )
                    neighbors.append(neighbor)

                self._set_mpls_route_clients()

                self._set_mpls_mesh_pe()

                self._set_mpls_rr_peers()

            if self.shared_utils.overlay_evpn_vxlan is True:
                for route_server, data in natural_sort(self._evpn_route_servers.items()):
                    neighbor = self._create_neighbor(
                        data["ip_address"],
                        route_server,
                        self.inputs.bgp_peer_groups.evpn_overlay_peers.name,
                        overlay_peering_interface=data.get("overlay_peering_interface"),
                    )
                    neighbors.append(neighbor)

                for route_client, data in natural_sort(self._evpn_route_clients.items()):
                    neighbor = self._create_neighbor(
                        data["ip_address"],
                        route_client,
                        self.inputs.bgp_peer_groups.evpn_overlay_peers.name,
                        overlay_peering_interface=data.get("overlay_peering_interface"),
                    )
                    neighbors.append(neighbor)

        if self.shared_utils.is_wan_client:
            if not self._ip_in_listen_ranges(self.shared_utils.vtep_ip, self.shared_utils.wan_listen_ranges):
                msg = f"{self.shared_utils.vtep_loopback} IP {self.shared_utils.vtep_ip} is not in the Route Reflector listen range prefixes"
                raise AristaAvdError(msg)
            for wan_route_server in self.shared_utils.filtered_wan_route_servers:
                neighbor = self._create_neighbor(
                    wan_route_server.vtep_ip,
                    wan_route_server.hostname,
                    self.inputs.bgp_peer_groups.wan_overlay_peers.name,
                    overlay_peering_interface=self.shared_utils.vtep_loopback,
                )
                neighbors.append(neighbor)

            if self.shared_utils.wan_ha:
                neighbors.append_new(
                    ip_address=self._wan_ha_peer_vtep_ip(),
                    peer=self.shared_utils.wan_ha_peer,
                    description=self.shared_utils.wan_ha_peer,
                    remote_as=self.shared_utils.bgp_as,
                    update_source="Dps1",
                    route_reflector_client=True,
                    send_community="all",
                    route_map_in="RM-WAN-HA-PEER-IN",
                    route_map_out="RM-WAN-HA-PEER-OUT",
                )

        elif self.shared_utils.is_wan_server:
            # No neighbor configured on the `wan_overlay_peers` peer group as it is covered by listen ranges
            for wan_route_server in self.shared_utils.filtered_wan_route_servers:
                neighbor = self._create_neighbor(
                    wan_route_server.vtep_ip,
                    wan_route_server.hostname,
                    self.inputs.bgp_peer_groups.wan_rr_overlay_peers.name,
                    overlay_peering_interface=self.shared_utils.vtep_loopback,
                )
                neighbors.append(neighbor)

        self._set_ipvpn_gateway_remote_peers()

    def _ip_in_listen_ranges(
        self: AvdStructuredConfigOverlayProtocol, source_ip: str, listen_range_prefixes: EosDesigns.BgpPeerGroups.WanOverlayPeers.ListenRangePrefixes
    ) -> bool:
        """Check if our source IP is in any of the listen range prefixes."""
        ip = ipaddress.ip_address(source_ip)
        return any(ip in ipaddress.ip_network(prefix) for prefix in listen_range_prefixes)

    def _set_evpn_gateway_remote_peers(self: AvdStructuredConfigOverlayProtocol) -> None:
        if not self.shared_utils.overlay_evpn:
            return

        for remote_peer in self.shared_utils.node_config.evpn_gateway.remote_peers._natural_sorted():
            remote_peer_name = remote_peer.hostname

            peer_facts = self.shared_utils.get_peer_facts(remote_peer_name, required=False)
            if peer_facts is None:
                # No matching host found in the inventory for this remote gateway
                bgp_as = remote_peer.bgp_as
                ip_address = remote_peer.ip_address
                overlay_peering_address = None
            else:
                # Found a matching name for this remote gateway in the inventory
                # Apply potential override if present in the input variables
                bgp_as = remote_peer.bgp_as or peer_facts.bgp_as
                if not (ip_address := remote_peer.ip_address or peer_facts.overlay.peering_address):
                    msg = f"Unable to determine the remote IP address to use for the EVPN Gateway peer '{remote_peer_name}'."
                    raise AristaAvdInvalidInputsError(msg)
                overlay_peering_address = "Loopback0"

            # In both cases if any key is missing raise
            if bgp_as is None or ip_address is None:
                msg = f"The EVPN Gateway remote peer '{remote_peer_name}' is missing either `bgp_as` or `ip_address`."
                raise AristaAvdError(msg)

            neighbor = self._create_neighbor(ip_address, remote_peer_name, self.inputs.bgp_peer_groups.evpn_overlay_core.name, bgp_as, overlay_peering_address)
            self.structured_config.router_bgp.neighbors.append(neighbor)

    def _set_ipvpn_gateway_remote_peers(self: AvdStructuredConfigOverlayProtocol) -> None:
        if not self.shared_utils.overlay_ipvpn_gateway:
            return

        for remote_peer in self.shared_utils.node_config.ipvpn_gateway.remote_peers._natural_sorted():
            # These remote gw are outside of the inventory
            neighbor = self._create_neighbor(
                remote_peer.ip_address,
                remote_peer.hostname,
                self.inputs.bgp_peer_groups.ipvpn_gateway_peers.name,
                remote_peer.bgp_as,
            )
            if remote_peer.bgp_as != default(self.shared_utils.node_config.ipvpn_gateway.local_as, self.shared_utils.bgp_as):
                neighbor.ebgp_multihop = self.inputs.evpn_ebgp_gateway_multihop

            self.structured_config.router_bgp.neighbors.append(neighbor)

    def _set_mpls_route_clients(self: AvdStructuredConfigOverlayProtocol) -> None:
        if self._is_mpls_server is not True:
            return

        for route_reflector_client in natural_sort(self.facts.mpls_route_reflector_clients):
            if route_reflector_client in self._mpls_route_reflectors:
                continue

            peer_facts = self.shared_utils.get_peer_facts(route_reflector_client)
            if not self._is_peer_mpls_client(peer_facts):
                continue

            if not (ip_address := peer_facts.overlay.peering_address):
                msg = f"Unable to determine the remote IP address to use for the MPLS Route Reflector client '{route_reflector_client}'."
                raise AristaAvdInvalidInputsError(msg)

            neighbor = self._create_neighbor(
                ip_address,
                route_reflector_client,
                self.inputs.bgp_peer_groups.mpls_overlay_peers.name,
                overlay_peering_interface="Loopback0",
            )

            self.structured_config.router_bgp.neighbors.append(neighbor)

    def _set_mpls_mesh_pe(self: AvdStructuredConfigOverlayProtocol) -> None:
        if not self.shared_utils.overlay_mpls or not self.inputs.bgp_mesh_pes:
            return

        for fabric_switch in natural_sort(self.shared_utils.all_fabric_devices):
            if fabric_switch in self._mpls_route_reflectors:
                continue
            if fabric_switch == self.shared_utils.hostname:
                continue

            peer_facts = self.shared_utils.get_peer_facts(fabric_switch)
            if not self._is_peer_mpls_client(peer_facts):
                continue

            if not (ip_address := peer_facts.overlay.peering_address):
                msg = f"Unable to determine the remote IP address to use for the MPLS PE '{fabric_switch}'."
                raise AristaAvdInvalidInputsError(msg)
            neighbor = self._create_neighbor(
                ip_address,
                fabric_switch,
                self.inputs.bgp_peer_groups.mpls_overlay_peers.name,
                overlay_peering_interface="Loopback0",
            )
            self.structured_config.router_bgp.neighbors.append(neighbor)

    def _set_mpls_rr_peers(self: AvdStructuredConfigOverlayProtocol) -> None:
        if self._is_mpls_server is not True:
            return

        for route_reflector in self.facts.mpls_route_reflectors:
            if route_reflector == self.shared_utils.hostname:
                continue

            peer_facts = self.shared_utils.get_peer_facts(route_reflector)
            if not self._is_peer_mpls_server(peer_facts):
                continue

            if not (ip_address := peer_facts.overlay.peering_address):
                msg = f"Unable to determine the remote IP address to use for the peer MPLS Route Reflector '{route_reflector}'."
                raise AristaAvdInvalidInputsError(msg)

            neighbor = self._create_neighbor(
                ip_address,
                route_reflector,
                self.inputs.bgp_peer_groups.rr_overlay_peers.name,
                overlay_peering_interface="Loopback0",
            )
            self.structured_config.router_bgp.neighbors.append(neighbor)

        for route_reflector_client in self.facts.mpls_route_reflector_clients:
            if route_reflector_client in self.facts.mpls_route_reflectors:
                continue

            peer_facts = self.shared_utils.get_peer_facts(route_reflector_client)
            if not self._is_peer_mpls_server(peer_facts):
                continue

            if not (ip_address := peer_facts.overlay.peering_address):
                msg = f"Unable to determine the remote IP address to use for the peer MPLS Route Reflector '{route_reflector_client}'."
                raise AristaAvdInvalidInputsError(msg)

            neighbor = self._create_neighbor(
                ip_address,
                route_reflector_client,
                self.inputs.bgp_peer_groups.rr_overlay_peers.name,
                overlay_peering_interface="Loopback0",
            )
            self.structured_config.router_bgp.neighbors.append(neighbor)
