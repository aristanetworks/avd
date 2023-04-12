---
search:
  boost: 2
---

# Network Services

## Global Network Services Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_rd_type</samp>](## "evpn_rd_type") <span style="color:red">removed</span> | Dictionary |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>overlay_rd_type</samp> instead.</span> |
    | [<samp>evpn_rt_type</samp>](## "evpn_rt_type") <span style="color:red">removed</span> | Dictionary |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>overlay_rt_type</samp> instead.</span> |
    | [<samp>overlay_rd_type</samp>](## "overlay_rd_type") | Dictionary |  |  |  | Specify RD type.<br>Route Distinguisher (RD) for L2 / L3 services is set to <overlay_loopback>:<vni> per default.<br>By configuring overlay_rd_type the Administrator subfield (first part of RD) can be set to other values.<br>Note:<br>RD is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.<br>For loopback or 32-bit ASN/number the VNI can only be a 16-bit number.<br>For 16-bit ASN/number the VNI can be a 32-bit number.<br> |
    | [<samp>overlay_rt_type</samp>](## "overlay_rt_type") | Dictionary |  |  |  | Specify RT type.<br>Route Target (RT) for L2 / L3 services is set to <vni>:<vni> per default.<br>By configuring overlay_rt_type the Administrator subfield (first part of RT) can be set to other values.<br>Notes:<br>RT is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.<br>For 32-bit ASN/number the VNI can only be a 16-bit number.<br>For 16-bit ASN/number the VNI can be a 32-bit number.<br> |

=== "YAML"

    ```yaml
    evpn_rd_type:
    evpn_rt_type:
    overlay_rd_type:
    overlay_rt_type:
    ```
