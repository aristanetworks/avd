<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>port_channel</samp>](## "port_channel") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;load_balance_trident_udf</samp>](## "port_channel.load_balance_trident_udf") | List, items: Dictionary |  |  |  | Trident chip UDF fields load balancing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;eth_type</samp>](## "port_channel.load_balance_trident_udf.[].eth_type") | String | Required |  | Valid Values:<br>- <code>ipv4</code><br>- <code>ipv6</code> | Ethernet type in the port channel hash. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_protocol</samp>](## "port_channel.load_balance_trident_udf.[].ip_protocol") | String |  |  |  | IP protocol name like - gre, icmp, tcp, udp, mpls-over-gre, sctp.<br>IP protocol number within the range <0-255>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;header</samp>](## "port_channel.load_balance_trident_udf.[].header") | String | Required |  | Valid Values:<br>- <code>inner_l3</code><br>- <code>inner_l4</code><br>- <code>outer_l2</code><br>- <code>outer_l3</code><br>- <code>outer_l4</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset</samp>](## "port_channel.load_balance_trident_udf.[].offset") | Integer | Required |  | Min: 0<br>Max: 64 | Offset starting from selected header in the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mask</samp>](## "port_channel.load_balance_trident_udf.[].mask") | String |  |  |  | Mask of the offset. A hex value within the range 0x01-0xFF. |

=== "YAML"

    ```yaml
    port_channel:

      # Trident chip UDF fields load balancing.
      load_balance_trident_udf:

          # Ethernet type in the port channel hash.
        - eth_type: <str; "ipv4" | "ipv6"; required>

          # IP protocol name like - gre, icmp, tcp, udp, mpls-over-gre, sctp.
          # IP protocol number within the range <0-255>.
          ip_protocol: <str>
          header: <str; "inner_l3" | "inner_l4" | "outer_l2" | "outer_l3" | "outer_l4"; required>

          # Offset starting from selected header in the packet.
          offset: <int; 0-64; required>

          # Mask of the offset. A hex value within the range 0x01-0xFF.
          mask: <str>
    ```
