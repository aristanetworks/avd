<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>address_locking_settings</samp>](## "address_locking_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;local_interface</samp>](## "address_locking_settings.local_interface") | String |  | `use_default_mgmt_method_interface` |  | The value will be interpreted according to these rules:<br>  - `use_mgmt_interface` will configure the `mgmt_interface` as the local interface.<br>  - `use_inband_mgmt_interface` will configure the `inband_mgmt_interface` as the local interface.<br>  - `use_default_mgmt_method_interface` will configure `mgmt_interface` or `inband_mgmt_interface` as the local interface depending on the value of `default_mgmt_method`.<br>  - Any other string will be used directly as the local interface. |
    | [<samp>&nbsp;&nbsp;dhcp_servers_ipv4</samp>](## "address_locking_settings.dhcp_servers_ipv4") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "address_locking_settings.dhcp_servers_ipv4.[]") | String |  |  |  | DHCP server IPv4 address. |
    | [<samp>&nbsp;&nbsp;dhcp_server_interfaces</samp>](## "address_locking_settings.dhcp_server_interfaces") | List, items: String |  |  |  | The list of interfaces connected to the DHCP server.<br>Requires EOS version 4.36 or later. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "address_locking_settings.dhcp_server_interfaces.[]") | String |  |  |  | Interface name. |
    | [<samp>&nbsp;&nbsp;disabled</samp>](## "address_locking_settings.disabled") | Boolean |  |  |  | Disable IP locking on configured ports. |
    | [<samp>&nbsp;&nbsp;leases</samp>](## "address_locking_settings.leases") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip</samp>](## "address_locking_settings.leases.[].ip") | String | Required |  |  | IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac</samp>](## "address_locking_settings.leases.[].mac") | String | Required |  |  | MAC address (hhhh.hhhh.hhhh or hh:hh:hh:hh:hh:hh). |
    | [<samp>&nbsp;&nbsp;locked_address</samp>](## "address_locking_settings.locked_address") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;expiration_mac_disabled</samp>](## "address_locking_settings.locked_address.expiration_mac_disabled") | Boolean |  |  |  | Configure deauthorizing locked addresses upon MAC aging out. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_enforcement_disabled</samp>](## "address_locking_settings.locked_address.ipv4_enforcement_disabled") | Boolean |  |  |  | Configure enforcement for locked IPv4 addresses. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enforcement_disabled</samp>](## "address_locking_settings.locked_address.ipv6_enforcement_disabled") | Boolean |  |  |  | Configure enforcement for locked IPv6 addresses. |

=== "YAML"

    ```yaml
    address_locking_settings:

      # The value will be interpreted according to these rules:
      #   - `use_mgmt_interface` will configure the `mgmt_interface` as the local interface.
      #   - `use_inband_mgmt_interface` will configure the `inband_mgmt_interface` as the local interface.
      #   - `use_default_mgmt_method_interface` will configure `mgmt_interface` or `inband_mgmt_interface` as the local interface depending on the value of `default_mgmt_method`.
      #   - Any other string will be used directly as the local interface.
      local_interface: <str; default="use_default_mgmt_method_interface">
      dhcp_servers_ipv4:

          # DHCP server IPv4 address.
        - <str>

      # The list of interfaces connected to the DHCP server.
      # Requires EOS version 4.36 or later.
      dhcp_server_interfaces:

          # Interface name.
        - <str>

      # Disable IP locking on configured ports.
      disabled: <bool>
      leases:

          # IP address.
        - ip: <str; required>

          # MAC address (hhhh.hhhh.hhhh or hh:hh:hh:hh:hh:hh).
          mac: <str; required>
      locked_address:

        # Configure deauthorizing locked addresses upon MAC aging out.
        expiration_mac_disabled: <bool>

        # Configure enforcement for locked IPv4 addresses.
        ipv4_enforcement_disabled: <bool>

        # Configure enforcement for locked IPv6 addresses.
        ipv6_enforcement_disabled: <bool>
    ```
