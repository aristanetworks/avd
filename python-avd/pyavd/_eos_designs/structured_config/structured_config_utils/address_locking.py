# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils.run_once import run_once_method
from pyavd._utils.undefined import Undefined

if TYPE_CHECKING:
    from . import StructuredConfigUtilsProtocol


class AddressLockingMixin(Protocol):
    @run_once_method
    def set_once_address_locking(self: StructuredConfigUtilsProtocol) -> None:
        """Set global address locking structured config from address_locking_settings."""
        feature_support = self.shared_utils.platform_settings.feature_support
        if not (address_locking_settings := self.inputs.address_locking_settings) or not feature_support.address_locking.supported:
            return

        if not self.inputs.avd_design_future.fix_address_locking_dhcp_server_interfaces:
            local_interface = self.shared_utils.get_local_interface(address_locking_settings.local_interface)
            dhcp_server_interfaces = Undefined
        elif address_locking_settings.local_interface and address_locking_settings.dhcp_server_interfaces:
            msg = "'address_locking_settings.local_interface' and 'address_locking_settings.dhcp_server_interfaces' are mutually exclusive."
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)
        else:
            dhcp_server_interfaces = address_locking_settings.dhcp_server_interfaces
            local_interface = None if dhcp_server_interfaces else self.shared_utils.get_local_interface(address_locking_settings.local_interface)
            dhcp_server_interfaces = dhcp_server_interfaces._cast_as(EosCliConfigGen.AddressLocking.DhcpServerInterfaces)

        locked_address = address_locking_settings.locked_address._cast_as(EosCliConfigGen.AddressLocking.LockedAddress)
        if not feature_support.address_locking.ipv4_enforcement_disabled:
            del locked_address.ipv4_enforcement_disabled
        if not feature_support.address_locking.ipv6_enforcement_disabled:
            del locked_address.ipv6_enforcement_disabled

        self.structured_config.address_locking._update(
            dhcp_server_interfaces=dhcp_server_interfaces,
            dhcp_servers_ipv4=address_locking_settings.dhcp_servers_ipv4._cast_as(EosCliConfigGen.AddressLocking.DhcpServersIpv4),
            local_interface=local_interface,
            locked_address=locked_address,
            disabled=address_locking_settings.disabled,
            leases=address_locking_settings.leases._cast_as(EosCliConfigGen.AddressLocking.Leases),
        )

    def ensure_address_locking(self: StructuredConfigUtilsProtocol, address_family: Literal["ipv4", "ipv6"], context: str) -> None:
        """Validate global address locking settings and configure them once."""
        address_locking_settings = self.inputs.address_locking_settings

        # A client cannot activate Address Locking without global settings because 'enforcement disabled' is only exposed in global settings.
        if not address_locking_settings:
            msg = (
                f"Address locking is enabled under '{context}' but 'address_locking_settings' is not configured. "
                "Configure the required global address locking settings before enabling address locking on an interface or VLAN."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

        feature_support = self.shared_utils.platform_settings.feature_support.address_locking
        if address_family == "ipv6":
            # EOS supports IPv6 Address Locking only with enforcement disabled.
            if not address_locking_settings.locked_address.ipv6_enforcement_disabled:
                msg = (
                    f"IPv6 address locking is enabled under '{context}' but "
                    "`address_locking_settings.locked_address.ipv6_enforcement_disabled: true` is required."
                )
                raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

            if not feature_support.ipv6_enforcement_disabled:
                msg = (
                    f"IPv6 address locking is enabled under '{context}' but the platform does not support "
                    "`locked-address ipv6 enforcement disabled`, which is required for IPv6 Address Locking."
                )
                raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

            self.set_once_address_locking()
            return

        # IPv4 Address Locking can operate without lease learning when enforcement is disabled.
        if address_locking_settings.locked_address.ipv4_enforcement_disabled and feature_support.ipv4_enforcement_disabled:
            self.set_once_address_locking()
            return

        # Server-interface mode learns leases from DHCP server interfaces.
        if self.inputs.avd_design_future.fix_address_locking_dhcp_server_interfaces and address_locking_settings.dhcp_server_interfaces:
            self.set_once_address_locking()
            return

        # LeaseQuery mode needs DHCP servers and a source interface to reach them.
        if address_locking_settings.dhcp_servers_ipv4 and self.shared_utils.get_local_interface(address_locking_settings.local_interface):
            self.set_once_address_locking()
            return

        if address_locking_settings.locked_address.ipv4_enforcement_disabled and not feature_support.ipv4_enforcement_disabled:
            msg = (
                f"IPv4 address locking is enabled under '{context}' with `ipv4_enforcement_disabled: true`, but the platform does not support "
                "`locked-address ipv4 enforcement disabled`. Configure LeaseQuery or server-interface mode instead."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

        # None of the EOS-supported IPv4 operating modes are configured.
        msg = (
            f"IPv4 address locking is enabled under '{context}' but one of the following is required: "
            "`address_locking_settings.locked_address.ipv4_enforcement_disabled: true`, "
            "`address_locking_settings.dhcp_servers_ipv4` with a local interface, or "
            "server-interface mode with `address_locking_settings.dhcp_server_interfaces` and "
            "`avd_design_future.fix_address_locking_dhcp_server_interfaces: true`."
        )
        raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)
