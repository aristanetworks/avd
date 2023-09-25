# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from asyncio import get_event_loop
from functools import partial
from json import JSONDecodeError, loads
from logging import getLogger

from ansible.errors import AnsibleError
from ansible.plugins.connection import ConnectionBase

logger = getLogger(__name__)

try:
    from anta import __DEBUG__
    from anta.device import AntaDevice
    from anta.models import AntaCommand
    from anta.tools.misc import exc_to_str

    HAS_ANTA = True
except ImportError:
    HAS_ANTA = False
    # Next line to make ansible-test sanity happy
    AntaDevice = object


class AnsibleEOSDevice(AntaDevice):
    """
    Implementation of an AntaDevice using Ansible HttpApi plugin for EOS.
    """

    def __init__(self, name: str, connection: ConnectionBase, tags: list = None) -> None:
        super().__init__(name, tags)
        if hasattr(connection, "httpapi") and connection._network_os in ["arista.eos.eos", "eos"]:
            self._connection = connection
        else:
            raise AnsibleError(f"Error while instantiating {self.__class__.__name__}: The provided Ansible connection does not use EOS HttpApi plugin")

    def __eq__(self, other: object) -> bool:
        """
        Two AnsibleEOSDevice objects are equal if the hostname and the port are the same.

        This covers the use case of port forwarding when the host is localhost and the devices have different ports.
        """
        if not isinstance(other, AnsibleEOSDevice):
            return False
        return self._connection._options.host == other._connection._options.host and self._connection._options.port == other._connection._options.port

    def __rich_repr__(self):
        """
        Implements Rich Repr Protocol
        https://rich.readthedocs.io/en/stable/pretty.html#rich-repr-protocol
        """
        connection_vars = vars(self._connection)
        if "_defs" in connection_vars:
            del connection_vars["_defs"]
        yield from super().__rich_repr__()
        if __DEBUG__:
            yield "_connection", connection_vars

    async def collect(self, command: AntaCommand) -> AntaCommand:
        """
        Collect device command result using Ansible HttpApi connection plugin.

        Supports outformat 'json' and 'text' as output structure.

        Args:
            command: the command to collect

        Raises:
            AnsibleError: Raises an error if the send request failed.
        """
        try:
            commands = []

            if command.revision:
                commands.append({"cmd": command.command, "revision": command.revision})
            else:
                commands.append({"cmd": command.command})

            # Run the synchronous function send_request() in a separate thread to not block the asyncio event loop
            send_request = partial(self._connection.send_request, commands, version=command.version, output=command.ofmt)
            loop = get_event_loop()
            response = await loop.run_in_executor(None, send_request)

            # Save the command result
            command.output = loads(response) if command.ofmt == "json" else response
            logger.debug("%s: %s", self.name, command)

        except ConnectionError as e:
            message = f"Cannot connect to device {self.name}: {exc_to_str(e)}"
            logger.error(message)
            command.failed = e
            raise AnsibleError(message) from e
        except JSONDecodeError:
            # Even if the outformat is 'json' send_request() sometimes returns a non-valid JSON depending on the output content
            # https://github.com/ansible-collections/arista.eos/blob/main/plugins/httpapi/eos.py#L194
            command.output = {"messages": [response]}
        except Exception as e:
            message = f"Exception raised while collecting command '{command.command}' on device {self.name}"
            if __DEBUG__:
                logger.exception(message)
            else:
                logger.error("%s: %s", message, exc_to_str(e))
            command.failed = e
            logger.debug(command)
            raise AnsibleError(message) from e

    async def refresh(self) -> None:
        """
        Update attributes of an AnsibleEOSDevice instance.

        This coroutine must update the following attributes of AnsibleEOSDevice:
        - is_online: When a device IP is reachable and a port can be open
        - established: When a command execution succeeds
        - hw_model: The hardware model of the device

        Raises:
          AnsibleError: Raises an error if the get_device_info() failed.
        """
        logger.debug("Refreshing device %s", self.name)

        try:
            device_info = self._connection.get_device_info()
        except ConnectionError as e:
            message = f"Connection error raised while getting the device information: {exc_to_str(e)}"
            logger.error(message)
            raise AnsibleError(message) from e
        self.is_online = self._connection._connected
        if self.is_online:
            self.hw_model = device_info["network_os_model"]
        else:
            logger.warning("Could not connect to device %s", self.name)
        self.established = bool(self.is_online and self.hw_model)
