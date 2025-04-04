<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>kernel</samp>](## "kernel") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;software_forwarding_ecmp</samp>](## "kernel.software_forwarding_ecmp") | Boolean |  |  |  | Program ECMP routes in the kernel. |

=== "YAML"

    ```yaml
    kernel:

      # Program ECMP routes in the kernel.
      software_forwarding_ecmp: <bool>
    ```
