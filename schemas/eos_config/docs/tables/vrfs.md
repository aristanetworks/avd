<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>vrfs</samp>](## "vrfs") | List, items: Dictionary |  |  |  | These keys are ignored if the name of the vrf is 'default'.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "vrfs.[].name") | String | Required, Unique |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "vrfs.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rd</samp>](## "vrfs.[].rd") | String |  |  |  | Renders Route Distinguisher under 'vrf instance'.<br>This is deprecated in EOS; configure the Route Distinguisher under 'router bgp' VRF submode instead using `router_bgp.vrfs[].rd`.<br>This key is kept only to support existing/legacy device configurations and is intentionally not shown in the generated device documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_routing</samp>](## "vrfs.[].ip_routing") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_routing</samp>](## "vrfs.[].ipv6_routing") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_routing_ipv6_interfaces</samp>](## "vrfs.[].ip_routing_ipv6_interfaces") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;metadata</samp>](## "vrfs.[].metadata") | Dictionary |  |  |  | The data under `metadata` is used for documentation, validation or integration purposes.<br>It will not affect the generated EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "vrfs.[].metadata.tenants") | List, items: String |  |  |  | Key only used for documentation or validation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "vrfs.[].metadata.tenants.[]") | String |  |  |  |  |

=== "YAML"

    ```yaml
    # These keys are ignored if the name of the vrf is 'default'.
    vrfs:

        # VRF Name.
      - name: <str; required; unique>
        description: <str>

        # Renders Route Distinguisher under 'vrf instance'.
        # This is deprecated in EOS; configure the Route Distinguisher under 'router bgp' VRF submode instead using `router_bgp.vrfs[].rd`.
        # This key is kept only to support existing/legacy device configurations and is intentionally not shown in the generated device documentation.
        rd: <str>
        ip_routing: <bool>
        ipv6_routing: <bool>
        ip_routing_ipv6_interfaces: <bool>

        # The data under `metadata` is used for documentation, validation or integration purposes.
        # It will not affect the generated EOS configuration.
        metadata:

          # Key only used for documentation or validation purposes.
          tenants:
            - <str>
    ```
