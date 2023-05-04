from __future__ import annotations

from functools import cached_property
from ipaddress import ip_network

from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.plugins.plugin_utils.errors.errors import AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


class AvdStructuredConfig(AvdFacts):
    @cached_property
    def vlans(self) -> dict | None:
        vlan_cfg = {
            "tenant": "system",
            "name": "L2LEAF_INBAND_MGMT",
        }

        if self.shared_utils.inband_management_vlan is not None:
            return {self.shared_utils.inband_management_vlan: vlan_cfg}

        if self._inband_management_parent_data.get("subnets"):
            return {vlan: vlan_cfg for vlan in self._inband_management_parent_data["vlans"]}

        return None

    @cached_property
    def management_interfaces(self) -> list | None:
        if self.shared_utils.inband_management_vlan is None:
            return None

        return [
            {
                "name": self.shared_utils.inband_management_interface,
                "description": "L2LEAF_INBAND_MGMT",
                "shutdown": False,
                "mtu": self.shared_utils.p2p_uplinks_mtu,
                "ip_address": self.shared_utils.inband_management_ip,
                "gateway": self.shared_utils.inband_management_gateway,
                "type": "inband",
            }
        ]

    @cached_property
    def static_routes(self) -> list | None:
        if self.shared_utils.inband_management_vlan is None:
            return None

        return [
            {
                "destination_address_prefix": "0.0.0.0/0",
                "gateway": self.shared_utils.inband_management_gateway,
            }
        ]

    @cached_property
    def _inband_management_parent_data(self) -> dict:
        vlans = []
        subnets = []
        peers = get(self._hostvars, f"avd_topology_peers..{self.shared_utils.hostname}", separator="..", default=[])
        for peer in peers:
            peer_facts = self.shared_utils.get_peer_facts(peer, required=True)
            if (vlan := peer_facts.get("inband_management_vlan")) is None:
                continue

            if (subnet := peer_facts.get("inband_management_subnet")) in subnets:
                continue

            subnets.append(subnet)
            vlans.append(vlan)

        if not subnets:
            return {}

        return {
            "vlans": vlans,
            "subnets": subnets,
        }

    @cached_property
    def vlan_interfaces(self) -> list | None:
        if not self._inband_management_parent_data.get("subnets"):
            return None

        if not self.shared_utils.underlay_router:
            return None

        vlan_interfaces = []
        for index, subnet in enumerate(self._inband_management_parent_data["subnets"]):
            vlan = self._inband_management_parent_data["vlans"][index]

            vlan_interfaces.append(self._get_svi_cfg(vlan, subnet))

        return vlan_interfaces

    def _get_svi_cfg(self, vlan, subnet) -> dict:
        subnet = ip_network(subnet, strict=False)
        hosts = list(subnet.hosts())
        prefix = str(subnet.prefixlen)

        if self.shared_utils.mlag_role == "secondary":
            ip_address = f"{str(hosts[2])}/{prefix}"
        else:
            ip_address = f"{str(hosts[1])}/{prefix}"

        return {
            "name": f"Vlan{vlan}",
            "description": "L2LEAF_INBAND_MGMT",
            "shutdown": False,
            "mtu": self.shared_utils.p2p_uplinks_mtu,
            "ip_address": ip_address,
            "ip_virtual_router_addresses": [str(hosts[0])],
            "ip_attached_host_route_export": {
                "enabled": True,
                "distance": 19,
            },
        }

    @cached_property
    def ip_virtual_router_mac_address(self) -> str | None:
        if not self._inband_management_parent_data.get("subnets"):
            return None

        if not self.shared_utils.underlay_router:
            return None

        if self.shared_utils.virtual_router_mac_address is None:
            raise AristaAvdMissingVariableError("'virtual_router_mac_address' must be set for inband management parent.")
        return str(self.shared_utils.virtual_router_mac_address).lower()

    @cached_property
    def router_bgp(self) -> dict | None:
        if not self._inband_management_parent_data.get("subnets"):
            return None

        if not self.shared_utils.underlay_bgp:
            return None

        return {
            "redistribute_routes": {
                "attached-host": {},
            }
        }

    @cached_property
    def prefix_lists(self) -> list | None:
        if not self._inband_management_parent_data.get("subnets"):
            return None

        if not self.shared_utils.underlay_bgp:
            return None

        if not self.shared_utils.underlay_filter_redistribute_connected:
            return None

        sequence_numbers = [
            {
                "sequence": ((index + 1) * 10),
                "action": f"permit {subnet}",
            }
            for index, subnet in enumerate(self._inband_management_parent_data["subnets"])
        ]
        return [
            {
                "name": "PL-L2LEAF-INBAND-MGMT",
                "sequence_numbers": sequence_numbers,
            }
        ]

    @cached_property
    def route_maps(self) -> dict | None:
        if not self._inband_management_parent_data.get("subnets"):
            return None

        if not self.shared_utils.underlay_bgp:
            return None

        if not self.shared_utils.underlay_filter_redistribute_connected:
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
