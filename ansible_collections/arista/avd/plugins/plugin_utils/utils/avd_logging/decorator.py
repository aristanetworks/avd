# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
import warnings
from collections.abc import Callable, Generator
from contextlib import contextmanager
from functools import wraps
from typing import Any

from ansible.utils.display import Display

from ansible_collections.arista.avd.plugins.plugin_utils.utils import AvdActionPlugin

from .config import get_avd_log_level
from .handlers import AnsibleDisplayHandler, ContextFilter, SaveToResultHandler


def avd_logging(
    add_hostname_context: bool = False,
    add_role_context: bool = False,
    target_loggers: list[str] | None = None,
    display: Display | None = None,
) -> Callable:
    """
    Decorator for AvdActionPlugin 'run_plugin' method to provide a managed logging environment.

    This decorator orchestrates the setup and teardown of logging for the duration of a plugin execution.

    Args:
        add_hostname_context: If True, injects the 'inventory_hostname' into log records.
        add_role_context: If True, injects the 'ansible_role_name' into log records.
        target_loggers: A list of logger names to configure. Defaults to ["ansible_collections.arista.avd"].
        display: An optional, pre-existing Ansible Display object. Primarily used for testing.
    """
    display = display or Display()

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
            if self._task.args.get("live_display", True):
                temp_handlers.append(AnsibleDisplayHandler(display))

            # Build the context data and log format string
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

            # Use the context manager to apply changes and ensure cleanup
            with (
                warnings.catch_warnings(record=True) as captured_warnings,
                avd_logging_context(
                    logger_names=loggers_to_target, temp_handlers=temp_handlers, temp_filters=temp_filters, log_format=log_format, verbosity=display.verbosity
                ),
            ):
                # DeprecationWarning is ignored by default
                warnings.simplefilter("always", DeprecationWarning)

                # Run the plugin
                final_result = func(self, *args, **kwargs)

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


@contextmanager
def avd_logging_context(
    logger_names: list[str],
    temp_handlers: list[logging.Handler],
    temp_filters: list[logging.Filter],
    log_format: str,
    verbosity: int,
) -> Generator[None, None, None]:
    """
    Context manager to temporarily apply a logging configuration and guarantee restoration.

    It creates a "sandbox" for logging during a plugin execution. If defends against side effects
    from other tasks or plugins by saving the original state of each targeted loggers and restoring
    it on exit.

    Args:
        logger_names: A list of logger names to configure.
        temp_handlers: A list of temporary handler instances to add to the loggers.
        temp_filters: A list of temporary filter instances to add to the handlers.
        log_format: The format string to apply to the temporary handlers.
        verbosity: The Ansible verbosity level, used to calculate the logging level.

    Yields:
        None, after the logging environment has been configured.
    """
    # Prepare the formatter and apply it to the temporary handlers
    formatter = logging.Formatter(log_format)
    for temp_handler in temp_handlers:
        temp_handler.setFormatter(formatter)
        # Add all temporary filters
        for temp_filter in temp_filters:
            temp_handler.addFilter(temp_filter)

    original_states = {}
    target_loggers = [logging.getLogger(name) for name in logger_names]

    for logger in target_loggers:
        # Save original state (level, handlers, propagation)
        original_states[logger.name] = {"level": logger.level, "handlers": list(logger.handlers), "propagate": logger.propagate}
        # Defend against lingering handlers from other plugins if not cleaned up
        logger.handlers.clear()

        # Disabling propagation to avoid duplicate logs in Ansible 'log_path' file
        logger.propagate = False

        # Apply new configuration
        desired_level = get_avd_log_level(logger.name, verbosity)
        logger.setLevel(desired_level)
        for temp_handler in temp_handlers:
            logger.addHandler(temp_handler)

    try:
        yield
    finally:
        for logger in target_loggers:
            # The temporary handlers are the only one present, so clear them
            logger.handlers.clear()

            # Restore the original state from before we started
            original_state = original_states[logger.name]
            logger.setLevel(original_state["level"])
            logger.handlers.extend(original_state["handlers"])
            logger.propagate = original_state["propagate"]
