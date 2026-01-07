# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import os
from concurrent.futures import ThreadPoolExecutor
from typing import TYPE_CHECKING

from pyavd._eos_designs.eos_designs_facts import EosDesignsFactsGenerator
from pyavd._eos_designs.shared_utils import SharedUtils
from pyavd._errors import AristaAvdError, AristaAvdMissingVariableError

if TYPE_CHECKING:
    from collections.abc import MutableMapping

    from ansible.template import Templar

    from pyavd._eos_designs.schema import EosDesigns
    from pyavd.api.pool_manager import PoolManager

    from .schema import EosDesignsFacts

# Maximum workers for parallel rendering. Can be overridden via environment variable.
_DEFAULT_MAX_WORKERS = 32
_MAX_WORKERS = min(os.cpu_count() or 1, int(os.environ.get("AVD_FACTS_MAX_WORKERS", _DEFAULT_MAX_WORKERS)))


def get_facts(
    all_inputs: dict[str, EosDesigns],
    all_hostvars: MutableMapping[str, MutableMapping],
    templar: Templar | None = None,
    pool_manager: PoolManager | None = None,
    digital_twin: bool = False,
) -> dict[str, EosDesignsFacts]:
    """
    Generate facts for all devices.

    Args:
        all_inputs: EosDesigns instances for each device.
        all_hostvars: Dictionaries with validated input vars.
        templar: Templater used to render custom jinja templates.
        pool_manager: instance of pool-manager used for dynamic assignments like node ids.
        digital_twin: Optional flag to enable avd_digital_twin_mode.

    Returns:
        EosDesignsFacts instances for each device.
    """
    peer_facts_generators: dict[str, EosDesignsFactsGenerator] = {}
    """Placeholder for generators. Referenced in the generators themselves as well as in shared_utils to be able to resolve facts for peers."""

    all_facts: dict[str, EosDesignsFacts] = {}
    """Placeholder for the final facts data to be returned."""

    mlag_groups: dict[str, set[str]] = {}
    """Placeholder for map of mlag_group to devices. Used to identify MLAG pairs from the mlag_group variable."""

    for hostname, inputs in all_inputs.items():
        hostvars = all_hostvars.get(hostname, {})
        peer_facts_generators[hostname] = _create_generator_instance(
            hostname, inputs, hostvars, templar, pool_manager, digital_twin, peer_facts_generators, mlag_groups
        )

    for generator in peer_facts_generators.values():
        generator.update_mlag_groups()

    for generator in peer_facts_generators.values():
        generator.cross_pollinate()

    # Parallelize render phase - each generator.render() is independent after cross-pollination
    # Use ThreadPoolExecutor since render() is CPU-bound but releases GIL during cached_property lookups
    num_devices = len(peer_facts_generators)
    if num_devices > 1:
        # Parallel execution for multiple devices
        max_workers = min(_MAX_WORKERS, num_devices)

        def _render_one(item: tuple[str, EosDesignsFactsGenerator]) -> tuple[str, EosDesignsFacts]:
            hostname, generator = item
            return hostname, generator.render()

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            try:
                for hostname, facts in executor.map(_render_one, peer_facts_generators.items()):
                    all_facts[hostname] = facts
            except AristaAvdMissingVariableError as e:
                # Exception from thread already has host info from _render_one
                raise AristaAvdMissingVariableError(variable=e.variable, host=e.host) from e
            except AristaAvdError as e:
                # Re-raise with host info preserved from the original exception
                host = e.host if hasattr(e, "host") and e.host else "unknown"
                msg = f"{str(e).removesuffix('.')} for host '{host}'."
                raise type(e)(msg, host=host) from e
    else:
        # Single device - no threading overhead
        for hostname, generator in peer_facts_generators.items():
            try:
                all_facts[hostname] = generator.render()
            except AristaAvdMissingVariableError as e:  # noqa: PERF203
                raise AristaAvdMissingVariableError(variable=e.variable, host=e.host or hostname) from e
            except AristaAvdError as e:
                host = e.host if hasattr(e, "host") and e.host else hostname
                msg = f"{str(e).removesuffix('.')} for host '{host}'."
                raise type(e)(msg, host=host) from e

    return all_facts


def _create_generator_instance(
    hostname: str,
    inputs: EosDesigns,
    hostvars: MutableMapping,
    templar: Templar | None,
    pool_manager: PoolManager | None,
    digital_twin: bool,
    peer_facts_generators: dict[str, EosDesignsFactsGenerator],
    mlag_groups: dict[str, set[str]],
) -> EosDesignsFactsGenerator:
    """Initialize SharedUtils and EosDesignsFactsGenerator and return the instance of the generator."""
    shared_utils = SharedUtils(
        hostname=hostname,
        hostvars=hostvars,
        inputs=inputs,
        templar=templar,
        peer_facts=peer_facts_generators,
        pool_manager=pool_manager,
        digital_twin=digital_twin,
    )
    return EosDesignsFactsGenerator(hostvars=hostvars, inputs=inputs, peer_generators=peer_facts_generators, shared_utils=shared_utils, mlag_groups=mlag_groups)
