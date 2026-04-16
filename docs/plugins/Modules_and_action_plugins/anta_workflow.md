---
# This title is used for search results
title: arista.avd.anta_workflow
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# anta_workflow

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.anta_workflow` when using this plugin.

!!! warning "This module is in **preview** mode"
    This module is not guaranteed to have a backwards compatible interface.

Uses ANTA from Ansible

## Synopsis

The `arista.avd.anta_workflow` module is an Ansible Action Plugin to leverage the ANTA test
framework to validate that the generated structured configurations by AVD are applied to the
devices and that the deployed network is working correctly. It can also be used to execute
user-defined ANTA test catalogs in conjunction with the Ansible inventory, providing similar
functionality and options as the ANTA CLI while benefiting from Ansible&#39;s inventory management
capabilities.

The plugin offers the following capabilities:

- Generating a per-device test catalog based on the AVD structured configuration.
- Running AVD-generated test catalogs against the devices.
- Running user-defined test catalogs against the devices.
- Generating reports in various formats.
- In dry-run mode, only the test catalogs are generated, and a report is created to preview the tests that would be run against each device.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>device_list</samp> | list | True | None | - | List of devices to run ANTA tests against. These devices must be defined in the Ansible inventory. |
| <samp>avd_catalogs</samp> | dict | optional | None | - | AVD-generated test catalogs settings. These settings are used to generate test catalogs based on the AVD structured configurations. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | bool | optional | True | - | Enable AVD catalogs generation. Can be disabled if only user-defined catalogs are to be run. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;output_dir</samp> | str | optional | None | - | Directory where the AVD-generated test catalogs will be stored. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config_dir</samp> | str | optional | None | - | Path to the directory containing the AVD structured configurations per device. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config_suffix</samp> | str | optional | yml | Valid values:<br>- <code>yml</code><br>- <code>yaml</code><br>- <code>json</code> | File suffix for AVD structured configuration files. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;extra_fabric_validation</samp> | bool | optional | False | - | If `true`, generate extra fabric-wide validation tests (e.g., reachability and routing tests). |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;filters</samp> | list | optional | None | - | Filters used to run or skip tests from the AVD-generated test catalogs. These filters do not apply to user-defined catalogs. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;device_list</samp> | list | optional | None | - | List of devices to apply the filters to. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;run_tests</samp> | list | optional | None | - | List of ANTA tests to only include in the AVD-generated catalogs. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;skip_tests</samp> | list | optional | None | - | List of ANTA tests to exclude from the AVD-generated catalogs. `skip_tests` takes precedence over `run_tests`. |
| <samp>user_catalogs</samp> | dict | optional | None | - | User-defined test catalogs settings. These settings are used to run user-provided ANTA catalogs against the devices. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | bool | optional | False | - | Enable used-defined catalogs generation. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;input_dir</samp> | str | optional | None | - | Directory containing the user-defined ANTA test catalogs. |
| <samp>runner</samp> | dict | optional | None | - | ANTA runner settings. These settings change the behavior of the ANTA runner. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp> | float | optional | 30.0 | - | Global timeout in seconds for API calls to the devices. Can be adjusted depending on the amount of devices and tests. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;batch_size</samp> | int | optional | 5 | - | Number of devices to run per ANTA instance. This can be increased based on the available resources of the Ansible runner. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;tags</samp> | list | optional | None | - | List of tags used with user-defined catalogs to filter which tests to run on which devices.<br>These tags are used in conjunction with `anta_tags` variable assigned to devices in the Ansible inventory. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;dry_run</samp> | bool | optional | False | - | Run ANTA in dry-run mode. In this mode, only the test catalogs are generated,<br>and a report is created to preview the tests that would be run against each device. |
| <samp>report</samp> | dict | optional | None | - | ANTA report settings. These settings define the output format and location of the ANTA reports. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;expand_results</samp> | bool | optional | False | - | Controls the granularity of the Markdown report.<br>When enabled, test entries are expanded to show the individual status of every check performed.<br>Not all ANTA tests currently support expanded results. For tests that do not support this feature yet,<br>the report will display the standard aggregated result regardless of this setting. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;generate_custom_field</samp> | bool | optional | False | - | Controls whether the `custom_field` column is generated in the Markdown report.<br>ANTA test definitions can include an arbitrary string in the `custom_field` input that will be added to the test result. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;csv_output</samp> | str | optional | None | - | Path to the CSV report file. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;md_output</samp> | str | optional | None | - | Path to the Markdown report file. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;json_output</samp> | str | optional | None | - | Path to the JSON report file. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;filters</samp> | dict | optional | None | - | Filters used to hide specific test statuses from the reports. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exclude_statuses</samp> | list | optional | None | Valid values:<br>- <code>success</code><br>- <code>failure</code><br>- <code>error</code><br>- <code>skipped</code><br>- <code>unset</code> | List of test statuses to exclude from the reports. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;sorting</samp> | dict | optional | None | - | Sorting options to apply to test results. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;status_priority</samp> | list | optional | ['error', 'failure', 'skipped', 'success', 'unset'] | Valid values:<br>- <code>error</code><br>- <code>failure</code><br>- <code>skipped</code><br>- <code>success</code><br>- <code>unset</code> | List of test statuses that defines the primary grouping order of the test results. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sort_fields</samp> | list | optional | ['device', 'categories', 'test', 'description', 'custom_field'] | Valid values:<br>- <code>categories</code><br>- <code>custom_field</code><br>- <code>description</code><br>- <code>device</code><br>- <code>test</code> | List of result attributes used to sort tests within each status group. |

## See Also

- ANTA website: [https://anta.arista.com](https://anta.arista.com)<br>Documentation for the ANTA test framework

## Examples

```yaml
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
```

## Authors

- Arista Ansible Team (@aristanetworks)
