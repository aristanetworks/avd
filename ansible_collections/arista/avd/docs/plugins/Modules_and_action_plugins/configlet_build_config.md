# arista.avd.configlet_build_config

Build arista\.cvp\.configlet configuration\.

## Synopsis

Build configuration to publish configlets to Cloudvision\.

## Parameters

| Argument | Type | Required | Default | Description |
| -------- | ---- | -------- | ------- | ----------- |
| configlet_dir | str | True | None | Directory where configlets are located\. |
| configlet_prefix | str | True | None | Prefix to append on configlet\. |
| destination | str | False |  | File where to save information\. |
| configlet_extension | str | False | conf | File extension to look for\. |

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

## Status

## Authors

- EMEA AS Team (@aristanetworks)
