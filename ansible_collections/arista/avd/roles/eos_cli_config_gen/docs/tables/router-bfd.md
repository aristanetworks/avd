<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_bfd</samp>](## "router_bfd") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;interval</samp>](## "router_bfd.interval") | Integer |  |  |  | Rate in milliseconds |
    | [<samp>&nbsp;&nbsp;min_rx</samp>](## "router_bfd.min_rx") | Integer |  |  |  | Rate in milliseconds |
    | [<samp>&nbsp;&nbsp;multiplier</samp>](## "router_bfd.multiplier") | Integer |  |  | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;multihop</samp>](## "router_bfd.multihop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "router_bfd.multihop.interval") | Integer |  |  |  | Rate in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "router_bfd.multihop.min_rx") | Integer |  |  |  | Rate in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "router_bfd.multihop.multiplier") | Integer |  |  | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;sbfd</samp>](## "router_bfd.sbfd") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "router_bfd.sbfd.local_interface") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "router_bfd.sbfd.local_interface.name") | String |  |  |  | Interface Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocols</samp>](## "router_bfd.sbfd.local_interface.protocols") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "router_bfd.sbfd.local_interface.protocols.ipv4") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "router_bfd.sbfd.local_interface.protocols.ipv6") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;initiator_interval</samp>](## "router_bfd.sbfd.initiator_interval") | Integer |  |  |  | Rate in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;initiator_multiplier</samp>](## "router_bfd.sbfd.initiator_multiplier") | Integer |  |  | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;initiator_measurement_round_trip</samp>](## "router_bfd.sbfd.initiator_measurement_round_trip") | Boolean |  |  |  | Enable round-trip delay measurement |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;reflector</samp>](## "router_bfd.sbfd.reflector") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "router_bfd.sbfd.reflector.min_rx") | Integer |  |  |  | Rate in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_discriminator</samp>](## "router_bfd.sbfd.reflector.local_discriminator") | String |  |  |  | IPv4 address or 32 bit integer |

=== "YAML"

    ```yaml
    router_bfd:

      # Rate in milliseconds
      interval: <int>

      # Rate in milliseconds
      min_rx: <int>
      multiplier: <int; 3-50>
      multihop:

        # Rate in milliseconds
        interval: <int>

        # Rate in milliseconds
        min_rx: <int>
        multiplier: <int; 3-50>
      sbfd:
        local_interface:

          # Interface Name
          name: <str>
          protocols:
            ipv4: <bool>
            ipv6: <bool>

        # Rate in milliseconds
        initiator_interval: <int>
        initiator_multiplier: <int; 3-50>

        # Enable round-trip delay measurement
        initiator_measurement_round_trip: <bool>
        reflector:

          # Rate in milliseconds
          min_rx: <int>

          # IPv4 address or 32 bit integer
          local_discriminator: <str>
    ```
