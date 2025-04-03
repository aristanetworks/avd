---
# This title is used for search results
title: arista.avd.eos_designs_facts
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
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
| <samp>template_output</samp> | bool | False | None |  | If true, the output data will be run through another jinja2 rendering before returning. This is to resolve any input values with inline jinja using variables/facts set by the input templates. |
| <samp>validation_mode</samp> | str | False | error | Valid values:<br>- <code>error</code><br>- <code>warning</code> | Run validation in either &#34;error&#34; or &#34;warning&#34; mode.<br>Validation will validate the input variables according to the schema.<br>During validation, messages will be generated with information about the host(s) and key(s) which failed validation.<br>validation_mode:error will produce error messages and fail the task.<br>validation_mode:warning will produce warning messages. |
| <samp>cprofile_file</samp> | str | False | None |  | Filename for storing cprofile data used to debug performance issues.<br>Running cprofile will slow down performance in it self, so only set this while troubleshooting. |

## Examples

```yaml
---
- name: Set eos_designs facts
  arista.avd.eos_designs_facts:
    schema_id: eos_designs
  check_mode: false
  run_once: true
```

## Authors

- Arista Ansible Team (@aristanetworks)
