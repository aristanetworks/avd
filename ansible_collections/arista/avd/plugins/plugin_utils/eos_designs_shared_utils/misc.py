from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get


class MiscMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    """

    any_network_services: bool
    hostvars: dict
    mlag: bool
    platform_settings: dict
    switch_data_combined: dict
    switch_data: dict
    underlay_ipv6: bool
    vtep: bool

    @cached_property
    def hostname(self) -> str:
        """
        hostname set based on inventory_hostname variable
        """
        return get(self.hostvars, "inventory_hostname", required=True)

    @cached_property
    def id(self) -> int | None:
        return get(self.switch_data_combined, "id")

    @cached_property
    def trunk_groups(self) -> dict:
        return {
            "mlag": {"name": get(self.hostvars, "trunk_groups.mlag.name", default="MLAG")},
            "mlag_l3": {"name": get(self.hostvars, "trunk_groups.mlag_l3.name", default="LEAF_PEER_L3")},
            "uplink": {"name": get(self.hostvars, "trunk_groups.uplink.name", default="UPLINK")},
        }

    @cached_property
    def enable_trunk_groups(self) -> bool:
        return get(self.hostvars, "enable_trunk_groups", default=False)

    @cached_property
    def filter_only_vlans_in_use(self) -> bool:
        return get(self.switch_data_combined, "filter.only_vlans_in_use", default=False)

    @cached_property
    def filter_tags(self) -> list:
        """
        Return filter.tags + group if defined
        """
        filter_tags = get(self.switch_data_combined, "filter.tags", default=["all"])
        if self.group is not None:
            filter_tags.append(self.group)
        return filter_tags

    @cached_property
    def filter_tenants(self) -> list:
        return get(self.switch_data_combined, "filter.tenants", default=["all"])

    @cached_property
    def group(self) -> str | None:
        """
        group set to "node_group" name or None
        """
        return get(self.switch_data, "group")

    @cached_property
    def igmp_snooping_enabled(self) -> bool:
        default_igmp_snooping_enabled = get(self.hostvars, "default_igmp_snooping_enabled")
        return get(self.switch_data_combined, "igmp_snooping_enabled", default=default_igmp_snooping_enabled) is True

    @cached_property
    def loopback_ipv4_offset(self) -> int:
        return get(self.switch_data_combined, "loopback_ipv4_offset", default=0)

    @cached_property
    def loopback_ipv6_offset(self) -> int:
        return get(self.switch_data_combined, "loopback_ipv6_offset", default=0)

    @cached_property
    def loopback_ipv6_pool(self):
        return get(self.switch_data_combined, "loopback_ipv6_pool", required=True)

    @cached_property
    def mgmt_interface(self) -> str | None:
        """
        mgmt_interface is inherited from
        Global var mgmt_interface ->
          Platform Settings management_interface ->
            Fabric Topology data model mgmt_interface
        """
        return default(
            get(self.switch_data_combined, "mgmt_interface"),
            self.platform_settings.get("management_interface"),
            get(self.hostvars, "mgmt_interface"),
        )

    @cached_property
    def only_local_vlan_trunk_groups(self) -> bool:
        return self.enable_trunk_groups and get(self.hostvars, "only_local_vlan_trunk_groups", default=False)

    @cached_property
    def system_mac_address(self) -> str | None:
        """
        system_mac_address is inherited from
        Fabric Topology data model system_mac_address ->
            Host variable var system_mac_address ->
        """
        return default(get(self.switch_data_combined, "system_mac_address"), get(self.hostvars, "system_mac_address"))

    @cached_property
    def uplink_switches(self) -> list:
        return get(self.switch_data_combined, "uplink_switches", default=[])

    @cached_property
    def virtual_router_mac_address(self) -> str | None:
        return get(self.switch_data_combined, "virtual_router_mac_address")

    @cached_property
    def vtep_loopback(self) -> str:
        return get(self.switch_data_combined, "vtep_loopback", default="Loopback1")

    @cached_property
    def vtep_ip(self) -> str | None:
        """
        Render ipv4 address for vtep_ip using dynamically loaded python module.
        """
        if self.mlag is True:
            return self.ip_addressing.vtep_ip_mlag()

        else:
            return self.ip_addressing.vtep_ip()

    @cached_property
    def vtep_vvtep_ip(self) -> str | None:
        return get(self.hostvars, "vtep_vvtep_ip")
