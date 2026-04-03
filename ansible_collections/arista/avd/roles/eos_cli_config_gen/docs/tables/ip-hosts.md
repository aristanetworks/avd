<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_hosts</samp>](## "ip_hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;hostname</samp>](## "ip_hosts.[].hostname") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_address</samp>](## "ip_hosts.[].ipv4_address") | String | Required |  |  |  |

=== "YAML"

    ```yaml
    ip_hosts:
      - hostname: <str; required; unique>
        ipv4_address: <str; required>
    ```
