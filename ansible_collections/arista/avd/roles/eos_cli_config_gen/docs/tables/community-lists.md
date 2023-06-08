=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>community_lists</samp>](## "community_lists") | List, items: Dictionary |  |  |  | AVD supports 2 different data models for community lists:<br><br>- The legacy `community_lists` data model that can be used for compatibility with the existing deployments.<br>- The improved `ip_community_lists` data model.<br><br>Both data models can coexist without conflicts, as different keys are used: `community_lists` vs `ip_community_lists`.<br>Community list names must be unique.<br><br>The legacy data model supports simplified community list definition that only allows a single action to be defined as string:<br> |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "community_lists.[].name") | String | Required, Unique |  |  | Community-list Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "community_lists.[].action") | String | Required |  |  | Action as string<br>Example: "permit GSHUT 65123:123" |

=== "YAML"

    ```yaml
    community_lists:
      - name: <str>
        action: <str>
    ```
