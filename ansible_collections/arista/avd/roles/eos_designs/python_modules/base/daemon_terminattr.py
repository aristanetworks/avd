# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_null_from_data
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class DaemonTerminattrMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def daemon_terminattr(self) -> dict | None:
        cv_settings = get(self._hostvars, "cv_settings")
        if not cv_settings:
            return self._get_deprecated_daemon_terminattr()

        daemon_terminattr = {}
        clusters = self._get_terminattr_clusters(cv_settings)
        if not clusters:
            return None

        if len(clusters) == 1:
            clusters[0].pop("name")
            daemon_terminattr.update(**clusters[0])
        else:
            daemon_terminattr["clusters"] = clusters

        daemon_terminattr.update(
            {
                "disable_aaa": get(cv_settings, "terminattr_disable_aaa", default=False),
                "ingestexclude": get(cv_settings, "terminattr_ingestexclude", default="/Sysdb/cell/1/agent,/Sysdb/cell/2/agent"),
                "smashexcludes": get(cv_settings, "terminattr_smashexcludes", default="ale,flexCounter,hardware,kni,pulse,strata"),
            }
        )
        return strip_null_from_data(daemon_terminattr) or None

    def _get_terminattr_clusters(self, cv_settings: dict) -> list:
        clusters = []
        for cluster in get(cv_settings, "cvaas_clusters", default=[]):
            vrf = self._get_terminattr_vrf(get(cluster, "vrf"), f"cv_settings.cvaas_clusters[name={cluster['name']}].vrf")
            source_interface = self._get_terminattr_source_interface(
                get(cluster, "source_interface"), f"cv_settings.cvaas_clusters[name={cluster['name']}].source_interface"
            )
            if not (vrf or source_interface):
                raise AristaAvdError(f"'vrf' or 'source_interface' must be set for cv_settings.cvaas_clusters.{cluster['name']}")
            clusters.append(
                {
                    "name": cluster["name"],
                    "cvaddrs": [f"{cluster['server']}:443"],
                    "cvauth": {
                        "method": "token-secure",
                        "token_file": get(cluster, "token_file", default="/tmp/cv-onboarding-token"),
                    },
                    "cvvrf": vrf if vrf != "default" else None,
                    "cvsourceintf": source_interface,
                }
            )

        for cluster in get(cv_settings, "onprem_clusters", default=[]):
            vrf = self._get_terminattr_vrf(get(cluster, "vrf"), f"cv_settings.onprem_clusters[name={cluster['name']}].vrf")
            source_interface = self._get_terminattr_source_interface(
                get(cluster, "source_interface"), f"cv_settings.onprem_clusters[name={cluster['name']}].source_interface"
            )
            if not (vrf or source_interface):
                raise AristaAvdError(f"'vrf' or 'source_interface' must be set for cv_settings.onprem_clusters.{cluster['name']}")
            use_key = get(cluster, "key") is not None
            clusters.append(
                {
                    "name": cluster["name"],
                    "cvaddrs": [f"{server['name']}:{get(server, 'port', default=9910)}" for server in cluster["servers"]],
                    "cvauth": {
                        "method": "key" if use_key else "token",
                        "key": cluster["key"] if use_key else None,
                        "token_file": get(cluster, "token_file", "/tmp/token") if not use_key else None,
                    },
                    "cvvrf": vrf if vrf != "default" else None,
                    "cvsourceintf": source_interface,
                }
            )

        return clusters

    def _get_terminattr_vrf(self, vrf: str, org_var: str) -> str:
        """
        Returns either the VRF given or the relevant mgmt VRF depending on special values
        `use_mgmt_interface_vrf` or `use_inband_mgmt_vrf`.

        Errors will be raised if the VRF does not match relevant management settings.
        """
        if vrf == "use_mgmt_interface_vrf":
            has_mgmt_ip = (self.shared_utils.mgmt_ip is not None) or (self.shared_utils.ipv6_mgmt_ip is not None)
            if not has_mgmt_ip:
                raise AristaAvdError(f"'{org_var}' is set to 'use_mgmt_interface_vrf' but this node is missing an 'mgmt_ip'")

            return self.shared_utils.mgmt_interface_vrf

        if vrf == "use_inband_mgmt_vrf":
            if self.shared_utils.inband_mgmt_interface is None:
                raise AristaAvdError("'{org_var}' is set to 'use_inband_mgmt_vrf' but this node is missing configuration for inband management")

            # self.shared_utils.inband_mgmt_vrf returns None for the default VRF.
            return self.shared_utils.inband_mgmt_vrf or "default"

        # Returning the given VRF name.
        return vrf

    def _get_terminattr_source_interface(self, source_interface: str, org_var: str) -> str:
        """
        Returns either the source_interface given or the relevant mgmt source intf depending on special values
        `use_mgmt_interface` or `use_inband_mgmt_interface`.

        Errors will be raised if the VRF does not match relevant management settings.
        """
        if source_interface == "use_mgmt_interface":
            has_mgmt_ip = (self.shared_utils.mgmt_ip is not None) or (self.shared_utils.ipv6_mgmt_ip is not None)
            if not has_mgmt_ip:
                raise AristaAvdError(f"'{org_var}' is set to 'use_mgmt_interface_vrf' but this node is missing an 'mgmt_ip'")

            return self.shared_utils.mgmt_interface

        if source_interface == "use_inband_mgmt_interface":
            if self.shared_utils.inband_mgmt_interface is None:
                raise AristaAvdError("'{org_var}' is set to 'use_inband_mgmt_vrf' but this node is missing configuration for inband management")

            return self.shared_utils.inband_mgmt_interface

        # Returning the given source interface name.
        return source_interface

    def _get_deprecated_daemon_terminattr(self) -> dict | None:
        """
        daemon_terminattr set based on the deprecated cvp_instance_ip and cvp_instance_ips variables

        Updating cvaddrs and cvauth considering conditions for cvaas and cvp_on_prem IPs

            if 'arista.io' in cvp_instance_ip:
                 <updating as cvaas_ip>
            else:
                 <updating as cvp_on_prem ip>
        """
        # cvp_instance_ip will be removed in AVD5.0
        cvp_instance_ip = get(self._hostvars, "cvp_instance_ip")
        cvp_instance_ip_list = get(self._hostvars, "cvp_instance_ips", [])
        if cvp_instance_ip is not None:
            cvp_instance_ip_list.append(cvp_instance_ip)
        if not cvp_instance_ip_list:
            return None

        daemon_terminattr = {"cvaddrs": []}
        for cvp_instance_ip in cvp_instance_ip_list:
            if "arista.io" in cvp_instance_ip:
                # updating for cvaas_ips
                daemon_terminattr["cvaddrs"].append(f"{cvp_instance_ip}:443")
                daemon_terminattr["cvauth"] = {
                    "method": "token-secure",
                    "token_file": get(self._hostvars, "cvp_token_file", "/tmp/cv-onboarding-token"),
                }
            else:
                # updating for cvp_on_prem_ips
                cv_address = f"{cvp_instance_ip}:{get(self._hostvars, 'terminattr_ingestgrpcurl_port', default=9910)}"
                daemon_terminattr["cvaddrs"].append(cv_address)
                if (cvp_ingestauth_key := get(self._hostvars, "cvp_ingestauth_key")) is not None:
                    daemon_terminattr["cvauth"] = {
                        "method": "key",
                        "key": cvp_ingestauth_key,
                    }
                else:
                    daemon_terminattr["cvauth"] = {
                        "method": "token",
                        "token_file": get(self._hostvars, "cvp_token_file", "/tmp/token"),
                    }

        daemon_terminattr["cvvrf"] = self.shared_utils.mgmt_interface_vrf
        daemon_terminattr["smashexcludes"] = get(self._hostvars, "terminattr_smashexcludes", default="ale,flexCounter,hardware,kni,pulse,strata")
        daemon_terminattr["ingestexclude"] = get(self._hostvars, "terminattr_ingestexclude", default="/Sysdb/cell/1/agent,/Sysdb/cell/2/agent")
        daemon_terminattr["disable_aaa"] = get(self._hostvars, "terminattr_disable_aaa", False)

        return daemon_terminattr
