# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import re
import sys
from copy import deepcopy
from typing import TYPE_CHECKING
from unittest.mock import patch

import pytest

from pyavd import get_avd_facts, get_device_config, get_device_structured_config, validate_inputs, validate_structured_config
from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.shared_utils import SharedUtils
from pyavd._utils import get
from pyavd.api.pool_manager.node_id_pools import NodeIdAssignmentKey
from tests.models import MoleculeScenario

if TYPE_CHECKING:
    from pyavd.api.pool_manager.node_id_pools import PoolAssignment


@pytest.mark.molecule_scenarios(
    "eos_designs_unit_tests",
)
def test_eos_designs_device_uid(molecule_scenario: MoleculeScenario) -> None:
    """
    Test that eos_designs can properly distinguish the device_uid from the hostname.

    First we load all the vars of the scenario and prefix all names with 'uid_'
    to represent something unique and different from hostname.

    On the calls to pyavd give the original names as hostnames and the prefixed variants as device_uids.

    Assert that the produced configs match the existing artifacts, since using different device_uids should not affect the config.
    """
    molecule_inputs = {host.name: deepcopy(host.hostvars) for host in molecule_scenario.hosts}
    expected_configs = {host.name: host.config for host in molecule_scenario.hosts}

    device_uid_to_hostname_map = {}
    device_uid_keyed_inputs: dict[str, dict] = {}

    for inputs in molecule_inputs.values():
        del inputs["groups"]

    for hostname in molecule_inputs:
        device_uid = f"uid_{hostname}"
        match = re.compile(rf"(^{hostname}|(?<=[ ]){hostname})($|(?=[,]))")
        # Inplace update vars for all devices where this device's hostname i mentioned.
        for other_inputs in molecule_inputs.values():
            dict_replace_value(other_inputs, match, device_uid)

    for hostname, inputs in molecule_inputs.items():
        device_uid = f"uid_{hostname}"
        device_uid_to_hostname_map[device_uid] = hostname
        validate_inputs(inputs)
        device_uid_keyed_inputs[device_uid] = inputs

        if get(inputs, "fabric_numbering.node_id.algorithm") == "pool_manager" and molecule_scenario.pool_manager is not None:
            # Patch the pool_manager assignments to use the uid
            tmp_shared_utils = SharedUtils(device_uid, hostname, inputs, EosDesigns._from_dict(inputs), None, {}, molecule_scenario.pool_manager)
            pool = molecule_scenario.pool_manager.get_pool("node_id_pools", tmp_shared_utils)
            new_assignments: dict[NodeIdAssignmentKey, PoolAssignment[NodeIdAssignmentKey, int]] = {}
            for assignment_key, assignment in pool.assignments.items():
                new_assignment_key = NodeIdAssignmentKey(f"uid_{assignment_key.device_uid}")
                new_assignments[new_assignment_key] = assignment
            pool.assignments = new_assignments

    with patch("sys.path", [*sys.path, *molecule_scenario.extra_python_paths]):
        avd_facts = get_avd_facts(device_uid_keyed_inputs, pool_manager=molecule_scenario.pool_manager, device_uid_to_hostname_map=device_uid_to_hostname_map)

        for device_uid, inputs in device_uid_keyed_inputs.items():
            structured_config = get_device_structured_config(
                device_uid.removeprefix("uid_"),
                inputs,
                avd_facts,
                device_uid=device_uid,
            )

            # run validation on structured_config to ensure it is converted
            validate_structured_config(structured_config)

            device_config = get_device_config(structured_config)

            assert device_config == expected_configs[device_uid.removeprefix("uid_")]


def dict_replace_value(dct: dict, match: re.Pattern, replacement: str) -> None:
    for key, value in dct.items():
        if isinstance(value, dict):
            dict_replace_value(value, match, replacement)
        elif isinstance(value, list):
            list_replace_value(value, match, replacement)
        elif isinstance(value, str):
            dct[key] = re.sub(match, replacement, value)


def list_replace_value(lst: list, match: re.Pattern, replacement: str) -> None:
    for index, item in enumerate(lst):
        if isinstance(item, list):
            list_replace_value(item, match, replacement)
        elif isinstance(item, dict):
            dict_replace_value(item, match, replacement)
        elif isinstance(item, str):
            lst[index] = re.sub(match, replacement, item)
