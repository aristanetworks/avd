# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from ipaddress import ip_network

from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.plugins.plugin_utils.errors.errors import AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


class AvdStructuredConfigInbandManagement(AvdFacts):
    @cached_property
    def vlans(self) -> list | None:
        if not self._inband_management_parent_vlans and not (self.shared_utils.configure_inband_mgmt or self.shared_utils.configure_inband_mgmt_ipv6):
            return None

        vlan_cfg = {
            "tenant": "system",
            "name": self.shared_utils.inband_mgmt_vlan_name,
        }

        if self.shared_utils.configure_inband_mgmt or self.shared_utils.configure_inband_mgmt_ipv6:
            return [{"id": self.shared_utils.inband_mgmt_vlan, **vlan_cfg}]

        if self._inband_management_parent_vlans:
            return [{"id": svi, **vlan_cfg} for svi in self._inband_management_parent_vlans]

        return None

    @cached_property
    def vlan_interfaces(self) -> list | None:
        """
        VLAN interfaces can be our own management interface and/or SVIs created on behalf of child switches using us as uplink_switch.
        """
        if not self._inband_management_parent_vlans and not (self.shared_utils.configure_inband_mgmt or self.shared_utils.configure_inband_mgmt_ipv6):
            return None

        if self.shared_utils.configure_inband_mgmt or self.shared_utils.configure_inband_mgmt_ipv6:
            return [self.get_local_inband_mgmt_interface_cfg()]

        if self._inband_management_parent_vlans:
            return [self.get_parent_svi_cfg(vlan, subnet["ipv4"], subnet["ipv6"]) for vlan, subnet in self._inband_management_parent_vlans.items()]

    @cached_property
    def static_routes(self) -> list | None:
        if not self.shared_utils.configure_inband_mgmt or self.shared_utils.inband_mgmt_gateway is None:
            return None

        return [
            strip_empties_from_dict(
                {
                    "destination_address_prefix": "0.0.0.0/0",
                    "gateway": self.shared_utils.inband_mgmt_gateway,
                    "vrf": self.shared_utils.inband_mgmt_vrf,
                }
            )
        ]

    @cached_property
    def ipv6_static_routes(self) -> list | None:
        if not self.shared_utils.configure_inband_mgmt_ipv6 or self.shared_utils.inband_mgmt_ipv6_gateway is None:
            return None

        return [
            strip_empties_from_dict(
                {
                    "destination_address_prefix": "::/0",
                    "gateway": self.shared_utils.inband_mgmt_ipv6_gateway,
                    "vrf": self.shared_utils.inband_mgmt_vrf,
                }
            )
        ]

    @cached_property
    def vrfs(self) -> list | None:
        if self.shared_utils.inband_mgmt_vrf is None:
            return None

        if not self._inband_management_parent_vlans and not self.shared_utils.configure_inband_mgmt:
            return None

        return [{"name": self.shared_utils.inband_mgmt_vrf}]

    @cached_property
    def ip_virtual_router_mac_address(self) -> str | None:
        if not self._inband_management_parent_vlans:
            return None

        if self.shared_utils.virtual_router_mac_address is None:
            raise AristaAvdMissingVariableError("'virtual_router_mac_address' must be set for inband management parent.")
        return str(self.shared_utils.virtual_router_mac_address).lower()

    @cached_property
    def router_bgp(self) -> dict | None:
        if not self._inband_management_parent_vlans:
            return None

        if self.shared_utils.inband_mgmt_vrf is not None:
            return None

        if not self.shared_utils.underlay_bgp:
            return None

        return {"redistribute_routes": [{"source_protocol": "attached-host"}]}

    @cached_property
    def prefix_lists(self) -> list | None:
        if not self._inband_management_parent_vlans:
            return None

        if self.shared_utils.inband_mgmt_vrf is not None:
            return None

        if not self.shared_utils.underlay_bgp:
            return None

        if not self.shared_utils.underlay_filter_redistribute_connected:
            return None

        sequence_numbers = [
            {
                "sequence": (index + 1) * 10,
                "action": f"permit {subnet['ipv4']}",
            }
            for index, subnet in enumerate(self._inband_management_parent_vlans.values())
        ]
        return [
            {
                "name": "PL-L2LEAF-INBAND-MGMT",
                "sequence_numbers": sequence_numbers,
            }
        ]

    @cached_property
    def ipv6_prefix_lists(self) -> list | None:
        if not self._inband_management_parent_vlans:
            return None

        if self.shared_utils.inband_mgmt_vrf is not None:
            return None

        if not self.shared_utils.underlay_bgp:
            return None

        if not self.shared_utils.underlay_filter_redistribute_connected:
            return None

        if not self.shared_utils.configure_inband_mgmt_ipv6:
            return None

        sequence_numbers = [
            {
                "sequence": (index + 1) * 10,
                "action": f"permit {subnet['ipv6']}",
            }
            for index, subnet in enumerate(self._inband_management_parent_vlans.values())
        ]
        return [
            {
                "name": "IPv6-PL-L2LEAF-INBAND-MGMT",
                "sequence_numbers": sequence_numbers,
            }
        ]

    @cached_property
    def route_maps(self) -> list | None:
        if not self._inband_management_parent_vlans:
            return None

        if self.shared_utils.inband_mgmt_vrf is not None:
            return None

        if not self.shared_utils.underlay_bgp:
            return None

        if not self.shared_utils.underlay_filter_redistribute_connected:
            return None

        route_map = {
                "name": "RM-CONN-2-BGP",
                "sequence_numbers": [
                    {
                        # sequence 10 is set in underlay so avoid setting it here
                        "sequence": 20,
                        "type": "permit",
                        "match": ["ip address prefix-list PL-L2LEAF-INBAND-MGMT"],
                    }
                ],
            }

        if self.shared_utils.configure_inband_mgmt_ipv6:
            route_map["sequence_numbers"].append({"sequence": 30, "type": "permit", "match": ["ipv6 address prefix-list IPv6-PL-L2LEAF-INBAND-MGMT"]})

        return [route_map]

    @cached_property
    def _inband_management_parent_vlans(self) -> dict:
        if not self.shared_utils.underlay_router:
            return {}

        svis = {}
        subnets = []
        peers = natural_sort(get(self._hostvars, f"avd_topology_peers..{self.shared_utils.hostname}", separator="..", default=[]))
        for peer in peers:
            peer_facts = self.shared_utils.get_peer_facts(peer, required=True)
            if (vlan := peer_facts.get("inband_mgmt_vlan")) is None:
                continue

            subnet = {"ipv4": peer_facts.get("inband_mgmt_subnet"), "ipv6": peer_facts.get("inband_mgmt_ipv6_subnet")}
            if subnet in subnets:
                continue

            subnets.append(subnet)
            svis[vlan] = subnet

        return svis

    def get_local_inband_mgmt_interface_cfg(self) -> dict:
        return strip_empties_from_dict(
            {
                "name": self.shared_utils.inband_mgmt_interface,
                "description": self.shared_utils.inband_mgmt_description,
                "shutdown": False,
                "mtu": self.shared_utils.inband_mgmt_mtu,
                "vrf": self.shared_utils.inband_mgmt_vrf,
                "ip_address": self.shared_utils.inband_mgmt_ip,
                "ipv6_enable": None if not self.shared_utils.configure_inband_mgmt_ipv6 else True,
                "ipv6_address": self.shared_utils.inband_mgmt_ipv6_address,
                "type": "inband_mgmt",
            }
        )

    def get_parent_svi_cfg(self, vlan: int, subnet: str, ipv6_subnet: str) -> dict:
        network = False
        v6_network = False
        ip_address = None
        gateway = None
        ipv6_address = None
        v6_gateway = None

        if subnet is not None:
            network = ip_network(subnet, strict=False)

        if ipv6_subnet is not None:
            v6_network = ip_network(ipv6_subnet, strict=False)

        if self.shared_utils.mlag_role == "secondary":
            if network:
                ip = str(network[3])
            if v6_network:
                ipv6 = str(v6_network[3])
        else:
            if network:
                ip = str(network[2])
            if v6_network:
                ipv6 = str(v6_network[2])

        if network:
            ip_address = f"{ip}/{network.prefixlen}"
            gateway = str(network[1])

        if v6_network:
            ipv6_address = f"{ipv6}/{v6_network.prefixlen}"
            v6_gateway = str(v6_network[1])

        return strip_empties_from_dict(
            {
                "name": f"Vlan{vlan}",
                "description": self.shared_utils.inband_mgmt_description,
                "shutdown": False,
                "mtu": self.shared_utils.inband_mgmt_mtu,
                "vrf": self.shared_utils.inband_mgmt_vrf,
                "ip_address": ip_address,
                "ip_virtual_router_addresses": [gateway],
                "ipv6_enable": None if not self.shared_utils.configure_inband_mgmt_ipv6 else True,
                "ipv6_address": ipv6_address,
                "ipv6_virtual_router_addresses": [v6_gateway],
                "ip_attached_host_route_export": {
                    "enabled": True,
                    "distance": 19,
                },
            }
        )
