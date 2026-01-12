<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_large_community_lists</samp>](## "ip_large_community_lists") | List, items: Dictionary |  |  |  | A BGP large-community access list filters prefixes based on their BGP large community values. Multiple large-community lists with the same name may be specified.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_large_community_lists.[].name") | String | Required, Unique |  |  | IP Large-community-list Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ip_large_community_lists.[].entries") | List, items: Dictionary | Required |  | Min Length: 1 | Large communities and regexp MUST not be configured in the same entry.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;action</samp>](## "ip_large_community_lists.[].entries.[].action") | String | Required |  | Valid Values:<br>- <code>permit</code><br>- <code>deny</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;large_communities</samp>](## "ip_large_community_lists.[].entries.[].large_communities") | List, items: String |  |  | Min Length: 1 | If defined, a standard large-community-list will be configured.<br>Large community values (ASN:Local-part-1:Local-part-2):<br>- ASN:nn:nn<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ip_large_community_lists.[].entries.[].large_communities.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;regexp</samp>](## "ip_large_community_lists.[].entries.[].regexp") | String |  |  |  | Regular Expression.<br>If defined, a regex large-community-list will be configured. |

=== "YAML"

    ```yaml
    # A BGP large-community access list filters prefixes based on their BGP large community values. Multiple large-community lists with the same name may be specified.
    ip_large_community_lists:

        # IP Large-community-list Name.
      - name: <str; required; unique>

        # Large communities and regexp MUST not be configured in the same entry.
        entries: # >=1 items; required
          - action: <str; "permit" | "deny"; required>

            # If defined, a standard large-community-list will be configured.
            # Large community values (ASN:Local-part-1:Local-part-2):
            # - ASN:nn:nn
            large_communities: # >=1 items
              - <str>

            # Regular Expression.
            # If defined, a regex large-community-list will be configured.
            regexp: <str>
    ```
