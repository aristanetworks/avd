# arista.avd.convert_schema

Convert AVD Schema to a chosen output format\.

## Synopsis

Only for internal use\.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| _input | string | True | None | Valid values:<br>- <code>eos_cli_config_gen</code><br>- <code>eos_designs</code> | ID of AVD Schema\. |
| type | string | True | None | Valid values:<br>- <code>documentation_tables</code><br>- <code>jsonschema</code> | Type of schema to convert to\. |

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | any | Schema of the requested type\. |

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
