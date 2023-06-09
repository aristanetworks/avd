=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ptp</samp>](## "ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "ptp.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;profile</samp>](## "ptp.profile") | String |  | `aes67-r16-2016` | Valid Values:<br>- aes67<br>- smpte2059-2<br>- aes67-r16-2016 |  |
    | [<samp>&nbsp;&nbsp;domain</samp>](## "ptp.domain") | Integer |  |  | Min: 0<br>Max: 255 |  |

=== "YAML"

    ```yaml
    ptp:
      enabled: <bool>
      profile: <str>
      domain: <int>
    ```
