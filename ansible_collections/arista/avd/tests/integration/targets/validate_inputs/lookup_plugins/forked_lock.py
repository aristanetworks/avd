# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Test lookup exposing lock state inherited by a forked process."""

from __future__ import annotations

import os
from threading import Event, Lock, Thread

from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase

_IMPORT_PID = os.getpid()
_LOCK = Lock()
_LOCK_ACQUIRED = Event()
_LOCK_HOLDER_STARTED = False


def _hold_lock() -> None:
    """Hold the lock for the lifetime of the lookup plugin process."""
    with _LOCK:
        _LOCK_ACQUIRED.set()
        Event().wait()


class LookupModule(LookupBase):
    """Return the input term unless running in a fork inheriting a held lock."""

    def run(self, terms: list[str], variables: dict | None = None, **kwargs: object) -> list[str]:  # noqa: ARG002
        """Prime the lock in the importing process and detect inherited lock state in a fork."""
        global _LOCK_HOLDER_STARTED  # noqa: PLW0603

        if os.getpid() == _IMPORT_PID:
            if not _LOCK_HOLDER_STARTED:
                _LOCK_HOLDER_STARTED = True
                Thread(target=_hold_lock, daemon=True).start()
                if not _LOCK_ACQUIRED.wait(timeout=2):
                    msg = "Test lookup failed to prime its lock."
                    raise AnsibleError(msg)
            return terms

        if not _LOCK.acquire(timeout=2):
            msg = "Lookup inherited a held lock from the parent process."
            raise AnsibleError(msg)
        _LOCK.release()
        return terms
