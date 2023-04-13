from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.range_expand import range_expand
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get


class MlagMixin:
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to the SharedUtils class
    """

    default_interfaces: dict
    hostname: str
    hostvars: dict
    node_type_key_data: dict
    switch_data_combined: dict
    switch_data_node_group_nodes: list
    underlay_router: bool

    @cached_property
    def mlag(self) -> bool:
        return (
            get(self.node_type_key_data, "mlag_support", default=False) is True
            and get(self.switch_data_combined, "mlag", default=True) is True
            and len(self.switch_data_node_group_nodes) == 2
        )

    @cached_property
    def mlag_ibgp_origin_incomplete(self) -> bool:
        return get(self.switch_data_combined, "mlag_ibgp_origin_incomplete", default=True)

    @cached_property
    def mlag_peer_vlan(self) -> int:
        return get(self.switch_data_combined, "mlag_peer_vlan", default=4094)

    @cached_property
    def mlag_interfaces(self) -> list:
        return range_expand(default(get(self.switch_data_combined, "mlag_interfaces"), get(self.default_interfaces, "mlag_interfaces"), []))

    @cached_property
    def mlag_interfaces_speed(self) -> str | None:
        return get(self.switch_data_combined, "mlag_interfaces_speed")

    @cached_property
    def mlag_peer_ipv4_pool(self) -> str:
        return get(self.switch_data_combined, "mlag_peer_ipv4_pool", required=True)

    @cached_property
    def mlag_peer_l3_ipv4_pool(self) -> str:
        return get(self.switch_data_combined, "mlag_peer_l3_ipv4_pool", required=True)

    @cached_property
    def mlag_role(self) -> str | None:
        if self.mlag:
            if self.switch_data_node_group_nodes[0]["name"] == self.hostname:
                return "primary"
            elif self.switch_data_node_group_nodes[1]["name"] == self.hostname:
                return "secondary"
            raise AristaAvdError("Unable to detect MLAG role")
        return None

    @cached_property
    def mlag_peer(self) -> str:
        if self.mlag_role == "primary":
            return self.switch_data_node_group_nodes[1]["name"]
        if self.mlag_role == "secondary":
            return self.switch_data_node_group_nodes[0]["name"]
        raise AristaAvdError("Unable to find MLAG peer within same node group")

    @cached_property
    def mlag_l3(self) -> bool:
        return self.mlag is True and self.underlay_router is True

    @cached_property
    def mlag_peer_l3_vlan(self) -> int | None:
        if self.mlag_l3:
            mlag_peer_vlan = self.mlag_peer_vlan
            mlag_peer_l3_vlan = get(self.switch_data_combined, "mlag_peer_l3_vlan", default=4093)
            if mlag_peer_l3_vlan not in [None, False, mlag_peer_vlan]:
                return mlag_peer_l3_vlan
        return None

    @cached_property
    def mlag_peer_ip(self) -> str:
        return get(
            self.hostvars,
            f"avd_switch_facts..{self.mlag_peer}..switch..mlag_ip",
            required=True,
            org_key=f"avd_switch_facts.({self.mlag_peer}).switch.mlag_ip",
            separator="..",
        )

    @cached_property
    def mlag_peer_l3_ip(self) -> str | None:
        if self.mlag_peer_l3_vlan is not None:
            return get(
                self.hostvars,
                f"avd_switch_facts..{self.mlag_peer}..switch..mlag_l3_ip",
                required=True,
                org_key=f"avd_switch_facts.({self.mlag_peer}).switch.mlag_l3_ip",
                separator="..",
            )
        return None
