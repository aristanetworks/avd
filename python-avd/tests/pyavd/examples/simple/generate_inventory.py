# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from random import Random
from typing import Any

FABRIC_VARS = {"fabric_name": "FABRIC"}
NETWORK_PORTS = {
    "port_profiles": [
        {
            "profile": "user",
            "vlans": "100-200,456,222,999,1000-3000",
            "mode": "trunk",
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
    hostvars = {}
    network_services = generate_network_services(vrf_count, per_vrf_svi_count)
    spines: list[str] = []
    l3leafs: list[str] = []
    for number in range(1, spine_count + 1):
        name = f"spine{number}"
        spines.append(name)
        host_hostvars = {"inventory_hostname": name}
        host_hostvars.update(FABRIC_VARS)
        host_hostvars.update(generate_spine_var(name, number))
        hostvars[name] = host_hostvars

    for number in range(1, l3leaf_count + 1):
        name = f"l3leaf{number}"
        l3leafs.append(name)
        host_hostvars = {"inventory_hostname": name}
        host_hostvars.update(FABRIC_VARS)
        host_hostvars.update(NETWORK_PORTS)
        host_hostvars.update(network_services)
        host_hostvars.update(generate_l3leaf_var(name, number, spines))
        hostvars[name] = host_hostvars

    for number in range(1, l2leaf_count + 1):
        name = f"l2leaf{number}"
        host_hostvars = {"inventory_hostname": name}
        host_hostvars.update(FABRIC_VARS)
        host_hostvars.update(NETWORK_PORTS)
        host_hostvars.update(network_services)
        host_hostvars.update(generate_l2leaf_var(name, number, l3leafs))
        hostvars[name] = host_hostvars

    return hostvars


def generate_network_services(vrf_count: int, per_vrf_svi_count: int) -> dict:
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


def generate_spine_var(name: str, number: int) -> dict:  # noqa: ARG001
    return {
        "type": "spine",
        "spine": {
            "defaults": {
                "bgp_as": "65000.0",
                "id": number,
                "loopback_ipv4_pool": "10.0.0.0/16",
            }
        },
    }


def generate_l3leaf_var(name: str, number: int, spines: list[str]) -> dict:
    r = Random(name)  # noqa: S311
    spines = spines.copy()
    r.shuffle(spines)
    return {
        "type": "l3leaf",
        "l3leaf": {
            "defaults": {
                "bgp_as": f"65000.{number}",
                "id": number,
                "uplink_switches": spines[:2],
                "uplink_interfaces": [f"Ethernet{number}/1", f"Ethernet{number}/2"],
                "uplink_switch_interfaces": [
                    f"Ethernet{number}/3",
                    f"Ethernet{number}/4",
                ],
                "filter": {"only_vlans_in_use": True},
                "loopback_ipv4_pool": "10.1.0.0/16",
                "vtep_loopback_ipv4_pool": "10.2.0.0/16",
                "uplink_ipv4_pool": "10.4.0.0/14",
                "virtual_router_mac_address": "00:11:22:33:44:55",
            }
        },
    }


def generate_l2leaf_var(name: str, number: int, l3leafs: list[str]) -> dict:
    r = Random(name)  # noqa: S311
    l3leafs = l3leafs.copy()
    r.shuffle(l3leafs)
    return {
        "type": "l2leaf",
        "l2leaf": {
            "defaults": {
                "id": number,
                "uplink_switches": l3leafs[:2],
                "uplink_interfaces": [f"Ethernet{number}/1", f"Ethernet{number}/2"],
                "uplink_switch_interfaces": [
                    f"Ethernet{number}/3",
                    f"Ethernet{number}/4",
                ],
                "filter": {"only_vlans_in_use": True},
            }
        },
    }
