# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
from collections.abc import Callable, Generator
from contextlib import contextmanager
from functools import wraps
from typing import Any

from ansible.utils.display import Display

from .avd_action_plugin import AvdActionPlugin

ANSIBLE_VERBOSITY_MAPPING: dict[int, dict[str, int]] = {
    0: {  # Verbosity: 0
        "ansible_collections.arista.avd": logging.WARNING,
        "pyavd": logging.WARNING,
        "schema_tools": logging.WARNING,
        "anta": logging.WARNING,
        "external_libs": logging.WARNING,
    },
    1: {  # Verbosity: -v
        "ansible_collections.arista.avd": logging.INFO,
        "pyavd": logging.INFO,
        "schema_tools": logging.INFO,
        "anta": logging.WARNING,
        "external_libs": logging.WARNING,
    },
    2: {  # Verbosity: -vv
        "ansible_collections.arista.avd": logging.INFO,
        "pyavd": logging.DEBUG,
        "schema_tools": logging.DEBUG,
        "anta": logging.WARNING,
        "external_libs": logging.WARNING,
    },
    3: {  # Verbosity: -vvv
        "ansible_collections.arista.avd": logging.DEBUG,
        "pyavd": logging.DEBUG,
        "schema_tools": logging.DEBUG,
        "anta": logging.INFO,
        "external_libs": logging.WARNING,
    },
    4: {  # Verbosity: -vvvv
        "ansible_collections.arista.avd": logging.DEBUG,
        "pyavd": logging.DEBUG,
        "schema_tools": logging.DEBUG,
        "anta": logging.DEBUG,
        "external_libs": logging.WARNING,
    },
    5: {  # Verbosity: -vvvvv
        "ansible_collections.arista.avd": logging.DEBUG,
        "pyavd": logging.DEBUG,
        "schema_tools": logging.DEBUG,
        "anta": logging.DEBUG,
        "external_libs": logging.INFO,
    },
    6: {  # Verbosity: -vvvvvv
        "ansible_collections.arista.avd": logging.DEBUG,
        "pyavd": logging.DEBUG,
        "schema_tools": logging.DEBUG,
        "anta": logging.DEBUG,
        "external_libs": logging.DEBUG,
    },
}

# Ignoring hpack logger from cv_workflow, too noisy
EXTERNAL_LIB_LOGGERS = ["asyncio", "httpcore", "httpx", "requests", "urllib3"]


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
    """Ansible display handler."""

    def __init__(self) -> None:
        """Initialize the handler."""
        super().__init__()
        self.display = Display()

    def emit(self, record: logging.LogRecord) -> None:
        """Process a log record."""
        message = self.format(record)
        if record.levelno >= logging.ERROR:
            self.display.error(message, wrap_text=False)
        elif record.levelno == logging.WARNING:
            self.display.warning(message, wrap_text=False)
        elif record.levelno == logging.INFO:
            self.display.v(message)
        elif record.levelno == logging.DEBUG:
            self.display.vvv(message)


@contextmanager
def avd_logging_manager(
    logger_names: list[str], handlers: list[logging.Handler], filters: list[logging.Filter], log_format: str | None = None
) -> Generator[None, None, None]:
    """Context manager to temporarily add handlers/filters and set a formatter on all handlers associated with the target loggers."""
    # Find all unique handlers currently on the target loggers
    existing_handlers: list[logging.Handler] = []
    for name in logger_names:
        existing_handlers.extend(logging.getLogger(name).handlers)

    # We will modify all existing handlers plus any new temporary handlers
    all_handlers_to_modify = set(existing_handlers + handlers)

    # Save original formatters to restore them later
    original_formatters = {handler: handler.formatter for handler in all_handlers_to_modify}

    # Keep track of what we add so we can remove it
    loggers_with_new_handlers: list[tuple[logging.Logger, logging.Handler]] = []
    handlers_with_new_filters: list[tuple[logging.Handler, logging.Filter]] = []

    try:
        new_formatter = logging.Formatter(log_format) if log_format else None

        # Apply new formatter and filters to all targeted handlers
        for handler in all_handlers_to_modify:
            if new_formatter:
                handler.setFormatter(new_formatter)
            for temp_filter in filters:
                handler.addFilter(temp_filter)
                handlers_with_new_filters.append((handler, temp_filter))

        # Add new temporary handlers to loggers
        for name in logger_names:
            logger = logging.getLogger(name)
            for temp_handler in handlers:
                logger.addHandler(temp_handler)
                loggers_with_new_handlers.append((logger, temp_handler))
        yield

    finally:
        # Remove temporary handlers from the loggers
        for logger, temp_handler in loggers_with_new_handlers:
            logger.removeHandler(temp_handler)

        # Restore original formatters and remove temporary filters
        for handler in all_handlers_to_modify:
            handler.setFormatter(original_formatters[handler])
            for _handler, temp_filter in handlers_with_new_filters:
                if temp_filter in handler.filters:
                    handler.removeFilter(temp_filter)


def avd_logging(add_hostname_context: bool = False, add_role_context: bool = False, target_loggers: list[str] | None = None) -> Callable:
    """Decorator for an action plugin to augment existing loggers."""

    def decorator(func: Callable) -> Callable:
        if func.__name__ != "run_plugin":
            msg = "The '@avd_logging' decorator can only be used on the 'run_plugin' method."
            raise TypeError(msg)

        @wraps(func)
        def wrapper(self: AvdActionPlugin, *args: Any, **kwargs: Any) -> Any:
            # Get task_vars from positional or keyword arguments
            task_vars = args[0] if args else kwargs.get("task_vars", {})
            loggers_to_target = target_loggers or ["ansible_collections.arista.avd"]

            # Prepare context data and format string based on knobs
            context_data = {}
            format_parts = []

            if add_role_context:
                context_data["role_name"] = task_vars.get("ansible_role_name")
                format_parts.append("[%(role_name)s] -")

            if add_hostname_context:
                context_data["hostname"] = task_vars.get("inventory_hostname")
                format_parts.append("<%(hostname)s>")

            if format_parts:
                format_parts.append("%(message)s")
            final_format_string = " ".join(format_parts)

            temp_handlers = []
            temp_filters = [ContextFilter(context_data)] if context_data else []

            # Use the context manager function to apply and then clean up the changes
            with avd_logging_manager(logger_names=loggers_to_target, handlers=temp_handlers, filters=temp_filters, log_format=final_format_string):
                return func(self, *args, **kwargs)

        return wrapper

    return decorator


def map_verbosity_to_log_levels(verbosity: int) -> dict[str, int]:
    """
    Maps an Ansible verbosity level to a dictionary of logger names and their corresponding Python logging levels.

    Args:
        verbosity: The Ansible verbosity level, as an integer.

    Returns:
        A dictionary where keys are logger names and values are logging level constants.
    """
    # If the level is higher than the max defined key (7), fall back to the highest defined level (6)
    max_defined_verbosity = max(ANSIBLE_VERBOSITY_MAPPING.keys())
    effective_verbosity = min(verbosity, max_defined_verbosity)

    # Get the base log levels from the mapping
    levels = ANSIBLE_VERBOSITY_MAPPING[effective_verbosity]

    # Expand the 'external_libs' key into individual logger entries
    external_level = levels.pop("external_libs")
    for logger_name in EXTERNAL_LIB_LOGGERS:
        levels[logger_name] = external_level

    return levels


def init_avd_logging() -> None:
    """Initialize AVD logging."""
    display = Display()
    verbosity = display.verbosity

    log_level_map = map_verbosity_to_log_levels(verbosity)
    handler = AnsibleDisplayHandler()

    for logger_name, level in log_level_map.items():
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)
        logger.addHandler(handler)
