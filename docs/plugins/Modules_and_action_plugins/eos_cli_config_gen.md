---
# This title is used for search results
title: arista.avd.eos_cli_config_gen
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# eos_cli_config_gen

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.eos_cli_config_gen` when using this plugin.

Generate AVD EOS device configurations and documentations

## Synopsis

The `arista.avd.eos_cli_config_gen` module is an Ansible Action Plugin providing the following capabilities:

- Generates device configuration and saves it to file
- Optionally generates device documentation and saves it to file

Note: Input validation is performed by the `arista.avd.validate_inputs` plugin, which must be run before this plugin.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>tmp_dir</samp> | str | True | None | - | Path to use as the AVD temporary directory for storing templated and validated data used internally by plugins.<br>Must be the same across all plugins. |
| <samp>config_filename</samp> | str | optional | None | - | The path to save the generated config to. Required if generate_device_config is true. |
| <samp>documentation_filename</samp> | str | optional | None | - | The path to save the generated documentation. Required if generate_device_doc is true. |
| <samp>generate_device_config</samp> | bool | optional | True | - | Flag to generate the device configuration. |
| <samp>generate_device_doc</samp> | bool | optional | True | - | Flag to generate the device documentation. |
| <samp>device_doc_toc</samp> | bool | optional | True | - | Flag to generate the table of content for the device documentation. |
| <samp>cprofile_file</samp> | str | False | None | - | Filename for storing cprofile data used to debug performance issues.<br>Running cprofile will slow down performance in it self, so only set this while troubleshooting. |

## Examples

```yaml
---
- name: Generate EOS intended configuration and device documentation
  arista.avd.eos_cli_config_gen:
    config_filename: "{{ eos_config_dir }}/{{ inventory_hostname }}.cfg"
    documentation_filename: "{{ devices_dir }}/{{ inventory_hostname }}.md"
  delegate_to: localhost

- name: Generate device documentation only
  arista.avd.eos_cli_config_gen:
    config_filename: "{{ eos_config_dir }}/{{ inventory_hostname }}.cfg"
    documentation_filename: "{{ devices_dir }}/{{ inventory_hostname }}.md"
    generate_device_config: false
    device_doc_toc: true
  delegate_to: localhost
```

## Authors

- Arista Ansible Team (@aristanetworks)
