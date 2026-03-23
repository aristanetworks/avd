# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Structured Config Utils Module.

This module provides utility classes for structured config generation.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.parent_interfaces import ParentInterfacesTracker
from pyavd._utils.run_once import RunOnceMethodStateHelper, run_once_method

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns
    from pyavd._eos_designs.shared_utils import SharedUtilsProtocol


class StructuredConfigUtils(RunOnceMethodStateHelper):
    """
    Utility class for structured config generation.

    This class holds shared utilities and trackers used across all structured config modules.
    """

    def __init__(
        self,
        structured_config: EosCliConfigGen,
        inputs: EosDesigns,
        shared_utils: SharedUtilsProtocol,
    ) -> None:
        """Initialize the StructuredConfigUtils with a ParentInterfacesTracker instance and structured config instance."""
        super().__init__()
        self.structured_config = structured_config
        self.inputs = inputs
        self.shared_utils = shared_utils
        """The shared structured config instance to write config into."""
        self.parent_interfaces_tracker = ParentInterfacesTracker()
        """Tracker for parent interfaces that need to be created for subinterfaces."""

    @run_once_method
    def set_once_route_map_mlag_peer_in(self) -> None:
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
    def set_once_route_map_connected_to_bgp_vrfs(self) -> None:
        """
        Set one route-map item.

        Filter MLAG peer subnets for redistribute connected for overlay VRFs.
        """
        route_maps_item = EosCliConfigGen.RouteMapsItem(name="RM-CONN-2-BGP-VRFS")
        route_maps_item.sequence_numbers.append_new(
            sequence=10,
            type="deny",
            match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-MLAG-PEER-VRFS"]),
        )
        route_maps_item.sequence_numbers.append_new(
            sequence=20,
            type="permit",
        )
        self.structured_config.route_maps.append(route_maps_item)


__all__ = ["StructuredConfigUtils"]
