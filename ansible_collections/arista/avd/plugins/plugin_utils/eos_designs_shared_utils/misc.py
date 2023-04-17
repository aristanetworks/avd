from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get

if TYPE_CHECKING:
    from .shared_utils import SharedUtils


class MiscMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using quoted type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def hostname(self: "SharedUtils") -> str:
        """
        hostname set based on inventory_hostname variable
        """
        return get(self.hostvars, "inventory_hostname", required=True)

    @cached_property
    def id(self: "SharedUtils") -> int | None:
        return get(self.switch_data_combined, "id")

    @cached_property
    def trunk_groups(self: "SharedUtils") -> dict:
        return {
            "mlag": {"name": get(self.hostvars, "trunk_groups.mlag.name", default="MLAG")},
            "mlag_l3": {"name": get(self.hostvars, "trunk_groups.mlag_l3.name", default="LEAF_PEER_L3")},
            "uplink": {"name": get(self.hostvars, "trunk_groups.uplink.name", default="UPLINK")},
        }

    @cached_property
    def enable_trunk_groups(self: "SharedUtils") -> bool:
        return get(self.hostvars, "enable_trunk_groups", default=False)

    @cached_property
    def filter_only_vlans_in_use(self: "SharedUtils") -> bool:
        return get(self.switch_data_combined, "filter.only_vlans_in_use", default=False)

    @cached_property
    def filter_tags(self: "SharedUtils") -> list:
        """
        Return filter.tags + group if defined
        """
        filter_tags = get(self.switch_data_combined, "filter.tags", default=["all"])
        if self.group is not None:
            filter_tags.append(self.group)
        return filter_tags

    @cached_property
    def filter_tenants(self: "SharedUtils") -> list:
        return get(self.switch_data_combined, "filter.tenants", default=["all"])

    @cached_property
    def igmp_snooping_enabled(self: "SharedUtils") -> bool:
        default_igmp_snooping_enabled = get(self.hostvars, "default_igmp_snooping_enabled")
        return get(self.switch_data_combined, "igmp_snooping_enabled", default=default_igmp_snooping_enabled) is True

    @cached_property
    def only_local_vlan_trunk_groups(self: "SharedUtils") -> bool:
        return self.enable_trunk_groups and get(self.hostvars, "only_local_vlan_trunk_groups", default=False)

    @cached_property
    def system_mac_address(self: "SharedUtils") -> str | None:
        """
        system_mac_address is inherited from
        Fabric Topology data model system_mac_address ->
            Host variable var system_mac_address ->
        """
        return default(get(self.switch_data_combined, "system_mac_address"), get(self.hostvars, "system_mac_address"))

    @cached_property
    def uplink_switches(self: "SharedUtils") -> list:
        return get(self.switch_data_combined, "uplink_switches", default=[])

    @cached_property
    def virtual_router_mac_address(self: "SharedUtils") -> str | None:
        return get(self.switch_data_combined, "virtual_router_mac_address")

    @cached_property
    def serial_number(self: "SharedUtils") -> str | None:
        """
        serial_number is inherited from
        Fabric Topology data model serial_number ->
            Host variable var serial_number
        """
        return default(get(self.switch_data_combined, "serial_number"), get(self.hostvars, "serial_number"))

    @cached_property
    def max_parallel_uplinks(self: "SharedUtils") -> int:
        """
        Exposed in avd_switch_facts
        """
        return get(self.switch_data_combined, "max_parallel_uplinks", default=1)

    @cached_property
    def max_uplink_switches(self: "SharedUtils") -> int:
        """
        max_uplink_switches will default to the length of uplink_switches
        """
        return get(self.switch_data_combined, "max_uplink_switches", default=len(self.uplink_switches))
