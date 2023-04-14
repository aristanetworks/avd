from __future__ import annotations

from functools import cached_property
from ipaddress import ip_interface
from re import findall
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.filter.range_expand import range_expand
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get

if TYPE_CHECKING:
    from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_facts import EosDesignsFacts


class MlagMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    """

    default_interfaces: dict
    hostname: str
    hostvars: dict
    id: int
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
        return self.get_mlag_peer_fact("mlag_ip")

    @cached_property
    def mlag_peer_l3_ip(self) -> str | None:
        if self.mlag_peer_l3_vlan is not None:
            return self.get_mlag_peer_fact("mlag_l3_ip")
        return None

    @cached_property
    def mlag_peer_id(self) -> int:
        return self.get_mlag_peer_fact("id")

    def get_mlag_peer_fact(self, key, required=True):
        return get(self.mlag_peer_facts, key, required=required, org_key=f"avd_switch_facts.({self.mlag_peer}).switch.{key}")

    @cached_property
    def mlag_peer_facts(self) -> EosDesignsFacts | dict:
        return get(
            self.hostvars,
            f"avd_switch_facts..{self.mlag_peer}..switch",
            required=True,
            org_key=f"avd_switch_facts.({self.mlag_peer}).switch",
            separator="..",
        )

    @cached_property
    def mlag_peer_mgmt_ip(self) -> str | None:
        if (mlag_peer_mgmt_ip := self.get_mlag_peer_fact("mgmt_ip", required=False)) is None:
            return None

        return str(ip_interface(mlag_peer_mgmt_ip).ip)

    @cached_property
    def mlag_ip(self) -> str | None:
        """
        Render ipv4 address for mlag_ip using dynamically loaded python module.
        """
        if self.mlag_role == "primary":
            return self.ip_addressing.mlag_ip_primary()
        elif self.mlag_role == "secondary":
            return self.ip_addressing.mlag_ip_secondary()

    @cached_property
    def mlag_l3_ip(self) -> str | None:
        """
        Render ipv4 address for mlag_l3_ip using dynamically loaded python module.
        """
        if self.mlag_role == "primary":
            return self.ip_addressing.mlag_l3_ip_primary()
        elif self.mlag_role == "secondary":
            return self.ip_addressing.mlag_l3_ip_secondary()

    @cached_property
    def mlag_switch_ids(self) -> dict | None:
        """
        Returns the switch id's of both primary and secondary switches for a given node group
        {"primary": int, "secondary": int}
        """
        if self.mlag_role == "primary":
            if self.id is None:
                raise AristaAvdMissingVariableError(f"'id' is not set on '{self.hostname}' and is required to compute MLAG ids")
            return {"primary": self.id, "secondary": self.mlag_peer_id}
        elif self.mlag_role == "secondary":
            if self.id is None:
                raise AristaAvdMissingVariableError(f"'id' is not set on '{self.hostname}' and is required to compute MLAG ids")
            return {"primary": self.mlag_peer_id, "secondary": self.id}

    @cached_property
    def mlag_port_channel_id(self) -> int:
        if not self.mlag_interfaces:
            raise AristaAvdMissingVariableError(f"'mlag_interfaces' not set on '{self.hostname}.")
        default_mlag_port_channel_id = "".join(findall(r"\d", self.mlag_interfaces[0]))
        return get(self.switch_data_combined, "mlag_port_channel_id", default_mlag_port_channel_id)

    @cached_property
    def mlag_peer_vlan_structured_config(self) -> dict | None:
        return get(self.switch_data_combined, "mlag_peer_vlan_structured_config")

    @cached_property
    def mlag_ibgp_ip(self) -> str:
        if self.mlag_l3_ip is not None:
            return self.mlag_l3_ip

        return self.mlag_ip

    @cached_property
    def mlag_peer_ibgp_ip(self) -> str:
        if self.mlag_peer_l3_ip is not None:
            return self.mlag_peer_l3_ip

        return self.mlag_peer_ip

    @cached_property
    def mlag_ibgp_peering_vrfs_base_vlan(self) -> int:
        return int(get(self.hostvars, "mlag_ibgp_peering_vrfs.base_vlan", required=True))
