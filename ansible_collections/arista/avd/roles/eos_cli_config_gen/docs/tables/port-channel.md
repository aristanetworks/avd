<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>port_channel</samp>](## "port_channel") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;load_balance_trident</samp>](## "port_channel.load_balance_trident") | Dictionary |  |  |  | Trident chip load balancing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;udf_eth_type</samp>](## "port_channel.load_balance_trident.udf_eth_type") | Dictionary |  |  |  | Ethernet type in the port channel hash. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;header</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv4.header") | Dictionary |  |  |  | Offset starting header from the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv4.header.inner") | Dictionary |  |  |  | Inner header from the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv4.header.inner.l3") | List, items: Dictionary |  |  |  | L3 header from the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;offset</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv4.header.inner.l3.[].offset") | Integer | Required |  |  | Offset starting from selected header in the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mask</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv4.header.inner.l3.[].mask") | String |  |  |  | Mask of the offset. Range - 0x01-0xFF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l4</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv4.header.inner.l4") | List, items: Dictionary |  |  |  | L4 header from the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;offset</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv4.header.inner.l4.[].offset") | Integer | Required |  |  | Offset starting from selected header in the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mask</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv4.header.inner.l4.[].mask") | String |  |  |  | Mask of the offset. Range - 0x01-0xFF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv4.header.outer") | Dictionary |  |  |  | Outer header from the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l2</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv4.header.outer.l2") | List, items: Dictionary |  |  |  | L2 header from the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;offset</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv4.header.outer.l2.[].offset") | Integer | Required |  |  | Offset starting from selected header in the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mask</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv4.header.outer.l2.[].mask") | String |  |  |  | Mask of the offset. Range - 0x01-0xFF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv4.header.outer.l3") | List, items: Dictionary |  |  |  | L3 header from the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;offset</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv4.header.outer.l3.[].offset") | Integer | Required |  |  | Offset starting from selected header in the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mask</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv4.header.outer.l3.[].mask") | String |  |  |  | Mask of the offset. Range - 0x01-0xFF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l4</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv4.header.outer.l4") | List, items: Dictionary |  |  |  | L4 header from the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;offset</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv4.header.outer.l4.[].offset") | Integer | Required |  |  | Offset starting from selected header in the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mask</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv4.header.outer.l4.[].mask") | String |  |  |  | Mask of the offset. Range - 0x01-0xFF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;header</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv6.header") | Dictionary |  |  |  | Offset starting header from the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv6.header.inner") | Dictionary |  |  |  | Inner header from the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv6.header.inner.l3") | List, items: Dictionary |  |  |  | L3 header from the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;offset</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv6.header.inner.l3.[].offset") | Integer | Required |  |  | Offset starting from selected header in the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mask</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv6.header.inner.l3.[].mask") | String |  |  |  | Mask of the offset. Range - 0x01-0xFF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l4</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv6.header.inner.l4") | List, items: Dictionary |  |  |  | L4 header from the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;offset</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv6.header.inner.l4.[].offset") | Integer | Required |  |  | Offset starting from selected header in the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mask</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv6.header.inner.l4.[].mask") | String |  |  |  | Mask of the offset. Range - 0x01-0xFF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv6.header.outer") | Dictionary |  |  |  | Outer header from the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l2</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv6.header.outer.l2") | List, items: Dictionary |  |  |  | L2 header from the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;offset</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv6.header.outer.l2.[].offset") | Integer | Required |  |  | Offset starting from selected header in the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mask</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv6.header.outer.l2.[].mask") | String |  |  |  | Mask of the offset. Range - 0x01-0xFF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv6.header.outer.l3") | List, items: Dictionary |  |  |  | L3 header from the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;offset</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv6.header.outer.l3.[].offset") | Integer | Required |  |  | Offset starting from selected header in the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mask</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv6.header.outer.l3.[].mask") | String |  |  |  | Mask of the offset. Range - 0x01-0xFF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l4</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv6.header.outer.l4") | List, items: Dictionary |  |  |  | L4 header from the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;offset</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv6.header.outer.l4.[].offset") | Integer | Required |  |  | Offset starting from selected header in the packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mask</samp>](## "port_channel.load_balance_trident.udf_eth_type.ipv6.header.outer.l4.[].mask") | String |  |  |  | Mask of the offset. Range - 0x01-0xFF. |

=== "YAML"

    ```yaml
    port_channel:

      # Trident chip load balancing.
      load_balance_trident:

        # Ethernet type in the port channel hash.
        udf_eth_type:
          ipv4:

            # Offset starting header from the packet.
            header:

              # Inner header from the packet.
              inner:

                # L3 header from the packet.
                l3:

                    # Offset starting from selected header in the packet.
                  - offset: <int; required>

                    # Mask of the offset. Range - 0x01-0xFF.
                    mask: <str>

                # L4 header from the packet.
                l4:

                    # Offset starting from selected header in the packet.
                  - offset: <int; required>

                    # Mask of the offset. Range - 0x01-0xFF.
                    mask: <str>

              # Outer header from the packet.
              outer:

                # L2 header from the packet.
                l2:

                    # Offset starting from selected header in the packet.
                  - offset: <int; required>

                    # Mask of the offset. Range - 0x01-0xFF.
                    mask: <str>

                # L3 header from the packet.
                l3:

                    # Offset starting from selected header in the packet.
                  - offset: <int; required>

                    # Mask of the offset. Range - 0x01-0xFF.
                    mask: <str>

                # L4 header from the packet.
                l4:

                    # Offset starting from selected header in the packet.
                  - offset: <int; required>

                    # Mask of the offset. Range - 0x01-0xFF.
                    mask: <str>
          ipv6:

            # Offset starting header from the packet.
            header:

              # Inner header from the packet.
              inner:

                # L3 header from the packet.
                l3:

                    # Offset starting from selected header in the packet.
                  - offset: <int; required>

                    # Mask of the offset. Range - 0x01-0xFF.
                    mask: <str>

                # L4 header from the packet.
                l4:

                    # Offset starting from selected header in the packet.
                  - offset: <int; required>

                    # Mask of the offset. Range - 0x01-0xFF.
                    mask: <str>

              # Outer header from the packet.
              outer:

                # L2 header from the packet.
                l2:

                    # Offset starting from selected header in the packet.
                  - offset: <int; required>

                    # Mask of the offset. Range - 0x01-0xFF.
                    mask: <str>

                # L3 header from the packet.
                l3:

                    # Offset starting from selected header in the packet.
                  - offset: <int; required>

                    # Mask of the offset. Range - 0x01-0xFF.
                    mask: <str>

                # L4 header from the packet.
                l4:

                    # Offset starting from selected header in the packet.
                  - offset: <int; required>

                    # Mask of the offset. Range - 0x01-0xFF.
                    mask: <str>
    ```
