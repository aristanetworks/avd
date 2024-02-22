<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_peer_groups</samp>](## "bgp_peer_groups") | Dictionary |  |  |  | Leverage an Arista EOS switch to generate the encrypted password using the correct peer group name.<br>Note that the name of the peer groups use '-' instead of '_' in EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;wan_overlay_peers</samp>](## "bgp_peer_groups.wan_overlay_peers") | Dictionary |  |  |  | PREVIEW: This key is currently not supported |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.wan_overlay_peers.name") | String |  | `WAN-OVERLAY-PEERS` |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.wan_overlay_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "bgp_peer_groups.wan_overlay_peers.bfd") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd_timers</samp>](## "bgp_peer_groups.wan_overlay_peers.bfd_timers") | Dictionary |  |  |  | Specify the BFD timers to override the default values.<br>It is recommended to keep BFD total timeout longer than the DPS timeout.<br>The Default BFD timeout is 10 x 1 seconds and the default DPS timeout is 5 x 1 seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "bgp_peer_groups.wan_overlay_peers.bfd_timers.interval") | Integer | Required | `1000` | Min: 50<br>Max: 60000 | Interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "bgp_peer_groups.wan_overlay_peers.bfd_timers.min_rx") | Integer | Required | `1000` | Min: 50<br>Max: 60000 | Rate in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "bgp_peer_groups.wan_overlay_peers.bfd_timers.multiplier") | Integer | Required | `10` | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;listen_range_prefixes</samp>](## "bgp_peer_groups.wan_overlay_peers.listen_range_prefixes") | List, items: String |  |  |  | Only used for nodes where `wan_role` is `server` like AutoVPN RRs and Pathfinders.<br>For clients, AVD will raise an error if the Loopback0 IP is not in any listen range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "bgp_peer_groups.wan_overlay_peers.listen_range_prefixes.[]") | String |  |  |  | The prefixes to use in listen_range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.wan_overlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ttl_maximum_hops</samp>](## "bgp_peer_groups.wan_overlay_peers.ttl_maximum_hops") | Integer |  | `1` |  |  |
    | [<samp>&nbsp;&nbsp;wan_rr_overlay_peers</samp>](## "bgp_peer_groups.wan_rr_overlay_peers") | Dictionary |  |  |  | PREVIEW: This key is currently not supported<br>Configuration options for the peer-group created to peer between<br>AutoVPN RRs or CV-Pathfinders. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.wan_rr_overlay_peers.name") | String |  | `WAN-RR-OVERLAY-PEERS` |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.wan_rr_overlay_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "bgp_peer_groups.wan_rr_overlay_peers.bfd") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd_timers</samp>](## "bgp_peer_groups.wan_rr_overlay_peers.bfd_timers") | Dictionary |  |  |  | Specify the BFD timers to override the default values.<br>It is recommended to keep BFD total timeout longer than the DPS timeout.<br>The Default BFD timeout is 10 x 1 seconds and the default DPS timeout is 5 x 1 seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "bgp_peer_groups.wan_rr_overlay_peers.bfd_timers.interval") | Integer | Required | `1000` | Min: 50<br>Max: 60000 | Interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "bgp_peer_groups.wan_rr_overlay_peers.bfd_timers.min_rx") | Integer | Required | `1000` | Min: 50<br>Max: 60000 | Rate in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "bgp_peer_groups.wan_rr_overlay_peers.bfd_timers.multiplier") | Integer | Required | `10` | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.wan_rr_overlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ttl_maximum_hops</samp>](## "bgp_peer_groups.wan_rr_overlay_peers.ttl_maximum_hops") | Integer |  | `1` |  |  |

=== "YAML"

    ```yaml
    # Leverage an Arista EOS switch to generate the encrypted password using the correct peer group name.
    # Note that the name of the peer groups use '-' instead of '_' in EOS configuration.
    bgp_peer_groups:

      # PREVIEW: This key is currently not supported
      wan_overlay_peers:

        # Name of peer group.
        name: <str; default="WAN-OVERLAY-PEERS">

        # Type 7 encrypted password.
        password: <str>
        bfd: <bool; default=True>

        # Specify the BFD timers to override the default values.
        # It is recommended to keep BFD total timeout longer than the DPS timeout.
        # The Default BFD timeout is 10 x 1 seconds and the default DPS timeout is 5 x 1 seconds.
        bfd_timers:

          # Interval in milliseconds.
          interval: <int; 50-60000; default=1000; required>

          # Rate in milliseconds.
          min_rx: <int; 50-60000; default=1000; required>
          multiplier: <int; 3-50; default=10; required>

        # Only used for nodes where `wan_role` is `server` like AutoVPN RRs and Pathfinders.
        # For clients, AVD will raise an error if the Loopback0 IP is not in any listen range.
        listen_range_prefixes:

            # The prefixes to use in listen_range.
          - <str>

        # Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
        structured_config: <dict>
        ttl_maximum_hops: <int; default=1>

      # PREVIEW: This key is currently not supported
      # Configuration options for the peer-group created to peer between
      # AutoVPN RRs or CV-Pathfinders.
      wan_rr_overlay_peers:

        # Name of peer group.
        name: <str; default="WAN-RR-OVERLAY-PEERS">

        # Type 7 encrypted password.
        password: <str>
        bfd: <bool; default=True>

        # Specify the BFD timers to override the default values.
        # It is recommended to keep BFD total timeout longer than the DPS timeout.
        # The Default BFD timeout is 10 x 1 seconds and the default DPS timeout is 5 x 1 seconds.
        bfd_timers:

          # Interval in milliseconds.
          interval: <int; 50-60000; default=1000; required>

          # Rate in milliseconds.
          min_rx: <int; 50-60000; default=1000; required>
          multiplier: <int; 3-50; default=10; required>

        # Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
        structured_config: <dict>
        ttl_maximum_hops: <int; default=1>
    ```
