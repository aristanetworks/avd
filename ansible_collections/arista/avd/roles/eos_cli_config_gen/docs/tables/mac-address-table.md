<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mac_address_table</samp>](## "mac_address_table") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;aging_time</samp>](## "mac_address_table.aging_time") | Integer |  |  | Min: 0<br>Max: 1000000 | Aging time in seconds 10-1000000.<br>Enter 0 to disable aging.<br> |
    | [<samp>&nbsp;&nbsp;notification_host_flap</samp>](## "mac_address_table.notification_host_flap") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "mac_address_table.notification_host_flap.logging") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "mac_address_table.notification_host_flap.detection") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;window</samp>](## "mac_address_table.notification_host_flap.detection.window") | Integer |  |  | Min: 2<br>Max: 300 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;moves</samp>](## "mac_address_table.notification_host_flap.detection.moves") | Integer |  |  | Min: 2<br>Max: 10 |  |
    | [<samp>&nbsp;&nbsp;static_entries</samp>](## "mac_address_table.static_entries") | List, items: Dictionary |  |  |  | Add static MAC address entries. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;mac_address</samp>](## "mac_address_table.static_entries.[].mac_address") | String | Required |  | Pattern: `^[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}$` | The static MAC address to configure.<br>The combination of 'mac_address' and 'vlan' must be unique across all static entries. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "mac_address_table.static_entries.[].vlan") | Integer | Required |  |  | The VLAN ID associated with the MAC address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "mac_address_table.static_entries.[].drop") | Boolean |  |  |  | If true, traffic destined for this MAC address on the specified VLAN will be dropped.<br>This option is mutually exclusive with 'interface' and takes precedence if both are defined. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "mac_address_table.static_entries.[].interface") | String |  |  |  | The allowed hardware Ethernet interface, LAG interface, or VXLAN tunnel interface associated with this MAC address and VLAN.<br>This option is mutually exclusive with 'drop'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eligibility_forwarding</samp>](## "mac_address_table.static_entries.[].eligibility_forwarding") | Boolean |  |  |  | Enable the ability to forward traffic on the specified interface and VLAN for this MAC address.<br>This option is only applicable when 'interface' is defined. |

=== "YAML"

    ```yaml
    mac_address_table:

      # Aging time in seconds 10-1000000.
      # Enter 0 to disable aging.
      aging_time: <int; 0-1000000>
      notification_host_flap:
        logging: <bool>
        detection:
          window: <int; 2-300>
          moves: <int; 2-10>

      # Add static MAC address entries.
      static_entries:

          # The static MAC address to configure.
          # The combination of 'mac_address' and 'vlan' must be unique across all static entries.
        - mac_address: <str; required>

          # The VLAN ID associated with the MAC address.
          vlan: <int; required>

          # If true, traffic destined for this MAC address on the specified VLAN will be dropped.
          # This option is mutually exclusive with 'interface' and takes precedence if both are defined.
          drop: <bool>

          # The allowed hardware Ethernet interface, LAG interface, or VXLAN tunnel interface associated with this MAC address and VLAN.
          # This option is mutually exclusive with 'drop'.
          interface: <str>

          # Enable the ability to forward traffic on the specified interface and VLAN for this MAC address.
          # This option is only applicable when 'interface' is defined.
          eligibility_forwarding: <bool>
    ```
