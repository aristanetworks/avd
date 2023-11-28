<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# eos_validate_state_runner

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.eos_validate_state_runner` when using this plugin.

!!! warning "This module is in **preview** mode"
    This module is not guaranteed to have a backwards compatible interface.

Utilizes ANTA for eos\_validate\_state role validation

## Synopsis

The <code>arista.avd.eos\_validate\_state\_runner</code> module is an Ansible Action Plugin leveraging the ANTA test framework to validate that the generated structured configurations by AVD are applied to the devices and that the deployed network is working correctly.

This plugin requires that structured\_configs for each device be present in hostvars\; otherwise, no tests will be executed.

The plugin offers the following capabilities\:
    \- Generating a per\-device test catalog based on the AVD structured\_config.
    \- Running generated tests against each device, saving the results in a temporary JSON file,
      and recording the file path in hostvars for use by the report plugin.
    \- In check\_mode, only the test catalog is generated, and a report is created to preview the tests that would be run against each device.
    \- Saving per\-device test catalogs and results to specified directories.
    \- Maintaining backward compatibility with existing ansible tags for eos\_validate\_state to filter test categories.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| logging_level | str | optional | WARNING | Valid values:<br>- <code>CRITICAL</code><br>- <code>ERROR</code><br>- <code>WARNING</code><br>- <code>INFO</code><br>- <code>DEBUG</code> | Sets the log level for the ANTA library. Defaults to \"WARNING\" if not specified. |
| save_catalog | bool | optional | False |  | Indicates whether to save the test catalog for each device. |
| save_results | bool | optional | False |  | Indicates whether to save test results in a JSON file for each device. |
| device_catalog_output_dir | str | optional | None |  | The directory where device test catalogs will be saved.<br>Required if <code>save\_catalog</code> is set to <code>True</code>. |
| device_results_output_dir | str | optional | None |  | The directory where device test results will be saved.<br>Required if <code>save\_results</code> is set to <code>True</code>. |
| skipped_tests | list | optional | None |  | A list of dictionaries specifying categories and tests to skip.<br>Each dictionary should have keys <code>category</code> and <code>tests</code>. |
|     category | str | optional | None |  | The name of an AvdTest category \(e.g., <code>AvdTestHardware</code>\). |
|     tests | list | optional | None |  | A list of specific tests in the category \(e.g., <code>VerifyRoutingProtocolModel</code> in <code>AvdTestBGP</code>\). |
| cprofile_file | any | optional | None |  | The filename for storing cProfile data, useful for debugging performance issues.<br>Be aware that enabling cProfile can affect performance, so use it only for troubleshooting. |

## Notes

- Enabling the cProfile feature for performance profiling may impact the plugin\'s performance, especially in production environments.
- The plugin manages the creation and cleanup of temporary JSON files used for storing test results.
- This module supports <code>check\_mode</code>, allowing the generation of test reports without executing the tests.

## See Also

- ANTA website: [https://anta.ninja](https://anta.ninja)<br>Documentation for the ANTA test framework

## Examples

```yaml
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
```

## Authors

- Arista Ansible Team (@aristanetworks)
