<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dhcp_relay</samp>](## "dhcp_relay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;servers</samp>](## "dhcp_relay.servers") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "dhcp_relay.servers.[]") | String |  |  |  | Server IP or Hostname. |
    | [<samp>&nbsp;&nbsp;tunnel_requests_disabled</samp>](## "dhcp_relay.tunnel_requests_disabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mlag_peerlink_requests_disabled</samp>](## "dhcp_relay.mlag_peerlink_requests_disabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;client_requests</samp>](## "dhcp_relay.client_requests") | Dictionary |  |  |  | Configure DHCP client request settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;flooding_suppression_vlans</samp>](## "dhcp_relay.client_requests.flooding_suppression_vlans") | List, items: String |  |  |  | Disable DHCP request flooding to other interfaces in VLAN. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "dhcp_relay.client_requests.flooding_suppression_vlans.[]") | String |  |  |  | VLAN ID or range(s) of VLAN IDs, <1-4094>.<br>Example:<br>  - 1000<br>  - 500-510<br>  - 2000,3000<br> |

=== "YAML"

    ```yaml
    dhcp_relay:
      servers:

          # Server IP or Hostname.
        - <str>
      tunnel_requests_disabled: <bool>
      mlag_peerlink_requests_disabled: <bool>

      # Configure DHCP client request settings.
      client_requests:

        # Disable DHCP request flooding to other interfaces in VLAN.
        flooding_suppression_vlans:

            # VLAN ID or range(s) of VLAN IDs, <1-4094>.
            # Example:
            #   - 1000
            #   - 500-510
            #   - 2000,3000
          - <str>
    ```
