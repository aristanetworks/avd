# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import os
from collections import ChainMap
from concurrent.futures import ThreadPoolExecutor
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Mapping

    from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts

# Maximum workers for parallel structured config generation.
# Can be overridden via environment variable.
_DEFAULT_MAX_WORKERS = 32
_MAX_WORKERS = min(os.cpu_count() or 1, int(os.environ.get("AVD_STRUCTURED_CONFIG_MAX_WORKERS", _DEFAULT_MAX_WORKERS)))


def get_device_structured_config(hostname: str, inputs: dict, avd_facts: dict[str, EosDesignsFacts], digital_twin: bool = False) -> dict:
    """
    Build and return the AVD structured configuration for one device.

    Args:
        hostname: Hostname of device.
        inputs: Dictionary with inputs for "eos_designs".
            Variables should be converted and validated according to AVD `eos_designs` schema first using `pyavd.validate_inputs`.
        avd_facts: Dictionary of avd_facts as returned from `pyavd.get_avd_facts`.
        digital_twin: PREVIEW: Optional flag to enable digital-twin mode.

    Returns:
        Device Structured Configuration as a dictionary
    """
    from ._eos_designs.structured_config import get_structured_config  # noqa: PLC0415
    from ._errors import AristaAvdError  # noqa: PLC0415
    from .avd_schema_tools import AvdSchemaTools  # noqa: PLC0415
    from .constants import EOS_DESIGNS_SCHEMA_ID  # noqa: PLC0415

    # Map in avd_facts without touching the hostvars
    mapped_hostvars = ChainMap(
        {
            "switch": avd_facts[hostname]._as_dict(),
        },
        inputs,
    )

    input_schema_tools = AvdSchemaTools(schema_id=EOS_DESIGNS_SCHEMA_ID)
    result = {}

    # We do not validate input variables in this stage (done in "validate_inputs")
    structured_config = get_structured_config(
        hostname=hostname,
        hostvars=mapped_hostvars,
        input_schema_tools=input_schema_tools,
        all_facts=avd_facts,
        result=result,
        templar=None,
        validate=False,
        digital_twin=digital_twin,
    )
    if result.get("failed") or structured_config is None:
        msg = f"{[str(error) for error in result['errors']]}"
        raise AristaAvdError(msg)

    return structured_config._as_dict()


def get_device_structured_configs(
    all_inputs: Mapping[str, dict],
    avd_facts: dict[str, EosDesignsFacts],
    *,
    max_workers: int | None = None,
    digital_twin: bool = False,
) -> dict[str, dict]:
    """
    Build and return the AVD structured configurations for multiple devices in parallel.

    This function processes multiple devices using ThreadPoolExecutor for improved performance
    on multi-core systems. For a single device, use `get_device_structured_config` instead.

    Args:
        all_inputs: Dictionary where keys are hostnames and values are input dictionaries.
            Variables should be converted and validated according to AVD `eos_designs` schema
            first using `pyavd.validate_inputs`.
        avd_facts: Dictionary of avd_facts as returned from `pyavd.get_avd_facts`.
        max_workers: Maximum number of parallel workers. Defaults to min(cpu_count, 32).
            Can also be set via `AVD_STRUCTURED_CONFIG_MAX_WORKERS` environment variable.
        digital_twin: PREVIEW: Optional flag to enable digital-twin mode.

    Returns:
        Dictionary mapping hostname to its structured configuration dictionary.

    Example:
        ```python
        all_inputs = {"spine1": {...}, "spine2": {...}, "leaf1": {...}}
        avd_facts = get_avd_facts(all_inputs)
        all_configs = get_device_structured_configs(all_inputs, avd_facts)
        ```
    """
    from ._errors import AristaAvdError  # noqa: PLC0415

    num_devices = len(all_inputs)
    if num_devices == 0:
        return {}

    if num_devices == 1:
        # Single device - avoid threading overhead
        hostname = next(iter(all_inputs))
        return {hostname: get_device_structured_config(hostname, all_inputs[hostname], avd_facts, digital_twin=digital_twin)}

    # Determine number of workers
    effective_max_workers = max_workers if max_workers is not None else _MAX_WORKERS
    effective_max_workers = max(1, min(effective_max_workers, num_devices, 128))

    def _generate_one(item: tuple[str, dict]) -> tuple[str, dict]:
        hostname, inputs = item
        return hostname, get_device_structured_config(hostname, inputs, avd_facts, digital_twin=digital_twin)

    all_configs: dict[str, dict] = {}

    with ThreadPoolExecutor(max_workers=effective_max_workers) as executor:
        try:
            for hostname, config in executor.map(_generate_one, all_inputs.items()):
                all_configs[hostname] = config
        except AristaAvdError:
            # Re-raise AVD errors as-is (they already contain context)
            raise

    return all_configs
