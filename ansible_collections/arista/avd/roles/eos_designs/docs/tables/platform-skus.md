<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>custom_platform_skus</samp>](## "custom_platform_skus") | List, items: Dictionary |  |  |  | Custom Platform settings to override the default `platform_skus`. This list will be prepended to the list of `platform_skus`. The first entry found where the `platform` node setting is fully matched by any regex in the `platforms` list will be chosen. If no matches are found, the first entry containing a platform `default` will be chosen. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "custom_platform_skus.[].name") | String | Required, Unique |  |  | Arista SKU name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;platform_family</samp>](## "custom_platform_skus.[].platform_family") | String | Required |  |  | Inherit settings from platform family name defined under `platform_families`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;management_interface</samp>](## "custom_platform_skus.[].management_interface") | String |  | `Management1` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;poe</samp>](## "custom_platform_skus.[].poe") | Boolean |  | `False` |  | Support for PoE.<br>The feature will be ignored on platforms where this is false. |
    | [<samp>platform_skus</samp>](## "platform_skus") | List, items: Dictionary |  |  |  | Platform settings. The first entry found where the `platform` node setting is fully matched by any regex in the `platforms` list will be chosen. If no matches are found, the first entry containing a platform `default` will be chosen. The default values will be overridden if `platform_skus` is defined. If you need to replace all the default platforms, it is recommended to copy the defaults and modify them. If you need to add custom platforms, create them under `custom_platform_skus`. Entries under `custom_platform_skus` will be matched before the equivalent entries from `platform_skus`. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "platform_skus.[].name") | String | Required, Unique |  |  | Arista SKU name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;platform_family</samp>](## "platform_skus.[].platform_family") | String | Required |  |  | Inherit settings from platform family name defined under `platform_families`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;management_interface</samp>](## "platform_skus.[].management_interface") | String |  | `Management1` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;poe</samp>](## "platform_skus.[].poe") | Boolean |  | `False` |  | Support for PoE.<br>The feature will be ignored on platforms where this is false. |

=== "YAML"

    ```yaml
    # Custom Platform settings to override the default `platform_skus`. This list will be prepended to the list of `platform_skus`. The first entry found where the `platform` node setting is fully matched by any regex in the `platforms` list will be chosen. If no matches are found, the first entry containing a platform `default` will be chosen.
    custom_platform_skus:

        # Arista SKU name.
      - name: <str; required; unique>

        # Inherit settings from platform family name defined under `platform_families`.
        platform_family: <str; required>
        management_interface: <str; default="Management1">

        # Support for PoE.
        # The feature will be ignored on platforms where this is false.
        poe: <bool; default=False>

    # Platform settings. The first entry found where the `platform` node setting is fully matched by any regex in the `platforms` list will be chosen. If no matches are found, the first entry containing a platform `default` will be chosen. The default values will be overridden if `platform_skus` is defined. If you need to replace all the default platforms, it is recommended to copy the defaults and modify them. If you need to add custom platforms, create them under `custom_platform_skus`. Entries under `custom_platform_skus` will be matched before the equivalent entries from `platform_skus`.
    platform_skus:

        # Arista SKU name.
      - name: <str; required; unique>

        # Inherit settings from platform family name defined under `platform_families`.
        platform_family: <str; required>
        management_interface: <str; default="Management1">

        # Support for PoE.
        # The feature will be ignored on platforms where this is false.
        poe: <bool; default=False>
    ```
