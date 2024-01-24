<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>new_network_services_bgp_vrf_config</samp>](## "new_network_services_bgp_vrf_config") | Boolean |  | `False` |  | PREVIEW: This key is currently not supported<br><br>Set this key to `true` in the node type to generate full BGP configuration<br>for network services even when `evpn` is not in the address families<br>(`evpn` is the default address family for `l3ls-evpn` but not for `l2ls`).<br><br>This may introduce breaking changes to your configuration. |

=== "YAML"

    ```yaml
    # PREVIEW: This key is currently not supported

    # Set this key to `true` in the node type to generate full BGP configuration
    # for network services even when `evpn` is not in the address families
    # (`evpn` is the default address family for `l3ls-evpn` but not for `l2ls`).

    # This may introduce breaking changes to your configuration.
    new_network_services_bgp_vrf_config: <bool; default=False>
    ```
