---
search:
  boost: 2
---

# Spanning Tree

## Spanning Tree

=== "Spanning Tree"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>spanning_tree</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;root_super</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;edge_port</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;bpdufilter_default</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;bpduguard_default</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;mode</samp> | String |  |  | Valid Values:<br>- mstp<br>- rstp<br>- rapid-pvst<br>- none |  |
    | <samp>&nbsp;&nbsp;bpduguard_rate_limit</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;count</samp> | Integer |  |  |  | Maximum number of BPDUs per timer interval |
    | <samp>&nbsp;&nbsp;rstp_priority</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;mst</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;pvst_border</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;configuration</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;revision</samp> | Integer |  |  |  | 0-65535 |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;instances</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp> | Integer | Required, Unique |  |  | Instance ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp> | String |  |  |  | "< vlan_id >, < vlan_id >-< vlan_id >"<br>Example: 15,16,17,18<br> |
    | <samp>&nbsp;&nbsp;mst_instances</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp> | String | Required, Unique |  |  | Instance ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;no_spanning_tree_vlan</samp> | String |  |  |  | "< vlan_id >, < vlan_id >-< vlan_id >"<br>Example: 105,202,505-506<br> |
    | <samp>&nbsp;&nbsp;rapid_pvst_instances</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp> | String | Required, Unique |  |  | "< vlan_id >, < vlan_id >-< vlan_id >"<br>Example: 105,202,505-506<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp> | Integer |  |  |  |  |

=== "YAML"

    ```yaml
    spanning_tree:
      root_super: <bool>
      edge_port:
        bpdufilter_default: <bool>
        bpduguard_default: <bool>
      mode: <str>
      bpduguard_rate_limit:
        default: <bool>
        count: <int>
      rstp_priority: <int>
      mst:
        pvst_border: <bool>
        configuration:
          name: <str>
          revision: <int>
          instances:
            - id: <int>
              vlans: <str>
      mst_instances:
        - id: <str>
          priority: <int>
      no_spanning_tree_vlan: <str>
      rapid_pvst_instances:
        - id: <str>
          priority: <int>
    ```
