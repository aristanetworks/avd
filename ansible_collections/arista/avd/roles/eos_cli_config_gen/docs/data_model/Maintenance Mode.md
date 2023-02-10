---
search:
  boost: 2
---

# Maintenance Mode

## BGP Groups

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_groups</samp>](## "bgp_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "bgp_groups.[].name") | String | Required, Unique |  |  | Group Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "bgp_groups.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "bgp_groups.[].neighbors") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "bgp_groups.[].neighbors.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_maintenance_profiles</samp>](## "bgp_groups.[].bgp_maintenance_profiles") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "bgp_groups.[].bgp_maintenance_profiles.[].&lt;str&gt;") | String |  |  |  | Profile Name |

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
    | [<samp>interface_groups</samp>](## "interface_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "interface_groups.[].name") | String | Required, Unique |  |  | Interface-Group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "interface_groups.[].interfaces") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "interface_groups.[].interfaces.[].&lt;str&gt;") | String |  |  |  | Interface Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_maintenance_profiles</samp>](## "interface_groups.[].bgp_maintenance_profiles") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "interface_groups.[].bgp_maintenance_profiles.[].&lt;str&gt;") | String |  |  |  | Name of BGP Maintenance Profile |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_maintenance_profiles</samp>](## "interface_groups.[].interface_maintenance_profiles") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "interface_groups.[].interface_maintenance_profiles.[].&lt;str&gt;") | String |  |  |  | Name of Interface Maintenance Profile |

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
    | [<samp>maintenance</samp>](## "maintenance") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;default_interface_profile</samp>](## "maintenance.default_interface_profile") | String |  |  |  | Name of default Interface Profile<br> |
    | [<samp>&nbsp;&nbsp;default_bgp_profile</samp>](## "maintenance.default_bgp_profile") | String |  |  |  | Name of default BGP Profile<br> |
    | [<samp>&nbsp;&nbsp;default_unit_profile</samp>](## "maintenance.default_unit_profile") | String |  |  |  | Name of default Unit Profile<br> |
    | [<samp>&nbsp;&nbsp;interface_profiles</samp>](## "maintenance.interface_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "maintenance.interface_profiles.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_monitoring</samp>](## "maintenance.interface_profiles.[].rate_monitoring") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;load_interval</samp>](## "maintenance.interface_profiles.[].rate_monitoring.load_interval") | Integer |  |  |  | Load Interval in Seconds<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "maintenance.interface_profiles.[].rate_monitoring.threshold") | Integer |  |  |  | Threshold in kbps<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "maintenance.interface_profiles.[].shutdown") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_delay</samp>](## "maintenance.interface_profiles.[].shutdown.max_delay") | Integer |  |  |  | Max delay in seconds<br> |
    | [<samp>&nbsp;&nbsp;bgp_profiles</samp>](## "maintenance.bgp_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "maintenance.bgp_profiles.[].name") | String | Required, Unique |  |  | BGP Profile Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;initiator</samp>](## "maintenance.bgp_profiles.[].initiator") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_inout</samp>](## "maintenance.bgp_profiles.[].initiator.route_map_inout") | String |  |  |  | Route Map |
    | [<samp>&nbsp;&nbsp;unit_profiles</samp>](## "maintenance.unit_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "maintenance.unit_profiles.[].name") | String | Required, Unique |  |  | Unit Profile Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_boot</samp>](## "maintenance.unit_profiles.[].on_boot") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;duration</samp>](## "maintenance.unit_profiles.[].on_boot.duration") | Integer |  |  | Min: 300<br>Max: 3600 | On-boot in seconds<br> |
    | [<samp>&nbsp;&nbsp;units</samp>](## "maintenance.units") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "maintenance.units.[].name") | String | Required, Unique |  |  | Unit Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quiesce</samp>](## "maintenance.units.[].quiesce") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "maintenance.units.[].profile") | String |  |  |  | Name of Unit Profile<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "maintenance.units.[].groups") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_groups</samp>](## "maintenance.units.[].groups.bgp_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "maintenance.units.[].groups.bgp_groups.[].&lt;str&gt;") | String |  |  |  | Name of BGP Group<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface_groups</samp>](## "maintenance.units.[].groups.interface_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "maintenance.units.[].groups.interface_groups.[].&lt;str&gt;") | String |  |  |  | Name of Interface Group |

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
