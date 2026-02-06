# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pyavd._eos_designs.eos_designs_facts import EosDesignsFactsGenerator
from pyavd._eos_designs.shared_utils import SharedUtils
from pyavd._errors import AristaAvdError, AristaAvdMissingVariableError

if TYPE_CHECKING:
    from collections.abc import Mapping, MutableMapping

    from ansible.template import Templar

    from pyavd.api.pool_manager import PoolManager
    from pyavd.api.schemas import AVDDesign

    from .schema import EosDesignsFacts


def get_facts(
    all_inputs: Mapping[str, AVDDesign | Mapping],
    all_hostvars: Mapping[str, MutableMapping[str, Any]] | None = None,
    templar: Templar | None = None,
    pool_manager: PoolManager | None = None,
    digital_twin: bool = False,
) -> dict[str, EosDesignsFacts]:
    """
    Generate facts for all devices.

    Args:
        all_inputs: Dictionary where keys are hostnames and values are the AVDDesign instance per device.
            Supporting dicts as well for backwards compatibility.
        all_hostvars: Raw hostvars exposed to custom jinja templates or custom python logic for each device.
            This is optional and only needed if custom templates or python modules are used for descriptions or IP addressing.
        templar: Templater used to render custom jinja templates.
            This is optional and only needed if custom templates are used for descriptions or IP addressing.
        pool_manager: instance of pool-manager used for dynamic assignments like node ids.
        digital_twin: Optional flag to enable avd_digital_twin_mode.

    Returns:
        EosDesignsFacts instances for each device.
    """
    from pyavd.api.schemas import AVDDesign  # noqa: PLC0415

    peer_facts_generators: dict[str, EosDesignsFactsGenerator] = {}
    """Placeholder for generators. Referenced in the generators themselves as well as in shared_utils to be able to resolve facts for peers."""

    all_facts: dict[str, EosDesignsFacts] = {}
    """Placeholder for the final facts data to be returned."""

    mlag_groups: dict[str, set[str]] = {}
    """Placeholder for map of mlag_group to devices. Used to identify MLAG pairs from the mlag_group variable."""

    if all_hostvars is None:
        all_hostvars = {}

    for hostname in all_inputs:
        hostvars = all_hostvars.get(hostname, {})

        inputs = all_inputs[hostname]
        if not isinstance(inputs, AVDDesign):
            inputs = AVDDesign._from_dict(inputs)

        peer_facts_generators[hostname] = _create_generator_instance(
            hostname, inputs, hostvars, templar, pool_manager, digital_twin, peer_facts_generators, mlag_groups
        )

    for generator in peer_facts_generators.values():
        generator.update_mlag_groups()

    for generator in peer_facts_generators.values():
        generator.cross_pollinate()

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
    inputs: AVDDesign,
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
