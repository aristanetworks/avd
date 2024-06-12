<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>arp</samp>](## "arp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;cache_persistent</samp>](## "arp.cache_persistent") | Boolean |  |  |  | Restore the ARP cache after reboot |
    | [<samp>&nbsp;&nbsp;persistent_refresh_delay</samp>](## "arp.persistent_refresh_delay") | Integer |  | `600` | Min: 600<br>Max: 3600 | Time to wait in seconds before refreshing the ARP cache after reboot. |
    | [<samp>&nbsp;&nbsp;aging</samp>](## "arp.aging") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;timeout_default</samp>](## "arp.aging.timeout_default") | Integer |  |  | Min: 60<br>Max: 65535 | Timeout in seconds. |
    | [<samp>&nbsp;&nbsp;static_entries</samp>](## "arp.static_entries") | List, items: Dictionary |  |  |  | Static ARP entries. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ipv4_address</samp>](## "arp.static_entries.[].ipv4_address") | String | Required |  |  | ARP entry IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "arp.static_entries.[].vrf") | String |  |  |  | ARP entry VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "arp.static_entries.[].mac_address") | String | Required |  | Pattern: ^[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}$ | ARP entry MAC address. |

=== "YAML"

    ```yaml
    arp:

      # Restore the ARP cache after reboot
      cache_persistent: <bool>

      # Time to wait in seconds before refreshing the ARP cache after reboot.
      persistent_refresh_delay: <int; 600-3600; default=600>
      aging:

        # Timeout in seconds.
        timeout_default: <int; 60-65535>

      # Static ARP entries.
      static_entries:

          # ARP entry IPv4 address.
        - ipv4_address: <str; required>

          # ARP entry VRF.
          vrf: <str>

          # ARP entry MAC address.
          mac_address: <str; required>
    ```
