---
# This title is used for search results
title: arista.avd.generate_lacp_id
---
<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# generate_lacp_id

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.generate_lacp_id` when using this plugin.

Transforms short\_esi <code>0303\:0202\:0101</code> to LACP ID format <code>0303.0202.0101</code>

## Synopsis

Replaces <code>\:</code> with <code>.</code>

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| _input | string | True | None |  | Short ESI value as per AVD definition in eos\_designs. |

## Examples

```yaml
---
lacp_id: "{{ short_esi | arista.avd.generate_lacp_id }}"
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | string | String based on LACP ID format like 0303.0202.0101 |

## Authors

- Arista Ansible Team (@aristanetworks)
