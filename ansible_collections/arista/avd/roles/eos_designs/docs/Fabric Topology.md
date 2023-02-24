---
search:
  boost: 2
---

# Fabric Topology

## Default Interfaces

- Set default uplink, downlink, and MLAG interfaces, which will be used if these interfaces are not defined on a device (either directly or through inheritance).
- These are defined based on the combination of node_type (e.g., l3leaf or spine) and a regex for matching the platform.
- A list of interfaces or interface ranges can be specified.
- Each list item supports range syntax that can be expanded into a list of interfaces. Interface range examples:
  - Ethernet49-52/1: Expands to [ Ethernet49/1, Ethernet50/1, Ethernet51/1, Ethernet52/1 ]
  - Ethernet1/31-34/1: Expands to [ Ethernet1/31/1, Ethernet1/32/1, Ethernet1/33/1, Ethernet1/34/1 ]
  - Ethernet49-50,53-54: Expands to [ Ethernet49, Ethernet50, Ethernet53, Ethernet54 ]
  - Ethernet1-2/1-4: Expands to [ Ethernet1/1, Ethernet1/2, Ethernet1/3, Ethernet1/4, Ethernet2/1, Ethernet2/2, Ethernet2/3, Ethernet2/4 ]
- `uplink_interfaces` and `mlag_interfaces` under `default_interfaces` are directly inherited by `uplink_interfaces` and `mlag_interfaces`.
- `downlink_interfaces` are referenced by the child switch (e.g., the leaf in a leaf/spine network). The child switch leverages an upstream switch's `default_downlink_interfaces` using the child switch ID.  This is then used to build `uplink_switch_interfaces` for that child.
  - In the case of `max_parallel_uplinks` > 1 the `default_downlink_interfaces` are mapped with consecutive downlinks per child ID.
  - Example for `max_parallel_uplinks: 2`, downlink interfaces will be mapped as `[ <downlink1 to leaf-id1>, <downlink2 to leaf-id1>, <downlink1 to leaf-id2>, <downlink2 to leaf-id2> ...]`
- Please note that no default interfaces are defined in AVD itself. You will need to create your own based on the example below.

Example:

```yaml
default_interfaces:
  - types: [ spine, l3leaf ]
    platforms: [ "7050[SC]X3", vEOS.*, default ]
    uplink_interfaces: [ Ethernet49-54/1 ]
    mlag_interfaces: [ Ethernet55-56/1 ]
    downlink_interfaces: [ Ethernet1-32/1 ]
```

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_interfaces</samp>](## "default_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- types</samp>](## "default_interfaces.[].types") | List, items: String | Required |  |  | List of node type keys |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_interfaces.[].types.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;platforms</samp>](## "default_interfaces.[].platforms") | List, items: String | Required |  |  | List of platform families<br>This is defined as a Python regular expression that matches the full platform type<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_interfaces.[].platforms.[].&lt;str&gt;") | String |  |  |  | Arista platform family regular expression |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "default_interfaces.[].uplink_interfaces") | List, items: String |  |  |  | List of uplink interfaces or uplink interface ranges |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_interfaces.[].uplink_interfaces.[].&lt;str&gt;") | String |  |  |  | Interface range or interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "default_interfaces.[].mlag_interfaces") | List, items: String |  |  |  | List of MLAG interfaces or MLAG interface ranges |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_interfaces.[].mlag_interfaces.[].&lt;str&gt;") | String |  |  |  | Interface range or interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;downlink_interfaces</samp>](## "default_interfaces.[].downlink_interfaces") | List, items: String |  |  |  | List of downlink interfaces or downlink interface ranges |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_interfaces.[].downlink_interfaces.[].&lt;str&gt;") | String |  |  |  | Interface range or interface |

=== "YAML"

    ```yaml
    default_interfaces:
      - types:
          - <str>
        platforms:
          - <str>
        uplink_interfaces:
          - <str>
        mlag_interfaces:
          - <str>
        downlink_interfaces:
          - <str>
    ```
