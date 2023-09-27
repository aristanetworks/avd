<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>aaa_authorization</samp>](## "aaa_authorization") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;policy</samp>](## "aaa_authorization.policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local_default_role</samp>](## "aaa_authorization.policy.local_default_role") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;exec</samp>](## "aaa_authorization.exec") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_authorization.exec.default") | String |  |  |  | Exec authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
    | [<samp>&nbsp;&nbsp;config_commands</samp>](## "aaa_authorization.config_commands") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;serial_console</samp>](## "aaa_authorization.serial_console") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;dynamic</samp>](## "aaa_authorization.dynamic") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x_additional_groups</samp>](## "aaa_authorization.dynamic.dot1x_additional_groups") | List, items: String |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "aaa_authorization.dynamic.dot1x_additional_groups.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;commands</samp>](## "aaa_authorization.commands") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;all_default</samp>](## "aaa_authorization.commands.all_default") | String |  |  |  | Command authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group tacacs+ group MYGROUP local<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "aaa_authorization.commands.privilege") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- level</samp>](## "aaa_authorization.commands.privilege.[].level") | String |  |  |  | Privilege level(s) 0-15 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_authorization.commands.privilege.[].default") | String |  |  |  | Command authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group tacacs+ group MYGROUP local" |

=== "YAML"

    ```yaml
    aaa_authorization:
      policy:
        local_default_role: <str>
      exec:
        default: <str>
      config_commands: <bool>
      serial_console: <bool>
      dynamic:
        dot1x_additional_groups:
          - <str>
      commands:
        all_default: <str>
        privilege:
          - level: <str>
            default: <str>
    ```
