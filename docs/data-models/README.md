<!--
  ~ Copyright (c) 2024-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Data Models

<div class="grid cards" markdown>

- :pencil2:{ .lg .middle } **AVD Design**

    ---

    AVD Design provides opinionated yet flexible network-wide data models expressing the intent of your network design and configuration.

    [Data Models](#avd-design) · <a href="../schema-explorer.html#/eos_designs">Schema Explorer</a>

- :material-file-document:{ .lg .middle } **EOS Config**

    ---

    EOS Config provides device-centric data models for expressing the Arista EOS device configuration syntax.

    [Data Models](../../ansible_collections/arista/avd/roles/eos_cli_config_gen/docs/data-models.md) · <a href="../schema-explorer.html#/eos_cli_config_gen">Schema Explorer</a>

</div>

The **[Schema Explorer](../schema-explorer.md)** offers a browsable, searchable view of every variable across both data models, with full type, default, deprecation, and cross-schema reference detail.

## AVD Design

The `eos_designs` input variable reference groups schema-backed data models by topic so you can navigate by area of the design, starting with [Topology](../../ansible_collections/arista/avd/roles/eos_designs/docs/user-manual/topology.md).

AVD Design data models are transformed by the Arista AVD framework to generate configuration, documentation and tests. You can extend or override Arista AVD's behaviour using `structured_config` or [custom structured configuration](../../ansible_collections/arista/avd/roles/eos_designs/docs/user-manual/custom-structured-configuration.md) with data models described in [EOS Config](../../ansible_collections/arista/avd/roles/eos_cli_config_gen/docs/data-models.md).

For Ansible users, the reference describes the supported input variables for the role `arista.avd.eos_designs`. The topic pages document the data models in tables and YAML.

Since several data models have changed between AVD versions 5.x and 6.x, it is recommended to study the [Porting Guide for AVD 6.x.x](../porting-guides/6.x.x.md) for existing deployments.

!!! note
    All AVD Design data models are validated by a schema. If additional custom keys are desired, keys starting with an underscore `_` will be ignored during validation.

!!! warning
    Available features and variables may vary by platform. Refer to documentation on arista.com for specifics.

!!! warning
    All keys marked as PREVIEW, or children of a key marked as PREVIEW, are subject to change and are not supported.
