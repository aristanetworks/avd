# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Final, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class IpNatMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    INTERNET_EXIT_ZSCALER_NAT_PROFILE_NAME: Final[str] = "NAT-IE-ZSCALER"
    INTERNET_EXIT_DIRECT_NAT_PROFILE_NAME: Final[str] = "NAT-IE-DIRECT"

    def get_internet_exit_nat_acl_name(self: AvdStructuredConfigNetworkServicesProtocol, nat_profile_name: str) -> str:
        return f"ACL-{nat_profile_name}"

    def _set_direct_ie_policy_ip_nat(self: AvdStructuredConfigNetworkServicesProtocol, ip_interfaces: set[str]) -> None:
        """Set the structured config for ip_nat."""
        profile = EosCliConfigGen.IpNat.ProfilesItem(name=self.INTERNET_EXIT_DIRECT_NAT_PROFILE_NAME)
        acl_name = self.get_internet_exit_nat_acl_name(self.INTERNET_EXIT_DIRECT_NAT_PROFILE_NAME)
        profile.source.dynamic.append_new(access_list=acl_name, nat_type="overload")
        self.structured_config.ip_nat.profiles.append(profile)

        # set the ACL
        self._set_direct_ie_policy_acl(ip_interfaces, acl_name)

    def _set_zscaler_ie_policy_ip_nat(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """Set the structured config for ip_nat."""
        pool = EosCliConfigGen.IpNat.PoolsItem(name="PORT-ONLY-POOL", type="port-only")
        pool.ranges.append_new(first_port=1500, last_port=65535)
        self.structured_config.ip_nat.pools.append(pool)
        profile = EosCliConfigGen.IpNat.ProfilesItem(name=self.INTERNET_EXIT_ZSCALER_NAT_PROFILE_NAME)

        acl_name = self.get_internet_exit_nat_acl_name(self.INTERNET_EXIT_ZSCALER_NAT_PROFILE_NAME)

        profile.source.dynamic.append_new(access_list=acl_name, pool_name="PORT-ONLY-POOL", nat_type="pool")
        self.structured_config.ip_nat.profiles.append(profile)

        # set the ACL
        self._set_zscaler_ie_policy_acl(acl_name)
