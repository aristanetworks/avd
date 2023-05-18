---
search:
  boost: 2
---

# L2 Protocol Forwarding

## L2 Protocol

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>l2_protocol</samp>](## "l2_protocol") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;forwarding_profiles</samp>](## "l2_protocol.forwarding_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "l2_protocol.forwarding_profiles.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocols</samp>](## "l2_protocol.forwarding_profiles.[].protocols") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "l2_protocol.forwarding_profiles.[].protocols.[].name") | String | Required, Unique |  | Valid Values:<br>- bfd per-link rfc-7130<br>- e-lmi<br>- isis<br>- lacp<br>- lldp<br>- macsec<br>- pause<br>- stp |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward</samp>](## "l2_protocol.forwarding_profiles.[].protocols.[].forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tagged_forward</samp>](## "l2_protocol.forwarding_profiles.[].protocols.[].tagged_forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;untagged_forward</samp>](## "l2_protocol.forwarding_profiles.[].protocols.[].untagged_forward") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    l2_protocol:
      forwarding_profiles:
        - name: <str>
          protocols:
            - name: <str>
              forward: <bool>
              tagged_forward: <bool>
              untagged_forward: <bool>
    ```
