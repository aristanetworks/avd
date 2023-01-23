---
search:
  boost: 2
---

# Maintenance Mode
## BGP Groups



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>bgp_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Group Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_maintenance_profiles</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Profile Name |

=== "YAML"

    ```yaml
    bgp_groups:
      - name: <str>
        vrf: <str>
        neighbors:
          - <str>
        bgp_maintenance_profiles:
          - <str>
    ```
## Maintenance Interface Groups



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>interface_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Interface-Group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Interface Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_maintenance_profiles</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Name of BGP Maintenance Profile |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_maintenance_profiles</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Name of Interface Maintenance Profile |

=== "YAML"

    ```yaml
    interface_groups:
      - name: <str>
        interfaces:
          - <str>
        bgp_maintenance_profiles:
          - <str>
        interface_maintenance_profiles:
          - <str>
    ```
## Maintenance Mode



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>maintenance</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;default_interface_profile</samp> | String |  |  |  | Name of default Interface Profile<br> |
    | <samp>&nbsp;&nbsp;default_bgp_profile</samp> | String |  |  |  | Name of default BGP Profile<br> |
    | <samp>&nbsp;&nbsp;default_unit_profile</samp> | String |  |  |  | Name of default Unit Profile<br> |
    | <samp>&nbsp;&nbsp;interface_profiles</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_monitoring</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;load_interval</samp> | Integer |  |  |  | Load Interval in Seconds<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp> | Integer |  |  |  | Threshold in kbps<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_delay</samp> | Integer |  |  |  | Max delay in seconds<br> |
    | <samp>&nbsp;&nbsp;bgp_profiles</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | BGP Profile Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;initiator</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_inout</samp> | String |  |  |  | Route Map |
    | <samp>&nbsp;&nbsp;unit_profiles</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Unit Profile Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_boot</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;duration</samp> | Integer |  |  | Min: 300<br>Max: 3600 | On-boot in seconds<br> |
    | <samp>&nbsp;&nbsp;units</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Unit Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quiesce</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp> | String | Required |  |  | Name of Unit Profile<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_groups</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Name of BGP Group<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface_groups</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Name of Interface Group |

=== "YAML"

    ```yaml
    maintenance:
      default_interface_profile: <str>
      default_bgp_profile: <str>
      default_unit_profile: <str>
      interface_profiles:
        - name: <str>
          rate_monitoring:
            load_interval: <int>
            threshold: <int>
          shutdown:
            max_delay: <int>
      bgp_profiles:
        - name: <str>
          initiator:
            route_map_inout: <str>
      unit_profiles:
        - name: <str>
          on_boot:
            duration: <int>
      units:
        - name: <str>
          quiesce: <bool>
          profile: <str>
          groups:
            bgp_groups:
              - <str>
            interface_groups:
              - <str>
    ```
