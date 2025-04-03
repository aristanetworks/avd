# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging


class AntaLoggingFilter(logging.Filter):
    """Filter logs for ANTA and its underlying libraries."""

    _anta_libraries = ("anta", "asyncio", "asyncssh", "httpcore", "httpx")

    def __init__(self, has_warnings_ref: list[bool] | None = None, *, exclude: bool = True) -> None:
        """
        Initializes the filter.

        Args:
          has_warnings_ref: Reference to a boolean list to track if any warnings or above are logged.
          exclude: Whether to exclude ANTA logs or not.
        """
        super().__init__()
        self.exclude = exclude
        self.has_warnings_ref = has_warnings_ref

    def filter(self, record: logging.LogRecord) -> bool:
        """Filter logs based on whether they're from ANTA libraries."""
        is_anta_library = any(record.name.startswith(name) for name in self._anta_libraries)

        # Update the warning tracker if this is a warning or above from an ANTA library
        if self.has_warnings_ref is not None and is_anta_library and record.levelno >= logging.WARNING:
            self.has_warnings_ref[0] = True

        # If exclude=True, return True for non-ANTA logs
        # If exclude=False, return True for ANTA logs
        return not is_anta_library if self.exclude else is_anta_library
