# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections.abc import Iterator, MutableMapping
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pathlib import Path

    from .avd_file_handler import AVDFileHandler


class LazyJsonFileMapping(MutableMapping[str, Any]):
    """Present a JSON object as a mutable mapping without loading it until first access."""

    def __init__(self, file_handler: AVDFileHandler, file_path: Path) -> None:
        self._file_handler = file_handler
        self._file_path = file_path
        self._data: dict[str, Any] | None = None

    def _load(self) -> dict[str, Any]:
        if self._data is None:
            data = self._file_handler.load_json(self._file_path)
            if not isinstance(data, dict):
                msg = f"Expected a JSON object in '{self._file_path}'."
                raise TypeError(msg)
            self._data = data

        return self._data

    def __getitem__(self, key: str) -> Any:
        return self._load()[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self._load()[key] = value

    def __delitem__(self, key: str) -> None:
        del self._load()[key]

    def __iter__(self) -> Iterator[str]:
        return iter(self._load())

    def __len__(self) -> int:
        return len(self._load())
