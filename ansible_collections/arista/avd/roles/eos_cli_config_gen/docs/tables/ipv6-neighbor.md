<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ipv6_neighbor</samp>](## "ipv6_neighbor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;static_entries</samp>](## "ipv6_neighbor.static_entries") | List, items: Dictionary |  |  |  | Static IPv6 neighbors entries. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ipv6_address</samp>](## "ipv6_neighbor.static_entries.[].ipv6_address") | String | Required |  |  | IPv6 address of neighbor. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ipv6_neighbor.static_entries.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "ipv6_neighbor.static_entries.[].interface") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "ipv6_neighbor.static_entries.[].mac_address") | String | Required |  | Pattern: ^(?:[0-9A-Fa-f]{1,4}\.){2}[0-9A-Fa-f]{1,4}$ | Hardware address of neighbor. |
    | [<samp>&nbsp;&nbsp;cache</samp>](## "ipv6_neighbor.cache") | Boolean |  |  |  | Manage the IPv6 neighbor cache. |
    | [<samp>&nbsp;&nbsp;persistent</samp>](## "ipv6_neighbor.persistent") | Boolean |  |  |  | Restore the IPv6 neighbor cache after reboot. |
    | [<samp>&nbsp;&nbsp;refresh_delay</samp>](## "ipv6_neighbor.refresh_delay") | Integer |  | `600` | Min: 600<br>Max: 3600 | Time to wait in seconds before refresh. |

=== "YAML"

    ```yaml
    ipv6_neighbor:

      # Static IPv6 neighbors entries.
      static_entries:

          # IPv6 address of neighbor.
        - ipv6_address: <str; required>
          vrf: <str>
          interface: <str; required>

          # Hardware address of neighbor.
          mac_address: <str; required>

      # Manage the IPv6 neighbor cache.
      cache: <bool>

      # Restore the IPv6 neighbor cache after reboot.
      persistent: <bool>

      # Time to wait in seconds before refresh.
      refresh_delay: <int; 600-3600; default=600>
    ```
