# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import threading
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
        if has_run:
            return

        with lock:
            if has_run:
                return

            has_run = True
            func(*args, **kwargs)

    return wrapper
