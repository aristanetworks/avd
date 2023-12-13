---
# This title is used for search results
title: arista.avd.convert_schema
---
<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# convert_schema

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.convert_schema` when using this plugin.

Convert AVD Schema to a chosen output format.

## Synopsis

Only for internal use.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| _input | string | True | None | Valid values:<br>- <code>eos_cli_config_gen</code><br>- <code>eos_designs</code> | ID of AVD Schema. |
| type | string | True | None | Valid values:<br>- <code>documentation_tables</code><br>- <code>jsonschema</code> | Type of schema to convert to. |

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | any | Schema of the requested type. |

## Authors

- Arista Ansible Team (@aristanetworks)
