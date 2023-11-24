<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>radius_servers</samp>](## "radius_servers") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version v5.0.0. Use <samp>radius_server.hosts</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;-&nbsp;host</samp>](## "radius_servers.[].host") | String |  |  |  | Host IP address or name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "radius_servers.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "radius_servers.[].key") | String |  |  |  | Encrypted key |

=== "YAML"

    ```yaml
    # This key is deprecated.
    # Support will be removed in AVD version v5.0.0.
    # Use <samp>radius_server.hosts</samp> instead.
    radius_servers:

        # Host IP address or name
      - host: <str>
        vrf: <str>

        # Encrypted key
        key: <str>
    ```
