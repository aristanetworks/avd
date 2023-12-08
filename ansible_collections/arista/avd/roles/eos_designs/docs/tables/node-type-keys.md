<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>node_type_keys</samp>](## "node_type_keys") | List, items: Dictionary |  |  |  | Define Node Type Keys, to specify the properties of each node type in the fabric.<br>This allows for complete customization of the fabric layout and functionality.<br>`node_type_keys` should be defined in top level group_var for the fabric.<br>The default values will be overridden if defining this key, so it is recommended to copy the defaults and modify them.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;key</samp>](## "node_type_keys.[].key") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "node_type_keys.[].type") | String |  |  |  | Type value matching this node_type_key. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;connected_endpoints</samp>](## "node_type_keys.[].connected_endpoints") | Boolean |  | `False` |  | Are endpoints connected to this node type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_evpn_role</samp>](## "node_type_keys.[].default_evpn_role") | String |  | `none` | Valid Values:<br>- <code>none</code><br>- <code>client</code><br>- <code>server</code> | Default evpn_role. Can be overridden in topology vars. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_ptp_priority1</samp>](## "node_type_keys.[].default_ptp_priority1") | Integer |  | `127` | Min: 0<br>Max: 255 | Default PTP priority 1 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_underlay_routing_protocol</samp>](## "node_type_keys.[].default_underlay_routing_protocol") | String |  | `ebgp` | Value is converted to lower case.<br>Valid Values:<br>- <code>ebgp</code><br>- <code>ibgp</code><br>- <code>ospf</code><br>- <code>ospf-ldp</code><br>- <code>isis</code><br>- <code>isis-sr</code><br>- <code>isis-ldp</code><br>- <code>isis-sr-ldp</code><br>- <code>none</code> | Set the default underlay routing_protocol.<br>Can be overridden by setting "underlay_routing_protocol" host/group_vars.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_overlay_routing_protocol</samp>](## "node_type_keys.[].default_overlay_routing_protocol") | String |  | `ebgp` | Value is converted to lower case.<br>Valid Values:<br>- <code>ebgp</code><br>- <code>ibgp</code><br>- <code>her</code><br>- <code>cvx</code><br>- <code>none</code> | Set the default overlay routing_protocol.<br>Can be overridden by setting "overlay_routing_protocol" host/group_vars.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_mpls_overlay_role</samp>](## "node_type_keys.[].default_mpls_overlay_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code><br>- <code>none</code> | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_overlay_address_families</samp>](## "node_type_keys.[].default_overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "node_type_keys.[].default_overlay_address_families.[]") | String |  |  | Value is converted to lower case.<br>Valid Values:<br>- <code>evpn</code><br>- <code>vpn-ipv4</code><br>- <code>vpn-ipv6</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_evpn_encapsulation</samp>](## "node_type_keys.[].default_evpn_encapsulation") | String |  |  | Value is converted to lower case.<br>Valid Values:<br>- <code>mpls</code><br>- <code>vxlan</code> | Set the default evpn encapsulation.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_support</samp>](## "node_type_keys.[].mlag_support") | Boolean |  | `False` |  | Can this node type support mlag. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;network_services</samp>](## "node_type_keys.[].network_services") | Dictionary |  |  |  | Will network services be deployed on this node type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l1</samp>](## "node_type_keys.[].network_services.l1") | Boolean |  | `False` |  | ?? |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l2</samp>](## "node_type_keys.[].network_services.l2") | Boolean |  | `False` |  | Vlans |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3</samp>](## "node_type_keys.[].network_services.l3") | Boolean |  | `False` |  | VRFs, SVIs (if l2 is true).<br>Only supported with underlay_router.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;underlay_router</samp>](## "node_type_keys.[].underlay_router") | Boolean |  | `True` |  | Is this node type a L3 device. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_type</samp>](## "node_type_keys.[].uplink_type") | String |  | `p2p` | Valid Values:<br>- <code>p2p</code><br>- <code>port-channel</code> | `uplink_type` must be "p2p" if `vtep` or `underlay_router` is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep</samp>](## "node_type_keys.[].vtep") | Boolean |  | `False` |  | Is this switch an EVPN VTEP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_lsr</samp>](## "node_type_keys.[].mpls_lsr") | Boolean |  | `False` |  | Is this switch an MPLS LSR. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_addressing</samp>](## "node_type_keys.[].ip_addressing") | Dictionary |  |  |  | Override ip_addressing templates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python_module</samp>](## "node_type_keys.[].ip_addressing.python_module") | String |  |  |  | Custom Python Module to import for IP addressing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python_class_name</samp>](## "node_type_keys.[].ip_addressing.python_class_name") | String |  |  |  | Name of Custom Python Class to import for IP addressing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "node_type_keys.[].ip_addressing.router_id") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id_ipv6</samp>](## "node_type_keys.[].ip_addressing.router_id_ipv6") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ip_primary</samp>](## "node_type_keys.[].ip_addressing.mlag_ip_primary") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ip_secondary</samp>](## "node_type_keys.[].ip_addressing.mlag_ip_secondary") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_l3_ip_primary</samp>](## "node_type_keys.[].ip_addressing.mlag_l3_ip_primary") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_l3_ip_secondary</samp>](## "node_type_keys.[].ip_addressing.mlag_l3_ip_secondary") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_peering_ip_primary</samp>](## "node_type_keys.[].ip_addressing.mlag_ibgp_peering_ip_primary") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_peering_ip_secondary</samp>](## "node_type_keys.[].ip_addressing.mlag_ibgp_peering_ip_secondary") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;p2p_uplinks_ip</samp>](## "node_type_keys.[].ip_addressing.p2p_uplinks_ip") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;p2p_uplinks_peer_ip</samp>](## "node_type_keys.[].ip_addressing.p2p_uplinks_peer_ip") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_ip_mlag</samp>](## "node_type_keys.[].ip_addressing.vtep_ip_mlag") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_ip</samp>](## "node_type_keys.[].ip_addressing.vtep_ip") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_descriptions</samp>](## "node_type_keys.[].interface_descriptions") | Dictionary |  |  |  | Override interface_descriptions templates<br>If description templates use Jinja2, they have to strip whitespaces using {%- -%} on any code blocks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python_module</samp>](## "node_type_keys.[].interface_descriptions.python_module") | String |  |  |  | Custom Python Module to import for interface descriptions. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python_class_name</samp>](## "node_type_keys.[].interface_descriptions.python_class_name") | String |  |  |  | Name of Custom Python Class to import for interface descriptions. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_ethernet_interfaces</samp>](## "node_type_keys.[].interface_descriptions.underlay_ethernet_interfaces") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_port_channel_interfaces</samp>](## "node_type_keys.[].interface_descriptions.underlay_port_channel_interfaces") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ethernet_interfaces</samp>](## "node_type_keys.[].interface_descriptions.mlag_ethernet_interfaces") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_interfaces</samp>](## "node_type_keys.[].interface_descriptions.mlag_port_channel_interfaces") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_endpoints_ethernet_interfaces</samp>](## "node_type_keys.[].interface_descriptions.connected_endpoints_ethernet_interfaces") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_endpoints_port_channel_interfaces</samp>](## "node_type_keys.[].interface_descriptions.connected_endpoints_port_channel_interfaces") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_loopback_interface</samp>](## "node_type_keys.[].interface_descriptions.overlay_loopback_interface") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_interface</samp>](## "node_type_keys.[].interface_descriptions.vtep_loopback_interface") | String |  |  |  | Path to Custom J2 template. |

=== "YAML"

    ```yaml
    # Define Node Type Keys, to specify the properties of each node type in the fabric.
    # This allows for complete customization of the fabric layout and functionality.
    # `node_type_keys` should be defined in top level group_var for the fabric.
    # The default values will be overridden if defining this key, so it is recommended to copy the defaults and modify them.
    node_type_keys:
      - key: <str; required; unique>

        # Type value matching this node_type_key.
        type: <str>

        # Are endpoints connected to this node type.
        connected_endpoints: <bool; default=False>

        # Default evpn_role. Can be overridden in topology vars.
        default_evpn_role: <str; "none" | "client" | "server"; default="none">

        # Default PTP priority 1
        default_ptp_priority1: <int; 0-255; default=127>

        # Set the default underlay routing_protocol.
        # Can be overridden by setting "underlay_routing_protocol" host/group_vars.
        default_underlay_routing_protocol: <str; "ebgp" | "ibgp" | "ospf" | "ospf-ldp" | "isis" | "isis-sr" | "isis-ldp" | "isis-sr-ldp" | "none"; default="ebgp">

        # Set the default overlay routing_protocol.
        # Can be overridden by setting "overlay_routing_protocol" host/group_vars.
        default_overlay_routing_protocol: <str; "ebgp" | "ibgp" | "her" | "cvx" | "none"; default="ebgp">

        # Set the default mpls overlay role.
        # Acting role in overlay control plane.
        default_mpls_overlay_role: <str; "client" | "server" | "none">

        # Set the default overlay address families.
        default_overlay_address_families:
          - <str; "evpn" | "vpn-ipv4" | "vpn-ipv6">

        # Set the default evpn encapsulation.
        default_evpn_encapsulation: <str; "mpls" | "vxlan">

        # Can this node type support mlag.
        mlag_support: <bool; default=False>

        # Will network services be deployed on this node type.
        network_services:

          # ??
          l1: <bool; default=False>

          # Vlans
          l2: <bool; default=False>

          # VRFs, SVIs (if l2 is true).
          # Only supported with underlay_router.
          l3: <bool; default=False>

        # Is this node type a L3 device.
        underlay_router: <bool; default=True>

        # `uplink_type` must be "p2p" if `vtep` or `underlay_router` is true.
        uplink_type: <str; "p2p" | "port-channel"; default="p2p">

        # Is this switch an EVPN VTEP.
        vtep: <bool; default=False>

        # Is this switch an MPLS LSR.
        mpls_lsr: <bool; default=False>

        # Override ip_addressing templates.
        ip_addressing:

          # Custom Python Module to import for IP addressing.
          python_module: <str>

          # Name of Custom Python Class to import for IP addressing.
          python_class_name: <str>

          # Path to Custom J2 template.
          router_id: <str>

          # Path to Custom J2 template.
          router_id_ipv6: <str>

          # Path to Custom J2 template.
          mlag_ip_primary: <str>

          # Path to Custom J2 template.
          mlag_ip_secondary: <str>

          # Path to Custom J2 template.
          mlag_l3_ip_primary: <str>

          # Path to Custom J2 template.
          mlag_l3_ip_secondary: <str>

          # Path to Custom J2 template.
          mlag_ibgp_peering_ip_primary: <str>

          # Path to Custom J2 template.
          mlag_ibgp_peering_ip_secondary: <str>

          # Path to Custom J2 template.
          p2p_uplinks_ip: <str>

          # Path to Custom J2 template.
          p2p_uplinks_peer_ip: <str>

          # Path to Custom J2 template.
          vtep_ip_mlag: <str>

          # Path to Custom J2 template.
          vtep_ip: <str>

        # Override interface_descriptions templates
        # If description templates use Jinja2, they have to strip whitespaces using {%- -%} on any code blocks.
        interface_descriptions:

          # Custom Python Module to import for interface descriptions.
          python_module: <str>

          # Name of Custom Python Class to import for interface descriptions.
          python_class_name: <str>

          # Path to Custom J2 template.
          underlay_ethernet_interfaces: <str>

          # Path to Custom J2 template.
          underlay_port_channel_interfaces: <str>

          # Path to Custom J2 template.
          mlag_ethernet_interfaces: <str>

          # Path to Custom J2 template.
          mlag_port_channel_interfaces: <str>

          # Path to Custom J2 template.
          connected_endpoints_ethernet_interfaces: <str>

          # Path to Custom J2 template.
          connected_endpoints_port_channel_interfaces: <str>

          # Path to Custom J2 template.
          overlay_loopback_interface: <str>

          # Path to Custom J2 template.
          vtep_loopback_interface: <str>
    ```
