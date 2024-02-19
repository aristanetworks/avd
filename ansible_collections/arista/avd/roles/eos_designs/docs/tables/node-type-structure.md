<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssl_profile</samp>](## "<node_type_keys.key>.defaults.ssl_profile") | String |  |  |  | ssl_profile_name will be used as a name for cert,<br>keys which will be internally created by CVP and pushed to respective devices.<br>Used for communication with stun server. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ssl_profile</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ssl_profile") | String |  |  |  | ssl_profile_name will be used as a name for cert,<br>keys which will be internally created by CVP and pushed to respective devices.<br>Used for communication with stun server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ssl_profile</samp>](## "<node_type_keys.key>.node_groups.[].ssl_profile") | String |  |  |  | ssl_profile_name will be used as a name for cert,<br>keys which will be internally created by CVP and pushed to respective devices.<br>Used for communication with stun server. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ssl_profile</samp>](## "<node_type_keys.key>.nodes.[].ssl_profile") | String |  |  |  | ssl_profile_name will be used as a name for cert,<br>keys which will be internally created by CVP and pushed to respective devices.<br>Used for communication with stun server. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # ssl_profile_name will be used as a name for cert,
        # keys which will be internally created by CVP and pushed to respective devices.
        # Used for communication with stun server.
        ssl_profile: <str>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # ssl_profile_name will be used as a name for cert,
              # keys which will be internally created by CVP and pushed to respective devices.
              # Used for communication with stun server.
              ssl_profile: <str>

          # ssl_profile_name will be used as a name for cert,
          # keys which will be internally created by CVP and pushed to respective devices.
          # Used for communication with stun server.
          ssl_profile: <str>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # ssl_profile_name will be used as a name for cert,
          # keys which will be internally created by CVP and pushed to respective devices.
          # Used for communication with stun server.
          ssl_profile: <str>
    ```
