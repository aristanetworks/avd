import glob
from collections import ChainMap
from os import path

import pytest
from pyavd import eos_cli_config_gen, eos_designs_facts, eos_designs_structured_configs
from utils import create_common_vars, get_files_in_folder, read_vars, write_result
from yaml import safe_dump as yaml_dump

common_varfiles = ["./pyavd/vendor/tests/eos_designs/pyavd_test_vars.yml"]
fact_file = "./pyavd/vendor/tests/eos_designs/facts/eos_designs_facts.yml"
device_varfiles = "./pyavd/vendor/tests/eos_designs/vars/"
expected_structured_configs = "./pyavd/vendor/tests/eos_designs/expected_structured_configs/"


@pytest.fixture(scope="module", autouse=True)
def generate_eos_designs_facts():
    """
    Generating EOS_DESIGNS_FACTS
    """

    common_vars = create_common_vars(common_varfiles)
    all_hostvars = {}

    for device_var_file in glob.iglob(f"{device_varfiles}*"):
        device_vars = common_vars.copy()
        device_vars.update(read_vars(device_var_file))
        hostname = str(path.basename(device_var_file)).removesuffix(".yaml").removesuffix(".yml").removesuffix(".json")
        all_hostvars[hostname] = device_vars

    hostnames = list(all_hostvars.keys())
    for hostname, device_vars in all_hostvars.items():
        # Insert ansible vars our code relies on today
        device_vars["inventory_hostname"] = hostname
        fabric_name = device_vars.get("fabric_name", "all")
        device_vars["groups"] = {fabric_name: hostnames}

    facts = eos_designs_facts(all_hostvars)

    # Insert ansible vars our code relies on today
    facts["groups"] = {fabric_name: hostnames}

    if fact_file:
        write_result(fact_file, yaml_dump(facts, sort_keys=False))


@pytest.mark.parametrize("device_var_file", get_files_in_folder(device_varfiles))
def test_eos_designs_structured_configs(device_var_file: str):
    """
    Testing eos_designs_structured_configs.
    Parameter: device_var_file - host file
    """

    common_vars = create_common_vars(common_varfiles)
    common_vars.update(read_vars(fact_file))

    hostname = str(path.basename(device_var_file)).removesuffix(".yaml").removesuffix(".yml").removesuffix(".json")
    device_vars = ChainMap(
        {},
        common_vars["avd_switch_facts"][hostname],
        read_vars(device_var_file),
        common_vars,
    )

    structured_configuration = eos_designs_structured_configs(hostname, device_vars)
    expected_structured_config = read_vars(f"{expected_structured_configs}/{hostname}.yml")
    assert structured_configuration == expected_structured_config


@pytest.mark.parametrize("input_structured_config", get_files_in_folder(expected_structured_configs))
def test_eos_cli_config_gen(input_structured_config: str):
    """
    Testing eos_cli_config_gen.
    Parameter: device_var_file - structured configs file
    """

    expected_configs = "./pyavd/vendor/tests/eos_designs/expected_configs"
    render_configuration = True

    device_vars = read_vars(input_structured_config)
    hostname = str(path.basename(input_structured_config)).removesuffix(".yaml").removesuffix(".yml").removesuffix(".json")
    configuration, documentation = eos_cli_config_gen(hostname, device_vars, render_configuration)

    with open(f"{expected_configs}/{hostname}.cfg", "r") as f:
        exp_file_output = f.read()
    assert configuration == exp_file_output
