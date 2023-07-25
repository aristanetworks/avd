# .configlet_build_config

Build arista\.cvp\.configlet configuration\.

## Synopsis

Build configuration to publish configlets to Cloudvision\.

## Parameters

  configlet_dir (True, str, None)
    Directory where configlets are located\.

  configlet_prefix (True, str, None)
    Prefix to append on configlet\.

  destination (False, str, )
    File where to save information\.

  configlet_extension (False, str, conf)
    File extension to look for\.

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
