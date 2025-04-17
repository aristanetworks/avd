# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class MonitorConnectivityMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def set_direct_ie_monitor_connectivity(
        self: AvdStructuredConfigNetworkServicesProtocol, interface_name: str, monitor_name: str, description: str, monitor_host: str
    ) -> None:
        """
        Set the structured config for one direct Internet Exit connection.

        Only used for CV Pathfinder edge routers today
        """
        interface_set_name = f"SET-{self.shared_utils.sanitize_interface_name(interface_name)}"
        self.structured_config.monitor_connectivity.interface_sets.obtain(interface_set_name).interfaces = interface_name

        self.structured_config.monitor_connectivity.hosts.append_new(
            name=monitor_name,
            description=description,
            ip=monitor_host,
            local_interfaces=interface_set_name,
            address_only=False,
        )

    def set_zscaler_ie_monitor_connectivity(
        self: AvdStructuredConfigNetworkServicesProtocol, tunnel_id: int, monitor_name: str, description: str, monitor_host: str
    ) -> None:
        """
        Set the structured config for one Zscaler Internet Exit connection.

        Only used for CV Pathfinder edge routers today
        """
        cloud_name = self._zscaler_endpoints.cloud_name

        interface_name = f"Tunnel{tunnel_id}"
        interface_set_name = f"SET-{self.shared_utils.sanitize_interface_name(interface_name)}"
        self.structured_config.monitor_connectivity.interface_sets.obtain(interface_set_name).interfaces = interface_name

        self.structured_config.monitor_connectivity.hosts.append_new(
            name=monitor_name,
            description=description,
            ip=monitor_host,
            local_interfaces=interface_set_name,
            address_only=False,
            # TODO: Do not hardcode this
            # Accepting SonarLint issue: The URL is just for verifying connectivity. No data is passed.
            url=f"http://gateway.{cloud_name}.net/vpntest",  # NOSONAR
        )
