# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging

from ansible.utils.display import Display


class AntaWorkflowFilter(logging.Filter):
    """
    ANTA workflow logging filter.

    Injects a unique ID into log records for context tracking.
    """

    def __init__(self, unique_id: str) -> None:
        """
        Initialize the filter.

        Args:
          unique_id: Identifier for the current context (e.g., 'anta-workflow'
                     or 'anta-run-xxxxxxxx'). Added to all records.
        """
        super().__init__()
        self.unique_id = unique_id

    def filter(self, record: logging.LogRecord) -> bool:
        """
        Add `unique_id` to the record.

        Args:
          record: The log record to be processed.

        Returns:
          bool: Always True.
        """
        record.unique_id = self.unique_id
        return True


class AntaWorkflowHandler(logging.Handler):
    """
    ANTA workflow logging handler.

    Route log records to Ansible Display based on level and track errors in a
    boolean list.
    """

    def __init__(self, has_errors_ref: list[bool]) -> None:
        """
        Initialize the handler.

        Args:
          has_errors_ref: Mutable boolean list to track errors.
                          It's expected to be a list with one boolean element.
        """
        super().__init__()
        self.display = Display()
        self.has_errors_ref = has_errors_ref

    def emit(self, record: logging.LogRecord) -> None:
        """
        Process a log record.

        Formats the message (including unique_id) and sends it to the appropriate
        Ansible Display method. Also update the error boolean list when handling error
        logs and above.

        Args:
          record: The log record to be processed.
        """
        # Get the unique_id injected by the AntaLoggingFilter
        unique_id = getattr(record, "unique_id", "unknown")

        # Format the message including unique_id
        base_message = self.format(record)
        final_message = f"[{unique_id}] {base_message}"

        if record.levelno >= logging.ERROR:
            self.display.error(final_message, wrap_text=False)
            self.has_errors_ref[0] = True
        elif record.levelno == logging.WARNING:
            self.display.warning(final_message)
        elif record.levelno == logging.INFO:
            self.display.v(final_message)
        elif record.levelno == logging.DEBUG:
            self.display.vvv(final_message)
