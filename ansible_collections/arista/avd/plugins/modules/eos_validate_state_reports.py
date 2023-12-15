# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

# NOTE: This is supposed to be deprecated as per
# https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_documenting.html#ansible-metadata-block
# But our doc Jinja2 template renders it as preview which is what we want
ANSIBLE_METADATA = {"metadata_version": "1.0", "status": ["preview"]}

DOCUMENTATION = r"""
---
module: eos_validate_state_reports
version_added: "4.5.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Generates validation reports for the eos_validate_state role
description:
  - The C(arista.avd.eos_validate_state_reports) module is an Ansible Action Plugin designed to generate
    validation reports from the test results produced by the ANTA test framework.
  - This plugin requires a JSON file for each host in the Ansible play, containing all test results. The JSON file
    is created automatically by the C(eos_validate_state_runner) plugin and is saved in the test results directory
    with the following naming convention C(<inventory_hostname>-results.json).
  - |-
    The plugin offers the following functionalities:
      - It aggregates all test results from every host in the Ansible play and generates a CSV report.
      - It produces a detailed Markdown report with various sections presenting key statistics derived from the results.
      - The design allows for easy extension to support additional report formats in the future.
options:
  validation_report_csv:
    description: Indicates whether a CSV report should be generated.
    type: bool
    default: true
  validation_report_md:
    description: Indicates whether a Markdown report should be generated.
    type: bool
    default: true
  only_failed_tests:
    description: Determines if the generated reports should include only the failed tests.
    type: bool
    default: false
  csv_report_path:
    description:
      - The absolute path where the CSV report will be saved.
      - Required if C(validation_report_csv) is set to C(True).
    type: str
  md_report_path:
    description:
      - The absolute path where the Markdown report will be saved.
      - Required if C(validation_report_md) is set to C(True).
    type: str
  test_results_dir:
    description:
    - The directory where the test results JSON file for each host will be saved.
  cprofile_file:
    description:
      - The filename for storing cProfile data, useful for debugging performance issues.
      - Be aware that enabling cProfile can affect performance, so use it only for troubleshooting.
seealso:
  - name: ANTA website
    description: Documentation for the ANTA test framework
    link: https://anta.ninja
notes:
  - Enabling the cProfile feature for performance profiling may impact the plugin's performance, especially in production environments.
  - Hosts with C(is_deployed) is False are automatically skipped, and no test results are processed for these hosts.
"""

EXAMPLES = r"""
- name: Generate validation reports from ANTA test results
  arista.avd.eos_validate_state_reports:
    csv_report_path: "/my_avd_project/reports/my-fabric-state.csv"
    md_report_path: "/my_avd_project/reports/my-fabric-state.md"
    validation_report_csv: true
    validation_report_md: true
    only_failed_tests: false
  delegate_to: localhost
  run_once: true
"""
