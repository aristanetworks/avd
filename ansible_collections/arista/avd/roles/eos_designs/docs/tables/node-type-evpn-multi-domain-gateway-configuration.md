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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway.<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.<br>Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.remote_peers.[].hostname") | String |  |  |  | Hostname of remote EVPN GW server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | BGP ASN of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.evpn_l2.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.evpn_l3.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.evpn_l3.inter_domain") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- group</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway.<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.<br>Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.remote_peers.[].hostname") | String |  |  |  | Hostname of remote EVPN GW server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | BGP ASN of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.evpn_l2.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.evpn_l3.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.evpn_l3.inter_domain") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway.<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.<br>Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.remote_peers.[].hostname") | String |  |  |  | Hostname of remote EVPN GW server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | BGP ASN of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.evpn_l2.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.evpn_l3.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.evpn_l3.inter_domain") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway.<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.<br>Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.remote_peers.[].hostname") | String |  |  |  | Hostname of remote EVPN GW server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | BGP ASN of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.evpn_l2.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.evpn_l3.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.evpn_l3.inter_domain") | Boolean |  | `True` |  |  |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
        evpn_gateway:
          remote_peers:
            - hostname: <str>
              ip_address: <str>
              bgp_as: <str>
          evpn_l2:
            enabled: <bool>
          evpn_l3:
            enabled: <bool>
            inter_domain: <bool>
      node_groups:
        - group: <str>
          nodes:
            - name: <str>
              evpn_gateway:
                remote_peers:
                  - hostname: <str>
                    ip_address: <str>
                    bgp_as: <str>
                evpn_l2:
                  enabled: <bool>
                evpn_l3:
                  enabled: <bool>
                  inter_domain: <bool>
          evpn_gateway:
            remote_peers:
              - hostname: <str>
                ip_address: <str>
                bgp_as: <str>
            evpn_l2:
              enabled: <bool>
            evpn_l3:
              enabled: <bool>
              inter_domain: <bool>
      nodes:
        - name: <str>
          evpn_gateway:
            remote_peers:
              - hostname: <str>
                ip_address: <str>
                bgp_as: <str>
            evpn_l2:
              enabled: <bool>
            evpn_l3:
              enabled: <bool>
              inter_domain: <bool>
    ```
