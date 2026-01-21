# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import threading
from dataclasses import dataclass, field
from functools import wraps
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import Any


class RunOnceMethodStateHelper:
    """
    Helper base class for classes using @run_once_method decorator.

    Provides thread-safe per-method-per-instance state management.
    """

    _run_once_state: dict[str, RunOnceMethodState]
    """Per-method-per-instance state for run_once_method decorator."""

    _run_once_init_lock: threading.Lock
    """Lock for initializing the per-method state."""

    def __init__(self) -> None:
        self._run_once_state = {}
        self._run_once_init_lock = threading.Lock()

    def _get_run_once_state(self, method_name: str) -> RunOnceMethodState:
        """
        Get or Initialize the run-once state for a method.

        This is thread-safe.
        """
        # Fast path: use .get() to avoid race between 'in' check and access
        method_state = self._run_once_state.get(method_name)
        if method_state is not None:
            return method_state

        with self._run_once_init_lock:
            # Double-check inside lock
            method_state = self._run_once_state.get(method_name)
            if method_state is None:
                method_state = RunOnceMethodState()
                self._run_once_state[method_name] = method_state
            return method_state


@dataclass
class RunOnceMethodState:
    """Per-method-per-instance state for run_once_method decorator."""

    lock: threading.Lock = field(default_factory=threading.Lock)
    has_run: bool = False


def run_once(func: Callable[..., None]) -> Callable[..., None]:
    """
    Decorator to run a function only once.

    This is useful for functions that are called multiple times but should only run once.

    This only supports functions without a return value.
    If the function raises an Exception it will be raised on the first call. Subsequent calls will still be ignored.
    This is thread-safe.
    """
    has_run = False
    lock = threading.Lock()

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> None:
        """
        Wrap the function to only call it once.

        First we check if it was already run, and if so we return immediately.
        After that we acquire the lock to ensure only one thread can run the function.
        Since multiple threads could be waiting to acquire the lock, we need to check has_run again
        after acquiring the lock to ensure we only run the function once.
        """
        nonlocal has_run

        if has_run:
            return

        with lock:
            if has_run:
                return

            has_run = True
            func(*args, **kwargs)

    return wrapper


def run_once_method(method: Callable[..., None]) -> Callable[..., None]:
    """
    Decorator to run a method only once per instance.

    This is useful for methods that are called multiple times but should only run once.
    The class holding the decorated method must inherit from RunOnceMethodStateHelper.

    This only supports methods without a return value.
    If the method raises an Exception it will be raised on the first call. Subsequent calls will still be ignored.
    This is thread-safe.
    """
    method_name = method.__name__

    @wraps(method)
    def wrapper(instance: RunOnceMethodStateHelper, *args: Any, **kwargs: Any) -> None:
        """
        Wrap the method to only call it once per instance.

        Uses a dict attribute on the instance to store per-method state.
        """
        if not isinstance(instance, RunOnceMethodStateHelper):
            msg = f"Class '{type(instance)}' does not inherit from RunOnceMethodStateHelper."
            msg += " Make sure to use RunOnceMethodStateHelper as base class for your class before using @run_once_method."
            raise TypeError(msg)

        # Get or create per-method state
        method_state = instance._get_run_once_state(method_name)

        # Fast path: already run
        if method_state.has_run:
            return

        with method_state.lock:
            # Double-check after acquiring lock
            if method_state.has_run:
                return

            method_state.has_run = True
            method(instance, *args, **kwargs)

    return wrapper
