<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>core_interfaces</samp>](## "core_interfaces") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;p2p_links_ip_pools</samp>](## "core_interfaces.p2p_links_ip_pools") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "core_interfaces.p2p_links_ip_pools.[].name") | String | Required, Unique |  |  | P2P pool name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_pool</samp>](## "core_interfaces.p2p_links_ip_pools.[].ipv4_pool") | String |  |  |  | IPv4 address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_size</samp>](## "core_interfaces.p2p_links_ip_pools.[].prefix_size") | Integer |  | `31` | Min: 8<br>Max: 31 | Subnet mask size. |
    | [<samp>&nbsp;&nbsp;p2p_links_profiles</samp>](## "core_interfaces.p2p_links_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "core_interfaces.p2p_links_profiles.[].name") | String | Required, Unique |  |  | P2P profile name. Any variable supported under p2p_links can be inherited from a profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "core_interfaces.p2p_links_profiles.[].id") | Integer |  |  |  | Unique id per subnet_summary. Used to calculate ip addresses.<br>Required with ip_pool. ID starting from 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "core_interfaces.p2p_links_profiles.[].speed") | String |  |  |  | The values can be speed or auto speed or forced speed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_pool</samp>](## "core_interfaces.p2p_links_profiles.[].ip_pool") | String |  |  |  | P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subnet</samp>](## "core_interfaces.p2p_links_profiles.[].subnet") | String |  |  |  | IPv4 address/Mask. Subnet used on this P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "core_interfaces.p2p_links_profiles.[].ip") | List, items: String |  |  |  | Specific IP addresses used on this P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links_profiles.[].ip.[].&lt;str&gt;") | String |  |  |  | Node IPv4 address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "core_interfaces.p2p_links_profiles.[].ipv6_enable") | Boolean |  | `False` |  | Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and include_in_underlay_protocol). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "core_interfaces.p2p_links_profiles.[].nodes") | List, items: String |  |  |  | Nodes where this link should be configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links_profiles.[].nodes.[].&lt;str&gt;") | String |  |  |  | The values can be < node_a >, < node_b >.<br>ex.- [ core-1-isis-sr-ldp, core-2-ospf-ldp ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "core_interfaces.p2p_links_profiles.[].interfaces") | List, items: String |  |  |  | Interfaces where this link should be configured and Required unless using port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links_profiles.[].interfaces.[].&lt;str&gt;") | String |  |  |  | The value can be like < node_a_interface >, < node_b_interface >.<br>ex. - [ Ethernet2, Ethernet2 ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as</samp>](## "core_interfaces.p2p_links_profiles.[].as") | List, items: String |  |  |  | AS numbers for BGP.<br>Required with bgp peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links_profiles.[].as.[].&lt;str&gt;") | String |  |  |  | The values can be like ["node_a_as", "node_b_as"]. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;descriptions</samp>](## "core_interfaces.p2p_links_profiles.[].descriptions") | List, items: String |  |  |  | Interface description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links_profiles.[].descriptions.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_in_underlay_protocol</samp>](## "core_interfaces.p2p_links_profiles.[].include_in_underlay_protocol") | Boolean |  | `True` |  | Add this interface to underlay routing protocol. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "core_interfaces.p2p_links_profiles.[].isis_hello_padding") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "core_interfaces.p2p_links_profiles.[].isis_metric") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "core_interfaces.p2p_links_profiles.[].isis_circuit_type") | String |  |  | Valid Values:<br>- level-1<br>- level-2<br>- level-1-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "core_interfaces.p2p_links_profiles.[].isis_authentication_mode") | String |  |  | Valid Values:<br>- md5<br>- text |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "core_interfaces.p2p_links_profiles.[].isis_authentication_key") | String |  |  |  | Type-7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ip</samp>](## "core_interfaces.p2p_links_profiles.[].mpls_ip") | Boolean |  |  |  | MPLS parameters. Default value is true if switch.mpls_lsr is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ldp</samp>](## "core_interfaces.p2p_links_profiles.[].mpls_ldp") | Boolean |  |  |  | MPLS parameters. Default value is true for ldp underlay variants, otherwise false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "core_interfaces.p2p_links_profiles.[].mtu") | Integer |  |  |  | MTU for this P2P link. Default value same as p2p_uplinks_mtu. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "core_interfaces.p2p_links_profiles.[].bfd") | Boolean |  | `False` |  | Enable BFD (only considered for BGP). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "core_interfaces.p2p_links_profiles.[].ptp") | Dictionary |  |  |  | PTP parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "core_interfaces.p2p_links_profiles.[].ptp.enabled") | Boolean |  | `False` |  | Enable PTP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sflow</samp>](## "core_interfaces.p2p_links_profiles.[].sflow") | Boolean |  |  |  | Enable sFlow. Overrides `fabric_sflow` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "core_interfaces.p2p_links_profiles.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;macsec_profile</samp>](## "core_interfaces.p2p_links_profiles.[].macsec_profile") | String |  |  |  | MAC security profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "core_interfaces.p2p_links_profiles.[].port_channel") | Dictionary |  |  |  | Port-channel parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "core_interfaces.p2p_links_profiles.[].port_channel.mode") | String |  | `active` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes_child_interfaces</samp>](## "core_interfaces.p2p_links_profiles.[].port_channel.nodes_child_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- node</samp>](## "core_interfaces.p2p_links_profiles.[].port_channel.nodes_child_interfaces.[].node") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "core_interfaces.p2p_links_profiles.[].port_channel.nodes_child_interfaces.[].interfaces") | List, items: String |  |  |  | List of node interfaces. Ex.- [ 'node1 interface1', 'node1 interface2' ]. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links_profiles.[].port_channel.nodes_child_interfaces.[].interfaces.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "core_interfaces.p2p_links_profiles.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the point-to-point interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "core_interfaces.p2p_links_profiles.[].structured_config") | Dictionary |  |  |  | Custom structured config for interfaces<br>Note! The content of this dictionary is _not_ validated by the schema, since it can be either ethernet_interfaces or port_channel_interfaces. |
    | [<samp>&nbsp;&nbsp;p2p_links</samp>](## "core_interfaces.p2p_links") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- nodes</samp>](## "core_interfaces.p2p_links.[].nodes") | List, items: String | Required |  |  | Nodes where this link should be configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].nodes.[].&lt;str&gt;") | String |  |  |  | The values can be < node_a >, < node_b >.<br>ex.- [ core-1-isis-sr-ldp, core-2-ospf-ldp ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "core_interfaces.p2p_links.[].profile") | String |  |  |  | P2P profile name. Profile defined under p2p_profiles. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "core_interfaces.p2p_links.[].id") | Integer |  |  |  | Unique id per subnet_summary. Used to calculate ip addresses.<br>Required with ip_pool. ID starting from 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "core_interfaces.p2p_links.[].speed") | String |  |  |  | The values can be speed or auto speed or forced speed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_pool</samp>](## "core_interfaces.p2p_links.[].ip_pool") | String |  |  |  | P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subnet</samp>](## "core_interfaces.p2p_links.[].subnet") | String |  |  |  | IPv4 address/Mask. Subnet used on this P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "core_interfaces.p2p_links.[].ip") | List, items: String |  |  |  | Specific IP addresses used on this P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].ip.[].&lt;str&gt;") | String |  |  |  | Node IPv4 address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "core_interfaces.p2p_links.[].ipv6_enable") | Boolean |  | `False` |  | Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and include_in_underlay_protocol). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "core_interfaces.p2p_links.[].interfaces") | List, items: String |  |  |  | Interfaces where this link should be configured and Required unless using port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].interfaces.[].&lt;str&gt;") | String |  |  |  | The value can be like < node_a_interface >, < node_b_interface >.<br>ex. - [ Ethernet2, Ethernet2 ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as</samp>](## "core_interfaces.p2p_links.[].as") | List, items: String |  |  |  | AS numbers for BGP.<br>Required with bgp peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].as.[].&lt;str&gt;") | String |  |  |  | The values can be like ["node_a_as", "node_b_as"]. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;descriptions</samp>](## "core_interfaces.p2p_links.[].descriptions") | List, items: String |  |  |  | Interface description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].descriptions.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_in_underlay_protocol</samp>](## "core_interfaces.p2p_links.[].include_in_underlay_protocol") | Boolean |  | `True` |  | Add this interface to underlay routing protocol. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "core_interfaces.p2p_links.[].isis_hello_padding") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "core_interfaces.p2p_links.[].isis_metric") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "core_interfaces.p2p_links.[].isis_circuit_type") | String |  |  | Valid Values:<br>- level-1<br>- level-2<br>- level-1-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "core_interfaces.p2p_links.[].isis_authentication_mode") | String |  |  | Valid Values:<br>- md5<br>- text |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "core_interfaces.p2p_links.[].isis_authentication_key") | String |  |  |  | Type-7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ip</samp>](## "core_interfaces.p2p_links.[].mpls_ip") | Boolean |  |  |  | MPLS parameters. Default value is true if switch.mpls_lsr is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ldp</samp>](## "core_interfaces.p2p_links.[].mpls_ldp") | Boolean |  |  |  | MPLS parameters. Default value is true for ldp underlay variants, otherwise false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "core_interfaces.p2p_links.[].mtu") | Integer |  |  |  | MTU for this P2P link. Default value same as p2p_uplinks_mtu. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "core_interfaces.p2p_links.[].bfd") | Boolean |  | `False` |  | Enable BFD (only considered for BGP). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "core_interfaces.p2p_links.[].ptp") | Dictionary |  |  |  | PTP parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "core_interfaces.p2p_links.[].ptp.enabled") | Boolean |  | `False` |  | Enable PTP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sflow</samp>](## "core_interfaces.p2p_links.[].sflow") | Boolean |  |  |  | Enable sFlow. Overrides `fabric_sflow` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "core_interfaces.p2p_links.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;macsec_profile</samp>](## "core_interfaces.p2p_links.[].macsec_profile") | String |  |  |  | MAC security profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "core_interfaces.p2p_links.[].port_channel") | Dictionary |  |  |  | Port-channel parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "core_interfaces.p2p_links.[].port_channel.mode") | String |  | `active` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes_child_interfaces</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- node</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces.[].node") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces.[].interfaces") | List, items: String |  |  |  | List of node interfaces. Ex.- [ 'node1 interface1', 'node1 interface2' ]. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces.[].interfaces.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "core_interfaces.p2p_links.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the point-to-point interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "core_interfaces.p2p_links.[].structured_config") | Dictionary |  |  |  | Custom structured config for interfaces<br>Note! The content of this dictionary is _not_ validated by the schema, since it can be either ethernet_interfaces or port_channel_interfaces. |

=== "YAML"

    ```yaml
    core_interfaces:
      p2p_links_ip_pools:
        - name: <str>
          ipv4_pool: <str>
          prefix_size: <int>
      p2p_links_profiles:
        - name: <str>
          id: <int>
          speed: <str>
          ip_pool: <str>
          subnet: <str>
          ip:
            - <str>
          ipv6_enable: <bool>
          nodes:
            - <str>
          interfaces:
            - <str>
          as:
            - <str>
          descriptions:
            - <str>
          include_in_underlay_protocol: <bool>
          isis_hello_padding: <bool>
          isis_metric: <int>
          isis_circuit_type: <str>
          isis_authentication_mode: <str>
          isis_authentication_key: <str>
          mpls_ip: <bool>
          mpls_ldp: <bool>
          mtu: <int>
          bfd: <bool>
          ptp:
            enabled: <bool>
          sflow: <bool>
          qos_profile: <str>
          macsec_profile: <str>
          port_channel:
            mode: <str>
            nodes_child_interfaces:
              - node: <str>
                interfaces:
                  - <str>
          raw_eos_cli: <str>
          structured_config: <dict>
      p2p_links:
        - nodes:
            - <str>
          profile: <str>
          id: <int>
          speed: <str>
          ip_pool: <str>
          subnet: <str>
          ip:
            - <str>
          ipv6_enable: <bool>
          interfaces:
            - <str>
          as:
            - <str>
          descriptions:
            - <str>
          include_in_underlay_protocol: <bool>
          isis_hello_padding: <bool>
          isis_metric: <int>
          isis_circuit_type: <str>
          isis_authentication_mode: <str>
          isis_authentication_key: <str>
          mpls_ip: <bool>
          mpls_ldp: <bool>
          mtu: <int>
          bfd: <bool>
          ptp:
            enabled: <bool>
          sflow: <bool>
          qos_profile: <str>
          macsec_profile: <str>
          port_channel:
            mode: <str>
            nodes_child_interfaces:
              - node: <str>
                interfaces:
                  - <str>
          raw_eos_cli: <str>
          structured_config: <dict>
    ```
