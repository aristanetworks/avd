<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>isis_advertise_passive_only</samp>](## "isis_advertise_passive_only") | Boolean |  | `False` |  |  |
    | [<samp>isis_area_id</samp>](## "isis_area_id") | String |  | `49.0001` |  |  |
    | [<samp>isis_default_circuit_type</samp>](## "isis_default_circuit_type") | String |  | `level-2` | Valid Values:<br>- <code>level-1-2</code><br>- <code>level-1</code><br>- <code>level-2</code> | These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden on link profile or link level.<br> |
    | [<samp>isis_default_is_type</samp>](## "isis_default_is_type") | String |  | `level-2` | Valid Values:<br>- <code>level-1-2</code><br>- <code>level-1</code><br>- <code>level-2</code> |  |
    | [<samp>isis_default_metric</samp>](## "isis_default_metric") | Integer |  | `50` |  | These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden at link profile or link level.<br> |
    | [<samp>isis_maximum_paths</samp>](## "isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>isis_system_id_format</samp>](## "isis_system_id_format") | String |  | `node_id` | Valid Values:<br>- <code>node_id</code><br>- <code>underlay_loopback</code> | Configures source for the system-id within the ISIS net id.<br>By default the `id` and `isis_system_id_prefix` fields configured under the node attributes are used to generate the system-id.<br><br>If `underlay_loopback` is selected then all node `isis_system_id_prefix` settings will be ignored and the loopback address will be used to generate the system-id. |
    | [<samp>isis_ti_lfa</samp>](## "isis_ti_lfa") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "isis_ti_lfa.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;protection</samp>](## "isis_ti_lfa.protection") | String |  |  | Valid Values:<br>- <code>link</code><br>- <code>node</code> |  |
    | [<samp>&nbsp;&nbsp;local_convergence_delay</samp>](## "isis_ti_lfa.local_convergence_delay") | Integer |  | `10000` |  | Local convergence delay in milliseconds. |
    | [<samp>underlay_isis_authentication</samp>](## "underlay_isis_authentication") | Dictionary |  |  |  | Only `md5` and `text` authentication modes are supported for `eos_designs`. |
    | [<samp>&nbsp;&nbsp;both</samp>](## "underlay_isis_authentication.both") | Dictionary |  |  |  | Authentication settings for level-1 and level-2. 'both' takes precedence over 'level_1' and 'level_2' settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "underlay_isis_authentication.both.key_type") | String |  |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. Default key_id is 0. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "underlay_isis_authentication.both.key") | String |  |  |  | Password string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key_ids</samp>](## "underlay_isis_authentication.both.key_ids") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "underlay_isis_authentication.both.key_ids.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 65535 | Configure authentication key-id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "underlay_isis_authentication.both.key_ids.[].algorithm") | String | Required |  | Valid Values:<br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "underlay_isis_authentication.both.key_ids.[].key_type") | String | Required |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "underlay_isis_authentication.both.key_ids.[].key") | String | Required |  |  | Password string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rfc_5310</samp>](## "underlay_isis_authentication.both.key_ids.[].rfc_5310") | Boolean |  |  |  | SHA digest computation according to rfc5310. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "underlay_isis_authentication.both.mode") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha</code><br>- <code>text</code><br>- <code>shared_secret</code> | Authentication mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha</samp>](## "underlay_isis_authentication.both.sha") | Dictionary |  |  |  | Required settings for authentication mode 'sha'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_id</samp>](## "underlay_isis_authentication.both.sha.key_id") | Integer | Required |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shared_secret</samp>](## "underlay_isis_authentication.both.shared_secret") | Dictionary |  |  |  | Required settings for authentication mode 'shared_secret'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "underlay_isis_authentication.both.shared_secret.profile") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "underlay_isis_authentication.both.shared_secret.algorithm") | String | Required |  | Valid Values:<br>- <code>md5</code><br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rx_disabled</samp>](## "underlay_isis_authentication.both.rx_disabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;level_1</samp>](## "underlay_isis_authentication.level_1") | Dictionary |  |  |  | Authentication settings for level-1. 'both' takes precedence over 'level_1' and 'level_2' settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "underlay_isis_authentication.level_1.key_type") | String |  |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. Default key_id is 0. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "underlay_isis_authentication.level_1.key") | String |  |  |  | Password string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key_ids</samp>](## "underlay_isis_authentication.level_1.key_ids") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "underlay_isis_authentication.level_1.key_ids.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 65535 | Configure authentication key-id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "underlay_isis_authentication.level_1.key_ids.[].algorithm") | String | Required |  | Valid Values:<br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "underlay_isis_authentication.level_1.key_ids.[].key_type") | String | Required |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "underlay_isis_authentication.level_1.key_ids.[].key") | String | Required |  |  | Password string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rfc_5310</samp>](## "underlay_isis_authentication.level_1.key_ids.[].rfc_5310") | Boolean |  |  |  | SHA digest computation according to rfc5310. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "underlay_isis_authentication.level_1.mode") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha</code><br>- <code>text</code><br>- <code>shared_secret</code> | Authentication mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha</samp>](## "underlay_isis_authentication.level_1.sha") | Dictionary |  |  |  | Required settings for authentication mode 'sha'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_id</samp>](## "underlay_isis_authentication.level_1.sha.key_id") | Integer | Required |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shared_secret</samp>](## "underlay_isis_authentication.level_1.shared_secret") | Dictionary |  |  |  | Required settings for authentication mode 'shared_secret'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "underlay_isis_authentication.level_1.shared_secret.profile") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "underlay_isis_authentication.level_1.shared_secret.algorithm") | String | Required |  | Valid Values:<br>- <code>md5</code><br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rx_disabled</samp>](## "underlay_isis_authentication.level_1.rx_disabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;level_2</samp>](## "underlay_isis_authentication.level_2") | Dictionary |  |  |  | Authentication settings for level-2. 'both' takes precedence over 'level_1' and 'level_2' settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "underlay_isis_authentication.level_2.key_type") | String |  |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. Default key_id is 0. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "underlay_isis_authentication.level_2.key") | String |  |  |  | Password string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key_ids</samp>](## "underlay_isis_authentication.level_2.key_ids") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "underlay_isis_authentication.level_2.key_ids.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 65535 | Configure authentication key-id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "underlay_isis_authentication.level_2.key_ids.[].algorithm") | String | Required |  | Valid Values:<br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "underlay_isis_authentication.level_2.key_ids.[].key_type") | String | Required |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "underlay_isis_authentication.level_2.key_ids.[].key") | String | Required |  |  | Password string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rfc_5310</samp>](## "underlay_isis_authentication.level_2.key_ids.[].rfc_5310") | Boolean |  |  |  | SHA digest computation according to rfc5310. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "underlay_isis_authentication.level_2.mode") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha</code><br>- <code>text</code><br>- <code>shared_secret</code> | Authentication mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha</samp>](## "underlay_isis_authentication.level_2.sha") | Dictionary |  |  |  | Required settings for authentication mode 'sha'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_id</samp>](## "underlay_isis_authentication.level_2.sha.key_id") | Integer | Required |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shared_secret</samp>](## "underlay_isis_authentication.level_2.shared_secret") | Dictionary |  |  |  | Required settings for authentication mode 'shared_secret'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "underlay_isis_authentication.level_2.shared_secret.profile") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "underlay_isis_authentication.level_2.shared_secret.algorithm") | String | Required |  | Valid Values:<br>- <code>md5</code><br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rx_disabled</samp>](## "underlay_isis_authentication.level_2.rx_disabled") | Boolean |  |  |  |  |
    | [<samp>underlay_isis_bfd</samp>](## "underlay_isis_bfd") | Boolean |  | `False` |  | Enable BFD for ISIS on all underlay links. |
    | [<samp>underlay_isis_instance_name</samp>](## "underlay_isis_instance_name") | String |  |  |  | Default -> "EVPN_UNDERLAY" for l3ls, "CORE" for mpls. |

=== "YAML"

    ```yaml
    isis_advertise_passive_only: <bool; default=False>
    isis_area_id: <str; default="49.0001">

    # These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden on link profile or link level.
    isis_default_circuit_type: <str; "level-1-2" | "level-1" | "level-2"; default="level-2">
    isis_default_is_type: <str; "level-1-2" | "level-1" | "level-2"; default="level-2">

    # These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden at link profile or link level.
    isis_default_metric: <int; default=50>

    # Number of path to configure in ECMP for ISIS.
    isis_maximum_paths: <int>

    # Configures source for the system-id within the ISIS net id.
    # By default the `id` and `isis_system_id_prefix` fields configured under the node attributes are used to generate the system-id.
    #
    # If `underlay_loopback` is selected then all node `isis_system_id_prefix` settings will be ignored and the loopback address will be used to generate the system-id.
    isis_system_id_format: <str; "node_id" | "underlay_loopback"; default="node_id">
    isis_ti_lfa:
      enabled: <bool; default=False>
      protection: <str; "link" | "node">

      # Local convergence delay in milliseconds.
      local_convergence_delay: <int; default=10000>

    # Only `md5` and `text` authentication modes are supported for `eos_designs`.
    underlay_isis_authentication:

      # Authentication settings for level-1 and level-2. 'both' takes precedence over 'level_1' and 'level_2' settings.
      both:

        # Configure authentication key type. Default key_id is 0.
        key_type: <str; "0" | "7" | "8a">

        # Password string.
        key: <str>
        key_ids:

            # Configure authentication key-id.
          - id: <int; 1-65535; required; unique>
            algorithm: <str; "sha-1" | "sha-224" | "sha-256" | "sha-384" | "sha-512"; required>

            # Configure authentication key type.
            key_type: <str; "0" | "7" | "8a"; required>

            # Password string.
            key: <str; required>

            # SHA digest computation according to rfc5310.
            rfc_5310: <bool>

        # Authentication mode.
        mode: <str; "md5" | "sha" | "text" | "shared_secret">

        # Required settings for authentication mode 'sha'.
        sha:
          key_id: <int; 1-65535; required>

        # Required settings for authentication mode 'shared_secret'.
        shared_secret:
          profile: <str; required>
          algorithm: <str; "md5" | "sha-1" | "sha-224" | "sha-256" | "sha-384" | "sha-512"; required>
        rx_disabled: <bool>

      # Authentication settings for level-1. 'both' takes precedence over 'level_1' and 'level_2' settings.
      level_1:

        # Configure authentication key type. Default key_id is 0.
        key_type: <str; "0" | "7" | "8a">

        # Password string.
        key: <str>
        key_ids:

            # Configure authentication key-id.
          - id: <int; 1-65535; required; unique>
            algorithm: <str; "sha-1" | "sha-224" | "sha-256" | "sha-384" | "sha-512"; required>

            # Configure authentication key type.
            key_type: <str; "0" | "7" | "8a"; required>

            # Password string.
            key: <str; required>

            # SHA digest computation according to rfc5310.
            rfc_5310: <bool>

        # Authentication mode.
        mode: <str; "md5" | "sha" | "text" | "shared_secret">

        # Required settings for authentication mode 'sha'.
        sha:
          key_id: <int; 1-65535; required>

        # Required settings for authentication mode 'shared_secret'.
        shared_secret:
          profile: <str; required>
          algorithm: <str; "md5" | "sha-1" | "sha-224" | "sha-256" | "sha-384" | "sha-512"; required>
        rx_disabled: <bool>

      # Authentication settings for level-2. 'both' takes precedence over 'level_1' and 'level_2' settings.
      level_2:

        # Configure authentication key type. Default key_id is 0.
        key_type: <str; "0" | "7" | "8a">

        # Password string.
        key: <str>
        key_ids:

            # Configure authentication key-id.
          - id: <int; 1-65535; required; unique>
            algorithm: <str; "sha-1" | "sha-224" | "sha-256" | "sha-384" | "sha-512"; required>

            # Configure authentication key type.
            key_type: <str; "0" | "7" | "8a"; required>

            # Password string.
            key: <str; required>

            # SHA digest computation according to rfc5310.
            rfc_5310: <bool>

        # Authentication mode.
        mode: <str; "md5" | "sha" | "text" | "shared_secret">

        # Required settings for authentication mode 'sha'.
        sha:
          key_id: <int; 1-65535; required>

        # Required settings for authentication mode 'shared_secret'.
        shared_secret:
          profile: <str; required>
          algorithm: <str; "md5" | "sha-1" | "sha-224" | "sha-256" | "sha-384" | "sha-512"; required>
        rx_disabled: <bool>

    # Enable BFD for ISIS on all underlay links.
    underlay_isis_bfd: <bool; default=False>

    # Default -> "EVPN_UNDERLAY" for l3ls, "CORE" for mpls.
    underlay_isis_instance_name: <str>
    ```
