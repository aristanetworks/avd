# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigNetworkServicesProtocol


class IpSecurityMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def _set_zscaler_internet_exit_policy_ip_security(
        self: AvdStructuredConfigNetworkServicesProtocol, internet_exit_policy: EosDesigns.CvPathfinderInternetExitPoliciesItem
    ) -> None:
        """Set ip_security in structued_config for the given internet_exit_policy."""
        policy_name = internet_exit_policy.name
        encrypt_traffic = internet_exit_policy.zscaler.encrypt_traffic
        ike_policy_name = f"IE-{policy_name}-IKE-POLICY"
        sa_policy_name = f"IE-{policy_name}-SA-POLICY"
        profile_name = f"IE-{policy_name}-PROFILE"
        ufqdn, ipsec_key = self._get_ipsec_credentials(internet_exit_policy)

        self.structured_config.ip_security.ike_policies.append_new(
            name=ike_policy_name,
            local_id_fqdn=ufqdn,
            ike_lifetime=24,
            encryption="aes256",
            dh_group=24,
        )
        self.structured_config.ip_security.sa_policies.append_new(
            name=sa_policy_name,
            pfs_dh_group=24,
            sa_lifetime=EosCliConfigGen.IpSecurity.SaPoliciesItem.SaLifetime(value=8),
            esp=EosCliConfigGen.IpSecurity.SaPoliciesItem.Esp(integrity="sha256", encryption="aes256" if encrypt_traffic else "disabled"),
        )
        self.structured_config.ip_security.profiles.append_new(
            name=profile_name,
            ike_policy=ike_policy_name,
            sa_policy=sa_policy_name,
            shared_key=ipsec_key,
            dpd=EosCliConfigGen.IpSecurity.ProfilesItem.Dpd(
                interval=10,
                time=60,
                action="clear",
            ),
            connection="start",
        )
