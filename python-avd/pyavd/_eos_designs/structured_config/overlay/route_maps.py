# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._utils.run_once import run_once_method

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlayProtocol


class RouteMapsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def set_route_map_evpn_filter_as(self: AvdStructuredConfigOverlayProtocol, asn: str) -> None:
        """Set route-map RM-EVPN-FILTER-AS{{ asn }}."""
        route_maps_item = EosCliConfigGen.RouteMapsItem(name=f"RM-EVPN-FILTER-AS{asn}")
        if self.inputs.evpn_prevent_readvertise_to_server_mode == "source_peer_asn":
            route_maps_item.sequence_numbers.append_new(sequence=10, type="deny", match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match([f"as {asn}"]))
        else:
            route_maps_item.sequence_numbers.append_new(
                sequence=10, type="deny", match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match([f"as-path AS{asn}"])
            )
            # Create the as-path access-list
            self.set_as_path_acl_as(asn)

        route_maps_item.sequence_numbers.append_new(sequence=20, type="permit")
        self.structured_config.route_maps.append(route_maps_item)

    @run_once_method
    def set_once_route_map_evpn_soo_in(self: AvdStructuredConfigOverlayProtocol) -> None:
        """Set route-maps RM-EVPN-SOO-IN."""
        route_maps_item = EosCliConfigGen.RouteMapsItem(name="RM-EVPN-SOO-IN")
        route_maps_item.sequence_numbers.append_new(
            sequence=10, type="deny", match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["extcommunity ECL-EVPN-SOO"])
        )
        # Create the extcommunity-list
        self.shared_utils.set_once_ip_extcommunity_list_evpn_soo(self.structured_config)

        route_maps_item.sequence_numbers.append_new(sequence=20, type="permit")
        self.structured_config.route_maps.append(route_maps_item)

    @run_once_method
    def set_once_route_map_evpn_soo_out(self: AvdStructuredConfigOverlayProtocol) -> None:
        """Set route-maps RM-EVPN-SOO-OUT."""
        route_maps_item = EosCliConfigGen.RouteMapsItem(name="RM-EVPN-SOO-OUT")
        route_maps_item.sequence_numbers.append_new(
            sequence=10,
            type="permit",
            set=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set([f"extcommunity soo {self.shared_utils.evpn_soo} additive"]),
        )
        self.structured_config.route_maps.append(route_maps_item)

    @run_once_method
    def set_once_route_map_wan_ha_peer_in(self: AvdStructuredConfigOverlayProtocol) -> None:
        """Set route-maps RM-WAN-HA-PEER-IN."""
        route_maps_item = EosCliConfigGen.RouteMapsItem(name="RM-WAN-HA-PEER-IN")
        route_maps_item.sequence_numbers.append_new(
            sequence=10,
            type="permit",
            description="Set tag 50 on routes received from HA peer over EVPN",
            set=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set(["tag 50"]),
        )
        self.structured_config.route_maps.append(route_maps_item)

    @run_once_method
    def set_once_route_map_wan_ha_peer_out(self: AvdStructuredConfigOverlayProtocol) -> None:
        """Set route-maps RM-WAN-HA-PEER-OUT."""
        route_maps_item = EosCliConfigGen.RouteMapsItem(name="RM-WAN-HA-PEER-OUT")
        route_maps_item.sequence_numbers.append_new(
            sequence=10,
            type="permit",
            match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["route-type internal"]),
            set=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set(["local-preference 50"]),
            description="Make EVPN routes learned from WAN less preferred on HA peer",
        )
        route_maps_item.sequence_numbers.append_new(
            sequence=20,
            type="permit",
            description="Make locally injected routes less preferred on HA peer",
            set=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set(["local-preference 75"]),
        )
        self.structured_config.route_maps.append(route_maps_item)
