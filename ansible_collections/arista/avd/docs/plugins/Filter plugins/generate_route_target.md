# arista.avd.generate_route_target

Transforms short\_esi <code>0303\:0202\:0101</code> to route\-target format <code>03\:03\:02\:02\:01\:01</code>

## Synopsis

Removes <code>\:</code> and inserts new <code>\:</code> for each two characters\.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| _input | string | True | None |  | Short ESI value as per AVD definition in eos\_designs\. |

## Examples

```yaml
---
rt: "{{ short_esi | arista.avd.generate_route_target }}"
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | string | String based on route\-target format like 03\:03\:02\:02\:01\:01 |

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
