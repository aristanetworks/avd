# arista.avd.hide_passwords

Replace a value by \"\<removed\>\"

## Synopsis

Replace the input data by \"\<removed\>\" if the hide\_passwords parameter is true

## Parameters

  _input (True, raw, None)
    Value to replace\.

  hide_passwords (True, bool, None)
    Flag to indicate whether or not the string should be replaced\.

## Examples

```yaml
ip ospf authentication-key 7 {{ vlan_interface.ospf_authentication_key | arista.avd.hide_passwords(true) }}
```

## Return Values

  _value (, string, )
    The original input or \'\<removed\>\'

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
