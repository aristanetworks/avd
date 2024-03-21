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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_service_insertion.connections.[].name") | String |  |  |  | Configure name of the network service. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "router_service_insertion.connections.[].interface") | Dictionary |  |  |  | Interface to be used to reach the network service. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ethernet</samp>](## "router_service_insertion.connections.[].interface.ethernet") | Dictionary |  |  |  | Configure to use ethernet interface to reach the network service. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface_name</samp>](## "router_service_insertion.connections.[].interface.ethernet.interface_name") | String |  |  |  | e.g. ethernet2 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_ip_address</samp>](## "router_service_insertion.connections.[].interface.ethernet.next_hop_ip_address") | String |  |  |  | Configure the next-hop ip address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel</samp>](## "router_service_insertion.connections.[].interface.tunnel") | Dictionary |  |  |  | Configure to use tunnel interface to reach the network service. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary_interface_name</samp>](## "router_service_insertion.connections.[].interface.tunnel.primary_interface_name") | String |  |  |  | e.g. tunnel2 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;secondary_interface_name</samp>](## "router_service_insertion.connections.[].interface.tunnel.secondary_interface_name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor_connectivity_to_host</samp>](## "router_service_insertion.connections.[].monitor_connectivity_to_host") | String |  |  |  | Monitor connectivity health to the network service host. |

=== "YAML"

    ```yaml
    # Configure network services inserted to data forwarding.
    router_service_insertion:
      enabled: <bool>
      connections:

          # Configure name of the network service.
        - name: <str>

          # Interface to be used to reach the network service.
          interface:

            # Configure to use ethernet interface to reach the network service.
            ethernet:

              # e.g. ethernet2
              interface_name: <str>

              # Configure the next-hop ip address.
              next_hop_ip_address: <str>

            # Configure to use tunnel interface to reach the network service.
            tunnel:

              # e.g. tunnel2
              primary_interface_name: <str>
              secondary_interface_name: <str>

          # Monitor connectivity health to the network service host.
          monitor_connectivity_to_host: <str>
    ```
