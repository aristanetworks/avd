# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

# NOTE that this is supposed to be deprecated as per
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
  - The C(arista.avd.eos_validate_state_reports) module, an Ansible Action Plugin, is designed to generate
    validation reports from the test results produced by the ANTA test framework.
  - This plugin requires a temporary JSON file for each host in the Ansible play, which contains all test results.
    The path to this temporary JSON file, used by the plugin, is supplied in the hostvars by the `eos_validate_state_runner` plugin.
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
      - Specifies the absolute path where the CSV report will be saved.
      - Required if C(validation_report_csv) is set to C(True).
    type: str
  md_report_path:
    description:
      - Specifies the absolute path where the Markdown report will be saved.
      - Required if C(validation_report_md) is set to C(True).
    type: str
  cprofile_file:
    description:
      - Specifies the filename for storing cProfile data, which aids in debugging performance issues.
      - Note that enabling cProfile can itself impact performance, so it should only be used for troubleshooting.
seealso:
  - name: ANTA website
    description: Documentation for the ANTA test framework
    link: https://anta.ninja
notes:
  - Enabling the cProfile feature for performance profiling may impact the plugin's performance, especially in production environments.
  - The plugin manages temporary files created for processing test results, ensuring clean-up post-execution.
  - Hosts marked as not deployed are automatically skipped, and no test results are processed for these hosts.
"""

EXAMPLES = r"""
- name: Generate validation reports from ANTA test results
  arista.avd.eos_validate_state_reports:
    csv_report_path: "/git_projects/my_avd_project/reports/my-fabric-state.csv"
    md_report_path: "/git_projects/my_avd_project/reports/my-fabric-state.md"
    validation_report_csv: true
    validation_report_md: true
    only_failed_tests: false
  delegate_to: localhost
  run_once: true
"""
