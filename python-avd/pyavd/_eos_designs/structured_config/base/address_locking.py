# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigBaseProtocol


class AddressLockingMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def address_locking(self: AvdStructuredConfigBaseProtocol) -> None:
        if not (address_locking_settings := self.inputs.address_locking_settings):
            return

        local_interface = self._get_local_interface(address_locking_settings.local_interface)
        self.structured_config.address_locking._update(
            dhcp_servers_ipv4=address_locking_settings.dhcp_servers_ipv4._cast_as(EosCliConfigGen.AddressLocking.DhcpServersIpv4),
            local_interface=local_interface,
            locked_address=address_locking_settings.locked_address._cast_as(EosCliConfigGen.AddressLocking.LockedAddress),
            disabled=address_locking_settings.disabled,
            leases=address_locking_settings.leases._cast_as(EosCliConfigGen.AddressLocking.Leases),
        )

    def _get_local_interface(self: AvdStructuredConfigBaseProtocol, input_interface: str | None) -> str | None:
        """
        Resolve and return the appropriate local interface.

        Given an `input_interface`, this function determines the corresponding local interface.
        If the input is None, empty, or one of the predefined keywords, it returns the relevant
        management or inband interface from `self.shared_utils`.
        Otherwise, the provided interface name is returned as-is.
        """
        match input_interface:
            case None | "" | "use_default_mgmt_method_interface":
                return self.shared_utils.default_mgmt_protocol_interface
            case "use_mgmt_interface":
                return self.shared_utils.mgmt_interface
            case "use_inband_mgmt_interface":
                return self.shared_utils.inband_mgmt_interface
        return input_interface
