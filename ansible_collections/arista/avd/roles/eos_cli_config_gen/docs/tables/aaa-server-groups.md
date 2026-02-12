<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>aaa_server_groups</samp>](## "aaa_server_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "aaa_server_groups.[].name") | String | Required, Unique |  | Pattern: `^(?:r[^a].*|ra[^d].*|rad[^i].*|radi[^u].*|radiu[^s].*|radius.+|t[^a].*|ta[^c].*|tac[^a].*|taca[^c].*|tacac[^s].*|tacacs[^+].*|tacacs\+.+|[^rt].*)$` | Group name.<br>The group names `radius` and `tacacs+` are reserved by EOS and must not be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_server_groups.[].type") | String | Required |  | Valid Values:<br>- <code>tacacs+</code><br>- <code>radius</code><br>- <code>ldap</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;servers</samp>](## "aaa_server_groups.[].servers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;server</samp>](## "aaa_server_groups.[].servers.[].server") | String | Required |  |  | Hostname or IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "aaa_server_groups.[].servers.[].vrf") | String |  |  |  | VRF name. |

=== "YAML"

    ```yaml
    aaa_server_groups:

        # Group name.
        # The group names `radius` and `tacacs+` are reserved by EOS and must not be used.
      - name: <str; required; unique>
        type: <str; "tacacs+" | "radius" | "ldap"; required>
        servers:

            # Hostname or IP address.
          - server: <str; required>

            # VRF name.
            vrf: <str>
    ```
