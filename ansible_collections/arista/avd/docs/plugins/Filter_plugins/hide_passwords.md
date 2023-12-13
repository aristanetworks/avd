---
# This title is used for search results
title: arista.avd.hide_passwords
---
<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# hide_passwords

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.hide_passwords` when using this plugin.

Replace a value by \"\<removed\>\"

## Synopsis

Replace the input data by \"\<removed\>\" if the hide\_passwords parameter is true

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| _input | raw | True | None |  | Value to replace. |
| hide_passwords | bool | True | None |  | Flag to indicate whether or not the string should be replaced. |

## Examples

```yaml
cli_with_hidden_password: "ip ospf authentication-key 7 {{ vlan_interface.ospf_authentication_key | arista.avd.hide_passwords(true) }}"
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | string | The original input or \'\<removed\>\' |

## Authors

- Arista Ansible Team (@aristanetworks)
