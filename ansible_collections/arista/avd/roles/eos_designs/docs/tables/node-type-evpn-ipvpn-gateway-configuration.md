<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway") | Dictionary |  |  |  | Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".<br>L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.evpn_domain_id") | String |  | `65535:1` |  | Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.ipvpn_domain_id") | String |  | `65535:2` |  | Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.enable_d_path") | Boolean |  | `True` |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.maximum_routes") | Integer |  | `0` |  | Maximum routes to accept from IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.local_as") | String |  | `none` |  | Apply local-as to peering with IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.address_families") | List, items: String |  | `['vpn-ipv4']` |  | IPVPN address families to enable for remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.address_families.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.remote_peers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.remote_peers.[].hostname") | String | Required |  |  | Hostname of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.remote_peers.[].ip_address") | String | Required |  | Format: ipv4 | Peering IP of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.remote_peers.[].bgp_as") | String | Required |  |  | BGP ASN of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- group</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway") | Dictionary |  |  |  | Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".<br>L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.evpn_domain_id") | String |  | `65535:1` |  | Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.ipvpn_domain_id") | String |  | `65535:2` |  | Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.enable_d_path") | Boolean |  | `True` |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.maximum_routes") | Integer |  | `0` |  | Maximum routes to accept from IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.local_as") | String |  | `none` |  | Apply local-as to peering with IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.address_families") | List, items: String |  | `['vpn-ipv4']` |  | IPVPN address families to enable for remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.address_families.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.remote_peers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.remote_peers.[].hostname") | String | Required |  |  | Hostname of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.remote_peers.[].ip_address") | String | Required |  | Format: ipv4 | Peering IP of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.remote_peers.[].bgp_as") | String | Required |  |  | BGP ASN of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway") | Dictionary |  |  |  | Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".<br>L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.evpn_domain_id") | String |  | `65535:1` |  | Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.ipvpn_domain_id") | String |  | `65535:2` |  | Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.enable_d_path") | Boolean |  | `True` |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.maximum_routes") | Integer |  | `0` |  | Maximum routes to accept from IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.local_as") | String |  | `none` |  | Apply local-as to peering with IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.address_families") | List, items: String |  | `['vpn-ipv4']` |  | IPVPN address families to enable for remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.address_families.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.remote_peers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.remote_peers.[].hostname") | String | Required |  |  | Hostname of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.remote_peers.[].ip_address") | String | Required |  | Format: ipv4 | Peering IP of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.remote_peers.[].bgp_as") | String | Required |  |  | BGP ASN of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway") | Dictionary |  |  |  | Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".<br>L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.evpn_domain_id") | String |  | `65535:1` |  | Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.ipvpn_domain_id") | String |  | `65535:2` |  | Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.enable_d_path") | Boolean |  | `True` |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.maximum_routes") | Integer |  | `0` |  | Maximum routes to accept from IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.local_as") | String |  | `none` |  | Apply local-as to peering with IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.address_families") | List, items: String |  | `['vpn-ipv4']` |  | IPVPN address families to enable for remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.address_families.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.remote_peers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.remote_peers.[].hostname") | String | Required |  |  | Hostname of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.remote_peers.[].ip_address") | String | Required |  | Format: ipv4 | Peering IP of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.remote_peers.[].bgp_as") | String | Required |  |  | BGP ASN of remote IPVPN Peer. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
        ipvpn_gateway:
          enabled: <bool>
          evpn_domain_id: <str>
          ipvpn_domain_id: <str>
          enable_d_path: <bool>
          maximum_routes: <int>
          local_as: <str>
          address_families:
            - <str>
          remote_peers:
            - hostname: <str>
              ip_address: <str>
              bgp_as: <str>
      node_groups:
        - group: <str>
          nodes:
            - name: <str>
              ipvpn_gateway:
                enabled: <bool>
                evpn_domain_id: <str>
                ipvpn_domain_id: <str>
                enable_d_path: <bool>
                maximum_routes: <int>
                local_as: <str>
                address_families:
                  - <str>
                remote_peers:
                  - hostname: <str>
                    ip_address: <str>
                    bgp_as: <str>
          ipvpn_gateway:
            enabled: <bool>
            evpn_domain_id: <str>
            ipvpn_domain_id: <str>
            enable_d_path: <bool>
            maximum_routes: <int>
            local_as: <str>
            address_families:
              - <str>
            remote_peers:
              - hostname: <str>
                ip_address: <str>
                bgp_as: <str>
      nodes:
        - name: <str>
          ipvpn_gateway:
            enabled: <bool>
            evpn_domain_id: <str>
            ipvpn_domain_id: <str>
            enable_d_path: <bool>
            maximum_routes: <int>
            local_as: <str>
            address_families:
              - <str>
            remote_peers:
              - hostname: <str>
                ip_address: <str>
                bgp_as: <str>
    ```
