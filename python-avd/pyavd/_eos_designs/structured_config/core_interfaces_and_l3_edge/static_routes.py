# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigCoreInterfacesAndL3EdgeProtocol


class StaticRoutesMixin(Protocol):
    """Mixin Class used to generate structured config for static_routes."""

    @structured_config_contributor
    def static_routes(self: AvdStructuredConfigCoreInterfacesAndL3EdgeProtocol) -> None:
        """Set the structured config for static_routes for tunnel p2p_links."""
        for _p2p_link, p2p_link_data in self._filtered_p2p_links:
            if not p2p_link_data.get("is_tunnel"):
                continue

            peer_source_ip = p2p_link_data.get("peer_source_ip")
            crypto_peer_ip = p2p_link_data.get("crypto_peer_ip")

            if not peer_source_ip or not crypto_peer_ip:
                continue

            self.structured_config.static_routes.append_unique(
                EosCliConfigGen.StaticRoutesItem(
                    prefix=f"{peer_source_ip}/32",
                    next_hop=crypto_peer_ip,
                    name=f"Tunnel endpoint {p2p_link_data['peer']}",
                ),
            )
