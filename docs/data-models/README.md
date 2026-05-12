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

The **[Schema Explorer](../schema-explorer.md)** offers a browsable, searchable view of every variable across both data models — grouped by category or by documentation table, with full type, default, deprecation, and cross-schema reference detail.

!!! note "Four integration variants for team comparison"

    - **Option 1 — iframe wrapper:** [Schema Explorer (iframe)](../schema-explorer.md). A MkDocs page hosts the SPA in an iframe; AVD docs banner stays put. SPA's own chrome hidden inside the iframe.
    - **Option 2 — banner-less SPA:** [Schema Explorer (no header)](../schema-explorer/index.html?style=none). Standalone SPA with no header at all — relies on whatever banner brought the user. Direct hits show no banner.
    - **Option 3 — standalone with restyled chrome:** [Schema Explorer (restyled)](../schema-explorer/index.html). Standalone SPA, but its header is restyled with the AVD logo, color, and typography so the visual swap from docs → SPA is near-invisible.
    - **Option 4 — MkDocs template override:** [Schema Explorer (native)](../schema-explorer-native.md). The SPA renders inside Material's chrome natively via a Jinja template override — no iframe, full Material header / nav / footer wrapping the SPA content.
