# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Logging utilities used by PyAVD for ANTA."""

from __future__ import annotations

import string
from contextlib import contextmanager
from enum import Enum
from logging import LoggerAdapter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator


class TestLoggerAdapter(LoggerAdapter):
    """
    Custom LoggerAdapter used to add device, test, and an optional context information to log messages.

    It uses the same constructor as the standard LoggerAdapter and `extra` should have the following structure:

    ```python
    extra = {
        "device": "<device_name>",
        "test": "<test_name>",
        "context": "<test_context>",  # Optional
    }
    ```

    When logging a message, the logger will format the `LogMessage` Enum message using the kwargs passed to the logger,
    and prepend the message with the device and test names, and optionally the context: `<device> test context message`.
    """

    def process(self, msg: LogMessage, kwargs: dict) -> tuple[str, dict]:
        """Process the message and kwargs before logging."""
        # Keep the extra dict in kwargs to pass it to the formatter if needed (following the standard LoggerAdapter behavior)
        kwargs["extra"] = self.extra

        # Extract the device, test, and context from extra
        device = self.extra["device"]
        test = self.extra["test"]
        context = self.extra.get("context")

        prefix = f"<{device}> {test}"
        if context:
            prefix += f" {context}"

        # Format the LogMessage using the provided kwargs and extract the fields name from the message string
        fields = [field_name for _, field_name, _, _ in string.Formatter().parse(msg.value) if field_name is not None]
        msg = msg.value.format(**kwargs)

        # Removing the fields name from kwargs to preserve standard logging kwargs only that should always be passed through (e.g. exc_info, stack_info, etc.)
        for field in fields:
            kwargs.pop(field, None)

        return f"{prefix} {msg}", kwargs

    @contextmanager
    def context(self, context: str) -> Generator[TestLoggerAdapter, None, None]:
        """Temporarily add context to the logger."""
        original_extra = dict(self.extra)
        try:
            self.extra["context"] = context
            yield self
        finally:
            self.extra = original_extra


class LogMessage(Enum):
    """
    Log message templates for test input generation.

    Adapter adds: `<device> [test] (context):`
    """

    # Peer-related messages
    PEER_UNAVAILABLE = "{identity} skipped - Peer {peer} not in fabric or not deployed"
    PEER_INTERFACE_NOT_FOUND = "{interface} skipped - peer {peer} interface {peer_interface} not found"
    PEER_INTERFACE_USING_DHCP = "{interface} skipped - peer {peer} interface {peer_interface} using DHCP"
    PEER_INTERFACE_UNNUMBERED = "{interface} skipped - peer {peer} interface {peer_interface} using IP unnumbered"
    PEER_INTERFACE_SHUTDOWN = "{interface} skipped - peer {peer} interface {peer_interface} is shutdown"

    # Interface state messages
    INTERFACE_SHUTDOWN = "{interface} skipped - Interface is shutdown"
    INTERFACE_USING_DHCP = "{interface} skipped - DHCP interface"
    INTERFACE_IS_SUBINTERFACE = "{interface} skipped - Subinterface"
    INTERFACE_VALIDATION_DISABLED = "{interface} skipped - validate_state or validate_lldp disabled"
    INTERFACE_NO_IP = "{interface} skipped - No IP address configured"
    INTERFACE_UNNUMBERED = "{interface} skipped - IP unnumbered interface"

    # WAN-specific messages
    PATH_GROUP_NO_STUN_INTERFACE = "path group {path_group} skipped - No STUN client interfaces found"
    PATH_GROUP_NO_LOCAL_INTERFACES = "path group {path_group} skipped - No local interfaces found"
    PATH_GROUP_NO_STATIC_PEERS = "path group {path_group} skipped - No static peers configured"
    NO_STATIC_PEERS = "skipped - No static peers configured in any path groups"

    # Input generation messages
    INPUT_NONE_FOUND = "skipped - No inputs available"
    INPUT_NO_DATA_MODELS = "skipped - Data models {data_models} not found"
    INPUT_MISSING_FIELDS = "{identity} skipped - Missing required fields: {fields}"
