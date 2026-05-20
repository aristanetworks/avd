<!--
  ~ Copyright (c) 2024-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

<div class="grid cards" markdown>

- :pencil2:{ .lg .middle } **AVD Design**

    ---

    AVD Design provides opinionated yet flexible network-wide data models expressing the intent of your network design and configuration.

    [Data Models](../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md) · [Schema Explorer](../schema-explorer.md#/eos_designs)

- :material-file-document:{ .lg .middle } **EOS Config**

    ---

    EOS Config provides device-centric data models for expressing the Arista EOS device configuration syntax.

    [Data Models](../../ansible_collections/arista/avd/roles/eos_cli_config_gen/docs/data-models.md) · [Schema Explorer](../schema-explorer.md#/eos_cli_config_gen)

</div>

The **[Schema Explorer](../schema-explorer.md)** offers a browsable, searchable view of every variable across both data models — grouped by category or by documentation table, with full type, default, deprecation, and cross-schema reference detail. It renders inside Material's chrome (same header, same nav) — no switch to a separate SPA page.

## Embedded preview

The same explorer can also be embedded directly inside any docs page via the `<schema-explorer>` custom element — Material's chrome, navigation, and right-rail TOC stay intact. Example below: a tree view scoped to the `router_bgp` subtree of the EOS Config schema.

<schema-explorer module="eos_cli_config_gen" root="router_bgp" height="500px"></schema-explorer>
