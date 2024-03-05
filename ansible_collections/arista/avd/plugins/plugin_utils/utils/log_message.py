# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from typing import Any

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError

LOGGER = logging.getLogger(__name__)
LOGGING_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


def log_message(
    key: str,
    value: Any = None,
    key_path: str | None = None,
    message: str | None = None,
    log_level: str = "INFO",
    *,
    key_missing: bool = True,
    prepend_message: bool = False,
) -> None:
    """Log the test being skipped appended to a formatted message based on the provided parameters.

    Args:
    ----
        message (Any | None): The message to be logged. If provided, it will be logged as is, ignoring other parameters.
        key (str | None): The key to be logged.
        value (Any | None): The expected value of the key. Must be provided when logging an invalid value.
        key_path (str | None): The key path in dot notation.
        is_missing (bool): Indicates whether the key is missing.
        logging_level (str): The logging level to use for the log message.
    """
    # Validate logging level
    if log_level.upper() not in LOGGING_LEVELS:
        raise AristaAvdError("Invalid logging level. Please choose from DEBUG, INFO, WARNING, ERROR, CRITICAL.")

    # Check if value is provided when logging an invalid value
    if value is None and key_missing is False:
        raise AristaAvdError("Error creating the log message: The key's value must be provided when logging an invalid value.")

    dot_notation = f"{key_path}.{key}" if key_path else f"{key}"
    msg_type = "is missing" if key_missing else f"!= '{value}'"
    log_msg = f"Key '{dot_notation}' {msg_type}."

    # Append or prepend the optional message
    if message:
        log_msg = f"{message}. {log_msg}" if prepend_message else f"{log_msg} {message}."

    # Logging the message
    log_level = logging.getLevelName(log_level.upper())
    LOGGER.log(log_level, log_msg)
