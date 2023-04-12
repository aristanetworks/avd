from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.plugin_utils.errors.errors import AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.merge import merge
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


def get_interface_descriptions_templates(hostvars) -> dict:
    """
    Return dict with interface_descriptions templates set based on
    templates.interface_descriptions.* combined with (overridden by)
    node_type_keys.<node_type_key>.interface_descriptions.*
    """
    node_type_key_data = get_node_type_key_data(hostvars)

    hostvar_templates = get(hostvars, "templates.interface_descriptions", default={})
    node_type_templates = get(node_type_key_data, "interface_descriptions", default={})
    if hostvar_templates or node_type_templates:
        return merge(hostvar_templates, node_type_templates, list_merge="replace", destructive_merge=False)
    else:
        return {}


def get_node_type_key_data(hostvars) -> dict:
    """
    internal _node_type_key_data containing settings for this node_type.
    """
    node_type = get(hostvars, "switch.type", required=True)

    node_type_keys = get(hostvars, "node_type_keys", required=True)
    node_type_keys = convert_dicts(node_type_keys, "key")
    for node_type_key in node_type_keys:
        if node_type_key["type"] == node_type:
            return node_type_key

    # Not found
    raise AristaAvdMissingVariableError(f"node_type_keys.<>.type=={node_type}")


class UtilsMixin:
    """
    Mixin Class with internal functions.
    Class should only be used as Mixin to an AvdInterfaceDescriptions class
    """

    _hostvars: dict

    @cached_property
    def _interface_descriptions_templates(self) -> dict:
        return get_interface_descriptions_templates(self._hostvars)

    @cached_property
    def _default_mpls_overlay_role(self) -> str:
        return get(self._hostvars, "switch.default_mpls_overlay_role")

    @cached_property
    def _mpls_lsr(self) -> str:
        return get(self._hostvars, "switch.mpls_lsr")

    @cached_property
    def _mlag_peer(self) -> str:
        return get(self._hostvars, "switch.mlag_peer", required=True)

    @cached_property
    def _mlag_port_channel_id(self) -> str:
        return get(self._hostvars, "switch.mlag_port_channel_id", required=True)
