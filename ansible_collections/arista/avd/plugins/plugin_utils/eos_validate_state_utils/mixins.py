# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from functools import cached_property
from ipaddress import ip_interface
from typing import Mapping

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get, get_item



class LoggingMixin:
    
    LOGGING_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

    def __init__(self):
        self.logger = self.get_logger()

    def get_logger(self):
        return logging.getLogger(__name__)
    
    def get_logging_level(self, level: str) -> int:
        return logging.getLevelName(level.upper())
    
    def check_logging_level(self, level: str):
        if level.upper() not in self.LOGGING_LEVELS:
            raise AristaAvdError("Invalid logging level. Please choose from DEBUG, INFO, WARNING, ERROR, CRITICAL.")
    
    def log_skip_message(
        self, message=None, key: str | None = None, value=None, key_path: str | None = None, is_missing: bool = True, logging_level: str = "INFO"
    ) -> None:
        """
        Logging function that logs the test being skipped appended to a formatted message based on the provided parameters.

        Args:
            message (Any | None): The message to be logged. If provided, it will be logged as is, ignoring other parameters.
            key (str | None): The key to be logged.
            value (Any | None): The expected value of the key. Must be provided when logging an invalid value.
            key_path (str | None): The key path in dot notation.
            is_missing (bool): Indicates whether the key is missing.
            logging_level (str): The logging level to use for the log message.
        """
        # Validate logging level
        self.check_logging_level(logging_level)

        # If message is provided, it will be logged as is, ignoring other parameters
        if message:
            log_msg = str(message)
        else:
            if key is None:
                raise AristaAvdError("Error creating the log message: Key argument is missing.")
            if value is None and is_missing is False:
                raise AristaAvdError("Error creating the log message: The key's value must be provided when logging an invalid value.")
            dot_notation = f"{key_path}.{key}" if key_path else f"{key}"
            msg_type = "is missing" if is_missing else f"!= '{value}'"
            log_msg = f"Key '{dot_notation}' {msg_type}."

        # Appending the skipped test
        log_msg += f" {self.__class__.__name__} is skipped."

        # Logging the message
        log_level = self.get_logging_level(logging_level)
        self.logger.log(log_level, log_msg)