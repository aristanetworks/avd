<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>vrfs</samp>](## "vrfs") | List, items: Dictionary |  |  |  | These keys are ignored if the name of the vrf is 'default'<br> |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "vrfs.[].name") | String | Required, Unique |  |  | VRF Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "vrfs.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_routing</samp>](## "vrfs.[].ip_routing") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_routing</samp>](## "vrfs.[].ipv6_routing") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_routing_ipv6_interfaces</samp>](## "vrfs.[].ip_routing_ipv6_interfaces") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp>](## "vrfs.[].tenant") | String |  |  |  | Key only used for documentation or validation purposes |

=== "YAML"

    ```yaml
    vrfs:
      - name: <str>
        description: <str>
        ip_routing: <bool>
        ipv6_routing: <bool>
        ip_routing_ipv6_interfaces: <bool>
        tenant: <str>
    ```
