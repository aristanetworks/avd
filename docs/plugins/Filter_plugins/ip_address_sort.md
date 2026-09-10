---
# This title is used for search results
title: arista.avd.ip_address_sort
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# ip_address_sort

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.ip_address_sort` when using this plugin.

Sort a list by IP address.

## Synopsis

Sorts IPv4 and IPv6 addresses, with or without prefix lengths, numerically. IPv4 addresses are sorted before IPv6 addresses.

The filter returns an empty list if the input is `None` or `undefined`.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>_input</samp> | list | True | None | - | List of IPv4 or IPv6 addresses with optional prefix lengths. |
| <samp>sort_key</samp> | string | optional | None | - | Key containing the IP address when sorting a list of dictionaries. |

## Examples

```yaml
---
sorted_ipv4_addresses: "{{ ['192.0.2.10/24', '192.0.2.2'] | arista.avd.ip_address_sort }}" # -> ["192.0.2.2", "192.0.2.10/24"]
sorted_ipv6_addresses: "{{ ['2001:db8::10/64', '2001:db8::2'] | arista.avd.ip_address_sort }}" # -> ["2001:db8::2", "2001:db8::10/64"]
sorted_neighbors: >-
  {{
    [{'ip_address': '192.0.2.10'}, {'ip_address': '192.0.2.2'}]
    | arista.avd.ip_address_sort(sort_key='ip_address')
  }}
# -> [{"ip_address": "192.0.2.2"}, {"ip_address": "192.0.2.10"}]
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | list | Input values sorted by IP version and numeric address. |

## Authors

- Arista Ansible Team (@aristanetworks)
