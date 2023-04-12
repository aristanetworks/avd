from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.plugin_utils.errors.errors import AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.merge import merge
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


def get_ip_addressing_templates(hostvars) -> dict:
    """
    Return dict with ip_addressing templates set based on
    templates.ip_addressing.* combined with (overridden by)
    node_type_keys.<node_type_key>.ip_addressing.*
    """
    node_type_key_data = get_node_type_key_data(hostvars)

    hostvar_templates = get(hostvars, "templates.ip_addressing", default={})
    node_type_templates = get(node_type_key_data, "ip_addressing", default={})
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
    Class should only be used as Mixin to an AvdIpAddressing class
    """

    _hostvars: dict

    @cached_property
    def _ip_addressing_templates(self) -> dict:
        return get_ip_addressing_templates(self._hostvars)

    @cached_property
    def _mlag_primary_id(self) -> int:
        return int(get(self._hostvars, "switch.mlag_switch_ids.primary", required=True))

    @cached_property
    def _mlag_secondary_id(self) -> int:
        return int(get(self._hostvars, "switch.mlag_switch_ids.secondary", required=True))

    @cached_property
    def _mlag_peer_ipv4_pool(self) -> str:
        return get(self._hostvars, "switch.mlag_peer_ipv4_pool", required=True)

    @cached_property
    def _mlag_peer_l3_ipv4_pool(self) -> str:
        return get(self._hostvars, "switch.mlag_peer_l3_ipv4_pool", required=True)

    @cached_property
    def _uplink_ipv4_pool(self) -> str:
        return get(self._hostvars, "switch.uplink_ipv4_pool", required=True)

    @cached_property
    def _id(self) -> int:
        return int(get(self._hostvars, "switch.id", required=True))

    @cached_property
    def _max_uplink_switches(self) -> int:
        return int(get(self._hostvars, "switch.max_uplink_switches", required=True))

    @cached_property
    def _max_parallel_uplinks(self) -> int:
        return int(get(self._hostvars, "switch.max_parallel_uplinks", required=True))

    @cached_property
    def _loopback_ipv4_pool(self) -> str:
        return get(self._hostvars, "switch.loopback_ipv4_pool", required=True)

    @cached_property
    def _loopback_ipv4_offset(self) -> int:
        return get(self._hostvars, "switch.loopback_ipv4_offset", required=True)

    @cached_property
    def _loopback_ipv6_pool(self) -> str:
        return get(self._hostvars, "switch.loopback_ipv6_pool", required=True)

    @cached_property
    def _loopback_ipv6_offset(self) -> int:
        return get(self._hostvars, "switch.loopback_ipv6_offset", required=True)

    @cached_property
    def _vtep_loopback_ipv4_pool(self) -> str:
        return get(self._hostvars, "switch.vtep_loopback_ipv4_pool", required=True)
