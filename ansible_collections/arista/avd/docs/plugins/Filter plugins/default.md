# arista.avd.default

Returns input value if defined and is not none\. Otherwise return default value\.

## Synopsis

The arista\.avd\.default filter can provide the same essential capability as the built\-in <code>default</code> filter\.
It will return the input value only if it\'s valid and\, if not\, provide a default value instead\.
Our custom filter requires a value to be <code>not undefined</code> and <code>not None</code> to pass through\.
Furthermore\, the filter allows multiple default values as arguments\, which will undergo the same validation until we find a valid default value\.
As a last resort\, the filter will return <code>None</code>\.

## Parameters

| Argument | Type | Required | Default | Description |
| -------- | ---- | -------- | ------- | ----------- |
| _input | any | True | None | Default value to check\. Will be returned untouched if <code>not undefined</code> and <code>not None</code>\. |
| default_values | any | optional | None | One or more default values which will be tested one by one and the first valid value will be used\. |

## Examples

```yaml
---
myvalue: "{{ variable | arista.avd.default(default_value_1, default_value_2) }}"
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | any | Input value if <code>not undefined</code> and <code>not None</code>\. Otherwise return first defined default value or <code>None</code>\. |

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
