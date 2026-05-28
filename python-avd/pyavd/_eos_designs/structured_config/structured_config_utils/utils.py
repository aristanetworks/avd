# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._utils import Undefined, UndefinedType
from pyavd._utils.run_once import run_once_method

if TYPE_CHECKING:
    from . import StructuredConfigUtilsProtocol


class UtilsMixin(Protocol):
    def get_interface_validate_state(self: StructuredConfigUtilsProtocol, user_input: bool | None = None, peer_in_fabric: bool = False) -> bool | UndefinedType:
        """
        Checks if validate_state flag should be set or not.

        Args:
            user_input: Boolean value of the `validate_state` from the inputs of the interface. `None` if not set in inputs.
            peer_in_fabric: Flag indicating if the interface peer is a known AVD fabric device.

        Returns:
            True: If `validate_state` should be enabled (set to True) for the interface.
            False: If `validate_state` should be disabled (set to False) for the interface.
            UndefinedType: If `validate_state` should not be set/changed for the interface.
        """
        if self.shared_utils.digital_twin:
            # Peer is not deployed in Digital Twin - interface will be down, so disable state validation.
            if not peer_in_fabric:
                return False
            # Peer is in the fabric - only respect an explicit False from user input; never force True in Digital Twin.
            return False if user_input is False else Undefined
        # Non-Digital-Twin: follow the user input if set, otherwise leave unset.
        return Undefined if user_input is None else user_input

    @run_once_method
    def set_once_ip_extcommunity_list_evpn_soo(self: StructuredConfigUtilsProtocol) -> None:
        """Set ip extcommunity-list ECL-EVPN-SOO."""
        ip_extcommunity_list = EosCliConfigGen.IpExtcommunityListsItem(name="ECL-EVPN-SOO")
        ip_extcommunity_list.entries.append_new(type="permit", extcommunities=f"soo {self.shared_utils.evpn_soo}")
        self.structured_config.ip_extcommunity_lists.append(ip_extcommunity_list)
