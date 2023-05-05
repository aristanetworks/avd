import glob
from collections import ChainMap
from os import path, system

import pytest
from pyavd import eos_cli_config_gen, eos_designs_facts, eos_designs_structured_configs
from yaml import safe_dump as yaml_dump

from .utils import create_common_vars, read_vars, write_result


@pytest.mark.parametrize(
    "common_varfiles, fact_file, device_varfiles",
    [
        (
            [
                "pyavd/vendor/tests/eos_designs/main.yml",
                "pyavd/vendor/tests/eos_designs/default-connected-endpoints-keys.yml",
                "pyavd/vendor/tests/eos_designs/default-node-type-keys.yml",
                "pyavd/vendor/tests/eos_designs/default-platform-settings.yml",
                "pyavd/vendor/tests/eos_designs/default-templates.yml",
                "pyavd/vendor/tests/eos_designs/pyavd_test_vars.yml",
            ],
            "./pyavd/vendor/tests/eos_designs/facts/eos_designs_facts.yml",
            "./pyavd/vendor/tests/eos_designs/vars/*",
        )
    ],
)
def test_eos_designs_facts(common_varfiles: list[str], fact_file: str, device_varfiles: str):
    common_vars = create_common_vars(common_varfiles)

    all_hostvars = {}
    for device_var_file in glob.iglob(device_varfiles):
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


@pytest.mark.parametrize(
    "common_varfiles, fact_file, device_varfiles, struct_cfg_file_dir, expected_config",
    [
        (
            [
                "pyavd/vendor/tests/eos_designs/main.yml",
                "pyavd/vendor/tests/eos_designs/default-connected-endpoints-keys.yml",
                "pyavd/vendor/tests/eos_designs/default-node-type-keys.yml",
                "pyavd/vendor/tests/eos_designs/default-platform-settings.yml",
                "pyavd/vendor/tests/eos_designs/default-templates.yml",
                "pyavd/vendor/tests/eos_designs/pyavd_test_vars.yml",
            ],
            "./pyavd/vendor/tests/eos_designs/facts/eos_designs_facts.yml",
            "./pyavd/vendor/tests/eos_designs/vars/*",
            "./pyavd/vendor/tests/eos_designs/structured_configs",
            "./pyavd/vendor/tests/eos_designs/expected_structured_configs/",
        )
    ],
)

# make sure vendor/tests/eos_designs/structured_configs is empty before starting the test_case
def test_eos_designs_structured_configs(common_varfiles: list[str], fact_file: str, device_varfiles: str, struct_cfg_file_dir: str, expected_config: str):
    # Read common vars
    common_vars = create_common_vars(common_varfiles)

    common_vars.update(read_vars(fact_file))

    for device_var_file in glob.iglob(device_varfiles):
        hostname = str(path.basename(device_var_file)).removesuffix(".yaml").removesuffix(".yml").removesuffix(".json")

        device_vars = ChainMap(
            {},
            common_vars["avd_switch_facts"][hostname],
            read_vars(device_var_file),
            common_vars,
        )

        structured_configuration = eos_designs_structured_configs(hostname, device_vars)
        write_result(path.join(struct_cfg_file_dir, f"{hostname}.yml"), yaml_dump(structured_configuration, sort_keys=False, width=130))
    diff = system(f"diff {expected_config} {struct_cfg_file_dir}")
    assert not diff


@pytest.mark.parametrize(
    "common_varfiles, device_varfiles, cfgfiles_dir, expected_config, docfiles",
    [
        (
            ["./pyavd/vendor/tests/eos_cli_config_gen/all.yml"],
            "./pyavd/vendor/tests/eos_cli_config_gen/vars/*",
            "./pyavd/vendor/tests/eos_cli_config_gen/configs",
            "./pyavd/vendor/tests/eos_cli_config_gen/expected_configs/",
            None,
        ),
        (
            [],
            "pyavd/vendor/tests/eos_designs/structured_configs/* ",
            "pyavd/vendor/tests/eos_designs/configs",
            "./pyavd/vendor/tests/eos_designs/expected_configs/",
            None,
        ),
    ],
)
# make sure vendor/tests/(eos_cli_config_gen|eos_designs)/configs is empty before starting the test_case
def test_eos_cli_config_gen(common_varfiles: list[str], device_varfiles: str, cfgfiles_dir: str, expected_config: str, docfiles: str | None):
    common_vars = create_common_vars(common_varfiles)

    render_configuration = cfgfiles_dir is not None
    render_documentation = docfiles is not None

    for device_varfile in glob.iglob(device_varfiles):
        device_vars = common_vars.copy()
        device_vars.update(read_vars(device_varfile))
        hostname = str(path.basename(device_varfile)).removesuffix(".yaml").removesuffix(".yml").removesuffix(".json")
        configuration, documentation = eos_cli_config_gen(hostname, device_vars, render_configuration, render_documentation)

        if render_configuration:
            write_result(path.join(cfgfiles_dir, f"{hostname}.cfg"), configuration)
        if render_documentation:
            write_result(path.join(docfiles, f"{hostname}.md"), documentation)

    diff = system(f"diff {expected_config} {cfgfiles_dir}")
    assert not diff
