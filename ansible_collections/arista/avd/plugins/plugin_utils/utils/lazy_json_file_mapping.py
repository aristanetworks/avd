# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import UserDict
from functools import cached_property
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pathlib import Path

    from .avd_file_handler import AVDFileHandler


class LazyJsonFileMapping(UserDict[str, Any]):
    """Present a JSON object as a mutable mapping without loading it until first access."""

    def __init__(self, file_handler: AVDFileHandler, file_path: Path) -> None:
        # Leave data unset so the cached property loads it on first access.
        self._file_handler = file_handler
        self._file_path = file_path

    @cached_property
    def data(self) -> dict[str, Any]:
        """Load and return the cached JSON object without copying it."""
        data = self._file_handler.load_json(self._file_path)
        if not isinstance(data, dict):
            msg = f"Expected a JSON object in '{self._file_path}'."
            raise TypeError(msg)
        return data
