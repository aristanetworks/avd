# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_null_from_data

from .cv_tags import CvTagsMixin


class AvdStructuredConfigMetadata(AvdFacts, CvTagsMixin):
    """
    This returns the metadata data strucutre as per the below example
    {
        "metadata": {
            "platform": "7050X3",
            "cv_tags": {
                "device_tags": [
                    {"name": "topology_hint_type", "value": <topology_hint_type taken from node_type_keys.[].cvp_tags.topology_hint_type> },
                    {"name: "topology_hint_dc", "value": <taken from the dc_name> },
                    {"name": "topology_hint_fabric", "value": <value copied from fabric_name>},
                    {"name": "topology_hint_pod", "value": <value copied from pod_name>},
                    {"name": "topolgoy_hint_rack", "value": <value copied from rack field if it is defined for the node>},
                    {"name": "<custom_tag_name>", "value": "custom tag value"},
                    {"name": "<custom_tag_name>", "value": "<value extracted from structured_config>"},
                    {"name": "Region", "value": <value copied from cv_pathfinder_region if cv_pathfinder_role is set but not 'pathfinder'>},
                    {"name": "Zone", "value": <always "DEFAULT-ZONE" if cv_pathfinder_role is set but not 'pathfinder'>},
                    {"name": "Site", "value": <value copied from cv_pathfinder_site if cv_pathfinder_role is set but not 'pathfinder'>},
                    {"name": "PathfinderSet", "value": <value copied from node group or default "PATHFINDERS" if cv_pathfinder_role is 'pathfinder'>},
                    {"name": "Role", "value": <value copied from cv_pathfinder_role if set>}
                },
                "interface_tags": [
                    {
                        "interface": "Ethernet1",
                        "tags":[
                            {"name": "peer", "value": "leaf1a"}
                            {"name": "Type", <"lan" or "wan" if cv_pathfinder_role is set>},
                            {"name": "Carrier", <value copied from wan_carrier if cv_pathfinder_role is set and this is a wan interface>},
                            {"name": "Circuit", <value copied from wan_circuit_id if cv_pathfinder_role is set and this is a wan interface>}
                        ]
                    }
                ]
            }
        }
    }
    """

    @cached_property
    def metadata(self) -> dict | None:
        metadata = {
            "platform": self.shared_utils.platform,
            "cv_tags": self._cv_tags(),
        }
        return strip_null_from_data(metadata) or None
