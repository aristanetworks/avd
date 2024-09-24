# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Any

from pyavd._errors import AristaAvdError
from pyavd._utils import default, get, get_item, strip_empties_from_dict, strip_empties_from_list

if TYPE_CHECKING:
    from . import AvdStructuredConfigMetadata

INVALID_CUSTOM_DEVICE_TAGS = [
    "topology_hint_type",
    "topology_type",
    "topology_hint_datacenter",
    "topology_datacenter",
    "topology_hint_rack",
    "topology_rack",
    "topology_pod",
    "topology_hint_pod",
    "eos",
    "eostrain",
    "ztp",
    "bgp",
    "container",
    "mpls",
    "topology_network_type",
    "model",
    "systype",
    "serialnumber",
    "tapagg",
    "hostname",
    "terminattr",
]
"""These tag names overlap with CV system tags or topology_hints"""


class CvTagsMixin:
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def _generate_cv_tags(self: AvdStructuredConfigMetadata) -> dict:
        return get(self._hostvars, "generate_cv_tags", default={})

    def _cv_tags(self: AvdStructuredConfigMetadata) -> dict | None:
        """Generate the data structure `metadata.cv_tags`."""
        if not self._generate_cv_tags and not self.shared_utils.is_cv_pathfinder_router:
            return None

        device_tags = self._get_topology_hints()
        device_tags.extend(self._get_cv_pathfinder_device_tags())
        device_tags.extend(self._get_device_tags())

        cv_tags = {"device_tags": device_tags, "interface_tags": self._get_interface_tags()}

        return strip_empties_from_dict(cv_tags) or None

    @staticmethod
    def _tag_dict(name: str, value: Any) -> dict | None:
        if value is None:
            return None
        return {"name": name, "value": str(value)}

    def _get_topology_hints(self: AvdStructuredConfigMetadata) -> list:
        """Return list of topology_hint tags."""
        if get(self._generate_cv_tags, "topology_hints") is not True:
            return []

        default_type_hint = get(self.shared_utils.node_type_key_data, "cv_tags_topology_type")
        return strip_empties_from_list(
            [
                self._tag_dict("topology_hint_datacenter", self.shared_utils.dc_name),
                self._tag_dict("topology_hint_fabric", self.shared_utils.fabric_name),
                self._tag_dict("topology_hint_pod", self.shared_utils.pod_name),
                self._tag_dict("topology_hint_type", get(self._hostvars, "cv_tags_topology_type", default=default_type_hint)),
                self._tag_dict("topology_hint_rack", default(self.shared_utils.rack, self.shared_utils.group)),
            ],
        )

    def _get_cv_pathfinder_device_tags(self: AvdStructuredConfigMetadata) -> list:
        """
        Return list of device_tags for cv_pathfinder solution.

        Example: [
            {"name": "Region", "value": <value copied from cv_pathfinder_region>},
            {"name": "Zone", "value": <"<region-name>-ZONE" for pathfinder clients>},
            {"name": "Site", "value": <value copied from cv_pathfinder_site for pathfinder clients>},
            {"name": "PathfinderSet", "value": <value copied from node group or default "PATHFINDERS" for pathfinder servers>},
            {"name": "Role", "value": <'pathfinder', 'edge', 'transit region' or 'transit zone'>}
        ].
        """
        if not self.shared_utils.is_cv_pathfinder_router:
            return []

        device_tags = [
            self._tag_dict("Role", self.shared_utils.cv_pathfinder_role),
            self._tag_dict("Region", get(self.shared_utils.wan_region or {}, "name")),
        ]
        if self.shared_utils.is_cv_pathfinder_server:
            device_tags.append(self._tag_dict("PathfinderSet", self.shared_utils.group or "PATHFINDERS"))
        else:
            device_tags.extend(
                [
                    self._tag_dict("Zone", self.shared_utils.wan_zone["name"]),
                    self._tag_dict("Site", self.shared_utils.wan_site["name"]),
                ],
            )

        return strip_empties_from_list(device_tags)

    def _get_device_tags(self: AvdStructuredConfigMetadata) -> list:
        """Return list of device_tags."""
        if not (tags_to_generate := get(self._generate_cv_tags, "device_tags")):
            return []

        device_tags = []
        for generate_tag in tags_to_generate:
            if generate_tag["name"] in INVALID_CUSTOM_DEVICE_TAGS:
                msg = (
                    f"The CloudVision tag name 'generate_cv_tags.device_tags[name={generate_tag['name']}] is invalid. "
                    "System Tags cannot be overridden. Try using a different name for this tag."
                )
                raise AristaAvdError(
                    msg,
                )

            # Get value from either 'value' key, structured config based on the 'data_path' key or raise.
            if get(generate_tag, "value") is not None:
                value = generate_tag["value"]
            elif get(generate_tag, "data_path") is not None:
                value = get(self._hostvars, generate_tag["data_path"])
                if type(value) in [list, dict]:
                    msg = (
                        f"'generate_cv_tags.device_tags[name={generate_tag['name']}].data_path' ({generate_tag['data_path']}) "
                        f"points to a variable of type {type(value).__name__}. This is not supported for cloudvision tag data_paths."
                    )
                    raise AristaAvdError(
                        msg,
                    )
            else:
                msg = f"'generate_cv_tags.device_tags[name={generate_tag['name']}]' is missing either a static 'value' or a dynamic 'data_path'"
                raise AristaAvdError(msg)

            # Silently ignoring empty values since structured config may vary between devices.
            if value:
                device_tags.append(self._tag_dict(generate_tag["name"], value))

        return device_tags

    def _get_interface_tags(self: AvdStructuredConfigMetadata) -> list:
        """Return list of interface_tags."""
        if not (tags_to_generate := get(self._generate_cv_tags, "interface_tags", default=[])) and not self.shared_utils.is_cv_pathfinder_router:
            return []

        interface_tags = []
        for ethernet_interface in get(self._hostvars, "ethernet_interfaces", default=[]):
            tags = []
            for generate_tag in tags_to_generate:
                # Get value from either 'value' key, structured config based on the 'data_path' key or raise.
                if get(generate_tag, "value") is not None:
                    value = generate_tag["value"]
                elif get(generate_tag, "data_path") is not None:
                    value = get(ethernet_interface, generate_tag["data_path"])
                    if type(value) in [list, dict]:
                        msg = (
                            f"'generate_cv_tags.interface_tags[name={generate_tag['name']}].data_path' ({generate_tag['data_path']}) "
                            f"points to a variable of type {type(value).__name__}. This is not supported for cloudvision tag data_paths."
                        )
                        raise AristaAvdError(
                            msg,
                        )
                else:
                    msg = f"'generate_cv_tags.interface_tags[name={generate_tag['name']}]' is missing either a static 'value' or a dynamic 'data_path'"
                    raise AristaAvdError(
                        msg,
                    )

                # Silently ignoring empty values since structured config may vary between devices.
                if value:
                    tags.append(self._tag_dict(generate_tag["name"], value))

            if self.shared_utils.is_cv_pathfinder_router:
                tags.extend(self._get_cv_pathfinder_interface_tags(ethernet_interface))

            if tags:
                interface_tags.append({"interface": ethernet_interface["name"], "tags": tags})

        return interface_tags

    def _get_cv_pathfinder_interface_tags(self: AvdStructuredConfigMetadata, ethernet_interface: dict) -> list:
        """
        Return list of device_tags for cv_pathfinder solution.

        Example: [
            {"name": "Type", <"lan" or "wan">},
            {"name": "Carrier", <value copied from wan_carrier if this is a wan interface>},
            {"name": "Circuit", <value copied from wan_circuit_id if this is a wan interface>}
        ].
        """
        if ethernet_interface["name"] in self._wan_interface_names:
            wan_interface = get_item(self.shared_utils.wan_interfaces, "name", ethernet_interface["name"], required=True)
            return strip_empties_from_list(
                [
                    self._tag_dict("Type", "wan"),
                    self._tag_dict("Carrier", get(wan_interface, "wan_carrier")),
                    self._tag_dict("Circuit", get(wan_interface, "wan_circuit_id")),
                ],
            )

        return [self._tag_dict("Type", "lan")]

    @cached_property
    def _wan_interface_names(self: AvdStructuredConfigMetadata) -> list:
        return [wan_interface["name"] for wan_interface in self.shared_utils.wan_interfaces]
