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
        device = self.extra.get("device", "-")
        test = self.extra.get("test", "-")
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
    PEER_UNAVAILABLE = "{caller} skipped - Peer {peer} not in fabric or not deployed"
    PEER_INTERFACE_NO_IP = "{caller} skipped - Peer {peer} interface {peer_interface} has no IP"

    # Interface state messages
    INTERFACE_SHUTDOWN = "{caller} skipped - Interface is shutdown"
    INTERFACE_USING_DHCP = "{caller} skipped - DHCP interface"
    INTERFACE_IS_SUBINTERFACE = "{caller} skipped - Subinterface"
    INTERFACE_VALIDATION_DISABLED = "{caller} skipped - validate_state or validate_lldp disabled"
    INTERFACE_NO_IP = "{caller} skipped - No IP address configured"

    # STUN-specific messages
    STUN_NO_CLIENT_INTERFACE = "path group {caller} skipped - No STUN client interfaces found"
    STUN_NO_STATIC_PEERS = "path group {caller} skipped - No static peers configured"

    # Input generation messages
    INPUT_NONE_FOUND = "skipped - No inputs available"
    INPUT_NO_DATA_MODEL = "skipped - Data model {caller} not found"
    INPUT_MISSING_FIELDS = "{caller} skipped - Missing required fields: {fields}"
    INPUT_RENDERING = "rendering inputs with {caller}"
    INPUT_RENDERED = "rendered input dict: {inputs}"
