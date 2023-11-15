# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, annotations, division, print_function

__metaclass__ = type

from pathlib import Path
from typing import Generator

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display
from yaml import safe_load_all

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.csv_report import CSVReport
from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.md_report import ValidateStateReport
from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.results_manager import ResultsManager
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


def _test_results_stream(input_path: str) -> Generator[dict, None, None]:
    """
    Streams test results from a YAML file for a specific host.

    Each YAML document in the file represents a single test result. This function
    opens the temporary file created by the `eos_validate_state_runner` action plugin,
    reads it, and yields each test result as a dictionary.

    Args:
      input_path (str): Path to the temporary YAML file containing test results for a host.

    Yields:
      Generator[dict, None, None]: Test result as a dictionary.
    """
    with open(input_path, "r", encoding="UTF-8") as file:
        yield from safe_load_all(stream=file)


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        # Get task arguments and validate them
        only_failed_tests = self._task.args.get("only_failed_tests", False)
        if not isinstance(only_failed_tests, bool):
            raise AnsibleActionFail(f"'only_failed_tests' must be a boolean, got {only_failed_tests}.")

        validation_report_csv = self._task.args.get("validation_report_csv", True)
        if not isinstance(validation_report_csv, bool):
            raise AnsibleActionFail(f"'validation_report_csv' must be a boolean, got {validation_report_csv}.")

        validation_report_md = self._task.args.get("validation_report_md", True)
        if not isinstance(validation_report_md, bool):
            raise AnsibleActionFail(f"'validation_report_md' must be a boolean, got {validation_report_md}.")

        if validation_report_csv:
            csv_report_path = self._task.args.get("csv_report_path")
            if not isinstance(csv_report_path, str) or not Path(csv_report_path).parent.exists():
                raise AnsibleActionFail("'csv_report_path' must be a valid path and his directory must exist.")

        if validation_report_md:
            md_report_path = self._task.args.get("md_report_path")
            if not isinstance(md_report_path, str) or not Path(md_report_path).parent.exists():
                raise AnsibleActionFail("'md_report_path' must be a valid path and his directory must exist.")

        # This is not all the hostvars, but just the Ansible Hostvars Manager object where we can retrieve hostvars for each host on-demand
        hostvars = task_vars["hostvars"]

        # For now we support the existing behavior of eos_validate_state, all hosts from the play
        ansible_play_hosts_all = task_vars.get("ansible_play_hosts_all", [])

        # Initialize an empty ResultsManager that will be used to store results and statistics
        try:
            test_results = ResultsManager(only_failed_tests=only_failed_tests)
        except Exception as error:
            raise AnsibleActionFail(f"Error while initializing ResultsManager: {str(error)}") from error

        for host in sorted(ansible_play_hosts_all):
            # Getting the host results temp file saved by eos_validate_state_runner action plugin
            temp_file = get(hostvars[host], "anta_results.results_temp_file")
            if not isinstance(temp_file, str) or not Path(temp_file).exists():
                display.warning(f"Results temporary file path is invalid or does not exist for host {host}.")
                continue
            try:
                # Process the host test results
                for test_result in _test_results_stream(temp_file):
                    test_results.update_results(test_result)
            except Exception as error:
                display.warning(f"Error while processing the test results of host {host}: {str(error)}")

            # Delete the host results temp file
            Path(temp_file).unlink()

        try:
            # Generate the CSV report
            if validation_report_csv:
                with open(csv_report_path, "w", encoding="UTF-8", newline="\n") as csvfile:
                    csv_report = CSVReport(csvfile=csvfile, results=test_results)
                    csv_report.generate_report()

            # Generate the MD report
            if validation_report_md:
                with open(md_report_path, "w", encoding="UTF-8") as mdfile:
                    md_report = ValidateStateReport(mdfile=mdfile, results=test_results)
                    md_report.generate_report()
        except Exception as error:
            raise AnsibleActionFail(f"Error while generating the reports: {str(error)}") from error

        # Make sure the ResultsManager temp file is getting closed and deleted
        if test_results.tmp_test_results_file and not test_results.tmp_test_results_file.closed:
            test_results.tmp_test_results_file.close()

        return result
