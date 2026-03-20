# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
    from pyavd._eos_designs.schema import EosDesigns


def append_gateway_routes(
    routes_list: EosCliConfigGen.StaticRoutes | EosCliConfigGen.Ipv6StaticRoutes,
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
            routes_list.append_new(vrf=vrf, prefix=prefix, next_hop=gateway)
    else:
        routes_list.append_new(vrf=vrf, prefix=default_prefix, next_hop=gateway)
