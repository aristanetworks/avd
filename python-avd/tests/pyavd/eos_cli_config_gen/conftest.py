# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path

import pytest

from tests.utils import read_file, read_vars

VARS_PATH = Path(Path(__file__).parent, "../artifacts/eos_cli_config_gen/vars")
CONFIGS_PATH = Path(Path(__file__).parent, "../artifacts/eos_cli_config_gen/configs")
DOCS_PATH = Path(Path(__file__).parent, "../artifacts/eos_cli_config_gen/documentation")


def get_hostnames() -> list:
    assert Path(VARS_PATH).is_dir()

    return [Path(device_var_file).name.removesuffix(".yaml").removesuffix(".yml").removesuffix(".json") for device_var_file in Path(VARS_PATH).glob("*")]


@pytest.fixture(scope="module")
def all_inputs() -> dict[str, dict]:
    """
    Return dict with all inputs.

    {
        "hostname1": dict
        "hostname2": dict
    }
    The inputs are read of test artifacts which are hostvars extracted from Ansible molecule scenarios.
    """
    assert Path(VARS_PATH).is_dir()

    inputs = {}
    for device_var_file in Path(VARS_PATH).glob("*"):
        hostname = Path(device_var_file).name.removesuffix(".yaml").removesuffix(".yml").removesuffix(".json")
        inputs[hostname] = read_vars(device_var_file)

    return inputs


@pytest.fixture(scope="module", params=get_hostnames())
def hostname(request: pytest.FixtureRequest) -> dict:
    return request.param


@pytest.fixture(scope="module")
def configs() -> dict:
    """
    Return dict with all configs.

    {
        "hostname1": str
        "hostname2": str
    }
    The contents are extracted from Ansible molecule scenarios.
    """
    assert Path(CONFIGS_PATH).is_dir()

    result = {}
    for filename in Path(CONFIGS_PATH).glob("*"):
        hostname = Path(filename).name.removesuffix(".cfg")
        result[hostname] = read_file(filename)

    return result


@pytest.fixture(scope="module")
def device_docs() -> dict:
    """
    Return dict with all docs.

    {
        "hostname1": str
        "hostname2": str
    }
    The contents are extracted from Ansible molecule scenarios.
    """
    assert Path(DOCS_PATH).is_dir()

    result = {}
    for filename in Path(DOCS_PATH).glob("*"):
        hostname = Path(filename).name.removesuffix(".md")
        result[hostname] = read_file(filename)

    return result
