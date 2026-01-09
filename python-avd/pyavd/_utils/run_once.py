# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import threading
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import Any


class RunOnce:
    """
    Decorator to run a function only once.

    This is useful for functions that are called multiple times but should only run once.
    This only supports functions without a return value.
    This is thread-safe.
    """

    func: Callable[(...), None]
    has_run: bool
    lock: threading.Lock

    def __init__(self, func: Callable[(...), None]) -> None:
        """
        Initialize the RunOnce decorator.

        Args:
            func: The function to be executed only once.
        """
        self.func = func
        self.has_run = False
        self.lock = threading.Lock()

    def __call__(self, *args: Any, **kwargs: Any) -> None:
        """Execute the wrapped function only once, ignoring subsequent calls."""
        if not self.has_run:
            with self.lock:
                if not self.has_run:
                    self.has_run = True
                    self.func(*args, **kwargs)
