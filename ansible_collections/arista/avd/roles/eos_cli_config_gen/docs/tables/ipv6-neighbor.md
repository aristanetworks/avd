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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "ipv6_neighbor.static_entries.[].interface") | String | Required |  |  | Interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "ipv6_neighbor.static_entries.[].mac_address") | String | Required |  | Pattern: ^([0-9a-f]{2}:){5}[0-9a-f]{2}$ | MAC address of neighbor like 'aa:af:12:34:bc:bf' |
    | [<samp>&nbsp;&nbsp;cache_persistent</samp>](## "ipv6_neighbor.cache_persistent") | Boolean |  |  |  | Restore the IPv6 neighbor cache after reboot. |
    | [<samp>&nbsp;&nbsp;persistent</samp>](## "ipv6_neighbor.persistent") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ipv6_neighbor.persistent.enabled") | Boolean | Required |  |  | Restore the IPv6 neighbor cache after reboot with default refresh delay. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;refresh_delay</samp>](## "ipv6_neighbor.persistent.refresh_delay") | Integer |  | `600` | Min: 600<br>Max: 3600 | Time to wait in seconds before refreshing the IPv6 neighbor cache after reboot.<br>It wil require to set the value of `enabled` key as true.<br> |

=== "YAML"

    ```yaml
    ipv6_neighbor:

      # Static IPv6 neighbor entries.
      static_entries:

          # IPv6 address of neighbor.
        - ipv6_address: <str; required>
          vrf: <str>

          # Interface name.
          interface: <str; required>

          # MAC address of neighbor like 'aa:af:12:34:bc:bf'
          mac_address: <str; required>

      # Restore the IPv6 neighbor cache after reboot.
      cache_persistent: <bool>
      persistent:

        # Restore the IPv6 neighbor cache after reboot with default refresh delay.
        enabled: <bool; required>

        # Time to wait in seconds before refreshing the IPv6 neighbor cache after reboot.
        # It wil require to set the value of `enabled` key as true.
        refresh_delay: <int; 600-3600; default=600>
    ```
