=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>aaa_accounting</samp>](## "aaa_accounting") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;exec</samp>](## "aaa_accounting.exec") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;console</samp>](## "aaa_accounting.exec.console") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.exec.console.type") | String |  |  | Valid Values:<br>- none<br>- start-stop<br>- stop-only |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.exec.console.group") | String |  |  |  | Group Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_accounting.exec.default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.exec.default.type") | String |  |  | Valid Values:<br>- none<br>- start-stop<br>- stop-only |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.exec.default.group") | String |  |  |  | Group Name |
    | [<samp>&nbsp;&nbsp;system</samp>](## "aaa_accounting.system") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_accounting.system.default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.system.default.type") | String |  |  | Valid Values:<br>- none<br>- start-stop<br>- stop-only |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.system.default.group") | String |  |  |  | Group Name |
    | [<samp>&nbsp;&nbsp;dot1x</samp>](## "aaa_accounting.dot1x") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_accounting.dot1x.default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.dot1x.default.type") | String |  |  | Valid Values:<br>- start-stop<br>- stop-only |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.dot1x.default.group") | String |  |  |  | Group Name |
    | [<samp>&nbsp;&nbsp;commands</samp>](## "aaa_accounting.commands") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;console</samp>](## "aaa_accounting.commands.console") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- commands</samp>](## "aaa_accounting.commands.console.[].commands") | String |  |  |  | Privelege level 'all' or 0-15 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.commands.console.[].type") | String |  |  | Valid Values:<br>- none<br>- start-stop<br>- stop-only |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.commands.console.[].group") | String |  |  |  | Group Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "aaa_accounting.commands.console.[].logging") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_accounting.commands.default") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- commands</samp>](## "aaa_accounting.commands.default.[].commands") | String |  |  |  | Privelege level 'all' or 0-15 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.commands.default.[].type") | String |  |  | Valid Values:<br>- none<br>- start-stop<br>- stop-only |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.commands.default.[].group") | String |  |  |  | Group Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "aaa_accounting.commands.default.[].logging") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    aaa_accounting:
      exec:
        console:
          type: <str>
          group: <str>
        default:
          type: <str>
          group: <str>
      system:
        default:
          type: <str>
          group: <str>
      dot1x:
        default:
          type: <str>
          group: <str>
      commands:
        console:
          - commands: <str>
            type: <str>
            group: <str>
            logging: <bool>
        default:
          - commands: <str>
            type: <str>
            group: <str>
            logging: <bool>
    ```
