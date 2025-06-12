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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp</samp>](## "load_balance.policies.sand_profiles.[].fields.udp") | Dictionary |  |  |  | UDP-specific fields used in the load balancing hash. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dst_port</samp>](## "load_balance.policies.sand_profiles.[].fields.udp.dst_port") | Integer | Required |  | Min: 0<br>Max: 65535 | Use the UDP destination port as a hash input. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;payload_bytes</samp>](## "load_balance.policies.sand_profiles.[].fields.udp.payload_bytes") | String |  |  |  | Specifies the number or range of UDP payload bytes to use in hash calculation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match</samp>](## "load_balance.policies.sand_profiles.[].fields.udp.match") | Dictionary |  |  |  | Configuration to match specific bits and define custom payload-based hashing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;payload_bits</samp>](## "load_balance.policies.sand_profiles.[].fields.udp.match.payload_bits") | String | Required |  |  | Bit range within the UDP payload to match for hashing (e.g., "0-15"). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pattern</samp>](## "load_balance.policies.sand_profiles.[].fields.udp.match.pattern") | Integer | Required |  |  | Bit pattern to match in the UDP payload. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_payload_bytes</samp>](## "load_balance.policies.sand_profiles.[].fields.udp.match.hash_payload_bytes") | String | Required |  |  | Number or range of UDP payload bytes to include in the hash after pattern match. |

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
              udp:

                # Use the UDP destination port as a hash input.
                dst_port: <int; 0-65535; required>

                # Specifies the number or range of UDP payload bytes to use in hash calculation.
                payload_bytes: <str>

                # Configuration to match specific bits and define custom payload-based hashing.
                match:

                  # Bit range within the UDP payload to match for hashing (e.g., "0-15").
                  payload_bits: <str; required>

                  # Bit pattern to match in the UDP payload.
                  pattern: <int; required>

                  # Number or range of UDP payload bytes to include in the hash after pattern match.
                  hash_payload_bytes: <str; required>
    ```
