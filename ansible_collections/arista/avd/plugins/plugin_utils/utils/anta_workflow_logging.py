# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
from collections import defaultdict

from ansible.utils.display import Display

ANTA_LIBRARIES = ("anta", "asyncio", "asyncssh", "httpcore", "httpx")
"""Define ANTA-related library names for filtering."""


class AntaWorkflowFilter(logging.Filter):
    """
    ANTA workflow logging filter.

    Injects a unique ID into log records and filters ANTA library logs
    below WARNING level (for console output).
    """

    def __init__(self, unique_id: str) -> None:
        """
        Initialize the filter with a specific ID.

        Args:
          unique_id: Identifier for the current context (e.g., 'anta-workflow'
                     or 'anta-run-xxxxxxxx'). Added to all records.
        """
        super().__init__()
        self.unique_id = unique_id

    def filter(self, record: logging.LogRecord) -> bool:
        """
        Add `unique_id` to the record and filter logs.

        Filtering logic:
            - Allow all logs from non-ANTA libraries.
            - Allow logs from ANTA libraries ONLY if they are WARNING level or higher.

        Args:
          record: The log record to be filtered.

        Returns:
          bool: True if the record should be processed, False otherwise.
        """
        # Always inject the unique ID for context tracking
        record.unique_id = self.unique_id

        # Check if the log record originated from one of the defined ANTA libraries
        is_anta_library = any(record.name.startswith(name) for name in ANTA_LIBRARIES)

        return bool(not is_anta_library or (is_anta_library and record.levelno >= logging.WARNING))


class AntaWorkflowHandler(logging.Handler):
    """
    ANTA workflow logging handler.

    Route log records to Ansible Display based on level and track error/warning counts
    in a shared statistics dictionary.
    """

    def __init__(self, log_stats: defaultdict[str, dict[str, int]], display: Display | None = None) -> None:
        """
        Initialize the handler.

        Args:
          log_stats: Dictionary shared with the main plugin to store
                     {'error_count': int, 'warning_count': int} per unique_id.
          display: Optional Ansible Display instance. Retrieves singleton if None.
        """
        super().__init__()
        self.display = display or Display()
        self.log_stats = log_stats

    def emit(self, record: logging.LogRecord) -> None:
        """
        Process a log record.

        Formats the message (including unique_id), sends it to the appropriate
        Ansible Display method and increments error/warning counts in the log_stats
        dictionary.

        Args:
          record: The log record to be processed.
        """
        # Get the unique_id injected by the AntaLoggingFilter
        unique_id = getattr(record, "unique_id", "unknown")

        message = str(self._format_msg(record))

        if record.levelno >= logging.ERROR:
            self.log_stats[unique_id]["error_count"] += 1
            self.display.error(message, wrap_text=False)
        elif record.levelno == logging.WARNING:
            self.log_stats[unique_id]["warning_count"] += 1
            self.display.warning(message)
        elif record.levelno == logging.INFO:
            self.display.v(message)
        elif record.levelno == logging.DEBUG:
            self.display.vvv(message)

    def _format_msg(self, record: logging.LogRecord) -> str:
        """Format the log record message, prepending the unique_id if present."""
        base_message = self.format(record)
        return f"[{record.unique_id}] {base_message}" if hasattr(record, "unique_id") else base_message
