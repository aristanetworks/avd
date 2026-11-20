# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
import os
import warnings
from contextlib import contextmanager
from dataclasses import dataclass
from logging.handlers import QueueListener
from typing import TYPE_CHECKING, TextIO

from .log_handlers import LogContextFilter

if TYPE_CHECKING:
    from collections.abc import Generator
    from multiprocessing.queues import Queue


@dataclass(frozen=True)
class WarningEvent:
    """Picklable worker warning data, without serializing custom warning objects."""

    message: str
    is_deprecation: bool
    version: str | None = None
    date: str | None = None


class AVDQueueListener(QueueListener):
    """Dispatch worker log records and Python warnings in the parent process."""

    def __init__(self, queue: Queue, *handlers: logging.Handler, warning_events: list[WarningEvent]) -> None:
        """Initialize the sinks for log records and warning events."""
        super().__init__(queue, *handlers, respect_handler_level=True)
        self.warning_events = warning_events

    def handle(self, record: object) -> None:
        """Only send LogRecords to logging handlers; collect warning events separately."""
        match record:
            case logging.LogRecord():
                super().handle(record)
            case WarningEvent():
                self.warning_events.append(record)
            case _:
                diagnostic = logging.LogRecord(
                    name=__name__,
                    level=logging.WARNING,
                    pathname=__file__,
                    lineno=0,
                    msg="Ignoring unexpected item of type '%s' in the AVD multiprocessing queue.",
                    args=(type(record).__name__,),
                    exc_info=None,
                )
                LogContextFilter().filter(diagnostic)
                # Dispatch directly: logging through a configured logger would enqueue
                # another record, potentially after the listener's shutdown sentinel.
                super().handle(diagnostic)


@contextmanager
def forward_worker_warnings(queue: Queue | None) -> Generator[None, None, None]:
    """Keep parent warning capture unchanged and forward warnings from forked workers."""
    if queue is None:
        yield
        return

    parent_pid = os.getpid()
    original_showwarning = warnings.showwarning

    def showwarning(
        message: Warning | str,
        category: type[Warning],
        filename: str,
        lineno: int,
        file: TextIO | None = None,
        line: str | None = None,
    ) -> None:
        if os.getpid() == parent_pid:
            original_showwarning(message, category, filename, lineno, file, line)
            return

        version = getattr(message, "version", None)
        date = getattr(message, "date", None)
        queue.put_nowait(
            WarningEvent(
                message=str(message),
                is_deprecation=issubclass(category, DeprecationWarning),
                version=str(version) if version is not None else None,
                date=str(date) if date is not None else None,
            )
        )

    warnings.showwarning = showwarning
    try:
        yield
    finally:
        warnings.showwarning = original_showwarning
