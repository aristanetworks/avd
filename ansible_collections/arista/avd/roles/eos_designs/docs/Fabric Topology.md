---
search:
  boost: 2
---

# Fabric Topology

## <Node Type Keys.Key>

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- group</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
      node_groups:
        - group: <str>
          nodes:
            - name: <str>
      nodes:
        - name: <str>
    ```

## Bgp & Evpn Control Plane

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.defaults.bgp_as") | String |  |  |  | Required with eBGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults.bgp_defaults") | List, items: String |  |  |  | List of EOS commands to apply to BGP daemon. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.bgp_defaults.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_role</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Acting role in EVPN control plane. Default is set in node_type definition from node_type_keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_route_servers</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_route_servers") | List, items: String |  |  |  | List of nodes acting as EVPN Route-Servers / Route-Reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_route_servers.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].bgp_as") | String |  |  |  | Required with eBGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_defaults</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].bgp_defaults") | List, items: String |  |  |  | List of EOS commands to apply to BGP daemon. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].bgp_defaults.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_role</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Acting role in EVPN control plane. Default is set in node_type definition from node_type_keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_route_servers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_route_servers") | List, items: String |  |  |  | List of nodes acting as EVPN Route-Servers / Route-Reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_route_servers.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].bgp_as") | String |  |  |  | Required with eBGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_defaults</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].bgp_defaults") | List, items: String |  |  |  | List of EOS commands to apply to BGP daemon. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].bgp_defaults.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_role</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Acting role in EVPN control plane. Default is set in node_type definition from node_type_keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_route_servers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_route_servers") | List, items: String |  |  |  | List of nodes acting as EVPN Route-Servers / Route-Reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_route_servers.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- bgp_as</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].bgp_as") | String |  |  |  | Required with eBGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_defaults</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].bgp_defaults") | List, items: String |  |  |  | List of EOS commands to apply to BGP daemon. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].bgp_defaults.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_role</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Acting role in EVPN control plane. Default is set in node_type definition from node_type_keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_route_servers</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_route_servers") | List, items: String |  |  |  | List of nodes acting as EVPN Route-Servers / Route-Reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_route_servers.[].&lt;str&gt;") | String |  |  |  |  |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
        bgp_as: <str>
        bgp_defaults:
          - <str>
        evpn_role: <str>
        evpn_route_servers:
          - <str>
      node_groups:
        - bgp_as: <str>
          bgp_defaults:
            - <str>
          evpn_role: <str>
          evpn_route_servers:
            - <str>
          nodes:
            - bgp_as: <str>
              bgp_defaults:
                - <str>
              evpn_role: <str>
              evpn_route_servers:
                - <str>
      nodes:
        - bgp_as: <str>
          bgp_defaults:
            - <str>
          evpn_role: <str>
          evpn_route_servers:
            - <str>
    ```

## Bgp & Evpn Multi-Domain Gateway

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway.<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.<br>Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.remote_peers.[].hostname") | String |  |  |  | Hostname of remote EVPN GW server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | BGP ASN of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.evpn_l2.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.evpn_l3.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.evpn_l3.inter_domain") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- evpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway.<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.<br>Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.remote_peers.[].hostname") | String |  |  |  | Hostname of remote EVPN GW server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | BGP ASN of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.evpn_l2.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.evpn_l3.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.evpn_l3.inter_domain") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- evpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway.<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.<br>Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.remote_peers.[].hostname") | String |  |  |  | Hostname of remote EVPN GW server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | BGP ASN of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.evpn_l2.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.evpn_l3.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.evpn_l3.inter_domain") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- evpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway.<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.<br>Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.remote_peers.[].hostname") | String |  |  |  | Hostname of remote EVPN GW server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | BGP ASN of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.evpn_l2.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.evpn_l3.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.evpn_l3.inter_domain") | Boolean |  | True |  |  |

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
        - evpn_gateway:
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
            - evpn_gateway:
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
        - evpn_gateway:
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

## Bgp & Ip-Vpn Gateway

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway") | Dictionary |  |  |  | Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".<br>L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.evpn_domain_id") | String |  | 0:1 |  | Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.ipvpn_domain_id") | String |  | 0:2 |  | Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.enable_d_path") | Boolean |  | True |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.maximum_routes") | Integer |  | 0 |  | Maximum routes to accept from IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.local_as") | String |  | none |  | Apply local-as to peering with IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.address_families") | List, items: String |  | ['vpn-ipv4'] |  | IPVPN address families to enable for remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.address_families.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.remote_peers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.remote_peers.[].hostname") | String | Required |  |  | Hostname of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.remote_peers.[].ip_address") | String | Required |  | Format: ipv4 | Peering IP of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.remote_peers.[].bgp_as") | String | Required |  |  | BGP ASN of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- ipvpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway") | Dictionary |  |  |  | Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".<br>L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.evpn_domain_id") | String |  | 0:1 |  | Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.ipvpn_domain_id") | String |  | 0:2 |  | Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.enable_d_path") | Boolean |  | True |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.maximum_routes") | Integer |  | 0 |  | Maximum routes to accept from IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.local_as") | String |  | none |  | Apply local-as to peering with IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.address_families") | List, items: String |  | ['vpn-ipv4'] |  | IPVPN address families to enable for remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.address_families.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.remote_peers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.remote_peers.[].hostname") | String | Required |  |  | Hostname of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.remote_peers.[].ip_address") | String | Required |  | Format: ipv4 | Peering IP of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.remote_peers.[].bgp_as") | String | Required |  |  | BGP ASN of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ipvpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway") | Dictionary |  |  |  | Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".<br>L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.evpn_domain_id") | String |  | 0:1 |  | Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.ipvpn_domain_id") | String |  | 0:2 |  | Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.enable_d_path") | Boolean |  | True |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.maximum_routes") | Integer |  | 0 |  | Maximum routes to accept from IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.local_as") | String |  | none |  | Apply local-as to peering with IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.address_families") | List, items: String |  | ['vpn-ipv4'] |  | IPVPN address families to enable for remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.address_families.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.remote_peers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.remote_peers.[].hostname") | String | Required |  |  | Hostname of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.remote_peers.[].ip_address") | String | Required |  | Format: ipv4 | Peering IP of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.remote_peers.[].bgp_as") | String | Required |  |  | BGP ASN of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- ipvpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway") | Dictionary |  |  |  | Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".<br>L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.evpn_domain_id") | String |  | 0:1 |  | Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.ipvpn_domain_id") | String |  | 0:2 |  | Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.enable_d_path") | Boolean |  | True |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.maximum_routes") | Integer |  | 0 |  | Maximum routes to accept from IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.local_as") | String |  | none |  | Apply local-as to peering with IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.address_families") | List, items: String |  | ['vpn-ipv4'] |  | IPVPN address families to enable for remote peers. |
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
        - ipvpn_gateway:
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
            - ipvpn_gateway:
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
        - ipvpn_gateway:
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

## Default Interfaces

- Set default uplink, downlink, and MLAG interfaces, which will be used if these interfaces are not defined on a device (either directly or through inheritance).
- These are defined based on the combination of node_type (e.g., l3leaf or spine) and a regex for matching the platform.
- A list of interfaces or interface ranges can be specified.
- Each list item supports range syntax that can be expanded into a list of interfaces. Interface range examples:
  - Ethernet49-52/1: Expands to [ Ethernet49/1, Ethernet50/1, Ethernet51/1, Ethernet52/1 ]
  - Ethernet1/31-34/1: Expands to [ Ethernet1/31/1, Ethernet1/32/1, Ethernet1/33/1, Ethernet1/34/1 ]
  - Ethernet49-50,53-54: Expands to [ Ethernet49, Ethernet50, Ethernet53, Ethernet54 ]
  - Ethernet1-2/1-4: Expands to [ Ethernet1/1, Ethernet1/2, Ethernet1/3, Ethernet1/4, Ethernet2/1, Ethernet2/2, Ethernet2/3, Ethernet2/4 ]
- `uplink_interfaces` and `mlag_interfaces` under `default_interfaces` are directly inherited by `uplink_interfaces` and `mlag_interfaces`.
- `downlink_interfaces` are referenced by the child switch (e.g., the leaf in a leaf/spine network). The child switch leverages an upstream switch's `default_downlink_interfaces` using the child switch ID.  This is then used to build `uplink_switch_interfaces` for that child.
  - In the case of `max_parallel_uplinks` > 1 the `default_downlink_interfaces` are mapped with consecutive downlinks per child ID.
  - Example for `max_parallel_uplinks: 2`, downlink interfaces will be mapped as `[ <downlink1 to leaf-id1>, <downlink2 to leaf-id1>, <downlink1 to leaf-id2>, <downlink2 to leaf-id2> ...]`
- Please note that no default interfaces are defined in AVD itself. You will need to create your own based on the example below.

Example:

```yaml
default_interfaces:
  - types: [ spine, l3leaf ]
    platforms: [ "7050[SC]X3", vEOS.*, default ]
    uplink_interfaces: [ Ethernet49-54/1 ]
    mlag_interfaces: [ Ethernet55-56/1 ]
    downlink_interfaces: [ Ethernet1-32/1 ]
```

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_interfaces</samp>](## "default_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- types</samp>](## "default_interfaces.[].types") | List, items: String | Required |  |  | List of node type keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_interfaces.[].types.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;platforms</samp>](## "default_interfaces.[].platforms") | List, items: String | Required |  |  | List of platform families.<br>This is defined as a Python regular expression that matches the full platform type.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_interfaces.[].platforms.[].&lt;str&gt;") | String |  |  |  | Arista platform family regular expression. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "default_interfaces.[].uplink_interfaces") | List, items: String |  |  |  | List of uplink interfaces or uplink interface ranges. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_interfaces.[].uplink_interfaces.[].&lt;str&gt;") | String |  |  |  | Interface range or interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "default_interfaces.[].mlag_interfaces") | List, items: String |  |  |  | List of MLAG interfaces or MLAG interface ranges. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_interfaces.[].mlag_interfaces.[].&lt;str&gt;") | String |  |  |  | Interface range or interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;downlink_interfaces</samp>](## "default_interfaces.[].downlink_interfaces") | List, items: String |  |  |  | List of downlink interfaces or downlink interface ranges. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_interfaces.[].downlink_interfaces.[].&lt;str&gt;") | String |  |  |  | Interface range or interface. |

=== "YAML"

    ```yaml
    default_interfaces:
      - types:
          - <str>
        platforms:
          - <str>
        uplink_interfaces:
          - <str>
        mlag_interfaces:
          - <str>
        downlink_interfaces:
          - <str>
    ```

## Design Variables

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>design</samp>](## "design") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;type</samp>](## "design.type") | String |  | l3ls-evpn | Valid Values:<br>- l3ls-evpn<br>- mpls<br>- l2ls | By setting the design.type variable, the default node-types and templates described in these documents will be used.<br> |

=== "YAML"

    ```yaml
    design:
      type: <str>
    ```

## Evpn Services Management

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_services_l2_only</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_services_l2_only") | Boolean |  | False |  | Possibility to prevent configuration of Tenant VRFs and SVIs.<br>Override node definition "network_services_l3" from node_type_keys.<br>This allows support for centralized routing.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter") | Dictionary |  |  |  | Filter L3 and L2 network services based on tenant and tags (and operation filter).<br>If filter is not defined it will default to all.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.tenants") | List, items: String |  | ['all'] |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.tags") | List, items: String |  | ['all'] |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.tags.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_include_vrfs_in_tenants</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.always_include_vrfs_in_tenants") | List, items: String |  |  |  | List of tenants where VRFs will be configured even if VLANs are not included in tags<br>Useful for L3 "border" leaf.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.always_include_vrfs_in_tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;only_vlans_in_use</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.only_vlans_in_use") | Boolean |  | False |  | Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.<br>Note! This feature only considers configuration managed by eos_designs.<br>This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.igmp_snooping_enabled") | Boolean |  | True |  | Activate or deactivate IGMP snooping on device level. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- evpn_services_l2_only</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_services_l2_only") | Boolean |  | False |  | Possibility to prevent configuration of Tenant VRFs and SVIs.<br>Override node definition "network_services_l3" from node_type_keys.<br>This allows support for centralized routing.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter") | Dictionary |  |  |  | Filter L3 and L2 network services based on tenant and tags (and operation filter).<br>If filter is not defined it will default to all.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.tenants") | List, items: String |  | ['all'] |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.tags") | List, items: String |  | ['all'] |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.tags.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_include_vrfs_in_tenants</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.always_include_vrfs_in_tenants") | List, items: String |  |  |  | List of tenants where VRFs will be configured even if VLANs are not included in tags<br>Useful for L3 "border" leaf.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.always_include_vrfs_in_tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;only_vlans_in_use</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.only_vlans_in_use") | Boolean |  | False |  | Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.<br>Note! This feature only considers configuration managed by eos_designs.<br>This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].igmp_snooping_enabled") | Boolean |  | True |  | Activate or deactivate IGMP snooping on device level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- evpn_services_l2_only</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_services_l2_only") | Boolean |  | False |  | Possibility to prevent configuration of Tenant VRFs and SVIs.<br>Override node definition "network_services_l3" from node_type_keys.<br>This allows support for centralized routing.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter") | Dictionary |  |  |  | Filter L3 and L2 network services based on tenant and tags (and operation filter).<br>If filter is not defined it will default to all.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.tenants") | List, items: String |  | ['all'] |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.tags") | List, items: String |  | ['all'] |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.tags.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_include_vrfs_in_tenants</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.always_include_vrfs_in_tenants") | List, items: String |  |  |  | List of tenants where VRFs will be configured even if VLANs are not included in tags<br>Useful for L3 "border" leaf.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.always_include_vrfs_in_tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;only_vlans_in_use</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.only_vlans_in_use") | Boolean |  | False |  | Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.<br>Note! This feature only considers configuration managed by eos_designs.<br>This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].igmp_snooping_enabled") | Boolean |  | True |  | Activate or deactivate IGMP snooping on device level. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- evpn_services_l2_only</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_services_l2_only") | Boolean |  | False |  | Possibility to prevent configuration of Tenant VRFs and SVIs.<br>Override node definition "network_services_l3" from node_type_keys.<br>This allows support for centralized routing.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter") | Dictionary |  |  |  | Filter L3 and L2 network services based on tenant and tags (and operation filter).<br>If filter is not defined it will default to all.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.tenants") | List, items: String |  | ['all'] |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.tags") | List, items: String |  | ['all'] |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.tags.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_include_vrfs_in_tenants</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.always_include_vrfs_in_tenants") | List, items: String |  |  |  | List of tenants where VRFs will be configured even if VLANs are not included in tags<br>Useful for L3 "border" leaf.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.always_include_vrfs_in_tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;only_vlans_in_use</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.only_vlans_in_use") | Boolean |  | False |  | Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.<br>Note! This feature only considers configuration managed by eos_designs.<br>This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].igmp_snooping_enabled") | Boolean |  | True |  | Activate or deactivate IGMP snooping on device level. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
        evpn_services_l2_only: <bool>
        filter:
          tenants:
            - <str>
          tags:
            - <str>
          always_include_vrfs_in_tenants:
            - <str>
          only_vlans_in_use: <bool>
        igmp_snooping_enabled: <bool>
      node_groups:
        - evpn_services_l2_only: <bool>
          filter:
            tenants:
              - <str>
            tags:
              - <str>
            always_include_vrfs_in_tenants:
              - <str>
            only_vlans_in_use: <bool>
          igmp_snooping_enabled: <bool>
          nodes:
            - evpn_services_l2_only: <bool>
              filter:
                tenants:
                  - <str>
                tags:
                  - <str>
                always_include_vrfs_in_tenants:
                  - <str>
                only_vlans_in_use: <bool>
              igmp_snooping_enabled: <bool>
      nodes:
        - evpn_services_l2_only: <bool>
          filter:
            tenants:
              - <str>
            tags:
              - <str>
            always_include_vrfs_in_tenants:
              - <str>
            only_vlans_in_use: <bool>
          igmp_snooping_enabled: <bool>
    ```

## Generic Configuration Management

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "&lt;node_type_keys.key&gt;.defaults.id") | Integer |  |  |  | Unique identifier used for IP addressing and other algorithms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "&lt;node_type_keys.key&gt;.defaults.platform") | String |  |  |  | Arista platform family. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "&lt;node_type_keys.key&gt;.defaults.mac_address") | String |  |  |  | Leverage to document management interface mac address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "&lt;node_type_keys.key&gt;.defaults.system_mac_address") | String |  |  |  | System MAC Address in this following format: "xx:xx:xx:xx:xx:xx".<br>Set to the same MAC address as available in "show version" on the device.<br>"system_mac_address" can also be set directly as a hostvar.<br>If both are set, the setting under "Fabric Topology" takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "&lt;node_type_keys.key&gt;.defaults.serial_number") | String |  |  |  | Set to the Serial Number of the device<br>For  now only used for documentation purpose in the fabric documentation<br>and part of the structured_config<br>"serial_number" can also be set directly as a hostvar.<br>If both are set, the setting under "Fabric Topology" takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "&lt;node_type_keys.key&gt;.defaults.rack") | String |  |  |  | Rack that the switch is located in (only used in snmp_settings location). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.defaults.mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipv6_mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv6 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "&lt;node_type_keys.key&gt;.defaults.mgmt_interface") | String |  |  |  | Management Interface Name.<br>Default -> platform_management_interface -> mgmt_interface -> "Management1".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking") | Dictionary |  |  |  | This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream interfaces.<br>Useful in EVPN multhoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking.groups") | List, items: Dictionary |  | [{'name': 'LT_GROUP1'}] |  | Link Tracking Groups.<br>By default a single group named "LT_GROUP1" is defined with default values.<br>Any groups defined under "groups" will replace the default.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking.groups.[].name") | String |  |  |  | Tracking group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking.groups.[].recovery_delay") | Integer |  |  | Min: 0<br>Max: 3600 | default -> platform_settings_mlag_reload_delay -> 300. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;links_minimum</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking.groups.[].links_minimum") | Integer |  |  | Min: 1<br>Max: 100000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_port_id_range</samp>](## "&lt;node_type_keys.key&gt;.defaults.lacp_port_id_range") | Dictionary |  |  |  | This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".<br>Unique LACP port-id ranges are recommended for EVPN Multihoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.lacp_port_id_range.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "&lt;node_type_keys.key&gt;.defaults.lacp_port_id_range.size") | Integer |  | 128 |  | Recommended size > = number of ports in the switch. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset</samp>](## "&lt;node_type_keys.key&gt;.defaults.lacp_port_id_range.offset") | Integer |  | 0 |  | Offset is used to avoid overlapping port-id ranges of different switches.<br>Useful when a "connected-endpoint" is connected to switches in different "node_groups".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;always_configure_ip_routing</samp>](## "&lt;node_type_keys.key&gt;.defaults.always_configure_ip_routing") | Boolean |  | False |  | Force configuration of "ip routing" even on L2 devices.<br>Use this to retain behavior of AVD versions below 4.0.0.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;node_type_keys.key&gt;.defaults.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;node_type_keys.key&gt;.defaults.structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].id") | Integer |  |  |  | Unique identifier used for IP addressing and other algorithms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].platform") | String |  |  |  | Arista platform family. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mac_address") | String |  |  |  | Leverage to document management interface mac address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].system_mac_address") | String |  |  |  | System MAC Address in this following format: "xx:xx:xx:xx:xx:xx".<br>Set to the same MAC address as available in "show version" on the device.<br>"system_mac_address" can also be set directly as a hostvar.<br>If both are set, the setting under "Fabric Topology" takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].serial_number") | String |  |  |  | Set to the Serial Number of the device<br>For  now only used for documentation purpose in the fabric documentation<br>and part of the structured_config<br>"serial_number" can also be set directly as a hostvar.<br>If both are set, the setting under "Fabric Topology" takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].rack") | String |  |  |  | Rack that the switch is located in (only used in snmp_settings location). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipv6_mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv6 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mgmt_interface") | String |  |  |  | Management Interface Name.<br>Default -> platform_management_interface -> mgmt_interface -> "Management1".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking") | Dictionary |  |  |  | This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream interfaces.<br>Useful in EVPN multhoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking.groups") | List, items: Dictionary |  | [{'name': 'LT_GROUP1'}] |  | Link Tracking Groups.<br>By default a single group named "LT_GROUP1" is defined with default values.<br>Any groups defined under "groups" will replace the default.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking.groups.[].name") | String |  |  |  | Tracking group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking.groups.[].recovery_delay") | Integer |  |  | Min: 0<br>Max: 3600 | default -> platform_settings_mlag_reload_delay -> 300. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;links_minimum</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking.groups.[].links_minimum") | Integer |  |  | Min: 1<br>Max: 100000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_port_id_range</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].lacp_port_id_range") | Dictionary |  |  |  | This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".<br>Unique LACP port-id ranges are recommended for EVPN Multihoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].lacp_port_id_range.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].lacp_port_id_range.size") | Integer |  | 128 |  | Recommended size > = number of ports in the switch. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].lacp_port_id_range.offset") | Integer |  | 0 |  | Offset is used to avoid overlapping port-id ranges of different switches.<br>Useful when a "connected-endpoint" is connected to switches in different "node_groups".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_configure_ip_routing</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].always_configure_ip_routing") | Boolean |  | False |  | Force configuration of "ip routing" even on L2 devices.<br>Use this to retain behavior of AVD versions below 4.0.0.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].id") | Integer |  |  |  | Unique identifier used for IP addressing and other algorithms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].platform") | String |  |  |  | Arista platform family. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mac_address") | String |  |  |  | Leverage to document management interface mac address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].system_mac_address") | String |  |  |  | System MAC Address in this following format: "xx:xx:xx:xx:xx:xx".<br>Set to the same MAC address as available in "show version" on the device.<br>"system_mac_address" can also be set directly as a hostvar.<br>If both are set, the setting under "Fabric Topology" takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].serial_number") | String |  |  |  | Set to the Serial Number of the device<br>For  now only used for documentation purpose in the fabric documentation<br>and part of the structured_config<br>"serial_number" can also be set directly as a hostvar.<br>If both are set, the setting under "Fabric Topology" takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].rack") | String |  |  |  | Rack that the switch is located in (only used in snmp_settings location). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipv6_mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv6 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mgmt_interface") | String |  |  |  | Management Interface Name.<br>Default -> platform_management_interface -> mgmt_interface -> "Management1".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking") | Dictionary |  |  |  | This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream interfaces.<br>Useful in EVPN multhoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking.groups") | List, items: Dictionary |  | [{'name': 'LT_GROUP1'}] |  | Link Tracking Groups.<br>By default a single group named "LT_GROUP1" is defined with default values.<br>Any groups defined under "groups" will replace the default.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking.groups.[].name") | String |  |  |  | Tracking group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking.groups.[].recovery_delay") | Integer |  |  | Min: 0<br>Max: 3600 | default -> platform_settings_mlag_reload_delay -> 300. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;links_minimum</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking.groups.[].links_minimum") | Integer |  |  | Min: 1<br>Max: 100000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_port_id_range</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].lacp_port_id_range") | Dictionary |  |  |  | This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".<br>Unique LACP port-id ranges are recommended for EVPN Multihoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].lacp_port_id_range.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].lacp_port_id_range.size") | Integer |  | 128 |  | Recommended size > = number of ports in the switch. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].lacp_port_id_range.offset") | Integer |  | 0 |  | Offset is used to avoid overlapping port-id ranges of different switches.<br>Useful when a "connected-endpoint" is connected to switches in different "node_groups".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_configure_ip_routing</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].always_configure_ip_routing") | Boolean |  | False |  | Force configuration of "ip routing" even on L2 devices.<br>Use this to retain behavior of AVD versions below 4.0.0.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].id") | Integer |  |  |  | Unique identifier used for IP addressing and other algorithms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].platform") | String |  |  |  | Arista platform family. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mac_address") | String |  |  |  | Leverage to document management interface mac address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].system_mac_address") | String |  |  |  | System MAC Address in this following format: "xx:xx:xx:xx:xx:xx".<br>Set to the same MAC address as available in "show version" on the device.<br>"system_mac_address" can also be set directly as a hostvar.<br>If both are set, the setting under "Fabric Topology" takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].serial_number") | String |  |  |  | Set to the Serial Number of the device<br>For  now only used for documentation purpose in the fabric documentation<br>and part of the structured_config<br>"serial_number" can also be set directly as a hostvar.<br>If both are set, the setting under "Fabric Topology" takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].rack") | String |  |  |  | Rack that the switch is located in (only used in snmp_settings location). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipv6_mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv6 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mgmt_interface") | String |  |  |  | Management Interface Name.<br>Default -> platform_management_interface -> mgmt_interface -> "Management1".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking") | Dictionary |  |  |  | This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream interfaces.<br>Useful in EVPN multhoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking.groups") | List, items: Dictionary |  | [{'name': 'LT_GROUP1'}] |  | Link Tracking Groups.<br>By default a single group named "LT_GROUP1" is defined with default values.<br>Any groups defined under "groups" will replace the default.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking.groups.[].name") | String |  |  |  | Tracking group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking.groups.[].recovery_delay") | Integer |  |  | Min: 0<br>Max: 3600 | default -> platform_settings_mlag_reload_delay -> 300. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;links_minimum</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking.groups.[].links_minimum") | Integer |  |  | Min: 1<br>Max: 100000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_port_id_range</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].lacp_port_id_range") | Dictionary |  |  |  | This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".<br>Unique LACP port-id ranges are recommended for EVPN Multihoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].lacp_port_id_range.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].lacp_port_id_range.size") | Integer |  | 128 |  | Recommended size > = number of ports in the switch. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].lacp_port_id_range.offset") | Integer |  | 0 |  | Offset is used to avoid overlapping port-id ranges of different switches.<br>Useful when a "connected-endpoint" is connected to switches in different "node_groups".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_configure_ip_routing</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].always_configure_ip_routing") | Boolean |  | False |  | Force configuration of "ip routing" even on L2 devices.<br>Use this to retain behavior of AVD versions below 4.0.0.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
        id: <int>
        platform: <str>
        mac_address: <str>
        system_mac_address: <str>
        serial_number: <str>
        rack: <str>
        mgmt_ip: <str>
        ipv6_mgmt_ip: <str>
        mgmt_interface: <str>
        link_tracking:
          enabled: <bool>
          groups:
            - name: <str>
              recovery_delay: <int>
              links_minimum: <int>
        lacp_port_id_range:
          enabled: <bool>
          size: <int>
          offset: <int>
        always_configure_ip_routing: <bool>
        raw_eos_cli: <str>
        structured_config:
      node_groups:
        - id: <int>
          platform: <str>
          mac_address: <str>
          system_mac_address: <str>
          serial_number: <str>
          rack: <str>
          mgmt_ip: <str>
          ipv6_mgmt_ip: <str>
          mgmt_interface: <str>
          link_tracking:
            enabled: <bool>
            groups:
              - name: <str>
                recovery_delay: <int>
                links_minimum: <int>
          lacp_port_id_range:
            enabled: <bool>
            size: <int>
            offset: <int>
          always_configure_ip_routing: <bool>
          raw_eos_cli: <str>
          structured_config:
          nodes:
            - id: <int>
              platform: <str>
              mac_address: <str>
              system_mac_address: <str>
              serial_number: <str>
              rack: <str>
              mgmt_ip: <str>
              ipv6_mgmt_ip: <str>
              mgmt_interface: <str>
              link_tracking:
                enabled: <bool>
                groups:
                  - name: <str>
                    recovery_delay: <int>
                    links_minimum: <int>
              lacp_port_id_range:
                enabled: <bool>
                size: <int>
                offset: <int>
              always_configure_ip_routing: <bool>
              raw_eos_cli: <str>
              structured_config:
      nodes:
        - id: <int>
          platform: <str>
          mac_address: <str>
          system_mac_address: <str>
          serial_number: <str>
          rack: <str>
          mgmt_ip: <str>
          ipv6_mgmt_ip: <str>
          mgmt_interface: <str>
          link_tracking:
            enabled: <bool>
            groups:
              - name: <str>
                recovery_delay: <int>
                links_minimum: <int>
          lacp_port_id_range:
            enabled: <bool>
            size: <int>
            offset: <int>
          always_configure_ip_routing: <bool>
          raw_eos_cli: <str>
          structured_config:
    ```

## Inband Management Vlan

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_management_subnet</samp>](## "&lt;node_type_keys.key&gt;.defaults.inband_management_subnet") | String |  |  | Format: ipv4_cidr | Optional IP subnet assigned to Inband Management SVI on l2leafs in default VRF.<br>Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP. This allows all l3leafs to reuse the same subnet.<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_management_vlan</samp>](## "&lt;node_type_keys.key&gt;.defaults.inband_management_vlan") | Integer |  | 4092 |  | VLAN number assigned to Inband Management SVI on l2leafs in default VRF. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- inband_management_subnet</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].inband_management_subnet") | String |  |  | Format: ipv4_cidr | Optional IP subnet assigned to Inband Management SVI on l2leafs in default VRF.<br>Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP. This allows all l3leafs to reuse the same subnet.<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].inband_management_vlan") | Integer |  | 4092 |  | VLAN number assigned to Inband Management SVI on l2leafs in default VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- inband_management_subnet</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].inband_management_subnet") | String |  |  | Format: ipv4_cidr | Optional IP subnet assigned to Inband Management SVI on l2leafs in default VRF.<br>Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP. This allows all l3leafs to reuse the same subnet.<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].inband_management_vlan") | Integer |  | 4092 |  | VLAN number assigned to Inband Management SVI on l2leafs in default VRF. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- inband_management_subnet</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].inband_management_subnet") | String |  |  | Format: ipv4_cidr | Optional IP subnet assigned to Inband Management SVI on l2leafs in default VRF.<br>Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP. This allows all l3leafs to reuse the same subnet.<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_vlan</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].inband_management_vlan") | Integer |  | 4092 |  | VLAN number assigned to Inband Management SVI on l2leafs in default VRF. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
        inband_management_subnet: <str>
        inband_management_vlan: <int>
      node_groups:
        - inband_management_subnet: <str>
          inband_management_vlan: <int>
          nodes:
            - inband_management_subnet: <str>
              inband_management_vlan: <int>
      nodes:
        - inband_management_subnet: <str>
          inband_management_vlan: <int>
    ```

## Isis Underlay Protocol Management

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "&lt;node_type_keys.key&gt;.defaults.isis_system_id_prefix") | String |  |  | Pattern: [0-9a-f]{4}\.[0-9a-f]{4} | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "&lt;node_type_keys.key&gt;.defaults.isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "&lt;node_type_keys.key&gt;.defaults.is_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "&lt;node_type_keys.key&gt;.defaults.node_sid_base") | Integer |  | 0 |  | Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- isis_system_id_prefix</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].isis_system_id_prefix") | String |  |  | Pattern: [0-9a-f]{4}\.[0-9a-f]{4} | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].is_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].node_sid_base") | Integer |  | 0 |  | Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- isis_system_id_prefix</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].isis_system_id_prefix") | String |  |  | Pattern: [0-9a-f]{4}\.[0-9a-f]{4} | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].is_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].node_sid_base") | Integer |  | 0 |  | Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- isis_system_id_prefix</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].isis_system_id_prefix") | String |  |  | Pattern: [0-9a-f]{4}\.[0-9a-f]{4} | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].is_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].node_sid_base") | Integer |  | 0 |  | Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
        isis_system_id_prefix: <str>
        isis_maximum_paths: <int>
        is_type: <str>
        node_sid_base: <int>
      node_groups:
        - isis_system_id_prefix: <str>
          isis_maximum_paths: <int>
          is_type: <str>
          node_sid_base: <int>
          nodes:
            - isis_system_id_prefix: <str>
              isis_maximum_paths: <int>
              is_type: <str>
              node_sid_base: <int>
      nodes:
        - isis_system_id_prefix: <str>
          isis_maximum_paths: <int>
          is_type: <str>
          node_sid_base: <int>
    ```

## Loopback And Vtep Management

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "&lt;node_type_keys.key&gt;.defaults.loopback_ipv4_offset") | Integer |  | 0 |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "&lt;node_type_keys.key&gt;.defaults.loopback_ipv6_offset") | Integer |  | 0 |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "&lt;node_type_keys.key&gt;.defaults.vtep_loopback") | String |  |  | Pattern: Loopback[\d/]+ | Set VXLAN source interface. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].loopback_ipv4_offset") | Integer |  | 0 |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].loopback_ipv6_offset") | Integer |  | 0 |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].vtep_loopback") | String |  |  | Pattern: Loopback[\d/]+ | Set VXLAN source interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].loopback_ipv4_offset") | Integer |  | 0 |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].loopback_ipv6_offset") | Integer |  | 0 |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].vtep_loopback") | String |  |  | Pattern: Loopback[\d/]+ | Set VXLAN source interface. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].loopback_ipv4_offset") | Integer |  | 0 |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].loopback_ipv6_offset") | Integer |  | 0 |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].vtep_loopback") | String |  |  | Pattern: Loopback[\d/]+ | Set VXLAN source interface. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
        loopback_ipv4_pool: <str>
        vtep_loopback_ipv4_pool: <str>
        loopback_ipv4_offset: <int>
        loopback_ipv6_pool: <str>
        loopback_ipv6_offset: <int>
        vtep_loopback: <str>
      node_groups:
        - loopback_ipv4_pool: <str>
          vtep_loopback_ipv4_pool: <str>
          loopback_ipv4_offset: <int>
          loopback_ipv6_pool: <str>
          loopback_ipv6_offset: <int>
          vtep_loopback: <str>
          nodes:
            - loopback_ipv4_pool: <str>
              vtep_loopback_ipv4_pool: <str>
              loopback_ipv4_offset: <int>
              loopback_ipv6_pool: <str>
              loopback_ipv6_offset: <int>
              vtep_loopback: <str>
      nodes:
        - loopback_ipv4_pool: <str>
          vtep_loopback_ipv4_pool: <str>
          loopback_ipv4_offset: <int>
          loopback_ipv6_pool: <str>
          loopback_ipv6_offset: <int>
          vtep_loopback: <str>
    ```

## Mlag Configuration Management

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag") | Boolean |  | True |  | Enable / Disable auto MLAG, when two nodes are defined in node group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_dual_primary_detection</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_dual_primary_detection") | Boolean |  | False |  | Enable / Disable MLAG dual primary detection. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_origin_incomplete</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_ibgp_origin_incomplete") | Boolean |  | True |  | Set origin of routes received from MLAG iBGP peer to incomplete.<br>The purpose is to optimize routing for leaf loopbacks from spine perspective and<br>avoid suboptimal routing via peerlink for control plane traffic.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_interfaces") | List, items: String |  |  |  | Each list item supports range syntax that can be expanded into a list of interfaces.<br>Required when MLAG leafs are present in the topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_interfaces.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces_speed</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_interfaces_speed") | String |  |  |  | Set MLAG interface speed.<br>< interface_speed or forced interface_speed or auto interface_speed >.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_peer_l3_vlan") | Integer |  | 4093 | Min: 0<br>Max: 4094 | Underlay L3 peering SVI interface id.<br>If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used for L3 peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_peer_l3_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG underlay L3 peering. IP is derived from the node id.<br>Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_peer_vlan") | Integer |  | 4094 | Min: 1<br>Max: 4094 | MLAG Peer Link (control link) SVI interface id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_link_allowed_vlans</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_peer_link_allowed_vlans") | String |  | 2-4094 |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_peer_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG Peer Link (control link). IP is derived from the node id.<br>Required when MLAG leafs present in topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_id</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_port_channel_id") | Integer |  |  |  | If not set, the mlag port-channel id is generated based on the digits of the first interface present in 'mlag_interfaces'.<br>Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_mode</samp>](## "&lt;node_type_keys.key&gt;.defaults.spanning_tree_mode") | String |  |  | Valid Values:<br>- mstp<br>- rstp<br>- rapid-pvst<br>- none |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_priority</samp>](## "&lt;node_type_keys.key&gt;.defaults.spanning_tree_priority") | Integer |  | 32768 |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_root_super</samp>](## "&lt;node_type_keys.key&gt;.defaults.spanning_tree_root_super") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;virtual_router_mac_address</samp>](## "&lt;node_type_keys.key&gt;.defaults.virtual_router_mac_address") | String |  |  | Format: mac | Virtual router mac address for anycast gateway. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- mlag</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag") | Boolean |  | True |  | Enable / Disable auto MLAG, when two nodes are defined in node group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_dual_primary_detection</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_dual_primary_detection") | Boolean |  | False |  | Enable / Disable MLAG dual primary detection. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_origin_incomplete</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_ibgp_origin_incomplete") | Boolean |  | True |  | Set origin of routes received from MLAG iBGP peer to incomplete.<br>The purpose is to optimize routing for leaf loopbacks from spine perspective and<br>avoid suboptimal routing via peerlink for control plane traffic.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_interfaces") | List, items: String |  |  |  | Each list item supports range syntax that can be expanded into a list of interfaces.<br>Required when MLAG leafs are present in the topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_interfaces.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces_speed</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_interfaces_speed") | String |  |  |  | Set MLAG interface speed.<br>< interface_speed or forced interface_speed or auto interface_speed >.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_peer_l3_vlan") | Integer |  | 4093 | Min: 0<br>Max: 4094 | Underlay L3 peering SVI interface id.<br>If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used for L3 peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_peer_l3_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG underlay L3 peering. IP is derived from the node id.<br>Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_peer_vlan") | Integer |  | 4094 | Min: 1<br>Max: 4094 | MLAG Peer Link (control link) SVI interface id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_link_allowed_vlans</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_peer_link_allowed_vlans") | String |  | 2-4094 |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_peer_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG Peer Link (control link). IP is derived from the node id.<br>Required when MLAG leafs present in topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_port_channel_id") | Integer |  |  |  | If not set, the mlag port-channel id is generated based on the digits of the first interface present in 'mlag_interfaces'.<br>Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_mode</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].spanning_tree_mode") | String |  |  | Valid Values:<br>- mstp<br>- rstp<br>- rapid-pvst<br>- none |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_priority</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].spanning_tree_priority") | Integer |  | 32768 |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_root_super</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].spanning_tree_root_super") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;virtual_router_mac_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].virtual_router_mac_address") | String |  |  | Format: mac | Virtual router mac address for anycast gateway. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- mlag</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag") | Boolean |  | True |  | Enable / Disable auto MLAG, when two nodes are defined in node group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_dual_primary_detection</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_dual_primary_detection") | Boolean |  | False |  | Enable / Disable MLAG dual primary detection. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_origin_incomplete</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_ibgp_origin_incomplete") | Boolean |  | True |  | Set origin of routes received from MLAG iBGP peer to incomplete.<br>The purpose is to optimize routing for leaf loopbacks from spine perspective and<br>avoid suboptimal routing via peerlink for control plane traffic.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_interfaces") | List, items: String |  |  |  | Each list item supports range syntax that can be expanded into a list of interfaces.<br>Required when MLAG leafs are present in the topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_interfaces.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces_speed</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_interfaces_speed") | String |  |  |  | Set MLAG interface speed.<br>< interface_speed or forced interface_speed or auto interface_speed >.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_peer_l3_vlan") | Integer |  | 4093 | Min: 0<br>Max: 4094 | Underlay L3 peering SVI interface id.<br>If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used for L3 peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_peer_l3_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG underlay L3 peering. IP is derived from the node id.<br>Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_peer_vlan") | Integer |  | 4094 | Min: 1<br>Max: 4094 | MLAG Peer Link (control link) SVI interface id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_link_allowed_vlans</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_peer_link_allowed_vlans") | String |  | 2-4094 |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_peer_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG Peer Link (control link). IP is derived from the node id.<br>Required when MLAG leafs present in topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_port_channel_id") | Integer |  |  |  | If not set, the mlag port-channel id is generated based on the digits of the first interface present in 'mlag_interfaces'.<br>Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_mode</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].spanning_tree_mode") | String |  |  | Valid Values:<br>- mstp<br>- rstp<br>- rapid-pvst<br>- none |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_priority</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].spanning_tree_priority") | Integer |  | 32768 |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_root_super</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].spanning_tree_root_super") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;virtual_router_mac_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].virtual_router_mac_address") | String |  |  | Format: mac | Virtual router mac address for anycast gateway. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- mlag</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag") | Boolean |  | True |  | Enable / Disable auto MLAG, when two nodes are defined in node group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_dual_primary_detection</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_dual_primary_detection") | Boolean |  | False |  | Enable / Disable MLAG dual primary detection. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_origin_incomplete</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_ibgp_origin_incomplete") | Boolean |  | True |  | Set origin of routes received from MLAG iBGP peer to incomplete.<br>The purpose is to optimize routing for leaf loopbacks from spine perspective and<br>avoid suboptimal routing via peerlink for control plane traffic.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_interfaces") | List, items: String |  |  |  | Each list item supports range syntax that can be expanded into a list of interfaces.<br>Required when MLAG leafs are present in the topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_interfaces.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces_speed</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_interfaces_speed") | String |  |  |  | Set MLAG interface speed.<br>< interface_speed or forced interface_speed or auto interface_speed >.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_peer_l3_vlan") | Integer |  | 4093 | Min: 0<br>Max: 4094 | Underlay L3 peering SVI interface id.<br>If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used for L3 peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_peer_l3_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG underlay L3 peering. IP is derived from the node id.<br>Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_peer_vlan") | Integer |  | 4094 | Min: 1<br>Max: 4094 | MLAG Peer Link (control link) SVI interface id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_link_allowed_vlans</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_peer_link_allowed_vlans") | String |  | 2-4094 |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_peer_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG Peer Link (control link). IP is derived from the node id.<br>Required when MLAG leafs present in topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_id</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_port_channel_id") | Integer |  |  |  | If not set, the mlag port-channel id is generated based on the digits of the first interface present in 'mlag_interfaces'.<br>Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_mode</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].spanning_tree_mode") | String |  |  | Valid Values:<br>- mstp<br>- rstp<br>- rapid-pvst<br>- none |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_priority</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].spanning_tree_priority") | Integer |  | 32768 |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_root_super</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].spanning_tree_root_super") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;virtual_router_mac_address</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].virtual_router_mac_address") | String |  |  | Format: mac | Virtual router mac address for anycast gateway. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
        mlag: <bool>
        mlag_dual_primary_detection: <bool>
        mlag_ibgp_origin_incomplete: <bool>
        mlag_interfaces:
          - <str>
        mlag_interfaces_speed: <str>
        mlag_peer_l3_vlan: <int>
        mlag_peer_l3_ipv4_pool: <str>
        mlag_peer_vlan: <int>
        mlag_peer_link_allowed_vlans: <str>
        mlag_peer_ipv4_pool: <str>
        mlag_port_channel_id: <int>
        spanning_tree_mode: <str>
        spanning_tree_priority: <int>
        spanning_tree_root_super: <bool>
        virtual_router_mac_address: <str>
      node_groups:
        - mlag: <bool>
          mlag_dual_primary_detection: <bool>
          mlag_ibgp_origin_incomplete: <bool>
          mlag_interfaces:
            - <str>
          mlag_interfaces_speed: <str>
          mlag_peer_l3_vlan: <int>
          mlag_peer_l3_ipv4_pool: <str>
          mlag_peer_vlan: <int>
          mlag_peer_link_allowed_vlans: <str>
          mlag_peer_ipv4_pool: <str>
          mlag_port_channel_id: <int>
          spanning_tree_mode: <str>
          spanning_tree_priority: <int>
          spanning_tree_root_super: <bool>
          virtual_router_mac_address: <str>
          nodes:
            - mlag: <bool>
              mlag_dual_primary_detection: <bool>
              mlag_ibgp_origin_incomplete: <bool>
              mlag_interfaces:
                - <str>
              mlag_interfaces_speed: <str>
              mlag_peer_l3_vlan: <int>
              mlag_peer_l3_ipv4_pool: <str>
              mlag_peer_vlan: <int>
              mlag_peer_link_allowed_vlans: <str>
              mlag_peer_ipv4_pool: <str>
              mlag_port_channel_id: <int>
              spanning_tree_mode: <str>
              spanning_tree_priority: <int>
              spanning_tree_root_super: <bool>
              virtual_router_mac_address: <str>
      nodes:
        - mlag: <bool>
          mlag_dual_primary_detection: <bool>
          mlag_ibgp_origin_incomplete: <bool>
          mlag_interfaces:
            - <str>
          mlag_interfaces_speed: <str>
          mlag_peer_l3_vlan: <int>
          mlag_peer_l3_ipv4_pool: <str>
          mlag_peer_vlan: <int>
          mlag_peer_link_allowed_vlans: <str>
          mlag_peer_ipv4_pool: <str>
          mlag_port_channel_id: <int>
          spanning_tree_mode: <str>
          spanning_tree_priority: <int>
          spanning_tree_root_super: <bool>
          virtual_router_mac_address: <str>
    ```

## Mpls Settings Management

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "&lt;node_type_keys.key&gt;.defaults.mpls_overlay_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "&lt;node_type_keys.key&gt;.defaults.overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.overlay_address_families.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- evpn<br>- vpn-ipv4<br>- vpn-ipv6 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "&lt;node_type_keys.key&gt;.defaults.mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.mpls_route_reflectors.[].&lt;str&gt;") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "&lt;node_type_keys.key&gt;.defaults.bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- mpls_overlay_role</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mpls_overlay_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].overlay_address_families.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- evpn<br>- vpn-ipv4<br>- vpn-ipv6 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mpls_route_reflectors.[].&lt;str&gt;") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- mpls_overlay_role</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mpls_overlay_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].overlay_address_families.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- evpn<br>- vpn-ipv4<br>- vpn-ipv6 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mpls_route_reflectors.[].&lt;str&gt;") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- mpls_overlay_role</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mpls_overlay_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].overlay_address_families.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- evpn<br>- vpn-ipv4<br>- vpn-ipv6 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mpls_route_reflectors.[].&lt;str&gt;") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
        mpls_overlay_role: <str>
        overlay_address_families:
          - <str>
        mpls_route_reflectors:
          - <str>
        bgp_cluster_id: <str>
      node_groups:
        - mpls_overlay_role: <str>
          overlay_address_families:
            - <str>
          mpls_route_reflectors:
            - <str>
          bgp_cluster_id: <str>
          nodes:
            - mpls_overlay_role: <str>
              overlay_address_families:
                - <str>
              mpls_route_reflectors:
                - <str>
              bgp_cluster_id: <str>
      nodes:
        - mpls_overlay_role: <str>
          overlay_address_families:
            - <str>
          mpls_route_reflectors:
            - <str>
          bgp_cluster_id: <str>
    ```

## Ptp Settings Management

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.profile") | String |  | aes67-r16-2016 | Valid Values:<br>- aes67<br>- smpte2059-2<br>- aes67-r16-2016 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.domain") | Integer |  | 127 | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority1</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.priority1") | Integer |  |  | Min: 0<br>Max: 255 | default -> automatically set based on node_type.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority2</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.priority2") | Integer |  |  | Min: 0<br>Max: 255 | default -> (node_id modulus 256).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_clock_identity</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.auto_clock_identity") | Boolean |  | True |  | If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour, simply disable the automatic PTP clock identity.<br>default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority 1 as HEX) + ":00:" + (PTP priority 2 as HEX).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity_prefix</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.clock_identity_prefix") | String |  |  |  | PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".<br>By default the 3-byte prefix is "00:1C:73".<br>This can be overridden if auto_clock_identity is set to true (which is the default).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.clock_identity") | String |  |  |  | Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ip</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.source_ip") | String |  |  |  | By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is the recommended behaviour.<br>This can be set manually if required, for example, to a value of "10.1.2.3".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.ttl") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward_unicast</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.forward_unicast") | Boolean |  | False |  | Enable PTP unicast forwarding.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.dscp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;general_messages</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.dscp.general_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event_messages</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.dscp.event_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.enabled") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.threshold.offset_from_master") | Integer |  | 250 | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.threshold.mean_path_delay") | Integer |  | 1500 | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.threshold.drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.threshold.drop.offset_from_master") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.threshold.drop.mean_path_delay") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_message</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.intervals") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.intervals.announce") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.intervals.follow_up") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.intervals.sync") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_ids</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.sequence_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.sequence_ids.enabled") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.sequence_ids.announce") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_resp</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.sequence_ids.delay_resp") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.sequence_ids.follow_up") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.sequence_ids.sync") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- ptp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.profile") | String |  | aes67-r16-2016 | Valid Values:<br>- aes67<br>- smpte2059-2<br>- aes67-r16-2016 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.domain") | Integer |  | 127 | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority1</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.priority1") | Integer |  |  | Min: 0<br>Max: 255 | default -> automatically set based on node_type.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority2</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.priority2") | Integer |  |  | Min: 0<br>Max: 255 | default -> (node_id modulus 256).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_clock_identity</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.auto_clock_identity") | Boolean |  | True |  | If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour, simply disable the automatic PTP clock identity.<br>default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority 1 as HEX) + ":00:" + (PTP priority 2 as HEX).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity_prefix</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.clock_identity_prefix") | String |  |  |  | PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".<br>By default the 3-byte prefix is "00:1C:73".<br>This can be overridden if auto_clock_identity is set to true (which is the default).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.clock_identity") | String |  |  |  | Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ip</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.source_ip") | String |  |  |  | By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is the recommended behaviour.<br>This can be set manually if required, for example, to a value of "10.1.2.3".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.ttl") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward_unicast</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.forward_unicast") | Boolean |  | False |  | Enable PTP unicast forwarding.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.dscp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;general_messages</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.dscp.general_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event_messages</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.dscp.event_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.enabled") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.threshold.offset_from_master") | Integer |  | 250 | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.threshold.mean_path_delay") | Integer |  | 1500 | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.threshold.drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.threshold.drop.offset_from_master") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.threshold.drop.mean_path_delay") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_message</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.intervals") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.intervals.announce") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.intervals.follow_up") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.intervals.sync") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_ids</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.sequence_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.sequence_ids.enabled") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.sequence_ids.announce") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_resp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.sequence_ids.delay_resp") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.sequence_ids.follow_up") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.sequence_ids.sync") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ptp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.profile") | String |  | aes67-r16-2016 | Valid Values:<br>- aes67<br>- smpte2059-2<br>- aes67-r16-2016 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.domain") | Integer |  | 127 | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority1</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.priority1") | Integer |  |  | Min: 0<br>Max: 255 | default -> automatically set based on node_type.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority2</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.priority2") | Integer |  |  | Min: 0<br>Max: 255 | default -> (node_id modulus 256).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_clock_identity</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.auto_clock_identity") | Boolean |  | True |  | If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour, simply disable the automatic PTP clock identity.<br>default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority 1 as HEX) + ":00:" + (PTP priority 2 as HEX).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity_prefix</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.clock_identity_prefix") | String |  |  |  | PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".<br>By default the 3-byte prefix is "00:1C:73".<br>This can be overridden if auto_clock_identity is set to true (which is the default).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.clock_identity") | String |  |  |  | Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ip</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.source_ip") | String |  |  |  | By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is the recommended behaviour.<br>This can be set manually if required, for example, to a value of "10.1.2.3".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.ttl") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward_unicast</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.forward_unicast") | Boolean |  | False |  | Enable PTP unicast forwarding.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.dscp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;general_messages</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.dscp.general_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event_messages</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.dscp.event_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.enabled") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.threshold.offset_from_master") | Integer |  | 250 | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.threshold.mean_path_delay") | Integer |  | 1500 | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.threshold.drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.threshold.drop.offset_from_master") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.threshold.drop.mean_path_delay") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_message</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.intervals") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.intervals.announce") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.intervals.follow_up") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.intervals.sync") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_ids</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids.enabled") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids.announce") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_resp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids.delay_resp") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids.follow_up") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids.sync") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- ptp</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.profile") | String |  | aes67-r16-2016 | Valid Values:<br>- aes67<br>- smpte2059-2<br>- aes67-r16-2016 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.domain") | Integer |  | 127 | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority1</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.priority1") | Integer |  |  | Min: 0<br>Max: 255 | default -> automatically set based on node_type.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority2</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.priority2") | Integer |  |  | Min: 0<br>Max: 255 | default -> (node_id modulus 256).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_clock_identity</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.auto_clock_identity") | Boolean |  | True |  | If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour, simply disable the automatic PTP clock identity.<br>default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority 1 as HEX) + ":00:" + (PTP priority 2 as HEX).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity_prefix</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.clock_identity_prefix") | String |  |  |  | PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".<br>By default the 3-byte prefix is "00:1C:73".<br>This can be overridden if auto_clock_identity is set to true (which is the default).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.clock_identity") | String |  |  |  | Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ip</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.source_ip") | String |  |  |  | By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is the recommended behaviour.<br>This can be set manually if required, for example, to a value of "10.1.2.3".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.ttl") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward_unicast</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.forward_unicast") | Boolean |  | False |  | Enable PTP unicast forwarding.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.dscp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;general_messages</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.dscp.general_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event_messages</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.dscp.event_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.enabled") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.threshold.offset_from_master") | Integer |  | 250 | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.threshold.mean_path_delay") | Integer |  | 1500 | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.threshold.drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.threshold.drop.offset_from_master") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.threshold.drop.mean_path_delay") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_message</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.intervals") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.intervals.announce") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.intervals.follow_up") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.intervals.sync") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_ids</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.sequence_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.sequence_ids.enabled") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.sequence_ids.announce") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_resp</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.sequence_ids.delay_resp") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.sequence_ids.follow_up") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.sequence_ids.sync") | Integer |  | 3 | Min: 2<br>Max: 255 |  |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
        ptp:
          enabled: <bool>
          profile: <str>
          domain: <int>
          priority1: <int>
          priority2: <int>
          auto_clock_identity: <bool>
          clock_identity_prefix: <str>
          clock_identity: <str>
          source_ip: <str>
          ttl: <int>
          forward_unicast: <bool>
          dscp:
            general_messages: <int>
            event_messages: <int>
          monitor:
            enabled: <bool>
            threshold:
              offset_from_master: <int>
              mean_path_delay: <int>
              drop:
                offset_from_master: <int>
                mean_path_delay: <int>
            missing_message:
              intervals:
                announce: <int>
                follow_up: <int>
                sync: <int>
              sequence_ids:
                enabled: <bool>
                announce: <int>
                delay_resp: <int>
                follow_up: <int>
                sync: <int>
      node_groups:
        - ptp:
            enabled: <bool>
            profile: <str>
            domain: <int>
            priority1: <int>
            priority2: <int>
            auto_clock_identity: <bool>
            clock_identity_prefix: <str>
            clock_identity: <str>
            source_ip: <str>
            ttl: <int>
            forward_unicast: <bool>
            dscp:
              general_messages: <int>
              event_messages: <int>
            monitor:
              enabled: <bool>
              threshold:
                offset_from_master: <int>
                mean_path_delay: <int>
                drop:
                  offset_from_master: <int>
                  mean_path_delay: <int>
              missing_message:
                intervals:
                  announce: <int>
                  follow_up: <int>
                  sync: <int>
                sequence_ids:
                  enabled: <bool>
                  announce: <int>
                  delay_resp: <int>
                  follow_up: <int>
                  sync: <int>
          nodes:
            - ptp:
                enabled: <bool>
                profile: <str>
                domain: <int>
                priority1: <int>
                priority2: <int>
                auto_clock_identity: <bool>
                clock_identity_prefix: <str>
                clock_identity: <str>
                source_ip: <str>
                ttl: <int>
                forward_unicast: <bool>
                dscp:
                  general_messages: <int>
                  event_messages: <int>
                monitor:
                  enabled: <bool>
                  threshold:
                    offset_from_master: <int>
                    mean_path_delay: <int>
                    drop:
                      offset_from_master: <int>
                      mean_path_delay: <int>
                  missing_message:
                    intervals:
                      announce: <int>
                      follow_up: <int>
                      sync: <int>
                    sequence_ids:
                      enabled: <bool>
                      announce: <int>
                      delay_resp: <int>
                      follow_up: <int>
                      sync: <int>
      nodes:
        - ptp:
            enabled: <bool>
            profile: <str>
            domain: <int>
            priority1: <int>
            priority2: <int>
            auto_clock_identity: <bool>
            clock_identity_prefix: <str>
            clock_identity: <str>
            source_ip: <str>
            ttl: <int>
            forward_unicast: <bool>
            dscp:
              general_messages: <int>
              event_messages: <int>
            monitor:
              enabled: <bool>
              threshold:
                offset_from_master: <int>
                mean_path_delay: <int>
                drop:
                  offset_from_master: <int>
                  mean_path_delay: <int>
              missing_message:
                intervals:
                  announce: <int>
                  follow_up: <int>
                  sync: <int>
                sequence_ids:
                  enabled: <bool>
                  announce: <int>
                  delay_resp: <int>
                  follow_up: <int>
                  sync: <int>
    ```

## Topology Variables

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dc_name</samp>](## "dc_name") | String |  |  |  | DC Name, required to match Ansible Group name covering all devices in the DC.<br>Required for 5-stage CLOS (Super-spines).<br> |
    | [<samp>fabric_name</samp>](## "fabric_name") | String | Required |  |  | Fabric Name, required to match Ansible Group name covering all devices in the Fabric, **must** be an inventory group name. |
    | [<samp>pod_name</samp>](## "pod_name") | String |  |  |  | POD Name, only used in Fabric Documentation (Optional), fallback to dc_name and then to fabric_name.<br>Recommended to be common between Spines and Leafs within a POD (One l3ls topology).<br> |

=== "YAML"

    ```yaml
    dc_name: <str>
    fabric_name: <str>
    pod_name: <str>
    ```

## Type

The `type:` variable needs to be defined for each device in the fabric.
This is leveraged to load the appropriate template to generate the configuration.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>type</samp>](## "type") | String |  |  | Valid Values:<br>- <value(s) of node_type_keys.type> |  |

=== "YAML"

    ```yaml
    type: <str>
    ```

## Uplink Management

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet to use to connect to uplink switches. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_interfaces") | List, items: String |  |  |  | Local uplink interfaces<br>Each list item supports range syntax that can be expanded into a list of interfaces.<br>If uplink_interfaces is not defined, platform-specific defaults (defined under default_interfaces) will be used instead.<br>Please note that default_interfaces are not defined by default, you should define these yourself.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_switch_interfaces</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_switch_interfaces") | List, items: String |  |  |  | Interfaces located on uplink switches |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_switch_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_switches") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_switches.[].&lt;str&gt;") | String | Required |  |  | Hostname of uplink switch.<br>If parallel uplinks are in use, update max_parallel_uplinks below and specify each uplink switch multiple times.<br>e.g. uplink_switches: [ 'DC1-SPINE1', 'DC1-SPINE1', 'DC1-SPINE2', 'DC1-SPINE2' ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_interface_speed</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_interface_speed") | String |  |  |  | Set point-to-Point interface speed and will apply to uplink interfaces on both ends.<br>interface_speed or forced interface_speed or auto interface_speed.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;max_uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.defaults.max_uplink_switches") | Integer |  |  |  | Maximum number of uplink switches.<br>Changing this value may change IP Addressing on uplinks.<br>Can be used to reserve IP space for future expansions.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;max_parallel_uplinks</samp>](## "&lt;node_type_keys.key&gt;.defaults.max_parallel_uplinks") | Integer |  |  |  | Number of parallel links towards uplink switches.<br>Changing this value may change interface naming on uplinks (and corresponding downlinks).<br>Can be used to reserve interfaces for future parallel uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_bfd</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_bfd") | Boolean |  | False |  | Enable bfd on uplink interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_native_vlan</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_native_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Only applicable to switches with layer-2 port-channel uplinks.<br>A suspended (disabled) vlan will be created in both ends of the link unless the vlan is defined under network services.<br>By default the uplink will not have a native_vlan configured, so EOS defaults to vlan 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_ptp</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_ptp") | Dictionary |  |  |  | Enable PTP on all infrastructure links. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_ptp.enable") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_macsec</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_macsec") | Dictionary |  |  |  | Enable MacSec on all uplinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_structured_config</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_structured_config") | Dictionary |  |  |  | Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".<br>When uplink_type == "p2p", custom structured config added under ethernet_interfaces.<interface> for eos_cli_config_gen overrides the settings on the ethernet interface level.<br>When uplink_type == "port-channel", custom structured config added under port_channel_interfaces.<interface> for eos_cli_config_gen overrides the settings on the port-channel interface level.<br>"uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_structured_config</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_port_channel_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG peer link port-channel id.<br>Added under port_channel_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the port-channel interface level.<br>"mlag_port_channel_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan_structured_config</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_peer_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG Peer Link (control link) SVI interface id.<br>Added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan_structured_config</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_peer_l3_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG underlay L3 peering SVI interface id.<br>Added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;node_type_keys.key&gt;.defaults.short_esi") | String |  |  |  | short_esi only valid for l2leaf devices using port-channel uplink.<br>Setting short_esi to "auto" generates the short_esi automatically using a hash of configuration elements.<br>< 0000:0000:0000 | auto >.<br> |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- uplink_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet to use to connect to uplink switches. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_interfaces") | List, items: String |  |  |  | Local uplink interfaces<br>Each list item supports range syntax that can be expanded into a list of interfaces.<br>If uplink_interfaces is not defined, platform-specific defaults (defined under default_interfaces) will be used instead.<br>Please note that default_interfaces are not defined by default, you should define these yourself.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switch_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_switch_interfaces") | List, items: String |  |  |  | Interfaces located on uplink switches |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_switch_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_switches") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_switches.[].&lt;str&gt;") | String | Required |  |  | Hostname of uplink switch.<br>If parallel uplinks are in use, update max_parallel_uplinks below and specify each uplink switch multiple times.<br>e.g. uplink_switches: [ 'DC1-SPINE1', 'DC1-SPINE1', 'DC1-SPINE2', 'DC1-SPINE2' ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interface_speed</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_interface_speed") | String |  |  |  | Set point-to-Point interface speed and will apply to uplink interfaces on both ends.<br>interface_speed or forced interface_speed or auto interface_speed.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].max_uplink_switches") | Integer |  |  |  | Maximum number of uplink switches.<br>Changing this value may change IP Addressing on uplinks.<br>Can be used to reserve IP space for future expansions.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_parallel_uplinks</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].max_parallel_uplinks") | Integer |  |  |  | Number of parallel links towards uplink switches.<br>Changing this value may change interface naming on uplinks (and corresponding downlinks).<br>Can be used to reserve interfaces for future parallel uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_bfd</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_bfd") | Boolean |  | False |  | Enable bfd on uplink interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_native_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_native_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Only applicable to switches with layer-2 port-channel uplinks.<br>A suspended (disabled) vlan will be created in both ends of the link unless the vlan is defined under network services.<br>By default the uplink will not have a native_vlan configured, so EOS defaults to vlan 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ptp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_ptp") | Dictionary |  |  |  | Enable PTP on all infrastructure links. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_ptp.enable") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_macsec</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_macsec") | Dictionary |  |  |  | Enable MacSec on all uplinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_structured_config") | Dictionary |  |  |  | Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".<br>When uplink_type == "p2p", custom structured config added under ethernet_interfaces.<interface> for eos_cli_config_gen overrides the settings on the ethernet interface level.<br>When uplink_type == "port-channel", custom structured config added under port_channel_interfaces.<interface> for eos_cli_config_gen overrides the settings on the port-channel interface level.<br>"uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_port_channel_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG peer link port-channel id.<br>Added under port_channel_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the port-channel interface level.<br>"mlag_port_channel_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan_structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_peer_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG Peer Link (control link) SVI interface id.<br>Added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan_structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_peer_l3_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG underlay L3 peering SVI interface id.<br>Added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].short_esi") | String |  |  |  | short_esi only valid for l2leaf devices using port-channel uplink.<br>Setting short_esi to "auto" generates the short_esi automatically using a hash of configuration elements.<br>< 0000:0000:0000 | auto >.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- uplink_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet to use to connect to uplink switches. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_interfaces") | List, items: String |  |  |  | Local uplink interfaces<br>Each list item supports range syntax that can be expanded into a list of interfaces.<br>If uplink_interfaces is not defined, platform-specific defaults (defined under default_interfaces) will be used instead.<br>Please note that default_interfaces are not defined by default, you should define these yourself.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switch_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_switch_interfaces") | List, items: String |  |  |  | Interfaces located on uplink switches |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_switch_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_switches") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_switches.[].&lt;str&gt;") | String | Required |  |  | Hostname of uplink switch.<br>If parallel uplinks are in use, update max_parallel_uplinks below and specify each uplink switch multiple times.<br>e.g. uplink_switches: [ 'DC1-SPINE1', 'DC1-SPINE1', 'DC1-SPINE2', 'DC1-SPINE2' ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interface_speed</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_interface_speed") | String |  |  |  | Set point-to-Point interface speed and will apply to uplink interfaces on both ends.<br>interface_speed or forced interface_speed or auto interface_speed.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].max_uplink_switches") | Integer |  |  |  | Maximum number of uplink switches.<br>Changing this value may change IP Addressing on uplinks.<br>Can be used to reserve IP space for future expansions.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_parallel_uplinks</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].max_parallel_uplinks") | Integer |  |  |  | Number of parallel links towards uplink switches.<br>Changing this value may change interface naming on uplinks (and corresponding downlinks).<br>Can be used to reserve interfaces for future parallel uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_bfd</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_bfd") | Boolean |  | False |  | Enable bfd on uplink interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_native_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_native_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Only applicable to switches with layer-2 port-channel uplinks.<br>A suspended (disabled) vlan will be created in both ends of the link unless the vlan is defined under network services.<br>By default the uplink will not have a native_vlan configured, so EOS defaults to vlan 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ptp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_ptp") | Dictionary |  |  |  | Enable PTP on all infrastructure links. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_ptp.enable") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_macsec</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_macsec") | Dictionary |  |  |  | Enable MacSec on all uplinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_structured_config") | Dictionary |  |  |  | Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".<br>When uplink_type == "p2p", custom structured config added under ethernet_interfaces.<interface> for eos_cli_config_gen overrides the settings on the ethernet interface level.<br>When uplink_type == "port-channel", custom structured config added under port_channel_interfaces.<interface> for eos_cli_config_gen overrides the settings on the port-channel interface level.<br>"uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_port_channel_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG peer link port-channel id.<br>Added under port_channel_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the port-channel interface level.<br>"mlag_port_channel_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan_structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_peer_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG Peer Link (control link) SVI interface id.<br>Added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan_structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_peer_l3_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG underlay L3 peering SVI interface id.<br>Added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].short_esi") | String |  |  |  | short_esi only valid for l2leaf devices using port-channel uplink.<br>Setting short_esi to "auto" generates the short_esi automatically using a hash of configuration elements.<br>< 0000:0000:0000 | auto >.<br> |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- uplink_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet to use to connect to uplink switches. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_interfaces") | List, items: String |  |  |  | Local uplink interfaces<br>Each list item supports range syntax that can be expanded into a list of interfaces.<br>If uplink_interfaces is not defined, platform-specific defaults (defined under default_interfaces) will be used instead.<br>Please note that default_interfaces are not defined by default, you should define these yourself.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switch_interfaces</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_switch_interfaces") | List, items: String |  |  |  | Interfaces located on uplink switches |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_switch_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_switches") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_switches.[].&lt;str&gt;") | String | Required |  |  | Hostname of uplink switch.<br>If parallel uplinks are in use, update max_parallel_uplinks below and specify each uplink switch multiple times.<br>e.g. uplink_switches: [ 'DC1-SPINE1', 'DC1-SPINE1', 'DC1-SPINE2', 'DC1-SPINE2' ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interface_speed</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_interface_speed") | String |  |  |  | Set point-to-Point interface speed and will apply to uplink interfaces on both ends.<br>interface_speed or forced interface_speed or auto interface_speed.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].max_uplink_switches") | Integer |  |  |  | Maximum number of uplink switches.<br>Changing this value may change IP Addressing on uplinks.<br>Can be used to reserve IP space for future expansions.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_parallel_uplinks</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].max_parallel_uplinks") | Integer |  |  |  | Number of parallel links towards uplink switches.<br>Changing this value may change interface naming on uplinks (and corresponding downlinks).<br>Can be used to reserve interfaces for future parallel uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_bfd</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_bfd") | Boolean |  | False |  | Enable bfd on uplink interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_native_vlan</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_native_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Only applicable to switches with layer-2 port-channel uplinks.<br>A suspended (disabled) vlan will be created in both ends of the link unless the vlan is defined under network services.<br>By default the uplink will not have a native_vlan configured, so EOS defaults to vlan 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ptp</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_ptp") | Dictionary |  |  |  | Enable PTP on all infrastructure links. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_ptp.enable") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_macsec</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_macsec") | Dictionary |  |  |  | Enable MacSec on all uplinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_structured_config</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_structured_config") | Dictionary |  |  |  | Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".<br>When uplink_type == "p2p", custom structured config added under ethernet_interfaces.<interface> for eos_cli_config_gen overrides the settings on the ethernet interface level.<br>When uplink_type == "port-channel", custom structured config added under port_channel_interfaces.<interface> for eos_cli_config_gen overrides the settings on the port-channel interface level.<br>"uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_structured_config</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_port_channel_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG peer link port-channel id.<br>Added under port_channel_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the port-channel interface level.<br>"mlag_port_channel_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan_structured_config</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_peer_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG Peer Link (control link) SVI interface id.<br>Added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan_structured_config</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_peer_l3_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG underlay L3 peering SVI interface id.<br>Added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].short_esi") | String |  |  |  | short_esi only valid for l2leaf devices using port-channel uplink.<br>Setting short_esi to "auto" generates the short_esi automatically using a hash of configuration elements.<br>< 0000:0000:0000 | auto >.<br> |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
        uplink_ipv4_pool: <str>
        uplink_interfaces:
          - <str>
        uplink_switch_interfaces:
          - <str>
        uplink_switches:
          - <str>
        uplink_interface_speed: <str>
        max_uplink_switches: <int>
        max_parallel_uplinks: <int>
        uplink_bfd: <bool>
        uplink_native_vlan: <int>
        uplink_ptp:
          enable: <bool>
        uplink_macsec:
        uplink_structured_config:
        mlag_port_channel_structured_config:
        mlag_peer_vlan_structured_config:
        mlag_peer_l3_vlan_structured_config:
        short_esi: <str>
      node_groups:
        - uplink_ipv4_pool: <str>
          uplink_interfaces:
            - <str>
          uplink_switch_interfaces:
            - <str>
          uplink_switches:
            - <str>
          uplink_interface_speed: <str>
          max_uplink_switches: <int>
          max_parallel_uplinks: <int>
          uplink_bfd: <bool>
          uplink_native_vlan: <int>
          uplink_ptp:
            enable: <bool>
          uplink_macsec:
          uplink_structured_config:
          mlag_port_channel_structured_config:
          mlag_peer_vlan_structured_config:
          mlag_peer_l3_vlan_structured_config:
          short_esi: <str>
          nodes:
            - uplink_ipv4_pool: <str>
              uplink_interfaces:
                - <str>
              uplink_switch_interfaces:
                - <str>
              uplink_switches:
                - <str>
              uplink_interface_speed: <str>
              max_uplink_switches: <int>
              max_parallel_uplinks: <int>
              uplink_bfd: <bool>
              uplink_native_vlan: <int>
              uplink_ptp:
                enable: <bool>
              uplink_macsec:
              uplink_structured_config:
              mlag_port_channel_structured_config:
              mlag_peer_vlan_structured_config:
              mlag_peer_l3_vlan_structured_config:
              short_esi: <str>
      nodes:
        - uplink_ipv4_pool: <str>
          uplink_interfaces:
            - <str>
          uplink_switch_interfaces:
            - <str>
          uplink_switches:
            - <str>
          uplink_interface_speed: <str>
          max_uplink_switches: <int>
          max_parallel_uplinks: <int>
          uplink_bfd: <bool>
          uplink_native_vlan: <int>
          uplink_ptp:
            enable: <bool>
          uplink_macsec:
          uplink_structured_config:
          mlag_port_channel_structured_config:
          mlag_peer_vlan_structured_config:
          mlag_peer_l3_vlan_structured_config:
          short_esi: <str>
    ```
