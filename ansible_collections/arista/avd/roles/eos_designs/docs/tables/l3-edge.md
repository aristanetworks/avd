<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>l3_edge</samp>](## "l3_edge") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;p2p_links_ip_pools</samp>](## "l3_edge.p2p_links_ip_pools") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "l3_edge.p2p_links_ip_pools.[].name") | String | Required, Unique |  |  | P2P pool name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_pool</samp>](## "l3_edge.p2p_links_ip_pools.[].ipv4_pool") | String |  |  |  | IPv4 address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_size</samp>](## "l3_edge.p2p_links_ip_pools.[].prefix_size") | Integer |  | `31` | Min: 8<br>Max: 31 | Subnet mask size. |
    | [<samp>&nbsp;&nbsp;p2p_links_profiles</samp>](## "l3_edge.p2p_links_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "l3_edge.p2p_links_profiles.[].name") | String | Required, Unique |  |  | P2P profile name. Any variable supported under p2p_links can be inherited from a profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "l3_edge.p2p_links_profiles.[].id") | Integer |  |  |  | Unique id per subnet_summary. Used to calculate ip addresses.<br>Required with ip_pool. ID starting from 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "l3_edge.p2p_links_profiles.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_pool</samp>](## "l3_edge.p2p_links_profiles.[].ip_pool") | String |  |  |  | P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subnet</samp>](## "l3_edge.p2p_links_profiles.[].subnet") | String |  |  |  | IPv4 address/Mask. Subnet used on this P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "l3_edge.p2p_links_profiles.[].ip") | List, items: String |  |  |  | Specific IP addresses used on this P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "l3_edge.p2p_links_profiles.[].ip.[]") | String |  |  |  | Node IPv4 address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "l3_edge.p2p_links_profiles.[].ipv6_enable") | Boolean |  | `False` |  | Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and include_in_underlay_protocol). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "l3_edge.p2p_links_profiles.[].nodes") | List, items: String |  |  |  | Nodes where this link should be configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "l3_edge.p2p_links_profiles.[].nodes.[]") | String |  |  |  | The values can be < node_a >, < node_b >.<br>ex.- [ core-1-isis-sr-ldp, core-2-ospf-ldp ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "l3_edge.p2p_links_profiles.[].interfaces") | List, items: String |  |  |  | Interfaces where this link should be configured and Required unless using port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "l3_edge.p2p_links_profiles.[].interfaces.[]") | String |  |  |  | The value can be like < node_a_interface >, < node_b_interface >.<br>ex. - [ Ethernet2, Ethernet2 ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as</samp>](## "l3_edge.p2p_links_profiles.[].as") | List, items: String |  |  |  | AS numbers for BGP.<br>Required with bgp peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "l3_edge.p2p_links_profiles.[].as.[]") | String |  |  |  | The values can be like ["node_a_as", "node_b_as"]. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;descriptions</samp>](## "l3_edge.p2p_links_profiles.[].descriptions") | List, items: String |  |  |  | Interface description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "l3_edge.p2p_links_profiles.[].descriptions.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_in_underlay_protocol</samp>](## "l3_edge.p2p_links_profiles.[].include_in_underlay_protocol") | Boolean |  | `True` |  | Add this interface to underlay routing protocol. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "l3_edge.p2p_links_profiles.[].isis_hello_padding") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "l3_edge.p2p_links_profiles.[].isis_metric") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "l3_edge.p2p_links_profiles.[].isis_circuit_type") | String |  |  | Valid Values:<br>- <code>level-1</code><br>- <code>level-2</code><br>- <code>level-1-2</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "l3_edge.p2p_links_profiles.[].isis_authentication_mode") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>text</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "l3_edge.p2p_links_profiles.[].isis_authentication_key") | String |  |  |  | Type-7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ip</samp>](## "l3_edge.p2p_links_profiles.[].mpls_ip") | Boolean |  |  |  | MPLS parameters. Default value is true if switch.mpls_lsr is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ldp</samp>](## "l3_edge.p2p_links_profiles.[].mpls_ldp") | Boolean |  |  |  | MPLS parameters. Default value is true for ldp underlay variants, otherwise false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "l3_edge.p2p_links_profiles.[].mtu") | Integer |  |  |  | MTU for this P2P link. Default value same as p2p_uplinks_mtu. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "l3_edge.p2p_links_profiles.[].bfd") | Boolean |  | `False` |  | Enable BFD (only considered for BGP). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "l3_edge.p2p_links_profiles.[].ptp") | Dictionary |  |  |  | PTP parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "l3_edge.p2p_links_profiles.[].ptp.enabled") | Boolean |  | `False` |  | Enable PTP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sflow</samp>](## "l3_edge.p2p_links_profiles.[].sflow") | Boolean |  |  |  | Enable sFlow. Overrides `fabric_sflow` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "l3_edge.p2p_links_profiles.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;macsec_profile</samp>](## "l3_edge.p2p_links_profiles.[].macsec_profile") | String |  |  |  | MAC security profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "l3_edge.p2p_links_profiles.[].port_channel") | Dictionary |  |  |  | Port-channel parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "l3_edge.p2p_links_profiles.[].port_channel.mode") | String |  | `active` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes_child_interfaces</samp>](## "l3_edge.p2p_links_profiles.[].port_channel.nodes_child_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;node</samp>](## "l3_edge.p2p_links_profiles.[].port_channel.nodes_child_interfaces.[].node") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "l3_edge.p2p_links_profiles.[].port_channel.nodes_child_interfaces.[].interfaces") | List, items: String |  |  |  | List of node interfaces. Ex.- [ 'node1 interface1', 'node1 interface2' ]. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "l3_edge.p2p_links_profiles.[].port_channel.nodes_child_interfaces.[].interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "l3_edge.p2p_links_profiles.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the point-to-point interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "l3_edge.p2p_links_profiles.[].structured_config") | Dictionary |  |  |  | Custom structured config for interfaces<br>Note! The content of this dictionary is _not_ validated by the schema, since it can be either ethernet_interfaces or port_channel_interfaces. |
    | [<samp>&nbsp;&nbsp;p2p_links</samp>](## "l3_edge.p2p_links") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;nodes</samp>](## "l3_edge.p2p_links.[].nodes") | List, items: String | Required |  |  | Nodes where this link should be configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "l3_edge.p2p_links.[].nodes.[]") | String |  |  |  | The values can be < node_a >, < node_b >.<br>ex.- [ core-1-isis-sr-ldp, core-2-ospf-ldp ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "l3_edge.p2p_links.[].profile") | String |  |  |  | P2P profile name. Profile defined under p2p_profiles. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "l3_edge.p2p_links.[].id") | Integer |  |  |  | Unique id per subnet_summary. Used to calculate ip addresses.<br>Required with ip_pool. ID starting from 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "l3_edge.p2p_links.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_pool</samp>](## "l3_edge.p2p_links.[].ip_pool") | String |  |  |  | P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subnet</samp>](## "l3_edge.p2p_links.[].subnet") | String |  |  |  | IPv4 address/Mask. Subnet used on this P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "l3_edge.p2p_links.[].ip") | List, items: String |  |  |  | Specific IP addresses used on this P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "l3_edge.p2p_links.[].ip.[]") | String |  |  |  | Node IPv4 address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "l3_edge.p2p_links.[].ipv6_enable") | Boolean |  | `False` |  | Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and include_in_underlay_protocol). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "l3_edge.p2p_links.[].interfaces") | List, items: String |  |  |  | Interfaces where this link should be configured and Required unless using port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "l3_edge.p2p_links.[].interfaces.[]") | String |  |  |  | The value can be like < node_a_interface >, < node_b_interface >.<br>ex. - [ Ethernet2, Ethernet2 ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as</samp>](## "l3_edge.p2p_links.[].as") | List, items: String |  |  |  | AS numbers for BGP.<br>Required with bgp peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "l3_edge.p2p_links.[].as.[]") | String |  |  |  | The values can be like ["node_a_as", "node_b_as"]. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;descriptions</samp>](## "l3_edge.p2p_links.[].descriptions") | List, items: String |  |  |  | Interface description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "l3_edge.p2p_links.[].descriptions.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_in_underlay_protocol</samp>](## "l3_edge.p2p_links.[].include_in_underlay_protocol") | Boolean |  | `True` |  | Add this interface to underlay routing protocol. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "l3_edge.p2p_links.[].isis_hello_padding") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "l3_edge.p2p_links.[].isis_metric") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "l3_edge.p2p_links.[].isis_circuit_type") | String |  |  | Valid Values:<br>- <code>level-1</code><br>- <code>level-2</code><br>- <code>level-1-2</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "l3_edge.p2p_links.[].isis_authentication_mode") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>text</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "l3_edge.p2p_links.[].isis_authentication_key") | String |  |  |  | Type-7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ip</samp>](## "l3_edge.p2p_links.[].mpls_ip") | Boolean |  |  |  | MPLS parameters. Default value is true if switch.mpls_lsr is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ldp</samp>](## "l3_edge.p2p_links.[].mpls_ldp") | Boolean |  |  |  | MPLS parameters. Default value is true for ldp underlay variants, otherwise false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "l3_edge.p2p_links.[].mtu") | Integer |  |  |  | MTU for this P2P link. Default value same as p2p_uplinks_mtu. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "l3_edge.p2p_links.[].bfd") | Boolean |  | `False` |  | Enable BFD (only considered for BGP). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "l3_edge.p2p_links.[].ptp") | Dictionary |  |  |  | PTP parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "l3_edge.p2p_links.[].ptp.enabled") | Boolean |  | `False` |  | Enable PTP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sflow</samp>](## "l3_edge.p2p_links.[].sflow") | Boolean |  |  |  | Enable sFlow. Overrides `fabric_sflow` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "l3_edge.p2p_links.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;macsec_profile</samp>](## "l3_edge.p2p_links.[].macsec_profile") | String |  |  |  | MAC security profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "l3_edge.p2p_links.[].port_channel") | Dictionary |  |  |  | Port-channel parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "l3_edge.p2p_links.[].port_channel.mode") | String |  | `active` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes_child_interfaces</samp>](## "l3_edge.p2p_links.[].port_channel.nodes_child_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;node</samp>](## "l3_edge.p2p_links.[].port_channel.nodes_child_interfaces.[].node") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "l3_edge.p2p_links.[].port_channel.nodes_child_interfaces.[].interfaces") | List, items: String |  |  |  | List of node interfaces. Ex.- [ 'node1 interface1', 'node1 interface2' ]. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "l3_edge.p2p_links.[].port_channel.nodes_child_interfaces.[].interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "l3_edge.p2p_links.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the point-to-point interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "l3_edge.p2p_links.[].structured_config") | Dictionary |  |  |  | Custom structured config for interfaces<br>Note! The content of this dictionary is _not_ validated by the schema, since it can be either ethernet_interfaces or port_channel_interfaces. |

=== "YAML"

    ```yaml
    l3_edge:
      p2p_links_ip_pools:

          # P2P pool name.
        - name: <str; required; unique>

          # IPv4 address/Mask.
          ipv4_pool: <str>

          # Subnet mask size.
          prefix_size: <int; 8-31; default=31>
      p2p_links_profiles:

          # P2P profile name. Any variable supported under p2p_links can be inherited from a profile.
        - name: <str; required; unique>

          # Unique id per subnet_summary. Used to calculate ip addresses.
          # Required with ip_pool. ID starting from 1.
          id: <int>

          # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
          speed: <str>

          # P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link.
          ip_pool: <str>

          # IPv4 address/Mask. Subnet used on this P2P link.
          subnet: <str>

          # Specific IP addresses used on this P2P link.
          ip:

              # Node IPv4 address/Mask.
            - <str>

          # Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and include_in_underlay_protocol).
          ipv6_enable: <bool; default=False>

          # Nodes where this link should be configured.
          nodes:

              # The values can be < node_a >, < node_b >.
              # ex.- [ core-1-isis-sr-ldp, core-2-ospf-ldp ].
            - <str>

          # Interfaces where this link should be configured and Required unless using port-channels.
          interfaces:

              # The value can be like < node_a_interface >, < node_b_interface >.
              # ex. - [ Ethernet2, Ethernet2 ].
            - <str>

          # AS numbers for BGP.
          # Required with bgp peering.
          as:

              # The values can be like ["node_a_as", "node_b_as"].
            - <str>

          # Interface description.
          descriptions:
            - <str>

          # Add this interface to underlay routing protocol.
          include_in_underlay_protocol: <bool; default=True>
          isis_hello_padding: <bool; default=False>
          isis_metric: <int>
          isis_circuit_type: <str; "level-1" | "level-2" | "level-1-2">
          isis_authentication_mode: <str; "md5" | "text">

          # Type-7 encrypted password.
          isis_authentication_key: <str>

          # MPLS parameters. Default value is true if switch.mpls_lsr is true.
          mpls_ip: <bool>

          # MPLS parameters. Default value is true for ldp underlay variants, otherwise false.
          mpls_ldp: <bool>

          # MTU for this P2P link. Default value same as p2p_uplinks_mtu.
          mtu: <int>

          # Enable BFD (only considered for BGP).
          bfd: <bool; default=False>

          # PTP parameters.
          ptp:

            # Enable PTP.
            enabled: <bool; default=False>

          # Enable sFlow. Overrides `fabric_sflow` setting.
          sflow: <bool>

          # QOS service profile.
          qos_profile: <str>

          # MAC security profile.
          macsec_profile: <str>

          # Port-channel parameters.
          port_channel:
            mode: <str; default="active">
            nodes_child_interfaces:
              - node: <str; required; unique>

                # List of node interfaces. Ex.- [ 'node1 interface1', 'node1 interface2' ].
                interfaces:
                  - <str>

          # EOS CLI rendered directly on the point-to-point interface in the final EOS configuration.
          raw_eos_cli: <str>

          # Custom structured config for interfaces
          # Note! The content of this dictionary is _not_ validated by the schema, since it can be either ethernet_interfaces or port_channel_interfaces.
          structured_config: <dict>
      p2p_links:

          # Nodes where this link should be configured.
        - nodes: # required

              # The values can be < node_a >, < node_b >.
              # ex.- [ core-1-isis-sr-ldp, core-2-ospf-ldp ].
            - <str>

          # P2P profile name. Profile defined under p2p_profiles.
          profile: <str>

          # Unique id per subnet_summary. Used to calculate ip addresses.
          # Required with ip_pool. ID starting from 1.
          id: <int>

          # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
          speed: <str>

          # P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link.
          ip_pool: <str>

          # IPv4 address/Mask. Subnet used on this P2P link.
          subnet: <str>

          # Specific IP addresses used on this P2P link.
          ip:

              # Node IPv4 address/Mask.
            - <str>

          # Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and include_in_underlay_protocol).
          ipv6_enable: <bool; default=False>

          # Interfaces where this link should be configured and Required unless using port-channels.
          interfaces:

              # The value can be like < node_a_interface >, < node_b_interface >.
              # ex. - [ Ethernet2, Ethernet2 ].
            - <str>

          # AS numbers for BGP.
          # Required with bgp peering.
          as:

              # The values can be like ["node_a_as", "node_b_as"].
            - <str>

          # Interface description.
          descriptions:
            - <str>

          # Add this interface to underlay routing protocol.
          include_in_underlay_protocol: <bool; default=True>
          isis_hello_padding: <bool; default=False>
          isis_metric: <int>
          isis_circuit_type: <str; "level-1" | "level-2" | "level-1-2">
          isis_authentication_mode: <str; "md5" | "text">

          # Type-7 encrypted password.
          isis_authentication_key: <str>

          # MPLS parameters. Default value is true if switch.mpls_lsr is true.
          mpls_ip: <bool>

          # MPLS parameters. Default value is true for ldp underlay variants, otherwise false.
          mpls_ldp: <bool>

          # MTU for this P2P link. Default value same as p2p_uplinks_mtu.
          mtu: <int>

          # Enable BFD (only considered for BGP).
          bfd: <bool; default=False>

          # PTP parameters.
          ptp:

            # Enable PTP.
            enabled: <bool; default=False>

          # Enable sFlow. Overrides `fabric_sflow` setting.
          sflow: <bool>

          # QOS service profile.
          qos_profile: <str>

          # MAC security profile.
          macsec_profile: <str>

          # Port-channel parameters.
          port_channel:
            mode: <str; default="active">
            nodes_child_interfaces:
              - node: <str; required; unique>

                # List of node interfaces. Ex.- [ 'node1 interface1', 'node1 interface2' ].
                interfaces:
                  - <str>

          # EOS CLI rendered directly on the point-to-point interface in the final EOS configuration.
          raw_eos_cli: <str>

          # Custom structured config for interfaces
          # Note! The content of this dictionary is _not_ validated by the schema, since it can be either ethernet_interfaces or port_channel_interfaces.
          structured_config: <dict>
    ```
