---
# This title is used for search results
title: arista.avd.generate_esi
---
<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# generate_esi

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.generate_esi` when using this plugin.

Transforms short_esi `0303:0202:0101` to EVPN ESI format `0000:0000:0303:0202:0101`

## Synopsis

Concatenates the given `esi_prefix` and `short_esi`.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>_input</samp> | string | True | None |  | Short ESI value as per AVD definition in eos_designs. |
| <samp>esi_prefix</samp> | string | optional | 0000:0000: |  | ESI prefix value. Will be concatenated with the `short_esi`. |

## Examples

```yaml
---
esi: "{{ short_esi | arista.avd.generate_esi('deaf:beed:') }}"
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | string | Concatenated string of `esi_prefix` and `short_esi` like `0000:0000:0303:0202:0101` |

## Authors

- Arista Ansible Team (@aristanetworks)
