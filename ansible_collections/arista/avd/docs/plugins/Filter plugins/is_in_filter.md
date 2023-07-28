# arista.avd.is_in_filter

Returns <code>True</code> if the input hostname matches the <em>hostname\_filter</em>\.

## Synopsis

The filter matches if any filter strings are found in the input hostname\.

<em>hostname\_filter\=\[\"all\"\]</em> or <em>hostname\_filter\=none</em> will match all hostnames\.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| _input | string | True | None |  | One hostname to match with <em>hostname\_filter</em>\. |
| hostname_filter | any | True | None |  | Filter as a list of strings or <code>None</code>\. |

## Examples

```yaml
---
found_all_1: "{{ 'myhostname' | arista.avd.is_in_filter(['all']) }}"
found_all_2: "{{ 'myhostname' | arista.avd.is_in_filter(none) }}"
found_1: "{{ 'myhostname' | arista.avd.is_in_filter(['my']) }}"
found_2: "{{ 'myhostname' | arista.avd.is_in_filter(['hostname']) }}"
not_found_1: "{{ 'myhostname' | arista.avd.is_in_filter(['myhost1', 'MYhostname']) }}"
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | boolean | <code>True</code> if the input hostname matches the <em>hostname\_filter</em>\. Otherwise <code>False</code> |

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
