<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>load_balance</samp>](## "load_balance") | Dictionary |  |  |  | Configuration for load balancing behavior across port-channels and ECMP paths. |
    | [<samp>&nbsp;&nbsp;policies</samp>](## "load_balance.policies") | Dictionary |  |  |  | Collection of load balancing policy definitions. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sand_profiles</samp>](## "load_balance.policies.sand_profiles") | List, items: Dictionary |  |  |  | List of load balancing profiles for SAND-based platforms, used for port-channel and ECMP hashing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "load_balance.policies.sand_profiles.[].name") | String | Required, Unique |  |  | Unique name of the load-balancing profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fields</samp>](## "load_balance.policies.sand_profiles.[].fields") | Dictionary |  |  |  | Configure packet fields used as input to the hash function for port-channel and ECMP load balancing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp</samp>](## "load_balance.policies.sand_profiles.[].fields.udp") | Dictionary |  |  |  | UDP-specific fields used in the load balancing hash.<br>Requires EOS version 4.33.1F or higher. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dst_port</samp>](## "load_balance.policies.sand_profiles.[].fields.udp.dst_port") | Integer | Required |  | Min: 0<br>Max: 65535 | Use the UDP destination port as a hash input. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;payload_bytes</samp>](## "load_balance.policies.sand_profiles.[].fields.udp.payload_bytes") | String |  |  |  | Specifies the UDP payload bytes to use in hash calculation.<br>Accepts single bytes (e.g., "10"), comma-separated bytes (e.g., "0,1,5"),<br>ranges (e.g., "0-15"), or combinations (e.g., "0-10,12,15,20-25").<br>Valid values are between 0 and 62. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match</samp>](## "load_balance.policies.sand_profiles.[].fields.udp.match") | Dictionary |  |  |  | Configuration to match specific bits and define custom payload-based hashing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;payload_bits</samp>](## "load_balance.policies.sand_profiles.[].fields.udp.match.payload_bits") | String | Required |  |  | Specifies the bit positions within the UDP payload to match for hashing.<br>Accepts a single bit (e.g., "12"), a comma-separated list (e.g., "0,3,8"),<br>a range (e.g., "0-15"), or combinations (e.g., "0-7,9,12-15").<br>Valid values must be in the range 0 to 503.<br>Matching is limited to a maximum of 16 bits total. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pattern</samp>](## "load_balance.policies.sand_profiles.[].fields.udp.match.pattern") | String | Required |  |  | Bit pattern to match in the UDP payload.<br>The value should be given as an hexadecimal format `0x...`.<br>The valid range is from 0 to (2^N - 1), where N is the number of bits selected in `payload_bits`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_payload_bytes</samp>](## "load_balance.policies.sand_profiles.[].fields.udp.match.hash_payload_bytes") | String | Required |  |  | Specifies the UDP payload byte positions to include in the hash after pattern match.<br>Accepts a single byte (e.g., "5"), a comma-separated list (e.g., "0,3,7"),<br>a range (e.g., "0-15"), or a combination (e.g., "0-5,8,12-14").<br>All byte positions must be within the range 0 to 62. |
    | [<samp>&nbsp;&nbsp;cluster</samp>](## "load_balance.cluster") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;destination_grouping</samp>](## "load_balance.cluster.destination_grouping") | String |  |  | Valid Values:<br>- <code>bgp field-set</code><br>- <code>prefix length</code><br>- <code>vtep</code> | Perform destination grouping using given setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;prefix_length</samp>](## "load_balance.cluster.prefix_length") | Integer |  |  | Min: 0<br>Max: 129 | Network address prefix length for destination grouping using prefix length.<br>This setting must be defined when `destination_grouping` is set to `prefix length`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;forwarding_type</samp>](## "load_balance.cluster.forwarding_type") | String |  |  | Valid Values:<br>- <code>bridged encapsulation vxlan ipv4</code><br>- <code>routed ipv4</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;load_balance_method_flow_round_robin</samp>](## "load_balance.cluster.load_balance_method_flow_round_robin") | Boolean |  |  |  | Enable round-robin load balancing for flow-based traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;flow</samp>](## "load_balance.cluster.flow") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor</samp>](## "load_balance.cluster.flow.monitor") | Boolean |  |  |  | Monitor the flows without affecting forwarding. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_learning_aging_timeout</samp>](## "load_balance.cluster.flow.source_learning_aging_timeout") | Integer |  |  | Min: 30<br>Max: 2147483647 | Flow aging timeout in seconds for flow discovery by learning. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;port_groups</samp>](## "load_balance.cluster.port_groups") | List, items: Dictionary |  |  |  | Host ports settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "load_balance.cluster.port_groups.[].group") | String | Required, Unique |  |  | Port group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;balance_factor</samp>](## "load_balance.cluster.port_groups.[].balance_factor") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "load_balance.cluster.port_groups.[].interface") | String |  |  |  | Ethernet interface/subinterface name. It could be a `,` separated list or range.<br>eg. Ethernet2,<br>    Ethernet2-5,<br>    Ethernet2.2,3.1,<br>    Ethernet3.1-2 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow</samp>](## "load_balance.cluster.port_groups.[].flow") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "load_balance.cluster.port_groups.[].flow.limit") | Integer |  |  | Min: 0<br>Max: 4294967295 | Maximum number of flows per port. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;warning</samp>](## "load_balance.cluster.port_groups.[].flow.warning") | Integer |  |  | Min: 0<br>Max: 4294967295 | Warning threshold of flows per port group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exhaustion_action</samp>](## "load_balance.cluster.port_groups.[].flow.exhaustion_action") | Dictionary |  |  |  | Forwarding action when flows reach limits. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "load_balance.cluster.port_groups.[].flow.exhaustion_action.dscp") | Integer |  |  | Min: 0<br>Max: 63 | Packet DSCP value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "load_balance.cluster.port_groups.[].flow.exhaustion_action.traffic_class") | Integer |  |  | Min: 0<br>Max: 11 | Packet traffic-class value. |

=== "YAML"

    ```yaml
    # Configuration for load balancing behavior across port-channels and ECMP paths.
    load_balance:

      # Collection of load balancing policy definitions.
      policies:

        # List of load balancing profiles for SAND-based platforms, used for port-channel and ECMP hashing.
        sand_profiles:

            # Unique name of the load-balancing profile.
          - name: <str; required; unique>

            # Configure packet fields used as input to the hash function for port-channel and ECMP load balancing.
            fields:

              # UDP-specific fields used in the load balancing hash.
              # Requires EOS version 4.33.1F or higher.
              udp:

                # Use the UDP destination port as a hash input.
                dst_port: <int; 0-65535; required>

                # Specifies the UDP payload bytes to use in hash calculation.
                # Accepts single bytes (e.g., "10"), comma-separated bytes (e.g., "0,1,5"),
                # ranges (e.g., "0-15"), or combinations (e.g., "0-10,12,15,20-25").
                # Valid values are between 0 and 62.
                payload_bytes: <str>

                # Configuration to match specific bits and define custom payload-based hashing.
                match:

                  # Specifies the bit positions within the UDP payload to match for hashing.
                  # Accepts a single bit (e.g., "12"), a comma-separated list (e.g., "0,3,8"),
                  # a range (e.g., "0-15"), or combinations (e.g., "0-7,9,12-15").
                  # Valid values must be in the range 0 to 503.
                  # Matching is limited to a maximum of 16 bits total.
                  payload_bits: <str; required>

                  # Bit pattern to match in the UDP payload.
                  # The value should be given as an hexadecimal format `0x...`.
                  # The valid range is from 0 to (2^N - 1), where N is the number of bits selected in `payload_bits`.
                  pattern: <str; required>

                  # Specifies the UDP payload byte positions to include in the hash after pattern match.
                  # Accepts a single byte (e.g., "5"), a comma-separated list (e.g., "0,3,7"),
                  # a range (e.g., "0-15"), or a combination (e.g., "0-5,8,12-14").
                  # All byte positions must be within the range 0 to 62.
                  hash_payload_bytes: <str; required>
      cluster:

        # Perform destination grouping using given setting.
        destination_grouping: <str; "bgp field-set" | "prefix length" | "vtep">

        # Network address prefix length for destination grouping using prefix length.
        # This setting must be defined when `destination_grouping` is set to `prefix length`.
        prefix_length: <int; 0-129>
        forwarding_type: <str; "bridged encapsulation vxlan ipv4" | "routed ipv4">

        # Enable round-robin load balancing for flow-based traffic.
        load_balance_method_flow_round_robin: <bool>
        flow:

          # Monitor the flows without affecting forwarding.
          monitor: <bool>

          # Flow aging timeout in seconds for flow discovery by learning.
          source_learning_aging_timeout: <int; 30-2147483647>

        # Host ports settings.
        port_groups:

            # Port group name.
          - group: <str; required; unique>
            balance_factor: <int; 0-4294967295>

            # Ethernet interface/subinterface name. It could be a `,` separated list or range.
            # eg. Ethernet2,
            #     Ethernet2-5,
            #     Ethernet2.2,3.1,
            #     Ethernet3.1-2
            interface: <str>
            flow:

              # Maximum number of flows per port.
              limit: <int; 0-4294967295>

              # Warning threshold of flows per port group.
              warning: <int; 0-4294967295>

              # Forwarding action when flows reach limits.
              exhaustion_action:

                # Packet DSCP value.
                dscp: <int; 0-63>

                # Packet traffic-class value.
                traffic_class: <int; 0-11>
    ```
