<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>monitor_telemetry_postcard</samp>](## "monitor_telemetry_postcard") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;disabled</samp>](## "monitor_telemetry_postcard.disabled") | Boolean |  |  |  | Enable or disable the postcard telemetry feature |
    | [<samp>&nbsp;&nbsp;ingress</samp>](## "monitor_telemetry_postcard.ingress") | Dictionary |  |  |  | Configure ingress parameters |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;collection</samp>](## "monitor_telemetry_postcard.ingress.collection") | Dictionary |  |  |  | Collector configuration |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "monitor_telemetry_postcard.ingress.collection.source") | String |  |  |  | GRE source configuration |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "monitor_telemetry_postcard.ingress.collection.destination") | String |  |  |  | GRE destination configuration |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "monitor_telemetry_postcard.ingress.collection.version") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | Postcard version |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "monitor_telemetry_postcard.ingress.sample") | Dictionary |  |  |  | Configure sampling parameters |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "monitor_telemetry_postcard.ingress.sample.rate") | Integer |  |  | Valid Values:<br>- <code>16384</code><br>- <code>32768</code><br>- <code>65536</code> | Configure sampling rate |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tcp_udp_checksum</samp>](## "monitor_telemetry_postcard.ingress.sample.tcp_udp_checksum") | Integer |  |  |  | Configure TCP/UDP checksum or IP ID checksum |
    | [<samp>&nbsp;&nbsp;profiles</samp>](## "monitor_telemetry_postcard.profiles") | List, items: Dictionary |  |  |  | Configure the postcard telemetry profile |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_telemetry_postcard.profiles.[].name") | String | Required, Unique |  |  | Profile name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ingress_sample_policy</samp>](## "monitor_telemetry_postcard.profiles.[].ingress_sample_policy") | String |  |  |  | Configure ingress parameters |
    | [<samp>&nbsp;&nbsp;sample_policies</samp>](## "monitor_telemetry_postcard.sample_policies") | List, items: Dictionary |  |  |  | Configure sample policies |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_telemetry_postcard.sample_policies.[].name") | String | Required, Unique |  |  | Configure sample policy name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_rules</samp>](## "monitor_telemetry_postcard.sample_policies.[].match_rules") | List, items: Dictionary |  |  |  | Configure match rules |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;rule_name</samp>](## "monitor_telemetry_postcard.sample_policies.[].match_rules.[].rule_name") | String | Required, Unique |  |  | Match rule name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "monitor_telemetry_postcard.sample_policies.[].match_rules.[].type") | String |  |  | Valid Values:<br>- <code>ipv4</code><br>- <code>ipv6</code> | Select the IP version |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_prefix</samp>](## "monitor_telemetry_postcard.sample_policies.[].match_rules.[].destination_prefix") | String |  |  |  | IPv4 Network/Mask or IPv6 Network/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_prefix</samp>](## "monitor_telemetry_postcard.sample_policies.[].match_rules.[].source_prefix") | String |  |  |  | IPv4 Network/Mask or IPv6 Network/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "monitor_telemetry_postcard.sample_policies.[].match_rules.[].protocol") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol_type</samp>](## "monitor_telemetry_postcard.sample_policies.[].match_rules.[].protocol.protocol_type") | String |  |  | Valid Values:<br>- <code>tcp</code><br>- <code>udp</code> | Select TCP/UDP |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_port</samp>](## "monitor_telemetry_postcard.sample_policies.[].match_rules.[].protocol.destination_port") | List |  |  |  | Enter the port name or range or  port numbers in a list.<br>Example:<br>  ["12","14-20", "www"]<br> |

=== "YAML"

    ```yaml
    monitor_telemetry_postcard:

      # Enable or disable the postcard telemetry feature
      disabled: <bool>

      # Configure ingress parameters
      ingress:

        # Collector configuration
        collection:

          # GRE source configuration
          source: <str>

          # GRE destination configuration
          destination: <str>

          # Postcard version
          version: <int; 1 | 2>

        # Configure sampling parameters
        sample:

          # Configure sampling rate
          rate: <int; 16384 | 32768 | 65536>

          # Configure TCP/UDP checksum or IP ID checksum
          tcp_udp_checksum: <int>

      # Configure the postcard telemetry profile
      profiles:

          # Profile name
        - name: <str; required; unique>

          # Configure ingress parameters
          ingress_sample_policy: <str>

      # Configure sample policies
      sample_policies:

          # Configure sample policy name
        - name: <str; required; unique>

          # Configure match rules
          match_rules:

              # Match rule name
            - rule_name: <str; required; unique>

              # Select the IP version
              type: <str; "ipv4" | "ipv6">

              # IPv4 Network/Mask or IPv6 Network/Mask
              destination_prefix: <str>

              # IPv4 Network/Mask or IPv6 Network/Mask
              source_prefix: <str>
              protocol:

                # Select TCP/UDP
                protocol_type: <str; "tcp" | "udp">

                # Enter the port name or range or  port numbers in a list.
                # Example:
                #   ["12","14-20", "www"]
                destination_port: <list>
    ```
