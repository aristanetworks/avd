# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from itertools import chain

from anta.input_models.interfaces import InterfaceState
from anta.tests.interfaces import VerifyInterfacesStatus, VerifyPortChannels, VerifyStormControlDrops

from pyavd._anta.logs import LogMessage
from pyavd.j2filters import natural_sort

from ._base_classes import AntaTestInputFactory


class VerifyInterfacesStatusInputFactory(AntaTestInputFactory[VerifyInterfacesStatus.Input]):
    """
    Input factory class for the `VerifyInterfacesStatus` test.

    Generates test inputs for verifying the status of the following interface types:
    - Ethernet, Port-Channel, VLAN, Loopback, and DPS interfaces
    - Vxlan1 interface (only if the device is a VTEP)

    The expected status is 'adminDown' when the interface is shutdown, 'up' otherwise.

    Notes:
    - Ethernet/Port-Channel: Considers `validate_state` knob (default: True)
    - Ethernet: Considers `interface_defaults.ethernet.shutdown` when `shutdown` is not explicitly set
    - Vxlan1: Only tested if at least one VNI (L2 or L3) is configured and its source interface is operational (not shutdown and has required IP address)
    """

    def create(self) -> list[VerifyInterfacesStatus.Input] | None:
        """Create a list of inputs for the `VerifyInterfacesStatus` test."""
        interfaces: list[InterfaceState] = []

        # Add Ethernet interfaces, considering `validate_state` knob and interface defaults
        for intf in self.structured_config.ethernet_interfaces:
            if intf.validate_state is False:
                self.logger_adapter.debug(LogMessage.INTERFACE_VALIDATION_DISABLED, interface=intf.name)
                continue
            status = "adminDown" if intf.shutdown or (intf.shutdown is None and self.structured_config.interface_defaults.ethernet.shutdown) else "up"

            interfaces.append(InterfaceState(name=intf.name, status=status))

        # Add Port-Channel interfaces, considering `validate_state` knob
        for intf in self.structured_config.port_channel_interfaces:
            if intf.validate_state is False:
                self.logger_adapter.debug(LogMessage.INTERFACE_VALIDATION_DISABLED, interface=intf.name)
                continue
            interfaces.append(InterfaceState(name=intf.name, status="adminDown" if intf.shutdown else "up"))

        # Add VLAN, Loopback, and DPS interfaces
        interfaces.extend(
            [
                InterfaceState(name=intf.name, status="adminDown" if intf.shutdown else "up")
                for intf in chain(self.structured_config.vlan_interfaces, self.structured_config.loopback_interfaces, self.structured_config.dps_interfaces)
            ]
        )

        # If the device is a VTEP, add the Vxlan1 interface to the list under certain conditions
        if self.device.is_vtep:
            vxlan_config = self.structured_config.vxlan_interface.vxlan1.vxlan

            # Check if VNIs are configured (VLANs or VRFs)
            has_vnis = bool(vxlan_config.vlans or vxlan_config.vlan_range or vxlan_config.vrfs)

            if not has_vnis:
                self.logger_adapter.debug(LogMessage.INTERFACE_VXLAN1_NO_VNI)
            elif not self._is_vxlan_source_interface_operational():
                self.logger_adapter.debug(LogMessage.INTERFACE_VXLAN1_NOT_OPERATIONAL, source_interface=vxlan_config.source_interface)
            else:
                status = "adminDown" if vxlan_config.shutdown else "up"
                interfaces.append(InterfaceState(name="Vxlan1", status=status))

        return [VerifyInterfacesStatus.Input(interfaces=natural_sort(interfaces, sort_key="name"))] if interfaces else None

    def _is_vxlan_source_interface_operational(self) -> bool:
        """Check if the VXLAN source interface is operational (not shutdown and has IP configured)."""
        vxlan_src_intf = self.structured_config.vxlan_interface.vxlan1.vxlan.source_interface
        ipv6_enabled = bool(self.structured_config.vxlan_interface.vxlan1.vxlan.encapsulations.ipv6)

        # Check DPS interfaces
        if "Dps" in vxlan_src_intf and vxlan_src_intf in self.structured_config.dps_interfaces:
            # DPS interfaces don't support IPv6
            if ipv6_enabled:
                return False
            interface = self.structured_config.dps_interfaces[vxlan_src_intf]
            has_ip = bool(interface.ip_address)
        # Check Loopback interfaces
        elif vxlan_src_intf in self.structured_config.loopback_interfaces:
            interface = self.structured_config.loopback_interfaces[vxlan_src_intf]
            has_ip = bool(interface.ipv6_address if ipv6_enabled else interface.ip_address)
        else:
            return False

        # Interface is operational if it's not shutdown AND has the required IP address
        return not interface.shutdown and has_ip


class VerifyPortChannelsInputFactory(AntaTestInputFactory[VerifyPortChannels.Input]):
    """
    Input factory class for the `VerifyPortChannels` test.

    Port-channel interfaces from `port_channel_interfaces` in the device
    structured config with `validate_state` set to False or `shutdown` set to True
    are ignored.
    """

    def create(self) -> list[VerifyPortChannels.Input] | None:
        """Create a list of inputs for the `VerifyPortChannels` test."""
        ignored_interfaces: list[str] = []

        for po_intf in self.structured_config.port_channel_interfaces:
            if po_intf.validate_state is False:
                self.logger_adapter.debug(LogMessage.INTERFACE_VALIDATION_DISABLED, interface=po_intf.name)
                ignored_interfaces.append(po_intf.name)
                continue
            if po_intf.shutdown:
                self.logger_adapter.debug(LogMessage.INTERFACE_SHUTDOWN, interface=po_intf.name)
                ignored_interfaces.append(po_intf.name)

        return [VerifyPortChannels.Input(ignored_interfaces=natural_sort(ignored_interfaces))] if ignored_interfaces else [VerifyPortChannels.Input()]


class VerifyStormControlDropsInputFactory(AntaTestInputFactory[VerifyStormControlDrops.Input]):
    """
    Input factory class for the `VerifyStormControlDrops` test.

    Generate the test inputs only if any Ethernet or Port-Channel interfaces are configured with storm-control.
    """

    def create(self) -> list[VerifyStormControlDrops.Input] | None:
        for intf in self.structured_config.ethernet_interfaces:
            if intf.storm_control:
                return [VerifyStormControlDrops.Input()]
        for po_intf in self.structured_config.port_channel_interfaces:
            if po_intf.storm_control:
                return [VerifyStormControlDrops.Input()]
        return None
