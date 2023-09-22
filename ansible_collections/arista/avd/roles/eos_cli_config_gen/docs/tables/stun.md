<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>stun</samp>](## "stun") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;client</samp>](## "stun.client") | Dictionary |  |  |  | "If a device is a client"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;server_profiles</samp>](## "stun.client.server_profiles") | List, items: Dictionary |  |  |  | Enable Server profiles need to reference the name of the profile and IP address<br>Examples:<br>- "server-profile profile1<br>      ip addres 1.1.1.1"<br>- "server-profile profile2<br>      ip addres 2.2.2.2"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "stun.client.server_profiles.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "stun.client.server_profiles.[].ip_address") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;server</samp>](## "stun.server") | Dictionary |  |  |  | "If a device is a server typically this device just needs to reference a interface with a IP address and also is typically the route reflector."<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "stun.server.local_interface") | String |  |  |  | "This is typically the ethernet interface that is connected to the wan. ie ethernet1" |

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
