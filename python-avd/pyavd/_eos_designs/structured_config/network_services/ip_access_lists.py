# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdError
from pyavd._utils import get_ip_from_ip_prefix

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigNetworkServicesProtocol


class IpAccesslistsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def _set_ipv4_acl(self: AvdStructuredConfigNetworkServicesProtocol, ipv4_acl: EosDesigns.Ipv4AclsItem) -> None:
        """
        Set structured config for ip_access_lists.

        Called for each interface in l3_interfaces and l3_port_channels when applying ipv4_acls
        """
        self.structured_config.ip_access_lists.append(ipv4_acl._cast_as(EosCliConfigGen.IpAccessListsItem))

    def _set_direct_ie_policy_acl(self: AvdStructuredConfigNetworkServicesProtocol, interface_ips: set[str], acl_name: str) -> None:
        """
        Configure an IP access list for the Direct Internet policy.

        Args:
            interface_ips: a set of IP address to configure on the ACL.
            acl_name: the name of the ACL to configure.
        """
        if acl_name in self.inputs.ipv4_acls:
            # pass substitution fields as anything to check if acl requires substitution or not
            acl = self.shared_utils.get_ipv4_acl(acl_name, "random", interface_ip="random", peer_ip="random")
            if acl.name == acl_name:
                # ACL doesn't need replacement
                self.structured_config.ip_access_lists.append(acl._cast_as(EosCliConfigGen.IpAccessListsItem))
                return

            # TODO: We still have one nat for all interfaces, need to also add logic to make nat per interface
            # if acl needs substitution
            msg = f"ipv4_acls[name={acl_name}] field substitution is not supported for internet exit access lists"
            raise AristaAvdError(msg)

        # Use default using interface_ips
        if interface_ips:
            # TODO: We probably should raise if there is no interface_ips
            acl = EosCliConfigGen.IpAccessListsItem(name=acl_name)
            i = 1
            for i, interface_ip in enumerate(sorted(interface_ips), start=1):
                acl.entries.append_new(sequence=i * 10, action="deny", protocol="ip", source=get_ip_from_ip_prefix(interface_ip), destination="any")

            # Last permit IP any any entry
            acl.entries.append_new(
                sequence=10 + i * 10,
                action="permit",
                protocol="ip",
                source="any",
                destination="any",
            )

            self.structured_config.ip_access_lists.append(acl)

    def _set_zscaler_ie_policy_acl(self: AvdStructuredConfigNetworkServicesProtocol, acl_name: str) -> None:
        """
        Configure an IP access list for the Zscaler Internet policy.

        Args:
            acl_name: the name of the ACL to configure.
        """
        if acl_name in self.inputs.ipv4_acls:
            # pass substitution fields as anything to check if acl requires substitution or not
            acl = self.shared_utils.get_ipv4_acl(acl_name, "random", interface_ip="random", peer_ip="random")
            if acl.name == acl_name:
                # ACL doesn't need replacement
                self.structured_config.ip_access_lists.append(acl._cast_as(EosCliConfigGen.IpAccessListsItem))
                return

            # TODO: We still have one nat for all interfaces, need to also add logic to make nat per interface
            # if acl needs substitution
            msg = f"ipv4_acls[name={acl_name}] field substitution is not supported for internet exit access lists"
            raise AristaAvdError(msg)

        ip_access_list = EosCliConfigGen.IpAccessListsItem(name=acl_name)
        ip_access_list.entries.append_new(sequence=10, action="permit", protocol="ip", source="any", destination="any")
        self.structured_config.ip_access_lists.append(ip_access_list)
