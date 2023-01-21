---
search:
  boost: 2
---

# System Boot Settings
## System Boot Settings

=== "System Boot Settings"

    Set the Aboot password


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>boot</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;secret</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp> | String |  | sha512 | Valid Values:<br>- md5<br>- sha512 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;key</samp> | String |  |  |  | Hashed Password |

=== "YAML"

    ```yaml
    boot:
      secret:
        hash_algorithm: <str>
        key: <str>
    ```
