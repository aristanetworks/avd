# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
import warnings
from collections.abc import Callable, Generator
from contextlib import contextmanager
from functools import wraps
from typing import Any

from ansible.errors import AnsibleActionFail
from ansible.utils.display import Display

from .avd_action_plugin import AvdActionPlugin

AVD_GLOBAL_DISPLAY_HANDLER_NAME = "avd_global_display_handler"

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

INTERNAL_LIB_LOGGERS = ["ansible_collections.arista.avd", "pyavd", "schema_tools", "anta"]


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

    def __init__(self, display: Display | None = None) -> None:
        """Initialize the handler."""
        super().__init__()
        self.display = display if display is not None else Display()

    def emit(self, record: logging.LogRecord) -> None:
        """Process a log record."""
        message = self.format(record)
        if record.levelno >= logging.ERROR:
            self.display.error(message, wrap_text=False)
        elif record.levelno == logging.WARNING:
            self.display.warning(message)
        elif record.levelno == logging.INFO:
            self.display.v(message)
        elif record.levelno == logging.DEBUG:
            self.display.vvv(message)


class SaveToResultHandler(logging.Handler):
    """A handler that saves log records to the Ansible result dictionary."""

    def __init__(self, result_dict: dict) -> None:
        super().__init__()
        self.result = result_dict
        self.result.setdefault("logs", {"warnings": [], "errors": []})

    def emit(self, record: logging.LogRecord) -> None:
        message = self.format(record)
        if record.levelno >= logging.ERROR:
            self.result["logs"]["errors"].append(message)
        elif record.levelno >= logging.WARNING:
            self.result["logs"]["warnings"].append(message)


@contextmanager
def avd_logging_context(
    logger_names: list[str], temp_handlers: list[logging.Handler], temp_filters: list[logging.Filter], log_format: str, *, remove_global_handler: bool
) -> Generator[None, None, None]:
    """Context manager to temporarily modify loggers, ensuring all changes are reverted."""
    loggers = [logging.getLogger(name) for name in logger_names]

    # Collect all handlers from target loggers
    existing_handlers: list[logging.Handler] = []
    for logger in loggers:
        existing_handlers.extend(logger.handlers)

    # We will modify all existing handlers plus any new temporary handlers
    all_handlers_to_modify = set(existing_handlers + temp_handlers)

    # Keep track of what we add/remove so we can revert it
    loggers_with_new_handlers: list[tuple[logging.Logger, logging.Handler]] = []
    handlers_with_new_filters: list[tuple[logging.Handler, logging.Filter]] = []
    loggers_with_removed_handlers: list[tuple[logging.Logger, logging.Handler]] = []
    original_formatters = {handler: handler.formatter for handler in all_handlers_to_modify}

    try:
        new_formatter = logging.Formatter(log_format)

        # Remove the global handler from loggers if requested
        if remove_global_handler:
            for logger in loggers:
                for handler in list(logger.handlers):
                    if handler.name == AVD_GLOBAL_DISPLAY_HANDLER_NAME:
                        loggers_with_removed_handlers.append((logger, handler))
                        logger.removeHandler(handler)

        removed_handlers = {h for _l, h in loggers_with_removed_handlers}

        # Apply new formatter and filters to all targeted handlers
        for handler in all_handlers_to_modify:
            if handler in removed_handlers:
                continue

            handler.setFormatter(new_formatter)
            for temp_filter in temp_filters:
                handler.addFilter(temp_filter)
                handlers_with_new_filters.append((handler, temp_filter))

        # Add new temporary handlers to loggers
        for logger in loggers:
            for temp_handler in temp_handlers:
                logger.addHandler(temp_handler)
                loggers_with_new_handlers.append((logger, temp_handler))
        yield

    finally:
        for logger, temp_handler in loggers_with_new_handlers:
            logger.removeHandler(temp_handler)

        for handler, temp_filter in handlers_with_new_filters:
            if temp_filter in handler.filters:
                handler.removeFilter(temp_filter)

        for logger, removed_handler in loggers_with_removed_handlers:
            logger.addHandler(removed_handler)

        for handler, original_formatter in original_formatters.items():
            handler.setFormatter(original_formatter)


def avd_logging(add_hostname_context: bool = False, add_role_context: bool = False, target_loggers: list[str] | None = None) -> Callable:
    """Decorator for an AVD action plugin 'run_plugin' method to augment loggers."""

    def decorator(func: Callable) -> Callable:
        if func.__name__ != "run_plugin":
            msg = "The '@avd_logging' decorator can only be used on the 'run_plugin' method."
            raise TypeError(msg)

        @wraps(func)
        def wrapper(self: AvdActionPlugin, *args: Any, **kwargs: Any) -> Any:
            # Get task_vars from positional or keyword arguments
            task_vars = args[0] if args else kwargs.get("task_vars", {})
            loggers_to_target = target_loggers or ["ansible_collections.arista.avd"]

            # Prepare handlers, filters, and format based on knobs and task arguments
            temp_handlers = []
            if self._task.args.get("save_logs", False):
                temp_handlers.append(SaveToResultHandler(result_dict=self.result))

            # Build the context data and log format string dynamically
            context_data, format_parts = {}, []
            if add_role_context:
                context_data["role_name"] = task_vars.get("ansible_role_name")
                format_parts.append("[%(role_name)s] -")
            if add_hostname_context:
                context_data["hostname"] = task_vars.get("inventory_hostname")
                format_parts.append("<%(hostname)s>")

            format_parts.append("%(message)s")
            log_format = " ".join(format_parts)

            temp_filters = [ContextFilter(context_data)] if context_data else []

            remove_global_handler = not self._task.args.get("live_display", True)

            # Use the context manager to apply changes and ensure cleanup
            with (
                warnings.catch_warnings(record=True) as captured_warnings,
                avd_logging_context(
                    logger_names=loggers_to_target,
                    temp_handlers=temp_handlers,
                    temp_filters=temp_filters,
                    log_format=log_format,
                    remove_global_handler=remove_global_handler,
                ),
            ):
                try:
                    final_result = func(self, *args, **kwargs)
                except BaseException as exc:
                    # Recast errors as AnsibleActionFail
                    msg = f"Error during plugin execution: {exc}"
                    raise AnsibleActionFail(msg) from exc

                # Process captured Python warnings and update the result object
                if captured_warnings:
                    final_result.setdefault("deprecations", [])
                    final_result.setdefault("warnings", [])
                    for w in captured_warnings:
                        msg = str(w.message)
                        if issubclass(w.category, DeprecationWarning):
                            # AvdDeprecationWarning's are added from AvdSchemaTools with more context
                            # This is a catch-all for other deprecations
                            final_result["deprecations"].append({"msg": msg})
                        else:
                            # Catch-all for standard Python warnings from any library
                            final_result["warnings"].append(msg)

            return final_result

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
    levels = ANSIBLE_VERBOSITY_MAPPING[effective_verbosity].copy()

    # Expand the 'external_libs' key into individual logger entries
    external_level = levels.pop("external_libs")
    for logger_name in EXTERNAL_LIB_LOGGERS:
        levels[logger_name] = external_level

    return levels


def init_avd_logging(display: Display | None = None) -> None:
    """Initialize AVD logging."""
    display = display if display is not None else Display()

    log_level_map = map_verbosity_to_log_levels(display.verbosity)
    handler = AnsibleDisplayHandler(display)
    handler.set_name(AVD_GLOBAL_DISPLAY_HANDLER_NAME)

    for logger_name, level in log_level_map.items():
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)
        # Avoid adding duplicate handlers if this function is ever called more than once
        if not any(h.name == AVD_GLOBAL_DISPLAY_HANDLER_NAME for h in logger.handlers):
            logger.addHandler(handler)
