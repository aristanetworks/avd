---
# This title is used for search results
title: arista.avd.status_render
---
<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# status_render

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.status_render` when using this plugin.

Convert Text to EMOJI code.

## Synopsis

Returns the input value unless <em>rendering</em> is set to \"github\".

Returns <code>\:x\:</code> if input status string is <code>FAIL</code> and <em>rendering</em> is set to \"github\".

Returns <code>\:white\_check\_mark\:</code> if input status string is <code>PASS</code> and <em>rendering</em> is set to \"github\".

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| _input | string | True | None |  | Text to convert to EMOJI. |
| rendering | string | True | None |  | Markdown Flavor to use for Emoji rendering. Only \"github\" is supported. |

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | string | Input value or GitHub Markdown emoji code. |

## Authors

- Arista Ansible Team (@aristanetworks)
