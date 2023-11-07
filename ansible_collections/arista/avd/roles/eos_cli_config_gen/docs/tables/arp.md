<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>arp</samp>](## "arp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;aging</samp>](## "arp.aging") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;timeout_default</samp>](## "arp.aging.timeout_default") | Integer |  |  | Min: 60<br>Max: 65535 | Timeout in seconds |
    | [<samp>&nbsp;&nbsp;static_entries</samp>](## "arp.static_entries") | List, items: Dictionary |  |  |  | Static ARP entries. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- ipv4_address</samp>](## "arp.static_entries.[].ipv4_address") | String | Required |  |  | ARP entry IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "arp.static_entries.[].vrf") | String |  |  |  | ARP entry VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "arp.static_entries.[].mac_address") | String | Required |  | Pattern: ^[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}$ | ARP entry MAC address. |

=== "YAML"

    ```yaml
    arp:
      aging:
        timeout_default: <int>
      static_entries:
        - ipv4_address: <str>
          vrf: <str>
          mac_address: <str>
    ```
