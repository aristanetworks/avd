<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>event_handlers</samp>](## "event_handlers") | List, items: Dictionary |  |  |  | Gives the ability to monitor and react to Syslog messages.<br>Event Handlers provide a powerful and flexible tool that can be used to apply self-healing actions,<br>customize the system behavior, and implement workarounds to problems discovered in the field.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "event_handlers.[].name") | String | Required, Unique |  |  | Event Handler Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action_type</samp>](## "event_handlers.[].action_type") | String |  |  | Valid Values:<br>- <code>bash</code><br>- <code>increment</code><br>- <code>log</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "event_handlers.[].action") | String |  |  |  | Command to execute<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "event_handlers.[].delay") | Integer |  |  |  | Event-handler delay in seconds<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger</samp>](## "event_handlers.[].trigger") | String |  |  | Valid Values:<br>- <code>on-boot</code><br>- <code>on-logging</code><br>- <code>on-startup-config</code> | Configure event trigger condition.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;regex</samp>](## "event_handlers.[].regex") | String |  |  |  | Regular expression to use for searching log messages. Required for on-logging trigger<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;asynchronous</samp>](## "event_handlers.[].asynchronous") | Boolean |  | `False` |  | Set the action to be non-blocking. |
    | [<samp>ipv6_mgmt_destination_networks</samp>](## "ipv6_mgmt_destination_networks") | List, items: String |  |  |  | List of IPv6 prefixes to configure as static routes towards the OOB IPv6 Management interface gateway.<br>Replaces the default route.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ipv6_mgmt_destination_networks.[]") | String |  |  |  | IPv6_network/Mask. |
    | [<samp>ipv6_mgmt_gateway</samp>](## "ipv6_mgmt_gateway") | String |  |  | Format: ipv6 | OOB Management interface gateway in IPv6 format.<br>Used as next-hop for default gateway or static routes defined under 'ipv6_mgmt_destination_networks'. |
    | [<samp>local_users</samp>](## "local_users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "local_users.[].name") | String | Required, Unique |  |  | Username |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "local_users.[].disabled") | Boolean |  |  |  | If true, the user will be removed and all other settings are ignored.<br>Useful for removing the default "admin" user.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "local_users.[].privilege") | Integer |  |  | Min: 0<br>Max: 15 | Initial privilege level with local EXEC authorization.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "local_users.[].role") | String |  |  |  | EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp>](## "local_users.[].sha512_password") | String |  |  |  | SHA512 Hash of Password<br>Must be the hash of the password. By default EOS salts the password with the username, so the simplest is to generate the hash on an EOS device using the same username.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;no_password</samp>](## "local_users.[].no_password") | Boolean |  |  |  | If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssh_key</samp>](## "local_users.[].ssh_key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shell</samp>](## "local_users.[].shell") | String |  |  | Valid Values:<br>- <code>/bin/bash</code><br>- <code>/bin/sh</code><br>- <code>/sbin/nologin</code> | Specify shell for the user<br> |
    | [<samp>management_eapi</samp>](## "management_eapi") | Dictionary |  |  |  | Default is HTTPS management eAPI enabled.<br>The VRF is set to < mgmt_interface_vrf >.<br> |
    | [<samp>&nbsp;&nbsp;enable_http</samp>](## "management_eapi.enable_http") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;enable_https</samp>](## "management_eapi.enable_https") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;default_services</samp>](## "management_eapi.default_services") | Boolean |  |  |  |  |
    | [<samp>name_servers</samp>](## "name_servers") | List, items: String |  |  |  | List of DNS servers. The VRF is set to < mgmt_interface_vrf >. |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "name_servers.[]") | String |  |  |  | IPv4 address |
    | [<samp>ntp_settings</samp>](## "ntp_settings") | Dictionary |  |  |  | NTP settings |
    | [<samp>&nbsp;&nbsp;server_vrf</samp>](## "ntp_settings.server_vrf") | String |  |  |  | EOS only supports NTP servers in one VRF, so this VRF is used for all NTP servers and one local-interface.<br>- `use_mgmt_interface_vrf` will configure the NTP server(s) under the VRF set with `mgmt_interface_vrf` and set the `mgmt_interface` as NTP local-interface.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the NTP server(s) under the VRF set with `inband_mgmt_vrf` and set the `inband_mgmt_interface` as NTP local-interface.<br>  An error will be raised if inband management is not configured for the device.<br>- Any other string will be used directly as the VRF name but local interface must be set with `custom_structured_configuration_ntp` if needed.<br>If not set, the VRF is automatically picked up from the global setting `default_mgmt_method`. |
    | [<samp>&nbsp;&nbsp;servers</samp>](## "ntp_settings.servers") | List, items: Dictionary |  |  |  | The first server is always set as "preferred". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ntp_settings.servers.[].name") | String |  |  |  | IP or hostname e.g., 2.2.2.55, ie.pool.ntp.org |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;burst</samp>](## "ntp_settings.servers.[].burst") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iburst</samp>](## "ntp_settings.servers.[].iburst") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "ntp_settings.servers.[].key") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maxpoll</samp>](## "ntp_settings.servers.[].maxpoll") | Integer |  |  | Min: 3<br>Max: 17 | Value of maxpoll between 3 - 17 (Logarithmic) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minpoll</samp>](## "ntp_settings.servers.[].minpoll") | Integer |  |  | Min: 3<br>Max: 17 | Value of minpoll between 3 - 17 (Logarithmic) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "ntp_settings.servers.[].version") | Integer |  |  | Min: 1<br>Max: 4 |  |
    | [<samp>&nbsp;&nbsp;authenticate</samp>](## "ntp_settings.authenticate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;authenticate_servers_only</samp>](## "ntp_settings.authenticate_servers_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;authentication_keys</samp>](## "ntp_settings.authentication_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "ntp_settings.authentication_keys.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 65534 | Key identifier |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "ntp_settings.authentication_keys.[].hash_algorithm") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha1</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "ntp_settings.authentication_keys.[].key") | String |  |  |  | Obfuscated key |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "ntp_settings.authentication_keys.[].key_type") | String |  |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> |  |
    | [<samp>&nbsp;&nbsp;trusted_keys</samp>](## "ntp_settings.trusted_keys") | String |  |  |  | List of trusted-keys as string ex. 10-12,15 |
    | [<samp>timezone</samp>](## "timezone") | String |  |  |  | Clock timezone like "CET" or "US/Pacific". |

=== "YAML"

    ```yaml
    # Gives the ability to monitor and react to Syslog messages.
    # Event Handlers provide a powerful and flexible tool that can be used to apply self-healing actions,
    # customize the system behavior, and implement workarounds to problems discovered in the field.
    event_handlers:

        # Event Handler Name
      - name: <str; required; unique>
        action_type: <str; "bash" | "increment" | "log">

        # Command to execute
        action: <str>

        # Event-handler delay in seconds
        delay: <int>

        # Configure event trigger condition.
        trigger: <str; "on-boot" | "on-logging" | "on-startup-config">

        # Regular expression to use for searching log messages. Required for on-logging trigger
        regex: <str>

        # Set the action to be non-blocking.
        asynchronous: <bool; default=False>

    # List of IPv6 prefixes to configure as static routes towards the OOB IPv6 Management interface gateway.
    # Replaces the default route.
    ipv6_mgmt_destination_networks:

        # IPv6_network/Mask.
      - <str>

    # OOB Management interface gateway in IPv6 format.
    # Used as next-hop for default gateway or static routes defined under 'ipv6_mgmt_destination_networks'.
    ipv6_mgmt_gateway: <str>
    local_users:

        # Username
      - name: <str; required; unique>

        # If true, the user will be removed and all other settings are ignored.
        # Useful for removing the default "admin" user.
        disabled: <bool>

        # Initial privilege level with local EXEC authorization.
        privilege: <int; 0-15>

        # EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator"
        role: <str>

        # SHA512 Hash of Password
        # Must be the hash of the password. By default EOS salts the password with the username, so the simplest is to generate the hash on an EOS device using the same username.
        sha512_password: <str>

        # If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user.
        no_password: <bool>
        ssh_key: <str>

        # Specify shell for the user
        shell: <str; "/bin/bash" | "/bin/sh" | "/sbin/nologin">

    # Default is HTTPS management eAPI enabled.
    # The VRF is set to < mgmt_interface_vrf >.
    management_eapi:
      enable_http: <bool; default=False>
      enable_https: <bool; default=True>
      default_services: <bool>

    # List of DNS servers. The VRF is set to < mgmt_interface_vrf >.
    name_servers:

        # IPv4 address
      - <str>

    # NTP settings
    ntp_settings:

      # EOS only supports NTP servers in one VRF, so this VRF is used for all NTP servers and one local-interface.
      # - `use_mgmt_interface_vrf` will configure the NTP server(s) under the VRF set with `mgmt_interface_vrf` and set the `mgmt_interface` as NTP local-interface.
      #   An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.
      # - `use_inband_mgmt_vrf` will configure the NTP server(s) under the VRF set with `inband_mgmt_vrf` and set the `inband_mgmt_interface` as NTP local-interface.
      #   An error will be raised if inband management is not configured for the device.
      # - Any other string will be used directly as the VRF name but local interface must be set with `custom_structured_configuration_ntp` if needed.
      # If not set, the VRF is automatically picked up from the global setting `default_mgmt_method`.
      server_vrf: <str>

      # The first server is always set as "preferred".
      servers:

          # IP or hostname e.g., 2.2.2.55, ie.pool.ntp.org
        - name: <str>
          burst: <bool>
          iburst: <bool>
          key: <int; 1-65535>

          # Value of maxpoll between 3 - 17 (Logarithmic)
          maxpoll: <int; 3-17>

          # Value of minpoll between 3 - 17 (Logarithmic)
          minpoll: <int; 3-17>
          version: <int; 1-4>
      authenticate: <bool>
      authenticate_servers_only: <bool>
      authentication_keys:

          # Key identifier
        - id: <int; 1-65534; required; unique>
          hash_algorithm: <str; "md5" | "sha1">

          # Obfuscated key
          key: <str>
          key_type: <str; "0" | "7" | "8a">

      # List of trusted-keys as string ex. 10-12,15
      trusted_keys: <str>

    # Clock timezone like "CET" or "US/Pacific".
    timezone: <str>
    ```
