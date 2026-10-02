<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>address_locking_settings</samp>](## "address_locking_settings") | Dictionary |  |  |  | Global Address Locking configuration.<br>With `avd_design_future.only_configure_address_locking_when_used: false` (the default), this configuration is rendered<br>whenever it has at least one setting.<br>With `avd_design_future.only_configure_address_locking_when_used: true`, it is rendered only when Address Locking is enabled on a connected endpoint, network port, VLAN, or SVI.<br>In this mode, IPv4 Address Locking requires IPv4 enforcement to be disabled, LeaseQuery mode, or server-interface mode.<br>LeaseQuery mode uses `dhcp_servers_ipv4` and a local interface. If `local_interface` is not set, AVD uses the default management interface, which must resolve to an interface.<br>Server-interface mode uses `dhcp_server_interfaces` with `avd_design_future.fix_address_locking_dhcp_server_interfaces: true`.<br>IPv6 Address Locking requires IPv6 enforcement to be disabled. |
    | [<samp>&nbsp;&nbsp;local_interface</samp>](## "address_locking_settings.local_interface") | String |  |  |  | The value will be interpreted according to these rules:<br>  - `use_mgmt_interface` will configure the `mgmt_interface` as the local interface.<br>  - `use_inband_mgmt_interface` will configure the `inband_mgmt_interface` as the local interface.<br>  - `use_default_mgmt_method_interface` will configure `mgmt_interface` or `inband_mgmt_interface` as the local interface depending on the value of `default_mgmt_method`.<br>  - Any other string will be used directly as the local interface.<br>When `avd_design_future.fix_address_locking_dhcp_server_interfaces` is `true`, this setting is mutually exclusive with `dhcp_server_interfaces`.<br>For IPv4 LeaseQuery mode, configure this setting, or use a resolvable default management interface, together with at least one `dhcp_servers_ipv4` entry. |
    | [<samp>&nbsp;&nbsp;dhcp_servers_ipv4</samp>](## "address_locking_settings.dhcp_servers_ipv4") | List, items: String |  |  |  | DHCP server IPv4 addresses used by IPv4 LeaseQuery mode.<br>Requires a local interface. If `local_interface` is not configured, AVD uses the default management interface, which must resolve to an interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "address_locking_settings.dhcp_servers_ipv4.[]") | String |  |  |  | DHCP server IPv4 address. |
    | [<samp>&nbsp;&nbsp;dhcp_server_interfaces</samp>](## "address_locking_settings.dhcp_server_interfaces") | List, items: String |  |  |  | The list of interfaces connected to the DHCP server.<br>Requires `avd_design_future.fix_address_locking_dhcp_server_interfaces: true`. Otherwise this setting is ignored.<br>When enabled, this setting is mutually exclusive with `local_interface`.<br>Requires EOS version 4.36 or later.<br>This is the server-interface mode for IPv4 Address Locking, where `dhcp_servers_ipv4` is optional.<br>EOS DHCP Snooping is incompatible with IP Locking and must not be configured alongside this mode. |
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
    # Global Address Locking configuration.
    # With `avd_design_future.only_configure_address_locking_when_used: false` (the default), this configuration is rendered
    # whenever it has at least one setting.
    # With `avd_design_future.only_configure_address_locking_when_used: true`, it is rendered only when Address Locking is enabled on a connected endpoint, network port, VLAN, or SVI.
    # In this mode, IPv4 Address Locking requires IPv4 enforcement to be disabled, LeaseQuery mode, or server-interface mode.
    # LeaseQuery mode uses `dhcp_servers_ipv4` and a local interface. If `local_interface` is not set, AVD uses the default management interface, which must resolve to an interface.
    # Server-interface mode uses `dhcp_server_interfaces` with `avd_design_future.fix_address_locking_dhcp_server_interfaces: true`.
    # IPv6 Address Locking requires IPv6 enforcement to be disabled.
    address_locking_settings:

      # The value will be interpreted according to these rules:
      #   - `use_mgmt_interface` will configure the `mgmt_interface` as the local interface.
      #   - `use_inband_mgmt_interface` will configure the `inband_mgmt_interface` as the local interface.
      #   - `use_default_mgmt_method_interface` will configure `mgmt_interface` or `inband_mgmt_interface` as the local interface depending on the value of `default_mgmt_method`.
      #   - Any other string will be used directly as the local interface.
      # When `avd_design_future.fix_address_locking_dhcp_server_interfaces` is `true`, this setting is mutually exclusive with `dhcp_server_interfaces`.
      # For IPv4 LeaseQuery mode, configure this setting, or use a resolvable default management interface, together with at least one `dhcp_servers_ipv4` entry.
      local_interface: <str>

      # DHCP server IPv4 addresses used by IPv4 LeaseQuery mode.
      # Requires a local interface. If `local_interface` is not configured, AVD uses the default management interface, which must resolve to an interface.
      dhcp_servers_ipv4:

          # DHCP server IPv4 address.
        - <str>

      # The list of interfaces connected to the DHCP server.
      # Requires `avd_design_future.fix_address_locking_dhcp_server_interfaces: true`. Otherwise this setting is ignored.
      # When enabled, this setting is mutually exclusive with `local_interface`.
      # Requires EOS version 4.36 or later.
      # This is the server-interface mode for IPv4 Address Locking, where `dhcp_servers_ipv4` is optional.
      # EOS DHCP Snooping is incompatible with IP Locking and must not be configured alongside this mode.
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
