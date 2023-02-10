---
search:
  boost: 2
---

# IP Hardware

## IP Hardware

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_hardware</samp>](## "ip_hardware") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;fib</samp>](## "ip_hardware.fib") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;optimize</samp>](## "ip_hardware.fib.optimize") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "ip_hardware.fib.optimize.prefixes") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "ip_hardware.fib.optimize.prefixes.profile") | String |  |  | Valid Values:<br>- internet<br>- urpf-internet |  |

=== "YAML"

    ```yaml
    ip_hardware:
      fib:
        optimize:
          prefixes:
            profile: <str>
    ```
