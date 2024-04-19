---
# This title is used for search results
title: arista.avd.cv_zscaler_endpoints
---
<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# cv_zscaler_endpoints

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.cv_zscaler_endpoints` when using this plugin.

PREVIEW - Fetch Zscaler endpoints used for CV Pathfinder internet-exit integration.

## Synopsis

Use this to autofill the `zscaler_endpoints` data model.

The arguments are optional. If not set the same vars must be set.

## Requirements

The below requirements are needed on the host that executes this module.

- md_toc

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>cv_server</samp> | str | True | None |  | CV server. |
| <samp>cv_token</samp> | str | True | None |  | CV token. |
| <samp>cv_verify_certs</samp> | bool | optional | True |  | Verify SSL certificates. |
| <samp>serial_number</samp> | str | True | None |  | Device serial number. |
| <samp>inventory_hostname</samp> | str | True | None |  | Device inventory hostname. |

## Examples

```yaml
---
zscaler_endpoints: "{{ lookup('arista.avd.cv_zscaler_endpoints') }}"
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | dict | Dict according to the `zscaler_endpoints` data model. |

## Authors

- Arista Ansible Team (@aristanetworks)
