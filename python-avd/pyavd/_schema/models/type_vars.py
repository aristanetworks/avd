# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeVar

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence

    from .avd_base import AvdBase
    from .avd_indexed_list import AvdIndexedList
    from .avd_list import AvdList
    from .avd_model import AvdModel

    AvdDataClass = AvdModel | AvdList[Any] | AvdIndexedList[Any, Any]
    AvdListItem = str | int | bool | AvdDataClass
    LoadDumpData = Sequence[Any] | Mapping[str, Any]
else:
    AvdDataClass = object
    AvdListItem = object
    LoadDumpData = object

T = TypeVar("T")
T_AvdBase = TypeVar("T_AvdBase", bound="AvdBase")
T_AvdModel = TypeVar("T_AvdModel", bound="AvdModel")
T_AvdIndexedList = TypeVar("T_AvdIndexedList", bound="AvdIndexedList[Any, Any]")
T_AvdList = TypeVar("T_AvdList", bound="AvdList[Any]")
T_AvdDataClass = TypeVar("T_AvdDataClass", bound=AvdDataClass)
T_PrimaryKey = TypeVar("T_PrimaryKey", int, str)
T_LoadDumpType = TypeVar("T_LoadDumpType", bound=LoadDumpData)
T_ItemType = TypeVar("T_ItemType", bound=AvdListItem)
