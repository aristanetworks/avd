# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class StaticRoutesMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def static_routes(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set the structured config for static_routes.

        Consist of
        - static_routes defined under the vrfs
        - static routes added automatically for VARP with prefixes
        """
        self.structured_config_utils.set_once_static_routes_from_network_services()

    def set_zscaler_ie_connection_static_route(self: AvdStructuredConfigNetworkServicesProtocol, destination_ip: str, name: str, next_hop: str) -> None:
        """Set the static route for one Zscaler Internet Exit connection."""
        self.structured_config.static_routes.append_unique(
            EosCliConfigGen.StaticRoutesItem(
                prefix=f"{destination_ip}/32",
                name=name,
                next_hop=next_hop,
            )
        )
