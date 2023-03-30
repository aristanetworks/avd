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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd_per_link_rfc_7130</samp>](## "l2_protocol.forwarding_profiles.[].bfd_per_link_rfc_7130") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward</samp>](## "l2_protocol.forwarding_profiles.[].bfd_per_link_rfc_7130.forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tagged_forward</samp>](## "l2_protocol.forwarding_profiles.[].bfd_per_link_rfc_7130.tagged_forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;untagged_forward</samp>](## "l2_protocol.forwarding_profiles.[].bfd_per_link_rfc_7130.untagged_forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e_lmi</samp>](## "l2_protocol.forwarding_profiles.[].e_lmi") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward</samp>](## "l2_protocol.forwarding_profiles.[].e_lmi.forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tagged_forward</samp>](## "l2_protocol.forwarding_profiles.[].e_lmi.tagged_forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;untagged_forward</samp>](## "l2_protocol.forwarding_profiles.[].e_lmi.untagged_forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis</samp>](## "l2_protocol.forwarding_profiles.[].isis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward</samp>](## "l2_protocol.forwarding_profiles.[].isis.forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tagged_forward</samp>](## "l2_protocol.forwarding_profiles.[].isis.tagged_forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;untagged_forward</samp>](## "l2_protocol.forwarding_profiles.[].isis.untagged_forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp</samp>](## "l2_protocol.forwarding_profiles.[].lacp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward</samp>](## "l2_protocol.forwarding_profiles.[].lacp.forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tagged_forward</samp>](## "l2_protocol.forwarding_profiles.[].lacp.tagged_forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;untagged_forward</samp>](## "l2_protocol.forwarding_profiles.[].lacp.untagged_forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lldp</samp>](## "l2_protocol.forwarding_profiles.[].lldp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward</samp>](## "l2_protocol.forwarding_profiles.[].lldp.forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tagged_forward</samp>](## "l2_protocol.forwarding_profiles.[].lldp.tagged_forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;untagged_forward</samp>](## "l2_protocol.forwarding_profiles.[].lldp.untagged_forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;macsec</samp>](## "l2_protocol.forwarding_profiles.[].macsec") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward</samp>](## "l2_protocol.forwarding_profiles.[].macsec.forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tagged_forward</samp>](## "l2_protocol.forwarding_profiles.[].macsec.tagged_forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;untagged_forward</samp>](## "l2_protocol.forwarding_profiles.[].macsec.untagged_forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pause</samp>](## "l2_protocol.forwarding_profiles.[].pause") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward</samp>](## "l2_protocol.forwarding_profiles.[].pause.forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tagged_forward</samp>](## "l2_protocol.forwarding_profiles.[].pause.tagged_forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;untagged_forward</samp>](## "l2_protocol.forwarding_profiles.[].pause.untagged_forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stp</samp>](## "l2_protocol.forwarding_profiles.[].stp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward</samp>](## "l2_protocol.forwarding_profiles.[].stp.forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tagged_forward</samp>](## "l2_protocol.forwarding_profiles.[].stp.tagged_forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;untagged_forward</samp>](## "l2_protocol.forwarding_profiles.[].stp.untagged_forward") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    l2_protocol:
      forwarding_profiles:
        - name: <str>
          bfd_per_link_rfc_7130:
            forward: <bool>
            tagged_forward: <bool>
            untagged_forward: <bool>
          e_lmi:
            forward: <bool>
            tagged_forward: <bool>
            untagged_forward: <bool>
          isis:
            forward: <bool>
            tagged_forward: <bool>
            untagged_forward: <bool>
          lacp:
            forward: <bool>
            tagged_forward: <bool>
            untagged_forward: <bool>
          lldp:
            forward: <bool>
            tagged_forward: <bool>
            untagged_forward: <bool>
          macsec:
            forward: <bool>
            tagged_forward: <bool>
            untagged_forward: <bool>
          pause:
            forward: <bool>
            tagged_forward: <bool>
            untagged_forward: <bool>
          stp:
            forward: <bool>
            tagged_forward: <bool>
            untagged_forward: <bool>
    ```
