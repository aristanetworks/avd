from __future__ import annotations

from functools import cached_property
from ipaddress import ip_network

from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


class AvdStructuredConfig(AvdFacts):
    def __init__(self, hostvars, templar):
        super().__init__(hostvars, templar)

    @cached_property
    def _inband_management_role(self) -> str:
        if (inband_management_role := get(self._hostvars, "switch.inband_management_role")) is not None:
            return inband_management_role

        if self._inband_management_data:
            return "parent"

    @cached_property
    def _inband_management_vlan(self) -> int:
        return get(self._hostvars, "switch.inband_management_vlan", required=True)

    @cached_property
    def _inband_management_interface(self) -> str:
        return get(self._hostvars, "switch.inband_management_interface", required=True)

    @cached_property
    def _inband_management_ip(self) -> str:
        return get(self._hostvars, "switch.inband_management_ip", required=True)

    @cached_property
    def _p2p_uplinks_mtu(self) -> int:
        return get(self._hostvars, "p2p_uplinks_mtu", required=True)

    @cached_property
    def _inband_management_gateway(self) -> str:
        return get(self._hostvars, "switch.inband_management_gateway", required=True)

    @cached_property
    def _hostname(self) -> str:
        return get(self._hostvars, "switch.hostname", required=True)

    @cached_property
    def _mlag(self) -> bool:
        return get(self._hostvars, "switch.mlag") is True

    @cached_property
    def _mlag_role(self) -> str | None:
        return get(self._hostvars, "switch.mlag_role")

    @cached_property
    def vlans(self) -> dict | None:
        vlan_cfg = {
            "tenant": "system",
            "name": "L2LEAF_INBAND_MGMT",
        }

        if self._inband_management_role == "child":
            return {self._inband_management_vlan: vlan_cfg}

        if self._inband_management_role == "parent":
            return {vlan: vlan_cfg for vlan in self._inband_management_data["vlans"]}

        return None

    @cached_property
    def management_interfaces(self) -> dict | None:
        if self._inband_management_role != "child":
            return None

        return {
            self._inband_management_interface: {
                "description": "L2LEAF_INBAND_MGMT",
                "shutdown": False,
                "mtu": self._p2p_uplinks_mtu,
                "ip_address": self._inband_management_ip,
                "gateway": self._inband_management_gateway,
                "type": "inband",
            }
        }

    @cached_property
    def static_routes(self) -> dict | None:
        if self._inband_management_role != "child":
            return None

        return [
            {
                "destination_address_prefix": "0.0.0.0/0",
                "gateway": self._inband_management_gateway,
            }
        ]

    @cached_property
    def _inband_management_data(self) -> dict:
        vlans = []
        subnets = []
        peers = get(self._hostvars, f"avd_topology_peers..{self._hostname}", separator="..", default=[])
        avd_switch_facts = get(self._hostvars, "avd_switch_facts", required=True)
        for peer in peers:
            if self._hostname not in get(avd_switch_facts, f"{peer}..switch..inband_management_parents", separator="..", default=[]):
                continue

            if (subnet := get(avd_switch_facts, f"{peer}..switch..inband_management_subnet", separator="..", required=True)) in subnets:
                continue

            subnets.append(subnet)
            vlans.append(get(avd_switch_facts, f"{peer}..switch..inband_management_vlan", separator="..", required=True))

        if not subnets:
            return {}

        return {
            "vlans": vlans,
            "subnets": subnets,
        }

    @cached_property
    def vlan_interfaces(self) -> dict | None:
        if self._inband_management_role != "parent":
            return None

        if not self._inband_management_data["subnets"]:
            return None

        vlan_interfaces = {}
        for index, subnet in enumerate(self._inband_management_data["subnets"]):
            vlan = self._inband_management_data["vlans"][index]
            vlan_interface_name = f"Vlan{vlan}"
            vlan_interfaces[vlan_interface_name] = self._get_svi_cfg(subnet)

        return vlan_interfaces

    def _get_svi_cfg(self, subnet) -> dict:
        subnet = ip_network(subnet, strict=False)
        hosts = list(subnet.hosts())
        prefix = str(subnet.prefixlen)

        if self._mlag and self._mlag_role == "secondary":
            ip_address = f"{str(hosts[2])}/{prefix}"
        else:
            ip_address = f"{str(hosts[1])}/{prefix}"

        return {
            "description": "L2LEAF_INBAND_MGMT",
            "shutdown": False,
            "mtu": self._p2p_uplinks_mtu,
            "ip_address": ip_address,
            "ip_virtual_router_addresses": [str(hosts[0])],
            "ip_attached_host_route_export": {
                "distance": 19,
            },
        }

    @cached_property
    def ip_virtual_router_mac_address(self) -> str | None:
        if self._inband_management_role != "parent":
            return None

        return str(get(self._hostvars, "switch.virtual_router_mac_address", required=True)).lower()

    @cached_property
    def _underlay_bgp(self) -> bool:
        return get(self._hostvars, "switch.underlay.bgp") is True

    @cached_property
    def router_bgp(self) -> dict | None:
        if self._inband_management_role != "parent":
            return None

        if not self._underlay_bgp:
            return None

        return {
            "redistribute_routes": {
                "attached-host": {},
            }
        }

    @cached_property
    def prefix_lists(self) -> dict | None:
        if self._inband_management_role != "parent":
            return None

        if not self._underlay_bgp:
            return None

        sequence_numbers = {
            ((index + 1) * 10): {
                "action": f"permit {subnet}",
            }
            for index, subnet in enumerate(self._inband_management_data["subnets"])
        }
        return {
            "PL-L2LEAF-INBAND-MGMT": {
                "sequence_numbers": sequence_numbers,
            }
        }

    @cached_property
    def route_maps(self) -> dict | None:
        if self._inband_management_role != "parent":
            return None

        if not self._underlay_bgp:
            return None

        return {
            "RM-CONN-2-BGP": {
                "sequence_numbers": {
                    # sequence 10 is set in underlay so avoid setting it here
                    20: {
                        "type": "permit",
                        "match": ["ip address prefix-list PL-L2LEAF-INBAND-MGMT"],
                    }
                },
            }
        }
