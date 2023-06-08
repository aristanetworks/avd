=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dc_name</samp>](## "dc_name") | String |  |  |  | DC Name, required to match Ansible Group name covering all devices in the DC.<br>Required for 5-stage CLOS (Super-spines).<br> |
    | [<samp>fabric_name</samp>](## "fabric_name") | String | Required |  |  | Fabric Name, required to match Ansible Group name covering all devices in the Fabric, **must** be an inventory group name. |
    | [<samp>pod_name</samp>](## "pod_name") | String |  |  |  | POD Name, only used in Fabric Documentation (Optional), fallback to dc_name and then to fabric_name.<br>Recommended to be common between Spines and Leafs within a POD (One l3ls topology).<br> |

=== "YAML"

    ```yaml
    dc_name: <str>
    fabric_name: <str>
    pod_name: <str>
    ```
