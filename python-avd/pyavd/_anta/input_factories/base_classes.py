# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from abc import ABC, abstractmethod
from logging import getLogger
from typing import TYPE_CHECKING, Generic, TypeVar

from anta.models import AntaTest

from pyavd._anta.logs import LogMessage, TestLoggerAdapter

if TYPE_CHECKING:
    from collections.abc import Iterator

    from pyavd._anta.models import InputFactoryDataSource

T_Input = TypeVar("T_Input", bound=AntaTest.Input)


class AntaTestInputFactory(ABC, Generic[T_Input]):
    """
    Base class for `AntaTest.Input` factories.

    Implementations of this class must provide a `create` method that yields
    `AntaTest.Input` models.

    Attributes:
        data_source: `InputFactoryDataSource` instance containing the required data and helpers the generate the test inputs.
        structured_config: `EosCliConfigGen` model of the device.
        logger_adapter: Custom `TestLoggerAdapter` logger adapter used for logging in the input factory.
    """

    def __init__(self, data_source: InputFactoryDataSource, test_name: str) -> None:
        """Initialize the `AntaTestInputFactory`."""
        self.data_source = data_source
        self.structured_config = data_source.structured_config

        # Create the logger adapter for the test input factory
        self.logger_adapter = TestLoggerAdapter(logger=getLogger(self.__module__), extra={"device": self.data_source.hostname, "test": test_name})

    @abstractmethod
    def create(self) -> Iterator[T_Input]:
        """
        Yield the `AntaTest.Input` models for the `AntaTest`.

        If no inputs can be generated (e.g., no eligible LLDP neighbors configured),
        the method should return without yielding any values.
        """

    def is_peer_available(self, peer: str, identity: str) -> bool:
        """Check if a peer is part of the fabric and is deployed."""
        if not self.data_source.get_peer_device(peer):
            self.logger_adapter.debug(LogMessage.PEER_UNAVAILABLE, identity=identity, peer=peer)
            return False
        return True

    def get_peer_interface_ip(self, peer: str, peer_interface: str, interface: str) -> str | None:
        """Get the IP address of a peer interface."""
        if not self.is_peer_available(peer, identity=interface):
            return None

        if (peer_intf := self.data_source.get_peer_interface(peer, peer_interface)) is None:
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
        if (peer_intf := self.data_source.get_peer_interface(peer, peer_interface)) is None:
            self.logger_adapter.debug(LogMessage.PEER_INTERFACE_NOT_FOUND, interface=interface, peer=peer, peer_interface=peer_interface)
            return None

        shutdown_status = peer_intf.shutdown
        if shutdown_status:
            self.logger_adapter.debug(LogMessage.PEER_INTERFACE_SHUTDOWN, interface=interface, peer=peer, peer_interface=peer_interface)

        return shutdown_status
