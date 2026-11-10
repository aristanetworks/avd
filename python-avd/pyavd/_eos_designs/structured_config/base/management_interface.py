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
        mgmt_settings = self.inputs.mgmt_interface_settings
        mgmt_ip = self.shared_utils.oob_mgmt_ip
        if mgmt_ip is not None:
            # Explicit IP set in node config takes precedence
            interface_settings.ip_address = mgmt_ip
            if mgmt_ip == "dhcp" and self.inputs.avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp:
                interface_settings.dhcp_client_accept_default_route = True
            else:
                # For static IP, set gateway (metadata field, actual routing done via static_routes)
                interface_settings.gateway = self.shared_utils.oob_mgmt_gateway
        elif mgmt_settings.ipv4.dhcp is True:
            interface_settings._update(ip_address="dhcp", dhcp_client_accept_default_route=mgmt_settings.ipv4.accept_default_route)

    def _set_ipv6_config(self: AvdStructuredConfigBaseProtocol, interface_settings: EosCliConfigGen.ManagementInterfacesItem) -> None:
        mgmt_settings = self.inputs.mgmt_interface_settings
        mgmt_ip = self.shared_utils.node_config.ipv6_mgmt_ip

        if mgmt_ip is not None:
            # Explicit IPv6 set in node config takes precedence
            interface_settings.ipv6_enable = True

            if mgmt_ip == "auto-config":
                interface_settings.ipv6_address_auto_config = True
                if self.inputs.avd_design_future.accept_ra_default_route_for_ipv6_mgmt_ip_auto_config:
                    interface_settings.ipv6_nd.ra.rx_accept._update(default_route=True, route_preference=True)
            else:
                interface_settings.ipv6_gateway = self.shared_utils.ipv6_mgmt_gateway
                interface_settings.ipv6_addresses.append(mgmt_ip)

        elif mgmt_settings.ipv6.slaac is True:
            interface_settings._update(ipv6_enable=True, ipv6_address_auto_config=True)
            if self.inputs.mgmt_interface_settings.ipv6.accept_default_route:
                interface_settings.ipv6_nd.ra.rx_accept._update(default_route=True, route_preference=True)

    @property
    def _is_management_interfaces_configuration_required(self: AvdStructuredConfigBaseProtocol) -> bool:
        """Identifies whether the management interface needs to be configured."""
        mgmt_settings = self.inputs.mgmt_interface_settings

        return (
            # Infer this implicitly from node configuration
            bool(self.shared_utils.node_config.mgmt_ip)
            or bool(self.shared_utils.node_config.ipv6_mgmt_ip)
            # ... or explicitly from mgmt_interface_settings
            or mgmt_settings.ipv4.dhcp is True
            or mgmt_settings.ipv6.slaac is True
        )

    @structured_config_contributor
    def management_interfaces(self: AvdStructuredConfigBaseProtocol) -> None:
        """management_interfaces set based on mgmt_interface, mgmt_ip, ipv6_mgmt_ip facts, mgmt_gateway, ipv6_mgmt_gateway and mgmt_interface_vrf variables."""
        mgmt_settings = self.inputs.mgmt_interface_settings

        if self._is_management_interfaces_configuration_required:
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
