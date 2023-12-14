---
# This title is used for search results
title: arista.avd.eos_designs_facts
---
<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# eos_designs_facts

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.eos_designs_facts` when using this plugin.

Set eos\_designs facts

## Synopsis

The \`arista.avd.eos\_designs\_facts\` module is an Ansible Action Plugin providing the following capabilities\:

\- Set \`avd\_switch\_facts\` fact containing both \`switch\` facts per host.
\- Set \`avd\_topology\_peers\` fact containing list of downlink switches per host.
  This list is built based on the \`uplink\_switches\` from all other hosts.
\- Set \`avd\_overlay\_peers\` fact containing list of EVPN or MPLS overlay peers per host.
  This list is built based on the \`evpn\_route\_servers\` and \`mpls\_route\_reflectors\` from all other hosts.

The plugin is designed to \`run\_once\`. With this, Ansible will set the same facts on all devices, so all devices can lookup values of any other device without using the slower \`hostvars\`.

The facts can also be copied to the \"root\" \`switch\` in a task run per\-device \(see example below\)

The module is used in \`arista.avd.eos\_designs\` to set facts for devices, which are then used by jinja templates and python module in \`arista.avd.eos\_designs\` to generate the \`structured\_configuration\`.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| template_output | bool | False | None |  | If true, the output data will be run through another jinja2 rendering before returning. This is to resolve any input values with inline jinja using variables/facts set by the input templates. |
| conversion_mode | str | False | debug | Valid values:<br>- <code>error</code><br>- <code>warning</code><br>- <code>info</code><br>- <code>debug</code><br>- <code>quiet</code><br>- <code>disabled</code> | Run data conversion in either \"error\", \"warning\", \"info\", \"debug\", \"quiet\" or \"disabled\" mode.<br>Conversion will perform type conversion of input variables as defined in the schema.<br>Conversion is intended to help the user to identify minor issues with the input data, while still allowing the data to be validated.<br>During conversion, messages will be generated with information about the host\(s\) and key\(s\) which required conversion.<br>conversion\_mode\:disabled means that conversion will not run.<br>conversion\_mode\:error will produce error messages and fail the task.<br>conversion\_mode\:warning will produce warning messages.<br>conversion\_mode\:info will produce regular log messages.<br>conversion\_mode\:debug will produce hidden messages viewable with \-v.<br>conversion\_mode\:quiet will not produce any messages. |
| validation_mode | str | False | warning | Valid values:<br>- <code>error</code><br>- <code>warning</code><br>- <code>info</code><br>- <code>debug</code><br>- <code>disabled</code> | Run validation in either \"error\", \"warning\", \"info\", \"debug\" or \"disabled\" mode.<br>Validation will validate the input variables according to the schema.<br>During validation, messages will be generated with information about the host\(s\) and key\(s\) which failed validation.<br>validation\_mode\:disabled means that validation will not run.<br>validation\_mode\:error will produce error messages and fail the task.<br>validation\_mode\:warning will produce warning messages.<br>validation\_mode\:info will produce regular log messages.<br>validation\_mode\:debug will produce hidden messages viewable with \-v. |
| cprofile_file | str | False | None |  | Filename for storing cprofile data used to debug performance issues.<br>Running cprofile will slow down performance in it self, so only set this while troubleshooting. |

## Examples

```yaml
---
- name: Set eos_designs facts
  tags: [build, provision, facts]
  arista.avd.eos_designs_facts:
    schema_id: eos_designs
  check_mode: False
  run_once: True

- name: Set eos_designs facts per device
  tags: [build, provision, facts]
  ansible.builtin.set_fact:
    switch: "{{ avd_switch_facts[inventory_hostname].switch }}"
  delegate_to: localhost
  changed_when: false
```

## Authors

- Arista Ansible Team (@aristanetworks)
