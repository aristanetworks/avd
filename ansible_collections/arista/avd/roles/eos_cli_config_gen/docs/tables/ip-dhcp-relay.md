<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_dhcp_relay</samp>](## "ip_dhcp_relay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;information_option</samp>](## "ip_dhcp_relay.information_option") | Boolean |  |  |  | Insert Option-82 information |

=== "YAML"

    ```yaml
    ip_dhcp_relay:

      # Insert Option-82 information
      information_option: <bool>
    ```
