---
# This title is used for search results
title: arista.avd.global_vars
---
<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# global_vars

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.global_vars` when using this plugin.

Variable plugins to allow loading global\_vars with less precedence than group\_vars or host\_vars

## Synopsis

Loads variables from variable files specified in ansible.cfg or in the environment variable.

Assign the loaded variables to the \'all\' inventory group.

Files are restricted by extension to one of .yaml, .json, .yml, or no extension.

Hidden files \(starting with \'.\'\) and backup files \(ending with \'\~\'\) are ignored.

Only applies to inventory sources that are existing paths.

<hr>

<b>ansible.cfg only example</b>

1 \- Enable the plugin in <code>ansible.cfg</code> \- DO NOT REMOVE <code>host\_group\_vars</code>.

<code>\[defaults\]</code>

<code>vars\_plugins\_enabled \= arista.avd.global\_vars, host\_group\_vars</code>

<code>\[vars\_global\_vars\]</code>

<code>paths \= ../relative/path/to/my/global/vars/file/or/dir</code>

2 \- Run your playbook

<code>ansible\-playbook \-i inventory.yml playbook.yml</code>

<hr>

<b>ansible.cfg \+ environment variable example</b>

1 \- Enable the plugin in <code>ansible.cfg</code> \- DO NOT REMOVE <code>host\_group\_vars</code>.

<code>\[defaults\]</code>

<code>vars\_plugins\_enabled \= arista.avd.global\_vars, host\_group\_vars</code>

2 \- Run your playbook

<code>ARISTA\_AVD\_GLOBAL\_VARS\_PATHS\=../relative/path/to/my/global/vars/file/or/dir ansible\-playbook \-i inventory.yml playbook.yml</code>

## Requirements

The below requirements are needed on the host that executes this module.

- This plugin should run at the \`inventory\` stage \(default\) before all other variable plugins to inject the variables before any group and host vars.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| paths | list | True | None |  | List of relative paths relative to the inventory file.<br>If path is a directory, all the valid files inside are loaded alphabetically.<br>If the environment variable is set, it takes precedence over ansible.cfg. |
| stage | any | optional | inventory | Valid values:<br>- <code>inventory</code> | The stage during which executing the plugin. It could be \'inventory\' or \'task\'<br>Given the expected usage of this plugin at the beginning of the run. It is hard\-coded to \'inventory\' |
| _valid_extensions | list | optional | ['.yml', '.yaml', '.json'] |  | Check all of these extensions when looking for \'variable\' files, which should be YAML, JSON, or vaulted versions.<br>This affects vars\_files, include\_vars, inventory, and vars plugins, among others. |

## Authors

- Arista Ansible Team (@aristanetworks)
