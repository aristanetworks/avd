<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>new_network_services_bgp_vrf_config</samp>](## "new_network_services_bgp_vrf_config") | Boolean |  |  |  | Set this key to `true` in the node type to generate full BGP configuration<br>for network services even when `evpn` is not in the address families<br>(`evpn` is the default address family for `l3ls-evpn` but not for `l2ls`).<br><br>This is `false` by default except if `uplink_type` is set to `p2p-vrfs`, then the default value is `true`.<br><br>This may introduce breaking changes to your configuration. |

=== "YAML"

    ```yaml
    # Set this key to `true` in the node type to generate full BGP configuration
    # for network services even when `evpn` is not in the address families
    # (`evpn` is the default address family for `l3ls-evpn` but not for `l2ls`).
    #
    # This is `false` by default except if `uplink_type` is set to `p2p-vrfs`, then the default value is `true`.
    #
    # This may introduce breaking changes to your configuration.
    new_network_services_bgp_vrf_config: <bool>
    ```
