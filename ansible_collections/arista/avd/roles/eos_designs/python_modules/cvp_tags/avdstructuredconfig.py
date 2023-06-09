from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible.utils.display import Display

from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get
from ansible_collections.arista.avd.roles.eos_designs.python_modules.underlay.utils import UtilsMixin

if TYPE_CHECKING:
    from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils import SharedUtils

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


class AvdStructuredConfigTags(AvdFacts, UtilsMixin):
    """
    This would return facts to ansible set at the rool-level of the host vars for the host calling this:
    {
        "cvp_tags": {
            "topology_hint_type": <topology_hint_type taken from node_type_keys.[].cvp_tags.topology_hint_type>,
        },
        "key2": "bar"
    }

    Missing fabric_name from shared_utils
    """

    def __init__(self, hostvars: dict, shared_utils: SharedUtils):
        # Init a display object in order to later issue warnings
        self.ansible_display = Display()
        super().__init__(hostvars=hostvars, shared_utils=shared_utils)

    @cached_property
    def cloudvision_tags(self) -> str:
        """
        Insert all the logic to deduct cvp tags here.
        User helper functions to larger code blocks
        Helper functions should be regular methods on the class (start with underscore)
        and if you need @cached_properties make sure to start the name with underscore.
        """
        # interface_peer_name = self._interface_peer_name
        device_tags = []

        hints = [self._topology_hint_dc, self._topology_hint_fabric, self._topology_hint_pod, self._topology_hint_type, self._topology_hint_rack]
        for hint in hints:
            if hint:
                device_tags.append(hint)

        for custom_tag in get(self.shared_utils.hostvars, "cloudvision_tags_device_custom", []):
            if custom_tag["label"].lower() not in INVALID_CUSTOM_DEVICE_TAGS:
                device_tags.append(custom_tag)
            else:
                raise AristaAvdError(f"{custom_tag['label']} is Invalid. System Tags cannot be overriden")

        for generate_tag in get(self.shared_utils.hostvars, "cloudvision_tags_device_generate", []):
            value = get(self.shared_utils.hostvars, generate_tag["field"])
            if generate_tag["label"] in INVALID_CUSTOM_DEVICE_TAGS:
                raise AristaAvdError(f"{generate_tag['label']} is Invalid. System Tags cannot be overriden")
            if type(value) in [list, dict]:
                raise AristaAvdError(f"The field {generate_tag['field']} appears to be a {type(value).__name__}. This is not supported for cloudvision fields.")
            if value:
                device_tags.append({"label": generate_tag["label"], "value": str(value)})
            else:
                self.ansible_display.warning(msg=f"{generate_tag['field']} not found for {self.shared_utils.hostname}")

        interface_tags = []
        for link in get(self.shared_utils.hostvars, "ethernet_interfaces", []):
            generated_interface_tags = self._interface_tags(link)
            if generated_interface_tags:
                interface_tags.append(generated_interface_tags)

        result = {"device_tags": device_tags}
        if interface_tags:
            result["interface_tags"] = interface_tags

        return result

    @staticmethod
    def tag_dict(name, value):
        return {"label": name, "value": value}

    @cached_property
    def _topology_hint_type(self) -> dict:
        """
        Retrun the topology hint type for the device.
        """
        hint_type = get(self.shared_utils.node_type_key_data, "cloudvision_tags_topology_type")

        hint_type = get(self.shared_utils.hostvars, "cloudvision_tags_topology_type", hint_type)

        if not hint_type:
            # raise AristaAvdError(f"No topology hint type found for {self.shared_utils.hostname}")
            self.ansible_display.warning(msg=f"No topology hint type found for {self.shared_utils.hostname}")
            return None

        return self.tag_dict("topology_hint_type", hint_type)

    @cached_property
    def _topology_hint_fabric(self) -> dict:
        """
        Return the topology fabric hint tag.
        """
        if not self.shared_utils.fabric_name:
            # raise AristaAvdError(f"'pod_name' not found for {self.shared_utils.hostname}")
            self.ansible_display.warning(msg=f"'fabric_name' not found for {self.shared_utils.hostname}")
            return None

        return self.tag_dict("topology_hint_fabric", self.shared_utils.fabric_name)

    @cached_property
    def _topology_hint_pod(self) -> dict:
        """
        Return the topology fabric hint tag.
        """
        if not self.shared_utils.pod_name:
            # raise AristaAvdError(f"'pod_name' not found for {self.shared_utils.hostname}")
            self.ansible_display.warning(msg=f"'pod_name' not found for {self.shared_utils.hostname}")
            return None

        return self.tag_dict("topology_hint_pod", self.shared_utils.pod_name)

    @cached_property
    def _topology_hint_dc(self) -> dict:
        """
        Return the topology fabric hint tag.
        """
        if not self.shared_utils.dc_name:
            # raise AristaAvdError(f"'dc_name' not found for {self.shared_utils.hostname}")
            self.ansible_display.warning(msg=f"'dc_name' not found for {self.shared_utils.hostname}")
            return None
        return self.tag_dict("topology_hint_datacenter", self.shared_utils.dc_name)

    @cached_property
    def _topology_hint_rack(self) -> dict | None:
        """
        Return the topology hint for the rack tag.
        """
        if not self.shared_utils.rack:
            self.ansible_display.warning(msg=f"'rack' information not found for {self.shared_utils.hostname} ")
            return None
        return self.tag_dict("topology_hint_rack", self.shared_utils.rack)

    def _interface_tags(self, link) -> dict | None:
        tags = []

        for generate_tag in get(self.shared_utils.hostvars, "cloudvision_tags_interface_generate", []):
            value = get(link, generate_tag["field"])
            if generate_tag["label"] in INVALID_CUSTOM_DEVICE_TAGS:
                raise AristaAvdError(f"{generate_tag['label']} is Invalid. System Tags cannot be overriden")
            if type(value) in [list, dict]:
                raise AristaAvdError(f"The field {generate_tag['field']} appears to be a {type(value).__name__}. This is not supported for cloudvision fields.")
            if value:
                tags.append({"label": generate_tag["label"], "value": str(value)})
            else:
                self.ansible_display.warning(msg=f"{generate_tag['field']} not found for {self.shared_utils.hostname}")
        if tags:
            return {"interface": link["name"], "tags": tags}
        self.ansible_display.warning(msg=f"No tags for {link['name']}")
        return None
