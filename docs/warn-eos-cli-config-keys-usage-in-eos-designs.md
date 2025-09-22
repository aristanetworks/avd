<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
# Of using `eos_cli_config_gen` native keys when running `eos_designs`

## Context

For several AVD major versions, it has been possible to use variables from the `eos_cli_config_gen` data model in conjunction with variables from the `eos_designs` data model. When the `eos_designs`
role runs, the `eos_cli_config_gen` keys are ignored but they will be read later by the `eos_cli_config_gen` role.

While this behavior could serve as a good escape hatch, it has led to confusion among users. Especially when new features introduced in `eos_designs` ended up shadowing the inputs intended for `eos_cli_config_gen`,
sometimes leading to configuration changes after a minor releases upgrade. This behavior is well documented and described in the `eos_designs` how-to on
[custom_structured_configuration](../ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-structured-configuration.md) which is the recommended way of
using `eos_cli_config_gen` variables within `eos_designs`. However the direct usage of `eos_cli_config_gen` variables still works.

## Changes

### AVD 5.6

Starting AVD 5.6, the `eos_designs` role emits deprecation warning identifying the native `eos_cli_config_gen` keys being used.

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
custom_structured_config_dns_domain: my.awesome.domain.local
```

### Future

Starting AVD 6.0, the nominal behavior of `eos_designs` will be to ignore `eos_cli_config_gen` native keys.

Please reach out to the maintainer team via [Github discussions](https://github.com/aristanetworks/avd/discussions) if you have any questions or concerns.
