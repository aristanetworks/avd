# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Structured Config Utils Module.

This module provides utility classes for structured config generation.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from pyavd._eos_designs.structured_config.parent_interfaces import ParentInterfacesTracker

if TYPE_CHECKING:
    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
    from pyavd._eos_designs.schema import EosDesigns


class StructuredConfigUtils:
    """
    Utility class for structured config generation.

    This class holds shared utilities and trackers used across all structured config modules.
    """

    def __init__(self, structured_config: EosCliConfigGen) -> None:
        """Initialize the StructuredConfigUtils with a ParentInterfacesTracker instance."""
        self.structured_config = structured_config
        self.parent_interfaces_tracker = ParentInterfacesTracker()
        """Tracker for parent interfaces that need to be created for subinterfaces."""

    def set_static_routes(
        self,
        static_route_type: Literal["ipv4", "ipv6"],
        gateway: str | None,
        vrf: str | None,
        destination_networks: EosDesigns.MgmtDestinationNetworks | EosDesigns.Ipv6MgmtDestinationNetworks | None = None,
        default_prefix: str = "",
    ) -> None:
        """Append static routes for a gateway."""
        if gateway is None:
            return

        if destination_networks:
            for prefix in destination_networks:
                if static_route_type == "ipv4":
                    self.structured_config.static_routes.append_new(vrf=vrf, prefix=prefix, next_hop=gateway)
                else:
                    self.structured_config.ipv6_static_routes.append_new(vrf=vrf, prefix=prefix, next_hop=gateway)
        elif static_route_type == "ipv4":
            self.structured_config.static_routes.append_new(vrf=vrf, prefix=default_prefix, next_hop=gateway)
        else:
            self.structured_config.ipv6_static_routes.append_new(vrf=vrf, prefix=default_prefix, next_hop=gateway)


__all__ = ["StructuredConfigUtils"]
