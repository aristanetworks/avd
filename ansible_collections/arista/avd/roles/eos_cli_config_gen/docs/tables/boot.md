<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>boot</samp>](## "boot") | Dictionary |  |  |  | Set the Aboot password<br> |
    | [<samp>&nbsp;&nbsp;secret</samp>](## "boot.secret") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "boot.secret.hash_algorithm") | String |  | `sha512` | Valid Values:<br>- md5<br>- sha512 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "boot.secret.key") | String |  |  |  | Hashed Password |

=== "YAML"

    ```yaml
    boot:
      secret:
        hash_algorithm: <str>
        key: <str>
    ```
