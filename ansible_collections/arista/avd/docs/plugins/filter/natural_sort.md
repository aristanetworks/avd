# arista.avd.natural_sort

Sort an input list with natural sorting\.

## Synopsis

Provides the capabilities to sort a list or a dictionary of integers and/or strings that contain alphanumeric characters naturally\.
When leveraged on a dictionary\, only the key value will be returned\.
An optional \`sort\_key\` can be specified\, to sort on content of certain key if the items are dictionaries\.

The filter will return an empty list if the value parsed to arista\.avd\.natural\_sort is <code>None</code> or <code>undefined</code>\.

## Parameters

| Argument | Type | Required | Default | Description |
| -------- | ---- | -------- | ------- | ----------- |
| _input | any | True | None | List or dictionary |
| sort_key | string | optional | None | Key to sort on when sorting a list of dictionaries |

## Examples

```yaml
---
sorted_list: "{{ ['test19', 'test9'] | natural_sort }}" # -> ["test9", "test19"]
sorted_keys: "{{ {'test19': 'value', 'test9': 'value'} | natural_sort }}" # -> ["test9", "test19"]
sorted_on_name_key: "{{ [{'name': 'test19'}, {'name': 'test9'}] | natural_sort('name') }}" # -> [{"name": "test9"}, {"name": "test19"}]
empty_list_1: "{{ none | natural_sort }}" # -> []
empty_list_2: "{{ some_undefined_var | natural_sort }}" # -> []
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | list | Sorted list if the input was a list\. Sorted keys if the input was a dictionary\. Empty list if the input value was <code>None</code> or <code>undefined</code>\. |

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
