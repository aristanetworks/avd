# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import warnings
from typing import Any

from pyavd._errors import AvdDeprecationWarning


class DeprecatedDict(dict):
    _done: bool
    _message: str

    def __init__(self, *args: Any, _message: str, **kwargs: Any) -> None:
        self._done = False
        self._message = _message
        super().__init__(*args, **kwargs)

    def __getitem__(self, key: Any) -> Any:
        if not self._done:
            warnings.warn(self._message, AvdDeprecationWarning, stacklevel=2)
            self._done = True
        return super().__getitem__(key)
