<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "<node_type_keys.key>.defaults.isis_system_id_prefix") | String |  |  | Pattern: `[0-9a-f]{4}\.[0-9a-f]{4}` | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "<node_type_keys.key>.defaults.isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "<node_type_keys.key>.defaults.is_type") | String |  |  | Valid Values:<br>- <code>level-1-2</code><br>- <code>level-1</code><br>- <code>level-2</code> | Overrides `isis_default_is_type`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "<node_type_keys.key>.defaults.node_sid_base") <span style="color:red">deprecated</span> | Integer |  | `0` |  | IPv4 Node-SID Index base for ISIS-SR underlay variants. Combined with node ID to generate ISIS-SR Node-SID index.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>isis_sr.ipv4_node_sid_index_base</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_sr</samp>](## "<node_type_keys.key>.defaults.isis_sr") | Dictionary |  |  |  | Device settings for ISIS-SR underlay variants. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_node_sid_index</samp>](## "<node_type_keys.key>.defaults.isis_sr.ipv4_node_sid_index") | Integer |  |  |  | Optional static IPv4 Node-SID Index.<br>Takes precedence over the default node ID + `ipv4_node_sid_index_base` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_node_sid_index_base</samp>](## "<node_type_keys.key>.defaults.isis_sr.ipv4_node_sid_index_base") | Integer |  | `0` |  | IPv4 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_node_sid_index</samp>](## "<node_type_keys.key>.defaults.isis_sr.ipv6_node_sid_index") | Integer |  |  |  | Optional static IPv6 Node-SID Index.<br>Takes precedence over the default node ID + `ipv6_node_sid_index_base` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_node_sid_index_base</samp>](## "<node_type_keys.key>.defaults.isis_sr.ipv6_node_sid_index_base") | Integer |  | `1000` |  | IPv6 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].isis_system_id_prefix") | String |  |  | Pattern: `[0-9a-f]{4}\.[0-9a-f]{4}` | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].is_type") | String |  |  | Valid Values:<br>- <code>level-1-2</code><br>- <code>level-1</code><br>- <code>level-2</code> | Overrides `isis_default_is_type`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].node_sid_base") <span style="color:red">deprecated</span> | Integer |  | `0` |  | IPv4 Node-SID Index base for ISIS-SR underlay variants. Combined with node ID to generate ISIS-SR Node-SID index.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>isis_sr.ipv4_node_sid_index_base</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_sr</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].isis_sr") | Dictionary |  |  |  | Device settings for ISIS-SR underlay variants. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_node_sid_index</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].isis_sr.ipv4_node_sid_index") | Integer |  |  |  | Optional static IPv4 Node-SID Index.<br>Takes precedence over the default node ID + `ipv4_node_sid_index_base` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_node_sid_index_base</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].isis_sr.ipv4_node_sid_index_base") | Integer |  | `0` |  | IPv4 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_node_sid_index</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].isis_sr.ipv6_node_sid_index") | Integer |  |  |  | Optional static IPv6 Node-SID Index.<br>Takes precedence over the default node ID + `ipv6_node_sid_index_base` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_node_sid_index_base</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].isis_sr.ipv6_node_sid_index_base") | Integer |  | `1000` |  | IPv6 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "<node_type_keys.key>.node_groups.[].isis_system_id_prefix") | String |  |  | Pattern: `[0-9a-f]{4}\.[0-9a-f]{4}` | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "<node_type_keys.key>.node_groups.[].isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "<node_type_keys.key>.node_groups.[].is_type") | String |  |  | Valid Values:<br>- <code>level-1-2</code><br>- <code>level-1</code><br>- <code>level-2</code> | Overrides `isis_default_is_type`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "<node_type_keys.key>.node_groups.[].node_sid_base") <span style="color:red">deprecated</span> | Integer |  | `0` |  | IPv4 Node-SID Index base for ISIS-SR underlay variants. Combined with node ID to generate ISIS-SR Node-SID index.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>isis_sr.ipv4_node_sid_index_base</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_sr</samp>](## "<node_type_keys.key>.node_groups.[].isis_sr") | Dictionary |  |  |  | Device settings for ISIS-SR underlay variants. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_node_sid_index</samp>](## "<node_type_keys.key>.node_groups.[].isis_sr.ipv4_node_sid_index") | Integer |  |  |  | Optional static IPv4 Node-SID Index.<br>Takes precedence over the default node ID + `ipv4_node_sid_index_base` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_node_sid_index_base</samp>](## "<node_type_keys.key>.node_groups.[].isis_sr.ipv4_node_sid_index_base") | Integer |  | `0` |  | IPv4 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_node_sid_index</samp>](## "<node_type_keys.key>.node_groups.[].isis_sr.ipv6_node_sid_index") | Integer |  |  |  | Optional static IPv6 Node-SID Index.<br>Takes precedence over the default node ID + `ipv6_node_sid_index_base` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_node_sid_index_base</samp>](## "<node_type_keys.key>.node_groups.[].isis_sr.ipv6_node_sid_index_base") | Integer |  | `1000` |  | IPv6 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "<node_type_keys.key>.nodes.[].isis_system_id_prefix") | String |  |  | Pattern: `[0-9a-f]{4}\.[0-9a-f]{4}` | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "<node_type_keys.key>.nodes.[].isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "<node_type_keys.key>.nodes.[].is_type") | String |  |  | Valid Values:<br>- <code>level-1-2</code><br>- <code>level-1</code><br>- <code>level-2</code> | Overrides `isis_default_is_type`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "<node_type_keys.key>.nodes.[].node_sid_base") <span style="color:red">deprecated</span> | Integer |  | `0` |  | IPv4 Node-SID Index base for ISIS-SR underlay variants. Combined with node ID to generate ISIS-SR Node-SID index.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>isis_sr.ipv4_node_sid_index_base</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_sr</samp>](## "<node_type_keys.key>.nodes.[].isis_sr") | Dictionary |  |  |  | Device settings for ISIS-SR underlay variants. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_node_sid_index</samp>](## "<node_type_keys.key>.nodes.[].isis_sr.ipv4_node_sid_index") | Integer |  |  |  | Optional static IPv4 Node-SID Index.<br>Takes precedence over the default node ID + `ipv4_node_sid_index_base` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_node_sid_index_base</samp>](## "<node_type_keys.key>.nodes.[].isis_sr.ipv4_node_sid_index_base") | Integer |  | `0` |  | IPv4 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_node_sid_index</samp>](## "<node_type_keys.key>.nodes.[].isis_sr.ipv6_node_sid_index") | Integer |  |  |  | Optional static IPv6 Node-SID Index.<br>Takes precedence over the default node ID + `ipv6_node_sid_index_base` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_node_sid_index_base</samp>](## "<node_type_keys.key>.nodes.[].isis_sr.ipv6_node_sid_index_base") | Integer |  | `1000` |  | IPv6 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index. |
    | [<samp>device_profiles</samp>](## "device_profiles") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "device_profiles.[].name") | String | Required, Unique |  |  | Profile Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "device_profiles.[].isis_system_id_prefix") | String |  |  | Pattern: `[0-9a-f]{4}\.[0-9a-f]{4}` | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "device_profiles.[].isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "device_profiles.[].is_type") | String |  |  | Valid Values:<br>- <code>level-1-2</code><br>- <code>level-1</code><br>- <code>level-2</code> | Overrides `isis_default_is_type`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "device_profiles.[].node_sid_base") <span style="color:red">deprecated</span> | Integer |  | `0` |  | IPv4 Node-SID Index base for ISIS-SR underlay variants. Combined with node ID to generate ISIS-SR Node-SID index.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>isis_sr.ipv4_node_sid_index_base</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_sr</samp>](## "device_profiles.[].isis_sr") | Dictionary |  |  |  | Device settings for ISIS-SR underlay variants. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_node_sid_index</samp>](## "device_profiles.[].isis_sr.ipv4_node_sid_index") | Integer |  |  |  | Optional static IPv4 Node-SID Index.<br>Takes precedence over the default node ID + `ipv4_node_sid_index_base` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_node_sid_index_base</samp>](## "device_profiles.[].isis_sr.ipv4_node_sid_index_base") | Integer |  | `0` |  | IPv4 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_node_sid_index</samp>](## "device_profiles.[].isis_sr.ipv6_node_sid_index") | Integer |  |  |  | Optional static IPv6 Node-SID Index.<br>Takes precedence over the default node ID + `ipv6_node_sid_index_base` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_node_sid_index_base</samp>](## "device_profiles.[].isis_sr.ipv6_node_sid_index_base") | Integer |  | `1000` |  | IPv6 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index. |
    | [<samp>devices</samp>](## "devices") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "devices.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "devices.[].isis_system_id_prefix") | String |  |  | Pattern: `[0-9a-f]{4}\.[0-9a-f]{4}` | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "devices.[].isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "devices.[].is_type") | String |  |  | Valid Values:<br>- <code>level-1-2</code><br>- <code>level-1</code><br>- <code>level-2</code> | Overrides `isis_default_is_type`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "devices.[].node_sid_base") <span style="color:red">deprecated</span> | Integer |  | `0` |  | IPv4 Node-SID Index base for ISIS-SR underlay variants. Combined with node ID to generate ISIS-SR Node-SID index.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>isis_sr.ipv4_node_sid_index_base</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_sr</samp>](## "devices.[].isis_sr") | Dictionary |  |  |  | Device settings for ISIS-SR underlay variants. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_node_sid_index</samp>](## "devices.[].isis_sr.ipv4_node_sid_index") | Integer |  |  |  | Optional static IPv4 Node-SID Index.<br>Takes precedence over the default node ID + `ipv4_node_sid_index_base` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_node_sid_index_base</samp>](## "devices.[].isis_sr.ipv4_node_sid_index_base") | Integer |  | `0` |  | IPv4 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_node_sid_index</samp>](## "devices.[].isis_sr.ipv6_node_sid_index") | Integer |  |  |  | Optional static IPv6 Node-SID Index.<br>Takes precedence over the default node ID + `ipv6_node_sid_index_base` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_node_sid_index_base</samp>](## "devices.[].isis_sr.ipv6_node_sid_index_base") | Integer |  | `1000` |  | IPv6 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # (4.4 hexadecimal).
        isis_system_id_prefix: <str>

        # Number of path to configure in ECMP for ISIS.
        isis_maximum_paths: <int>

        # Overrides `isis_default_is_type`.
        is_type: <str; "level-1-2" | "level-1" | "level-2">

        # IPv4 Node-SID Index base for ISIS-SR underlay variants. Combined with node ID to generate ISIS-SR Node-SID index.
        # This key is deprecated.
        # Support will be removed in AVD version 7.0.0.
        # Use `isis_sr.ipv4_node_sid_index_base` instead.
        node_sid_base: <int; default=0>

        # Device settings for ISIS-SR underlay variants.
        isis_sr:

          # Optional static IPv4 Node-SID Index.
          # Takes precedence over the default node ID + `ipv4_node_sid_index_base`
          ipv4_node_sid_index: <int>

          # IPv4 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index.
          ipv4_node_sid_index_base: <int; default=0>

          # Optional static IPv6 Node-SID Index.
          # Takes precedence over the default node ID + `ipv6_node_sid_index_base`
          ipv6_node_sid_index: <int>

          # IPv6 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index.
          ipv6_node_sid_index_base: <int; default=1000>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # (4.4 hexadecimal).
              isis_system_id_prefix: <str>

              # Number of path to configure in ECMP for ISIS.
              isis_maximum_paths: <int>

              # Overrides `isis_default_is_type`.
              is_type: <str; "level-1-2" | "level-1" | "level-2">

              # IPv4 Node-SID Index base for ISIS-SR underlay variants. Combined with node ID to generate ISIS-SR Node-SID index.
              # This key is deprecated.
              # Support will be removed in AVD version 7.0.0.
              # Use `isis_sr.ipv4_node_sid_index_base` instead.
              node_sid_base: <int; default=0>

              # Device settings for ISIS-SR underlay variants.
              isis_sr:

                # Optional static IPv4 Node-SID Index.
                # Takes precedence over the default node ID + `ipv4_node_sid_index_base`
                ipv4_node_sid_index: <int>

                # IPv4 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index.
                ipv4_node_sid_index_base: <int; default=0>

                # Optional static IPv6 Node-SID Index.
                # Takes precedence over the default node ID + `ipv6_node_sid_index_base`
                ipv6_node_sid_index: <int>

                # IPv6 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index.
                ipv6_node_sid_index_base: <int; default=1000>

          # (4.4 hexadecimal).
          isis_system_id_prefix: <str>

          # Number of path to configure in ECMP for ISIS.
          isis_maximum_paths: <int>

          # Overrides `isis_default_is_type`.
          is_type: <str; "level-1-2" | "level-1" | "level-2">

          # IPv4 Node-SID Index base for ISIS-SR underlay variants. Combined with node ID to generate ISIS-SR Node-SID index.
          # This key is deprecated.
          # Support will be removed in AVD version 7.0.0.
          # Use `isis_sr.ipv4_node_sid_index_base` instead.
          node_sid_base: <int; default=0>

          # Device settings for ISIS-SR underlay variants.
          isis_sr:

            # Optional static IPv4 Node-SID Index.
            # Takes precedence over the default node ID + `ipv4_node_sid_index_base`
            ipv4_node_sid_index: <int>

            # IPv4 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index.
            ipv4_node_sid_index_base: <int; default=0>

            # Optional static IPv6 Node-SID Index.
            # Takes precedence over the default node ID + `ipv6_node_sid_index_base`
            ipv6_node_sid_index: <int>

            # IPv6 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index.
            ipv6_node_sid_index_base: <int; default=1000>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # (4.4 hexadecimal).
          isis_system_id_prefix: <str>

          # Number of path to configure in ECMP for ISIS.
          isis_maximum_paths: <int>

          # Overrides `isis_default_is_type`.
          is_type: <str; "level-1-2" | "level-1" | "level-2">

          # IPv4 Node-SID Index base for ISIS-SR underlay variants. Combined with node ID to generate ISIS-SR Node-SID index.
          # This key is deprecated.
          # Support will be removed in AVD version 7.0.0.
          # Use `isis_sr.ipv4_node_sid_index_base` instead.
          node_sid_base: <int; default=0>

          # Device settings for ISIS-SR underlay variants.
          isis_sr:

            # Optional static IPv4 Node-SID Index.
            # Takes precedence over the default node ID + `ipv4_node_sid_index_base`
            ipv4_node_sid_index: <int>

            # IPv4 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index.
            ipv4_node_sid_index_base: <int; default=0>

            # Optional static IPv6 Node-SID Index.
            # Takes precedence over the default node ID + `ipv6_node_sid_index_base`
            ipv6_node_sid_index: <int>

            # IPv6 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index.
            ipv6_node_sid_index_base: <int; default=1000>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    device_profiles:

        # Profile Name
      - name: <str; required; unique>

        # (4.4 hexadecimal).
        isis_system_id_prefix: <str>

        # Number of path to configure in ECMP for ISIS.
        isis_maximum_paths: <int>

        # Overrides `isis_default_is_type`.
        is_type: <str; "level-1-2" | "level-1" | "level-2">

        # IPv4 Node-SID Index base for ISIS-SR underlay variants. Combined with node ID to generate ISIS-SR Node-SID index.
        # This key is deprecated.
        # Support will be removed in AVD version 7.0.0.
        # Use `isis_sr.ipv4_node_sid_index_base` instead.
        node_sid_base: <int; default=0>

        # Device settings for ISIS-SR underlay variants.
        isis_sr:

          # Optional static IPv4 Node-SID Index.
          # Takes precedence over the default node ID + `ipv4_node_sid_index_base`
          ipv4_node_sid_index: <int>

          # IPv4 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index.
          ipv4_node_sid_index_base: <int; default=0>

          # Optional static IPv6 Node-SID Index.
          # Takes precedence over the default node ID + `ipv6_node_sid_index_base`
          ipv6_node_sid_index: <int>

          # IPv6 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index.
          ipv6_node_sid_index_base: <int; default=1000>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    devices:

        # The Node Name is used as "hostname".
        name: <str; required; unique>

        # (4.4 hexadecimal).
        isis_system_id_prefix: <str>

        # Number of path to configure in ECMP for ISIS.
        isis_maximum_paths: <int>

        # Overrides `isis_default_is_type`.
        is_type: <str; "level-1-2" | "level-1" | "level-2">

        # IPv4 Node-SID Index base for ISIS-SR underlay variants. Combined with node ID to generate ISIS-SR Node-SID index.
        # This key is deprecated.
        # Support will be removed in AVD version 7.0.0.
        # Use `isis_sr.ipv4_node_sid_index_base` instead.
        node_sid_base: <int; default=0>

        # Device settings for ISIS-SR underlay variants.
        isis_sr:

          # Optional static IPv4 Node-SID Index.
          # Takes precedence over the default node ID + `ipv4_node_sid_index_base`
          ipv4_node_sid_index: <int>

          # IPv4 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index.
          ipv4_node_sid_index_base: <int; default=0>

          # Optional static IPv6 Node-SID Index.
          # Takes precedence over the default node ID + `ipv6_node_sid_index_base`
          ipv6_node_sid_index: <int>

          # IPv6 Node-SID Index base. Combined with node ID to generate ISIS-SR Node-SID index.
          ipv6_node_sid_index_base: <int; default=1000>
    ```
