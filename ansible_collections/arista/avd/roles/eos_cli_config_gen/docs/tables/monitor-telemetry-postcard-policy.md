<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>monitor_telemetry_postcard_policy</samp>](## "monitor_telemetry_postcard_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;disabled</samp>](## "monitor_telemetry_postcard_policy.disabled") | Boolean |  |  |  | Enable or disable the postcard telemetry feature. |
    | [<samp>&nbsp;&nbsp;ingress</samp>](## "monitor_telemetry_postcard_policy.ingress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;collection</samp>](## "monitor_telemetry_postcard_policy.ingress.collection") | Dictionary |  |  |  | Collector configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "monitor_telemetry_postcard_policy.ingress.collection.source") | String |  |  |  | Configure source IP address of GRE tunnel. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "monitor_telemetry_postcard_policy.ingress.collection.destination") | String |  |  |  | Configure destination IP address of GRE tunnel. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "monitor_telemetry_postcard_policy.ingress.collection.version") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | Postcard version |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "monitor_telemetry_postcard_policy.ingress.sample") | Dictionary |  |  |  | Sampling parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "monitor_telemetry_postcard_policy.ingress.sample.rate") | Integer |  |  | Valid Values:<br>- <code>16384</code><br>- <code>32768</code><br>- <code>65536</code> | Sampling rate. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tcp_udp_checksum</samp>](## "monitor_telemetry_postcard_policy.ingress.sample.tcp_udp_checksum") | Integer |  |  | Min: 0<br>Max: 65535 | TCP/UDP checksum or IP ID value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mask</samp>](## "monitor_telemetry_postcard_policy.ingress.sample.mask") | String |  |  |  | 16 bit hexadecimal mask for TCP/UDP or IP ID with atmost 2 unser bits. |
    | [<samp>&nbsp;&nbsp;vxlan_marking_bit</samp>](## "monitor_telemetry_postcard_policy.vxlan_marking_bit") | Integer |  | `0` | Min: 0<br>Max: 31 |  |
    | [<samp>&nbsp;&nbsp;profiles</samp>](## "monitor_telemetry_postcard_policy.profiles") | List, items: Dictionary |  |  |  | Postcard telemetry profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_telemetry_postcard_policy.profiles.[].name") | String | Required, Unique |  |  | Profile name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ingress_sample_policy</samp>](## "monitor_telemetry_postcard_policy.profiles.[].ingress_sample_policy") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;sample_policies</samp>](## "monitor_telemetry_postcard_policy.sample_policies") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_rules</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].match_rules") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].type") | String |  |  | Valid Values:<br>- <code>ipv4</code><br>- <code>ipv6</code> | IP address version. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_prefix</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].destination_prefix") | String |  |  |  | IPv4 Network/Mask or IPv6 Network/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_prefix</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].source_prefix") | String |  |  |  | IPv4 Network/Mask or IPv6 Network/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ports</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].ports") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;protocol</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].ports.[].protocol") | String | Required, Unique |  | Valid Values:<br>- <code>tcp</code><br>- <code>udp</code> | TCP/UDP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_ports</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].ports.[].destination_ports") | List |  |  |  | Enter the port name or range or port numbers in a list.<br>Example:<br>  ["12","14-20", "www"] |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ports</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].ports.[].source_ports") | List |  |  |  | Enter the port name or range or port numbers in a list.<br>Example:<br>  ["12","14-20", "www"] |

=== "YAML"

    ```yaml
    monitor_telemetry_postcard_policy:

      # Enable or disable the postcard telemetry feature.
      disabled: <bool>
      ingress:

        # Collector configuration.
        collection:

          # Configure source IP address of GRE tunnel.
          source: <str>

          # Configure destination IP address of GRE tunnel.
          destination: <str>

          # Postcard version
          version: <int; 1 | 2>

        # Sampling parameters.
        sample:

          # Sampling rate.
          rate: <int; 16384 | 32768 | 65536>

          # TCP/UDP checksum or IP ID value.
          tcp_udp_checksum: <int; 0-65535>

          # 16 bit hexadecimal mask for TCP/UDP or IP ID with atmost 2 unser bits.
          mask: <str>
      vxlan_marking_bit: <int; 0-31; default=0>

      # Postcard telemetry profile.
      profiles:

          # Profile name
        - name: <str; required; unique>
          ingress_sample_policy: <str>
      sample_policies:
        - name: <str; required; unique>
          match_rules:
            - name: <str; required; unique>

              # IP address version.
              type: <str; "ipv4" | "ipv6">

              # IPv4 Network/Mask or IPv6 Network/Mask.
              destination_prefix: <str>

              # IPv4 Network/Mask or IPv6 Network/Mask.
              source_prefix: <str>
              ports:

                  # TCP/UDP.
                - protocol: <str; "tcp" | "udp"; required; unique>

                  # Enter the port name or range or port numbers in a list.
                  # Example:
                  #   ["12","14-20", "www"]
                  destination_ports: <list>

                  # Enter the port name or range or port numbers in a list.
                  # Example:
                  #   ["12","14-20", "www"]
                  source_ports: <list>
    ```
