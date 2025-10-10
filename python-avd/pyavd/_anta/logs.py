# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Logging utilities used by PyAVD for ANTA."""

from __future__ import annotations

import string
from collections.abc import Generator
from contextlib import contextmanager
from enum import Enum
from logging import Logger, LoggerAdapter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator, MutableMapping


class TestLoggerAdapter(LoggerAdapter[Logger]):
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

    def process(self, msg: LogMessage | str, kwargs: MutableMapping[str, object]) -> tuple[str, MutableMapping[str, object]]:
        """Process the message and kwargs before logging."""
        # Ensure we always have a dict[str, object]
        extra: dict[str, object] = dict(self.extra or {})
        kwargs["extra"] = extra

        # Safely extract info
        device = str(extra.get("device", "unknown"))
        test = str(extra.get("test", "unknown"))
        context = extra.get("context")

        prefix = f"<{device}> {test}"
        if isinstance(context, str):
            prefix += f" {context}"

        # Support both LogMessage enums and plain strings
        msg_value: str = msg.value if isinstance(msg, LogMessage) else str(msg)

        # Find format field names
        fields = [field_name for _, field_name, _, _ in string.Formatter().parse(msg_value) if field_name is not None]

        # Try formatting; if fails, keep raw text
        try:
            formatted_msg = msg_value.format(**kwargs)
        except Exception:
            formatted_msg = msg_value

        # Remove used fields to not interfere with logging kwargs
        for field in fields:
            kwargs.pop(field, None)

        return f"{prefix} {formatted_msg}", kwargs

    @contextmanager
    def context(self, context: str) -> Generator[TestLoggerAdapter, None, None]:
        """Temporarily add context to the logger."""
        original_extra = dict(getattr(self, "extra", {}) or {})
        try:
            mutable_extra = dict(original_extra)
            mutable_extra["context"] = context
            self.extra = mutable_extra
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
    IPv6_STATIC_PEER = "static peer {peer} skipped - ANTA not support IPv6 static peer"

    # Input generation messages
    INPUT_NONE_FOUND = "skipped - No inputs available"
    INPUT_NO_DATA_MODELS = "skipped - Data models {data_models} not found"
    INPUT_MISSING_FIELDS = "{identity} skipped - Missing required fields: {fields}"
