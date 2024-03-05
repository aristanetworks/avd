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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;import_path_groups</samp>](## "wan_path_groups.[].import_path_groups") | List, items: Dictionary |  |  |  | List of path-groups to import in this path-group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;remote</samp>](## "wan_path_groups.[].import_path_groups.[].remote") | String |  |  |  | Remote path-group to import. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local</samp>](## "wan_path_groups.[].import_path_groups.[].local") | String |  |  |  | Optional, if not set, the path-group `name` is used as local. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_preference</samp>](## "wan_path_groups.[].default_preference") | String |  | `preferred` |  | Preference value used when a preference is not given for a path-group in the `wan_virtual_topologies.policies` input or when<br>the path-group is used in an auto generated policy except if `excluded_from_default_policy` is set to `true.<br><br>Valid values are 1-65535 | "preferred" | "alternate".<br><br>`preferred` is converted to priority 1.<br>`alternate` is converted to priority 2. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;excluded_from_default_policy</samp>](## "wan_path_groups.[].excluded_from_default_policy") | Boolean |  | `False` |  | When set to `true`, the path-group is excluded from AVD auto generated policies. |
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

        # List of path-groups to import in this path-group.
        import_path_groups:

            # Remote path-group to import.
          - remote: <str>

            # Optional, if not set, the path-group `name` is used as local.
            local: <str>

        # Preference value used when a preference is not given for a path-group in the `wan_virtual_topologies.policies` input or when
        # the path-group is used in an auto generated policy except if `excluded_from_default_policy` is set to `true.
        #
        # Valid values are 1-65535 | "preferred" | "alternate".
        #
        # `preferred` is converted to priority 1.
        # `alternate` is converted to priority 2.
        default_preference: <str; default="preferred">

        # When set to `true`, the path-group is excluded from AVD auto generated policies.
        excluded_from_default_policy: <bool; default=False>

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
