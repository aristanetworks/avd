<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# inventory\_to\_container

Transform information from inventory to arista.cvp collection

Module added in version 2.9

<div class="contents" data-local="" data-depth="2">

</div>

## Synopsis

Transform information from ansible inventory to be able to provision
CloudVision Platform using arista.cvp collection and its specific data
structure.

## Module-specific Options

The following options may be specified for this module:

<table border=1 cellpadding=4>

<tr>
<th class="head">parameter</th>
<th class="head">type</th>
<th class="head">required</th>
<th class="head">default</th>
<th class="head">choices</th>
<th class="head">comments</th>
</tr>

<tr>
<td>configlet_dir<br/><div style="font-size: small;"></div></td>
<td>str</td>
<td>no</td>
<td></td>
<td></td>
<td>
    <div>Directory where intended configurations are located.</div>
</td>
</tr>

<tr>
<td>configlet_prefix<br/><div style="font-size: small;"></div></td>
<td>str</td>
<td>no</td>
<td></td>
<td></td>
<td>
    <div>Prefix to put on configlet.</div>
</td>
</tr>

<tr>
<td>container_root<br/><div style="font-size: small;"></div></td>
<td>str</td>
<td>yes</td>
<td></td>
<td></td>
<td>
    <div>Ansible group name to consider to be Root of our topology.</div>
</td>
</tr>

<tr>
<td>destination<br/><div style="font-size: small;"></div></td>
<td>str</td>
<td>no</td>
<td></td>
<td></td>
<td>
    <div>Optional path to save variable.</div>
</td>
</tr>

<tr>
<td>device_filter<br/><div style="font-size: small;"></div></td>
<td>list</td>
<td>no</td>
<td>[&#x27;all&#x27;]</td>
<td></td>
<td>
    <div>Filter to apply intended mode on a set of configlet. If not used, then module only uses ADD mode. device_filter list devices that can be modified or deleted based on configlets entries.</div>
</td>
</tr>

<tr>
<td>inventory<br/><div style="font-size: small;"></div></td>
<td>str</td>
<td>yes</td>
<td></td>
<td></td>
<td>
    <div>YAML inventory file</div>
</td>
</tr>

</table>
</br>

## Examples

```yaml
- name: Generate intended variables
  arista.avd.inventory_to_container:
    inventory: 'inventory.yml'
    container_root: 'DC1_FABRIC'
    configlet_dir: 'intended_configs'
    configlet_prefix: 'AVD'
    device_filter: ['DC1-LE']
    # destination: 'generated_vars/{{inventory_hostname}}.yml'
  register: cvp_vars

- name: 'Collecting facts from CVP {{ inventory_hostname }}.'
  arista.cvp.cv_facts:
  register: cvp_facts

- name: 'Create configlets on CVP {{ inventory_hostname }}.'
  arista.cvp.cv_configlet:
    cvp_facts: "{{ cvp_facts.ansible_facts }}"
    configlets: "{{ cvp_vars.cvp_configlets }}"
    configlet_filter: ["AVD"]

- name: "Building Container topology on {{ inventory_hostname }}"
  arista.cvp.cv_container:
    topology: '{{ cvp_vars.cvp_topology }}'
    cvp_facts: '{{ cvp_facts.ansible_facts }}'
    save_topology: true
- Ansible Arista Team (@aristanetworks)

### Status

This module is flagged as **preview** which means that it's not
guaranteed to have a backwards compatible interface.
