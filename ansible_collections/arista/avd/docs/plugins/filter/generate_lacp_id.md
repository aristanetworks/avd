# arista.avd.generate_lacp_id

Transforms short\_esi <code>0303\:0202\:0101</code> to LACP ID format <code>0303\.0202\.0101</code>

## Synopsis

Replaces <code>\:</code> with <code>\.</code>

## Parameters

  _input (True, string, None)
    Short ESI value as per AVD definition in eos\_designs\.

## Examples

```yaml
---
lacp_id: "{{ short_esi | arista.avd.generate_lacp_id }}"
```

## Return Values

  _value (, string, )
    String based on LACP ID format like 0303\.0202\.0101

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
