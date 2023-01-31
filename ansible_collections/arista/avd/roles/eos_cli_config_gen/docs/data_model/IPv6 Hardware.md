---
search:
  boost: 2
---

# IPv6 Hardware

## IPv6 Hardware

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ipv6_hardware</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;fib</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;optimize</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp> | String |  |  |  | Pre-defined profile 'internet' or user-defined profile name |

=== "YAML"

    ```yaml
    ipv6_hardware:
      fib:
        optimize:
          prefixes:
            profile: <str>
    ```
