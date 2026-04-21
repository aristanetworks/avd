# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from .avd_model import AvdModel
from .input_path import InputPath

if TYPE_CHECKING:
    from collections.abc import Mapping

    from typing_extensions import Self


class EosCliConfigGenRootModel(AvdModel):
    @classmethod
    def _from_dict(cls, data: Mapping, data_source: InputPath | None = None) -> Self:
        """
        Returns a new instance loaded with the data from the given dict.

        Args:
            data: A mapping containing the EosDesigns input data to be loaded.
            data_source: An InputPath for this EosCliConfigGenRootModel instance.
        """
        return super()._from_dict(data, data_source=data_source or InputPath())
