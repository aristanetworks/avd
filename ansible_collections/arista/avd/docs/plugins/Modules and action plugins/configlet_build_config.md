---
# This title is used for search results
title: arista.avd.configlet_build_config
---
<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# configlet_build_config

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.configlet_build_config` when using this plugin.

Build arista.cvp.configlet configuration.

## Synopsis

Build configuration to publish configlets to Cloudvision.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| configlet_dir | str | True | None |  | Directory where configlets are located. |
| configlet_prefix | str | True | None |  | Prefix to append on configlet. |
| destination | str | False | None |  | File where to save information. |
| configlet_extension | str | False | conf |  | File extension to look for. |

## Examples

```yaml
# tasks file for configlet_build_config
- name: generate intended variables
  tags: [build, provision]
  configlet_build_config:
    configlet_dir: '/path/to/configlets/folder/'
    configlet_prefix: 'AVD_'
    configlet_extension: 'cfg'
```

## Authors

- EMEA AS Team (@aristanetworks)
