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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "monitor_telemetry_postcard.ingress.collection.source") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "monitor_telemetry_postcard.ingress.collection.destination") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "monitor_telemetry_postcard.ingress.sample") | Dictionary |  |  |  | Configure sampling parameters |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "monitor_telemetry_postcard.ingress.sample.rate") | Integer |  |  | Valid Values:<br>- <code>16384</code><br>- <code>32768</code><br>- <code>65536</code> | Configure sampling rate |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tcp_udp_checksum</samp>](## "monitor_telemetry_postcard.ingress.sample.tcp_udp_checksum") | Integer |  |  |  | Configure TCP/UDP checksum or IP ID checksum |
    | [<samp>&nbsp;&nbsp;profile</samp>](## "monitor_telemetry_postcard.profile") | Dictionary |  |  |  | Configure the postcard telemetry profile |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "monitor_telemetry_postcard.profile.name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ingress_sample_policy</samp>](## "monitor_telemetry_postcard.profile.ingress_sample_policy") | String |  |  |  | Configure ingress parameters |
    | [<samp>&nbsp;&nbsp;sample_policy</samp>](## "monitor_telemetry_postcard.sample_policy") | Dictionary |  |  |  | Configure sampling feature |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "monitor_telemetry_postcard.sample_policy.name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;match_rule</samp>](## "monitor_telemetry_postcard.sample_policy.match_rule") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rule_name</samp>](## "monitor_telemetry_postcard.sample_policy.match_rule.rule_name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipversion</samp>](## "monitor_telemetry_postcard.sample_policy.match_rule.ipversion") | String |  |  | Valid Values:<br>- <code>ipv4</code><br>- <code>ipv6</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_prefix</samp>](## "monitor_telemetry_postcard.sample_policy.match_rule.destination_prefix") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_address</samp>](## "monitor_telemetry_postcard.sample_policy.match_rule.destination_prefix.prefix_address") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_mask</samp>](## "monitor_telemetry_postcard.sample_policy.match_rule.destination_prefix.prefix_mask") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_prefix</samp>](## "monitor_telemetry_postcard.sample_policy.match_rule.source_prefix") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_address</samp>](## "monitor_telemetry_postcard.sample_policy.match_rule.source_prefix.prefix_address") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_mask</samp>](## "monitor_telemetry_postcard.sample_policy.match_rule.source_prefix.prefix_mask") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "monitor_telemetry_postcard.sample_policy.match_rule.protocol") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type_of_protocol</samp>](## "monitor_telemetry_postcard.sample_policy.match_rule.protocol.type_of_protocol") | String |  |  | Valid Values:<br>- <code>tcp</code><br>- <code>udp</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_port</samp>](## "monitor_telemetry_postcard.sample_policy.match_rule.protocol.destination_port") | List |  |  |  | Enter the port number or range or multiple port numbers with comma seperated values.<br>Examples:<br>  "65-78"<br>  "55"<br>  "4, 55, 66"<br> |

=== "YAML"

    ```yaml
    monitor_telemetry_postcard:

      # Enable or disable the postcard telemetry feature
      disabled: <bool>

      # Configure ingress parameters
      ingress:

        # Collector configuration
        collection:
          source: <str>
          destination: <str>

        # Configure sampling parameters
        sample:

          # Configure sampling rate
          rate: <int; 16384 | 32768 | 65536>

          # Configure TCP/UDP checksum or IP ID checksum
          tcp_udp_checksum: <int>

      # Configure the postcard telemetry profile
      profile:
        name: <str>

        # Configure ingress parameters
        ingress_sample_policy: <str>

      # Configure sampling feature
      sample_policy:
        name: <str>
        match_rule:
          rule_name: <str>
          ipversion: <str; "ipv4" | "ipv6">
          destination_prefix:
            prefix_address: <str>
            prefix_mask: <int>
          source_prefix:
            prefix_address: <str>
            prefix_mask: <int>
          protocol:
            type_of_protocol: <str; "tcp" | "udp">

            # Enter the port number or range or multiple port numbers with comma seperated values.
            # Examples:
            #   "65-78"
            #   "55"
            #   "4, 55, 66"
            destination_port: <list>
    ```
