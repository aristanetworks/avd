# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class RouterServiceInsertionMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def set_zscaler_ie_router_service_insertion(self: AvdStructuredConfigNetworkServicesProtocol, monitor_name: str, tunnel_id: int) -> None:
        """
        Set the structured config for router_service_insertion for one Zscaler Internet Exit connection.

        Only used for CV Pathfinder edge routers today
        """
        service_connection = EosCliConfigGen.RouterServiceInsertion.ConnectionsItem(name=monitor_name, monitor_connectivity_host=monitor_name)
        service_connection.tunnel_interface.primary = f"Tunnel{tunnel_id}"
        self.structured_config.router_service_insertion.connections.append(service_connection)

    def set_direct_ie_router_service_insertion(
        self: AvdStructuredConfigNetworkServicesProtocol, monitor_name: str, source_interface: str, next_hop: str
    ) -> None:
        """
        Set the structured config for router_service_insertion for one Direct Internet Exit connection.

        Only used for CV Pathfinder edge routers today
        """
        service_connection = EosCliConfigGen.RouterServiceInsertion.ConnectionsItem(name=monitor_name, monitor_connectivity_host=monitor_name)
        service_connection.ethernet_interface._update(name=source_interface, next_hop=next_hop)
        self.structured_config.router_service_insertion.connections.append(service_connection)
