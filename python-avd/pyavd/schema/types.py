# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import Iterator

from annotated_types import BaseMetadata, GroupedMetadata
from pydantic import BeforeValidator


class StrConvert(GroupedMetadata):
    def __init__(
        self,
        convert_types: tuple[type] | None = None,
        to_lower: bool = False,
    ):
        self.convert_types = convert_types
        self.to_lower = to_lower

    def __iter__(self) -> Iterator[BaseMetadata]:
        if self.to_lower:
            yield BeforeValidator(lambda v: v.lower() if isinstance(v, str) else v)
        if self.convert_types is not None:
            yield BeforeValidator(lambda v: str(v) if isinstance(v, self.convert_types) else v)


class IntConvert(GroupedMetadata):
    def __init__(
        self,
        convert_types: tuple[type] | None = None,
    ):
        self.convert_types = convert_types

    def __iter__(self) -> Iterator[BaseMetadata]:
        if self.convert_types is not None:
            yield BeforeValidator(lambda v: int(v) if isinstance(v, self.convert_types) else v)


class BoolConvert(GroupedMetadata):
    def __init__(
        self,
        convert_types: tuple[type] | None = None,
    ):
        self.convert_types = convert_types

    def __iter__(self) -> Iterator[BaseMetadata]:
        if self.convert_types is not None:
            yield BeforeValidator(lambda v: bool(v) if isinstance(v, self.convert_types) else v)
