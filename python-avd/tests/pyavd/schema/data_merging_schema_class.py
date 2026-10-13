# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import ClassVar

from pyavd._schema.models.avd_indexed_list import AvdIndexedList
from pyavd._schema.models.avd_list import AvdList
from pyavd._schema.models.avd_model import AvdModel


class DataMergingTestSchema(AvdModel):
    """Minimal model tree used to test AVD model merging and combining."""

    class SomeIndexedListItem(AvdModel):
        _fields: ClassVar[dict] = {"name": {"type": str}, "some_int": {"type": int}}

        name: str
        some_int: int | None

    class SomeIndexedList(AvdIndexedList[str, SomeIndexedListItem]):
        _primary_key: ClassVar[str] = "name"

    SomeIndexedList._item_type = SomeIndexedListItem

    class SomeList(AvdList[int]):
        pass

    SomeList._item_type = int

    class SomeDict(AvdModel):
        _fields: ClassVar[dict] = {"some_nested_key": {"type": str}}

        some_nested_key: str | None

    _fields: ClassVar[dict] = {
        "some_indexed_list": {"type": SomeIndexedList},
        "some_list": {"type": SomeList},
        "some_dict": {"type": SomeDict},
        "some_key": {"type": int},
    }
    _allow_other_keys: ClassVar[bool] = True

    some_indexed_list: SomeIndexedList
    some_list: SomeList
    some_dict: SomeDict
    some_key: int | None
