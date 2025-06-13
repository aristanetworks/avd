<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_interfaces</samp>](## "management_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "management_interfaces.[].name") | String | Required, Unique |  |  | Management Interface Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "management_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "management_interfaces.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "management_interfaces.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "management_interfaces.[].mtu") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_interfaces.[].vrf") | String |  |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "management_interfaces.[].ip_address") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "management_interfaces.[].ipv6_enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "management_interfaces.[].ipv6_address") | String |  |  |  | IPv6_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "management_interfaces.[].type") | String |  | `oob` | Valid Values:<br>- <code>oob</code><br>- <code>inband</code> | For documentation purposes only. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "management_interfaces.[].gateway") | String |  |  |  | IPv4 address of default gateway in management VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_gateway</samp>](## "management_interfaces.[].ipv6_gateway") | String |  |  |  | IPv6 address of default gateway in management VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "management_interfaces.[].mac_address") | String |  |  |  | MAC address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lldp</samp>](## "management_interfaces.[].lldp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transmit</samp>](## "management_interfaces.[].lldp.transmit") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "management_interfaces.[].lldp.receive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ztp_vlan</samp>](## "management_interfaces.[].lldp.ztp_vlan") | Integer |  |  |  | ZTP vlan number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;redundancy</samp>](## "management_interfaces.[].redundancy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fallback_delay</samp>](## "management_interfaces.[].redundancy.fallback_delay") | String |  |  |  | The duration to wait before falling back to the higher-priority interface.<br>Accepts a value between 0 and 3600 seconds, or the string `infinity` to disable fallback. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor</samp>](## "management_interfaces.[].redundancy.monitor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_state</samp>](## "management_interfaces.[].redundancy.monitor.link_state") | Boolean |  |  |  | Link state of interface.<br>`neighbor` and `link_state` are mutually exclusive and `link_state` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbor</samp>](## "management_interfaces.[].redundancy.monitor.neighbor") | Dictionary |  |  |  | To configure an IPv6 neighbor as monitor, `fallback_delay` must be set as infinity.<br>`neighbor` and `link_state` are mutually exclusive and `link_state` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "management_interfaces.[].redundancy.monitor.neighbor.ipv6_address") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "management_interfaces.[].redundancy.monitor.neighbor.interval") | Integer |  |  | Min: 1<br>Max: 300000 | Interval between neighbor probes in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "management_interfaces.[].redundancy.monitor.neighbor.multiplier") | Integer |  |  | Min: 1<br>Max: 100 | Number of missed neighbor replies after which it is timed out. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;supervisor_1</samp>](## "management_interfaces.[].redundancy.supervisor_1") | Dictionary |  |  |  | Configuration for supervisor 1, including its primary and backup management interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary_management_interface</samp>](## "management_interfaces.[].redundancy.supervisor_1.primary_management_interface") | String | Required |  |  | Primary management interface name like 'Management1/1'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;backup_management_interfaces</samp>](## "management_interfaces.[].redundancy.supervisor_1.backup_management_interfaces") | List, items: String | Required |  | Min Length: 1 | Backup management interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_interfaces.[].redundancy.supervisor_1.backup_management_interfaces.[]") | String |  |  |  | Management interface name like 'Management2/1'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;supervisor_2</samp>](## "management_interfaces.[].redundancy.supervisor_2") | Dictionary |  |  |  | Configuration for supervisor 2, including its primary and backup management interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary_management_interface</samp>](## "management_interfaces.[].redundancy.supervisor_2.primary_management_interface") | String | Required |  |  | Primary management interface name like 'Management1/1'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;backup_management_interfaces</samp>](## "management_interfaces.[].redundancy.supervisor_2.backup_management_interfaces") | List, items: String | Required |  | Min Length: 1 | Backup management interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_interfaces.[].redundancy.supervisor_2.backup_management_interfaces.[]") | String |  |  |  | Management interface name like 'Management2/1'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "management_interfaces.[].eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the management interface in the final EOS configuration. |

=== "YAML"

    ```yaml
    management_interfaces:

        # Management Interface Name.
      - name: <str; required; unique>
        description: <str>
        shutdown: <bool>

        # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
        speed: <str>
        mtu: <int>

        # VRF Name.
        vrf: <str>

        # IPv4_address/Mask.
        ip_address: <str>
        ipv6_enable: <bool>

        # IPv6_address/Mask.
        ipv6_address: <str>

        # For documentation purposes only.
        type: <str; "oob" | "inband"; default="oob">

        # IPv4 address of default gateway in management VRF.
        gateway: <str>

        # IPv6 address of default gateway in management VRF.
        ipv6_gateway: <str>

        # MAC address.
        mac_address: <str>
        lldp:
          transmit: <bool>
          receive: <bool>

          # ZTP vlan number.
          ztp_vlan: <int>
        redundancy:

          # The duration to wait before falling back to the higher-priority interface.
          # Accepts a value between 0 and 3600 seconds, or the string `infinity` to disable fallback.
          fallback_delay: <str>
          monitor:

            # Link state of interface.
            # `neighbor` and `link_state` are mutually exclusive and `link_state` takes precedence.
            link_state: <bool>

            # To configure an IPv6 neighbor as monitor, `fallback_delay` must be set as infinity.
            # `neighbor` and `link_state` are mutually exclusive and `link_state` takes precedence.
            neighbor:
              ipv6_address: <str; required>

              # Interval between neighbor probes in milliseconds.
              interval: <int; 1-300000>

              # Number of missed neighbor replies after which it is timed out.
              multiplier: <int; 1-100>

          # Configuration for supervisor 1, including its primary and backup management interfaces.
          supervisor_1:

            # Primary management interface name like 'Management1/1'.
            primary_management_interface: <str; required>

            # Backup management interfaces.
            backup_management_interfaces: # >=1 items; required

                # Management interface name like 'Management2/1'.
              - <str>

          # Configuration for supervisor 2, including its primary and backup management interfaces.
          supervisor_2:

            # Primary management interface name like 'Management1/1'.
            primary_management_interface: <str; required>

            # Backup management interfaces.
            backup_management_interfaces: # >=1 items; required

                # Management interface name like 'Management2/1'.
              - <str>

        # Multiline EOS CLI rendered directly on the management interface in the final EOS configuration.
        eos_cli: <str>
    ```
