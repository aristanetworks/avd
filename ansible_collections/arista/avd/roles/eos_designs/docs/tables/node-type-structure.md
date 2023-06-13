=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_compact_addressing</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_compact_addressing") | Boolean |  | `False` |  | Generate MLAG ip addresses based on the odd ID of an ID pair, this a /31 per allocation<br>Requires MLAG pairs have nodes with an odd and even ID<br> |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- group</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_compact_addressing</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_compact_addressing") | Boolean |  | `False` |  | Generate MLAG ip addresses based on the odd ID of an ID pair, this a /31 per allocation<br>Requires MLAG pairs have nodes with an odd and even ID<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_compact_addressing</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_compact_addressing") | Boolean |  | `False` |  | Generate MLAG ip addresses based on the odd ID of an ID pair, this a /31 per allocation<br>Requires MLAG pairs have nodes with an odd and even ID<br> |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_compact_addressing</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_compact_addressing") | Boolean |  | `False` |  | Generate MLAG ip addresses based on the odd ID of an ID pair, this a /31 per allocation<br>Requires MLAG pairs have nodes with an odd and even ID<br> |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
        mlag_compact_addressing: <bool>
      node_groups:
        - group: <str>
          nodes:
            - name: <str>
              mlag_compact_addressing: <bool>
          mlag_compact_addressing: <bool>
      nodes:
        - name: <str>
          mlag_compact_addressing: <bool>
    ```
