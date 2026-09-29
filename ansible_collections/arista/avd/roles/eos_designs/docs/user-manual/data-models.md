---
# This title is used for search results
title: AVD Design data models (eos_designs)
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# AVD Design data models (eos_designs)

AVD Design data models provide opinionated yet flexible network-wide data models expressing the intent of your network design and configuration. AVD Design data models are transformed by the Arista AVD framework to generate configuration, documentation and tests. You can extend or override Arista AVD's behaviour by leveraging "structured config" or [custom structured configuration](../how-to/custom-structured-configuration.md) with data models described in [EOS Config](../../../eos_cli_config_gen/docs/data-models.md).

For Ansible users this document describes the supported input variables for the role `arista.avd.eos_designs`.

Since several data models have changed between AVD versions 5.x and 6.x, it is recommended to study the [Porting Guide for AVD 6.x.x](../../../../../../../docs/porting-guides/6.x.x.md) for existing deployments.

The data models are documented below in tables and YAML.

!!! note
    All AVD Design data models are validated by a schema. If additional custom keys are desired, a key starting with an underscore `_`, will be ignored.

!!! warning
    Available features and variables may vary by platforms, refer to documentation on arista.com for specifics.

!!! warning
    All the keys marked as PREVIEW or children of a key marked as PREVIEW are subject to change and are not supported.

## Custom Structured Configuration

See the [Custom Structured Configuration](../how-to/custom-structured-configuration.md) how-to for details.

--8<--
schemas/avd_design/docs/tables/custom-structured-configuration.md
--8<--
