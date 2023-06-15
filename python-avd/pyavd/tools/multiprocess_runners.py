import glob
from collections import ChainMap
from concurrent.futures import ProcessPoolExecutor
from itertools import repeat
from os import path

from yaml import safe_dump as yaml_dump

from ..get_avd_facts import get_avd_facts
from ..get_device_config import get_device_config
from ..get_device_doc import get_device_doc
from ..get_device_structured_config import get_device_structured_config
from .read_vars import read_vars
from .write_result import write_result


def run_eos_cli_config_gen_process(
    device_var_file: str,
    common_vars: dict,
    struct_cfg_file_dir: str | None,
    cfg_file_dir: str | None,
    doc_file_dir: str | None,
) -> None:
    """
    Function run as process by ProcessPoolExecutor.

    Read device variables from files and run eos_cli_config_gen for one device.

    Parameters
    ----------
    device_var_file : str
        Path to device specific var file to import and merge on top of common vars.
        Filename will be used as hostname.
    common_vars : dict
        Common vars to be applied on all devices.
    struct_cfg_file_dir: str | None
        Path to dir for input structured_config files.
    cfg_file_dir: str | None
        Path to dir for output config file if set.
    doc_file_dir: str | None
        Path to dir for output documentation file if set.
    verbosity: int
        Vebosity level for output. Passed along to other functions
    """

    render_configuration = cfg_file_dir is not None
    render_documentation = doc_file_dir is not None

    device_vars = common_vars.copy()
    device_vars.update(read_vars(device_var_file))
    hostname = str(path.basename(device_var_file)).removesuffix(".yaml").removesuffix(".yml").removesuffix(".json")
    if struct_cfg_file_dir is not None:
        structured_config_file = path.join(struct_cfg_file_dir, f"{hostname}.yml")
        device_vars.update(read_vars(structured_config_file))

    if render_configuration:
        configuration = get_device_config(hostname, device_vars)
        write_result(path.join(cfg_file_dir, f"{hostname}.cfg"), configuration)
    if render_documentation:
        documentation = get_device_doc(hostname, device_vars)
        write_result(path.join(doc_file_dir, f"{hostname}.md"), documentation)

    print(f"OK: {hostname}")


def run_eos_cli_config_gen(
    common_varfiles: list[str],
    device_varfiles: str,
    struct_cfg_file_dir: str | None,
    cfgfiles_dir: str | None,
    docfiles_dir: str | None,
) -> None:
    """
    Read common variables from files and run eos_cli_config_gen for each device in process workers.

    Intended for CLI use via runner.py

    Parameters
    ----------
    common_varfiles : list[str]
        List of common var files to import and merge.
    device_varfiles : str
        Glob for device specific var files to import and merge on top of common vars.
        Filenames will be used as hostname.
    struct_cfg_file_dir: str | None
        Path to dir for input structured_config files.
    cfgfiles_dir: str | None
        Path to dir for output config files if set.
    docfiles_dir: str | None
        Path to dir for output documentation files if set.
    """

    # Read common vars
    common_vars = {}

    for file in common_varfiles:
        common_vars.update(read_vars(file))

    with ProcessPoolExecutor(max_workers=20) as executor:
        return_values = executor.map(
            run_eos_cli_config_gen_process,
            glob.iglob(device_varfiles),
            repeat(common_vars),
            repeat(struct_cfg_file_dir),
            repeat(cfgfiles_dir),
            repeat(docfiles_dir),
        )

    for return_value in return_values:
        if return_value is not None:
            print(return_value)


def run_eos_designs_facts(common_varfiles: list[str], device_varfiles: str, facts_file: str) -> None:
    """
    Read variables from files and run eos_designs_facts.

    Intended for CLI use via runner.py

    Parameters
    ----------
    common_varfiles : list[str]
        List of common var files to import and merge.
    device_varfiles : str
        Glob for device specific var files to import and merge on top of common vars.
        Filenames will be used as hostnames.
    facts_file: str
        Path to output facts file
    """

    # Read common vars
    common_vars = {}

    for file in common_varfiles:
        common_vars.update(read_vars(file))

    all_hostvars = {}
    for device_var_file in glob.iglob(device_varfiles):
        device_vars = ChainMap(read_vars(device_var_file), common_vars)
        hostname = str(path.basename(device_var_file)).removesuffix(".yaml").removesuffix(".yml").removesuffix(".json")

        all_hostvars[hostname] = device_vars

    print("Imported files ", end=None)

    # hostnames = list(all_hostvars.keys())
    # for hostname, device_vars in all_hostvars.items():
    #     # Insert ansible vars our code relies on today
    #     fabric_name = device_vars.get("fabric_name", "all")
    #     device_vars["groups"] = {fabric_name: hostnames}

    facts = get_avd_facts(all_hostvars)

    # # Insert ansible vars our code relies on today
    # facts["groups"] = {fabric_name: hostnames}

    if facts_file:
        write_result(facts_file, yaml_dump(facts, sort_keys=False))

    print("OK eos_designs_facts")


def run_eos_designs_structured_configs_process(device_var_file: str, common_vars: dict, avd_facts: dict, struct_cfg_file_dir: str) -> None:
    """
    Function run as process by ProcessPoolExecutor.

    Read device variables from files and run eos_designs_structured_configs for one device.

    Parameters
    ----------
    device_var_file : str
        Path to device specific var file to import and shallow merge on top of common vars and facts.
        Filename will be used as hostname.
    common_vars : dict
        Common vars to be applied to all devices.
        Per-device facts will be extracted from avd_switch_facts and merged on top of device vars.
    avd_facts : dict
        Dictionary of avd_facts as returned from 'get_avd_facts'.
    struct_cfg_file_dir: str
        Path to dir for output structured_config files.
    """

    hostname = str(path.basename(device_var_file)).removesuffix(".yaml").removesuffix(".yml").removesuffix(".json")

    device_vars = ChainMap(
        {},
        read_vars(device_var_file),
        common_vars,
    )

    structured_configuration = get_device_structured_config(hostname, device_vars, avd_facts)
    write_result(
        path.join(struct_cfg_file_dir, f"{hostname}.yml"),
        yaml_dump(structured_configuration, sort_keys=False, width=130),
    )
    print(f"OK: {hostname}")


def run_eos_designs_structured_configs(
    common_varfiles: list[str],
    fact_file: str,
    device_varfiles: str,
    struct_cfgfiles: str,
) -> None:
    """
    Read common variables from files and run eos_cli_config_gen for each device in process workers.

    Intended for CLI use via runner.py

    Parameters
    ----------
    common_varfiles : list[str]
        List of common var files to import and merge.
    fact_file : str
        Path to fact file produced by eos_designs_facts.
    device_varfiles : str
        Glob for device specific var files to import and shallow merge on top of common vars.
        Filenames will be used as hostname.
    struct_cfgfiles: str
        Path to dir for output structured_config files.
    verbosity: int
        Vebosity level for output. Passed along to other functions
    """

    # Read common vars
    common_vars = {}

    for file in common_varfiles:
        common_vars.update(read_vars(file))

    avd_facts = read_vars(fact_file)

    with ProcessPoolExecutor(max_workers=10) as executor:
        return_values = executor.map(
            run_eos_designs_structured_configs_process,
            glob.iglob(device_varfiles),
            repeat(common_vars),
            repeat(avd_facts),
            repeat(struct_cfgfiles),
        )

    for return_value in return_values:
        if return_value is not None:
            print(return_value)
