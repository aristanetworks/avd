---
# This title is used for search results
title: arista.avd.validate_inputs
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# validate_inputs

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.validate_inputs` when using this plugin.

Validate variables against AVD schemas

## Synopsis

The `arista.avd.validate_inputs` module is an Ansible Action Plugin designed to validate device variables against Arista AVD schemas.

The plugin performs two phases:

1. **Templating Phase**: Resolves Ansible hostvars and writes the templated data as JSON files to the AVD temporary directory.
    This phase is skipped if `input_dir` is provided, treating the input files as already templated.
2. **Validation Phase**: Validates the inputs against the specified AVD schema using `pyavd-utils` and writes the validated
    data as JSON files to the AVD temporary directory.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>schema_name</samp> | str | optional | avd_design | Valid values:<br>- <code>avd_design</code><br>- <code>eos_config</code> | The AVD schema to validate against.<br>If set to `avd_design`, the plugin will validate the inputs for the entire fabric (requiring `fabric_name` to be set).<br>If set to `eos_config`, the plugin will validate the inputs for the devices in the current play. |
| <samp>input_dir</samp> | str | False | None | - | Optional path to a directory containing input files to validate directly.<br>If provided, the templating phase is skipped and files are read from this directory.<br>Files must be named `device_name.input_suffix`. |
| <samp>input_suffix</samp> | str | optional | json | Valid values:<br>- <code>yml</code><br>- <code>yaml</code><br>- <code>json</code> | File suffix for files located in `input_dir`.<br>Only used when `input_dir` is provided. |
| <samp>fail_on_validation_errors</samp> | bool | optional | False | - | If `true`, the task will fail if any validation errors are detected.<br>If `false`, errors will be reported but the task will succeed. |
| <samp>batch_size</samp> | int | optional | 10 | - | The number of devices to process per child process during the templating phase. |
| <samp>validation_configuration</samp> | dict | False | None | - | Optional dictionary containing configuration options to control validation behavior. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;warn_eos_config_keys</samp> | bool | optional | False | - | Enable warnings for EOS Config keys used in AVD Design input data.<br>When enabled, warnings will be emitted during validation if any top-level keys<br>from the EOS Config schema are found at the top level of AVD Design input data. |

## Examples

```yaml
---
- name: Validate eos_designs inputs for the fabric
  arista.avd.validate_inputs:
    schema_name: avd_design
    fail_on_validation_errors: true

- name: Validate eos_designs inputs with custom validation configuration
  arista.avd.validate_inputs:
    schema_name: avd_design
    fail_on_validation_errors: true
    validation_configuration:
      warn_eos_config_keys: true

- name: Validate eos_cli_config_gen inputs from structured config files
  arista.avd.validate_inputs:
    schema_name: eos_config
    input_dir: "{{ inventory_dir }}/intended/structured_configs"
    input_suffix: "yml"
    fail_on_validation_errors: false
```

## Authors

- Arista Ansible Team (@aristanetworks)
