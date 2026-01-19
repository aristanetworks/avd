# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Mapping, MutableMapping

    from ._eos_designs.eos_designs_facts.schema import EosDesignsFacts
    from .api.pool_manager import PoolManager
    from .api.schemas import AVDDesign


def get_avd_facts(
    all_inputs: Mapping[str, AVDDesign | Mapping],
    all_hostvars: Mapping[str, MutableMapping] | None = None,
    pool_manager: PoolManager | None = None,
    digital_twin: bool = False,
) -> dict[str, EosDesignsFacts]:
    """
    Build avd_facts using the AVD eos_designs_facts logic.

    Variables should be validated and loaded into instances of the AVDDesign class first.

    Note! No support for inline templating or jinja templates for descriptions or ip addressing

    Args:
        all_inputs:
            A dictionary where keys are hostnames and values are the AVDDesign instance per device.
            Supporting dicts as well for backwards compatibility.
        all_hostvars:
            Raw hostvars exposed to custom python logic for each device.
            This is optional and only needed if custom python modules are used for descriptions or IP addressing.
        pool_manager:
            PREVIEW: Optional instance of pyavd.avd.PoolManager or subclass hereof,
            implementing ".get_assignment(pool_type: PoolType, shared_utils: SharedUtils)".
            Used for dynamic ID allocations using the "pool_manager" feature.
        digital_twin:
            PREVIEW: Optional flag to enable digital-twin mode.

    Returns:
        Dictionary with various internal "facts" keyed by device hostname.

        The full dict must be given as argument to `pyavd.get_device_structured_config`.
    """
    from ._eos_designs.eos_designs_facts.get_facts import get_facts  # noqa: PLC0415

    return get_facts(all_inputs=all_inputs, all_hostvars=all_hostvars, pool_manager=pool_manager, digital_twin=digital_twin)
