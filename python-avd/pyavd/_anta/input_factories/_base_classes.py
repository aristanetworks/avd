# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from abc import ABC, abstractmethod
from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._anta.logs import LogMessage, TestLoggerAdapter

if TYPE_CHECKING:
    from anta.models import AntaTest

    from pyavd._anta.models import DeviceTestContext


class AntaTestInputFactory(ABC):
    """
    Base class for `AntaTest.Input` factories.

    Implementations of this class must provide a `create` method that returns
    a list of `AntaTest.Input` models or `None`.

    Attributes:
    ----------
    device : DeviceTestContext
        The device context for the test.
    structured_config : EosCliConfigGen
        The structured configuration model of the device.
    minimal_structured_configs : dict[str, MinimalStructuredConfig]
        The minimal structured configurations of all devices in the fabric.
    logger_adapter : TestLoggerAdapter
        Custom logger adapter used for the input factory.
    """

    def __init__(self, device_context: DeviceTestContext, test_name: str) -> None:
        """Initialize the `AntaTestInputFactory`."""
        self.device = device_context
        self.structured_config = device_context.structured_config
        self.minimal_structured_configs = device_context.minimal_structured_configs

        # Create the logger adapter for the test input factory
        self.logger_adapter = TestLoggerAdapter(logger=getLogger(self.__module__), extra={"device": self.device.hostname, "test": test_name})

    @abstractmethod
    def create(self) -> list[AntaTest.Input] | None:
        """Create the `AntaTest.Input` models for the `AntaTest`."""

    def is_peer_available(self, peer: str, identity: str) -> bool:
        """Check if a peer is part of the fabric and is deployed."""
        if peer not in self.minimal_structured_configs or not self.minimal_structured_configs[peer].is_deployed:
            self.logger_adapter.debug(LogMessage.PEER_UNAVAILABLE, identity=identity, peer=peer)
            return False
        return True

    def get_interface_ip(self, peer: str, peer_interface: str, interface: str) -> str | None:
        """Get the IP address of a peer interface."""
        if not self.is_peer_available(peer, identity=interface):
            return None

        for intf in self.minimal_structured_configs[peer].ethernet_interfaces:
            if intf.name == peer_interface:
                if intf.ip_address == "dhcp":
                    self.logger_adapter.debug(LogMessage.PEER_INTERFACE_USING_DHCP, interface=interface, peer=peer, peer_interface=peer_interface)
                    return None
                if "unnumbered" in intf.ip_address:
                    self.logger_adapter.debug(LogMessage.PEER_INTERFACE_UNNUMBERED, interface=interface, peer=peer, peer_interface=peer_interface)
                    return None
                return intf.ip_address
        self.logger_adapter.debug(LogMessage.PEER_INTERFACE_NOT_FOUND, interface=interface, peer=peer, peer_interface=peer_interface)
        return None

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
        peer_intf = next((intf for intf in self.minimal_structured_configs[peer].ethernet_interfaces if intf.name == peer_interface), None)

        if peer_intf is None:
            self.logger_adapter.debug(LogMessage.PEER_INTERFACE_NOT_FOUND, interface=interface, peer=peer, peer_interface=peer_interface)
            return None

        shutdown_status = peer_intf.shutdown
        if shutdown_status:
            self.logger_adapter.debug(LogMessage.PEER_INTERFACE_SHUTDOWN, interface=interface, peer=peer, peer_interface=peer_interface)

        return shutdown_status
