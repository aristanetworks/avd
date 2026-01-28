<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_ftp_client_source_interfaces</samp>](## "ip_ftp_client_source_interfaces") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>ip_ftp_client in 6.0</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_ftp_client_source_interfaces.[].name") | String | Required |  |  | Interface Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_ftp_client_source_interfaces.[].vrf") | String |  |  |  | VRF Name. |

=== "YAML"

    ```yaml
    # This key is deprecated.
    # Support will be removed in AVD version 6.0.0.
    # Use `ip_ftp_client in 6.0` instead.
    ip_ftp_client_source_interfaces:

        # Interface Name.
      - name: <str; required>

        # VRF Name.
        vrf: <str>
    ```
