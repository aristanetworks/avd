# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Generate synthetic AVD inventory for large fabric benchmarking."""

from random import Random
from typing import Any

FABRIC_VARS = {"fabric_name": "FABRIC"}
NETWORK_PORTS = {
    "port_profiles": [
        {
            "profile": "user",
            "vlans": 100,
            "mode": "access",
            "description": "User port",
        },
        {
            "profile": "phone",
            "mode": "trunk phone",
            "native_vlan": 200,
            "description": "Phone port",
        },
    ],
    "network_ports": [
        {
            "switches": ["l[23]leaf.+"],
            "switch_ports": ["Ethernet1-24"],
            "profile": "user",
        },
        {
            "switches": ["l[23]leaf.+"],
            "switch_ports": ["Ethernet25-48"],
            "profile": "phone",
        },
    ],
}


def generate_hostvars(
    spine_count: int,
    l3leaf_count: int,
    l2leaf_count: int,
    vrf_count: int,
    per_vrf_svi_count: int,
) -> dict[str, dict[str, Any]]:
    """
    Generate synthetic hostvars for benchmarking.

    Args:
        spine_count: Number of spine switches
        l3leaf_count: Number of L3 leaf switches
        l2leaf_count: Number of L2 leaf switches
        vrf_count: Number of VRFs per tenant
        per_vrf_svi_count: Number of SVIs per VRF

    Returns:
        Dictionary of hostvars keyed by hostname
    """
    if l3leaf_count < 2 or l3leaf_count % 2:
        msg = "l3leaf_count must be a positive even number to form MLAG pairs"
        raise ValueError(msg)

    hostvars: dict[str, Any] = {}
    network_services = generate_network_services(vrf_count, per_vrf_svi_count)
    spines: list[str] = []
    l3leafs: list[str] = []
    for number in range(1, spine_count + 1):
        name = f"spine{number}"
        spines.append(name)
        host_hostvars: dict[str, Any] = {"inventory_hostname": name}
        host_hostvars.update(FABRIC_VARS)
        host_hostvars.update(generate_spine_var(name, number))
        hostvars[name] = host_hostvars

    for number in range(1, l3leaf_count + 1):
        name = f"l3leaf{number}"
        l3leafs.append(name)
        host_hostvars: dict[str, Any] = {"inventory_hostname": name}
        host_hostvars.update(FABRIC_VARS)
        host_hostvars.update(NETWORK_PORTS)
        host_hostvars.update(network_services)
        host_hostvars.update(generate_l3leaf_var(number, spines))
        hostvars[name] = host_hostvars

    for number in range(1, l2leaf_count + 1):
        name = f"l2leaf{number}"
        host_hostvars: dict[str, Any] = {"inventory_hostname": name}
        host_hostvars.update(FABRIC_VARS)
        host_hostvars.update(NETWORK_PORTS)
        host_hostvars.update(network_services)
        host_hostvars.update(generate_l2leaf_var(number, l3leafs))
        hostvars[name] = host_hostvars

    return hostvars


def generate_network_services(vrf_count: int, per_vrf_svi_count: int) -> dict:
    """Generate network services configuration."""
    return {
        "tenants": [
            {
                "name": "TENANT1",
                "mac_vrf_vni_base": 10000,
                "vrfs": [
                    {
                        "name": f"VRF{vrf_id}",
                        "vrf_id": vrf_id,
                        "svis": [
                            {
                                "id": vrf_id * 100 + svi_id,
                                "name": f"VLAN{vrf_id * 100 + svi_id}",
                                "ip_address_virtual": f"10.{vrf_id}.{svi_id}.1/24",
                            }
                            for svi_id in range(1, per_vrf_svi_count + 1)
                        ],
                    }
                    for vrf_id in range(1, vrf_count + 1)
                ],
            }
        ]
    }


def generate_spine_var(_name: str, number: int) -> dict:
    """Generate spine-specific variables."""
    return {
        "type": "spine",
        "spine": {
            "defaults": {
                "bgp_as": "65000.0",
                "id": f"{number}",
                "loopback_ipv4_pool": "10.0.0.0/16",
            }
        },
    }


def generate_l3leaf_var(number: int, spines: list[str]) -> dict:
    """Generate L3 leaf variables with adjacent leaves forming an MLAG pair."""
    pair_number = (number + 1) // 2
    first_node_id = 2 * pair_number - 1
    group_name = f"L3LEAF_PAIR{pair_number}"
    r = Random(group_name)  # noqa: S311
    spines = spines.copy()
    r.shuffle(spines)
    return {
        "type": "l3leaf",
        "l3leaf": {
            "defaults": {
                "bgp_as": f"65000.{pair_number}",
                "uplink_switches": spines[:2],
                "uplink_interfaces": ["Ethernet49", "Ethernet50"],
                "mlag_interfaces": ["Ethernet51", "Ethernet52"],
                "mlag_peer_ipv4_pool": "10.255.252.0/24",
                "mlag_peer_l3_ipv4_pool": "10.255.251.0/24",
                "loopback_ipv4_pool": "10.1.0.0/16",
                "vtep_loopback_ipv4_pool": "10.2.0.0/16",
                "uplink_ipv4_pool": "10.4.0.0/14",
                "virtual_router_mac_address": "00:11:22:33:44:55",
            },
            "node_groups": [
                {
                    "group": group_name,
                    "nodes": [
                        {
                            "name": f"l3leaf{node_id}",
                            "id": node_id,
                            "uplink_switch_interfaces": [f"Ethernet{node_id}/3", f"Ethernet{node_id}/4"],
                        }
                        for node_id in (first_node_id, first_node_id + 1)
                    ],
                }
            ],
        },
    }


def generate_l2leaf_var(number: int, l3leafs: list[str]) -> dict:
    """Generate L2 leaf variables with uplinks to both members of one MLAG pair."""
    pair_start = 2 * ((number - 1) % (len(l3leafs) // 2))
    return {
        "type": "l2leaf",
        "l2leaf": {
            "defaults": {
                "id": f"{number}",
                "uplink_switches": l3leafs[pair_start : pair_start + 2],
                "uplink_interfaces": ["Ethernet49", "Ethernet50"],
                "uplink_switch_interfaces": [f"Ethernet{number + 52}", f"Ethernet{number + 52}"],
            }
        },
    }
