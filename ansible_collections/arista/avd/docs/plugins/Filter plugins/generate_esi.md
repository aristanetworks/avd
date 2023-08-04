# generate_esi

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.generate_esi` when using this plugin.

Transforms short\_esi <code>0303\:0202\:0101</code> to EVPN ESI format <code>0000\:0000\:0303\:0202\:0101</code>

## Synopsis

Concatenates the given <em>esi\_prefix</em> and <em>short\_esi</em>\.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| _input | string | True | None |  | Short ESI value as per AVD definition in eos\_designs\. |
| esi_prefix | string | optional | 0000:0000: |  | ESI prefix value\. Will be concatenated with the <em>short\_esi</em>\. |

## Examples

```yaml
---
esi: "{{ short_esi | arista.avd.generate_esi('deaf:beed:') }}"
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | string | Concatenated string of <em>esi\_prefix</em> and <em>short\_esi</em> like <code>0000\:0000\:0303\:0202\:0101</code> |

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
