<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>arp</samp>](## "arp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;aging</samp>](## "arp.aging") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;timeout_default</samp>](## "arp.aging.timeout_default") | Integer |  |  | Min: 60<br>Max: 65535 | Timeout in seconds |

=== "YAML"

    ```yaml
    arp:
      aging:
        timeout_default: <int>
    ```
