# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item

if TYPE_CHECKING:
    from .avdstructuredconfig import AvdStructuredConfigMetadata


class CvPathfinderMixin:
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    def _cv_pathfinder(self: AvdStructuredConfigMetadata) -> dict | None:
        """
        Generate metadata for CV Pathfinder feature.
        Only relevant for cv_pathfinder routers
        """
        if not self.shared_utils.is_cv_pathfinder_router:
            return None

        # Pathfinder
        if self.shared_utils.is_cv_pathfinder_server:
            return {
                "role": self.shared_utils.cv_pathfinder_role,
                "ssl_profile": self.shared_utils.wan_stun_dtls_profile_name,
                "vtep_ip": self.shared_utils.vtep_ip,
                "interfaces": self._metadata_interfaces(),
                "pathgroups": self._metadata_pathgroups(),
                "regions": self._metadata_regions(),
                "vrfs": self._metadata_vrfs(),
            }

        # Edge or transit
        return {
            "role": self.shared_utils.cv_pathfinder_role,
            "vtep_ip": self.shared_utils.vtep_ip,
            "region": self.shared_utils.wan_region["name"],
            "zone": self.shared_utils.wan_zone["name"],
            "site": self.shared_utils.wan_site["name"],
            "interfaces": self._metadata_interfaces(),
            "pathfinders": self._metadata_pathfinder_vtep_ips(),
        }

    def _metadata_interfaces(self: AvdStructuredConfigMetadata) -> list:
        return [
            {
                "name": interface["name"],
                "carrier": carrier["name"],
                "circuit_id": interface.get("wan_circuit_id"),
                "pathgroup": carrier["path_group"],
                "public_ip": str(interface["ip_address"]).split("/", maxsplit=1)[0] if self.shared_utils.is_cv_pathfinder_server else None,
            }
            for carrier in self.shared_utils.wan_local_carriers
            for interface in carrier["interfaces"]
        ]

    def _metadata_pathgroups(self: AvdStructuredConfigMetadata) -> list:
        return [
            {
                "name": pathgroup["name"],
                "carriers": [
                    {
                        "name": carrier["name"],
                    }
                    for carrier in self.shared_utils.wan_carriers
                    if carrier["path_group"] == pathgroup["name"]
                ],
                "imported_carriers": [
                    {
                        "name": carrier["name"],
                    }
                    for carrier in self.shared_utils.wan_carriers
                    if carrier["path_group"] in [imported_pathgroup["remote"] for imported_pathgroup in pathgroup.get("import_path_groups", [])]
                ],
            }
            for pathgroup in self.shared_utils.wan_path_groups
        ]

    def _metadata_regions(self: AvdStructuredConfigMetadata) -> list:
        regions = get(
            self._hostvars, "cv_pathfinder_regions", required=True, org_key="'cv_pathfinder_regions' key must be set when 'wan_mode' is 'cv-pathfinder'."
        )
        return [
            {
                "name": region["name"],
                "id": region["id"],
                "zones": [
                    {
                        # TODO: Once we give configurable zones this should be updated
                        "name": self.shared_utils.wan_zone["name"],
                        "id": self.shared_utils.wan_zone["id"],
                        "sites": [
                            {
                                "name": site["name"],
                                "id": site["id"],
                                "location": (
                                    {
                                        "address": site.get("location"),
                                    }
                                    if site.get("location")
                                    else None
                                ),
                            }
                            for site in region["sites"]
                        ],
                    }
                ],
            }
            for region in regions
        ]

    def _metadata_pathfinder_vtep_ips(self: AvdStructuredConfigMetadata) -> list:
        return [
            {
                "vtep_ip": wan_route_server["vtep_ip"],
            }
            for wan_route_server in self.shared_utils.filtered_wan_route_servers.values()
        ]

    def _metadata_vrfs(self: AvdStructuredConfigMetadata) -> list:
        """
        Extracting metadata for VRFs by parsing the generated structured config
        and flatten it a bit (like hiding load-balance policies)
        """
        if (avt_vrfs := get(self._hostvars, "router_adaptive_virtual_topology.vrfs")) is None:
            return []

        if (load_balance_policies := get(self._hostvars, "router_path_selection.load_balance_policies")) is None:
            return []

        return [
            {
                "name": vrf["name"],
                "vni": self._get_vni_for_vrf_name(vrf["name"]),
                "avts": [
                    {
                        "constraints": {
                            "jitter": lb_policy.get("jitter"),
                            "latency": lb_policy.get("latency"),
                            "lossrate": float(lb_policy["lossrate"]) if "lossrate" in lb_policy else None,
                        },
                        "description": "",  # TODO: Not sure we have this field anywhere
                        "id": profile["id"],
                        "name": profile["name"],
                        "pathgroups": [
                            {
                                "name": pathgroup["name"],
                                "preference": "alternate" if pathgroup.get("priority", 1) > 1 else "preferred",
                            }
                            for pathgroup in lb_policy["path_groups"]
                        ],
                    }
                    for profile in vrf["profiles"]
                    for lb_policy in [get_item(load_balance_policies, "name", self.shared_utils.generate_lb_policy_name(profile["name"]), required=True)]
                ],
            }
            for vrf in avt_vrfs
        ]

    @cached_property
    def _all_vrfs_from_all_tenants(self: AvdStructuredConfigMetadata) -> list[dict]:
        """
        Unfiltered list of VRFs found under tenants.
        Used to find VNI for each VRF used in cv_pathfinder.

        We cannot use filtered_tenants since pathfinders do not necessarily have all VRFs defined in the policies.

        Potential issue with this is if some VRFs are defined multiple times with different information.
        """
        all_vrfs = [
            vrf
            for network_services_key in self.shared_utils.network_services_keys
            for tenant in convert_dicts(get(self._hostvars, network_services_key["name"]), "name")
            for vrf in tenant["vrfs"]
        ]
        # Add the default WAN VRF at the end. Will only be reached if default VRF was not defined in inputs
        all_vrfs.append({"name": "default", "vrf_id": 1})
        return all_vrfs

    def _get_vni_for_vrf_name(self: AvdStructuredConfigMetadata, vrf_name: str):
        if (vrf := get_item(self._all_vrfs_from_all_tenants, "name", vrf_name)) is None:
            raise AristaAvdError(f"Unable to find VNI for VRF {vrf_name} during generation of cv_pathfinder metadata.")

        return self.shared_utils.get_vrf_vni(vrf)
