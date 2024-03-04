<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>wan_path_groups</samp>](## "wan_path_groups") | List, items: Dictionary |  |  |  | PREVIEW: This key is currently not supported<br>List of path-groups used for the WAN configuration. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "wan_path_groups.[].name") | String | Required, Unique |  |  | Path-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "wan_path_groups.[].id") | Integer | Required |  |  | Path-group id.<br><br>TODO: Required until an auto ID algorithm is implemented. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "wan_path_groups.[].description") | String |  |  |  | Additional information about the path-group for documentation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipsec</samp>](## "wan_path_groups.[].ipsec") | Boolean |  | `True` |  | Flag to configure IPsec at the path-group level.<br><br>When set to `true`, IPsec is enabled for both the static and dynamic peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;import_path_groups</samp>](## "wan_path_groups.[].import_path_groups") | List, items: Dictionary |  |  |  | List of [ath-groups to import in this path-group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;remote</samp>](## "wan_path_groups.[].import_path_groups.[].remote") | String |  |  |  | Remote path-group to import. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local</samp>](## "wan_path_groups.[].import_path_groups.[].local") | String |  |  |  | Optional, if not set, the path-group `name` is used as local. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dps_keepalive</samp>](## "wan_path_groups.[].dps_keepalive") | Dictionary |  |  |  | Period between the transmission of consecutive keepalive messages, and failure threshold. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "wan_path_groups.[].dps_keepalive.interval") | String |  |  |  | Interval in milliseconds. Valid values are 50-60000 | "auto"<br><br>When auto, the interval and failure_threshold are automatically determined based on<br>path state. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;failure_threshold</samp>](## "wan_path_groups.[].dps_keepalive.failure_threshold") | Integer |  | `5` | Min: 2<br>Max: 100 | Failure threshold in number of lost keep-alive messages. |

=== "YAML"

    ```yaml
    # PREVIEW: This key is currently not supported
    # List of path-groups used for the WAN configuration.
    wan_path_groups:

        # Path-group name.
      - name: <str; required; unique>

        # Path-group id.
        #
        # TODO: Required until an auto ID algorithm is implemented.
        id: <int; required>

        # Additional information about the path-group for documentation purposes.
        description: <str>

        # Flag to configure IPsec at the path-group level.
        #
        # When set to `true`, IPsec is enabled for both the static and dynamic peers.
        ipsec: <bool; default=True>

        # List of [ath-groups to import in this path-group.
        import_path_groups:

            # Remote path-group to import.
          - remote: <str>

            # Optional, if not set, the path-group `name` is used as local.
            local: <str>

        # Period between the transmission of consecutive keepalive messages, and failure threshold.
        dps_keepalive:

          # Interval in milliseconds. Valid values are 50-60000 | "auto"
          #
          # When auto, the interval and failure_threshold are automatically determined based on
          # path state.
          interval: <str>

          # Failure threshold in number of lost keep-alive messages.
          failure_threshold: <int; 2-100; default=5>
    ```
