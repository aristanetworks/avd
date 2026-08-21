# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from pyavd._eos_designs.schema import EosDesigns as AVDDesign
from pyavd._schema.models.avd_model import AvdModel
from pyavd._schema.models.eos_designs_root_model import EosDesignsRootModel

from .models import ConsolidatedData

if TYPE_CHECKING:
    from collections.abc import Mapping


class PrunedAVDDesign(AVDDesign):
    """AVD Design inputs already normalized and pruned during consolidation."""

    @classmethod
    # pylint: disable-next=arguments-differ
    def _from_dict(cls, data: Mapping) -> PrunedAVDDesign:  # pyright: ignore[reportIncompatibleMethodOverride]
        """Load inputs without repeating dynamic-key and custom-structured-configuration preprocessing."""
        return super(EosDesignsRootModel, cls)._from_dict(data)


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

        from .consolidator import consolidate_avd_design  # noqa: PLC0415

        if isinstance(avd_design, ConsolidatedAVDDesign):
            return avd_design

        if not isinstance(avd_design, AVDDesign):
            avd_design = AVDDesign._from_dict(avd_design)

        inputs = avd_design._cast_as(PrunedAVDDesign)
        consolidated = consolidate_avd_design(device_name, inputs)
        return cls(inputs=inputs, consolidated=consolidated)
