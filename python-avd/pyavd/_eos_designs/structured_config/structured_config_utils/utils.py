# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._errors import AristaAvdInvalidInputsError, AristaAvdMissingVariableError
from pyavd._utils.run_once import run_once_method
from pyavd._utils.undefined import Undefined, UndefinedType

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

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

    def _set_ipv4_acl(self: StructuredConfigUtilsProtocol, ipv4_acl: EosDesigns.Ipv4AclsItem) -> None:
        """Append an IPv4 ACL to structured config ip_access_lists."""
        self.structured_config.ip_access_lists.append(ipv4_acl._cast_as(EosCliConfigGen.IpAccessListsItem))

    def _set_ipv6_acl(self: StructuredConfigUtilsProtocol, ipv6_acl: EosDesigns.Ipv6AclsItem) -> None:
        """Append an IPv6 ACL to structured config ipv6_access_lists."""
        self.structured_config.ipv6_access_lists.append(ipv6_acl._cast_as(EosCliConfigGen.Ipv6AccessListsItem))

    @run_once_method
    def set_once_ip_extcommunity_list_evpn_soo(self: StructuredConfigUtilsProtocol) -> None:
        """Set ip extcommunity-list ECL-EVPN-SOO."""
        ip_extcommunity_list = EosCliConfigGen.IpExtcommunityListsItem(name="ECL-EVPN-SOO")
        ip_extcommunity_list.entries.append_new(type="permit", extcommunities=f"soo {self.shared_utils.evpn_soo}")
        self.structured_config.ip_extcommunity_lists.append(ip_extcommunity_list)

    def _validate_ipv4_acl_exclusion(
        self: StructuredConfigUtilsProtocol,
        ipv4_acl: str | None,
        ipv4_standard_acl: str | None,
        name: str,
        direction: str,
    ) -> None:
        """Raise AristaAvdInvalidInputsError if both an extended and a standard IPv4 ACL are set for the same direction."""
        if not (ipv4_acl and ipv4_standard_acl):
            return
        direction_label = "ingress" if direction == "in" else "egress"
        msg = (
            f"'ipv4_acl_{direction}' and 'ipv4_standard_acl_{direction}' are mutually exclusive on interface '{name}'. "
            f"Only one {direction_label} IPv4 ACL can be configured."
        )
        raise AristaAvdInvalidInputsError(msg)

    @run_once_method
    def set_once_oob_mgmt_vrf(self: StructuredConfigUtilsProtocol) -> None:
        """Set OOB management VRF once when required."""
        vrf_settings = EosCliConfigGen.VrfsItem(name=self.shared_utils.mgmt_interface_vrf, ip_routing=self.shared_utils.mgmt_vrf_routing)

        if self.shared_utils.node_config.ipv6_mgmt_ip is not None:
            vrf_settings.ipv6_routing = self.shared_utils.mgmt_vrf_routing
        self.structured_config.vrfs.append(vrf_settings)

    def _set_ipv4_standard_acl(self: StructuredConfigUtilsProtocol, acl_name: str) -> None:
        if acl_name not in self.inputs.ipv4_standard_acls:
            msg = f"ipv4_standard_acls[name={acl_name}]"
            raise AristaAvdMissingVariableError(msg, host=self.shared_utils.hostname)
        self.structured_config.standard_access_lists.append(self.inputs.ipv4_standard_acls[acl_name]._cast_as(EosCliConfigGen.StandardAccessListsItem))
