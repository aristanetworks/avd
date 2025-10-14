# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
import warnings
from abc import abstractmethod
from collections.abc import Generator
from contextlib import contextmanager
from typing import Any, ClassVar, final

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase

from .log_config import AvdLoggingConfig, LoggerState, get_avd_log_level
from .log_handlers import AnsibleDisplayHandler, ContextFilter, SaveToResultHandler


class AvdActionPlugin(ActionBase):
    """Base class for AVD Ansible action plugins to provide common functionality."""

    _primary_logger_name: ClassVar[str] = "ansible_collections.arista.avd"
    _logging_config: ClassVar[AvdLoggingConfig] = AvdLoggingConfig()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the action plugin."""
        super().__init__(*args, **kwargs)
        self.result: dict[str, Any] = {}
        self.logger = logging.getLogger(self._primary_logger_name)

        # Enforce that the primary logger is always a target for configuration
        if self._primary_logger_name not in self._logging_config.target_loggers:
            msg = (
                f"The _primary_logger_name '{self._primary_logger_name}' must be included "
                f"in the _logging_config.target_loggers tuple for the plugin to work correctly."
            )
            raise ValueError(msg)

    @abstractmethod
    def main(self, task_vars: dict[str, Any]) -> None:
        """
        This method must be implemented by child plugins with their core logic.

        It will be called by the `run()` method implementation below.

        Update the `self.result` dictionary attribute in-place to return data to Ansible.
        """

    @final
    def run(self, tmp: Any = None, task_vars: dict[str, Any] | None = None) -> dict[str, Any]:
        """Ansible Action entry point."""
        if task_vars is None:
            task_vars = {}

        self.result.update(super().run(tmp, task_vars))
        del tmp  # tmp no longer has any effect

        # Prepare handlers, filters, and format based on logging config and task arguments
        temp_handlers: list[logging.Handler] = []
        if self._task.args.get("save_logs", False):
            temp_handlers.append(SaveToResultHandler(result_dict=self.result))
        if self._task.args.get("live_display", True):
            temp_handlers.append(AnsibleDisplayHandler())

        # Build the context data and log format string
        context_data: dict[str, Any] = {}
        format_parts: list[str] = []
        if self._logging_config.add_role_context:
            context_data["role_name"] = task_vars.get("ansible_role_name")
            format_parts.append("[%(role_name)s] -")
        if self._logging_config.add_hostname_context:
            context_data["hostname"] = task_vars.get("inventory_hostname")
            format_parts.append("<%(hostname)s>")

        format_parts.append("%(message)s")
        log_format = " ".join(format_parts)

        temp_filters: list[logging.Filter] = [ContextFilter(context_data)] if context_data else []

        try:
            # Use the context manager to apply changes and ensure cleanup
            with (
                warnings.catch_warnings(record=True) as captured_warnings,
                self._logging_context(temp_handlers=temp_handlers, temp_filters=temp_filters, log_format=log_format),
            ):
                # DeprecationWarning is ignored by default
                # NOTE: This will override PYTHONWARNINGS environment variable
                warnings.simplefilter("always", DeprecationWarning)

                # Run the plugin
                self.main(task_vars)

            # Process captured Python warnings and update the result object
            if captured_warnings:
                self.result.setdefault("deprecations", [])
                self.result.setdefault("warnings", [])
                for w in captured_warnings:
                    msg = str(w.message)
                    if issubclass(w.category, DeprecationWarning):
                        # AvdDeprecationWarning's are added from AvdSchemaTools with more context
                        # This is a catch-all for other deprecations
                        self.result["deprecations"].append({"msg": msg})
                    else:
                        # Catch-all for standard Python warnings from any library
                        self.result["warnings"].append(msg)

        except Exception as exc:
            # Recast errors as AnsibleActionFail
            # Ignoring Pyright since 'ansible_name' is not typed in Ansible world
            msg = f"Error during plugin '{self.ansible_name}' execution: '{exc}'"  # pyright: ignore[reportAttributeAccessIssue]
            raise AnsibleActionFail(msg) from exc
        else:
            return self.result

    @contextmanager
    def _logging_context(
        self,
        temp_handlers: list[logging.Handler],
        temp_filters: list[logging.Filter],
        log_format: str,
    ) -> Generator[None, None, None]:
        """
        Context manager to temporarily apply a logging configuration and guarantee restoration.

        It creates a "sandbox" for logging during a plugin execution. If defends against side effects
        from other tasks or plugins by saving the original state of each targeted loggers and restoring
        it on exit.

        Args:
            temp_handlers: A list of temporary handler instances to add to the loggers.
            temp_filters: A list of temporary filter instances to add to the handlers.
            log_format: The format string to apply to the temporary handlers.

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

        original_states: dict[str, LoggerState] = {}
        target_loggers = [logging.getLogger(name) for name in self._logging_config.target_loggers]

        for logger in target_loggers:
            # Save original state (level, handlers, propagation)
            original_states[logger.name] = LoggerState(level=logger.level, handlers=tuple(logger.handlers), propagate=logger.propagate)

            # Defend against lingering handlers from other plugins if not cleaned up
            logger.handlers.clear()

            # Disabling propagation to avoid duplicate logs in Ansible 'log_path' file
            logger.propagate = False

            # Apply new configuration
            desired_level = get_avd_log_level(logger.name)
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
                logger.setLevel(original_state.level)
                logger.handlers.extend(original_state.handlers)
                logger.propagate = original_state.propagate
