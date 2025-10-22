<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>address_locking_settings</samp>](## "address_locking_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;local_interface</samp>](## "address_locking_settings.local_interface") | String |  | `use_default_mgmt_method_interface` |  | The value will be interpreted according to these rules:<br>  - `use_mgmt_interface` will configure the `mgmt_interface` as the local interface.<br>  - `use_inband_mgmt_interface` will configure the `inband_mgmt_interface` as the local interface.<br>  - `use_default_mgmt_method_interface` will configure `mgmt_interface` or `inband_mgmt_interface` as the local interface depending on the value of `default_mgmt_method`.<br>  - Any other string will be used directly as the local interface. |
    | [<samp>&nbsp;&nbsp;local_users</samp>](## "address_locking_settings.local_users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "address_locking_settings.local_users.[].name") | String | Required, Unique |  |  | Username. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "address_locking_settings.local_users.[].disabled") | Boolean |  |  |  | If true, the user will be removed and all other settings are ignored.<br>Useful for removing the default "admin" user.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "address_locking_settings.local_users.[].privilege") | Integer |  |  | Min: 0<br>Max: 15 | Initial privilege level with local EXEC authorization.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "address_locking_settings.local_users.[].role") | String |  |  |  | EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp>](## "address_locking_settings.local_users.[].sha512_password") | String |  |  |  | SHA512 Hash of Password.<br>Must be the hash of the password. By default EOS salts the password with the username, so the simplest is to generate the hash on an EOS device using the same username.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_password</samp>](## "address_locking_settings.local_users.[].no_password") | Boolean |  |  |  | If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ssh_key</samp>](## "address_locking_settings.local_users.[].ssh_key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;secondary_ssh_key</samp>](## "address_locking_settings.local_users.[].secondary_ssh_key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shell</samp>](## "address_locking_settings.local_users.[].shell") | String |  |  | Valid Values:<br>- <code>/bin/bash</code><br>- <code>/bin/sh</code><br>- <code>/sbin/nologin</code> | Specify shell for the user.<br> |
    | [<samp>&nbsp;&nbsp;dhcp_servers_ipv4</samp>](## "address_locking_settings.dhcp_servers_ipv4") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "address_locking_settings.dhcp_servers_ipv4.[]") | String |  |  |  | DHCP server IPv4 address. |
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
      local_users:

          # Username.
        - name: <str; required; unique>

          # If true, the user will be removed and all other settings are ignored.
          # Useful for removing the default "admin" user.
          disabled: <bool>

          # Initial privilege level with local EXEC authorization.
          privilege: <int; 0-15>

          # EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator".
          role: <str>

          # SHA512 Hash of Password.
          # Must be the hash of the password. By default EOS salts the password with the username, so the simplest is to generate the hash on an EOS device using the same username.
          sha512_password: <str>

          # If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user.
          no_password: <bool>
          ssh_key: <str>
          secondary_ssh_key: <str>

          # Specify shell for the user.
          shell: <str; "/bin/bash" | "/bin/sh" | "/sbin/nologin">
      dhcp_servers_ipv4:

          # DHCP server IPv4 address.
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
