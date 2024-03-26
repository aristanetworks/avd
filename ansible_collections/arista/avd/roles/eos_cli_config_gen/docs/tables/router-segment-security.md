<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_segment_security</samp>](## "router_segment_security") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "router_segment_security.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;policies</samp>](## "router_segment_security.policies") | List, items: Dictionary |  |  |  | Customised application policies.<br>Using the Application Traffic Recognition L4 profiles, custom policies can be defined. The built-in application 'app-match-all' can be used to match any packets.<br>Note that this is stateless, so both the source and destination flows need to be considered. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_segment_security.policies.[].name") | String | Required, Unique |  |  | Policy name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "router_segment_security.policies.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "router_segment_security.policies.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;application</samp>](## "router_segment_security.policies.[].sequence_numbers.[].application") | String | Required |  |  | The name of the application. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "router_segment_security.policies.[].sequence_numbers.[].action") | String | Required |  | Valid Values:<br>- <code>permit</code><br>- <code>deny</code> |  |
    | [<samp>&nbsp;&nbsp;segments</samp>](## "router_segment_security.segments") | List, items: Dictionary | Required |  |  | Defining the segments and associated policies. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_segment_security.segments.[].name") | String | Required, Unique |  |  | Segment name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "router_segment_security.segments.[].vrf") | String |  | `default` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;definition</samp>](## "router_segment_security.segments.[].definition") | List, items: Dictionary | Required |  |  | The set of match-lists that define the segment. These can be a mix of IPv4 and IPv6 lists. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_segment_security.segments.[].definition.[].name") | String |  |  |  | The name of the prefix match-list. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family</samp>](## "router_segment_security.segments.[].definition.[].address_family") | String | Required |  | Valid Values:<br>- <code>ipv4</code><br>- <code>ipv6</code> | Indicate which address family the match list belongs to e.g. ipv4 or ipv6. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;covered</samp>](## "router_segment_security.segments.[].definition.[].covered") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policies</samp>](## "router_segment_security.segments.[].policies") | List, items: Dictionary | Required |  |  | The policies controlling traffic into the segment. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source</samp>](## "router_segment_security.segments.[].policies.[].source") | String |  |  |  | The name of the source segment. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policy</samp>](## "router_segment_security.segments.[].policies.[].policy") | String |  |  |  | The name of the policy to apply. The built-in policies are ‘policy-forward-all’ and ‘policy-drop-all’. |

=== "YAML"

    ```yaml
    router_segment_security:
      enabled: <bool>

      # Customised application policies.
      # Using the Application Traffic Recognition L4 profiles, custom policies can be defined. The built-in application 'app-match-all' can be used to match any packets.
      # Note that this is stateless, so both the source and destination flows need to be considered.
      policies:

          # Policy name.
        - name: <str; required; unique>
          sequence_numbers: # required

              # Sequence ID.
            - sequence: <int; required; unique>

              # The name of the application.
              application: <str; required>
              action: <str; "permit" | "deny"; required>

      # Defining the segments and associated policies.
      segments: # required

          # Segment name.
        - name: <str; required; unique>
          vrf: <str; default="default">

          # The set of match-lists that define the segment. These can be a mix of IPv4 and IPv6 lists.
          definition: # required

              # The name of the prefix match-list.
            - name: <str>

              # Indicate which address family the match list belongs to e.g. ipv4 or ipv6.
              address_family: <str; "ipv4" | "ipv6"; required>
              covered: <bool; default=False>

          # The policies controlling traffic into the segment.
          policies: # required

              # The name of the source segment.
            - source: <str>

              # The name of the policy to apply. The built-in policies are ‘policy-forward-all’ and ‘policy-drop-all’.
              policy: <str>
    ```
