---
search:
  boost: 2
---

# System Control-Plane
## System



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>system</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;control_plane</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;tcp_mss</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp> | Integer |  |  |  | Segment size |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp> | Integer |  |  |  | Segment size |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_access_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- acl_name</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- acl_name</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  |  |

=== "YAML"

    ```yaml
    system:
      control_plane:
        tcp_mss:
          ipv4: <int>
          ipv6: <int>
        ipv4_access_groups:
          - acl_name: <str>
            vrf: <str>
        ipv6_access_groups:
          - acl_name: <str>
            vrf: <str>
    ```
## VMTracer Sessions



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>vmtracer_sessions</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Vmtracer Session Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;url</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;username</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp> | String |  |  |  | Type 7 Password Hash |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;autovlan_disable</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp> | String |  |  |  |  |

=== "YAML"

    ```yaml
    vmtracer_sessions:
      - name: <str>
        url: <str>
        username: <str>
        password: <str>
        autovlan_disable: <bool>
        source_interface: <str>
    ```
