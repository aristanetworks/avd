# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigBaseProtocol


class ManagementInterfaceMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def management_interfaces(self: AvdStructuredConfigBaseProtocol) -> None:
        """management_interfaces set based on mgmt_interface, mgmt_ip, ipv6_mgmt_ip facts, mgmt_gateway, ipv6_mgmt_gateway and mgmt_interface_vrf variables."""
        if self.shared_utils.node_config.mgmt_ip or self.shared_utils.node_config.ipv6_mgmt_ip:
            # Check if mgmt_ip is set to "dhcp"
            is_dhcp = self.shared_utils.node_config.mgmt_ip == "dhcp"

            interface_settings = EosCliConfigGen.ManagementInterfacesItem(
                name=self.shared_utils.mgmt_interface,
                description=self.shared_utils.mgmt_interface_description,
                shutdown=False,
                vrf=self.shared_utils.mgmt_interface_vrf,
                ip_address=self.shared_utils.node_config.mgmt_ip,
                type="oob",
            )

            # For DHCP, automatically accept default route instead of using gateway
            if is_dhcp and self.inputs.avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp:
                interface_settings.dhcp_client_accept_default_route = True
            else:
                # For static IP, set gateway (metadata field, actual routing done via static_routes)
                interface_settings.gateway = self.shared_utils.mgmt_gateway

            """
            inserting ipv6 variables if ipv6_mgmt_ip is set
            """
            if self.shared_utils.node_config.ipv6_mgmt_ip:
                interface_settings._update(
                    ipv6_enable=True,
                    ipv6_gateway=self.shared_utils.ipv6_mgmt_gateway,
                )
                interface_settings.ipv6_addresses.append(self.shared_utils.node_config.ipv6_mgmt_ip)

            if self.inputs.mgmt_interface_settings.lldp:
                interface_settings.lldp = self.inputs.mgmt_interface_settings.lldp._cast_as(EosCliConfigGen.ManagementInterfacesItem.Lldp)
            self.structured_config.management_interfaces.append(interface_settings)
