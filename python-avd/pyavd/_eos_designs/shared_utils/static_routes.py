# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen


def append_gateway_routes(
    routes_list: EosCliConfigGen.StaticRoutes | EosCliConfigGen.Ipv6StaticRoutes,
    gateway: str | None,
    vrf: str | None,
    destination_networks: Sequence[str] | None = None,
    default_prefix: str = "",
) -> None:
    """
    Append static routes for a gateway. No-op if gateway is None.

    If destination_networks is provided, one route is created per destination.
    Otherwise a single route is created using default_prefix.

    This is the centralized helper for all gateway-based static route patterns
    (management, inband management, etc.) across all structured config generators.

    Args:
        routes_list: The structured config route list to append to
                     (e.g. structured_config.static_routes or structured_config.ipv6_static_routes).
        gateway: Next-hop gateway IP. If None, this function is a no-op.
        vrf: VRF name for the route.
        destination_networks: Optional list of prefixes. If given, one route per prefix is added.
        default_prefix: Fallback prefix used when destination_networks is empty or None.
    """
    if gateway is None:
        return

    if destination_networks:
        for prefix in destination_networks:
            routes_list.append_new(vrf=vrf, prefix=prefix, next_hop=gateway)
    else:
        routes_list.append_new(vrf=vrf, prefix=default_prefix, next_hop=gateway)
