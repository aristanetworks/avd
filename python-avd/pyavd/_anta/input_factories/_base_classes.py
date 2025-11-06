# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from abc import ABC, abstractmethod
from logging import getLogger
from typing import TYPE_CHECKING, Generic, TypeVar

from anta.models import AntaTest

from pyavd._anta.logs import LogMessage, TestLoggerAdapter

if TYPE_CHECKING:
    from pyavd._anta.models import DeviceTestContext

Input = TypeVar("Input", bound=AntaTest.Input)


class AntaTestInputFactory(ABC, Generic[Input]):
    """
    Base class for `AntaTest.Input` factories.

    Implementations of this class must provide a `create` method that returns
    a list of `AntaTest.Input` models or `None`.

    Attributes:
        device: `DeviceTestContext` instance for the test.
        structured_config: `EosCliConfigGen` model of the device.
        fabric_data: `AvdFabricData` instance containing data of all devices in the fabric.
        logger_adapter: Custom `TestLoggerAdapter` logger adapter used for logging in the input factory.
    """

    def __init__(self, device_context: DeviceTestContext, test_name: str) -> None:
        """Initialize the `AntaTestInputFactory`."""
        self.device = device_context
        self.structured_config = device_context.structured_config
        self.fabric_data = device_context.fabric_data

        # Create the logger adapter for the test input factory
        self.logger_adapter = TestLoggerAdapter(logger=getLogger(self.__module__), extra={"device": self.device.hostname, "test": test_name})

    @abstractmethod
    def create(self) -> list[Input] | None:
        """Create the `AntaTest.Input` models for the `AntaTest`."""

    def is_peer_available(self, peer: str, identity: str) -> bool:
        """Check if a peer is part of the fabric and is deployed."""
        if peer not in self.fabric_data.devices or not self.fabric_data.devices[peer].is_deployed:
            self.logger_adapter.debug(LogMessage.PEER_UNAVAILABLE, identity=identity, peer=peer)
            return False
        return True

    def get_peer_interface_ip(self, peer: str, peer_interface: str, interface: str) -> str | None:
        """Get the IP address of a peer interface."""
        if not self.is_peer_available(peer, identity=interface):
            return None

        if (peer_intf := self.fabric_data.devices[peer].ethernet_interfaces.get(peer_interface)) is None:
            self.logger_adapter.debug(LogMessage.PEER_INTERFACE_NOT_FOUND, interface=interface, peer=peer, peer_interface=peer_interface)
            return None

        peer_interface_ip = peer_intf.ip_address

        if peer_interface_ip is None:
            log_message = LogMessage.PEER_INTERFACE_NO_IP
        elif peer_interface_ip == "dhcp":
            log_message = LogMessage.PEER_INTERFACE_USING_DHCP
        elif "unnumbered" in peer_interface_ip:
            log_message = LogMessage.PEER_INTERFACE_UNNUMBERED
        else:
            log_message = None

        if log_message:
            self.logger_adapter.debug(log_message, interface=interface, peer=peer, peer_interface=peer_interface)
            return None

        return peer_interface_ip

    def is_peer_interface_shutdown(self, peer: str, peer_interface: str, interface: str) -> bool | None:
        """
        Check if a peer's Ethernet interface is in a shutdown state.

        Assumes the peer is available and its structured config has been loaded.

        Args:
            peer: The name of the peer device.
            peer_interface: The name of the Ethernet interface on the peer device.
            interface: The name of the Ethernet interface on the local device (for logging).

        Returns:
            The shutdown state (True or False) if the interface is found, otherwise None.
        """
        if (peer_intf := self.fabric_data.devices[peer].ethernet_interfaces.get(peer_interface)) is None:
            self.logger_adapter.debug(LogMessage.PEER_INTERFACE_NOT_FOUND, interface=interface, peer=peer, peer_interface=peer_interface)
            return None

        shutdown_status = peer_intf.shutdown
        if shutdown_status:
            self.logger_adapter.debug(LogMessage.PEER_INTERFACE_SHUTDOWN, interface=interface, peer=peer, peer_interface=peer_interface)

        return shutdown_status
