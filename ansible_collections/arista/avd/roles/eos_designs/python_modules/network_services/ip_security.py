# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.password_utils.password import simple_7_encrypt
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_null_from_data
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class IpSecurityMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def ip_security(self) -> dict | None:
        """
        ip_security set based on cv_pathfinder_internet_exit_policies
        """

        if not self.shared_utils.is_cv_pathfinder_client:
            return None

        ip_security = {"ike_policies": [], "sa_policies": [], "profiles": []}
        for internet_exit_policy in self._filtered_internet_exit_policies:
            # Currently we only need ipsec for zscaler.
            if internet_exit_policy["type"] != "zscaler":
                continue

            policy_name = internet_exit_policy["name"]
            domain_name = get(internet_exit_policy, "zscaler.domain_name", required=True)
            ipsec_key_salt = get(internet_exit_policy, "zscaler.ipsec_key_salt", required=True)
            ike_policy_name = f"IE-{policy_name}-IKE-POLICY"
            sa_policy_name = f"IE-{policy_name}-SA-POLICY"
            profile_name = f"IE-{policy_name}-PROFILE"
            ipsec_key = self._generate_ipsec_key(name=policy_name, salt=ipsec_key_salt)
            ufqdn = f"{self.shared_utils.hostname}_{policy_name}@{domain_name}"

            ip_security["ike_policies"].append(
                {
                    "name": ike_policy_name,
                    "local_id_fqdn": ufqdn,
                    "ike_lifetime": 24,
                    "encryption": "aes256",
                    "dh_group": 24,
                }
            )
            ip_security["sa_policies"].append(
                {
                    "name": sa_policy_name,
                    "pfs_dh_group": 24,
                    "sa_lifetime": {"value": 8},
                    "esp": {
                        "integrity": "sha256",
                        "encryption": "disabled",
                    },
                }
            )
            ip_security["profiles"].append(
                {
                    "name": profile_name,
                    "ike_policy": ike_policy_name,
                    "sa_policy": sa_policy_name,
                    "shared_key": ipsec_key,
                    "dpd": {
                        "interval": 10,
                        "time": 60,
                        "action": "clear",
                    },
                }
            )

        return strip_null_from_data(ip_security)

    def _generate_ipsec_key(self, name: str, salt: str) -> str:
        """
        Build a secret containing various components for this policy and device.
        Run type-7 obfuscation using a algoritmic salt so we ensure the same key every time.

        TODO: Maybe introduce some formatting with max length of each element, since the keys can be come very very long.
        """
        secret = "_".join((self.shared_utils.hostname, name, salt))
        type_7_salt = sum(salt.encode("utf-8")) % 16
        return simple_7_encrypt(secret, type_7_salt)
