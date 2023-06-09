=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;network_services_keys.name&gt;</samp>](## "&lt;network_services_keys.name&gt;") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs") | List, items: Dictionary |  |  |  | VRFs will only be configured on a node if any of the underlying objects like `svis` or `l3_interfaces` apply to the node.<br><br>It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants<br>are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.<br><br>VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,<br>route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.<br>Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes") | List, items: Dictionary |  |  |  | List of static routes for v4 and/or v6.<br>This will create static routes inside the tenant VRF.<br>If nodes are not specified, all l3leafs that carry the VRF will also be applied the static routes.<br>If a node has a static route in the VRF, redistribute static will be automatically enabled in that VRF.<br>This automatic behavior can be overridden non-selectively with the redistribute_static knob for the VRF.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- destination_address_prefix</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].destination_address_prefix") | String |  |  |  | IPv4_address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].gateway") | String |  |  |  | IPv4_address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;track_bfd</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].track_bfd") | Boolean |  |  |  | Track next-hop using BFD. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].name") | String |  |  |  | description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].nodes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_static_routes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- destination_address_prefix</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].destination_address_prefix") | String |  |  |  | IPv6_address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].gateway") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;track_bfd</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].track_bfd") | Boolean |  |  |  | Track next-hop using BFD. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].name") | String |  |  |  | description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].nodes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_static</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].redistribute_static") | Boolean |  |  |  | Non-selectively enabling or disabling redistribute static inside the VRF. |

=== "YAML"

    ```yaml
    <network_services_keys.name>:
      - name: <str>
        vrfs:
          - name: <str>
            static_routes:
              - destination_address_prefix: <str>
                gateway: <str>
                track_bfd: <bool>
                distance: <int>
                tag: <int>
                name: <str>
                metric: <int>
                interface: <str>
                nodes:
                  - <str>
            ipv6_static_routes:
              - destination_address_prefix: <str>
                gateway: <str>
                track_bfd: <bool>
                distance: <int>
                tag: <int>
                name: <str>
                metric: <int>
                interface: <str>
                nodes:
                  - <str>
            redistribute_static: <bool>
    ```
