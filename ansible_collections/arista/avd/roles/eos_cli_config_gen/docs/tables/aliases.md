=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>aliases</samp>](## "aliases") | String |  |  |  | Multi-line string with one or more alias commands.<br><br>Example:<br><br>```yaml<br>aliases: |<br>  alias wr copy running-config startup-config<br>  alias siib show ip interface brief<br>``` |

=== "YAML"

    ```yaml
    aliases: <str>
    ```
