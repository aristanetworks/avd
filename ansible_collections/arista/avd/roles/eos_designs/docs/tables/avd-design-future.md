<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>avd_design_future</samp>](## "avd_design_future") | Dictionary |  |  |  | Opt-in to future AVD behaviors which will become default behaviors in a future AVD major version. |
    | [<samp>&nbsp;&nbsp;remove_redundant_ipv4_unicast_for_peer_groups</samp>](## "avd_design_future.remove_redundant_ipv4_unicast_for_peer_groups") | Boolean |  | `False` |  | Deactivate the IPv4 unicast Address Family for BGP Peer Groups only when IPv4 is activated by default instead of always deactivating it. |

=== "YAML"

    ```yaml
    # Opt-in to future AVD behaviors which will become default behaviors in a future AVD major version.
    avd_design_future:

      # Deactivate the IPv4 unicast Address Family for BGP Peer Groups only when IPv4 is activated by default instead of always deactivating it.
      remove_redundant_ipv4_unicast_for_peer_groups: <bool; default=False>
    ```
