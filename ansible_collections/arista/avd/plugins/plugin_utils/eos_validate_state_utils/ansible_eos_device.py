# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from asyncio import get_event_loop
from functools import partial
from json import JSONDecodeError, loads
from logging import getLogger
from typing import TYPE_CHECKING, Generator
from urllib.error import HTTPError

from ansible.errors import AnsibleConnectionFailure
from ansible.module_utils.connection import ConnectionError

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError

logger = getLogger(__name__)

REQUIRED_ANTA_VERSION = "v0.14.0"
"""This is temporary until the ANTA mode is out of preview and the `anta` Python library requirement is added to
the AVD repository's `requirements.txt` file. This constant and the condition below must be removed once the requirement is added."""

try:
    from anta import __version__ as anta_version

    if anta_version != REQUIRED_ANTA_VERSION:
        raise AristaAvdError(message=f"AVD requires 'anta' Python library version {REQUIRED_ANTA_VERSION}, found {anta_version}")
    from anta import __DEBUG__
    from anta.device import AntaDevice
    from anta.logger import anta_log_exception

    HAS_ANTA = True
except ImportError:
    HAS_ANTA = False
    # Next line to make ansible-test sanity happy
    AntaDevice = object
except TypeError as e:
    # Known bug with Python 3.9.7 and Pydantic `conint`, impacting ANTA. Issue: https://github.com/arista-netdevops-community/anta/issues/557
    if "Interval() takes no arguments" in str(e):
        msg = (
            "The ANTA testing framework, utilized in the AVD eos_validate_state role, has identified a compatibility issue with Python 3.9.x. "
            "We recommend trying a different Python version; 3.9.13 has been confirmed to work, or consider upgrading to version 3.10 or newer.\n"
            "For further assistance or to report your Python version, please visit the AVD and ANTA GitHub repositories:\n"
            "https://github.com/aristanetworks/avd/\n"
            "https://github.com/arista-netdevops-community/anta"
        )
        raise AristaAvdError(msg) from e
    else:
        # If the TypeError is not related to the known bug, raise it to avoid silencing other issues
        raise

if TYPE_CHECKING:
    from ansible.plugins.connection import ConnectionBase
    from anta.models import AntaCommand

ANSIBLE_EOS_PLUGIN_NAME = "ansible_collections.arista.eos.plugins.httpapi.eos"


class AnsibleEOSDevice(AntaDevice):
    """Implementation of an AntaDevice using Ansible HttpApi plugin for EOS."""

    def __init__(self, name: str, connection: ConnectionBase, tags: list | None = None, *, check_mode: bool = False) -> None:
        """Initialize an instance of the AnsibleEOSDevice class.

        Args:
        ----
            name (str): Name of the AnsibleEOSDevice instance.
            connection (ConnectionBase): An instance of Ansible ConnectionBase. It must utilize the EOS HttpApi plugin to manage the device's connection.
            tags (list, optional): A list of tags associated with the device. Defaults to None.
            check_mode (bool, optional): If True, initializes the class in check mode. Defaults to False.

        Attributes:
        ----------
            check_mode (bool): Flag indicating if the class is operating in check mode.
            _connection (ConnectionBase): An instance of ConnectionBase using the EOS HttpApi plugin for device connection management.

        Raises:
        ------
            AristaAvdError: Raised if ANTA is not imported or if the provided Ansible connection does not use the EOS HttpApi plugin.
        """
        if not HAS_ANTA:
            raise AristaAvdError(message="AVD could not import the required 'anta' Python library")

        super().__init__(name, tags, disable_cache=False)
        self.check_mode = check_mode
        # In check_mode we don't care that we cannot connect to the device
        if self.check_mode or (plugin_name := connection._sub_plugin.get("name")) == ANSIBLE_EOS_PLUGIN_NAME:
            self._connection = connection
        else:
            raise AristaAvdError(message=f"The provided Ansible connection does not use EOS HttpApi plugin: {plugin_name}")

    @property
    def _keys(self) -> tuple:
        """Keys used to implement hashing and equality for an AntaDevice instance."""
        return (self._connection._options.get("host"), self._connection._options.get("use_ssl"), self._connection._options.get("network_os"))

    def __rich_repr__(self) -> Generator:
        """Implement Rich Repr Protocol."""
        connection_vars = vars(self._connection)
        if "_defs" in connection_vars:
            del connection_vars["_defs"]
        yield from super().__rich_repr__()
        if __DEBUG__:
            yield "_connection", connection_vars

    async def _collect(self, command: AntaCommand) -> None:
        """Collect device command result using Ansible HttpApi connection plugin.

        Supports outformat 'json' and 'text' as output structure.

        Args:
        ----
            command (AntaCommand): The command to collect.

        If there is an exception while collecting the command, the exception will be propagated
        and handled in ANTA. That means ANTA will set the test result to 'error', the play will
        continue and the test will be marked as FAIL in the eos_validate_state report.
        """
        if self.check_mode:
            logger.info("_collect was called in check_mode, doing nothing")
            return
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

        except JSONDecodeError:
            # Even if the outformat is 'json' send_request() sometimes returns a non-valid JSON depending on the output content
            # https://github.com/ansible-collections/arista.eos/blob/main/plugins/httpapi/eos.py#L194
            command.output = {"messages": [response]}

        except Exception as e:
            message = f"Command '{command.command}' failed"
            command.failed = e
            logger.debug(command)
            msg = f"{message}: {e!s}"
            raise e.__class__(msg) from e

    async def refresh(self) -> None:
        """Update attributes of an AnsibleEOSDevice instance.

        This coroutine must update the following attributes of AnsibleEOSDevice:
        - is_online: When a device IP is reachable and a port can be open
        - established: When a command execution succeeded
        - hw_model: The hardware model of the device

        On `get_device_info()` failure:
        - The exception is caught and logged locally
        - The exception won't be propagated to ANTA
        - The task will fail per the logger handler and the play for the device will stop
        """
        logger.debug("Refreshing device %s", self.name)
        if self.check_mode:
            logger.info("Refresh was called in check_mode, doing nothing")
            return

        try:
            device_info = self._connection.get_device_info()
        except (AnsibleConnectionFailure, HTTPError) as e:
            message = "Failed to connect to device"
            anta_log_exception(e, message, logger)
        except ConnectionError as e:
            message = "Error while getting the device information"
            anta_log_exception(e, message, logger)
        else:
            self.is_online = self._connection.connected
            self.hw_model = device_info["network_os_model"]

        self.established = bool(self.is_online and self.hw_model)
