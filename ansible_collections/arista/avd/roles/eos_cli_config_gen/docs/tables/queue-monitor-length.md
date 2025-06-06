<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>queue_monitor_length</samp>](## "queue_monitor_length") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "queue_monitor_length.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;default_thresholds</samp>](## "queue_monitor_length.default_thresholds") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;high</samp>](## "queue_monitor_length.default_thresholds.high") | Integer | Required |  |  | Default high threshold for Ethernet Interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;low</samp>](## "queue_monitor_length.default_thresholds.low") | Integer |  |  |  | Default low threshold for Ethernet Interfaces.<br>Low threshold support is platform dependent.<br> |
    | [<samp>&nbsp;&nbsp;log</samp>](## "queue_monitor_length.log") | Integer |  |  |  | Logging interval in seconds. |
    | [<samp>&nbsp;&nbsp;notifying</samp>](## "queue_monitor_length.notifying") | Boolean |  |  |  | Should only be used for platforms supporting the "queue-monitor length notifying" CLI. |
    | [<samp>&nbsp;&nbsp;cpu</samp>](## "queue_monitor_length.cpu") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;thresholds</samp>](## "queue_monitor_length.cpu.thresholds") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;high</samp>](## "queue_monitor_length.cpu.thresholds.high") | Integer | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;low</samp>](## "queue_monitor_length.cpu.thresholds.low") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;tx_latency</samp>](## "queue_monitor_length.tx_latency") | Boolean |  |  |  | Enable tx-latency mode. |
    | [<samp>&nbsp;&nbsp;mirror</samp>](## "queue_monitor_length.mirror") | Dictionary |  |  |  | Enable frame mirroring during congestion. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "queue_monitor_length.mirror.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "queue_monitor_length.mirror.destination") | Dictionary |  |  |  | Mirror destination. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cpu</samp>](## "queue_monitor_length.mirror.destination.cpu") | Boolean |  |  |  | CPU ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ethernet_interfaces</samp>](## "queue_monitor_length.mirror.destination.ethernet_interfaces") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "queue_monitor_length.mirror.destination.ethernet_interfaces.[]") | String |  |  |  | Ethernet interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel_mode_gre</samp>](## "queue_monitor_length.mirror.destination.tunnel_mode_gre") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "queue_monitor_length.mirror.destination.tunnel_mode_gre.source") | String | Required |  |  | Source IP address of GRE tunnel. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "queue_monitor_length.mirror.destination.tunnel_mode_gre.destination") | String | Required |  |  | Destination IP address of GRE tunnel. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "queue_monitor_length.mirror.destination.tunnel_mode_gre.dscp") | Integer |  |  | Min: 0<br>Max: 63 | DSCP of the GRE tunnel. EOS default is 0. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "queue_monitor_length.mirror.destination.tunnel_mode_gre.ttl") | Integer |  |  | Min: 1<br>Max: 255 | TTL range. EOS default is 128. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "queue_monitor_length.mirror.destination.tunnel_mode_gre.protocol") | String |  |  |  | Protocol type in GRE header. Protocol range - 0x0000-0xFFFF.<br>EOS default is 0x88BE. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "queue_monitor_length.mirror.destination.tunnel_mode_gre.vrf") | String |  |  |  | VRF name of the GRE tunnel. EOS default is "default". |

=== "YAML"

    ```yaml
    queue_monitor_length:
      enabled: <bool; required>
      default_thresholds:

        # Default high threshold for Ethernet Interfaces.
        high: <int; required>

        # Default low threshold for Ethernet Interfaces.
        # Low threshold support is platform dependent.
        low: <int>

      # Logging interval in seconds.
      log: <int>

      # Should only be used for platforms supporting the "queue-monitor length notifying" CLI.
      notifying: <bool>
      cpu:
        thresholds:
          high: <int; required>
          low: <int>

      # Enable tx-latency mode.
      tx_latency: <bool>

      # Enable frame mirroring during congestion.
      mirror:
        enabled: <bool>

        # Mirror destination.
        destination:

          # CPU ports.
          cpu: <bool>
          ethernet_interfaces:

              # Ethernet interface name.
            - <str>
          tunnel_mode_gre:

            # Source IP address of GRE tunnel.
            source: <str; required>

            # Destination IP address of GRE tunnel.
            destination: <str; required>

            # DSCP of the GRE tunnel. EOS default is 0.
            dscp: <int; 0-63>

            # TTL range. EOS default is 128.
            ttl: <int; 1-255>

            # Protocol type in GRE header. Protocol range - 0x0000-0xFFFF.
            # EOS default is 0x88BE.
            protocol: <str>

            # VRF name of the GRE tunnel. EOS default is "default".
            vrf: <str>
    ```
