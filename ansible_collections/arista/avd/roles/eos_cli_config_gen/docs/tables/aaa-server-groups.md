<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>aaa_server_groups</samp>](## "aaa_server_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "aaa_server_groups.[].name") | String |  |  |  | Group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_server_groups.[].type") | String |  |  | Valid Values:<br>- tacacs+<br>- radius<br>- ldap |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;servers</samp>](## "aaa_server_groups.[].servers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- server</samp>](## "aaa_server_groups.[].servers.[].server") | String |  |  |  | Hostname or IP address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "aaa_server_groups.[].servers.[].vrf") | String |  |  |  | VRF name |

=== "YAML"

    ```yaml
    aaa_server_groups:
      - name: <str>
        type: <str>
        servers:
          - server: <str>
            vrf: <str>
    ```
