---
search:
  boost: 2
---

# Hardware
## Hardware



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>hardware</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;access_list</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;mechanism</samp> | String |  |  | Valid Values:<br>- algomatch<br>- none<br>- tcam |  |
    | <samp>&nbsp;&nbsp;speed_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- speed_group</samp> | Integer | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serdes</samp> | String |  |  |  | Serdes speed like "10g" or "25g" |

=== "YAML"

    ```yaml
    hardware:
      access_list:
        mechanism: <str>
      speed_groups:
        - speed_group: <int>
          serdes: <str>
    ```
## Hardware Counters



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>hardware_counters</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;features</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp> | String | Required |  | Valid Values:<br>- in<br>- out |  |

=== "YAML"

    ```yaml
    hardware_counters:
      features:
        - name: <str>
          direction: <str>
    ```
## Platform



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>platform</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;trident</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;forwarding_table_partition</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;sand</samp> | Dictionary |  |  |  | Most of the platform sand options are hardware dependant and optional |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;qos_maps</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- traffic_class</samp> | Integer |  |  | Min: 0<br>Max: 7 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to_network_qos</samp> | Integer |  |  | Min: 0<br>Max: 63 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;lag</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_only</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;forwarding_mode</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;multicast_replication</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp> | String |  |  | Valid Values:<br>- ingress<br>- egress |  |

=== "YAML"

    ```yaml
    platform:
      trident:
        forwarding_table_partition: <str>
      sand:
        qos_maps:
          - traffic_class: <int>
            to_network_qos: <int>
        lag:
          hardware_only: <bool>
          mode: <str>
        forwarding_mode: <str>
        multicast_replication:
          default: <str>
    ```
## Redundancy



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>redundancy</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;protocol</samp> | String |  |  |  | Redundancy Protocol |

=== "YAML"

    ```yaml
    redundancy:
      protocol: <str>
    ```
## Hardware TCAM Profiles



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>tcam_profile</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;system</samp> | String |  |  |  | TCAM profile name to activate<br> |
    | <samp>&nbsp;&nbsp;profiles</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Tcam-Profile Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;config</samp> | String | Required |  |  | TCAM Profile Config. Since these can be very long, it is often a good idea to import the config from a file.<br>Example: "{{lookup('file', '{{ root_dir }}/inventory/TCAM_TRAFFIC_POLICY.conf')}}" |

=== "YAML"

    ```yaml
    tcam_profile:
      system: <str>
      profiles:
        - name: <str>
          config: <str>
    ```
