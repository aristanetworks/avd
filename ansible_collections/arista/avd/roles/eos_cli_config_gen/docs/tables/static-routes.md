<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>static_routes</samp>](## "static_routes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;vrf</samp>](## "static_routes.[].vrf") | String |  |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;destination_address_prefix</samp>](## "static_routes.[].destination_address_prefix") <span style="color:red">deprecated</span> | String |  |  |  | IPv4_network/Mask.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>prefix</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;prefix</samp>](## "static_routes.[].prefix") | String |  |  |  | IPv4_network/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "static_routes.[].interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "static_routes.[].gateway") <span style="color:red">deprecated</span> | String |  |  |  | IPv4 Address.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>next_hop</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;next_hop</samp>](## "static_routes.[].next_hop") | String |  |  |  | IPv4 Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;track_bfd</samp>](## "static_routes.[].track_bfd") | Boolean |  |  |  | Track next-hop using BFD. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "static_routes.[].name") | String |  |  |  | Description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |

=== "YAML"

    ```yaml
    static_routes:

        # VRF Name.
      - vrf: <str>

        # IPv4_network/Mask.
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>prefix</samp> instead.
        destination_address_prefix: <str>

        # IPv4_network/Mask.
        prefix: <str>
        interface: <str>

        # IPv4 Address.
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>next_hop</samp> instead.
        gateway: <str>

        # IPv4 Address.
        next_hop: <str>

        # Track next-hop using BFD.
        track_bfd: <bool>
        distance: <int; 1-255>
        tag: <int; 0-4294967295>

        # Description.
        name: <str>
        metric: <int; 0-4294967295>
    ```
