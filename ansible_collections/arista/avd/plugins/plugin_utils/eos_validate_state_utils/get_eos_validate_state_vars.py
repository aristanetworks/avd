# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ipaddress import ip_interface

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


def get_eos_validate_state_vars(vars: dict) -> dict:
    """
    Generates variables for the eos_validate_state tests, which are used in AvdTestBase subclasses.
    These variables include mappings for loopback and VTEP interfaces.

    Args:
      vars (dict): A dictionary of devices and their configurations.

    Returns:
        dict: A dictionary containing:
            - "loopback0_mapping": a list of tuples where each tuple contains a hostname and its Loopback0 IP address.
            - "vtep_mapping": a list of tuples where each tuple contains a hostname and its VTEP IP address if `Vxlan1` is the source_interface.
    """
    results = {}

    for host in vars:
        loopback_interfaces = get(vars, f"{host};loopback_interfaces", [], separator=";")
        vtep_interface = get(vars, f"{host};vxlan_interface;Vxlan1;vxlan;source_interface", separator=";")

        for loopback_interface in loopback_interfaces:
            # TODO Add more conditions here to avoid using type `l3leaf` in connectivity tests; router_id or update_source maybe?
            if loopback_interface["name"] == "Loopback0":
                results.setdefault("loopback0_mapping", []).append((host, str(ip_interface(loopback_interface["ip_address"]).ip)))
            if vtep_interface == loopback_interface["name"]:
                results.setdefault("vtep_mapping", []).append((host, str(ip_interface(loopback_interface["ip_address"]).ip)))

    return results
