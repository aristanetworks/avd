<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>lldp</samp>](## "lldp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;timer</samp>](## "lldp.timer") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;timer_reinitialization</samp>](## "lldp.timer_reinitialization") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;holdtime</samp>](## "lldp.holdtime") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;management_address</samp>](## "lldp.management_address") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;vrf</samp>](## "lldp.vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;receive_packet_tagged_drop</samp>](## "lldp.receive_packet_tagged_drop") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;tlvs</samp>](## "lldp.tlvs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "lldp.tlvs.[].name") | String | Required, Unique |  | Valid Values:<br>- link-aggregation<br>- management-address<br>- max-frame-size<br>- med<br>- port-description<br>- port-vlan<br>- power-via-mdi<br>- system-capabilities<br>- system-description<br>- system-name<br>- vlan-name |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transmit</samp>](## "lldp.tlvs.[].transmit") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;run</samp>](## "lldp.run") | Boolean |  |  |  |  |

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
