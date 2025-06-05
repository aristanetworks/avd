# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from itertools import chain

from anta.input_models.interfaces import InterfaceState
from anta.tests.interfaces import (
    VerifyIllegalLACP,
    VerifyInterfaceDiscards,
    VerifyInterfaceErrors,
    VerifyInterfacesStatus,
    VerifyInterfaceUtilization,
    VerifyPortChannels,
    VerifyStormControlDrops,
)

from pyavd._anta.logs import LogMessage
from pyavd.j2filters import natural_sort

from ._base_classes import AntaTestInputFactory


class VerifyInterfacesStatusInputFactory(AntaTestInputFactory):
    """
    Input factory class for the `VerifyInterfacesStatus` test.

    This factory generates test inputs for verifying the status of interfaces.

    The following interfaces are checked:
    - Ethernet interfaces - `ethernet_interfaces`
    - Port-Channel interfaces - `port_channel_interfaces`
    - VLAN interfaces - `vlan_interfaces`
    - Loopback interfaces - `loopback_interfaces`
    - DPS interfaces - `dps_interfaces`
    - Vxlan1 interface, if the device is a VTEP

    The expected status is 'adminDown' when the interface is shutdown, 'up' otherwise.

    For Ethernet and Port-Channel interfaces, `validate_state` knob (default: True) is considered.

    For Ethernet interfaces, `interface_defaults.ethernet.shutdown` is considered when `shutdown` is not set
    """

    def create(self) -> list[VerifyInterfacesStatus.Input] | None:
        """Create a list of inputs for the `VerifyInterfacesStatus` test."""
        interfaces = []

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

        # If the device is a VTEP, add the Vxlan1 interface to the list
        if self.device.is_vtep:
            interfaces.append(InterfaceState(name="Vxlan1", status="up"))

        return [VerifyInterfacesStatus.Input(interfaces=natural_sort(interfaces, sort_key="name"))] if interfaces else None


class VerifyInterfaceDiscardsInputFactory(AntaTestInputFactory):
    """Input factory class for the `VerifyInterfaceDiscards` test."""

    def create(self) -> list[VerifyInterfaceDiscards.Input] | None:
        """Create a list of inputs for the `VerifyInterfaceDiscards` test."""
        interfaces = [
            intf.name
            for intf in self.device.filtered_ethernet_interfaces
            if "." not in intf.name  # Subinterfaces do not contain discard info
        ]

        return [VerifyInterfaceDiscards.Input(interfaces=natural_sort(interfaces))] if interfaces else None


class VerifyInterfaceErrorsInputFactory(AntaTestInputFactory):
    """Input factory class for the `VerifyInterfaceErrors` test."""

    def create(self) -> list[VerifyInterfaceErrors.Input] | None:
        """Create a list of inputs for the `VerifyInterfaceErrors` test."""
        interfaces = [
            intf.name
            for intf in self.device.filtered_ethernet_interfaces
            if "." not in intf.name  # Subinterfaces do not contain error info
        ]

        return [VerifyInterfaceErrors.Input(interfaces=natural_sort(interfaces))] if interfaces else None


class VerifyInterfaceUtilizationInputFactory(AntaTestInputFactory):
    """Input factory class for the `VerifyInterfaceUtilization` test."""

    def create(self) -> list[VerifyInterfaceUtilization.Input] | None:
        """Create a list of inputs for the `VerifyInterfaceUtilization` test."""
        interfaces = [
            intf.name
            for intf in self.device.filtered_ethernet_interfaces
            if "." not in intf.name  # Subinterfaces do not contain rates info
        ]

        return [VerifyInterfaceUtilization.Input(interfaces=natural_sort(interfaces))] if interfaces else None


class VerifyPortChannelsInputFactory(AntaTestInputFactory):
    """Input factory class for the `VerifyPortChannels` test."""

    def create(self) -> list[VerifyPortChannels.Input] | None:
        """Create a list of inputs for the `VerifyPortChannels` test."""
        interfaces = [
            intf.name
            for intf in self.device.filtered_port_channel_interfaces
            if "." not in intf.name  # Only parent port-channels are needed
        ]

        return [VerifyPortChannels.Input(interfaces=natural_sort(interfaces))] if interfaces else None


class VerifyIllegalLACPInputFactory(AntaTestInputFactory):
    """Input factory class for the `VerifyIllegalLACP` test."""

    def create(self) -> list[VerifyIllegalLACP.Input] | None:
        """Create a list of inputs for the `VerifyIllegalLACP` test."""
        interfaces = [
            intf.name
            for intf in self.device.filtered_port_channel_interfaces
            if "." not in intf.name  # Only parent port-channels are needed
        ]

        return [VerifyIllegalLACP.Input(interfaces=natural_sort(interfaces))] if interfaces else None


class VerifyStormControlDropsInputFactory(AntaTestInputFactory):
    """Input factory class for the `VerifyStormControlDrops` test."""

    def create(self) -> list[VerifyStormControlDrops.Input] | None:
        """Create a list of inputs for the `VerifyStormControlDrops` test."""
        interfaces = [intf.name for intf in chain(self.device.filtered_ethernet_interfaces, self.device.filtered_port_channel_interfaces) if intf.storm_control]

        return [VerifyStormControlDrops.Input(interfaces=natural_sort(interfaces))] if interfaces else None
