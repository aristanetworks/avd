<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "<node_type_keys.key>.defaults.mpls_overlay_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code><br>- <code>none</code> | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "<node_type_keys.key>.defaults.overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.defaults.overlay_address_families.[]") | String |  |  | Valid Values:<br>- <code>evpn</code><br>- <code>vpn-ipv4</code><br>- <code>vpn-ipv6</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "<node_type_keys.key>.defaults.mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.defaults.mpls_route_reflectors.[]") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "<node_type_keys.key>.defaults.bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mpls_overlay_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code><br>- <code>none</code> | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].overlay_address_families.[]") | String |  |  | Valid Values:<br>- <code>evpn</code><br>- <code>vpn-ipv4</code><br>- <code>vpn-ipv6</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mpls_route_reflectors.[]") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "<node_type_keys.key>.node_groups.[].mpls_overlay_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code><br>- <code>none</code> | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "<node_type_keys.key>.node_groups.[].overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].overlay_address_families.[]") | String |  |  | Valid Values:<br>- <code>evpn</code><br>- <code>vpn-ipv4</code><br>- <code>vpn-ipv6</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "<node_type_keys.key>.node_groups.[].mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].mpls_route_reflectors.[]") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "<node_type_keys.key>.node_groups.[].bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "<node_type_keys.key>.nodes.[].mpls_overlay_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code><br>- <code>none</code> | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "<node_type_keys.key>.nodes.[].overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.nodes.[].overlay_address_families.[]") | String |  |  | Valid Values:<br>- <code>evpn</code><br>- <code>vpn-ipv4</code><br>- <code>vpn-ipv6</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "<node_type_keys.key>.nodes.[].mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.nodes.[].mpls_route_reflectors.[]") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "<node_type_keys.key>.nodes.[].bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |
    | [<samp>device_profiles</samp>](## "device_profiles") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "device_profiles.[].name") | String | Required, Unique |  |  | Profile Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "device_profiles.[].mpls_overlay_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code><br>- <code>none</code> | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "device_profiles.[].overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "device_profiles.[].overlay_address_families.[]") | String |  |  | Valid Values:<br>- <code>evpn</code><br>- <code>vpn-ipv4</code><br>- <code>vpn-ipv6</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "device_profiles.[].mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "device_profiles.[].mpls_route_reflectors.[]") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "device_profiles.[].bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |
    | [<samp>device_roles</samp>](## "device_roles") | List, items: Dictionary |  | See (+) on YAML tab |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "device_roles.[].name") | String | Required, Unique |  |  | Role Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "device_roles.[].overlay_address_families") | List, items: String |  | `['evpn']` |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "device_roles.[].overlay_address_families.[]") | String |  |  | Valid Values:<br>- <code>evpn</code><br>- <code>vpn-ipv4</code><br>- <code>vpn-ipv6</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "device_roles.[].mpls_overlay_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code><br>- <code>none</code> | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "device_roles.[].mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "device_roles.[].mpls_route_reflectors.[]") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "device_roles.[].bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |
    | [<samp>devices</samp>](## "devices") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "devices.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "devices.[].mpls_overlay_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code><br>- <code>none</code> | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "devices.[].overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "devices.[].overlay_address_families.[]") | String |  |  | Valid Values:<br>- <code>evpn</code><br>- <code>vpn-ipv4</code><br>- <code>vpn-ipv6</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "devices.[].mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "devices.[].mpls_route_reflectors.[]") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "devices.[].bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |
    | [<samp>match_devices</samp>](## "match_devices") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time.<br>If a device is not defined under `devices`, AVD will check for a matching entry here, and apply the device settings for the first match. |
    | [<samp>&nbsp;&nbsp;-&nbsp;hostname_pattern</samp>](## "match_devices.[].hostname_pattern") | String | Required, Unique |  |  | Regex pattern matching the full inventory hostname of one or more devices. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "match_devices.[].mpls_overlay_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code><br>- <code>none</code> | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "match_devices.[].overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "match_devices.[].overlay_address_families.[]") | String |  |  | Valid Values:<br>- <code>evpn</code><br>- <code>vpn-ipv4</code><br>- <code>vpn-ipv6</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "match_devices.[].mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "match_devices.[].mpls_route_reflectors.[]") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "match_devices.[].bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # Set the default mpls overlay role.
        # Acting role in overlay control plane.
        mpls_overlay_role: <str; "client" | "server" | "none">

        # Set the default overlay address families.
        overlay_address_families:
          - <str; "evpn" | "vpn-ipv4" | "vpn-ipv6">

        # List of inventory hostname acting as MPLS route-reflectors.
        mpls_route_reflectors:

            # Inventory_hostname_of_mpls_route_reflectors.
          - <str>

        # Set BGP cluster id.
        bgp_cluster_id: <str>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # Set the default mpls overlay role.
              # Acting role in overlay control plane.
              mpls_overlay_role: <str; "client" | "server" | "none">

              # Set the default overlay address families.
              overlay_address_families:
                - <str; "evpn" | "vpn-ipv4" | "vpn-ipv6">

              # List of inventory hostname acting as MPLS route-reflectors.
              mpls_route_reflectors:

                  # Inventory_hostname_of_mpls_route_reflectors.
                - <str>

              # Set BGP cluster id.
              bgp_cluster_id: <str>

          # Set the default mpls overlay role.
          # Acting role in overlay control plane.
          mpls_overlay_role: <str; "client" | "server" | "none">

          # Set the default overlay address families.
          overlay_address_families:
            - <str; "evpn" | "vpn-ipv4" | "vpn-ipv6">

          # List of inventory hostname acting as MPLS route-reflectors.
          mpls_route_reflectors:

              # Inventory_hostname_of_mpls_route_reflectors.
            - <str>

          # Set BGP cluster id.
          bgp_cluster_id: <str>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # Set the default mpls overlay role.
          # Acting role in overlay control plane.
          mpls_overlay_role: <str; "client" | "server" | "none">

          # Set the default overlay address families.
          overlay_address_families:
            - <str; "evpn" | "vpn-ipv4" | "vpn-ipv6">

          # List of inventory hostname acting as MPLS route-reflectors.
          mpls_route_reflectors:

              # Inventory_hostname_of_mpls_route_reflectors.
            - <str>

          # Set BGP cluster id.
          bgp_cluster_id: <str>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    device_profiles:

        # Profile Name
      - name: <str; required; unique>

        # Set the default mpls overlay role.
        # Acting role in overlay control plane.
        mpls_overlay_role: <str; "client" | "server" | "none">

        # Set the default overlay address families.
        overlay_address_families:
          - <str; "evpn" | "vpn-ipv4" | "vpn-ipv6">

        # List of inventory hostname acting as MPLS route-reflectors.
        mpls_route_reflectors:

            # Inventory_hostname_of_mpls_route_reflectors.
          - <str>

        # Set BGP cluster id.
        bgp_cluster_id: <str>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    device_roles: # (1)!

        # Role Name
      - name: <str; required; unique>

        # Set the default overlay address families.
        overlay_address_families: # default=['evpn']
          - <str; "evpn" | "vpn-ipv4" | "vpn-ipv6">

        # Set the default mpls overlay role.
        # Acting role in overlay control plane.
        mpls_overlay_role: <str; "client" | "server" | "none">

        # List of inventory hostname acting as MPLS route-reflectors.
        mpls_route_reflectors:

            # Inventory_hostname_of_mpls_route_reflectors.
          - <str>

        # Set BGP cluster id.
        bgp_cluster_id: <str>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    devices:

        # The Node Name is used as "hostname".
        name: <str; required; unique>

        # Set the default mpls overlay role.
        # Acting role in overlay control plane.
        mpls_overlay_role: <str; "client" | "server" | "none">

        # Set the default overlay address families.
        overlay_address_families:
          - <str; "evpn" | "vpn-ipv4" | "vpn-ipv6">

        # List of inventory hostname acting as MPLS route-reflectors.
        mpls_route_reflectors:

            # Inventory_hostname_of_mpls_route_reflectors.
          - <str>

        # Set BGP cluster id.
        bgp_cluster_id: <str>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    # If a device is not defined under `devices`, AVD will check for a matching entry here, and apply the device settings for the first match.
    match_devices:

        # Regex pattern matching the full inventory hostname of one or more devices.
      - hostname_pattern: <str; required; unique>

        # Set the default mpls overlay role.
        # Acting role in overlay control plane.
        mpls_overlay_role: <str; "client" | "server" | "none">

        # Set the default overlay address families.
        overlay_address_families:
          - <str; "evpn" | "vpn-ipv4" | "vpn-ipv6">

        # List of inventory hostname acting as MPLS route-reflectors.
        mpls_route_reflectors:

            # Inventory_hostname_of_mpls_route_reflectors.
          - <str>

        # Set BGP cluster id.
        bgp_cluster_id: <str>
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
