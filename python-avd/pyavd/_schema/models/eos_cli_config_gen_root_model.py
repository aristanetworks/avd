# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from .avd_model import AvdModel

if TYPE_CHECKING:
    from collections.abc import Mapping

    from typing_extensions import Self


class EosCliConfigGenRootModel(AvdModel):
    @classmethod
    def _from_dict(cls, data: Mapping) -> Self:
        """
        Returns a new instance loaded with the data from the given dict.

        Args:
            data: A mapping containing the EosDesigns input data to be loaded.

        """
        return super()._from_dict(data)
