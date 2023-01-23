---
search:
  boost: 2
---

# IP Hardware
## IP Hardware



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ip_hardware</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;fib</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;optimize</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp> | String |  |  | Valid Values:<br>- internet<br>- urpf-internet |  |

=== "YAML"

    ```yaml
    ip_hardware:
      fib:
        optimize:
          prefixes:
            profile: <str>
    ```
