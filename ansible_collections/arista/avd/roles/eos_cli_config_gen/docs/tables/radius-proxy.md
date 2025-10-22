<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>radius_proxy</samp>](## "radius_proxy") | Dictionary |  |  |  | Configure RADIUS proxy parameters. |
    | [<samp>&nbsp;&nbsp;client_key</samp>](## "radius_proxy.client_key") | String |  |  |  | Set client secret key, allowed max size is 128.<br>Only type 7 supported. |
    | [<samp>&nbsp;&nbsp;client_session_idle_timeout</samp>](## "radius_proxy.client_session_idle_timeout") | Integer |  |  | Min: 1<br>Max: 86400 | Idle timeout in seconds. |
    | [<samp>&nbsp;&nbsp;dynamic_authorization</samp>](## "radius_proxy.dynamic_authorization") | Boolean |  |  |  | Enable/Disable dynamic authorization. |
    | [<samp>&nbsp;&nbsp;client_groups</samp>](## "radius_proxy.client_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "radius_proxy.client_groups.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;server_groups</samp>](## "radius_proxy.client_groups.[].server_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "radius_proxy.client_groups.[].server_groups.[]") | String |  |  |  | RADIUS server-group names. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "radius_proxy.client_groups.[].vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "radius_proxy.client_groups.[].vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_clients</samp>](## "radius_proxy.client_groups.[].vrfs.[].ipv4_clients") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;address</samp>](## "radius_proxy.client_groups.[].vrfs.[].ipv4_clients.[].address") | String | Required, Unique |  | Format: ipv4 | IPv4 address "A.B.C.D" or prefix "A.B.C.D/E". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "radius_proxy.client_groups.[].vrfs.[].ipv4_clients.[].key") | String |  |  |  | Key for this client. Overrides`radius_proxy.client_key`.<br>Only type 7 supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_clients</samp>](## "radius_proxy.client_groups.[].vrfs.[].ipv6_clients") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;address</samp>](## "radius_proxy.client_groups.[].vrfs.[].ipv6_clients.[].address") | String | Required, Unique |  | Format: ipv6 | IPv6 address "A:B:C:D:E:F:G:H" prefix "A:B:C:D:E:F:G:H/I". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "radius_proxy.client_groups.[].vrfs.[].ipv6_clients.[].key") | String |  |  |  | Key for this client. Overrides`radius_proxy.client_key`.<br>Only type 7 supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_clients</samp>](## "radius_proxy.client_groups.[].vrfs.[].host_clients") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "radius_proxy.client_groups.[].vrfs.[].host_clients.[].name") | String | Required, Unique |  |  | Hostname. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "radius_proxy.client_groups.[].vrfs.[].host_clients.[].key") | String |  |  |  | Key for this client. Overrides`radius_proxy.client_key`.<br>Only type 7 supported. |

=== "YAML"

    ```yaml
    # Configure RADIUS proxy parameters.
    radius_proxy:

      # Set client secret key, allowed max size is 128.
      # Only type 7 supported.
      client_key: <str>

      # Idle timeout in seconds.
      client_session_idle_timeout: <int; 1-86400>

      # Enable/Disable dynamic authorization.
      dynamic_authorization: <bool>
      client_groups:
        - name: <str; required; unique>
          server_groups:

              # RADIUS server-group names.
            - <str>
          vrfs:
            - name: <str; required; unique>
              ipv4_clients:

                  # IPv4 address "A.B.C.D" or prefix "A.B.C.D/E".
                - address: <str; required; unique>

                  # Key for this client. Overrides`radius_proxy.client_key`.
                  # Only type 7 supported.
                  key: <str>
              ipv6_clients:

                  # IPv6 address "A:B:C:D:E:F:G:H" prefix "A:B:C:D:E:F:G:H/I".
                - address: <str; required; unique>

                  # Key for this client. Overrides`radius_proxy.client_key`.
                  # Only type 7 supported.
                  key: <str>
              host_clients:

                  # Hostname.
                - name: <str; required; unique>

                  # Key for this client. Overrides`radius_proxy.client_key`.
                  # Only type 7 supported.
                  key: <str>
    ```
