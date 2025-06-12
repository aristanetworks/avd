<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_hardware</samp>](## "ip_hardware") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;fib</samp>](## "ip_hardware.fib") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;optimize</samp>](## "ip_hardware.fib.optimize") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "ip_hardware.fib.optimize.prefixes") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "ip_hardware.fib.optimize.prefixes.profile") | String |  |  | Valid Values:<br>- <code>internet</code><br>- <code>urpf-internet</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;load_balance_distribution</samp>](## "ip_hardware.fib.load_balance_distribution") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "ip_hardware.fib.load_balance_distribution.dynamic") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ip_hardware.fib.load_balance_distribution.dynamic.enabled") | Boolean | Required |  |  | Enable dynamic load balancing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_set_size</samp>](## "ip_hardware.fib.load_balance_distribution.dynamic.flow_set_size") | Integer |  |  | Min: 1<br>Max: 7 | Set flow set size. Requires `enabled` key to be set to `true`.<br>1: Allow up to 128 ECMP groups of 256 entries each.<br>2: Allow up to 64 ECMP groups of 512 entries each.<br>3: Allow up to 32 ECMP groups of 1024 entries each.<br>4: Allow up to 16 ECMP groups of 2048 entries each.<br>5: Allow up to 8 ECMP groups of 4096 entries each.<br>6: Allow up to 4 ECMP groups of 8192 entries each.<br>7: Allow up to 2 ECMP groups of 16384 entries each. |

=== "YAML"

    ```yaml
    ip_hardware:
      fib:
        optimize:
          prefixes:
            profile: <str; "internet" | "urpf-internet">
        load_balance_distribution:
          dynamic:

            # Enable dynamic load balancing.
            enabled: <bool; required>

            # Set flow set size. Requires `enabled` key to be set to `true`.
            # 1: Allow up to 128 ECMP groups of 256 entries each.
            # 2: Allow up to 64 ECMP groups of 512 entries each.
            # 3: Allow up to 32 ECMP groups of 1024 entries each.
            # 4: Allow up to 16 ECMP groups of 2048 entries each.
            # 5: Allow up to 8 ECMP groups of 4096 entries each.
            # 6: Allow up to 4 ECMP groups of 8192 entries each.
            # 7: Allow up to 2 ECMP groups of 16384 entries each.
            flow_set_size: <int; 1-7>
    ```
