---
# This title is used for search results
title: arista.avd.legacy_role_vars
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# legacy_role_vars

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.legacy_role_vars` when using this plugin.

Validate legacy role variable aliases

## Synopsis

The C(arista.avd.legacy_role_vars) action plugin detects legacy unprefixed role variables.
It can emit one aggregated warning, reject the variables, or accept them silently.
Variable values are never returned or displayed.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>role_name</samp> | str | True | None | - | Name of the role owning the variables. |
| <samp>aliases</samp> | dict | True | None | - | Mapping of legacy variable names to canonical role-prefixed names. |
| <samp>mode</samp> | str | False | warning | Valid values:<br>- <code>warning</code><br>- <code>error</code><br>- <code>silent</code> | Behavior when a consumed legacy alias is detected. |

## Examples

```yaml
- name: Validate legacy eos_designs variables
  arista.avd.legacy_role_vars:
    role_name: eos_designs
    aliases:
      root_dir: eos_designs_root_dir
    mode: "{{ avd_legacy_role_vars_mode | default('warning') }}"
  run_once: true
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| legacy_aliases | list | Names of consumed legacy aliases. Values are never returned. |

## Authors

- Arista Ansible Team (@aristanetworks)
