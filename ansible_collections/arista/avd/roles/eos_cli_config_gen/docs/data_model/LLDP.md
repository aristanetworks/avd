---
search:
  boost: 2
---

# LLDP
## LLDP



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>lldp</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;timer</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;timer_reinitialization</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;holdtime</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;management_address</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;vrf</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;receive_packet_tagged_drop</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;tlvs</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  | Valid Values:<br>- link-aggregation<br>- management-address<br>- max-frame-size<br>- med<br>- port-description<br>- port-vlan<br>- power-via-mdi<br>- system-capabilities<br>- system-description<br>- system-name<br>- vlan-name |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transmit</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;run</samp> | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    lldp:
      timer: <int>
      timer_reinitialization: <str>
      holdtime: <int>
      management_address: <str>
      vrf: <str>
      receive_packet_tagged_drop: <str>
      tlvs:
        - name: <str>
          transmit: <bool>
      run: <bool>
    ```
