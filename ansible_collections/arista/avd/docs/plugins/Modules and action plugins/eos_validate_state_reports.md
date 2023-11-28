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

The <code>arista.avd.eos\_validate\_state\_reports</code> module, an Ansible Action Plugin, is designed to generate validation reports from the test results produced by the ANTA test framework.

This plugin requires a temporary JSON file for each host in the Ansible play, which contains all test results. The path to this temporary JSON file, used by the plugin, is supplied in the hostvars by the \`eos\_validate\_state\_runner\` plugin.

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
| csv_report_path | str | optional | None |  | Specifies the absolute path where the CSV report will be saved.<br>Required if <code>validation\_report\_csv</code> is set to <code>True</code>. |
| md_report_path | str | optional | None |  | Specifies the absolute path where the Markdown report will be saved.<br>Required if <code>validation\_report\_md</code> is set to <code>True</code>. |
| cprofile_file | any | optional | None |  | Specifies the filename for storing cProfile data, which aids in debugging performance issues.<br>Note that enabling cProfile can itself impact performance, so it should only be used for troubleshooting. |

## Notes

- Enabling the cProfile feature for performance profiling may impact the plugin\'s performance, especially in production environments.
- The plugin manages temporary files created for processing test results, ensuring clean\-up post\-execution.
- Hosts marked as not deployed are automatically skipped, and no test results are processed for these hosts.

## See Also

- ANTA website: [https://anta.ninja](https://anta.ninja)<br>Documentation for the ANTA test framework

## Examples

```yaml
- name: Generate validation reports from ANTA test results
  arista.avd.eos_validate_state_reports:
    csv_report_path: "/git_projects/my_avd_project/reports/my-fabric-state.csv"
    md_report_path: "/git_projects/my_avd_project/reports/my-fabric-state.md"
    validation_report_csv: true
    validation_report_md: true
    only_failed_tests: false
  delegate_to: localhost
  run_once: true
```

## Authors

- Arista Ansible Team (@aristanetworks)
