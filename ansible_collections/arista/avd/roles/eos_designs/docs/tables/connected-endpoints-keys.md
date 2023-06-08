=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>connected_endpoints_keys</samp>](## "connected_endpoints_keys") | List, items: Dictionary |  | See (+) on YAML tab |  |  |
    | [<samp>&nbsp;&nbsp;- key</samp>](## "connected_endpoints_keys.[].key") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "connected_endpoints_keys.[].type") | String |  |  |  | Type used for documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "connected_endpoints_keys.[].description") | String |  |  |  | Description used for documentation. |

=== "YAML"

    ```yaml
    1 # (1)!
      - key: <str>
        type: <str>
        description: <str>
    ```

    0. Default Value

        ```yaml
        connected_endpoints_keys:
        - description: Server
          key: servers
          type: server
        - description: Firewall
          key: firewalls
          type: firewall
        - description: Router
          key: routers
          type: router
        - description: Load Balancer
          key: load_balancers
          type: load_balancer
        - description: Storage Array
          key: storage_arrays
          type: storage_array
        - description: CPE
          key: cpes
          type: cpe
        - description: Workstation
          key: workstations
          type: workstation
        - description: Access Point
          key: access_points
          type: access_point
        - description: Phone
          key: phones
          type: phone
        - description: Printer
          key: printers
          type: printer
        - description: Camera
          key: cameras
          type: camera
        - description: Generic Device
          key: generic_devices
          type: generic_device

        ```
