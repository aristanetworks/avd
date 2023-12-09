# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, annotations, division, print_function

__metaclass__ = type

import cProfile
import pstats
from json import JSONDecodeError, load
from pathlib import Path
from typing import Generator

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils import CSVReport, MDReport, ResultsManager
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_and_validate, verify_and_return_path


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
    try:
        with Path(input_path).open(encoding="UTF-8") as file:
            yield from load(file)
    except (JSONDecodeError, UnicodeDecodeError, OSError) as error:
        error_message = f"{error.__class__.__name__}: {error}"
        raise AristaAvdError(error_message) from error


class ActionModule(ActionBase):
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
        only_failed_tests = get_and_validate(data=self._task.args, key="only_failed_tests", expected_type=bool, default_value=False)
        validation_report_csv = get_and_validate(data=self._task.args, key="validation_report_csv", expected_type=bool, default_value=True)
        validation_report_md = get_and_validate(data=self._task.args, key="validation_report_md", expected_type=bool, default_value=True)
        csv_report_path = verify_and_return_path(path_input=self._task.args.get("csv_report_path")) if validation_report_csv else None
        md_report_path = verify_and_return_path(path_input=self._task.args.get("md_report_path")) if validation_report_md else None

        # This is not all the hostvars, but just the Ansible Hostvars Manager object where we can retrieve hostvars for each host on-demand
        hostvars = task_vars["hostvars"]
        # For now we support the existing behavior of eos_validate_state, all hosts from the play
        ansible_play_hosts_all = task_vars.get("ansible_play_hosts_all", [])
        # List to track each host results temporary file
        temp_files = []

        try:
            # Initialize an empty ResultsManager that will be used to store results and statistics
            test_results = ResultsManager(only_failed_tests=only_failed_tests)
            for host in sorted(ansible_play_hosts_all):
                host_hostvars = hostvars[host]
                # Hosts marked as not deployed do not have any results
                if not get(host_hostvars, "is_deployed", default=True):
                    display.warning(f"No test results for host {host} since 'is_deployed' is False.")
                    continue
                try:
                    # Getting the host results temp file saved by eos_validate_state_runner action plugin
                    temp_file = get(host_hostvars, "anta_results.results_temp_file")
                    verify_and_return_path(path_input=temp_file)
                except (TypeError, FileNotFoundError) as error:
                    display.warning(str(error))
                    continue

                # Track the temp file
                temp_files.append(temp_file)

                try:
                    # Process the host test results
                    for test_result in _test_results_gen(temp_file):
                        test_results.update_results(test_result)
                except AristaAvdError as error:
                    display.warning(f"Exception raised while processing the test results of host {host}: {error}.")

            # Generate the reports
            if validation_report_csv:
                with Path(csv_report_path).open("w", encoding="UTF-8") as report_file:
                    csv_report = CSVReport(report_file, test_results)
                    csv_report.generate_report()
            if validation_report_md:
                with Path(md_report_path).open("w", encoding="UTF-8") as report_file:
                    md_report = MDReport(report_file, test_results)
                    md_report.generate_report()

        except Exception as error:
            raise AnsibleActionFail(f"Error during plugin execution: {error}") from error
        finally:
            # Cleanup temporary files
            for file_path in temp_files:
                Path(file_path).unlink(missing_ok=True)

        if cprofile_file:
            profiler.disable()
            stats = pstats.Stats(profiler).sort_stats("cumtime")
            stats.dump_stats(cprofile_file)

        return result
