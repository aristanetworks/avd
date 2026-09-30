# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from pyavd._schema.models.avd_model import AvdModel

from .consolidator import PrunedAVDDesign, consolidate_avd_design
from .models import ConsolidatedData

if TYPE_CHECKING:
    from collections.abc import Mapping

    from pyavd._eos_designs.schema import EosDesigns as AVDDesign


class ConsolidatedAVDDesign(AvdModel):
    """Serializable artifact containing pruned inputs and device-local consolidated data."""

    _fields: ClassVar[dict] = {
        "inputs": {"type": PrunedAVDDesign},
        "consolidated": {"type": ConsolidatedData},
    }
    inputs: PrunedAVDDesign
    consolidated: ConsolidatedData

    @classmethod
    def _from_avd_design(cls, device_name: str, avd_design: AVDDesign | Mapping | ConsolidatedAVDDesign) -> ConsolidatedAVDDesign:
        from pyavd._eos_designs.schema import EosDesigns as AVDDesign  # noqa: PLC0415

        if isinstance(avd_design, ConsolidatedAVDDesign):
            return avd_design

        if not isinstance(avd_design, AVDDesign):
            avd_design = AVDDesign._from_dict(avd_design)

        pruned_inputs, consolidated = consolidate_avd_design(device_name, avd_design)
        return cls(inputs=pruned_inputs, consolidated=consolidated)
