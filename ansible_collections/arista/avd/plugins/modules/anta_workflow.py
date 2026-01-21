# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
ANSIBLE_METADATA = {"metadata_version": "1.0", "status": ["preview"]}

DOCUMENTATION = r"""
---
module: anta_workflow
version_added: "5.3.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Uses ANTA from Ansible
description: |-
  The `arista.avd.anta_workflow` module is an Ansible Action Plugin to leverage the ANTA test
  framework to validate that the generated structured configurations by AVD are applied to the
  devices and that the deployed network is working correctly. It can also be used to execute
  user-defined ANTA test catalogs in conjunction with the Ansible inventory, providing similar
  functionality and options as the ANTA CLI while benefiting from Ansible's inventory management
  capabilities.

  The plugin offers the following capabilities:

  - Generating a per-device test catalog based on the AVD structured configuration.
  - Running AVD-generated test catalogs against the devices.
  - Running user-defined test catalogs against the devices.
  - Generating reports in various formats.
  - In dry-run mode, only the test catalogs are generated, and a report is created to preview the tests that would be run against each device.
options:
  device_list:
    description: List of devices to run ANTA tests against. These devices must be defined in the Ansible inventory.
    type: list
    required: true
    elements: str
  avd_catalogs:
    description: AVD-generated test catalogs settings. These settings are used to generate test catalogs based on the AVD structured configurations.
    type: dict
    suboptions:
      enabled:
        description: Enable AVD catalogs generation. Can be disabled if only user-defined catalogs are to be run.
        type: bool
        default: true
      output_dir:
        description: Directory where the AVD-generated test catalogs will be stored.
        type: str
      structured_config_dir:
        description: Path to the directory containing the AVD structured configurations per device.
        type: str
      structured_config_suffix:
        description: File suffix for AVD structured configuration files.
        type: str
        default: "yml"
        choices: ["yml", "yaml", "json"]
      extra_fabric_validation:
        description: If `true`, generate extra fabric-wide validation tests (e.g., reachability and routing tests).
        type: bool
        default: false
      filters:
        description: Filters used to run or skip tests from the AVD-generated test catalogs. These filters do not apply to user-defined catalogs.
        type: list
        elements: dict
        suboptions:
          device_list:
            description: List of devices to apply the filters to.
            type: list
            elements: str
          run_tests:
            description: List of ANTA tests to only include in the AVD-generated catalogs.
            type: list
            elements: str
          skip_tests:
            description: List of ANTA tests to exclude from the AVD-generated catalogs. `skip_tests` takes precedence over `run_tests`.
            type: list
            elements: str
  user_catalogs:
    description: User-defined test catalogs settings. These settings are used to run user-provided ANTA catalogs against the devices.
    type: dict
    suboptions:
      enabled:
        description: Enable used-defined catalogs generation.
        type: bool
        default: false
      input_dir:
        description: Directory containing the user-defined ANTA test catalogs.
        type: str
  runner:
    description: ANTA runner settings. These settings change the behavior of the ANTA runner.
    type: dict
    suboptions:
      timeout:
        description: Global timeout in seconds for API calls to the devices. Can be adjusted depending on the amount of devices and tests.
        type: float
        default: 30.0
      batch_size:
        description: Number of devices to run per ANTA instance. This can be increased based on the available resources of the Ansible runner.
        type: int
        default: 5
      tags:
        description: |-
          List of tags used with user-defined catalogs to filter which tests to run on which devices.
          These tags are used in conjunction with `anta_tags` variable assigned to devices in the Ansible inventory.
        type: list
        elements: str
      dry_run:
        description: |-
          Run ANTA in dry-run mode. In this mode, only the test catalogs are generated,
          and a report is created to preview the tests that would be run against each device.
        type: bool
        default: false
  report:
    description: ANTA report settings. These settings define the output format and location of the ANTA reports.
    type: dict
    suboptions:
      expand_results:
        description: |-
          Controls the granularity of the Markdown report.
          When enabled, test entries are expanded to show the individual status of every check performed.
          Not all ANTA tests currently support expanded results. For tests that do not support this feature yet,
          the report will display the standard aggregated result regardless of this setting.
        type: bool
        default: false
      generate_custom_field:
        description: |
          Controls whether the `custom_field` column is generated in the Markdown report.
          ANTA test definitions can include an arbitrary string in the `custom_field` input that will be added to the test result.
        type: bool
        default: false
      csv_output:
        description: Path to the CSV report file.
        type: str
      md_output:
        description: Path to the Markdown report file.
        type: str
      json_output:
        description: Path to the JSON report file.
        type: str
      filters:
        description: Filters used to hide specific test statuses from the reports.
        type: dict
        suboptions:
          exclude_statuses:
            description: List of test statuses to exclude from the reports.
            type: list
            elements: str
            choices: ["success", "failure", "error", "skipped", "unset"]
      sorting:
        description: Sorting options to apply to test results.
        type: dict
        suboptions:
          status_priority:
            description: List of test statuses that defines the primary grouping order of the test results.
            type: list
            elements: str
            choices: ["error", "failure", "skipped", "success", "unset"]
            default: ["error", "failure", "skipped", "success", "unset"]
          sort_fields:
            description: List of result attributes used to sort tests within each status group.
            type: list
            elements: str
            choices: ["categories", "custom_field", "description", "device", "test"]
            default: ["device", "categories", "test", "description", "custom_field"]
seealso:
  - name: ANTA website
    description: Documentation for the ANTA test framework
    link: https://anta.arista.com
"""

EXAMPLES = r"""
- name: Run ANTA
  hosts: FABRIC
  connection: local
  gather_facts: false
  tasks:
    - name: Run ANTA workflow
      run_once: true
      delegate_to: localhost
      arista.avd.anta_workflow:
        device_list: "{{ ansible_play_hosts }}"
        avd_catalogs:
          enabled: true
          output_dir: "{{ inventory_dir }}/anta/avd_catalogs"
          structured_config_dir: "{{ inventory_dir }}/intended/structured_configs"
          # structured_config_suffix: ".yml"
          # filters:
          #   - device_list: "{{ groups['DC1'] }}"
          #     skip_tests:
          #       - VerifyNTP
          # extra_fabric_validation: true
        user_catalogs:
          enabled: true
          input_dir: "{{ inventory_dir }}/anta/user_catalogs"
        runner:
          timeout: 360.0
          batch_size: 10
          # tags:
          #   - leaf
          # dry_run: true
        report:
          csv_output: "{{ inventory_dir }}/anta/reports/anta_report.csv"
          md_output: "{{ inventory_dir }}/anta/reports/anta_report.md"
          json_output: "{{ inventory_dir }}/anta/reports/anta_report.json"
          # filters:
          #   exclude_statuses:
          #     - success
          #     - skipped
          # sorting:
          #   status_priority:
          #     - failure
          #     - error
          #     - skipped
          #   sort_fields:
          #     - categories
          # expand_results: true
          # generate_custom_field: true
"""
