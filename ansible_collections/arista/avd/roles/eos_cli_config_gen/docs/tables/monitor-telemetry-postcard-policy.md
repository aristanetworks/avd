<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>monitor_telemetry_postcard_policy</samp>](## "monitor_telemetry_postcard_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;disabled</samp>](## "monitor_telemetry_postcard_policy.disabled") | Boolean |  | `True` |  | Enable or disable the postcard telemetry feature. |
    | [<samp>&nbsp;&nbsp;ingress</samp>](## "monitor_telemetry_postcard_policy.ingress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;collection</samp>](## "monitor_telemetry_postcard_policy.ingress.collection") | Dictionary |  |  |  | Collector configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "monitor_telemetry_postcard_policy.ingress.collection.source") | String |  |  |  | Source IP address of GRE tunnel. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "monitor_telemetry_postcard_policy.ingress.collection.destination") | String |  |  |  | Destination IP address of GRE tunnel. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "monitor_telemetry_postcard_policy.ingress.collection.version") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | Postcard version. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "monitor_telemetry_postcard_policy.ingress.sample") | Dictionary |  |  |  | Sampling parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "monitor_telemetry_postcard_policy.ingress.sample.rate") | Integer |  |  | Valid Values:<br>- <code>16384</code><br>- <code>32768</code><br>- <code>65536</code> | Sampling rate. `rate` is preferred when both `rate` and `tcp_udp_checksum` are defined. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tcp_udp_checksum</samp>](## "monitor_telemetry_postcard_policy.ingress.sample.tcp_udp_checksum") | Dictionary |  |  |  | TCP/UDP parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "monitor_telemetry_postcard_policy.ingress.sample.tcp_udp_checksum.value") | Integer |  |  | Min: 0<br>Max: 65535 | TCP/UDP checksum or IP ID value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mask</samp>](## "monitor_telemetry_postcard_policy.ingress.sample.tcp_udp_checksum.mask") | String |  |  |  | 16 bit hexadecimal mask for TCP/UDP or IP ID with atmost 2 unset bits. |
    | [<samp>&nbsp;&nbsp;marker_vxlan</samp>](## "monitor_telemetry_postcard_policy.marker_vxlan") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "monitor_telemetry_postcard_policy.marker_vxlan.enabled") | Boolean |  |  |  | Enable vxlan marking using default bit 0. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;header_word_zero_bit</samp>](## "monitor_telemetry_postcard_policy.marker_vxlan.header_word_zero_bit") | Integer |  |  | Min: 1<br>Max: 31 |  |
    | [<samp>&nbsp;&nbsp;profiles</samp>](## "monitor_telemetry_postcard_policy.profiles") | List, items: Dictionary |  |  |  | Postcard telemetry profiles. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_telemetry_postcard_policy.profiles.[].name") | String | Required, Unique |  |  | Profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ingress_sample_policy</samp>](## "monitor_telemetry_postcard_policy.profiles.[].ingress_sample_policy") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;sample_policies</samp>](## "monitor_telemetry_postcard_policy.sample_policies") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_rules</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].match_rules") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].type") | String | Required |  | Valid Values:<br>- <code>ipv4</code><br>- <code>ipv6</code> | IP address version. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_prefix</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].destination_prefix") | String |  |  |  | IPv4 Network/Mask or IPv6 Network/Mask. Host part of prefix must be zero.<br>eg. 10.3.3.0/24 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_prefix</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].source_prefix") | String |  |  |  | IPv4 Network/Mask or IPv6 Network/Mask. Host part of prefix must be zero.<br>eg. 10.3.3.0/24 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocols</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].protocols") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;protocol</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].protocols.[].protocol") | String | Required, Unique |  | Valid Values:<br>- <code>tcp</code><br>- <code>udp</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ports</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].protocols.[].source_ports") | List, items: String |  |  |  | A list of port numbers or port range or port name. Combination of port numbers or range and port name is not supported on EOS. The port numbers should be in range of 0-65535.<br>e.g.<br>  [ "12", "14-20" ]<br>  [ "www" ] |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].protocols.[].source_ports.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_ports</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].protocols.[].destination_ports") | List, items: String |  |  |  | A list of port numbers or port range or port name. Combination of port numbers or range and port name is not supported on EOS. The port numbers should be in range of 0-65535.<br>e.g.<br>  [ "12", "14-20", "80" ]<br>  [ "https" ] |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].protocols.[].destination_ports.[]") | String |  |  |  |  |

=== "YAML"

    ```yaml
    monitor_telemetry_postcard_policy:

      # Enable or disable the postcard telemetry feature.
      disabled: <bool; default=True>
      ingress:

        # Collector configuration.
        collection:

          # Source IP address of GRE tunnel.
          source: <str>

          # Destination IP address of GRE tunnel.
          destination: <str>

          # Postcard version.
          version: <int; 1 | 2>

        # Sampling parameters.
        sample:

          # Sampling rate. `rate` is preferred when both `rate` and `tcp_udp_checksum` are defined.
          rate: <int; 16384 | 32768 | 65536>

          # TCP/UDP parameters.
          tcp_udp_checksum:

            # TCP/UDP checksum or IP ID value.
            value: <int; 0-65535>

            # 16 bit hexadecimal mask for TCP/UDP or IP ID with atmost 2 unset bits.
            mask: <str>
      marker_vxlan:

        # Enable vxlan marking using default bit 0.
        enabled: <bool>
        header_word_zero_bit: <int; 1-31>

      # Postcard telemetry profiles.
      profiles:

          # Profile name.
        - name: <str; required; unique>
          ingress_sample_policy: <str>
      sample_policies:
        - name: <str; required; unique>
          match_rules:
            - name: <str; required; unique>

              # IP address version.
              type: <str; "ipv4" | "ipv6"; required>

              # IPv4 Network/Mask or IPv6 Network/Mask. Host part of prefix must be zero.
              # eg. 10.3.3.0/24
              destination_prefix: <str>

              # IPv4 Network/Mask or IPv6 Network/Mask. Host part of prefix must be zero.
              # eg. 10.3.3.0/24
              source_prefix: <str>
              protocols:
                - protocol: <str; "tcp" | "udp"; required; unique>

                  # A list of port numbers or port range or port name. Combination of port numbers or range and port name is not supported on EOS. The port numbers should be in range of 0-65535.
                  # e.g.
                  #   [ "12", "14-20" ]
                  #   [ "www" ]
                  source_ports:
                    - <str>

                  # A list of port numbers or port range or port name. Combination of port numbers or range and port name is not supported on EOS. The port numbers should be in range of 0-65535.
                  # e.g.
                  #   [ "12", "14-20", "80" ]
                  #   [ "https" ]
                  destination_ports:
                    - <str>
    ```
