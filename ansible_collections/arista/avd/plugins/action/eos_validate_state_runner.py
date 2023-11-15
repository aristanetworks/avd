# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, annotations, division, print_function

__metaclass__ = type

import logging
from pathlib import Path
from tempfile import NamedTemporaryFile

from ansible.errors import AnsibleActionFail
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.plugins.action import ActionBase, display
from yaml import dump_all

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils import AnsibleEOSDevice, get_anta_results
from ansible_collections.arista.avd.plugins.plugin_utils.utils import PythonToAnsibleContextFilter, PythonToAnsibleHandler

LOGGER = logging.getLogger("ansible_collections.arista.avd")
# ANTA 0.10.0 currently add some RichHandler to the root logger so need to disable propagation
LOGGER.propagate = False


class AnsibleNoAliasDumper(AnsibleDumper):
    def ignore_aliases(self, data):
        return True


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        self._supports_check_mode = True

        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        hostname = task_vars["inventory_hostname"]
        ansible_connection = self._connection
        ansible_check_mode = task_vars.get("ansible_check_mode", False)
        is_deployed = task_vars.get("is_deployed", True)

        if not is_deployed:
            result["skipped"] = True
            result["msg"] = f"Device {hostname} is marked as not deployed. Skipping all tests."
            return result

        # Handle logging
        setup_module_logging(hostname, result)

        # Get task arguments and validate them
        logging_level = self._task.args.get("logging_level")
        VALID_VALUES = ["DEBUG", "INFO", "ERROR", "WARNING", "CRITICAL"]
        if logging_level is None or not isinstance(logging_level, str) or logging_level not in VALID_VALUES:
            raise AnsibleActionFail(f"'logging_level' must be a string in {VALID_VALUES}, got {logging_level}")

        save_catalog = self._task.args.get("save_catalog")
        if not isinstance(save_catalog, bool):
            raise AnsibleActionFail(f"'save_catalog' must be a boolean, got {save_catalog}.")

        save_catalog_name = None
        if save_catalog:
            device_catalog_output_dir = self._task.args.get("device_catalog_output_dir")
            if device_catalog_output_dir is not None:
                save_catalog_name = f"{device_catalog_output_dir}/{hostname}-catalog.yml"
            else:
                raise AnsibleActionFail("'device_catalog_output_dir' must be set when 'save_catalog' is True.")

        skipped_tests = self._task.args.get("skipped_tests", [])
        # TODO once we have pydantic, check the list elements
        if not isinstance(skipped_tests, list):
            raise AnsibleActionFail(f"'skipped_tests' must be a list of dictionnaries, got {skipped_tests}.")

        # Fetching ansible tags for backward compatibility
        ansible_tags = {
            "ansible_run_tags": task_vars.get("ansible_run_tags", ()),
            "ansible_skip_tags": task_vars.get("ansible_skip_tags", ()),
        }

        # This is not all the hostvars, but just the Ansible Hostvars Manager object where we can retrieve hostvars for each host on-demand.
        hostvars = task_vars["hostvars"]

        try:
            anta_device = AnsibleEOSDevice(name=hostname, connection=ansible_connection, check_mode=ansible_check_mode)
            anta_results = get_anta_results(
                anta_device=anta_device,
                hostvars=hostvars,
                logging_level=logging_level,
                skipped_tests=skipped_tests,
                ansible_tags=ansible_tags,
                save_catalog_name=save_catalog_name,
                # This convert Ansible Check Mode to dry_run
                dry_run=ansible_check_mode,
                yaml_dumper=AnsibleNoAliasDumper,
            )
            # Call the function to handle temp file creation
            temp_file_name = create_temp_file(hostname, anta_results)

        except Exception as error:
            raise AnsibleActionFail(message=str(error)) from error

        # Add the temp file path to the Ansible result
        result["results_temp_file"] = temp_file_name

        return result


def create_temp_file(hostname: str, anta_results: list[dict]) -> str:
    """
    Create a temporary YAML file to save all test results from ANTA.
    The function will also search for leftover temp files in the `/tmp` folder and delete them.

    The temp file is saved in `/tmp` with a prefix of `<hostname>_` and `.yml` extension.

    Args:
      hostname (str): Current inventory device that is running the plugin.
      anta_results (list[dict]): The list of ANTA results that will be saved in the YAML file.

    Returns:
      str: The absolute path of the temp file.
    """
    temp_file_prefix = f"{hostname}_"
    temp_file_directory = Path("/tmp")

    # Search for leftover temp files with the hostname prefix and delete them.
    for file in temp_file_directory.glob(f"{temp_file_prefix}*"):
        file.unlink(missing_ok=True)

    # Create the temp YAML file to save the ANTA results
    with NamedTemporaryFile(mode="w+", encoding="UTF-8", suffix=".yml", prefix=f"{hostname}_", dir=str(temp_file_directory), delete=False) as temp_file:
        # Each YAML document in the file represents a single test result
        temp_file.write(dump_all(anta_results, Dumper=AnsibleDumper, indent=2, sort_keys=False, width=130))
        return temp_file.name


def setup_module_logging(hostname: str, result: dict) -> None:
    """
    Create a Filter to add the hostname to generate logs,
    Add a Handler to copy the logs from the plugin into Ansible output based on their level

    Args:
      hostname (str): Current Inventory device being used to augment the logs with <hostname>
      result (dict): The ansible dictionary used for the results
    """
    python_to_ansible_filter = PythonToAnsibleContextFilter(hostname)
    python_to_ansible_handler = PythonToAnsibleHandler(result, display)
    python_to_ansible_handler.addFilter(python_to_ansible_filter)
    LOGGER.addHandler(python_to_ansible_handler)
    # TODO mechanism to manipulate the logger globally for pyavd
    # Keep debug to be able to see logs with `-v` and `-vvv`
    LOGGER.setLevel(logging.DEBUG)
