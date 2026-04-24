<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;network_services_keys.name&gt;</samp>](## "<network_services_keys.name>") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "<network_services_keys.name>.[].vrfs") | List, items: Dictionary |  |  |  | VRFs will only be configured on a node if any of the underlying objects like `svis`, `l3_interfaces` or `l3_port_channels` apply to the node.<br><br>It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants<br>are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.<br><br>VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,<br>route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.<br>Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_ospf</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_ospf") | Dictionary |  |  |  | Router OSPFv3 configuration.<br>This will create an OSPFv3 routing instance in the tenant VRF. If there is no nodes definition, the OSPF instance will be<br>created on all leafs where the VRF is deployed.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;process_id</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_ospf.process_id") | Integer |  |  |  | If not set, "vrf_id" will be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_ospf.router_id") | String |  | `main_router_id` |  | Router ID to use for OSPF in this VRF.<br>This can be an IPv4 address, "main_router_id", "none" or "diagnostic_loopback".<br>- "main_router_id" will use the IP address of Loopback0 or the common `router general` Router ID if `use_router_general_for_router_id` is set."<br>- "none" will not configure a OSPF Router ID for this VRF. EOS will use the main OSPF Router ID.<br>- "diagnostic_loopback" will use the IP address of the VRF Diagnostic Loopback interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_bgp</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_ospf.redistribute_bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_ospf.redistribute_bgp.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_ospf.redistribute_bgp.route_map") | String |  |  |  | Route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_connected</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_ospf.redistribute_connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_ospf.redistribute_connected.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_ospf.redistribute_connected.route_map") | String |  |  |  | Route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_ospf.nodes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_ospf.nodes.[]") | String |  |  |  | Hostname. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_ospf.structured_config") | Dictionary |  |  |  | Custom structured config added under ipv6_router_ospf.process_ids.[process_id=<process_id>] for the EOS Config schema. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;svis</samp>](## "<network_services_keys.name>.[].vrfs.[].svis") | List, items: Dictionary |  |  |  | List of SVIs.<br>This will create both the L3 SVI and L2 VLAN based on filters applied to the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].id") | Integer | Required |  | Min: 1<br>Max: 4096 | SVI interface id and VLAN id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes") | List, items: Dictionary |  |  |  | Define node specific configuration, such as unique IP addresses.<br>Any keys set here will be merged onto the SVI config, except `structured_config` keys which will replace the `structured_config` set on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;node</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].node") | String | Required, Unique |  |  | Node inventory hostname. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_ospf</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ipv6_ospf") | Dictionary |  |  |  | OSPFv3 interface configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ipv6_ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ipv6_ospf.point_to_point") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ipv6_ospf.area") | String |  | `0.0.0.0` |  | OSPFv3 area ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_ospf</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ipv6_ospf") | Dictionary |  |  |  | OSPFv3 interface configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ipv6_ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ipv6_ospf.point_to_point") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ipv6_ospf.area") | String |  | `0.0.0.0` |  | OSPFv3 area ID. |
    | [<samp>svi_profiles</samp>](## "svi_profiles") | List, items: Dictionary |  |  |  | Profiles to share common settings for SVIs under `<network_services_key>.[].vrfs.svis`.<br>Keys are the same used under SVIs. Keys defined under SVIs take precedence.<br>Note: structured configuration is not merged recursively and will be taken directly from the most specific level in the following order:<br>1. svi.nodes[inventory_hostname].structured_config<br>2. svi_profile.nodes[inventory_hostname].structured_config<br>3. svi_parent_profile.nodes[inventory_hostname].structured_config<br>4. svi.structured_config<br>5. svi_profile.structured_config<br>6. svi_parent_profile.structured_config<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;profile</samp>](## "svi_profiles.[].profile") | String | Required, Unique |  |  | Profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "svi_profiles.[].nodes") | List, items: Dictionary |  |  |  | Define node specific configuration, such as unique IP addresses.<br>Any keys set here will be merged onto the SVI config, except `structured_config` keys which will replace the `structured_config` set on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;node</samp>](## "svi_profiles.[].nodes.[].node") | String | Required, Unique |  |  | Node inventory hostname. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_ospf</samp>](## "svi_profiles.[].nodes.[].ipv6_ospf") | Dictionary |  |  |  | OSPFv3 interface configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].ipv6_ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "svi_profiles.[].nodes.[].ipv6_ospf.point_to_point") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "svi_profiles.[].nodes.[].ipv6_ospf.area") | String |  | `0.0.0.0` |  | OSPFv3 area ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_ospf</samp>](## "svi_profiles.[].ipv6_ospf") | Dictionary |  |  |  | OSPFv3 interface configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].ipv6_ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "svi_profiles.[].ipv6_ospf.point_to_point") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "svi_profiles.[].ipv6_ospf.area") | String |  | `0.0.0.0` |  | OSPFv3 area ID. |

=== "YAML"

    ```yaml
    <network_services_keys.name>:

        # Specify a tenant name.
        # Tenant provide a construct to group L3 VRFs and L2 VLANs.
        # Networks services can be filtered by tenant name.
      - name: <str; required; unique>

        # VRFs will only be configured on a node if any of the underlying objects like `svis`, `l3_interfaces` or `l3_port_channels` apply to the node.
        #
        # It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants
        # are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.
        #
        # VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,
        # route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.
        # Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.
        vrfs:
          - name: <str; required; unique>

            # Router OSPFv3 configuration.
            # This will create an OSPFv3 routing instance in the tenant VRF. If there is no nodes definition, the OSPF instance will be
            # created on all leafs where the VRF is deployed.
            ipv6_ospf:
              enabled: <bool>

              # If not set, "vrf_id" will be used.
              process_id: <int>

              # Router ID to use for OSPF in this VRF.
              # This can be an IPv4 address, "main_router_id", "none" or "diagnostic_loopback".
              # - "main_router_id" will use the IP address of Loopback0 or the common `router general` Router ID if `use_router_general_for_router_id` is set."
              # - "none" will not configure a OSPF Router ID for this VRF. EOS will use the main OSPF Router ID.
              # - "diagnostic_loopback" will use the IP address of the VRF Diagnostic Loopback interface.
              router_id: <str; default="main_router_id">
              redistribute_bgp:
                enabled: <bool; default=True>

                # Route-map name.
                route_map: <str>
              redistribute_connected:
                enabled: <bool; default=False>

                # Route-map name.
                route_map: <str>
              nodes:

                  # Hostname.
                - <str>

              # Custom structured config added under ipv6_router_ospf.process_ids.[process_id=<process_id>] for the EOS Config schema.
              structured_config: <dict>

            # List of SVIs.
            # This will create both the L3 SVI and L2 VLAN based on filters applied to the node.
            svis:

                # SVI interface id and VLAN id.
              - id: <int; 1-4096; required>

                # Define node specific configuration, such as unique IP addresses.
                # Any keys set here will be merged onto the SVI config, except `structured_config` keys which will replace the `structured_config` set on SVI level.
                nodes:

                    # Node inventory hostname.
                  - node: <str; required; unique>

                    # OSPFv3 interface configuration.
                    ipv6_ospf:
                      enabled: <bool>
                      point_to_point: <bool; default=False>

                      # OSPFv3 area ID.
                      area: <str; default="0.0.0.0">

                # OSPFv3 interface configuration.
                ipv6_ospf:
                  enabled: <bool>
                  point_to_point: <bool; default=False>

                  # OSPFv3 area ID.
                  area: <str; default="0.0.0.0">

    # Profiles to share common settings for SVIs under `<network_services_key>.[].vrfs.svis`.
    # Keys are the same used under SVIs. Keys defined under SVIs take precedence.
    # Note: structured configuration is not merged recursively and will be taken directly from the most specific level in the following order:
    # 1. svi.nodes[inventory_hostname].structured_config
    # 2. svi_profile.nodes[inventory_hostname].structured_config
    # 3. svi_parent_profile.nodes[inventory_hostname].structured_config
    # 4. svi.structured_config
    # 5. svi_profile.structured_config
    # 6. svi_parent_profile.structured_config
    svi_profiles:

        # Profile name.
      - profile: <str; required; unique>

        # Define node specific configuration, such as unique IP addresses.
        # Any keys set here will be merged onto the SVI config, except `structured_config` keys which will replace the `structured_config` set on SVI level.
        nodes:

            # Node inventory hostname.
          - node: <str; required; unique>

            # OSPFv3 interface configuration.
            ipv6_ospf:
              enabled: <bool>
              point_to_point: <bool; default=False>

              # OSPFv3 area ID.
              area: <str; default="0.0.0.0">

        # OSPFv3 interface configuration.
        ipv6_ospf:
          enabled: <bool>
          point_to_point: <bool; default=False>

          # OSPFv3 area ID.
          area: <str; default="0.0.0.0">
    ```
