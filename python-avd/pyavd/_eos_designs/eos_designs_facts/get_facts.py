# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._eos_designs.eos_designs_facts import EosDesignsFactsGenerator
from pyavd._eos_designs.shared_utils import SharedUtils
from pyavd._errors import AristaAvdError, AristaAvdMissingVariableError

if TYPE_CHECKING:
    from collections.abc import Mapping

    from ansible.template import Templar

    from pyavd._eos_designs.schema import EosDesigns
    from pyavd.api.pool_manager import PoolManager

    from .schema import EosDesignsFacts


def get_facts(
    all_inputs: dict[str, EosDesigns],
    all_hostvars: Mapping[str, Mapping],
    templar: Templar | None = None,
    pool_manager: PoolManager | None = None,
    device_uid_to_hostname_map: Mapping[str, str] | None = None,
) -> dict[str, EosDesignsFacts]:
    """
    Generate facts for all devices.

    Args:
        all_inputs: EosDesigns instances for each device. Keyed by device_uid - most often the same as hostname.
        all_hostvars: Dictionaries with validated input vars. Keyed by device_uid - most often the same as hostname.
        templar: Templater used to render custom jinja templates.
        pool_manager: instance of pool-manager used for dynamic assignments like node ids.
        device_uid_to_hostname_map: Map from device_uid to hostname. Assumes hostname == device_uid if not set.

    Returns:
        EosDesignsFacts instances for each device. Keyed by device_uid - most often the same as hostname.
    """
    peer_facts_generators: dict[str, EosDesignsFactsGenerator] = {}
    """Placeholder for generators. Referenced in the generators themselves as well as in shared_utils to be able to resolve facts for peers."""

    all_facts: dict[str, EosDesignsFacts] = {}
    """Placeholder for the final facts data to be returned."""

    if not device_uid_to_hostname_map:
        device_uid_to_hostname_map = {}

    for device_uid, inputs in all_inputs.items():
        hostname = device_uid_to_hostname_map.get(device_uid, device_uid)
        hostvars = all_hostvars.get(device_uid, {})
        peer_facts_generators[device_uid] = _create_generator_instance(device_uid, hostname, inputs, hostvars, templar, pool_manager, peer_facts_generators)

    for generator in peer_facts_generators.values():
        generator.cross_pollinate()

    for hostname, generator in peer_facts_generators.items():
        try:
            all_facts[hostname] = generator.render()
        except AristaAvdMissingVariableError as e:  # noqa: PERF203
            raise AristaAvdMissingVariableError(variable=e.variable, host=hostname) from e
        except AristaAvdError as e:
            msg = f"{str(e).removesuffix('.')} for host '{hostname}'."
            raise type(e)(msg) from e

    return all_facts


def _create_generator_instance(
    device_uid: str,
    hostname: str,
    inputs: EosDesigns,
    hostvars: Mapping,
    templar: Templar | None,
    pool_manager: PoolManager | None,
    peer_facts_generators: dict[str, EosDesignsFactsGenerator],
) -> EosDesignsFactsGenerator:
    """Initialize SharedUtils and EosDesignsFactsGenerator and return the instance of the generator."""
    shared_utils = SharedUtils(
        device_uid=device_uid, hostname=hostname, hostvars=hostvars, inputs=inputs, templar=templar, peer_facts=peer_facts_generators, pool_manager=pool_manager
    )
    return EosDesignsFactsGenerator(hostvars=hostvars, inputs=inputs, peer_generators=peer_facts_generators, shared_utils=shared_utils)
