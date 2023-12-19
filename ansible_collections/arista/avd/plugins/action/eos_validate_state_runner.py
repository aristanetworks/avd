# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, annotations, division, print_function

__metaclass__ = type

import logging
from json import dump
from typing import TYPE_CHECKING

from ansible.errors import AnsibleActionFail
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils import AnsibleEOSDevice, get_anta_results
from ansible_collections.arista.avd.plugins.plugin_utils.utils import (
    PythonToAnsibleContextFilter,
    PythonToAnsibleHandler,
    get_validated_path,
    get_validated_value,
)

if TYPE_CHECKING:
    from pathlib import Path

LOGGER = logging.getLogger("ansible_collections.arista.avd")
# ANTA currently add some RichHandler to the root logger so need to disable propagation
LOGGER.propagate = False
LOGGING_LEVELS = ["DEBUG", "INFO", "ERROR", "WARNING", "CRITICAL"]


class AnsibleNoAliasDumper(AnsibleDumper):
    def ignore_aliases(self, data):
        return True


class ActionModule(ActionBase):
    # @cprofile
    def run(self, tmp=None, task_vars=None):
        self._supports_check_mode = True

        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

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
        try:
            logging_level = get_validated_value(
                data=self._task.args, key="logging_level", expected_type=str, default_value="WARNING", allowed_values=LOGGING_LEVELS
            )
            skipped_tests = get_validated_value(data=self._task.args, key="skipped_tests", expected_type=list, default_value=[])
            save_catalog = get_validated_value(data=self._task.args, key="save_catalog", expected_type=bool, default_value=False)
            catalog_path = get_validated_path(path_input=self._task.args.get("device_catalog_path"), parent=True) if save_catalog else None
            test_results_dir = get_validated_path(path_input=self._task.args.get("test_results_dir"), parent=False)
        except (TypeError, ValueError, FileNotFoundError) as error:
            msg = f"Failed to validate task arguments: {error}"
            raise AnsibleActionFail(msg) from error

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

            # Write the results to a JSON file
            write_results(hostname=hostname, anta_results=anta_results, test_results_dir=test_results_dir)

        except Exception as error:
            msg = f"Error during plugin execution: {error}"
            raise AnsibleActionFail(msg) from error

        return result


def write_results(hostname: str, anta_results: list[dict], test_results_dir: Path) -> None:
    """Save all test results from ANTA to a JSON file.

    The JSON file name is hard coded here to make sure we can retrieve it in the report plugin.

    Args:
    ----
      hostname (str): Current inventory device that is running the plugin.
      anta_results (list[dict]): The list of ANTA results that will be saved in the JSON file.
      test_results_dir (Path): The test results directory where the results will be saved.
    """
    result_path = test_results_dir / f"{hostname}-results.json"
    with result_path.open(mode="w", encoding="UTF-8") as result_file:
        dump(anta_results, result_file, indent=2, sort_keys=False)


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
