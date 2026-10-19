# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
from collections.abc import Generator
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass
from typing import Any

from ansible.utils.display import Display

_LOG_CONTEXT: ContextVar[str | None] = ContextVar("avd_log_context", default=None)
_PROCESS_LOG_CONTEXT: str | None = None


@contextmanager
def log_context(value: str | None) -> Generator[None, None, None]:
    """Set task-local and process-fallback log context for the duration of the context manager."""
    global _PROCESS_LOG_CONTEXT  # noqa: PLW0603

    previous_process_context = _PROCESS_LOG_CONTEXT
    _PROCESS_LOG_CONTEXT = value
    token = _LOG_CONTEXT.set(value)
    try:
        yield
    finally:
        _LOG_CONTEXT.reset(token)
        _PROCESS_LOG_CONTEXT = previous_process_context


@dataclass
class LoggingOutcome:
    """Mutable outcome populated while an action plugin's log records are handled."""

    has_errors: bool = False


class ErrorTrackingHandler(logging.Handler):
    """Track whether an error-level record was handled without deciding task status."""

    def __init__(self, logging_outcome: LoggingOutcome) -> None:
        """Initialize the handler with the outcome to update."""
        super().__init__(level=logging.ERROR)
        self.logging_outcome = logging_outcome

    def emit(self, record: logging.LogRecord) -> None:  # noqa: ARG002
        """Record that an error-level log record was handled."""
        self.logging_outcome.has_errors = True


class LogContextFilter(logging.Filter):
    """Inject the process-local log context before a record enters a multiprocessing queue."""

    def filter(self, record: logging.LogRecord) -> bool:
        """Add the active log context to the record."""
        context = _LOG_CONTEXT.get()
        # Standard CPython threads do not inherit ContextVar values by default.
        # Python 3.14 can opt in with Thread(context=...), while free-threaded
        # builds inherit the caller's context by default.
        # The process fallback preserves context for those records, matching the old
        # fixed child-process logging filter used by the ANTA workflow.
        record.avd_log_context = _PROCESS_LOG_CONTEXT if context is None else context
        return True


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
        """Process a log record and delegate it to the appropriate Ansible display method."""
        message = self.format(record)

        if record.levelno >= logging.ERROR:
            self.display.error(message, wrap_text=False)
        elif record.levelno == logging.WARNING:
            self.display.warning(message)
        elif record.levelno == logging.INFO:
            self.display.v(message)
        elif record.levelno == logging.DEBUG:
            # Logger levels enforce component-specific thresholds; -vv is the earliest DEBUG level.
            self.display.vv(message)


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
