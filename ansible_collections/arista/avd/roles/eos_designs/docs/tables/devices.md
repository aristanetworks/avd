<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>device_profiles</samp>](## "device_profiles") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "device_profiles.[].name") | String | Required, Unique |  |  | Profile Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;parent_profile</samp>](## "device_profiles.[].parent_profile") | String |  |  |  | Inherit settings from a parent profile defined under `device_profiles`.<br>Max two levels of profiles and a role, device -> profile -> parent_profile -> role |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "device_profiles.[].role") | String |  |  |  | Inherit settings from a role defined under `device_roles`.<br>Max two levels of profiles and a role, device -> profile -> parent_profile -> role |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_group</samp>](## "device_profiles.[].mlag_group") | String |  |  |  | Name of MLAG group. Exactly two devices must share the same mlag_group.<br>The group is used for creating MLAG Pairs, for port-channel descriptions on peers and for MLAG domain-id (unless mlag_domain_id is set). |
    | [<samp>device_roles</samp>](## "device_roles") | List, items: Dictionary |  | See (+) on YAML tab |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "device_roles.[].name") | String | Required, Unique |  |  | Role Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_lsr</samp>](## "device_roles.[].mpls_lsr") | Boolean |  | `False` |  | Is this switch an MPLS LSR. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;connected_endpoints</samp>](## "device_roles.[].connected_endpoints") | Boolean |  | `False` |  | Are endpoints connected to this node type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_encapsulation</samp>](## "device_roles.[].evpn_encapsulation") | String |  | `vxlan` | Value is converted to lower case.<br>Valid Values:<br>- <code>mpls</code><br>- <code>vxlan</code> | Set the default evpn encapsulation.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_support</samp>](## "device_roles.[].mlag_support") | Boolean |  | `False` |  | Can this node type support mlag. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;network_services</samp>](## "device_roles.[].network_services") | Dictionary |  |  |  | Will network services be deployed on this node type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l1</samp>](## "device_roles.[].network_services.l1") | Boolean |  | `False` |  | Point-to-point services |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l2</samp>](## "device_roles.[].network_services.l2") | Boolean |  | `False` |  | Vlans |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3</samp>](## "device_roles.[].network_services.l3") | Boolean |  | `False` |  | VRFs, SVIs (if l2 is true).<br>Only supported with underlay_router.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;underlay_router</samp>](## "device_roles.[].underlay_router") | Boolean |  | `True` |  | Is this node type a L3 device. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;overlay_routing_protocol</samp>](## "device_roles.[].overlay_routing_protocol") | String |  | `ebgp` | Value is converted to lower case.<br>Valid Values:<br>- <code>ebgp</code><br>- <code>ibgp</code><br>- <code>her</code><br>- <code>cvx</code><br>- <code>none</code> | Set the default overlay routing_protocol.<br>Can be overridden by setting "overlay_routing_protocol" host/group_vars.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;custom_ip_addressing</samp>](## "device_roles.[].custom_ip_addressing") | Dictionary |  |  |  | Override ip_addressing templates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python_module</samp>](## "device_roles.[].custom_ip_addressing.python_module") | String |  |  |  | Custom Python Module to import for IP addressing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python_class_name</samp>](## "device_roles.[].custom_ip_addressing.python_class_name") | String |  | `AvdIpAddressing` |  | Name of Custom Python Class to import for IP addressing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "device_roles.[].custom_ip_addressing.router_id") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id_ipv6</samp>](## "device_roles.[].custom_ip_addressing.router_id_ipv6") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ip_primary</samp>](## "device_roles.[].custom_ip_addressing.mlag_ip_primary") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ip_secondary</samp>](## "device_roles.[].custom_ip_addressing.mlag_ip_secondary") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_l3_ip_primary</samp>](## "device_roles.[].custom_ip_addressing.mlag_l3_ip_primary") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_l3_ip_secondary</samp>](## "device_roles.[].custom_ip_addressing.mlag_l3_ip_secondary") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_peering_ip_primary</samp>](## "device_roles.[].custom_ip_addressing.mlag_ibgp_peering_ip_primary") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_peering_ip_secondary</samp>](## "device_roles.[].custom_ip_addressing.mlag_ibgp_peering_ip_secondary") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;p2p_uplinks_ip</samp>](## "device_roles.[].custom_ip_addressing.p2p_uplinks_ip") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;p2p_uplinks_peer_ip</samp>](## "device_roles.[].custom_ip_addressing.p2p_uplinks_peer_ip") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_ip_mlag</samp>](## "device_roles.[].custom_ip_addressing.vtep_ip_mlag") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_ip</samp>](## "device_roles.[].custom_ip_addressing.vtep_ip") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;custom_interface_descriptions</samp>](## "device_roles.[].custom_interface_descriptions") | Dictionary |  |  |  | Override interface_descriptions templates.<br>If description templates use Jinja2, they have to strip whitespaces using {%- -%} on any code blocks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python_module</samp>](## "device_roles.[].custom_interface_descriptions.python_module") | String |  |  |  | Custom Python Module to import for interface descriptions. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python_class_name</samp>](## "device_roles.[].custom_interface_descriptions.python_class_name") | String |  | `AvdInterfaceDescriptions` |  | Name of Custom Python Class to import for interface descriptions. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_ethernet_interfaces</samp>](## "device_roles.[].custom_interface_descriptions.underlay_ethernet_interfaces") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_port_channel_interfaces</samp>](## "device_roles.[].custom_interface_descriptions.underlay_port_channel_interfaces") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ethernet_interfaces</samp>](## "device_roles.[].custom_interface_descriptions.mlag_ethernet_interfaces") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_interfaces</samp>](## "device_roles.[].custom_interface_descriptions.mlag_port_channel_interfaces") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_endpoints_ethernet_interfaces</samp>](## "device_roles.[].custom_interface_descriptions.connected_endpoints_ethernet_interfaces") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_endpoints_port_channel_interfaces</samp>](## "device_roles.[].custom_interface_descriptions.connected_endpoints_port_channel_interfaces") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id_loopback_interface</samp>](## "device_roles.[].custom_interface_descriptions.router_id_loopback_interface") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_interface</samp>](## "device_roles.[].custom_interface_descriptions.vtep_loopback_interface") | String |  |  |  | Path to Custom J2 template. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_loopback_interface</samp>](## "device_roles.[].custom_interface_descriptions.overlay_loopback_interface") <span style="color:red">removed</span> | String |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>router_id_loopback_interface</samp> instead.</span> |
    | [<samp>devices</samp>](## "devices") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;-&nbsp;profile</samp>](## "devices.[].profile") | String |  |  |  | Inherit settings from a profile defined under `device_profiles`.<br>Max two levels of profiles and a role, device -> profile -> parent_profile -> role |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "devices.[].role") | String |  |  |  | Inherit settings from a role defined under `device_roles`.<br>Max two levels of profiles and a role, device -> profile -> parent_profile -> role |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_group</samp>](## "devices.[].mlag_group") | String |  |  |  | Name of MLAG group. Exactly two devices must share the same mlag_group.<br>The group is used for creating MLAG Pairs, for port-channel descriptions on peers and for MLAG domain-id (unless mlag_domain_id is set). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "devices.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>match_devices</samp>](## "match_devices") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time.<br>If a device is not defined under `devices`, AVD will check for a matching entry here, and apply the device settings for the first match. |
    | [<samp>&nbsp;&nbsp;-&nbsp;hostname_pattern</samp>](## "match_devices.[].hostname_pattern") | String | Required, Unique |  |  | Regex pattern matching the full inventory hostname of one or more devices. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "match_devices.[].name") | String |  |  |  | Do not set. T O D O: Rearrange schema so we can remove name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "match_devices.[].profile") | String |  |  |  | Inherit settings from a profile defined under `device_profiles`.<br>Max two levels of profiles and a role, device -> profile -> parent_profile -> role |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "match_devices.[].role") | String |  |  |  | Inherit settings from a role defined under `device_roles`.<br>Max two levels of profiles and a role, device -> profile -> parent_profile -> role |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_group</samp>](## "match_devices.[].mlag_group") | String |  |  |  | Name of MLAG group. Exactly two devices must share the same mlag_group.<br>The group is used for creating MLAG Pairs, for port-channel descriptions on peers and for MLAG domain-id (unless mlag_domain_id is set). |

=== "YAML"

    ```yaml
    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    device_profiles:

        # Profile Name
      - name: <str; required; unique>

        # Inherit settings from a parent profile defined under `device_profiles`.
        # Max two levels of profiles and a role, device -> profile -> parent_profile -> role
        parent_profile: <str>

        # Inherit settings from a role defined under `device_roles`.
        # Max two levels of profiles and a role, device -> profile -> parent_profile -> role
        role: <str>

        # Name of MLAG group. Exactly two devices must share the same mlag_group.
        # The group is used for creating MLAG Pairs, for port-channel descriptions on peers and for MLAG domain-id (unless mlag_domain_id is set).
        mlag_group: <str>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    device_roles: # (1)!

        # Role Name
      - name: <str; required; unique>

        # Is this switch an MPLS LSR.
        mpls_lsr: <bool; default=False>

        # Are endpoints connected to this node type.
        connected_endpoints: <bool; default=False>

        # Set the default evpn encapsulation.
        evpn_encapsulation: <str; "mpls" | "vxlan"; default="vxlan">

        # Can this node type support mlag.
        mlag_support: <bool; default=False>

        # Will network services be deployed on this node type.
        network_services:

          # Point-to-point services
          l1: <bool; default=False>

          # Vlans
          l2: <bool; default=False>

          # VRFs, SVIs (if l2 is true).
          # Only supported with underlay_router.
          l3: <bool; default=False>

        # Is this node type a L3 device.
        underlay_router: <bool; default=True>

        # Set the default overlay routing_protocol.
        # Can be overridden by setting "overlay_routing_protocol" host/group_vars.
        overlay_routing_protocol: <str; "ebgp" | "ibgp" | "her" | "cvx" | "none"; default="ebgp">

        # Override ip_addressing templates.
        custom_ip_addressing:

          # Custom Python Module to import for IP addressing.
          python_module: <str>

          # Name of Custom Python Class to import for IP addressing.
          python_class_name: <str; default="AvdIpAddressing">

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

        # Override interface_descriptions templates.
        # If description templates use Jinja2, they have to strip whitespaces using {%- -%} on any code blocks.
        custom_interface_descriptions:

          # Custom Python Module to import for interface descriptions.
          python_module: <str>

          # Name of Custom Python Class to import for interface descriptions.
          python_class_name: <str; default="AvdInterfaceDescriptions">

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
          router_id_loopback_interface: <str>

          # Path to Custom J2 template.
          vtep_loopback_interface: <str>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    devices:

        # Inherit settings from a profile defined under `device_profiles`.
        # Max two levels of profiles and a role, device -> profile -> parent_profile -> role
      - profile: <str>

        # Inherit settings from a role defined under `device_roles`.
        # Max two levels of profiles and a role, device -> profile -> parent_profile -> role
        role: <str>

        # Name of MLAG group. Exactly two devices must share the same mlag_group.
        # The group is used for creating MLAG Pairs, for port-channel descriptions on peers and for MLAG domain-id (unless mlag_domain_id is set).
        mlag_group: <str>

        # The Node Name is used as "hostname".
        name: <str; required; unique>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    # If a device is not defined under `devices`, AVD will check for a matching entry here, and apply the device settings for the first match.
    match_devices:

        # Regex pattern matching the full inventory hostname of one or more devices.
      - hostname_pattern: <str; required; unique>

        # Do not set. T O D O: Rearrange schema so we can remove name
        name: <str>

        # Inherit settings from a profile defined under `device_profiles`.
        # Max two levels of profiles and a role, device -> profile -> parent_profile -> role
        profile: <str>

        # Inherit settings from a role defined under `device_roles`.
        # Max two levels of profiles and a role, device -> profile -> parent_profile -> role
        role: <str>

        # Name of MLAG group. Exactly two devices must share the same mlag_group.
        # The group is used for creating MLAG Pairs, for port-channel descriptions on peers and for MLAG domain-id (unless mlag_domain_id is set).
        mlag_group: <str>
    ```

    1. Default Value

        ```yaml
        device_roles:
        - name: spine
          evpn_role: server
          ptp:
            priority1: 20
          cv_tags_topology_type: spine
        - name: l3leaf
          connected_endpoints: true
          evpn_role: client
          mlag_support: true
          network_services:
            l2: true
            l3: true
          vtep: true
          ptp:
            priority1: 30
          cv_tags_topology_type: leaf
        - name: l2leaf
          connected_endpoints: true
          mlag_support: true
          network_services:
            l2: true
          underlay_router: false
          uplink_type: port-channel
          cv_tags_topology_type: leaf
        ```
