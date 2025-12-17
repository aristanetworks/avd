# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._eos_designs.eos_designs_facts.schema import EosDesignsFacts
    from .api.schemas import Design, EOSConfig


def get_device_structured_config(hostname: str, inputs: Design | dict, avd_facts: dict[str, EosDesignsFacts], digital_twin: bool = False) -> EOSConfig:
    """
    Build and return the AVD structured configuration for one device.

    Args:
        hostname: Hostname of device.
        inputs: Design instance or dictionary with the validated design inputs.
        avd_facts: Dictionary of avd_facts as returned from `pyavd.get_avd_facts`.
        digital_twin: PREVIEW: Optional flag to enable digital-twin mode.

    Returns:
        Device Structured Configuration as an instance of EOSConfig.
    """
    from ._eos_designs.structured_config import get_structured_config  # noqa: PLC0415
    from .api.schemas import Design  # noqa: PLC0415

    if not isinstance(inputs, Design):
        inputs = Design._from_dict(inputs)

    return get_structured_config(
        hostname=hostname,
        inputs=inputs,
        all_facts=avd_facts,
        templar=None,
        digital_twin=digital_twin,
    )
