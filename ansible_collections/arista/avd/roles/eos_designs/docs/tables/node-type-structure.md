<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_listen_range_prefixes</samp>](## "<node_type_keys.key>.defaults.bgp_listen_range_prefixes") | List, items: String |  |  |  | Only used for nodes where `wan_role` is `server` like AutoVPN RRs and Pathfinders. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.defaults.bgp_listen_range_prefixes.[]") | String |  |  |  | The prefixes to use in listen_range. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_listen_range_prefixes</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].bgp_listen_range_prefixes") | List, items: String |  |  |  | Only used for nodes where `wan_role` is `server` like AutoVPN RRs and Pathfinders. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].bgp_listen_range_prefixes.[]") | String |  |  |  | The prefixes to use in listen_range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_listen_range_prefixes</samp>](## "<node_type_keys.key>.node_groups.[].bgp_listen_range_prefixes") | List, items: String |  |  |  | Only used for nodes where `wan_role` is `server` like AutoVPN RRs and Pathfinders. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].bgp_listen_range_prefixes.[]") | String |  |  |  | The prefixes to use in listen_range. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_listen_range_prefixes</samp>](## "<node_type_keys.key>.nodes.[].bgp_listen_range_prefixes") | List, items: String |  |  |  | Only used for nodes where `wan_role` is `server` like AutoVPN RRs and Pathfinders. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.nodes.[].bgp_listen_range_prefixes.[]") | String |  |  |  | The prefixes to use in listen_range. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # Only used for nodes where `wan_role` is `server` like AutoVPN RRs and Pathfinders.
        bgp_listen_range_prefixes:

            # The prefixes to use in listen_range.
          - <str>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # Only used for nodes where `wan_role` is `server` like AutoVPN RRs and Pathfinders.
              bgp_listen_range_prefixes:

                  # The prefixes to use in listen_range.
                - <str>

          # Only used for nodes where `wan_role` is `server` like AutoVPN RRs and Pathfinders.
          bgp_listen_range_prefixes:

              # The prefixes to use in listen_range.
            - <str>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # Only used for nodes where `wan_role` is `server` like AutoVPN RRs and Pathfinders.
          bgp_listen_range_prefixes:

              # The prefixes to use in listen_range.
            - <str>
    ```
