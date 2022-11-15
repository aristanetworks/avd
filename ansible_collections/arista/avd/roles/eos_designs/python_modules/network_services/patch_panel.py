from __future__ import annotations

import re
from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class PatchPanelMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def patch_panel(self) -> dict | None:
        """
        Return structured config for patch_panel
        """

        if not self._network_services_l1:
            return None

        patches = []
        for tenant in self._filtered_tenants:
            if "point_to_point_services" not in tenant:
                continue

            for point_to_point_service in natural_sort(tenant["point_to_point_services"], "name"):
                if subifs := point_to_point_service.get("subinterfaces", []):
                    subifs = [subif for subif in subifs if subif.get("number") is not None]
                for endpoint in point_to_point_service.get("endpoints", []):
                    if self._hostname not in endpoint.get("nodes", []):
                        continue

                    node_index = list(endpoint["nodes"]).index(self._hostname)
                    interface = endpoint["interfaces"][node_index]
                    if get(endpoint, "port_channel.mode") in ["active", "on"]:
                        channel_group_id = "".join(re.findall(r"\d", interface))
                        interface = f"Port-Channel{channel_group_id}"

                    if subifs:
                        for subif in subifs:
                            patch = {
                                "name": f"{point_to_point_service['name']}_{subif['number']}",
                                "enabled": True,
                                "connectors": [
                                    {
                                        "id": 1,
                                        "type": "interface",
                                        "endpoint": f"{interface}.{subif['number']}",
                                    },
                                ],
                            }
                            if point_to_point_service.get("type") == "vpws-pseudowire":
                                patch["connectors"].append(
                                    {
                                        "id": 2,
                                        "type": "pseudowire",
                                        "endpoint": f"bgp vpws {tenant['name']} pseudowire {point_to_point_service['name']}_{subif['number']}",
                                    }
                                )
                            patches.append(patch)
                    else:
                        patch = {
                            "name": f"{point_to_point_service['name']}",
                            "enabled": True,
                            "connectors": [
                                {
                                    "id": 1,
                                    "type": "interface",
                                    "endpoint": f"{interface}",
                                }
                            ],
                        }
                        if point_to_point_service.get("type") == "vpws-pseudowire":
                            patch["connectors"].append(
                                {
                                    "id": 2,
                                    "type": "pseudowire",
                                    "endpoint": f"bgp vpws {tenant['name']} pseudowire {point_to_point_service['name']}",
                                }
                            )
                        patches.append(patch)

        if patches:
            return {"patches": patches}

        return None
