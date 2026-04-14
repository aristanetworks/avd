<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>banners</samp>](## "banners") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;login</samp>](## "banners.login") | String |  |  |  | Legal notification or security warning displayed to all users before authentication. |
    | [<samp>&nbsp;&nbsp;motd</samp>](## "banners.motd") | String |  |  |  | Informational or operational message displayed to authorized users after a successful login. |

=== "YAML"

    ```yaml
    banners:

      # Legal notification or security warning displayed to all users before authentication.
      login: <str>

      # Informational or operational message displayed to authorized users after a successful login.
      motd: <str>
    ```
