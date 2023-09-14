<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;network_services_keys.name&gt;</samp>](## "&lt;network_services_keys.name&gt;") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2vlans</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans") | List, items: Dictionary |  |  |  | Define L2 network services organized by vlan id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 4094 | VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the VNI will be derived from mac_vrf_vni_base.<br>The vni_override, allows to override this value and statically define it.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].rt_override") | String |  |  |  | By default the MAC VRF RT will be derived from mac_vrf_id_base + vlan_id.<br>The rt_override allows us to override this value and statically define it.<br>rt_override will default to vni_override if set.<br><br>rt_override supports two formats:<br>  - A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for details).<br>  - A full RT string with colon seperator which will override the full RT.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd_override</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].rd_override") | String |  |  |  | By default the MAC VRF RD will be derived from mac_vrf_id_base + vlan_id.<br>The rt_override allows us to override this value and statically define it.<br>rd_override will default to rt_override or vni_override if set.<br><br>rd_override supports two formats:<br>  - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rd_type' for details).<br>  - A full RD string with colon seperator which will override the full RD.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].name") | String | Required |  |  | VLAN name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].tags") | List, items: String |  |  |  | Tags leveraged for networks services filtering.<br>Tags are matched against filter.tags defined under node type settings.<br>Tags are also matched against the node_group name under node type settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].tags.[].&lt;str&gt;") | String |  | `all` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].vxlan") | Boolean |  | `True` |  | Extend this L2VLAN over VXLAN. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group.<br>Requires enable_trunk_groups: true.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].bgp.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.vlans.[id=<vlan>] for eos_cli_config_gen.<br>This configuration will not be applied to vlan aware bundles.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].bgp.raw_eos_cli") | String |  |  |  | EOS cli commands rendered on router_bgp.vlans.<br>This configuration will not be applied to vlan aware bundles.<br> |

=== "YAML"

    ```yaml
    <network_services_keys.name>:
      - name: <str>
        l2vlans:
          - id: <int>
            vni_override: <int>
            rt_override: <str>
            rd_override: <str>
            name: <str>
            tags:
              - <str>
            vxlan: <bool>
            trunk_groups:
              - <str>
            bgp:
              structured_config: <dict>
              raw_eos_cli: <str>
    ```
