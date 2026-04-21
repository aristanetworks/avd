# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence


def json_path_to_string(json_path: Sequence[str | int]) -> str:
    path = ""
    for index, elem in enumerate(json_path):
        if isinstance(elem, int) or elem.isnumeric():
            path += f"[{elem}]"
        else:
            if index == 0:
                path += elem
                continue
            path += f".{elem}"
    return path
