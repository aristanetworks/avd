<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>aaa_server_groups</samp>](## "aaa_server_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "aaa_server_groups.[].name") | String | Required, Unique |  | Pattern: `(?!radius$|tacacs\+$|ldap$).+` | Group name.<br>The group names 'radius', 'tacacs+' and 'ldap' are reserved by EOS and must not be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_server_groups.[].type") | String | Required |  | Valid Values:<br>- <code>tacacs+</code><br>- <code>radius</code><br>- <code>ldap</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;servers</samp>](## "aaa_server_groups.[].servers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;server</samp>](## "aaa_server_groups.[].servers.[].server") | String | Required |  |  | Hostname or IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "aaa_server_groups.[].servers.[].vrf") | String |  |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tls</samp>](## "aaa_server_groups.[].servers.[].tls") | Dictionary |  |  |  | TLS settings for the RADIUS group server. Only applicable when the parent server group type is 'radius'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "aaa_server_groups.[].servers.[].tls.enabled") | Boolean | Required |  |  | Enable TLS to secure communication with the RADIUS group server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "aaa_server_groups.[].servers.[].tls.port") | Integer |  |  | Min: 1<br>Max: 65535 | TCP port used for TLS-secured RADIUS communication. Overrides the default RadSec port (EOS default is 2083). |

=== "YAML"

    ```yaml
    aaa_server_groups:

        # Group name.
        # The group names 'radius', 'tacacs+' and 'ldap' are reserved by EOS and must not be used.
      - name: <str; required; unique>
        type: <str; "tacacs+" | "radius" | "ldap"; required>
        servers:

            # Hostname or IP address.
          - server: <str; required>

            # VRF name.
            vrf: <str>

            # TLS settings for the RADIUS group server. Only applicable when the parent server group type is 'radius'.
            tls:

              # Enable TLS to secure communication with the RADIUS group server.
              enabled: <bool; required>

              # TCP port used for TLS-secured RADIUS communication. Overrides the default RadSec port (EOS default is 2083).
              port: <int; 1-65535>
    ```
