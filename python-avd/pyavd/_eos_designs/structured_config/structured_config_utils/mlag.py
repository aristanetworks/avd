# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils.format_string import AvdStringFormatter
from pyavd._utils.run_once import run_once_method

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import StructuredConfigUtilsProtocol


class MlagMixin(Protocol):
    @run_once_method
    def set_once_route_map_mlag_peer_in(self: StructuredConfigUtilsProtocol) -> None:
        """
        Set route-map RM-MLAG-PEER-IN.

        Makes routes learned over the MLAG Peer-link less preferred on spines
        to ensure optimal routing by setting origin to incomplete.
        """
        route_map = EosCliConfigGen.RouteMapsItem(name="RM-MLAG-PEER-IN")
        route_map.sequence_numbers.append_new(
            sequence=10,
            type="permit",
            description="Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing",
            set=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set(["origin incomplete"]),
        )
        self.structured_config.route_maps.append(route_map)

    @run_once_method
    def set_once_peer_group_mlag_ipv4_underlay_peer(self: StructuredConfigUtilsProtocol) -> None:
        """
        Set router_bgp structured_config covering the MLAG peer_group and associated address_family activations.

        This is called from:
        - MLAG in the case of BGP underlay routing protocol.
        - Network services in the case of iBGP MLAG peering for VRFs

        """
        bgp_peer_group = self.inputs.bgp_peer_groups.mlag_ipv4_underlay_peer
        self.set_mlag_peer_group(bgp_peer_group)
        if not self.shared_utils.underlay_ipv6_numbered:
            address_family_ipv4_peer_groups = self.structured_config.router_bgp.address_family_ipv4.peer_groups.append_new(
                name=bgp_peer_group.name, activate=True
            )
            if self.inputs.underlay_rfc5549:
                address_family_ipv4_peer_groups.next_hop.address_family_ipv6._update(enabled=True, originate=True)
        if self.shared_utils.underlay_ipv6:
            self.structured_config.router_bgp.address_family_ipv6.peer_groups.append_new(name=bgp_peer_group.name, activate=True)

    @run_once_method
    def set_once_peer_group_mlag_ipv4_vrfs_peer(self: StructuredConfigUtilsProtocol) -> None:
        """Set router_bgp structured_config covering the MLAG peer_group(s) in case there are VRFs with iBGP peerings using a separate peer-group."""
        bgp_peer_group = self.inputs.bgp_peer_groups.mlag_ipv4_vrfs_peer
        self.set_mlag_peer_group(bgp_peer_group)
        if (
            self.inputs.avd_design_future.fix_mlag_vrf_peer_group_address_families
            and self.shared_utils.underlay_ipv6_numbered
            and not self.inputs.overlay_mlag_rfc5549
        ):
            # Without the IPv6 next hop, IPv4 routes received over the IPv6 session are dropped by EOS.
            return
        address_family_ipv4_peer_groups = self.structured_config.router_bgp.address_family_ipv4.peer_groups.append_new(name=bgp_peer_group.name, activate=True)
        if self.inputs.overlay_mlag_rfc5549:
            address_family_ipv4_peer_groups.next_hop.address_family_ipv6._update(enabled=True, originate=True)

    @run_once_method
    def set_once_mlag_vrfs_peer_group_address_families(self: StructuredConfigUtilsProtocol) -> None:
        """
        Set the address families of the MLAG peer group used for iBGP peerings in VRFs, when these sessions run over IPv6.

        Raise when these sessions run over IPv4 with `overlay_mlag_rfc5549` or `underlay_ipv6`, since they cannot carry the requested routes.

        Only active with `avd_design_future.fix_mlag_vrf_peer_group_address_families`.

        This is called from network services when the device has at least one MLAG iBGP peering in a VRF,
        after the peer group itself has been set by `set_once_peer_group_mlag_ipv4_underlay_peer` or `set_once_peer_group_mlag_ipv4_vrfs_peer`.
        """
        if not self.inputs.avd_design_future.fix_mlag_vrf_peer_group_address_families:
            return

        ipv6_session = (self.inputs.underlay_rfc5549 and self.inputs.overlay_mlag_rfc5549) or self.shared_utils.underlay_ipv6_numbered
        if not ipv6_session:
            if self.inputs.overlay_mlag_rfc5549:
                msg = (
                    "Invalid combination of inputs. 'overlay_mlag_rfc5549: true' requires 'underlay_rfc5549: true' or 'underlay_ipv6_numbered: true' "
                    "when 'avd_design_future.fix_mlag_vrf_peer_group_address_families' is enabled."
                )
                raise AristaAvdInvalidInputsError(msg)
            if self.shared_utils.underlay_ipv6:
                msg = (
                    "Invalid combination of inputs. IPv6 routes requested with 'underlay_ipv6: true' cannot be carried over the MLAG iBGP peerings in VRFs, "
                    "since these sessions run over IPv4. "
                    "With 'underlay_rfc5549: true', set 'overlay_mlag_rfc5549: true' to run these sessions over IPv6. "
                    "Otherwise, this combination is not supported yet when 'avd_design_future.fix_mlag_vrf_peer_group_address_families' is enabled."
                )
                raise AristaAvdInvalidInputsError(msg)
            return

        peer_group_name = self.shared_utils.mlag_vrfs_peer_group_name
        if self.inputs.overlay_mlag_rfc5549:
            address_family_ipv4_peer_group = self.structured_config.router_bgp.address_family_ipv4.peer_groups.obtain(peer_group_name)
            address_family_ipv4_peer_group.activate = True
            address_family_ipv4_peer_group.next_hop.address_family_ipv6._update(enabled=True, originate=True)
            if not self.shared_utils.use_separate_peer_group_for_mlag_vrfs:
                # The shared peer group also carries the underlay MLAG session in the default VRF.
                self.structured_config.ip_routing_ipv6_interfaces = True
        if self.shared_utils.underlay_ipv6:
            self.structured_config.router_bgp.address_family_ipv6.peer_groups.obtain(peer_group_name).activate = True

    def set_mlag_peer_group(
        self: StructuredConfigUtilsProtocol, bgp_peer_group: EosDesigns.BgpPeerGroups.MlagIpv4UnderlayPeer | EosDesigns.BgpPeerGroups.MlagIpv4VrfsPeer
    ) -> None:
        """Set structured_config for one MLAG peer_group."""
        router_bgp = self.structured_config.router_bgp
        peer_group_name = bgp_peer_group.name
        peer_group = EosCliConfigGen.RouterBgp.PeerGroupsItem(
            name=peer_group_name,
            remote_as=self.shared_utils.formatted_bgp_as,
            next_hop_self=True,
            description=AvdStringFormatter().format(self.inputs.mlag_bgp_peer_group_description, mlag_peer=self.shared_utils.mlag_peer),
            password=self.shared_utils.get_bgp_password(bgp_peer_group),
            bfd=bgp_peer_group.bfd or None,
            maximum_routes=bgp_peer_group.maximum_routes,
            send_community="all",
        )
        peer_group.metadata.type = "ipv4"

        if bgp_peer_group.structured_config:
            self.custom_structured_configs.nested.router_bgp.peer_groups.obtain(peer_group_name)._deepmerge(
                bgp_peer_group.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
            )

        if self.shared_utils.node_config.mlag_ibgp_origin_incomplete:
            peer_group.route_map_in = "RM-MLAG-PEER-IN"
            self.set_once_route_map_mlag_peer_in()

        router_bgp.peer_groups.append(peer_group)
