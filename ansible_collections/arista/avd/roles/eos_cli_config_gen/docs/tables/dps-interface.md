<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dps_interface</samp>](## "dps_interface") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;Dps1</samp>](## "dps_interface.Dps1") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "dps_interface.Dps1.description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "dps_interface.Dps1.ip_address") | String |  |  |  | IPv4 address/mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;flow_tracker</samp>](## "dps_interface.Dps1.flow_tracker") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sampled</samp>](## "dps_interface.Dps1.flow_tracker.sampled") | String |  |  |  | Sampled flow tracker name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware</samp>](## "dps_interface.Dps1.flow_tracker.hardware") | String |  |  |  | Hardware flow tracker name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tcp_mss_ceiling</samp>](## "dps_interface.Dps1.tcp_mss_ceiling") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "dps_interface.Dps1.tcp_mss_ceiling.ipv4") | Integer |  |  | Min: 64<br>Max: 65495 | Segment Size for IPv4 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "dps_interface.Dps1.tcp_mss_ceiling.ipv6") | Integer |  |  | Min: 64<br>Max: 65475 | Segment Size for IPv6 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "dps_interface.Dps1.tcp_mss_ceiling.direction") | String |  |  | Valid Values:<br>- ingress<br>- egress | Optional direction ('ingress', 'egress')  for tcp mss ceiling<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "dps_interface.Dps1.eos_cli") | String |  |  |  | Multiline String with EOS CLI rendered directly on the Dps interface in the final EOS configuration. |

=== "YAML"

    ```yaml
    dps_interface:
      Dps1:
        description: <str>
        ip_address: <str>
        flow_tracker:
          sampled: <str>
          hardware: <str>
        tcp_mss_ceiling:
          ipv4: <int>
          ipv6: <int>
          direction: <str>
        eos_cli: <str>
    ```
