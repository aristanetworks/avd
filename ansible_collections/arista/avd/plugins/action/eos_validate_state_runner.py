# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, annotations, division, print_function

__metaclass__ = type

import cProfile
import logging
import pstats
from json import dump, dumps
from pathlib import Path
from tempfile import NamedTemporaryFile

from ansible.errors import AnsibleActionFail
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils import AnsibleEOSDevice, get_anta_results
from ansible_collections.arista.avd.plugins.plugin_utils.utils import PythonToAnsibleContextFilter, PythonToAnsibleHandler

LOGGER = logging.getLogger("ansible_collections.arista.avd")
# ANTA currently add some RichHandler to the root logger so need to disable propagation
LOGGER.propagate = False
LOGGING_LEVELS = ["DEBUG", "INFO", "ERROR", "WARNING", "CRITICAL"]


class AnsibleNoAliasDumper(AnsibleDumper):
    def ignore_aliases(self, data):
        return True


class ActionModule(ActionBase):
    def _get_and_validate_arg(
        self, argument: str, expected_type: type, default_value: bool | list | str | None = None, allowed_values: list[str] | None = None
    ) -> bool | list | str:
        """Validate a task argument, returns the value if the validation succeeds."""
        result = self._task.args.get(argument, default_value)
        if not isinstance(result, expected_type) or (allowed_values and result not in allowed_values):
            allowed = f" in {allowed_values}" if allowed_values else ""
            raise AnsibleActionFail(f"'{argument}' must be a {expected_type.__name__}{allowed}, got {result}.")
        return result

    def _get_and_validate_dir_arg(self, argument: str) -> str:
        """Validate if a task directory argument is valid and exists, returns the value if the validation succeeds."""
        result = self._task.args.get(argument)
        if not isinstance(result, str) or not Path(result).exists():
            raise AnsibleActionFail(f"'{argument}' must be a valid directory path and must exist.")
        return result

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
        logging_level = self._get_and_validate_arg(argument="logging_level", expected_type=str, default_value="WARNING", allowed_values=LOGGING_LEVELS)
        skipped_tests = self._get_and_validate_arg(argument="skipped_tests", expected_type=list, default_value=[])
        save_catalog = self._get_and_validate_arg(argument="save_catalog", expected_type=bool, default_value=False)
        save_results = self._get_and_validate_arg(argument="save_results", expected_type=bool, default_value=False)
        save_catalog_name = Path(self._get_and_validate_dir_arg(argument="device_catalog_output_dir")) / f"{hostname}-catalog.yml" if save_catalog else None
        save_results_name = Path(self._get_and_validate_dir_arg(argument="device_results_output_dir")) / f"{hostname}-results.json" if save_results else None

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
            temp_file_name = _create_temp_file(hostname, anta_results)

            # Save test results
            if save_results_name:
                with Path(save_results_name).open("w", encoding="UTF-8") as results_file:
                    dump(anta_results, results_file, indent=2, sort_keys=False)

        except Exception as error:
            raise AnsibleActionFail(message=str(error)) from error

        # Add the temp file path to the Ansible result
        result["results_temp_file"] = temp_file_name

        if cprofile_file:
            profiler.disable()
            stats = pstats.Stats(profiler).sort_stats("cumtime")
            stats.dump_stats(cprofile_file)

        return result


def _create_temp_file(hostname: str, anta_results: list[dict]) -> str:
    """Create a temporary JSON file to save all test results from ANTA.

    The function will also search for leftover temp files in the `/tmp` folder and delete them.

    The temp file is saved in `/tmp` with a prefix of `<hostname>_` and `.json` extension.

    Args:
    ----
      hostname (str): Current inventory device that is running the plugin.
      anta_results (list[dict]): The list of ANTA results that will be saved in the JSON file.

    Returns:
    -------
      str: The absolute path of the temp file.
    """
    temp_file_prefix = f"{hostname}_"
    temp_file_directory = Path("/tmp")

    # Search for leftover temp files with the hostname prefix and delete them.
    for file in temp_file_directory.glob(f"{temp_file_prefix}*"):
        file.unlink(missing_ok=True)

    # Create the temp JSON file to save the ANTA results
    with NamedTemporaryFile(mode="w", encoding="UTF-8", suffix=".json", prefix=f"{hostname}_", dir=str(temp_file_directory), delete=False) as temp_file:
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
