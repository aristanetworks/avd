---
search:
  boost: 2
---

# Input Variables

## Node Type Keys

Define Node Type Keys, to specify the properties of each node type in the fabric
This allows for complete customization of the fabric layout.
This should be defined in top level group_var for the fabric.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>node_type_keys</samp>](## "node_type_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- key</samp>](## "node_type_keys.[].key") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "node_type_keys.[].type") | String |  |  |  | Type value matching this node_type_key |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;connected_endpoints</samp>](## "node_type_keys.[].connected_endpoints") | Boolean |  | False |  | Are endpoints connected to this node type |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_evpn_role</samp>](## "node_type_keys.[].default_evpn_role") | String |  | none | Valid Values:<br>- none<br>- client<br>- server | Default evpn_role. Can be overridden in topology vars. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_underlay_routing_protocol</samp>](## "node_type_keys.[].default_underlay_routing_protocol") | String |  | ebgp |  | Set the default underlay routing_protocol.<br>Can be overridden by setting "underlay_routing_protocol" host/group_vars<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_support</samp>](## "node_type_keys.[].mlag_support") | Boolean |  | False |  | Can this node type support mlag |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;network_services</samp>](## "node_type_keys.[].network_services") | Dictionary |  |  |  | Will network services be deployed on this node type |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l2</samp>](## "node_type_keys.[].network_services.l2") | Boolean |  | False |  | Vlans |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3</samp>](## "node_type_keys.[].network_services.l3") | Boolean |  | False |  | VRFs, SVIs (if l2 is true)<br>Only supported with underlay_router<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;underlay_router</samp>](## "node_type_keys.[].underlay_router") | Boolean |  | True |  | Is this node type a L3 device |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_type</samp>](## "node_type_keys.[].uplink_type") | String |  | p2p | Valid Values:<br>- p2p<br>- port-channel | Uplinks must be p2p if "vtep" or "underlay_router" is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep</samp>](## "node_type_keys.[].vtep") | Boolean |  | False |  | Is this switch an EVPN VTEP |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_lsr</samp>](## "node_type_keys.[].mpls_lsr") | Boolean |  | False |  | Is this switch an MPLS LSR |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_addressing</samp>](## "node_type_keys.[].ip_addressing") | Dictionary |  |  |  | Override ip_addressing templates |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "node_type_keys.[].ip_addressing.router_id") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.router_id |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ip_primary</samp>](## "node_type_keys.[].ip_addressing.mlag_ip_primary") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.mlag_ip_primary |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ip_secondary</samp>](## "node_type_keys.[].ip_addressing.mlag_ip_secondary") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.mlag_ip_secondary |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_l3_ip_primary</samp>](## "node_type_keys.[].ip_addressing.mlag_l3_ip_primary") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.mlag_l3_ip_primary |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_l3_ip_secondary</samp>](## "node_type_keys.[].ip_addressing.mlag_l3_ip_secondary") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.mlag_l3_ip_secondary |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;p2p_uplinks_ip</samp>](## "node_type_keys.[].ip_addressing.p2p_uplinks_ip") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.p2p_uplinks_ip |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;p2p_uplinks_peer_ip</samp>](## "node_type_keys.[].ip_addressing.p2p_uplinks_peer_ip") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.p2p_uplinks_peer_ip |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_ip_mlag</samp>](## "node_type_keys.[].ip_addressing.vtep_ip_mlag") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.vtep_ip_mlag |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_ip</samp>](## "node_type_keys.[].ip_addressing.vtep_ip") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.vtep_ip |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_descriptions</samp>](## "node_type_keys.[].interface_descriptions") | Dictionary |  |  |  | Override interface_descriptions templates<br>If description templates use Jinja2, they have to strip whitespaces using {%- -%} on any code blocks<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_ethernet_interfaces</samp>](## "node_type_keys.[].interface_descriptions.underlay_ethernet_interfaces") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.underlay_ethernet_interfaces |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_port_channel_interfaces</samp>](## "node_type_keys.[].interface_descriptions.underlay_port_channel_interfaces") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.underlay_port_channel_interfaces |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_ethernet_mlag_interfaces</samp>](## "node_type_keys.[].interface_descriptions.underlay_ethernet_mlag_interfaces") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.underlay_ethernet_mlag_interfaces |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_port_channel_mlag_interfaces</samp>](## "node_type_keys.[].interface_descriptions.underlay_port_channel_mlag_interfaces") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.underlay_port_channel_mlag_interfaces |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_endpoints_ethernet_interfaces</samp>](## "node_type_keys.[].interface_descriptions.connected_endpoints_ethernet_interfaces") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.connected_endpoints_ethernet_interfaces |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_endpoints_port_channel_interfaces</samp>](## "node_type_keys.[].interface_descriptions.connected_endpoints_port_channel_interfaces") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.connected_endpoints_port_channel_interfaces |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_loopback_interface</samp>](## "node_type_keys.[].interface_descriptions.overlay_loopback_interface") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.overlay_loopback_interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_interface</samp>](## "node_type_keys.[].interface_descriptions.vtep_loopback_interface") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.vtep_loopback_interface |

=== "YAML"

    ```yaml
    node_type_keys:
      - key: <str>
        type: <str>
        connected_endpoints: <bool>
        default_evpn_role: <str>
        default_underlay_routing_protocol: <str>
        mlag_support: <bool>
        network_services:
          l2: <bool>
          l3: <bool>
        underlay_router: <bool>
        uplink_type: <str>
        vtep: <bool>
        mpls_lsr: <bool>
        ip_addressing:
          router_id: <str>
          mlag_ip_primary: <str>
          mlag_ip_secondary: <str>
          mlag_l3_ip_primary: <str>
          mlag_l3_ip_secondary: <str>
          p2p_uplinks_ip: <str>
          p2p_uplinks_peer_ip: <str>
          vtep_ip_mlag: <str>
          vtep_ip: <str>
        interface_descriptions:
          underlay_ethernet_interfaces: <str>
          underlay_port_channel_interfaces: <str>
          underlay_ethernet_mlag_interfaces: <str>
          underlay_port_channel_mlag_interfaces: <str>
          connected_endpoints_ethernet_interfaces: <str>
          connected_endpoints_port_channel_interfaces: <str>
          overlay_loopback_interface: <str>
          vtep_loopback_interface: <str>
    ```

## Type

The `type:` variable needs to be defined for each device in the fabric.
This is leveraged to load the appropriate template to generate the configuration.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>type</samp>](## "type") | String | Required |  | Valid Values:<br>- <value(s) of node_type_keys.type> |  |

=== "YAML"

    ```yaml
    type: <str>
    ```
