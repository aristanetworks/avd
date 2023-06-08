=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>prefix_lists</samp>](## "prefix_lists") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "prefix_lists.[].name") | String | Required, Unique |  |  | Prefix-list Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "prefix_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "prefix_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "prefix_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string<br>Example: "permit 10.255.0.0/27 eq 32" |

=== "YAML"

    ```yaml
    prefix_lists:
      - name: <str>
        sequence_numbers:
          - sequence: <int>
            action: <str>
    ```
