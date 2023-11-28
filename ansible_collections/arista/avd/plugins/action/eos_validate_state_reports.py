# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, annotations, division, print_function

__metaclass__ = type

import cProfile
import pstats
from json import load
from pathlib import Path
from typing import Generator

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils import CSVReport, ResultsManager, ValidateStateReport
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


def _test_results_gen(input_path: str) -> Generator[dict, None, None]:
    """Generate test results from a JSON file for a specific host.

    This function opens the JSON temporary file created by the `eos_validate_state_runner` action plugin
    and yields each test result as a dictionary.

    Args:
    ----
      input_path (str): Path to the temporary JSON file containing test results for a host.

    Yields:
    ------
      Generator[dict, None, None]: Test result as a dictionary.
    """
    with Path(input_path).open(encoding="UTF-8") as file:
        yield from load(file)


class ActionModule(ActionBase):
    def _get_and_validate_bool_arg(self, argument: str, *, default_value: bool) -> bool:
        """Validate if a task argument is a boolean, returns the value if the validation succeeds."""
        result = self._task.args.get(argument, default_value)
        if not isinstance(result, bool):
            raise AnsibleActionFail(f"'{argument}' must be a boolean, got {result}.")
        return result

    def _get_and_validate_path_arg(self, argument: str) -> str:
        """Validate if a task path argument is valid and exists, returns the value if the validation succeeds."""
        result = self._task.args.get(argument)
        if not isinstance(result, str) or not Path(result).parent.exists():
            raise AnsibleActionFail(f"'{argument}' must be a valid path and its directory must exist.")
        return result

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        # Profiling
        cprofile_file = self._task.args.get("cprofile_file")
        if cprofile_file:
            profiler = cProfile.Profile()
            profiler.enable()

        # Get task arguments and validate them
        only_failed_tests = self._get_and_validate_bool_arg(argument="only_failed_tests", default_value=False)
        validation_report_csv = self._get_and_validate_bool_arg(argument="validation_report_csv", default_value=True)
        validation_report_md = self._get_and_validate_bool_arg(argument="validation_report_md", default_value=True)

        if validation_report_csv:
            csv_report_path = self._get_and_validate_path_arg("csv_report_path")
        if validation_report_md:
            md_report_path = self._get_and_validate_path_arg("md_report_path")

        # This is not all the hostvars, but just the Ansible Hostvars Manager object where we can retrieve hostvars for each host on-demand
        hostvars = task_vars["hostvars"]
        # For now we support the existing behavior of eos_validate_state, all hosts from the play
        ansible_play_hosts_all = task_vars.get("ansible_play_hosts_all", [])
        # List to track all results temp files for each host
        temp_files = []

        try:
            # Initialize an empty ResultsManager that will be used to store results and statistics
            test_results = ResultsManager(only_failed_tests=only_failed_tests)
            for host in sorted(ansible_play_hosts_all):
                host_hostvars = hostvars[host]
                # Hosts marked as not deployed do not have any results
                if not get(host_hostvars, "is_deployed", default=True):
                    display.warning(f"No test results for host {host} since it's marked as not deployed.")
                    continue
                # Getting the host results temp file saved by eos_validate_state_runner action plugin
                temp_file = get(host_hostvars, "anta_results.results_temp_file")
                if not isinstance(temp_file, str) or not Path(temp_file).exists():
                    display.warning(f"Results temporary file path is invalid or does not exist for host {host}.")
                    continue
                # Track the temp file
                temp_files.append(temp_file)

                try:
                    # Process the host test results
                    for test_result in _test_results_gen(temp_file):
                        test_results.update_results(test_result)
                except Exception as error:
                    display.warning(f"Error while processing the test results of host {host}: {error}.")

            # Generate the reports
            if validation_report_csv:
                with Path(csv_report_path).open("w", encoding="UTF-8") as report_file:
                    csv_report = CSVReport(report_file, test_results)
                    csv_report.generate_report()
            if validation_report_md:
                with Path(md_report_path).open("w", encoding="UTF-8") as report_file:
                    md_report = ValidateStateReport(report_file, test_results)
                    md_report.generate_report()

        except Exception as error:
            raise AnsibleActionFail(f"Error during plugin execution: {error}") from error
        finally:
            # Cleanup for each host's temporary file
            for file_path in temp_files:
                Path(file_path).unlink(missing_ok=True)

        if cprofile_file:
            profiler.disable()
            stats = pstats.Stats(profiler).sort_stats("cumtime")
            stats.dump_stats(cprofile_file)

        return result
