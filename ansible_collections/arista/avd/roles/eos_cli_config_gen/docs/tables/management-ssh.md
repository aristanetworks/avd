<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_ssh</samp>](## "management_ssh") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;authentication</samp>](## "management_ssh.authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;empty_passwords</samp>](## "management_ssh.authentication.empty_passwords") | String |  |  | Valid Values:<br>- <code>auto</code><br>- <code>deny</code><br>- <code>permit</code> | Permit or deny empty passwords for SSH authentication. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;protocols</samp>](## "management_ssh.authentication.protocols") | List, items: String |  |  |  | Allowed SSH authentication methods. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_ssh.authentication.protocols.[]") | String |  |  | Valid Values:<br>- <code>keyboard-interactive</code><br>- <code>password</code><br>- <code>public-key</code> |  |
    | [<samp>&nbsp;&nbsp;access_groups</samp>](## "management_ssh.access_groups") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>ip_access_group_in or vrfs.ip_access_group_in</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_ssh.access_groups.[].name") | String |  |  |  | Standard ACL Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_ssh.access_groups.[].vrf") | String |  |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;ipv6_access_groups</samp>](## "management_ssh.ipv6_access_groups") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>ipv6_access_group_in or vrfs.ipv6_access_group_in</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_ssh.ipv6_access_groups.[].name") | String |  |  |  | Standard ACL Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_ssh.ipv6_access_groups.[].vrf") | String |  |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;ip_access_group_in</samp>](## "management_ssh.ip_access_group_in") | String |  |  |  | Standard ACL Name. |
    | [<samp>&nbsp;&nbsp;ipv6_access_group_in</samp>](## "management_ssh.ipv6_access_group_in") | String |  |  |  | Standard IPv6 ACL Name. |
    | [<samp>&nbsp;&nbsp;idle_timeout</samp>](## "management_ssh.idle_timeout") | Integer |  |  | Min: 0<br>Max: 86400 | Idle timeout in minutes. |
    | [<samp>&nbsp;&nbsp;cipher</samp>](## "management_ssh.cipher") | List, items: String |  |  |  | Cryptographic ciphers for SSH to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_ssh.cipher.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;key_exchange</samp>](## "management_ssh.key_exchange") | List, items: String |  |  |  | Cryptographic key exchange methods for SSH to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_ssh.key_exchange.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mac</samp>](## "management_ssh.mac") | List, items: String |  |  |  | Cryptographic MAC algorithms for SSH to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_ssh.mac.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;fips_restrictions</samp>](## "management_ssh.fips_restrictions") | Boolean |  |  |  | Use FIPS compliant algorithms. |
    | [<samp>&nbsp;&nbsp;hostkey</samp>](## "management_ssh.hostkey") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;server</samp>](## "management_ssh.hostkey.server") | List, items: String |  |  |  | SSH host key settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_ssh.hostkey.server.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;server_cert</samp>](## "management_ssh.hostkey.server_cert") | String |  |  |  | Configure switch's hostkey cert file. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;client_strict_checking</samp>](## "management_ssh.hostkey.client_strict_checking") | Boolean |  |  |  | Enforce strict host key checking. |
    | [<samp>&nbsp;&nbsp;enable</samp>](## "management_ssh.enable") | Boolean |  |  |  | Enable SSH for VRF default. |
    | [<samp>&nbsp;&nbsp;connection</samp>](## "management_ssh.connection") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "management_ssh.connection.limit") | Integer |  |  | Min: 1<br>Max: 100 | Maximum total number of SSH sessions to device. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;per_host</samp>](## "management_ssh.connection.per_host") | Integer |  |  | Min: 1<br>Max: 20 | Maximum number of SSH sessions to device from a single host. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "management_ssh.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_ssh.vrfs.[].name") | String | Required, Unique |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "management_ssh.vrfs.[].enable") | Boolean |  |  |  | Enable SSH in VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_access_group_in</samp>](## "management_ssh.vrfs.[].ip_access_group_in") | String |  |  |  | Standard ACL Name.<br>This should not be set for VRF 'default'. Use `management_ssh.ip_access_group_in` instead. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_in</samp>](## "management_ssh.vrfs.[].ipv6_access_group_in") | String |  |  |  | Standard IPv6 ACL Name.<br>This should not be set for VRF 'default'. Use `management_ssh.ipv6_access_group_in` instead. |
    | [<samp>&nbsp;&nbsp;log_level</samp>](## "management_ssh.log_level") | String |  |  |  | SSH daemon log level. |
    | [<samp>&nbsp;&nbsp;client_alive</samp>](## "management_ssh.client_alive") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;count_max</samp>](## "management_ssh.client_alive.count_max") | Integer |  |  | Min: 1<br>Max: 1000 | Number of keep-alive packets that can be sent without a response before the connection is assumed dead. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "management_ssh.client_alive.interval") | Integer |  |  | Min: 1<br>Max: 1000 | Time period (in seconds) to send SSH keep-alive packets. |

=== "YAML"

    ```yaml
    management_ssh:
      authentication:

        # Permit or deny empty passwords for SSH authentication.
        empty_passwords: <str; "auto" | "deny" | "permit">

        # Allowed SSH authentication methods.
        protocols:
          - <str; "keyboard-interactive" | "password" | "public-key">
      # This key is deprecated.
      # Support will be removed in AVD version 6.0.0.
      # Use `ip_access_group_in` or `vrfs.ip_access_group_in` instead.
      access_groups:

          # Standard ACL Name.
        - name: <str>

          # VRF Name.
          vrf: <str>
      # This key is deprecated.
      # Support will be removed in AVD version 6.0.0.
      # Use `ipv6_access_group_in` or `vrfs.ipv6_access_group_in` instead.
      ipv6_access_groups:

          # Standard ACL Name.
        - name: <str>

          # VRF Name.
          vrf: <str>

      # Standard ACL Name.
      ip_access_group_in: <str>

      # Standard IPv6 ACL Name.
      ipv6_access_group_in: <str>

      # Idle timeout in minutes.
      idle_timeout: <int; 0-86400>

      # Cryptographic ciphers for SSH to use.
      cipher:
        - <str>

      # Cryptographic key exchange methods for SSH to use.
      key_exchange:
        - <str>

      # Cryptographic MAC algorithms for SSH to use.
      mac:
        - <str>

      # Use FIPS compliant algorithms.
      fips_restrictions: <bool>
      hostkey:

        # SSH host key settings.
        server:
          - <str>

        # Configure switch's hostkey cert file.
        server_cert: <str>

        # Enforce strict host key checking.
        client_strict_checking: <bool>

      # Enable SSH for VRF default.
      enable: <bool>
      connection:

        # Maximum total number of SSH sessions to device.
        limit: <int; 1-100>

        # Maximum number of SSH sessions to device from a single host.
        per_host: <int; 1-20>
      vrfs:

          # VRF Name.
        - name: <str; required; unique>

          # Enable SSH in VRF.
          enable: <bool>

          # Standard ACL Name.
          # This should not be set for VRF 'default'. Use `management_ssh.ip_access_group_in` instead.
          ip_access_group_in: <str>

          # Standard IPv6 ACL Name.
          # This should not be set for VRF 'default'. Use `management_ssh.ipv6_access_group_in` instead.
          ipv6_access_group_in: <str>

      # SSH daemon log level.
      log_level: <str>
      client_alive:

        # Number of keep-alive packets that can be sent without a response before the connection is assumed dead.
        count_max: <int; 1-1000>

        # Time period (in seconds) to send SSH keep-alive packets.
        interval: <int; 1-1000>
    ```
