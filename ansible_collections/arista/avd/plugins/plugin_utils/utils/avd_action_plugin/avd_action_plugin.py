# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
import warnings
from abc import abstractmethod
from contextlib import contextmanager
from logging.handlers import QueueHandler
from multiprocessing import get_context
from typing import TYPE_CHECKING, Any, ClassVar, final

from ansible.plugins.action import ActionBase

from ansible_collections.arista.avd.plugins.plugin_utils.utils.raise_action_fail import raise_action_fail

from .log_config import AVDLoggingConfig, LoggerState, get_avd_log_level
from .log_handlers import AnsibleDisplayHandler, ContextFilter, ErrorTrackingHandler, LogContextFilter, LoggingOutcome, SaveToResultHandler, log_context
from .multiprocessing_logging import AVDQueueListener, WarningEvent, forward_worker_warnings

if TYPE_CHECKING:
    from collections.abc import Generator


def _handle_captured_warnings(captured_warnings: list[warnings.WarningMessage] | list[WarningEvent], result: dict[str, Any]) -> None:
    """Add captured Python warnings to the appropriate lists in the Ansible result."""
    if not captured_warnings:
        return

    result.setdefault("deprecations", [])
    result.setdefault("warnings", [])
    for warning in captured_warnings:
        message = str(warning.message)
        is_deprecation = warning.is_deprecation if isinstance(warning, WarningEvent) else issubclass(warning.category, DeprecationWarning)
        if not is_deprecation:
            # Catch-all for standard Python warnings from any library
            result["warnings"].append(message)
            continue

        deprecation: dict[str, Any] = {"msg": message}
        metadata = warning if isinstance(warning, WarningEvent) else warning.message
        if (date := getattr(metadata, "date", None)) is not None:
            deprecation.update(date=date, collection_name="arista.avd")
        elif (version := getattr(metadata, "version", None)) is not None:
            deprecation.update(version=version, collection_name="arista.avd")
        result["deprecations"].append(deprecation)


class AVDActionPlugin(ActionBase):
    """Base class for AVD Ansible action plugins to provide common functionality."""

    _primary_logger_name: ClassVar[str] = "ansible_collections.arista.avd"
    _logging_config: ClassVar[AVDLoggingConfig] = AVDLoggingConfig()

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

    def _handle_logging_outcome(self, logging_outcome: LoggingOutcome) -> None:
        """Allow subclasses to apply plugin-specific policy after all log records are handled."""

    @final
    def run(self, tmp: Any = None, task_vars: dict[str, Any] | None = None) -> dict[str, Any]:
        """Ansible Action entry point."""
        if task_vars is None:
            task_vars = {}

        self.result.update(super().run(tmp, task_vars))
        del tmp  # tmp no longer has any effect

        # Prepare handlers, filters, and format based on logging config and task arguments
        logging_outcome = LoggingOutcome() if self._logging_config.track_log_errors else None
        temp_handlers: list[logging.Handler] = []
        if logging_outcome is not None:
            temp_handlers.append(ErrorTrackingHandler(logging_outcome))
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
        if self._logging_config.log_context is not None:
            format_parts.append("[%(avd_log_context)s]")

        format_parts.append("%(message)s")
        log_format = " ".join(format_parts)

        temp_filters: list[logging.Filter] = [ContextFilter(context_data)] if context_data else []
        producer_filters: list[logging.Filter] = [LogContextFilter()] if self._logging_config.log_context is not None else []
        worker_warnings: list[WarningEvent] = []

        try:
            # Use the context manager to apply changes and ensure cleanup
            with (
                warnings.catch_warnings(record=True) as captured_warnings,
                log_context(self._logging_config.log_context),
                self._logging_context(
                    temp_handlers=temp_handlers,
                    temp_filters=temp_filters,
                    producer_filters=producer_filters,
                    log_format=log_format,
                    worker_warnings=worker_warnings,
                ),
            ):
                # DeprecationWarning is ignored by default
                # NOTE: This will override PYTHONWARNINGS environment variable
                warnings.simplefilter("always", DeprecationWarning)

                # Run the plugin
                self.main(task_vars)

            if logging_outcome is not None:
                # QueueListener.stop() has drained multiprocessing records before this hook runs.
                # Logging observation is centralized here, while each plugin owns any result policy.
                self._handle_logging_outcome(logging_outcome)
            _handle_captured_warnings(captured_warnings, self.result)
            _handle_captured_warnings(worker_warnings, self.result)

        except Exception as exc:
            # Recast errors as AnsibleActionFail
            msg = f"Error during plugin '{self.ansible_name}' execution: {exc}"
            raise_action_fail(msg, exc)

        return self.result

    @contextmanager
    def _logging_context(
        self,
        temp_handlers: list[logging.Handler],
        temp_filters: list[logging.Filter],
        producer_filters: list[logging.Filter],
        log_format: str,
        worker_warnings: list[WarningEvent],
    ) -> Generator[None, None, None]:
        """
        Context manager to temporarily apply a logging configuration and guarantee restoration.

        It creates a "sandbox" for logging during a plugin execution. If defends against side effects
        from other tasks or plugins by saving the original state of each targeted loggers and restoring
        it on exit.

        Args:
            temp_handlers: A list of temporary handler instances to add to the loggers.
            temp_filters: A list of temporary filter instances to add to the handlers.
            producer_filters: Filters applied before records enter a multiprocessing queue.
            log_format: The format string to apply to the temporary handlers.
            worker_warnings: The parent-side list collecting transported Python warnings.

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

        log_queue = None
        queue_listener = None
        configured_handlers = temp_handlers
        if self._logging_config.use_multiprocessing_queue:
            # The action plugins using queue logging create their process pools with the
            # explicit "fork" context, so the queue must come from the same context.
            log_queue = get_context("fork").Queue()
            # Even without log sinks, the queue is needed for worker Python warnings.
            # Do not transport ordinary logs when there are no handlers to consume them.
            configured_handlers = [QueueHandler(log_queue)] if temp_handlers else []
            queue_listener = AVDQueueListener(log_queue, *temp_handlers, warning_events=worker_warnings)

        for configured_handler in configured_handlers:
            for producer_filter in producer_filters:
                configured_handler.addFilter(producer_filter)

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
            for configured_handler in configured_handlers:
                logger.addHandler(configured_handler)

        active_exception: BaseException | None = None
        listener_started = False
        try:
            if queue_listener is not None:
                queue_listener.start()
                listener_started = True
            with forward_worker_warnings(log_queue):
                yield
        except BaseException as exc:
            active_exception = exc
            raise
        finally:
            for logger in target_loggers:
                # The temporary handlers are the only one present, so clear them
                logger.handlers.clear()

            cleanup_exceptions: list[Exception] = []
            if listener_started and queue_listener is not None:
                try:
                    # QueueListener.stop() places a sentinel after all queued records
                    # and waits for the listener thread, so records are drained before
                    # the action returns.
                    queue_listener.stop()
                except Exception as exc:  # pragma: no cover - defensive cleanup
                    cleanup_exceptions.append(exc)

            if log_queue is not None:
                try:
                    log_queue.close()
                    log_queue.join_thread()
                except Exception as exc:  # pragma: no cover - defensive cleanup
                    cleanup_exceptions.append(exc)

            for logger in target_loggers:
                # Restore the original state from before we started
                original_state = original_states[logger.name]
                logger.setLevel(original_state.level)
                logger.handlers.extend(original_state.handlers)
                logger.propagate = original_state.propagate

            if cleanup_exceptions and active_exception is None:
                raise cleanup_exceptions[0]
