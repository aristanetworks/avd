# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import MutableMapping

    from ._eos_designs.eos_designs_facts.schema import EosDesignsFacts
    from .api.schemas import AVDDesign, EOSConfig


def get_device_structured_config(
    hostname: str, inputs: AVDDesign | dict, avd_facts: dict[str, EosDesignsFacts], hostvars: MutableMapping | None = None, digital_twin: bool = False
) -> EOSConfig:
    """
    Build and return the AVD structured configuration for one device.

    Args:
        hostname:
            Hostname of device.
        inputs:
            AVDDesign instance or dictionary with the validated design inputs.
        avd_facts:
            Dictionary of avd_facts as returned from `pyavd.get_avd_facts`.
        hostvars:
            Per-device dictionaries with variables exposed to custom ip addressing or description logic.
            This is optional and only needed if custom python modules are used for descriptions or IP addressing.
        digital_twin:
            PREVIEW: Optional flag to enable digital-twin mode.

    Returns:
        Device structured configuration as an instance of EOSConfig.
    """
    from ._eos_designs.structured_config import get_structured_config  # noqa: PLC0415
    from .api.schemas import AVDDesign  # noqa: PLC0415

    if not isinstance(inputs, AVDDesign):
        inputs = AVDDesign._from_dict(inputs)

    return get_structured_config(
        hostname=hostname,
        inputs=inputs,
        all_facts=avd_facts,
        hostvars=hostvars,
        templar=None,
        digital_twin=digital_twin,
    )
