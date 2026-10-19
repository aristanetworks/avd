# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import warnings
from typing import Any

from pyavd._errors import AvdDeprecationWarning


class DeprecatedDict(dict):
    _deprecated_dict_key: str
    _done: set[str]
    _new_keys: dict[str, str]
    _remove_in_version: str

    def __init__(self, *args: Any, _deprecated_dict_key: str, _new_keys: dict[str, str], _remove_in_version: str, **kwargs: Any) -> None:
        self._deprecated_dict_key = _deprecated_dict_key
        self._done = set()
        self._new_keys = _new_keys
        self._remove_in_version = _remove_in_version
        super().__init__(*args, **kwargs)

    def _warn(self, key: str) -> None:
        if key in self._done or key not in self._new_keys:
            return

        path = [self._deprecated_dict_key, key]
        new_key = self._new_keys[key]

        deprecation_warning = AvdDeprecationWarning(path, new_key, remove_in_version=self._remove_in_version)
        warnings.warn(deprecation_warning, stacklevel=2)
        self._done.add(key)

    def __getitem__(self, key: Any) -> Any:
        self._warn(key)
        return super().__getitem__(key)

    def get(self, key: Any, default: Any = None) -> Any:
        self._warn(key)
        return super().get(key, default)
