# arista.avd.list_compress

Compress a list of integers to a range string\.

## Synopsis

Provides the capability to generate a string representing ranges of VLANs or VNIs

## Parameters

  _input (True, list, None)
    List of integers to compress into a range\.

## Examples

```yaml
---
list1: "{{ [1,2,3,4,5] | arista.avd.list_compress }}" # -> "1-5"
list2: "{{ [1,2,3,7,8] | arista.avd.list_compress }}" # -> "1-3,7-8"
```

## Return Values

  _value (, string, )
    Range string like \"1\-3\,7\-8\"

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
