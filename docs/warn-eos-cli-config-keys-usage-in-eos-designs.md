<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
# Using `eos_cli_config_gen` native keys when running `eos_designs`

## Context

For several AVD major versions, it has been possible to use variables from the `eos_cli_config_gen` data model in conjunction with variables from the `eos_designs` data model. When the `eos_designs`
role runs, the `eos_cli_config_gen` keys are ignored but they will be read later by the `eos_cli_config_gen` role.

While this behavior could serve as a good escape hatch, it has led to confusion among users. Especially when new features introduced in `eos_designs` ended up shadowing the inputs intended for `eos_cli_config_gen`,
sometimes leading to configuration changes after a minor releases upgrade. This behavior is well documented and described in the `eos_designs` how-to on
[custom_structured_configuration](../ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-structured-configuration.md) which is the recommended way of
using `eos_cli_config_gen` variables within `eos_designs`. However the direct usage of `eos_cli_config_gen` variables still works.

!!! note
    Only top-level keys from the `eos_cli_config_gen` schema are detected and warned about. Nested keys within `eos_designs` data structures are not affected by this validation.

## Changes

### AVD 6.0 and Later

Starting with AVD 6.0, the `eos_designs` role emits warnings identifying the native `eos_cli_config_gen` keys being used at the top level of input data. The nominal behavior of `eos_designs` is to ignore `eos_cli_config_gen` native keys found at the top level of input data.

The solutions to address such warning should be in order of priority:

1. Look at the newest models introduced in `eos_designs` and use the relevant one. Many new features are added in each minor release to cover more and more in `eos_designs`.
2. If 1. is not possible, open an issue on Github describing your need and usecase and use custom structured configuration.

#### Example

The following `eos_cli_config_gen` key:

```yaml
# This will warn
dns_domain: my.awesome.domain.local
```

will emit a warning when read by `eos_designs`.

Following 1, it should be changed to

```yaml
dns_settings:
  # This will not warn
  domain: my.awesome.domain.local
```

Following the less preferred option 2, it could have been changed to:

```yaml
---
# assuming a default custom strutcured configuration prefix
# this will not warn
custom_structured_configuration_dns_domain: my.awesome.domain.local
```

#### Disabling Warnings

By default, warnings are enabled to help identify configuration that will be ignored. If you want to disable these warnings (for example, if you are aware of the ignored keys and want to suppress the notifications), you can set the `avd_eos_designs_warn_eos_cli_config_gen_keys` variable to `false`:

**In playbook:**

```yaml
- name: Generate AVD Structured Configurations and Fabric Documentation
  ansible.builtin.import_role:
    name: arista.avd.eos_designs
  vars:
    avd_eos_designs_warn_eos_cli_config_gen_keys: false
```

**In group_vars or host_vars:**

```yaml
# group_vars/FABRIC.yml
avd_eos_designs_warn_eos_cli_config_gen_keys: false
```

!!! warning
    Even when warnings are disabled, the top-level `eos_cli_config_gen` keys in `eos_designs` input data will still be ignored during `eos_cli_config_gen` processing. Disabling the warnings only suppresses the notification; it does not change the behavior of ignoring these keys.

### AVD 5.6

Starting with AVD 5.6, the `eos_designs` role emitted deprecation warnings identifying the native `eos_cli_config_gen` keys being used. This behavior was enhanced in AVD 6.0 to use the new validation system.

Please reach out to the maintainer team via [Github discussions](https://github.com/aristanetworks/avd/discussions) if you have any questions or concerns.
