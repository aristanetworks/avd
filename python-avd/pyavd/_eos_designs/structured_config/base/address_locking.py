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

        local_interface = self.shared_utils.get_local_interface(address_locking_settings.local_interface)
        self.structured_config.address_locking._update(
            dhcp_servers_ipv4=address_locking_settings.dhcp_servers_ipv4._cast_as(EosCliConfigGen.AddressLocking.DhcpServersIpv4),
            local_interface=local_interface,
            locked_address=address_locking_settings.locked_address._cast_as(EosCliConfigGen.AddressLocking.LockedAddress),
            disabled=address_locking_settings.disabled,
            leases=address_locking_settings.leases._cast_as(EosCliConfigGen.AddressLocking.Leases),
        )
