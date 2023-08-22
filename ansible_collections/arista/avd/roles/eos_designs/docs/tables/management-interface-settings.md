<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_destination_networks</samp>](## "mgmt_destination_networks") | List, items: String |  |  |  | List of IPv4 prefixes to configure as static routes towards the OOB Management interface gateway.<br>Replaces the default route. |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "mgmt_destination_networks.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>mgmt_gateway</samp>](## "mgmt_gateway") | String |  |  |  | OOB Management interface gateway in IPv4 format.<br>Used as next-hop for default gateway or static routes defined under 'mgmt_destination_networks'. |
    | [<samp>mgmt_interface</samp>](## "mgmt_interface") | String |  | `Management1` |  | OOB Management interface. |
    | [<samp>mgmt_interface_description</samp>](## "mgmt_interface_description") | String |  | `oob_management` |  | Management interface description.<br> |
    | [<samp>mgmt_interface_vrf</samp>](## "mgmt_interface_vrf") | String |  | `MGMT` |  | OOB Management VRF. |
    | [<samp>mgmt_vrf_routing</samp>](## "mgmt_vrf_routing") | Boolean |  | `False` |  | Configure IP routing for the OOB Management VRF. |

=== "YAML"

    ```yaml
    # List of IPv4 prefixes to configure as static routes towards the OOB Management interface gateway.
    # Replaces the default route.
    mgmt_destination_networks:
      - <str>
    # OOB Management interface gateway in IPv4 format.
    # Used as next-hop for default gateway or static routes defined under 'mgmt_destination_networks'.
    mgmt_gateway: <str>
    # OOB Management interface.
    mgmt_interface: <str; default="Management1">
    # Management interface description.
    mgmt_interface_description: <str; default="oob_management">
    # OOB Management VRF.
    mgmt_interface_vrf: <str; default="MGMT">
    # Configure IP routing for the OOB Management VRF.
    mgmt_vrf_routing: <bool; default=False>
    ```
