# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
from typing import Any

from ansible.utils.display import Display


class ContextFilter(logging.Filter):
    """A logging filter that injects a dictionary of context attributes into the log record."""

    def __init__(self, context: dict[str, Any]) -> None:
        """Initialize the filter."""
        super().__init__()
        self.context = context

    def filter(self, record: logging.LogRecord) -> bool:
        """Adds all keys from the context dict as attributes to the log record."""
        record.__dict__.update(self.context)
        return True


class AnsibleDisplayHandler(logging.Handler):
    """A handler to bridge Python logging to the Ansible Display object for screen output."""

    def __init__(self) -> None:
        """Initialize the handler."""
        super().__init__()
        self.display = Display()

    def emit(self, record: logging.LogRecord) -> None:
        """
        Process a log record and delegate it to the appropriate Ansible display method.

        Check for a 'color' attribute in the record to allow for explicit color overrides.
        """
        message = self.format(record)

        color = getattr(record, "color", None)
        if color:
            # If a color is explicitly provided, use it
            self.display.display(message, color=color)
            return

        # If no color is specified, map log levels to display methods
        if record.levelno >= logging.ERROR:
            self.display.error(message, wrap_text=False)
        elif record.levelno == logging.WARNING:
            self.display.warning(message)
        elif record.levelno == logging.INFO:
            self.display.v(message)
        elif record.levelno == logging.DEBUG:
            self.display.vvv(message)


class SaveToResultHandler(logging.Handler):
    """A handler that saves warning and error logs to the Ansible result dictionary."""

    def __init__(self, result_dict: dict[str, Any]) -> None:
        """Initialize the handler."""
        super().__init__()
        self.result = result_dict
        self.result.setdefault("logs", {"warnings": [], "errors": []})

    def emit(self, record: logging.LogRecord) -> None:
        """Save formatted warning and error messages to the result dictionary."""
        message = self.format(record)
        if record.levelno >= logging.ERROR:
            self.result["logs"]["errors"].append(message)
        elif record.levelno >= logging.WARNING:
            self.result["logs"]["warnings"].append(message)
