# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import threading
from dataclasses import dataclass
from functools import wraps
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import Any


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

        if not has_run:
            with lock:
                if not has_run:
                    has_run = True
                    func(*args, **kwargs)

    return wrapper


def run_once_method(method: Callable[..., None]) -> Callable[..., None]:
    """
    Decorator to run a method only once per instance.

    This is useful for methods that are called multiple times but should only run once.

    This only supports methods without a return value.
    If the method raises an Exception it will be raised on the first call. Subsequent calls will still be ignored.
    This is thread-safe.
    """
    common_lock = threading.Lock()
    """Common lock used when creating the per instance locks."""

    instance_infos: dict[int, RunOnceInstanceInfo] = {}
    """
    Per instance run_once details for this method.
    """

    @wraps(method)
    def wrapper(instance: Any, *args: Any, **kwargs: Any) -> None:
        """
        Wrap the method to only call it once.

        First we check if it was already run, and if so we return immediately.
        After that we acquire the lock to ensure only one thread can run the method.
        Since multiple threads could be waiting to acquire the lock, we need to check has_run again
        after acquiring the lock to ensure we only run the method once.
        """
        nonlocal instance_infos

        instance_id = id(instance)
        if instance_id not in instance_infos:
            with common_lock:
                # Checking again in case it was set while waiting for the lock.
                if instance_id not in instance_infos:
                    instance_infos[instance_id] = RunOnceInstanceInfo(lock=threading.Lock(), has_run=False)

        instance_info = instance_infos[instance_id]

        if not instance_info.has_run:
            with instance_info.lock:
                # Checking again in case it was set while waiting for the lock.
                if not instance_info.has_run:
                    instance_info.has_run = True
                    method(instance, *args, **kwargs)

    return wrapper


@dataclass
class RunOnceInstanceInfo:
    lock: threading.Lock
    has_run: bool
