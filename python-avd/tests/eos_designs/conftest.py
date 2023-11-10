# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from glob import iglob
from pathlib import Path

import pytest
from pyavd import AvdPoolManager, get_avd_facts

from ..utils import read_file, read_vars

OUTPUT_DIR = Path(Path(__file__).parent, "../artifacts/eos_designs_unit_tests")
VARS_PATH = OUTPUT_DIR.joinpath("vars")
STRUCTURED_CONFIGS_PATH = OUTPUT_DIR.joinpath("structured_configs")
CONFIGS_PATH = OUTPUT_DIR.joinpath("configs")


def get_hostnames():
    assert Path(VARS_PATH).is_dir()

    hostnames = []
    for device_var_file in iglob(f"{VARS_PATH}/*"):
        hostnames.append(Path(device_var_file).name.removesuffix(".yaml").removesuffix(".yml").removesuffix(".json"))

    return hostnames


@pytest.fixture(scope="module")
def all_inputs() -> dict[str, dict]:
    """
    Return dict with all inputs like
    {
        "hostname1": dict
        "hostname2": dict
    }
    The inputs are read of test artifacts which are hostvars extracted from Ansible molecule scenarios.
    """
    assert Path(VARS_PATH).is_dir()

    inputs = {}
    for device_var_file in iglob(f"{VARS_PATH}/*"):
        hostname = Path(device_var_file).name.removesuffix(".yaml").removesuffix(".yml").removesuffix(".json")
        inputs[hostname] = read_vars(device_var_file)

    return inputs


@pytest.fixture(scope="module")
def pool_manager() -> dict:
    """
    Return instance of AvdPoolManager initialized with output_dir=OUTPUT_DIR
    """
    assert Path(OUTPUT_DIR).is_dir()
    return AvdPoolManager(OUTPUT_DIR)


@pytest.fixture(scope="module")
def avd_facts(all_inputs: dict, pool_manager: AvdPoolManager):
    """
    Test get_avd_facts
    """
    return get_avd_facts(all_inputs, pool_manager=pool_manager)


@pytest.fixture(scope="module", params=get_hostnames())
def hostname(request) -> dict:
    hostname = request.param
    return hostname


@pytest.fixture(scope="module")
def structured_configs() -> dict:
    """
    Return dict with all structured_configs like
    {
        "hostname1": dict
        "hostname2": dict
    }
    The contents are extracted from Ansible molecule scenarios.
    """
    assert Path(STRUCTURED_CONFIGS_PATH).is_dir()

    result = {}
    for filename in iglob(f"{STRUCTURED_CONFIGS_PATH}/*"):
        hostname = Path(filename).name.removesuffix(".yaml").removesuffix(".yml").removesuffix(".json")
        result[hostname] = read_vars(filename)

    return result


@pytest.fixture(scope="module")
def configs() -> dict:
    """
    Return dict with all configs like
    {
        "hostname1": str
        "hostname2": str
    }
    The contents are extracted from Ansible molecule scenarios.
    """
    assert Path(CONFIGS_PATH).is_dir()

    result = {}
    for filename in iglob(f"{CONFIGS_PATH}/*"):
        hostname = Path(filename).name.removesuffix(".cfg")
        result[hostname] = read_file(filename)

    return result
