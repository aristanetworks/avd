=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>qos_profiles</samp>](## "qos_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "qos_profiles.[].name") | String | Required, Unique |  |  | Profile-Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trust</samp>](## "qos_profiles.[].trust") | String |  |  | Valid Values:<br>- cos<br>- dscp<br>- disabled |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "qos_profiles.[].cos") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "qos_profiles.[].dscp") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "qos_profiles.[].shape") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "qos_profiles.[].shape.rate") | String |  |  |  | Supported options are platform dependent<br>Example: "< rate > kbps", "1-100 percent", "< rate > pps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_policy</samp>](## "qos_profiles.[].service_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "qos_profiles.[].service_policy.type") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_input</samp>](## "qos_profiles.[].service_policy.type.qos_input") | String |  |  |  | Policy-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tx_queues</samp>](## "qos_profiles.[].tx_queues") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "qos_profiles.[].tx_queues.[].id") | Integer | Required, Unique |  |  | TX-Queue ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_percent</samp>](## "qos_profiles.[].tx_queues.[].bandwidth_percent") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_guaranteed_percent</samp>](## "qos_profiles.[].tx_queues.[].bandwidth_guaranteed_percent") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "qos_profiles.[].tx_queues.[].priority") | String |  |  | Valid Values:<br>- priority strict<br>- no priority |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "qos_profiles.[].tx_queues.[].shape") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "qos_profiles.[].tx_queues.[].shape.rate") | String |  |  |  | Supported options are platform dependent<br>Example: "< rate > kbps", "1-100 percent", "< rate > pps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "qos_profiles.[].tx_queues.[].comment") | String |  |  |  | Text comment added to queue.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uc_tx_queues</samp>](## "qos_profiles.[].uc_tx_queues") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "qos_profiles.[].uc_tx_queues.[].id") | Integer | Required, Unique |  |  | UC TX queue ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_percent</samp>](## "qos_profiles.[].uc_tx_queues.[].bandwidth_percent") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_guaranteed_percent</samp>](## "qos_profiles.[].uc_tx_queues.[].bandwidth_guaranteed_percent") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "qos_profiles.[].uc_tx_queues.[].priority") | String |  |  | Valid Values:<br>- priority strict<br>- no priority |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "qos_profiles.[].uc_tx_queues.[].shape") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "qos_profiles.[].uc_tx_queues.[].shape.rate") | String |  |  |  | Supported options are platform dependent<br>Example: "< rate > kbps", "1-100 percent", "< rate > pps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "qos_profiles.[].uc_tx_queues.[].comment") | String |  |  |  | Text comment added to queue.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mc_tx_queues</samp>](## "qos_profiles.[].mc_tx_queues") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "qos_profiles.[].mc_tx_queues.[].id") | Integer | Required, Unique |  |  | MC TX queue ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_percent</samp>](## "qos_profiles.[].mc_tx_queues.[].bandwidth_percent") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_guaranteed_percent</samp>](## "qos_profiles.[].mc_tx_queues.[].bandwidth_guaranteed_percent") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "qos_profiles.[].mc_tx_queues.[].priority") | String |  |  | Valid Values:<br>- priority strict<br>- no priority |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "qos_profiles.[].mc_tx_queues.[].shape") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "qos_profiles.[].mc_tx_queues.[].shape.rate") | String |  |  |  | Supported options are platform dependent<br>Example: "< rate > kbps", "1-100 percent", "< rate > pps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "qos_profiles.[].mc_tx_queues.[].comment") | String |  |  |  | Text comment added to queue. |

=== "YAML"

    ```yaml
    qos_profiles:
      - name: <str>
        trust: <str>
        cos: <int>
        dscp: <int>
        shape:
          rate: <str>
        service_policy:
          type:
            qos_input: <str>
        tx_queues:
          - id: <int>
            bandwidth_percent: <int>
            bandwidth_guaranteed_percent: <int>
            priority: <str>
            shape:
              rate: <str>
            comment: <str>
        uc_tx_queues:
          - id: <int>
            bandwidth_percent: <int>
            bandwidth_guaranteed_percent: <int>
            priority: <str>
            shape:
              rate: <str>
            comment: <str>
        mc_tx_queues:
          - id: <int>
            bandwidth_percent: <int>
            bandwidth_guaranteed_percent: <int>
            priority: <str>
            shape:
              rate: <str>
            comment: <str>
    ```
