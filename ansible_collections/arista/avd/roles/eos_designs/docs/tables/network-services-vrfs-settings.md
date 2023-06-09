=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;network_services_keys.name&gt;</samp>](## "&lt;network_services_keys.name&gt;") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enable_mlag_ibgp_peering_vrfs</samp>](## "&lt;network_services_keys.name&gt;.[].enable_mlag_ibgp_peering_vrfs") | Boolean |  |  |  | MLAG iBGP peering per VRF.<br>By default an iBGP peering is configured per VRF between MLAG peers on separate VLANs.<br>Setting enable_mlag_ibgp_peering_vrfs: false under tenant will change this default to prevent configuration of these peerings and VLANs for all VRFs in the tenant.<br>This setting can be overridden per VRF.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs") | List, items: Dictionary |  |  |  | VRFs will only be configured on a node if any of the underlying objects like `svis` or `l3_interfaces` apply to the node.<br><br>It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants<br>are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.<br><br>VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,<br>route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.<br>Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].address_families") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].address_families.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- evpn<br>- vpn-ipv4<br>- vpn-ipv6 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].description") | String |  |  |  | VRF description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf_vni</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vrf_vni") | Integer |  |  | Min: 1<br>Max: 16777215 | Required if "vrf_id" is not set.<br>The VRF VNI range is not limited, but if vrf_id is not set, "vrf_vni" is used for calculating MLAG iBGP peering vlan id.<br>See "mlag_ibgp_peering_vrfs.base_vlan" for details.<br>If vrf_vni > 10000 make sure to adjust "mac_vrf_vni_base" accordingly to avoid overlap.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf_id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vrf_id") | Integer |  |  | Min: 1<br>Max: 1024 | Required if "vrf_vni" is not set.<br>"vrf_id" is used as default value for "vrf_vni" and "ospf.process_id" unless those are set.<br>"vrf_id" is preferred over "vrf_vni" for VRF RD/RT ID before vrf_vni.<br>"vrf_id" is preferred over "vrf_vni" for MLAG iBGP peering vlan, see "mlag_ibgp_peering_vrfs.base_vlan" for details.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_peering_ipv4_pool</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].mlag_ibgp_peering_ipv4_pool") | String |  |  |  | IPv4_address/Mask<br>The subnet used for iBGP peering in the VRF.<br>Each MLAG pair will be assigned a subnet based on the ID of the primary MLAG switch.<br>If not set, "mlag_peer_l3_ipv4_pool" or "mlag_peer_ipv4_pool" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, uses current VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_mlag_ibgp_peering_vrfs</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].enable_mlag_ibgp_peering_vrfs") | Boolean |  |  |  | MLAG iBGP peering per VRF.<br>By default an iBGP peering is configured per VRF between MLAG peers on separate VLANs.<br>Setting enable_mlag_ibgp_peering_vrfs: false under vrf will change this default and/or override the tenant-wide setting.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_peering_vlan</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].mlag_ibgp_peering_vlan") | Integer |  |  | Min: 1<br>Max: 4096 | Manually define the VLAN used on the MLAG pair for the iBGP session.<br>By default this parameter is calculated using the following formula: <mlag_ibgp_peering_vrfs.base_vlan> + <vrf_id> - 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_diagnostic</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic") | Dictionary |  |  |  | Enable VTEP Network diagnostics.<br>This will create a loopback with virtual source-nat enable to perform diagnostics from the switch.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback") | Integer |  |  | Min: 2<br>Max: 2100 | Loopback interface number, required when vtep_diagnotics defined.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback_description") | String |  |  |  | Provide a custom description for loopback interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ip_range</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback_ip_range") | String |  |  |  | IPv4_address/Mask.<br>Loopback ip range, a unique ip is derived from this ranged and assignedto each l3 leaf based on it's unique id.<br>Loopback is not created unless loopback_ip_range or loopback_ip_pools are set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ip_pools</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback_ip_pools") | List, items: Dictionary |  |  |  | For inventories with multiple PODs a loopback range can be set per POD to avoid overlaps.<br>This only takes effect when loopback_ip_range is not defined, ptional (loopback is not created unless loopback_ip_range or loopback_ip_pools are set).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- pod</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback_ip_pools.[].pod") | String |  |  |  | POD name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_pool</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback_ip_pools.[].ipv4_pool") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the Router BGP, VRF definition in the final EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.vrfs.<vrf> for eos_cli_config_gen.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_route_targets</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets") | List, items: Dictionary |  |  |  | Configuration of extra route-targets for this VRF. Useful for route-leaking or gateway between address families. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- type</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets.[].type") | String |  |  | Valid Values:<br>- import<br>- export |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets.[].address_family") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets.[].route_target") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |

=== "YAML"

    ```yaml
    <network_services_keys.name>:
      - name: <str>
        enable_mlag_ibgp_peering_vrfs: <bool>
        vrfs:
          - name: <str>
            address_families:
              - <str>
            description: <str>
            vrf_vni: <int>
            vrf_id: <int>
            mlag_ibgp_peering_ipv4_pool: <str>
            ip_helpers:
              - ip_helper: <str>
                source_interface: <str>
                source_vrf: <str>
            enable_mlag_ibgp_peering_vrfs: <bool>
            mlag_ibgp_peering_vlan: <int>
            vtep_diagnostic:
              loopback: <int>
              loopback_description: <str>
              loopback_ip_range: <str>
              loopback_ip_pools:
                - pod: <str>
                  ipv4_pool: <str>
            bgp:
              raw_eos_cli: <str>
              structured_config: <dict>
            additional_route_targets:
              - type: <str>
                address_family: <str>
                route_target: <str>
                nodes:
                  - <str>
            raw_eos_cli: <str>
            structured_config: <dict>
    ```
