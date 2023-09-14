<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "&lt;node_type_keys.key&gt;.defaults.isis_system_id_prefix") | String |  |  | Pattern: [0-9a-f]{4}\.[0-9a-f]{4} | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "&lt;node_type_keys.key&gt;.defaults.isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "&lt;node_type_keys.key&gt;.defaults.is_type") | String |  | `level-2` | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "&lt;node_type_keys.key&gt;.defaults.node_sid_base") | Integer |  | `0` |  | Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- group</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].isis_system_id_prefix") | String |  |  | Pattern: [0-9a-f]{4}\.[0-9a-f]{4} | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].is_type") | String |  | `level-2` | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].node_sid_base") | Integer |  | `0` |  | Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].isis_system_id_prefix") | String |  |  | Pattern: [0-9a-f]{4}\.[0-9a-f]{4} | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].is_type") | String |  | `level-2` | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].node_sid_base") | Integer |  | `0` |  | Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].isis_system_id_prefix") | String |  |  | Pattern: [0-9a-f]{4}\.[0-9a-f]{4} | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].is_type") | String |  | `level-2` | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].node_sid_base") | Integer |  | `0` |  | Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
        isis_system_id_prefix: <str>
        isis_maximum_paths: <int>
        is_type: <str>
        node_sid_base: <int>
      node_groups:
        - group: <str>
          nodes:
            - name: <str>
              isis_system_id_prefix: <str>
              isis_maximum_paths: <int>
              is_type: <str>
              node_sid_base: <int>
          isis_system_id_prefix: <str>
          isis_maximum_paths: <int>
          is_type: <str>
          node_sid_base: <int>
      nodes:
        - name: <str>
          isis_system_id_prefix: <str>
          isis_maximum_paths: <int>
          is_type: <str>
          node_sid_base: <int>
    ```
