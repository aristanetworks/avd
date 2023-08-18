=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_vlan_bundles</samp>](## "evpn_vlan_bundles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "evpn_vlan_bundles.[].name") | String | Required, Unique |  |  | Specify a EVPN vlan-aware-bundle name.<br>A EVPN vlan-aware-bundle provide a construct to group L2 VLANs and define common settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "evpn_vlan_bundles.[].id") | Integer | Required |  | Min: 1<br>Max: 1024 | "id" may also be used for vlan-aware-bundle RD/RT ID and therefore should not overlap with l2vlan IDs which are not part of this bundle. <br>See "overlay_rd_type" and "overlay_rt_type" for details.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "evpn_vlan_bundles.[].rt_override") | String |  |  |  | By default the MAC VRF bundle RT will be derived from mac_vrf_id_base + bundle_id.<br>The rt_override allows us to override this value and statically define it.<br>rt_override will default to vni_override if set.<br><br>rt_override supports two formats:<br>  - A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for details).<br>  - A full RT string with colon seperator which will override the full RT.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rd_override</samp>](## "evpn_vlan_bundles.[].rd_override") | String |  |  |  | By default the MAC VRF bundle RD will be derived from mac_vrf_id_base + bundle_id.<br>The rt_override allows us to override this value and statically define it.<br>rd_override will default to rt_override or vni_override if set.<br><br>rd_override supports two formats:<br>  - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rd_type' for details).<br>  - A full RD string with colon seperator which will override the full RD.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "evpn_vlan_bundles.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "evpn_vlan_bundles.[].bgp.raw_eos_cli") | String |  |  |  | EOS cli commands rendered on router_bgp.vlans-aware-bundle. |

=== "YAML"

    ```yaml
    evpn_vlan_bundles:
      - name: <str>
        id: <int>
        rt_override: <str>
        rd_override: <str>
        bgp:
          raw_eos_cli: <str>
    ```
