---
# This title is used for search results
title: arista.avd.eos_designs_facts
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# eos_designs_facts

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.eos_designs_facts` when using this plugin.

Set eos_designs facts

## Synopsis

The `arista.avd.eos_designs_facts` module is an Ansible Action Plugin providing the following capabilities:

- Set `avd_switch_facts` fact containing internal AVD facts per host.

The plugin is designed to `run_once`. With this, Ansible will set the same facts on all devices, so all devices can lookup values of any other device without using the slower `hostvars`.

The module is used in `arista.avd.eos_designs` to set facts for devices, which are then used by jinja templates and python module in `arista.avd.eos_designs` to generate the `structured_configuration`.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>tmp_dir</samp> | str | True | None | - | Path to use as the AVD temporary directory for storing templated and validated data used internally by plugins.<br>Must be the same across all plugins. |
| <samp>output_dir</samp> | str | True | None | - | Directory where the plugin stores updated pool assignment files.<br>Required for initializing the pool manager used while building eos_designs facts. |
| <samp>template_output</samp> | bool | False | None | - | If true, the output data will be run through another jinja2 rendering before returning. This is to resolve any input values with inline jinja using variables/facts set by the input templates.<br>Ignored for ansible-core versions &gt;= 2.19, since it is no longer needed. |
| <samp>cprofile_file</samp> | str | False | None | - | Filename for storing cprofile data used to debug performance issues.<br>Running cprofile will slow down performance in it self, so only set this while troubleshooting. |
| <samp>digital_twin</samp> | bool | optional | False | - | PREVIEW: This option is marked as &#34;preview&#34;, meaning the data models or generated configuration can change at any time.<br>Generate Digital Twin topology information. |

## Examples

```yaml
---
- name: Set eos_designs facts
  arista.avd.eos_designs_facts:
    tmp_dir: "intended/tmp_eos_designs"
    output_dir: "intended"
  check_mode: false
  run_once: true
```

## Authors

- Arista Ansible Team (@aristanetworks)
