<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>new_network_services_bgp_vrf_config</samp>](## "new_network_services_bgp_vrf_config") <span style="color:red">removed</span> | Boolean |  | `True` |  | This key was used to generate BGP configuration for network services even when `evpn` is not in the address families for the node as well as the VRF.<br>(`evpn` is the default address family for `l3leaf` but not for `l3spine`).<br>This is now the default behavior so this key can be removed.<span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. See [here](https://avd.arista.com/devel/porting-guides/5.x.x.html#) for details.</span> |

=== "YAML"

    ```yaml

    ```
