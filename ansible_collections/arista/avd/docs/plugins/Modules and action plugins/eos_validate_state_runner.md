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

Leverage ANTA for eos\_validate\_state role

## Synopsis

The \`arista.avd.eos\_validate\_state\_runner\` module is an Ansible Action Plugin leveraging the ANTA test
framework to validate that the generated structured configurations by AVD are applied to the devices and
that the deployed network is working correctly.

This plugin expects that the structued\_configs of each device is present in hostvars, otherwise no test will be generated.

The plugin provides the following capabilities\:
  \- Generate a per\-device test catalog based on the structured\_configs
  \- Run the generated tests against each device and generate a report in Markdown and CSV format.
  \- When using check\_mode, only generate the test catalog and generate a report to preview what would
    tests be run against each device
  \- Dumping the per\-device catalog to a file.
  \- Backward compatibility with existing ansible tags behavior for eos\_validate\_state to filter categories of tests.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| logging_level | str | False | WARNING | Valid values:<br>- <code>CRITICAL</code><br>- <code>ERROR</code><br>- <code>WARNING</code><br>- <code>INFO</code><br>- <code>DEBUG</code> | Controls the log level for the ANTA library. If unset, the Action plugin will set it to \"WARNING\" |
| save_catalog | bool | optional | False |  | A boolean to indicate whether or not the catalog should be saved for each device. |
| device_catalog_output_dir | str | optional | None |  | When \`save\_catalog\` is True, this is the directory where the device catalogs will be saved.<br>Required if <em>save\_catalog\=True</em> |
| skipped_test | dict | optional | None |  | A dictionary to indicate skipped tests. |

## Notes

- \`check\_mode\` is supported for this module and allows to generate a Test Report without running the tests.

## See Also

   `ANTA website <https://anta.ninja>`_
       ANTA documentation

## Examples

```yaml
- name: Run eos_validate_state_runner leveraging ANTA
  arista.avd.eos_validate_state_runner:
    logging_level: ERROR
    save_catalog: True
    eos_validate_state_dir: "/tmp"
    skipped_tests: {"BGP"}
  register: anta_results
```

## Status

- This module is not guaranteed to have a backwards compatible interface. *[preview]*

## Authors

- Arista Ansible Team (@aristanetworks)
