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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_service_insertion.connections.[].name") | String | Required, Unique |  |  | Connection name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ethernet_interface</samp>](## "router_service_insertion.connections.[].ethernet_interface") | Dictionary |  |  |  | Outgoing physical interface or subinterface to use for the connection.<br>If both ethernet interface and tunnel interface are configured, ethernet interface will be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "router_service_insertion.connections.[].ethernet_interface.name") | String |  |  |  | e.g. Ethernet2/2.2 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop</samp>](## "router_service_insertion.connections.[].ethernet_interface.next_hop") | String |  |  |  | Next-hop IPv4 address (without mask). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel_interface</samp>](## "router_service_insertion.connections.[].tunnel_interface") | Dictionary |  |  |  | Outgoing tunnel interface(s) to use for this connection.<br>If both ethernet interface and tunnel interface are configured, ethernet interface will be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary</samp>](## "router_service_insertion.connections.[].tunnel_interface.primary") | String |  |  |  | e.g. Tunnel2 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;secondary</samp>](## "router_service_insertion.connections.[].tunnel_interface.secondary") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor_connectivity_host</samp>](## "router_service_insertion.connections.[].monitor_connectivity_host") | String |  |  |  | Monitor connectivity host to use to derive the health of the connecion.<br>The host must be defined under `monitor_connectivity.hosts`. |

=== "YAML"

    ```yaml
    # Configure network services inserted to data forwarding.
    router_service_insertion:
      enabled: <bool>
      connections:

          # Connection name.
        - name: <str; required; unique>

          # Outgoing physical interface or subinterface to use for the connection.
          # If both ethernet interface and tunnel interface are configured, ethernet interface will be used.
          ethernet_interface:

            # e.g. Ethernet2/2.2
            name: <str>

            # Next-hop IPv4 address (without mask).
            next_hop: <str>

          # Outgoing tunnel interface(s) to use for this connection.
          # If both ethernet interface and tunnel interface are configured, ethernet interface will be used.
          tunnel_interface:

            # e.g. Tunnel2
            primary: <str>
            secondary: <str>

          # Monitor connectivity host to use to derive the health of the connecion.
          # The host must be defined under `monitor_connectivity.hosts`.
          monitor_connectivity_host: <str>
    ```
