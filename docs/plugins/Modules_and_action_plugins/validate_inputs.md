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

The `arista.avd.validate_inputs` module is an Ansible Action Plugin designed to validate host variables against Arista AVD schemas.

The plugin offers the following capabilities:

- **Templating Phase**: Resolves Ansible host variables (and optionally loads data from an external directory).
- **Validation Phase**: Validates the templated data against the specified AVD schema (e.g., `eos_designs` or `eos_cli_config_gen`) using `pyavd-utils`.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>schema_name</samp> | str | optional | eos_designs | Valid values:<br>- <code>eos_designs</code><br>- <code>eos_cli_config_gen</code> | The AVD schema to validate against.<br>If set to `eos_designs`, the plugin will validate the inputs for the entire fabric (requiring `fabric_name` to be set).<br>If set to `eos_cli_config_gen`, the plugin will validate the inputs for the hosts in the current play. |
| <samp>template_inputs</samp> | bool | optional | True | - | If `true`, the plugin will run the templating phase to resolve host variables.<br>If `false`, it assumes inputs are already available. |
| <samp>input_dir</samp> | str | False | None | - | Optional path to a directory containing additional host variables files.<br>If provided, these files are loaded and overlaid onto the host variables during the templating phase. |
| <samp>input_suffix</samp> | str | optional | yml | Valid values:<br>- <code>yml</code><br>- <code>yaml</code><br>- <code>json</code> | File suffix for files located in `input_dir`. |
| <samp>fail_on_validation_errors</samp> | bool | optional | True | - | If `true`, the task will fail if any validation errors are detected.<br>If `false`, errors will be reported but the task will succeed. |
| <samp>batch_size</samp> | int | optional | 10 | - | The number of hosts to process in a single batch during the templating phase. |

## Examples

```yaml
---
- name: Validate eos_designs inputs for the fabric
  arista.avd.validate_inputs:
    schema_name: eos_designs
    template_inputs: true
    fail_on_validation_errors: true

- name: Validate eos_cli_config_gen inputs
  arista.avd.validate_inputs:
    schema_name: eos_cli_config_gen
    input_dir: "{{ inventory_dir }}/intended/structured_configs"
    input_suffix: "yml"
    template_inputs: true
    fail_on_validation_errors: false
```

## Authors

- Arista Ansible Team (@aristanetworks)
