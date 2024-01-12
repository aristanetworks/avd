# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

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
        Only relevant if cv_pathfinder_role is not None
        """
        if self.shared_utils.cv_pathfinder_role is None:
            return None

        # Pathfinder
        if self.shared_utils.cv_pathfinder_role == "pathfinder":
            return {
                "role": self.shared_utils.cv_pathfinder_role,
                "ssl_profile": None,  # TODO: Pick up ssl profile from self.shared_utils.this_wan_route_server.ssl_profile_name
                "vtep_ip": self.shared_utils.router_id,
                "interfaces": self._metadata_interfaces(),
                "pathgroups": self._metadata_pathgroups(),
                "regions": self._metadata_regions(),
                "vrfs": self._metadata_vrfs(),
            }

        # Edge or transit
        return {
            "role": self.shared_utils.cv_pathfinder_role,
            "vtep_ip": self.shared_utils.router_id,
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
                "public_ip": str(interface["ip_address"]).split("/", maxsplit=1)[0] if self.shared_utils.cv_pathfinder_role == "pathfinder" else None,
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
                                "location": site.get("location"),
                            }
                            for site in region["sites"]
                        ],
                    }
                ],
            }
            for region in regions
        ]

    def _metadata_vrfs(self: AvdStructuredConfigMetadata) -> list:
        return []  # TODO

    def _metadata_pathfinder_vtep_ips(self: AvdStructuredConfigMetadata) -> list:
        return [
            {
                "vtep_ip": wan_route_server["router_id"],
            }
            for wan_route_server in self.shared_utils.filtered_wan_route_servers.values()
        ]
