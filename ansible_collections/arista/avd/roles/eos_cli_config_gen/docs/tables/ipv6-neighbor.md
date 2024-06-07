<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ipv6_neighbor</samp>](## "ipv6_neighbor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;static_entries</samp>](## "ipv6_neighbor.static_entries") | List, items: Dictionary |  |  |  | Static IPv6 neighbor entries. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ipv6_address</samp>](## "ipv6_neighbor.static_entries.[].ipv6_address") | String | Required |  |  | IPv6 address of neighbor. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ipv6_neighbor.static_entries.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "ipv6_neighbor.static_entries.[].interface") | String | Required |  |  | Interface name.<br>Example - Ethernet4<br>          Loopback4-6<br>          Port-channel4,7<br>          Management 1<br>          Tunnel10<br>          Vlan101,102 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "ipv6_neighbor.static_entries.[].mac_address") | String | Required |  | Pattern: ^(?:[0-9A-Fa-f]{1,4}\.){2}[0-9A-Fa-f]{1,4}$ | Hardware address of neighbor.<br>Example - aaaf.1234.bcbf |
    | [<samp>&nbsp;&nbsp;cache</samp>](## "ipv6_neighbor.cache") | Boolean |  |  |  | Manage the IPv6 neighbor cache. |
    | [<samp>&nbsp;&nbsp;persistent</samp>](## "ipv6_neighbor.persistent") | Boolean |  |  |  | Restore the IPv6 neighbor cache after reboot. |
    | [<samp>&nbsp;&nbsp;refresh_delay</samp>](## "ipv6_neighbor.refresh_delay") | Integer |  | `600` | Min: 600<br>Max: 3600 | Time to wait in seconds before refresh. |

=== "YAML"

    ```yaml
    ipv6_neighbor:

      # Static IPv6 neighbor entries.
      static_entries:

          # IPv6 address of neighbor.
        - ipv6_address: <str; required>
          vrf: <str>

          # Interface name.
          # Example - Ethernet4
          #           Loopback4-6
          #           Port-channel4,7
          #           Management 1
          #           Tunnel10
          #           Vlan101,102
          interface: <str; required>

          # Hardware address of neighbor.
          # Example - aaaf.1234.bcbf
          mac_address: <str; required>

      # Manage the IPv6 neighbor cache.
      cache: <bool>

      # Restore the IPv6 neighbor cache after reboot.
      persistent: <bool>

      # Time to wait in seconds before refresh.
      refresh_delay: <int; 600-3600; default=600>
    ```
