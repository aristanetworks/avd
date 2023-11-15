<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_ssh</samp>](## "management_ssh") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;access_groups</samp>](## "management_ssh.access_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_ssh.access_groups.[].name") | String |  |  |  | Standard ACL Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_ssh.access_groups.[].vrf") | String |  |  |  | VRF Name |
    | [<samp>&nbsp;&nbsp;ipv6_access_groups</samp>](## "management_ssh.ipv6_access_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_ssh.ipv6_access_groups.[].name") | String |  |  |  | Standard ACL Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_ssh.ipv6_access_groups.[].vrf") | String |  |  |  | VRF Name |
    | [<samp>&nbsp;&nbsp;idle_timeout</samp>](## "management_ssh.idle_timeout") | Integer |  |  | Min: 0<br>Max: 86400 | Idle timeout in minutes |
    | [<samp>&nbsp;&nbsp;cipher</samp>](## "management_ssh.cipher") | List, items: String |  |  |  | Cryptographic ciphers for SSH to use |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_ssh.cipher.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;key_exchange</samp>](## "management_ssh.key_exchange") | List, items: String |  |  |  | Cryptographic key exchange methods for SSH to use |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_ssh.key_exchange.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mac</samp>](## "management_ssh.mac") | List, items: String |  |  |  | Cryptographic MAC algorithms for SSH to use |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_ssh.mac.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;hostkey</samp>](## "management_ssh.hostkey") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;server</samp>](## "management_ssh.hostkey.server") | List, items: String |  |  |  | SSH host key settings |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_ssh.hostkey.server.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable</samp>](## "management_ssh.enable") | Boolean |  |  |  | Enable SSH daemon |
    | [<samp>&nbsp;&nbsp;connection</samp>](## "management_ssh.connection") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "management_ssh.connection.limit") | Integer |  |  | Min: 1<br>Max: 100 | Maximum total number of SSH sessions to device |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;per_host</samp>](## "management_ssh.connection.per_host") | Integer |  |  | Min: 1<br>Max: 20 | Maximum number of SSH sessions to device from a single host |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "management_ssh.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_ssh.vrfs.[].name") | String | Required, Unique |  |  | VRF Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "management_ssh.vrfs.[].enable") | Boolean |  |  |  | Enable SSH in VRF |
    | [<samp>&nbsp;&nbsp;log_level</samp>](## "management_ssh.log_level") | String |  |  |  | SSH daemon log level |
    | [<samp>&nbsp;&nbsp;client_alive</samp>](## "management_ssh.client_alive") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;count_max</samp>](## "management_ssh.client_alive.count_max") | Integer |  |  | Min: 1<br>Max: 1000 | Number of keep-alive packets that can be sent without a response before the connection is assumed dead. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "management_ssh.client_alive.interval") | Integer |  |  | Min: 1<br>Max: 1000 | Time period (in seconds) to send SSH keep-alive packets. |

=== "YAML"

    ```yaml
    management_ssh:
      access_groups:

          # Standard ACL Name
        - name: <str>

          # VRF Name
          vrf: <str>
      ipv6_access_groups:

          # Standard ACL Name
        - name: <str>

          # VRF Name
          vrf: <str>

      # Idle timeout in minutes
      idle_timeout: <int; 0-86400>

      # Cryptographic ciphers for SSH to use
      cipher:
        - <str>

      # Cryptographic key exchange methods for SSH to use
      key_exchange:
        - <str>

      # Cryptographic MAC algorithms for SSH to use
      mac:
        - <str>
      hostkey:

        # SSH host key settings
        server:
          - <str>

      # Enable SSH daemon
      enable: <bool>
      connection:

        # Maximum total number of SSH sessions to device
        limit: <int; 1-100>

        # Maximum number of SSH sessions to device from a single host
        per_host: <int; 1-20>
      vrfs:

          # VRF Name
        - name: <str; required; unique>

          # Enable SSH in VRF
          enable: <bool>

      # SSH daemon log level
      log_level: <str>
      client_alive:

        # Number of keep-alive packets that can be sent without a response before the connection is assumed dead.
        count_max: <int; 1-1000>

        # Time period (in seconds) to send SSH keep-alive packets.
        interval: <int; 1-1000>
    ```
