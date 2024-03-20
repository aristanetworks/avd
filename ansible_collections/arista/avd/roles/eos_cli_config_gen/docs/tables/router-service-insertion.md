<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_service_insertion</samp>](## "router_service_insertion") | Dictionary |  |  |  | Configure network services inserted to data forwarding. |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "router_service_insertion.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;connections</samp>](## "router_service_insertion.connections") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;connection_name</samp>](## "router_service_insertion.connections.[].connection_name") | String |  |  |  | Configure name of the network service. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "router_service_insertion.connections.[].interface") | String |  |  |  | Interface to be used to reach the network service. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel_config</samp>](## "router_service_insertion.connections.[].tunnel_config") | String |  |  | Valid Values:<br>- <code>primary</code><br>- <code>secondary</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_ip_address</samp>](## "router_service_insertion.connections.[].next_hop_ip_address") | String |  |  |  | Configure the next-hop ip address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor_connectivity_to_host</samp>](## "router_service_insertion.connections.[].monitor_connectivity_to_host") | String |  |  |  | Monitor connectivity health to the network service host. |

=== "YAML"

    ```yaml
    # Configure network services inserted to data forwarding.
    router_service_insertion:
      enabled: <bool>
      connections:

          # Configure name of the network service.
        - connection_name: <str>

          # Interface to be used to reach the network service.
          interface: <str>
          tunnel_config: <str; "primary" | "secondary">

          # Configure the next-hop ip address.
          next_hop_ip_address: <str>

          # Monitor connectivity health to the network service host.
          monitor_connectivity_to_host: <str>
    ```
