<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>stun</samp>](## "stun") | Dictionary |  |  |  | STUN configuration |
    | [<samp>&nbsp;&nbsp;client</samp>](## "stun.client") | Dictionary |  |  |  | STUN client settings |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;server_profiles</samp>](## "stun.client.server_profiles") | List, items: Dictionary |  |  |  | List of server profiles for the client |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "stun.client.server_profiles.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "stun.client.server_profiles.[].ip_address") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;server</samp>](## "stun.server") | Dictionary |  |  |  | STUN server settings |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "stun.server.local_interface") | String |  |  |  |  |

=== "YAML"

    ```yaml
    stun:
      client:
        server_profiles:
          - name: <str>
            ip_address: <str>
      server:
        local_interface: <str>
    ```
