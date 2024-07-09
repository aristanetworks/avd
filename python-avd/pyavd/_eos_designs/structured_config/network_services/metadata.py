# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ...._utils import get, strip_empties_from_list
from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class MetadataMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def metadata(self: AvdStructuredConfigNetworkServices) -> dict | None:
        """
        Generate metadata.cv_pathfinder.internet_exit_policies if available.
        """
        if not self._filtered_internet_exit_policies:
            return None

        internet_exit_polices = []
        for internet_exit_policy in self._filtered_internet_exit_policies:
            # Currently only supporting zscaler
            if internet_exit_policy["type"] != "zscaler":
                continue

            ufqdn, ipsec_key = self._get_ipsec_credentials(internet_exit_policy)
            internet_exit_polices.append(
                {
                    "name": internet_exit_policy["name"],
                    "type": internet_exit_policy["type"],
                    "city": get(self._zscaler_endpoints, "device_location.city", required=True, org_key="zscaler_endpoints.device_location.city"),
                    "country": get(self._zscaler_endpoints, "device_location.country", required=True, org_key="zscaler_endpoints.device_location.country"),
                    "upload_bandwidth": get(internet_exit_policy, "zscaler.upload_bandwidth"),
                    "download_bandwidth": get(internet_exit_policy, "zscaler.download_bandwidth"),
                    "firewall": get(internet_exit_policy, "zscaler.firewall.enabled", default=False),
                    "ips_control": get(internet_exit_policy, "zscaler.firewall.ips", default=False),
                    "acceptable_use_policy": get(internet_exit_policy, "zscaler.acceptable_use_policy", default=False),
                    "vpn_credentials": [
                        {
                            "fqdn": ufqdn,
                            "vpn_type": "UFQDN",
                            "pre_shared_key": ipsec_key,
                        }
                    ],
                    "tunnels": [
                        {
                            "name": f"Tunnel{connection['tunnel_id']}",
                            "preference": "Preferred" if connection["preference"] == "primary" else "Alternate",
                        }
                        for connection in internet_exit_policy["connections"]
                    ],
                }
            )

        return {"cv_pathfinder": {"internet_exit_policies": strip_empties_from_list(internet_exit_polices, (None, [], {}))}}
