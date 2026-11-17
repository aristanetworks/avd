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

    def _set_ipv4_config(self: AvdStructuredConfigBaseProtocol, interface_settings: EosCliConfigGen.ManagementInterfacesItem) -> None:
        mgmt_ip = self.shared_utils.oob_mgmt_ip
        if not mgmt_ip:
            return

        interface_settings.ip_address = mgmt_ip
        if mgmt_ip == "dhcp":
            if (accept_default_route := self.shared_utils.mgmt_ip_dhcp_accept_default_route) is not None:
                interface_settings.dhcp_client_accept_default_route = accept_default_route
            return

        # For static IP, set gateway (metadata field, actual routing done via static_routes)
        interface_settings.gateway = self.shared_utils.oob_mgmt_gateway

    def _set_ipv6_config(self: AvdStructuredConfigBaseProtocol, interface_settings: EosCliConfigGen.ManagementInterfacesItem) -> None:
        mgmt_ip = self.shared_utils.ipv6_mgmt_ip

        if not mgmt_ip:
            return

        interface_settings.ipv6_enable = True
        if mgmt_ip == "auto-config":
            interface_settings.ipv6_address_auto_config = True
            if self.shared_utils.ipv6_mgmt_ip_auto_config_accept_default_route is True:
                interface_settings.ipv6_nd.ra.rx_accept._update(default_route=True, route_preference=True)
        else:
            interface_settings.ipv6_gateway = self.shared_utils.ipv6_mgmt_gateway
            interface_settings.ipv6_addresses.append(mgmt_ip)

    @structured_config_contributor
    def management_interfaces(self: AvdStructuredConfigBaseProtocol) -> None:
        """management_interfaces set based on mgmt_interface, mgmt_ip, ipv6_mgmt_ip facts, mgmt_gateway, ipv6_mgmt_gateway and mgmt_interface_vrf variables."""
        mgmt_settings = self.inputs.mgmt_interface_settings

        if self.shared_utils.mgmt_ip or self.shared_utils.ipv6_mgmt_ip:
            self.structured_config_utils.set_once_oob_mgmt_vrf()

            interface_settings = EosCliConfigGen.ManagementInterfacesItem(
                name=self.shared_utils.mgmt_interface,
                description=self.shared_utils.mgmt_interface_description,
                shutdown=mgmt_settings.shutdown == "true",
                vrf=self.shared_utils.mgmt_interface_vrf,
                type="oob",
            )

            self._set_ipv4_config(interface_settings)
            self._set_ipv6_config(interface_settings)

            if mgmt_settings.lldp:
                interface_settings.lldp = mgmt_settings.lldp._cast_as(EosCliConfigGen.ManagementInterfacesItem.Lldp)
            self.structured_config.management_interfaces.append(interface_settings)

        elif mgmt_settings.shutdown in ("true", "auto"):
            # Shutdown the unused management interface.
            interface_settings = EosCliConfigGen.ManagementInterfacesItem(
                name=self.shared_utils.mgmt_interface,
                shutdown=True,
            )
            self.structured_config.management_interfaces.append(interface_settings)
