# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from ipaddress import IPv4Address, ip_interface
from logging import getLogger
from typing import Any

from pyavd._utils import get, get_item

LOGGER = getLogger(__name__)


@dataclass(frozen=True)
class AvdEthernetInterface:
    """A minimal version of an Ethernet interface containing only the required data to generate tests."""

    name: str
    ip_address: str | None
    shutdown: bool


@dataclass(frozen=True)
class AvdDeviceData:
    """A minimal version of a device structured configuration containing only the required data to generate tests."""

    hostname: str
    is_deployed: bool
    dns_domain: str | None
    ethernet_interfaces: dict[str, AvdEthernetInterface]
    loopback0_ip: IPv4Address | None
    vtep_ip: IPv4Address | None

    @classmethod
    def from_structured_config(cls, structured_config: dict[str, Any]) -> AvdDeviceData:
        """
        Build and return an `AvdDeviceData` instance from a device AVD structured configuration.

        Args:
            structured_config: A dictionary with structured configuration.
                Variables should be converted and validated according to AVD `eos_cli_config_gen` schema first using `pyavd.validate_structured_config`.

        Returns:
            An `AvdDeviceData` instance populated with data.
        """
        # Get the Ethernet interfaces
        default_shutdown = get(structured_config, "interface_defaults.ethernet.shutdown", False)
        ethernet_interfaces: dict[str, AvdEthernetInterface] = {
            intf["name"]: AvdEthernetInterface(
                name=intf["name"],
                ip_address=get(intf, "ip_address"),
                shutdown=get(intf, "shutdown", default_shutdown),
            )
            for intf in get(structured_config, "ethernet_interfaces", default=[])
        }

        # Get the Loopback0 IP
        loopback0_ip = get(get_item(get(structured_config, "loopback_interfaces", []), "name", "Loopback0", default={}), "ip_address")

        # Get the VTEP IP
        vxlan_source_interface = get(structured_config, "vxlan_interface.vxlan1.vxlan.source_interface")
        if vxlan_source_interface is not None:
            if "Dps" in vxlan_source_interface:
                interface_model = get(structured_config, "dps_interfaces", default=[])
            else:
                interface_model = get(structured_config, "loopback_interfaces", default=[])
            vtep_ip = get(get_item(interface_model, "name", vxlan_source_interface, default={}), "ip_address")
        else:
            vtep_ip = None

        # Create and return the device AvdDeviceData
        return AvdDeviceData(
            hostname=structured_config["hostname"],
            is_deployed=get(structured_config, "metadata.is_deployed", default=False),
            dns_domain=get(structured_config, "dns_domain"),
            ethernet_interfaces=ethernet_interfaces,
            loopback0_ip=ip_interface(loopback0_ip).ip if loopback0_ip else None,
            vtep_ip=ip_interface(vtep_ip).ip if vtep_ip else None,
        )


@dataclass(frozen=True)
class AvdFabricData:
    """
    Aggregates minimal data for all devices in the fabric, optimized to generate tests.

    It is recommended to instantiate this class using the `from_structured_configs` class method.
    """

    devices: dict[str, AvdDeviceData]
    """Mapping of device hostname to its `AvdDeviceData` for all devices."""
    loopback0_ips: dict[str, IPv4Address]
    """Mapping of device hostname to its Loopback0 IPv4 address. Only includes devices that have a Loopback0 IP configured."""
    vtep_ips: dict[str, IPv4Address]
    """Mapping of device hostname to its VTEP IPv4 address. Only includes devices that have a VTEP IP configured."""
    special_ips: defaultdict[str, list[IPv4Address]]
    """Mapping of device hostname to a list of 'special' IPs (Loopback0 and VTEP). Only includes devices with at least one special IP."""

    @classmethod
    def from_structured_configs(cls, structured_configs: dict[str, dict[str, Any]]) -> AvdFabricData:
        """
        Build and return an `AvdFabricData` instance from a dictionary of AVD structured configurations.

        Args:
            structured_configs: A dictionary of structured configurations for all devices, keyed by hostname.
                Variables should be converted and validated according to AVD `eos_cli_config_gen` schema first using `pyavd.validate_structured_config`.

        Returns:
            An `AvdFabricData` instance populated with data.
        """
        devices: dict[str, AvdDeviceData] = {}
        loopback0_ips: dict[str, IPv4Address] = {}
        vtep_ips: dict[str, IPv4Address] = {}
        special_ips: defaultdict[str, list[IPv4Address]] = defaultdict(list)

        for device, structured_config in structured_configs.items():
            device_data = AvdDeviceData.from_structured_config(structured_config)

            # Update the IP mappings
            if device_data.loopback0_ip:
                loopback0_ips[device] = device_data.loopback0_ip
                special_ips[device].append(device_data.loopback0_ip)
            else:
                LOGGER.debug("<%s> Skipped Loopback0 IP mapping - IP not found", device)

            if device_data.vtep_ip:
                vtep_ips[device] = device_data.vtep_ip
                special_ips[device].append(device_data.vtep_ip)
            else:
                LOGGER.debug("<%s> Skipped VTEP IP mapping - IP not found", device)

            # Update the devices mapping
            devices[device] = device_data

        return AvdFabricData(devices=devices, loopback0_ips=loopback0_ips, vtep_ips=vtep_ips, special_ips=special_ips)
