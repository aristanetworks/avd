---
# This title is used for search results
title: arista.avd.eos_validate_state_reports
---
<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# eos_validate_state_reports

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.eos_validate_state_reports` when using this plugin.

!!! warning "This module is in **preview** mode"
    This module is not guaranteed to have a backwards compatible interface.

Generates validation reports for the eos\_validate\_state role

## Synopsis

The <code>arista.avd.eos\_validate\_state\_reports</code> module is an Ansible Action Plugin designed to generate validation reports from the test results produced by the ANTA test framework.

This plugin requires a JSON file for each host in the Ansible play, containing all test results. The JSON file is created automatically by the <code>eos\_validate\_state\_runner</code> plugin and is saved in the test results directory with the following naming convention <code>\<inventory\_hostname\>\-results.json</code>.

The plugin offers the following functionalities\:
  \- It aggregates all test results from every host in the Ansible play and generates a CSV report.
  \- It produces a detailed Markdown report with various sections presenting key statistics derived from the results.
  \- The design allows for easy extension to support additional report formats in the future.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| validation_report_csv | bool | optional | True |  | Indicates whether a CSV report should be generated. |
| validation_report_md | bool | optional | True |  | Indicates whether a Markdown report should be generated. |
| only_failed_tests | bool | optional | False |  | Determines if the generated reports should include only the failed tests. |
| csv_report_path | str | optional | None |  | The absolute path where the CSV report will be saved.<br>Required if <code>validation\_report\_csv</code> is set to <code>True</code>. |
| md_report_path | str | optional | None |  | The absolute path where the Markdown report will be saved.<br>Required if <code>validation\_report\_md</code> is set to <code>True</code>. |
| test_results_dir | any | optional | None |  | The directory where the test results JSON file for each host will be saved. |
| cprofile_file | any | optional | None |  | The filename for storing cProfile data, useful for debugging performance issues.<br>Be aware that enabling cProfile can affect performance, so use it only for troubleshooting. |

## Notes

- Enabling the cProfile feature for performance profiling may impact the plugin\'s performance, especially in production environments.
- Hosts with <code>is\_deployed</code> is False are automatically skipped, and no test results are processed for these hosts.

## See Also

- ANTA website: [https://anta.ninja](https://anta.ninja)<br>Documentation for the ANTA test framework

## Examples

```yaml
- name: Generate validation reports from ANTA test results
  arista.avd.eos_validate_state_reports:
    csv_report_path: "/my_avd_project/reports/my-fabric-state.csv"
    md_report_path: "/my_avd_project/reports/my-fabric-state.md"
    validation_report_csv: true
    validation_report_md: true
    only_failed_tests: false
  delegate_to: localhost
  run_once: true
```

## Authors

- Arista Ansible Team (@aristanetworks)
