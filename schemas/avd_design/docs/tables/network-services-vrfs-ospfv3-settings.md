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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "<network_services_keys.name>.[].vrfs.[].ospfv3") | Dictionary |  |  |  | Router OSPFv3 settings for the VRF.<br>The OSPFv3 configuration is created automatically on a device when at least one OSPFv3-enabled SVI in this VRF is configured on that device.<br>These settings only override the defaults.<br>VRF `default` is not supported yet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "<network_services_keys.name>.[].vrfs.[].ospfv3.router_id") | String |  | `main_router_id` |  | Router ID to use for OSPFv3 in this VRF.<br>This can be an IPv4 address, "main_router_id", "none" or "diagnostic_loopback".<br>- "main_router_id" will use the IP address of Loopback0 or the common `router general` Router ID if `use_router_general_for_router_id` is set.<br>- "none" will not configure an OSPFv3 Router ID for this VRF.<br>  EOS then uses the `router general` Router ID or an IPv4 address of an interface in the VRF.<br>  If neither exists, for example in an IPv6-only VRF, the OSPFv3 instance does not start.<br>- "diagnostic_loopback" will use the IP address of the VRF Diagnostic Loopback interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_bgp</samp>](## "<network_services_keys.name>.[].vrfs.[].ospfv3.redistribute_bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].ospfv3.redistribute_bgp.enabled") | Boolean |  | `True` |  | Redistribute BGP into OSPFv3.<br>Ignored on devices where BGP is not configured for this VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_connected</samp>](## "<network_services_keys.name>.[].vrfs.[].ospfv3.redistribute_connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].ospfv3.redistribute_connected.enabled") | Boolean |  | `False` |  | Redistribute connected routes into OSPFv3. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<network_services_keys.name>.[].vrfs.[].ospfv3.structured_config") | Dictionary |  |  |  | Custom structured config added under router_ospfv3.vrfs.[name=<vrf>] for the EOS Config schema. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_ospfv3</samp>](## "<network_services_keys.name>.[].vrfs.[].redistribute_ospfv3") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].redistribute_ospfv3.enabled") | Boolean |  | `True` |  | Redistribute OSPFv3 internal routes into BGP for this VRF.<br>Ignored on devices where BGP is not configured for this VRF or where the VRF has no OSPFv3 instance.<br>OSPFv3 external routes are not redistributed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;svis</samp>](## "<network_services_keys.name>.[].vrfs.[].svis") | List, items: Dictionary |  |  |  | List of SVIs.<br>This will create both the L3 SVI and L2 VLAN based on filters applied to the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].id") | Integer | Required |  | Min: 1<br>Max: 4096 | SVI interface id and VLAN id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes") | List, items: Dictionary |  |  |  | Define node specific configuration, such as unique IP addresses.<br>Any keys set here will be merged onto the SVI config, except `structured_config` keys which will replace the `structured_config` set on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;node</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].node") | String | Required, Unique |  |  | Node inventory hostname. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ospfv3") | Dictionary |  |  |  | OSPFv3 interface configuration.<br>Enabling OSPFv3 on an SVI automatically creates the OSPFv3 configuration for the VRF of the SVI on the device.<br>Only the IPv6 address family is currently supported.<br>SVIs with IPv4 addressing require `ospfv3.ipv4.enabled: false`.<br>OSPFv3 uses the IPv6 link-local address of the SVI, so `ipv6_enable: true` is set automatically on SVIs without `ipv6_address` (`ipv6_enable: false` is not supported).<br>Anycast IPv6 (`ipv6_address_virtuals`) is not supported.<br>SVIs extended over VXLAN are not supported. Set `vxlan: false` on the SVI.<br>VRF `default` and SVIs deployed as subinterfaces with `uplink_type: lan` are not supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ospfv3.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ospfv3.area") | String |  | `0.0.0.0` |  | OSPFv3 area ID in IPv4 address or decimal format (range 0 to 4294967295). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ospfv3.point_to_point") | Boolean |  | `False` |  | Configure the OSPFv3 network type as point-to-point. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ospfv3.passive") | Boolean |  | `False` |  | Advertise the SVI subnet into OSPFv3 without forming adjacencies.<br>By default, OSPFv3-enabled SVIs are configured with `no ospfv3 passive-interface`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ospfv3.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ospfv3.ipv4.enabled") | Boolean |  |  |  | Set to `false` to exclude the IPv4 address family from OSPFv3 on an SVI with IPv4 addressing.<br>The IPv4 address family is not supported yet, so `true` raises an error.<br>An SVI with IPv4 addressing also raises an error unless this is set to `false`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ospfv3") | Dictionary |  |  |  | OSPFv3 interface configuration.<br>Enabling OSPFv3 on an SVI automatically creates the OSPFv3 configuration for the VRF of the SVI on the device.<br>Only the IPv6 address family is currently supported.<br>SVIs with IPv4 addressing require `ospfv3.ipv4.enabled: false`.<br>OSPFv3 uses the IPv6 link-local address of the SVI, so `ipv6_enable: true` is set automatically on SVIs without `ipv6_address` (`ipv6_enable: false` is not supported).<br>Anycast IPv6 (`ipv6_address_virtuals`) is not supported.<br>SVIs extended over VXLAN are not supported. Set `vxlan: false` on the SVI.<br>VRF `default` and SVIs deployed as subinterfaces with `uplink_type: lan` are not supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ospfv3.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ospfv3.area") | String |  | `0.0.0.0` |  | OSPFv3 area ID in IPv4 address or decimal format (range 0 to 4294967295). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ospfv3.point_to_point") | Boolean |  | `False` |  | Configure the OSPFv3 network type as point-to-point. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ospfv3.passive") | Boolean |  | `False` |  | Advertise the SVI subnet into OSPFv3 without forming adjacencies.<br>By default, OSPFv3-enabled SVIs are configured with `no ospfv3 passive-interface`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ospfv3.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ospfv3.ipv4.enabled") | Boolean |  |  |  | Set to `false` to exclude the IPv4 address family from OSPFv3 on an SVI with IPv4 addressing.<br>The IPv4 address family is not supported yet, so `true` raises an error.<br>An SVI with IPv4 addressing also raises an error unless this is set to `false`. |
    | [<samp>network_services</samp>](## "network_services") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "network_services.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "network_services.[].vrfs") | List, items: Dictionary |  |  |  | VRFs will only be configured on a node if any of the underlying objects like `svis`, `l3_interfaces` or `l3_port_channels` apply to the node.<br><br>It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants<br>are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.<br><br>VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,<br>route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.<br>Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "network_services.[].vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "network_services.[].vrfs.[].ospfv3") | Dictionary |  |  |  | Router OSPFv3 settings for the VRF.<br>The OSPFv3 configuration is created automatically on a device when at least one OSPFv3-enabled SVI in this VRF is configured on that device.<br>These settings only override the defaults.<br>VRF `default` is not supported yet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "network_services.[].vrfs.[].ospfv3.router_id") | String |  | `main_router_id` |  | Router ID to use for OSPFv3 in this VRF.<br>This can be an IPv4 address, "main_router_id", "none" or "diagnostic_loopback".<br>- "main_router_id" will use the IP address of Loopback0 or the common `router general` Router ID if `use_router_general_for_router_id` is set.<br>- "none" will not configure an OSPFv3 Router ID for this VRF.<br>  EOS then uses the `router general` Router ID or an IPv4 address of an interface in the VRF.<br>  If neither exists, for example in an IPv6-only VRF, the OSPFv3 instance does not start.<br>- "diagnostic_loopback" will use the IP address of the VRF Diagnostic Loopback interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_bgp</samp>](## "network_services.[].vrfs.[].ospfv3.redistribute_bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].vrfs.[].ospfv3.redistribute_bgp.enabled") | Boolean |  | `True` |  | Redistribute BGP into OSPFv3.<br>Ignored on devices where BGP is not configured for this VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_connected</samp>](## "network_services.[].vrfs.[].ospfv3.redistribute_connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].vrfs.[].ospfv3.redistribute_connected.enabled") | Boolean |  | `False` |  | Redistribute connected routes into OSPFv3. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "network_services.[].vrfs.[].ospfv3.structured_config") | Dictionary |  |  |  | Custom structured config added under router_ospfv3.vrfs.[name=<vrf>] for the EOS Config schema. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_ospfv3</samp>](## "network_services.[].vrfs.[].redistribute_ospfv3") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].vrfs.[].redistribute_ospfv3.enabled") | Boolean |  | `True` |  | Redistribute OSPFv3 internal routes into BGP for this VRF.<br>Ignored on devices where BGP is not configured for this VRF or where the VRF has no OSPFv3 instance.<br>OSPFv3 external routes are not redistributed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;svis</samp>](## "network_services.[].vrfs.[].svis") | List, items: Dictionary |  |  |  | List of SVIs.<br>This will create both the L3 SVI and L2 VLAN based on filters applied to the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "network_services.[].vrfs.[].svis.[].id") | Integer | Required |  | Min: 1<br>Max: 4096 | SVI interface id and VLAN id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "network_services.[].vrfs.[].svis.[].nodes") | List, items: Dictionary |  |  |  | Define node specific configuration, such as unique IP addresses.<br>Any keys set here will be merged onto the SVI config, except `structured_config` keys which will replace the `structured_config` set on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;node</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].node") | String | Required, Unique |  |  | Node inventory hostname. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].ospfv3") | Dictionary |  |  |  | OSPFv3 interface configuration.<br>Enabling OSPFv3 on an SVI automatically creates the OSPFv3 configuration for the VRF of the SVI on the device.<br>Only the IPv6 address family is currently supported.<br>SVIs with IPv4 addressing require `ospfv3.ipv4.enabled: false`.<br>OSPFv3 uses the IPv6 link-local address of the SVI, so `ipv6_enable: true` is set automatically on SVIs without `ipv6_address` (`ipv6_enable: false` is not supported).<br>Anycast IPv6 (`ipv6_address_virtuals`) is not supported.<br>SVIs extended over VXLAN are not supported. Set `vxlan: false` on the SVI.<br>VRF `default` and SVIs deployed as subinterfaces with `uplink_type: lan` are not supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].ospfv3.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].ospfv3.area") | String |  | `0.0.0.0` |  | OSPFv3 area ID in IPv4 address or decimal format (range 0 to 4294967295). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].ospfv3.point_to_point") | Boolean |  | `False` |  | Configure the OSPFv3 network type as point-to-point. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].ospfv3.passive") | Boolean |  | `False` |  | Advertise the SVI subnet into OSPFv3 without forming adjacencies.<br>By default, OSPFv3-enabled SVIs are configured with `no ospfv3 passive-interface`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].ospfv3.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].ospfv3.ipv4.enabled") | Boolean |  |  |  | Set to `false` to exclude the IPv4 address family from OSPFv3 on an SVI with IPv4 addressing.<br>The IPv4 address family is not supported yet, so `true` raises an error.<br>An SVI with IPv4 addressing also raises an error unless this is set to `false`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "network_services.[].vrfs.[].svis.[].ospfv3") | Dictionary |  |  |  | OSPFv3 interface configuration.<br>Enabling OSPFv3 on an SVI automatically creates the OSPFv3 configuration for the VRF of the SVI on the device.<br>Only the IPv6 address family is currently supported.<br>SVIs with IPv4 addressing require `ospfv3.ipv4.enabled: false`.<br>OSPFv3 uses the IPv6 link-local address of the SVI, so `ipv6_enable: true` is set automatically on SVIs without `ipv6_address` (`ipv6_enable: false` is not supported).<br>Anycast IPv6 (`ipv6_address_virtuals`) is not supported.<br>SVIs extended over VXLAN are not supported. Set `vxlan: false` on the SVI.<br>VRF `default` and SVIs deployed as subinterfaces with `uplink_type: lan` are not supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].vrfs.[].svis.[].ospfv3.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "network_services.[].vrfs.[].svis.[].ospfv3.area") | String |  | `0.0.0.0` |  | OSPFv3 area ID in IPv4 address or decimal format (range 0 to 4294967295). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "network_services.[].vrfs.[].svis.[].ospfv3.point_to_point") | Boolean |  | `False` |  | Configure the OSPFv3 network type as point-to-point. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive</samp>](## "network_services.[].vrfs.[].svis.[].ospfv3.passive") | Boolean |  | `False` |  | Advertise the SVI subnet into OSPFv3 without forming adjacencies.<br>By default, OSPFv3-enabled SVIs are configured with `no ospfv3 passive-interface`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "network_services.[].vrfs.[].svis.[].ospfv3.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].vrfs.[].svis.[].ospfv3.ipv4.enabled") | Boolean |  |  |  | Set to `false` to exclude the IPv4 address family from OSPFv3 on an SVI with IPv4 addressing.<br>The IPv4 address family is not supported yet, so `true` raises an error.<br>An SVI with IPv4 addressing also raises an error unless this is set to `false`. |
    | [<samp>svi_profiles</samp>](## "svi_profiles") | List, items: Dictionary |  |  |  | Profiles to share common settings for SVIs under `<network_services_key>.[].vrfs.svis`.<br>Keys are the same used under SVIs. Keys defined under SVIs take precedence.<br>Note: structured configuration is not merged recursively and will be taken directly from the most specific level in the following order:<br>1. svi.nodes[inventory_hostname].structured_config<br>2. svi_profile.nodes[inventory_hostname].structured_config<br>3. svi_parent_profile.nodes[inventory_hostname].structured_config<br>4. Further ancestor profiles' nodes[inventory_hostname].structured_config in nearest-to-farthest order (when recursive inheritance is enabled)<br>5. svi.structured_config<br>6. svi_profile.structured_config<br>7. svi_parent_profile.structured_config<br>8. Further ancestor profiles' structured_config in nearest-to-farthest order (when recursive inheritance is enabled)<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;profile</samp>](## "svi_profiles.[].profile") | String | Required, Unique |  |  | Profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "svi_profiles.[].nodes") | List, items: Dictionary |  |  |  | Define node specific configuration, such as unique IP addresses.<br>Any keys set here will be merged onto the SVI config, except `structured_config` keys which will replace the `structured_config` set on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;node</samp>](## "svi_profiles.[].nodes.[].node") | String | Required, Unique |  |  | Node inventory hostname. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "svi_profiles.[].nodes.[].ospfv3") | Dictionary |  |  |  | OSPFv3 interface configuration.<br>Enabling OSPFv3 on an SVI automatically creates the OSPFv3 configuration for the VRF of the SVI on the device.<br>Only the IPv6 address family is currently supported.<br>SVIs with IPv4 addressing require `ospfv3.ipv4.enabled: false`.<br>OSPFv3 uses the IPv6 link-local address of the SVI, so `ipv6_enable: true` is set automatically on SVIs without `ipv6_address` (`ipv6_enable: false` is not supported).<br>Anycast IPv6 (`ipv6_address_virtuals`) is not supported.<br>SVIs extended over VXLAN are not supported. Set `vxlan: false` on the SVI.<br>VRF `default` and SVIs deployed as subinterfaces with `uplink_type: lan` are not supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].ospfv3.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "svi_profiles.[].nodes.[].ospfv3.area") | String |  | `0.0.0.0` |  | OSPFv3 area ID in IPv4 address or decimal format (range 0 to 4294967295). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "svi_profiles.[].nodes.[].ospfv3.point_to_point") | Boolean |  | `False` |  | Configure the OSPFv3 network type as point-to-point. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive</samp>](## "svi_profiles.[].nodes.[].ospfv3.passive") | Boolean |  | `False` |  | Advertise the SVI subnet into OSPFv3 without forming adjacencies.<br>By default, OSPFv3-enabled SVIs are configured with `no ospfv3 passive-interface`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "svi_profiles.[].nodes.[].ospfv3.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].ospfv3.ipv4.enabled") | Boolean |  |  |  | Set to `false` to exclude the IPv4 address family from OSPFv3 on an SVI with IPv4 addressing.<br>The IPv4 address family is not supported yet, so `true` raises an error.<br>An SVI with IPv4 addressing also raises an error unless this is set to `false`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "svi_profiles.[].ospfv3") | Dictionary |  |  |  | OSPFv3 interface configuration.<br>Enabling OSPFv3 on an SVI automatically creates the OSPFv3 configuration for the VRF of the SVI on the device.<br>Only the IPv6 address family is currently supported.<br>SVIs with IPv4 addressing require `ospfv3.ipv4.enabled: false`.<br>OSPFv3 uses the IPv6 link-local address of the SVI, so `ipv6_enable: true` is set automatically on SVIs without `ipv6_address` (`ipv6_enable: false` is not supported).<br>Anycast IPv6 (`ipv6_address_virtuals`) is not supported.<br>SVIs extended over VXLAN are not supported. Set `vxlan: false` on the SVI.<br>VRF `default` and SVIs deployed as subinterfaces with `uplink_type: lan` are not supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].ospfv3.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "svi_profiles.[].ospfv3.area") | String |  | `0.0.0.0` |  | OSPFv3 area ID in IPv4 address or decimal format (range 0 to 4294967295). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "svi_profiles.[].ospfv3.point_to_point") | Boolean |  | `False` |  | Configure the OSPFv3 network type as point-to-point. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive</samp>](## "svi_profiles.[].ospfv3.passive") | Boolean |  | `False` |  | Advertise the SVI subnet into OSPFv3 without forming adjacencies.<br>By default, OSPFv3-enabled SVIs are configured with `no ospfv3 passive-interface`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "svi_profiles.[].ospfv3.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].ospfv3.ipv4.enabled") | Boolean |  |  |  | Set to `false` to exclude the IPv4 address family from OSPFv3 on an SVI with IPv4 addressing.<br>The IPv4 address family is not supported yet, so `true` raises an error.<br>An SVI with IPv4 addressing also raises an error unless this is set to `false`. |

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

            # Router OSPFv3 settings for the VRF.
            # The OSPFv3 configuration is created automatically on a device when at least one OSPFv3-enabled SVI in this VRF is configured on that device.
            # These settings only override the defaults.
            # VRF `default` is not supported yet.
            ospfv3:

              # Router ID to use for OSPFv3 in this VRF.
              # This can be an IPv4 address, "main_router_id", "none" or "diagnostic_loopback".
              # - "main_router_id" will use the IP address of Loopback0 or the common `router general` Router ID if `use_router_general_for_router_id` is set.
              # - "none" will not configure an OSPFv3 Router ID for this VRF.
              #   EOS then uses the `router general` Router ID or an IPv4 address of an interface in the VRF.
              #   If neither exists, for example in an IPv6-only VRF, the OSPFv3 instance does not start.
              # - "diagnostic_loopback" will use the IP address of the VRF Diagnostic Loopback interface.
              router_id: <str; default="main_router_id">
              redistribute_bgp:

                # Redistribute BGP into OSPFv3.
                # Ignored on devices where BGP is not configured for this VRF.
                enabled: <bool; default=True>
              redistribute_connected:

                # Redistribute connected routes into OSPFv3.
                enabled: <bool; default=False>

              # Custom structured config added under router_ospfv3.vrfs.[name=<vrf>] for the EOS Config schema.
              structured_config: <dict>
            redistribute_ospfv3:

              # Redistribute OSPFv3 internal routes into BGP for this VRF.
              # Ignored on devices where BGP is not configured for this VRF or where the VRF has no OSPFv3 instance.
              # OSPFv3 external routes are not redistributed.
              enabled: <bool; default=True>

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
                    # Enabling OSPFv3 on an SVI automatically creates the OSPFv3 configuration for the VRF of the SVI on the device.
                    # Only the IPv6 address family is currently supported.
                    # SVIs with IPv4 addressing require `ospfv3.ipv4.enabled: false`.
                    # OSPFv3 uses the IPv6 link-local address of the SVI, so `ipv6_enable: true` is set automatically on SVIs without `ipv6_address` (`ipv6_enable: false` is not supported).
                    # Anycast IPv6 (`ipv6_address_virtuals`) is not supported.
                    # SVIs extended over VXLAN are not supported. Set `vxlan: false` on the SVI.
                    # VRF `default` and SVIs deployed as subinterfaces with `uplink_type: lan` are not supported.
                    ospfv3:
                      enabled: <bool>

                      # OSPFv3 area ID in IPv4 address or decimal format (range 0 to 4294967295).
                      area: <str; default="0.0.0.0">

                      # Configure the OSPFv3 network type as point-to-point.
                      point_to_point: <bool; default=False>

                      # Advertise the SVI subnet into OSPFv3 without forming adjacencies.
                      # By default, OSPFv3-enabled SVIs are configured with `no ospfv3 passive-interface`.
                      passive: <bool; default=False>
                      ipv4:

                        # Set to `false` to exclude the IPv4 address family from OSPFv3 on an SVI with IPv4 addressing.
                        # The IPv4 address family is not supported yet, so `true` raises an error.
                        # An SVI with IPv4 addressing also raises an error unless this is set to `false`.
                        enabled: <bool>

                # OSPFv3 interface configuration.
                # Enabling OSPFv3 on an SVI automatically creates the OSPFv3 configuration for the VRF of the SVI on the device.
                # Only the IPv6 address family is currently supported.
                # SVIs with IPv4 addressing require `ospfv3.ipv4.enabled: false`.
                # OSPFv3 uses the IPv6 link-local address of the SVI, so `ipv6_enable: true` is set automatically on SVIs without `ipv6_address` (`ipv6_enable: false` is not supported).
                # Anycast IPv6 (`ipv6_address_virtuals`) is not supported.
                # SVIs extended over VXLAN are not supported. Set `vxlan: false` on the SVI.
                # VRF `default` and SVIs deployed as subinterfaces with `uplink_type: lan` are not supported.
                ospfv3:
                  enabled: <bool>

                  # OSPFv3 area ID in IPv4 address or decimal format (range 0 to 4294967295).
                  area: <str; default="0.0.0.0">

                  # Configure the OSPFv3 network type as point-to-point.
                  point_to_point: <bool; default=False>

                  # Advertise the SVI subnet into OSPFv3 without forming adjacencies.
                  # By default, OSPFv3-enabled SVIs are configured with `no ospfv3 passive-interface`.
                  passive: <bool; default=False>
                  ipv4:

                    # Set to `false` to exclude the IPv4 address family from OSPFv3 on an SVI with IPv4 addressing.
                    # The IPv4 address family is not supported yet, so `true` raises an error.
                    # An SVI with IPv4 addressing also raises an error unless this is set to `false`.
                    enabled: <bool>
    network_services:

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

            # Router OSPFv3 settings for the VRF.
            # The OSPFv3 configuration is created automatically on a device when at least one OSPFv3-enabled SVI in this VRF is configured on that device.
            # These settings only override the defaults.
            # VRF `default` is not supported yet.
            ospfv3:

              # Router ID to use for OSPFv3 in this VRF.
              # This can be an IPv4 address, "main_router_id", "none" or "diagnostic_loopback".
              # - "main_router_id" will use the IP address of Loopback0 or the common `router general` Router ID if `use_router_general_for_router_id` is set.
              # - "none" will not configure an OSPFv3 Router ID for this VRF.
              #   EOS then uses the `router general` Router ID or an IPv4 address of an interface in the VRF.
              #   If neither exists, for example in an IPv6-only VRF, the OSPFv3 instance does not start.
              # - "diagnostic_loopback" will use the IP address of the VRF Diagnostic Loopback interface.
              router_id: <str; default="main_router_id">
              redistribute_bgp:

                # Redistribute BGP into OSPFv3.
                # Ignored on devices where BGP is not configured for this VRF.
                enabled: <bool; default=True>
              redistribute_connected:

                # Redistribute connected routes into OSPFv3.
                enabled: <bool; default=False>

              # Custom structured config added under router_ospfv3.vrfs.[name=<vrf>] for the EOS Config schema.
              structured_config: <dict>
            redistribute_ospfv3:

              # Redistribute OSPFv3 internal routes into BGP for this VRF.
              # Ignored on devices where BGP is not configured for this VRF or where the VRF has no OSPFv3 instance.
              # OSPFv3 external routes are not redistributed.
              enabled: <bool; default=True>

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
                    # Enabling OSPFv3 on an SVI automatically creates the OSPFv3 configuration for the VRF of the SVI on the device.
                    # Only the IPv6 address family is currently supported.
                    # SVIs with IPv4 addressing require `ospfv3.ipv4.enabled: false`.
                    # OSPFv3 uses the IPv6 link-local address of the SVI, so `ipv6_enable: true` is set automatically on SVIs without `ipv6_address` (`ipv6_enable: false` is not supported).
                    # Anycast IPv6 (`ipv6_address_virtuals`) is not supported.
                    # SVIs extended over VXLAN are not supported. Set `vxlan: false` on the SVI.
                    # VRF `default` and SVIs deployed as subinterfaces with `uplink_type: lan` are not supported.
                    ospfv3:
                      enabled: <bool>

                      # OSPFv3 area ID in IPv4 address or decimal format (range 0 to 4294967295).
                      area: <str; default="0.0.0.0">

                      # Configure the OSPFv3 network type as point-to-point.
                      point_to_point: <bool; default=False>

                      # Advertise the SVI subnet into OSPFv3 without forming adjacencies.
                      # By default, OSPFv3-enabled SVIs are configured with `no ospfv3 passive-interface`.
                      passive: <bool; default=False>
                      ipv4:

                        # Set to `false` to exclude the IPv4 address family from OSPFv3 on an SVI with IPv4 addressing.
                        # The IPv4 address family is not supported yet, so `true` raises an error.
                        # An SVI with IPv4 addressing also raises an error unless this is set to `false`.
                        enabled: <bool>

                # OSPFv3 interface configuration.
                # Enabling OSPFv3 on an SVI automatically creates the OSPFv3 configuration for the VRF of the SVI on the device.
                # Only the IPv6 address family is currently supported.
                # SVIs with IPv4 addressing require `ospfv3.ipv4.enabled: false`.
                # OSPFv3 uses the IPv6 link-local address of the SVI, so `ipv6_enable: true` is set automatically on SVIs without `ipv6_address` (`ipv6_enable: false` is not supported).
                # Anycast IPv6 (`ipv6_address_virtuals`) is not supported.
                # SVIs extended over VXLAN are not supported. Set `vxlan: false` on the SVI.
                # VRF `default` and SVIs deployed as subinterfaces with `uplink_type: lan` are not supported.
                ospfv3:
                  enabled: <bool>

                  # OSPFv3 area ID in IPv4 address or decimal format (range 0 to 4294967295).
                  area: <str; default="0.0.0.0">

                  # Configure the OSPFv3 network type as point-to-point.
                  point_to_point: <bool; default=False>

                  # Advertise the SVI subnet into OSPFv3 without forming adjacencies.
                  # By default, OSPFv3-enabled SVIs are configured with `no ospfv3 passive-interface`.
                  passive: <bool; default=False>
                  ipv4:

                    # Set to `false` to exclude the IPv4 address family from OSPFv3 on an SVI with IPv4 addressing.
                    # The IPv4 address family is not supported yet, so `true` raises an error.
                    # An SVI with IPv4 addressing also raises an error unless this is set to `false`.
                    enabled: <bool>

    # Profiles to share common settings for SVIs under `<network_services_key>.[].vrfs.svis`.
    # Keys are the same used under SVIs. Keys defined under SVIs take precedence.
    # Note: structured configuration is not merged recursively and will be taken directly from the most specific level in the following order:
    # 1. svi.nodes[inventory_hostname].structured_config
    # 2. svi_profile.nodes[inventory_hostname].structured_config
    # 3. svi_parent_profile.nodes[inventory_hostname].structured_config
    # 4. Further ancestor profiles' nodes[inventory_hostname].structured_config in nearest-to-farthest order (when recursive inheritance is enabled)
    # 5. svi.structured_config
    # 6. svi_profile.structured_config
    # 7. svi_parent_profile.structured_config
    # 8. Further ancestor profiles' structured_config in nearest-to-farthest order (when recursive inheritance is enabled)
    svi_profiles:

        # Profile name.
      - profile: <str; required; unique>

        # Define node specific configuration, such as unique IP addresses.
        # Any keys set here will be merged onto the SVI config, except `structured_config` keys which will replace the `structured_config` set on SVI level.
        nodes:

            # Node inventory hostname.
          - node: <str; required; unique>

            # OSPFv3 interface configuration.
            # Enabling OSPFv3 on an SVI automatically creates the OSPFv3 configuration for the VRF of the SVI on the device.
            # Only the IPv6 address family is currently supported.
            # SVIs with IPv4 addressing require `ospfv3.ipv4.enabled: false`.
            # OSPFv3 uses the IPv6 link-local address of the SVI, so `ipv6_enable: true` is set automatically on SVIs without `ipv6_address` (`ipv6_enable: false` is not supported).
            # Anycast IPv6 (`ipv6_address_virtuals`) is not supported.
            # SVIs extended over VXLAN are not supported. Set `vxlan: false` on the SVI.
            # VRF `default` and SVIs deployed as subinterfaces with `uplink_type: lan` are not supported.
            ospfv3:
              enabled: <bool>

              # OSPFv3 area ID in IPv4 address or decimal format (range 0 to 4294967295).
              area: <str; default="0.0.0.0">

              # Configure the OSPFv3 network type as point-to-point.
              point_to_point: <bool; default=False>

              # Advertise the SVI subnet into OSPFv3 without forming adjacencies.
              # By default, OSPFv3-enabled SVIs are configured with `no ospfv3 passive-interface`.
              passive: <bool; default=False>
              ipv4:

                # Set to `false` to exclude the IPv4 address family from OSPFv3 on an SVI with IPv4 addressing.
                # The IPv4 address family is not supported yet, so `true` raises an error.
                # An SVI with IPv4 addressing also raises an error unless this is set to `false`.
                enabled: <bool>

        # OSPFv3 interface configuration.
        # Enabling OSPFv3 on an SVI automatically creates the OSPFv3 configuration for the VRF of the SVI on the device.
        # Only the IPv6 address family is currently supported.
        # SVIs with IPv4 addressing require `ospfv3.ipv4.enabled: false`.
        # OSPFv3 uses the IPv6 link-local address of the SVI, so `ipv6_enable: true` is set automatically on SVIs without `ipv6_address` (`ipv6_enable: false` is not supported).
        # Anycast IPv6 (`ipv6_address_virtuals`) is not supported.
        # SVIs extended over VXLAN are not supported. Set `vxlan: false` on the SVI.
        # VRF `default` and SVIs deployed as subinterfaces with `uplink_type: lan` are not supported.
        ospfv3:
          enabled: <bool>

          # OSPFv3 area ID in IPv4 address or decimal format (range 0 to 4294967295).
          area: <str; default="0.0.0.0">

          # Configure the OSPFv3 network type as point-to-point.
          point_to_point: <bool; default=False>

          # Advertise the SVI subnet into OSPFv3 without forming adjacencies.
          # By default, OSPFv3-enabled SVIs are configured with `no ospfv3 passive-interface`.
          passive: <bool; default=False>
          ipv4:

            # Set to `false` to exclude the IPv4 address family from OSPFv3 on an SVI with IPv4 addressing.
            # The IPv4 address family is not supported yet, so `true` raises an error.
            # An SVI with IPv4 addressing also raises an error unless this is set to `false`.
            enabled: <bool>
    ```
