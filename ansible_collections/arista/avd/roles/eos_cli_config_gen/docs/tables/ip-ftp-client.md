<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_ftp_client</samp>](## "ip_ftp_client") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;source_interface</samp>](## "ip_ftp_client.source_interface") | String |  |  |  | Source interface name for default vrf. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "ip_ftp_client.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_ftp_client.vrfs.[].name") | String | Required, Unique |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "ip_ftp_client.vrfs.[].source_interface") | String |  |  |  | Interface Name. |
    | [<samp>ip_ftp_client_source_interfaces</samp>](## "ip_ftp_client_source_interfaces") <span style="color:red">removed</span> | List |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>ip_ftp_client</samp> instead.</span> |

=== "YAML"

    ```yaml
    ip_ftp_client:

      # Source interface name for default vrf.
      source_interface: <str>
      vrfs:

          # VRF Name.
        - name: <str; required; unique>

          # Interface Name.
          source_interface: <str>
    ```
