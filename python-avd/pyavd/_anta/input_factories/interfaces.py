# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from itertools import chain

from anta.input_models.interfaces import InterfaceState
from anta.tests.interfaces import VerifyInterfacesStatus, VerifyPortChannels

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


class VerifyPortChannelsInputFactory(AntaTestInputFactory):
    """
    Input factory class for the `VerifyPortChannels` test.

    Port-channel interfaces from `port_channel_interfaces` in the device
    structured config with `validate_state` set to False or `shutdown` set to True
    are ignored.
    """

    def create(self) -> list[VerifyPortChannels.Input] | None:
        """Create a list of inputs for the `VerifyPortChannels` test."""
        ignored_interfaces = []

        for po_intf in self.structured_config.port_channel_interfaces:
            if po_intf.validate_state is False:
                self.logger_adapter.debug(LogMessage.INTERFACE_VALIDATION_DISABLED, interface=po_intf.name)
                ignored_interfaces.append(po_intf.name)
                continue
            if po_intf.shutdown:
                self.logger_adapter.debug(LogMessage.INTERFACE_SHUTDOWN, interface=po_intf.name)
                ignored_interfaces.append(po_intf.name)
                continue

        return [VerifyPortChannels.Input(ignored_interfaces=natural_sort(ignored_interfaces))] if ignored_interfaces else [VerifyPortChannels.Input()]
