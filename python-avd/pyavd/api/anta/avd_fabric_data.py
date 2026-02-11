# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass
from ipaddress import IPv4Address, IPv4Interface, ip_interface
from logging import getLogger
from typing import Any

from pyavd._utils import get, get_item

LOGGER = getLogger(__name__)


@dataclass(frozen=True)
class AVDEthernetInterface:
    """A minimal version of an Ethernet interface containing only the required data to generate tests."""

    name: str
    ip_address: str | None
    shutdown: bool


@dataclass(frozen=True)
class AVDDeviceData:
    """A minimal version of a device structured configuration containing only the required data to generate tests."""

    hostname: str
    is_deployed: bool
    dns_domain: str | None
    ethernet_interfaces: dict[str, AVDEthernetInterface]
    loopback0_ip: IPv4Address | None
    vtep_ip: IPv4Address | None
    mlag_vtep_ip: IPv4Address | None
    is_vtep: bool
    is_wan_router: bool
    exclude_as_extra_fabric_validation_target: bool

    @classmethod
    def from_structured_config(cls, structured_config: dict[str, Any]) -> AVDDeviceData:
        """
        Build and return an `AVDDeviceData` instance from a device AVD structured configuration.

        Args:
            structured_config: A dictionary with structured configuration.
                Variables should be converted and validated according to AVD `eos_cli_config_gen` schema first using `pyavd.validate_structured_config`.

        Returns:
            An `AVDDeviceData` instance populated with data.
        """
        # Get the Ethernet interfaces
        default_shutdown = get(structured_config, "interface_defaults.ethernet.shutdown", False)
        ethernet_interfaces: dict[str, AVDEthernetInterface] = {
            intf["name"]: AVDEthernetInterface(
                name=intf["name"],
                ip_address=get(intf, "ip_address"),
                shutdown=get(intf, "shutdown", default_shutdown),
            )
            for intf in get(structured_config, "ethernet_interfaces", default=[])
        }

        # Get the Loopback0 IP
        loopback0_ip_str = get(get_item(get(structured_config, "loopback_interfaces", []), "name", "Loopback0", default={}), "ip_address")
        loopback0_ip = IPv4Interface(loopback0_ip_str).ip if loopback0_ip_str else None

        # Get the VTEP IPs
        vtep_ip, mlag_vtep_ip = cls._get_vtep_ips(structured_config)

        # Get the VTEP roles
        is_vtep, is_wan_router = cls._get_vtep_roles(structured_config)

        # Create and return the device AVDDeviceData
        return cls(
            hostname=structured_config["hostname"],
            is_deployed=get(structured_config, "metadata.is_deployed", default=False),
            dns_domain=get(structured_config, "dns_domain"),
            ethernet_interfaces=ethernet_interfaces,
            loopback0_ip=loopback0_ip,
            vtep_ip=vtep_ip,
            mlag_vtep_ip=mlag_vtep_ip,
            is_vtep=is_vtep,
            is_wan_router=is_wan_router,
            exclude_as_extra_fabric_validation_target=get(structured_config, "metadata.exclude_as_extra_fabric_validation_target", default=False),
        )

    @staticmethod
    def _get_vtep_ips(structured_config: dict[str, Any]) -> tuple[IPv4Address | None, IPv4Address | None]:
        """
        Get the VTEP and MLAG VTEP IPv4 addresses from the structured configuration.

        Args:
            structured_config: Device structured configuration dictionary.

        Returns:
            A tuple of VTEP IP and MLAG VTEP IP. Either or both may be None if not configured or if IPv6-only encapsulation is used.
        """
        vtep_ip = None
        mlag_vtep_ip = None

        # Check VXLAN encapsulation type to determine which IP address family is used on source interfaces
        # If not explicitly configured, EOS defaults to IPv4 encapsulation
        vxlan_encap_ipv4 = get(structured_config, "vxlan_interface.vxlan1.vxlan.encapsulations.ipv4")
        vxlan_encap_ipv6 = get(structured_config, "vxlan_interface.vxlan1.vxlan.encapsulations.ipv6")

        # Return early if IPv6-only encapsulation is configured
        if vxlan_encap_ipv6 is True and vxlan_encap_ipv4 is not True:
            return None, None

        # Get the VTEP IP
        vxlan_source_interface = get(structured_config, "vxlan_interface.vxlan1.vxlan.source_interface")
        loopback_interfaces = get(structured_config, "loopback_interfaces", default=[])
        dps_interfaces = get(structured_config, "dps_interfaces", default=[])
        if vxlan_source_interface is not None:
            # Determine which interface model to pick based on source interface type
            interface_model = dps_interfaces if "Dps" in vxlan_source_interface else loopback_interfaces

            vtep_ip_str = get(get_item(interface_model, "name", vxlan_source_interface, default={}), "ip_address")
            vtep_ip = vtep_ip_addr if vtep_ip_str and isinstance((vtep_ip_addr := ip_interface(vtep_ip_str).ip), IPv4Address) else None

        # Get the MLAG VTEP IP (for Multi-VTEP MLAG feature)
        vxlan_mlag_source_interface = get(structured_config, "vxlan_interface.vxlan1.vxlan.mlag_source_interface")
        if vxlan_mlag_source_interface is not None:
            # Only supported with loopback interfaces
            mlag_vtep_ip_str = get(get_item(loopback_interfaces, "name", vxlan_mlag_source_interface, default={}), "ip_address")
            mlag_vtep_ip = mlag_vtep_ip_addr if mlag_vtep_ip_str and isinstance((mlag_vtep_ip_addr := ip_interface(mlag_vtep_ip_str).ip), IPv4Address) else None

        return vtep_ip, mlag_vtep_ip

    @staticmethod
    def _get_vtep_roles(structured_config: dict[str, Any]) -> tuple[bool, bool]:
        """
        Get the VTEP-related roles based on VXLAN configuration.

        Args:
            structured_config: Device structured configuration dictionary.

        Returns:
            A tuple of two booleans, indicating if the device is a VTEP and a WAN router.
        """
        vxlan_source_interface = get(structured_config, "vxlan_interface.vxlan1.vxlan.source_interface")
        is_vtep = vxlan_source_interface is not None
        is_wan_router = is_vtep and "Dps" in vxlan_source_interface
        return is_vtep, is_wan_router


@dataclass(frozen=True)
class AVDFabricData:
    """
    Aggregates minimal data for all devices in the fabric, optimized to generate tests.

    It is recommended to instantiate this class using the `from_structured_configs` class method.
    """

    devices: dict[str, AVDDeviceData]
    """Mapping of device hostname to its `AVDDeviceData` for all devices."""
    loopback0_mapping: dict[str, IPv4Address]
    """Mapping of device hostname to its Loopback0 IPv4 address.

    Includes deployed devices that have a Loopback0 IP configured.

    WAN devices and devices that are marked as excluded as targets from extra validation tests are excluded."""
    dps_mapping: dict[str, IPv4Address]
    """Mapping of device hostname to its DPS IPv4 address.

    Includes deployed WAN routers that have a DPS interface configured as their VXLAN source interface.

    Devices that are marked as excluded as targets from extra validation tests are excluded.
    """
    underlay_reachability_targets: set[IPv4Address]
    """Set of all underlay reachability target IPv4 addresses (Loopback0, VTEP, and MLAG VTEP).

    Includes IPs of all deployed devices.

    IPs of WAN devices and devices that are marked as excluded as targets from extra validation tests are excluded.

    Uses a set to deduplicate IPs across devices (e.g., MLAG pairs sharing the same VTEP IP
    or in Multi-VTEP scenarios where Loopback0 is commonly reused as the local VTEP IP).
    """

    @classmethod
    def from_structured_configs(cls, structured_configs: dict[str, dict[str, Any]]) -> AVDFabricData:
        """
        Build and return an `AVDFabricData` instance from a dictionary of AVD structured configurations.

        Args:
            structured_configs: A dictionary of structured configurations for all devices, keyed by hostname.
                Variables should be converted and validated according to AVD `eos_cli_config_gen` schema first using `pyavd.validate_structured_config`.

        Returns:
            An `AVDFabricData` instance populated with data.
        """
        devices: dict[str, AVDDeviceData] = {}
        loopback0_mapping: dict[str, IPv4Address] = {}
        dps_mapping: dict[str, IPv4Address] = {}
        underlay_reachability_targets: set[IPv4Address] = set()

        for device, structured_config in structured_configs.items():
            device_data = AVDDeviceData.from_structured_config(structured_config)

            # Update the devices mapping
            devices[device] = device_data

            # Devices excluded as destination targets are not added to the IP mappings
            if device_data.exclude_as_extra_fabric_validation_target:
                LOGGER.debug("<%s> Skipped from all IPv4 mappings - Device excluded as a target from extra validation tests", device)
                continue

            # Undeployed devices are not added to the IP mappings
            if not device_data.is_deployed:
                LOGGER.debug("<%s> Skipped from all IPv4 mappings - Device is not deployed", device)
                continue

            # Collect DPS IP
            if device_data.is_wan_router:
                if device_data.vtep_ip:
                    dps_mapping[device] = device_data.vtep_ip
                else:
                    LOGGER.debug("<%s> Skipped DPS IP from DPS mapping - IP address not configured or IPv6-only", device)
                # WAN routers are not added to the other IP mappings
                continue

            # Collect Loopback0 IP
            if device_data.loopback0_ip:
                loopback0_mapping[device] = device_data.loopback0_ip
                underlay_reachability_targets.add(device_data.loopback0_ip)
            else:
                LOGGER.debug(
                    "<%s> Skipped Loopback0 IP from Loopback0 mapping and underlay reachability targets - IP address not configured or IPv6-only", device
                )

            # Collect VTEP IPs
            if device_data.vtep_ip:
                underlay_reachability_targets.add(device_data.vtep_ip)
            else:
                LOGGER.debug("<%s> Skipped VTEP IP from underlay reachability targets - IP address not configured or IPv6-only", device)
            if device_data.mlag_vtep_ip:
                underlay_reachability_targets.add(device_data.mlag_vtep_ip)
            else:
                LOGGER.debug("<%s> Skipped MLAG VTEP IP from underlay reachability targets - IP address not configured or IPv6-only", device)

        return AVDFabricData(
            devices=devices,
            loopback0_mapping=loopback0_mapping,
            dps_mapping=dps_mapping,
            underlay_reachability_targets=underlay_reachability_targets,
        )
