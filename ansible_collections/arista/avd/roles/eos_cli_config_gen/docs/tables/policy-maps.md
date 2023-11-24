<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>policy_maps</samp>](## "policy_maps") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;pbr</samp>](## "policy_maps.pbr") | List, items: Dictionary |  |  |  | PBR Policy-Maps |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "policy_maps.pbr.[].name") | String | Required, Unique |  |  | Policy-Map Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;classes</samp>](## "policy_maps.pbr.[].classes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "policy_maps.pbr.[].classes.[].name") | String | Required, Unique |  |  | Class Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index</samp>](## "policy_maps.pbr.[].classes.[].index") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "policy_maps.pbr.[].classes.[].drop") | Boolean |  |  |  | 'drop' and 'set' are mutually exclusive |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set</samp>](## "policy_maps.pbr.[].classes.[].set") | Dictionary |  |  |  | Set Nexthop<br>'drop' and 'set' are mutually exclusive<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nexthop</samp>](## "policy_maps.pbr.[].classes.[].set.nexthop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "policy_maps.pbr.[].classes.[].set.nexthop.ip_address") | String |  |  |  | IPv4 or IPv6 Address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recursive</samp>](## "policy_maps.pbr.[].classes.[].set.nexthop.recursive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;qos</samp>](## "policy_maps.qos") | List, items: Dictionary |  |  |  | QOS Policy-Maps |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "policy_maps.qos.[].name") | String | Required, Unique |  |  | Policy-Map Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;classes</samp>](## "policy_maps.qos.[].classes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "policy_maps.qos.[].classes.[].name") | String | Required, Unique |  |  | Class Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set</samp>](## "policy_maps.qos.[].classes.[].set") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "policy_maps.qos.[].classes.[].set.cos") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "policy_maps.qos.[].classes.[].set.dscp") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "policy_maps.qos.[].classes.[].set.traffic_class") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop_precedence</samp>](## "policy_maps.qos.[].classes.[].set.drop_precedence") | Integer |  |  |  |  |

=== "YAML"

    ```yaml
    policy_maps:

      # PBR Policy-Maps
      pbr:

          # Policy-Map Name
        - name: <str; required; unique>
          classes:

              # Class Name
            - name: <str; required; unique>
              index: <int>

              # 'drop' and 'set' are mutually exclusive
              drop: <bool>

              # Set Nexthop
              # 'drop' and 'set' are mutually exclusive
              set:
                nexthop:

                  # IPv4 or IPv6 Address
                  ip_address: <str>
                  recursive: <bool>

      # QOS Policy-Maps
      qos:

          # Policy-Map Name
        - name: <str; required; unique>
          classes:

              # Class Name
            - name: <str; required; unique>
              set:
                cos: <int>
                dscp: <str>
                traffic_class: <int>
                drop_precedence: <int>
    ```
