=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_access_lists_max_entries</samp>](## "ip_access_lists_max_entries") | Integer |  |  |  | The `ip_access_lists` data model allows to limit the number of ACL entries that AVD is allowed to generate by defining `ip_access_lists_max_entries`.<br>Only normal entries under `ip_access_lists` will be counted, remarks will be ignored.<br>If the number is above the limit, the playbook will fail. This provides a simplified control over hardware utilization.<br>The numbers must be based on the hardware tests and AVD does not provide any guidance. Note that other EOS features may use the same hardware resources and affect the supported scale. |

=== "YAML"

    ```yaml
    ip_access_lists_max_entries: <int>
    ```
