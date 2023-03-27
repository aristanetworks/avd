---
search:
  boost: 2
---

# Hardware

## Hardware

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>hardware</samp>](## "hardware") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;access_list</samp>](## "hardware.access_list") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mechanism</samp>](## "hardware.access_list.mechanism") | String |  |  | Valid Values:<br>- algomatch<br>- none<br>- tcam |  |
    | [<samp>&nbsp;&nbsp;speed_groups</samp>](## "hardware.speed_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- speed_group</samp>](## "hardware.speed_groups.[].speed_group") | Integer | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serdes</samp>](## "hardware.speed_groups.[].serdes") | String |  |  |  | Serdes speed like "10g" or "25g" |

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
    | [<samp>hardware_counters</samp>](## "hardware_counters") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;features</samp>](## "hardware_counters.features") | List, items: Dictionary |  |  |  |  |

=== "YAML"

    ```yaml
    hardware_counters:
      features:
    ```

## Platform

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>platform</samp>](## "platform") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;trident</samp>](## "platform.trident") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;forwarding_table_partition</samp>](## "platform.trident.forwarding_table_partition") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;sand</samp>](## "platform.sand") | Dictionary |  |  |  | Most of the platform sand options are hardware dependant and optional |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;qos_maps</samp>](## "platform.sand.qos_maps") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- traffic_class</samp>](## "platform.sand.qos_maps.[].traffic_class") | Integer |  |  | Min: 0<br>Max: 7 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to_network_qos</samp>](## "platform.sand.qos_maps.[].to_network_qos") | Integer |  |  | Min: 0<br>Max: 63 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lag</samp>](## "platform.sand.lag") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_only</samp>](## "platform.sand.lag.hardware_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "platform.sand.lag.mode") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;forwarding_mode</samp>](## "platform.sand.forwarding_mode") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;multicast_replication</samp>](## "platform.sand.multicast_replication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "platform.sand.multicast_replication.default") | String |  |  | Valid Values:<br>- ingress<br>- egress |  |

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
    | [<samp>redundancy</samp>](## "redundancy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;protocol</samp>](## "redundancy.protocol") | String |  |  |  | Redundancy Protocol |

=== "YAML"

    ```yaml
    redundancy:
      protocol: <str>
    ```

## Hardware TCAM Profiles

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>tcam_profile</samp>](## "tcam_profile") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;system</samp>](## "tcam_profile.system") | String |  |  |  | TCAM profile name to activate<br> |
    | [<samp>&nbsp;&nbsp;profiles</samp>](## "tcam_profile.profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "tcam_profile.profiles.[].name") | String | Required, Unique |  |  | Tcam-Profile Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;config</samp>](## "tcam_profile.profiles.[].config") | String | Required |  |  | TCAM Profile Config. Since these can be very long, it is often a good idea to import the config from a file.<br>Example: "{{ lookup('file', 'TCAM_TRAFFIC_POLICY.conf') }}" |

=== "YAML"

    ```yaml
    tcam_profile:
      system: <str>
      profiles:
        - name: <str>
          config: <str>
    ```
