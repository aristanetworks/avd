# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, annotations, division, print_function

__metaclass__ = type

import cProfile
import logging
import pstats
from json import dumps
from shutil import copy2
from tempfile import NamedTemporaryFile

from ansible.errors import AnsibleActionFail
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils import AnsibleEOSDevice, get_anta_results
from ansible_collections.arista.avd.plugins.plugin_utils.utils import (
    PythonToAnsibleContextFilter,
    PythonToAnsibleHandler,
    get_and_validate,
    verify_and_return_path,
)

LOGGER = logging.getLogger("ansible_collections.arista.avd")
# ANTA currently add some RichHandler to the root logger so need to disable propagation
LOGGER.propagate = False
LOGGING_LEVELS = ["DEBUG", "INFO", "ERROR", "WARNING", "CRITICAL"]


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

        # Setup profiling
        cprofile_file = self._task.args.get("cprofile_file")
        if cprofile_file:
            profiler = cProfile.Profile()
            profiler.enable()

        # Setup variables
        hostname = task_vars["inventory_hostname"]
        ansible_connection = self._connection
        ansible_check_mode = task_vars.get("ansible_check_mode", False)
        is_deployed = task_vars.get("is_deployed", True)
        ansible_tags = {
            "ansible_run_tags": task_vars.get("ansible_run_tags", ()),
            "ansible_skip_tags": task_vars.get("ansible_skip_tags", ()),
        }
        # This is not all the hostvars, but just the Ansible Hostvars Manager object where we can retrieve hostvars for each host on-demand.
        hostvars = task_vars["hostvars"]

        # Skip all tests if the device is marked as not deployed
        if not is_deployed:
            result["skipped"] = True
            result["msg"] = f"Device {hostname} is marked as not deployed. Skipping all tests."
            return result

        # Setup module logging
        setup_module_logging(hostname, result)

        # Get task arguments and validate them
        # TODO: Try Except
        logging_level = get_and_validate(data=self._task.args, key="logging_level", expected_type=str, default_value="WARNING", allowed_values=LOGGING_LEVELS)
        skipped_tests = get_and_validate(data=self._task.args, key="skipped_tests", expected_type=list, default_value=[])
        save_catalog = get_and_validate(data=self._task.args, key="save_catalog", expected_type=bool, default_value=False)
        save_results = get_and_validate(data=self._task.args, key="save_results", expected_type=bool, default_value=False)
        catalog_path = verify_and_return_path(path_input=self._task.args.get("device_catalog_path")) if save_catalog else None
        result_path = verify_and_return_path(path_input=self._task.args.get("device_result_path")) if save_results else None

        try:
            anta_device = AnsibleEOSDevice(name=hostname, connection=ansible_connection, check_mode=ansible_check_mode)
            anta_results = get_anta_results(
                anta_device=anta_device,
                hostvars=hostvars,
                logging_level=logging_level,
                skipped_tests=skipped_tests,
                ansible_tags=ansible_tags,
                save_catalog_name=catalog_path,
                # This convert Ansible Check Mode to dry_run
                dry_run=ansible_check_mode,
                yaml_dumper=AnsibleNoAliasDumper,
            )
            # Call the function to handle temp file creation
            temp_file_path = _create_temp_file(hostname, anta_results)

            # Copy the temp file to the result_path if provided
            if result_path:
                copy2(temp_file_path, result_path)

        except Exception as error:
            raise AnsibleActionFail(message=str(error)) from error

        # Add the temp file path to the Ansible result
        result["results_temp_file"] = temp_file_path

        if cprofile_file:
            profiler.disable()
            stats = pstats.Stats(profiler).sort_stats("cumtime")
            stats.dump_stats(cprofile_file)

        return result


def _create_temp_file(hostname: str, anta_results: list[dict]) -> str:
    """Create a temporary JSON file to save all test results from ANTA.

    The temp file is saved in `/tmp` with a prefix of `<hostname>_` and `.json` extension.

    Args:
    ----
      hostname (str): Current inventory device that is running the plugin.
      anta_results (list[dict]): The list of ANTA results that will be saved in the JSON file.

    Returns:
    -------
      str: The absolute path of the temp file.
    """
    # Create the temp JSON file to save the ANTA results
    with NamedTemporaryFile(mode="w", encoding="UTF-8", suffix=".json", prefix=f"{hostname}_", delete=False) as temp_file:
        # Serialize to JSON and write to the temp file
        temp_file.write(dumps(anta_results, indent=2, sort_keys=False))
        return temp_file.name


def setup_module_logging(hostname: str, result: dict) -> None:
    """Create a Filter to add the hostname to generate logs.

    Add a Handler to copy the logs from the plugin into Ansible output based on their level

    Args:
    ----
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
