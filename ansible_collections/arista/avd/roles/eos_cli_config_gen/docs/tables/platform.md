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
