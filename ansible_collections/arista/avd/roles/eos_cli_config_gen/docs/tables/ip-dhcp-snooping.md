<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_dhcp_snooping</samp>](## "ip_dhcp_snooping") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "ip_dhcp_snooping.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;bridging</samp>](## "ip_dhcp_snooping.bridging") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;information_option</samp>](## "ip_dhcp_snooping.information_option") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ip_dhcp_snooping.information_option.enabled") | Boolean |  |  |  | Enable insertion of option-82 in DHCP request packets |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;circuit_id_type</samp>](## "ip_dhcp_snooping.information_option.circuit_id_type") | String |  |  |  | "none" or <0 - 255> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;circuit_id_type_format</samp>](## "ip_dhcp_snooping.information_option.circuit_id_type_format") | String |  |  | Valid Values:<br>- %h:%p<br>- %p:%v | - "%h:%p" Hostname and interface name or<br>- "%p:%v" Interface name and VLAN ID |
    | [<samp>&nbsp;&nbsp;vlan</samp>](## "ip_dhcp_snooping.vlan") | String |  |  |  | VLAN range as string.<br>"< vlan_id >, < vlan_id >-< vlan_id >"<br>Example: 15,16,17,18 |

=== "YAML"

    ```yaml
    ip_dhcp_snooping:
      enabled: <bool>
      bridging: <bool>
      information_option:
        enabled: <bool>
        circuit_id_type: <str>
        circuit_id_type_format: <str>
      vlan: <str>
    ```
