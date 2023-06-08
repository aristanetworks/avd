=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>access_lists</samp>](## "access_lists") | List, items: Dictionary |  |  |  | AVD currently supports 2 different data models for extended ACLs:<br><br>- The legacy `access_lists` data model, for compatibility with existing deployments<br>- The improved `ip_access_lists` data model, for access to more EOS features<br><br>Both data models can coexists without conflicts, as different keys are used: `access_lists` vs `ip_access_lists`.<br>Access list names must be unique.<br><br>The legacy data model supports simplified ACL definition with `sequence` to `action` mapping:<br> |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "access_lists.[].name") | String | Required, Unique |  |  | Access-list Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "access_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "access_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "access_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string<br>Example: "deny ip any any" |

=== "YAML"

    ```yaml
    access_lists:
      - name: <str>
        counters_per_entry: <bool>
        sequence_numbers:
          - sequence: <int>
            action: <str>
    ```
