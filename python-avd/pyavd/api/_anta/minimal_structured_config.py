# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass

from pyavd._utils import get, get_item


@dataclass(frozen=True)
class MinimalEthernetInterface:
    """A minimal version of an Ethernet interface containing only the required data to generate tests."""

    name: str
    ip_address: str
    shutdown: bool


@dataclass(frozen=True)
class MinimalStructuredConfig:
    """A minimal version of a device structured configuration containing only the required data to generate tests."""

    hostname: str
    is_deployed: bool
    dns_domain: str | None
    ethernet_interfaces: list[MinimalEthernetInterface]
    loopback0_ip: str | None
    vtep_ip: str | None


def get_minimal_structured_configs(structured_configs: dict[str, dict]) -> dict[str, MinimalStructuredConfig]:
    """
    Get a minimal version of structured configurations for all devices to generate tests.

    Loaded in dataclasses and used in `pyavd.get_device_test_catalog` to generate ANTA catalogs.

    Parameters
    ----------
    structured_configs : dict[str, dict]
        Dictionary keyed by hostname containing structured configurations for all devices.
        Each structured config should be converted and validated according to AVD `eos_cli_config_gen` schema first using `pyavd.validate_structured_config`.

    Returns:
    -------
    dict[str, MinimalStructuredConfig]
        Dictionary keyed by hostname containing minimal structured configurations for all devices.
    """
    minimal_structured_configs: dict[str, MinimalStructuredConfig] = {}

    for device, structured_config in structured_configs.items():
        # Parse the Ethernet interfaces
        minimal_ethernet_interfaces = [
            MinimalEthernetInterface(
                name=intf["name"], ip_address=intf_ip, shutdown=get(intf, "shutdown", get(structured_config, "interface_defaults.ethernet.shutdown", False))
            )
            for intf in get(structured_config, "ethernet_interfaces", default=[])
            if (intf_ip := get(intf, "ip_address")) and get(intf, "switchport.enabled") is False
        ]

        # Get the VTEP IP if any
        vxlan_source_interface = get(structured_config, "vxlan_interface.vxlan1.vxlan.source_interface")
        if vxlan_source_interface is not None:
            if "Dps" in vxlan_source_interface:
                interface_model = get(structured_config, "dps_interfaces", default=[])
            else:
                interface_model = get(structured_config, "loopback_interfaces", default=[])
            vtep_ip = get(get_item(interface_model, "name", vxlan_source_interface, default={}), "ip_address")
        else:
            vtep_ip = None

        # Create the minimal structured configuration
        minimal_structured_configs[device] = MinimalStructuredConfig(
            hostname=structured_config["hostname"],
            is_deployed=get(structured_config, "metadata.is_deployed", default=False),
            dns_domain=get(structured_config, "dns_domain"),
            ethernet_interfaces=minimal_ethernet_interfaces,
            loopback0_ip=get(get_item(get(structured_config, "loopback_interfaces", []), "name", "Loopback0", default={}), "ip_address"),
            vtep_ip=vtep_ip,
        )
    return minimal_structured_configs
