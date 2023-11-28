# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

# NOTE: This is supposed to be deprecated as per
# https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_documenting.html#ansible-metadata-block
# But our doc Jinja2 template renders it as preview which is what we want
ANSIBLE_METADATA = {"metadata_version": "1.0", "status": ["preview"]}

DOCUMENTATION = r"""
---
module: eos_validate_state_runner
version_added: "4.4.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Utilizes ANTA for eos_validate_state role validation
description:
  - The C(arista.avd.eos_validate_state_runner) module is an Ansible Action Plugin leveraging the ANTA test
    framework to validate that the generated structured configurations by AVD are applied to the devices and
    that the deployed network is working correctly.
  - This plugin requires that structured_configs for each device be present in hostvars; otherwise, no tests will be executed.
  - |-
    The plugin offers the following capabilities:
        - Generating a per-device test catalog based on the AVD structured_config.
        - Running generated tests against each device, saving the results in a temporary JSON file,
          and recording the file path in hostvars for use by the report plugin.
        - In check_mode, only the test catalog is generated, and a report is created to preview the tests that would be run against each device.
        - Saving per-device test catalogs and results to specified directories.
        - Maintaining backward compatibility with existing ansible tags for eos_validate_state to filter test categories.
options:
  logging_level:
    description: Sets the log level for the ANTA library. Defaults to "WARNING" if not specified.
    type: str
    choices: ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]
    default: "WARNING"
  save_catalog:
    description: Indicates whether to save the test catalog for each device.
    type: bool
    default: false
  save_results:
    description: Indicates whether to save test results in a JSON file for each device.
    type: bool
    default: false
  device_catalog_output_dir:
    description:
      - The directory where device test catalogs will be saved.
      - Required if C(save_catalog) is set to C(True).
    type: str
  device_results_output_dir:
    description:
      - The directory where device test results will be saved.
      - Required if C(save_results) is set to C(True).
    type: str
  skipped_tests:
    description:
      - A list of dictionaries specifying categories and tests to skip.
      - Each dictionary should have keys C(category) and C(tests).
    type: list
    elements: dict
    suboptions:
      category:
        type: str
        description: The name of an AvdTest category (e.g., C(AvdTestHardware)).
      tests:
        type: list
        elements: str
        description: A list of specific tests in the category (e.g., C(VerifyRoutingProtocolModel) in C(AvdTestBGP)).
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
  - The plugin manages the creation and cleanup of temporary JSON files used for storing test results.
  - This module supports C(check_mode), allowing the generation of test reports without executing the tests.
"""

EXAMPLES = r"""
- name: Execute eos_validate_state_runner leveraging ANTA
  arista.avd.eos_validate_state_runner:
    logging_level: ERROR
    save_catalog: true
    save_results: false
    device_catalog_output_dir: "/git_projects/my_avd_project/intended/test_catalogs"
    device_results_output_dir: "/git_projects/my_avd_project/reports/test_results"
    skipped_tests:
      - category: AvdTestHardware
      - category: AvdTestBGP
        tests:
          - VerifyRoutingProtocolModel
  register: anta_results
"""
