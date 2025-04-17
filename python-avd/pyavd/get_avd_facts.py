# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts
    from pyavd.api.pool_manager import PoolManager


def get_avd_facts(all_inputs: dict[str, dict], pool_manager: PoolManager | None = None) -> dict[str, EosDesignsFacts]:
    """
    Build avd_facts using the AVD eos_designs_facts logic.

    Variables should be converted and validated according to AVD `eos_designs` schema first using `pyavd.validate_inputs`.

    Note! No support for inline templating or jinja templates for descriptions or ip addressing

    Args:
        all_inputs: A dictionary where keys are hostnames and values are dictionaries of input variables per device.
            ```python
            {
                "<hostname1>": dict,
                "<hostname2>": dict,
                ...
            }
            ```
        pool_manager: PREVIEW: Optional instance of pyavd.avd.PoolManager or subclass hereof,
            implementing ".get_assignment(pool_type: PoolType, shared_utils: SharedUtils)".
            Used for dynamic ID allocations using the "pool_manager" feature.

    Returns:
        Dictionary with various internal "facts" keyed by device hostname. The full dict must be given as argument to `pyavd.get_device_structured_config`.
    """
    # pylint: disable=import-outside-toplevel
    from pyavd._eos_designs.eos_designs_facts.get_facts import get_facts
    from pyavd._eos_designs.schema import EosDesigns

    # pylint: enable=import-outside-toplevel

    all_input_classes: dict[str, EosDesigns] = {}
    all_input_classes = {hostname: EosDesigns._from_dict(hostvars) for hostname, hostvars in all_inputs.items()}
    return get_facts(all_inputs=all_input_classes, pool_manager=pool_manager, all_hostvars=all_inputs)
