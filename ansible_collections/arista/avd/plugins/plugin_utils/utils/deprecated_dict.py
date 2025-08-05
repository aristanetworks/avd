# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ansible.utils.display import Display


class DeprecatedDict(dict):
    _ansible_display: Display
    _done: bool
    _message: str

    def __init__(self, *args: Any, _display: Display, _message: str, **kwargs: Any) -> None:
        self._ansible_display = _display
        self._done = False
        self._message = _message
        super().__init__(*args, **kwargs)

    def get(self, key: Any, default: Any = None) -> Any:
        if not self._done:
            self._ansible_display.deprecated(
                msg=self._message,
                version="6.0.0",
                collection_name="arista.avd",
                removed=False,
            )
            self._done = True
        return super().get(key, default)

    def __getitem__(self, key: Any) -> Any:
        if not self._done:
            self._ansible_display.deprecated(
                msg=self._message,
                version="6.0.0",
                collection_name="arista.avd",
                removed=False,
            )
            self._done = True
        return super().__getitem__(key)
