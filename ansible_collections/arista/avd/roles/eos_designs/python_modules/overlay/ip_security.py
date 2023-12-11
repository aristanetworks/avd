# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

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
        ip_security set based on autovpn_ipsec data_model
        """
        if not self.shared_utils.wan_role:
            return None

        wan_ipsec_profiles = get(self._hostvars, "wan_ipsec_profiles", required=True)

        ike_policies = []
        sa_policies = []
        profiles = []

        ip_security = {"ike_policies": ike_policies, "sa_policies": sa_policies, "profiles": profiles}

        if (data_plane := get(wan_ipsec_profiles, "data_plane", None)) is not None:
            ike_policy_name = get(data_plane, "ike_policy_name", "DP-IKE-POLICY")
            sa_policy_name = get(data_plane, "sa_policy_name", "DP-SA-POLICY")
            profile_name = get(data_plane, "profile_name", "DP-PROFILE")
            key = get(data_plane, "shared_key", required=True)

            ike_policies.append(self._ike_policy(ike_policy_name))
            sa_policies.append(self._sa_policy(sa_policy_name))
            profiles.append(self._profile(profile_name, ike_policy_name, sa_policy_name, key))

            # For data plane, adding this
            ip_security["key_controller"] = self._key_controller(profile_name)

        if (control_plane := get(wan_ipsec_profiles, "control_plane", None)) is not None:
            ike_policy_name = get(control_plane, "ike_policy_name", "CP-IKE-POLICY")
            sa_policy_name = get(control_plane, "sa_policy_name", "CP-SA-POLICY")
            profile_name = get(control_plane, "profile_name", "CP-PROFILE")
            key = get(control_plane, "shared_key", required=True)

            ike_policies.append(self._ike_policy(ike_policy_name))
            sa_policies.append(self._sa_policy(sa_policy_name))
            profiles.append(self._profile(profile_name, ike_policy_name, sa_policy_name, key))

            if not ip_security.get("key_controller"):
                # If there is not data plane IPSec profile, use the control plane one for key controller
                ip_security["key_controller"] = self._key_controller(profile_name)

        return strip_null_from_data(ip_security)

    def _ike_policy(self, name: str) -> dict | None:
        """
        Return an IKE policy
        """
        return {
            "name": name,
            "local_id": self.shared_utils.router_id,
        }

    def _sa_policy(self, name: str) -> dict | None:
        """
        Return an SA policy
        """
        sa_policy = {"name": name}
        if self.shared_utils.cv_pathfinder_role:
            # TODO, provide options to change this cv_pathfinder_wide
            sa_policy["esp"] = {"encryption": "aes128"}
            sa_policy["pfs_dh_group"] = 14
        return sa_policy

    def _profile(self, profile_name: str, ike_policy_name: str, sa_policy_name: str, key: str) -> dict | None:
        """
        Return one IPsec Profile
        """
        return {
            "name": profile_name,
            "ike_policy": ike_policy_name,
            "sa_policy": sa_policy_name,
            "connection": "start",
            "shared_key": key,
            "dpd": {"interval": 10, "time": 50, "action": "clear"},
            "mode": "transport",
        }

    def _key_controller(self, profile_name: str) -> dict | None:
        """
        Return a key_controller structure if the device is not a RR or pathfinder
        """
        if self.shared_utils.wan_role != "client":
            return None

        return {"profile": profile_name}
