---
# This title is used for search results
title: arista.avd.generate_route_target
---
<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# generate_route_target

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.generate_route_target` when using this plugin.

Transforms short_esi `0303:0202:0101` to route-target format `03:03:02:02:01:01`

## Synopsis

Removes `:` and inserts new `:` for each two characters.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>_input</samp> | string | True | None |  | Short ESI value as per AVD definition in eos_designs. |

## Examples

```yaml
---
rt: "{{ short_esi | arista.avd.generate_route_target }}"
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | string | String based on route-target format like 03:03:02:02:01:01 |

## Authors

- Arista Ansible Team (@aristanetworks)
