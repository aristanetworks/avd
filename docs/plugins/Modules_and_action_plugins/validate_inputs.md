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

1. **Templating Phase**: Resolves Ansible hostvars and writes them as JSON files. This phase is skipped if `input_dir` is provided
   or pre-templated files already exist in the AVD temporary directory (e.g., from `eos_designs_structured_config`).
2. **Validation Phase**: Validates the data against the specified AVD schema using `pyavd-utils`.

The plugin uses multiprocessing for templating (CPU-bound) and multithreading for validation (I/O-bound with GIL released by Rust).

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>schema_name</samp> | str | optional | eos_designs | Valid values:<br>- <code>eos_designs</code><br>- <code>eos_cli_config_gen</code> | The AVD schema to validate against.<br>If set to `eos_designs`, the plugin will validate the inputs for the entire fabric (requiring `fabric_name` to be set).<br>If set to `eos_cli_config_gen`, the plugin will validate the inputs for the devices in the current play. |
| <samp>input_dir</samp> | str | False | None | - | Optional path to a directory containing input files to validate directly.<br>If provided, the templating phase is skipped and files are read from this directory.<br>Files must be named `&lt;device_name&gt;.&lt;input_suffix&gt;`. |
| <samp>input_suffix</samp> | str | optional | json | Valid values:<br>- <code>yml</code><br>- <code>yaml</code><br>- <code>json</code> | File suffix for files located in `input_dir`.<br>Only used when `input_dir` is provided. |
| <samp>fail_on_validation_errors</samp> | bool | optional | True | - | If `true`, the task will fail if any validation errors are detected.<br>If `false`, errors will be reported but the task will succeed. |
| <samp>batch_size</samp> | int | optional | 10 | - | The number of devices to process per child process during the templating phase. |

## Examples

```yaml
---
- name: Validate eos_designs inputs for the fabric
  arista.avd.validate_inputs:
    schema_name: eos_designs
    fail_on_validation_errors: true

- name: Validate eos_cli_config_gen inputs from structured config files
  arista.avd.validate_inputs:
    schema_name: eos_cli_config_gen
    input_dir: "{{ inventory_dir }}/intended/structured_configs"
    input_suffix: "yml"
    fail_on_validation_errors: false
```

## Authors

- Arista Ansible Team (@aristanetworks)
