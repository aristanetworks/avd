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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_addresses</samp>](## "ip_hosts.[].ipv4_addresses") | List, items: String | Required |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ip_hosts.[].ipv4_addresses.[]") | String |  |  |  |  |

=== "YAML"

    ```yaml
    ip_hosts:
      - hostname: <str; required; unique>
        ipv4_addresses: # >=1 items; required
          - <str>
    ```
