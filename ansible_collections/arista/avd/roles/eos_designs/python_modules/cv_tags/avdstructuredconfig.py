# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

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


class AvdStructuredConfigTags(AvdFacts):
    """
    This returns the cv_tags data strucutre as per the below example
    {
        "cv_tags": {
            "device_tags": [
                {"name": "topology_hint_type", "value": <topology_hint_type taken from node_type_keys.[].cvp_tags.topology_hint_type> },
                {"name: "topology_hint_dc", "value": <taken from the dc_name> },
                {"name": "topology_hint_fabric", "value": <value copied from fabric_name>},
                {"name": "topology_hint_pod", "value": <value copied from pod_name>},
                {"name": "topolgoy_hint_rack", "value": <value copied from rack field if it is defined for the node>},
                {"name": "<custom_tag_name>", "value": "custom tag value"},
                {"name": "<gerenrated_tag_name>", "value": "<value extracted from structured_config>"}
            },
            "interface_tags": [
                {
                    "interface": "Ethernet1",
                    "tags":[
                        {
                            "name": "peer"
                            "value": "leaf1a"
                        }
                    ]
                }
            ]
        },
    }

    """

    @cached_property
    def cv_tags(self) -> str | None:
        """
        Generate the data structure `cv_tags`.
        """
        if not get(self._hostvars, "cv_tags_enabled", False):
            # We do not want to define this datastructure if the feature is not
            # enabled
            return

        hints = [self._topology_hint_dc, self._topology_hint_fabric, self._topology_hint_pod, self._topology_hint_type, self._topology_hint_rack]
        device_tags = [hint for hint in hints if hint]

        for custom_tag in get(self._hostvars, "cv_tags_device_custom", []):
            if custom_tag["name"].lower() not in INVALID_CUSTOM_DEVICE_TAGS:
                device_tags.append(custom_tag)
            else:
                raise AristaAvdError(
                    f"The CloudVision tag name {custom_tag['name']} is Invalid. System Tags cannot be overriden. Try using a different name for this tag."
                )

        for generate_tag in get(self._hostvars, "cv_tags_generate_device", []):
            value = get(self._hostvars, generate_tag["field"], None)
            if generate_tag["name"] in INVALID_CUSTOM_DEVICE_TAGS:
                raise AristaAvdError(
                    f"The CloudVision tag name {generate_tag['name']} is Invalid. System Tags cannot be overriden. Try using a different name for this tag."
                )
            if type(value) in [list, dict]:
                raise AristaAvdError(f"The field {generate_tag['field']} appears to be a {type(value).__name__}. This is not supported for cloudvision fields.")
            if value is not None:
                device_tags.append(self._tag_dict(generate_tag["name"], value))

        interface_tags = []
        for link in get(self._hostvars, "ethernet_interfaces", []):
            interface_tags.extend(self._interface_tags(link))

        result = {"device_tags": device_tags}
        if interface_tags:
            result["interface_tags"] = interface_tags

        return result

    def _tag_dict(self, name, value) -> dict:
        return {"name": name, "value": str(value)}

    @cached_property
    def _topology_hint_type(self) -> dict | None:
        """
        Return the topology hint type for the device.
        """
        hint_type = get(self.shared_utils.node_type_key_data, "cv_tags_topology_type")

        hint_type = get(self._hostvars, "cv_tags_topology_type", hint_type)

        if not hint_type:
            return None

        return self._tag_dict("topology_hint_type", hint_type)

    @cached_property
    def _topology_hint_fabric(self) -> dict:
        """
        Return the topology fabric hint tag.
        """
        # `fabric_name` is required for any fabric, so we don't need to handle
        # the case this is not available
        return self._tag_dict("topology_hint_fabric", self.shared_utils.fabric_name)

    @cached_property
    def _topology_hint_pod(self) -> dict | None:
        """
        Return the topology fabric hint tag.
        """
        if not self.shared_utils.pod_name:
            return None

        return self._tag_dict("topology_hint_pod", self.shared_utils.pod_name)

    @cached_property
    def _topology_hint_dc(self) -> dict | None:
        """
        Return the topology fabric hint tag.
        """
        if not self.shared_utils.dc_name:
            return None
        return self._tag_dict("topology_hint_datacenter", self.shared_utils.dc_name)

    @cached_property
    def _topology_hint_rack(self) -> dict | None:
        """
        Return the topology hint for the rack tag.
        """
        if not self.shared_utils.rack:
            return None
        return self._tag_dict("topology_hint_rack", self.shared_utils.rack)

    def _interface_tags(self, link) -> list:
        tags = []

        for generate_tag in get(self._hostvars, "cv_tags_generate_interface", []):
            value = get(link, generate_tag["field"])
            if generate_tag["name"] in INVALID_CUSTOM_DEVICE_TAGS:
                raise AristaAvdError(
                    f"The CloudVision tag name {generate_tag['name']} is Invalid. System Tags cannot be overriden. Try using a different name for this tag."
                )
            if type(value) in [list, dict]:
                raise AristaAvdError(f"The field {generate_tag['field']} appears to be a {type(value).__name__}. This is not supported for cloudvision fields.")
            if value:
                tags.append(self._tag_dict(generate_tag["name"], value))
        if tags:
            return [{"interface": link["name"], "tags": tags}]
        return []
