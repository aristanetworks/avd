<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>qos</samp>](## "qos") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;map</samp>](## "qos.map") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "qos.map.cos") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "qos.map.cos.[].&lt;str&gt;") | String |  |  |  | Example: "0 1 to traffic-class 1"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "qos.map.dscp") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "qos.map.dscp.[].&lt;str&gt;") | String |  |  |  | Example: "8 9 10 to traffic-class 1"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "qos.map.traffic_class") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "qos.map.traffic_class.[].&lt;str&gt;") | String |  |  |  | Example: "1 to dscp 32"<br> |
    | [<samp>&nbsp;&nbsp;rewrite_dscp</samp>](## "qos.rewrite_dscp") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    qos:
      map:
        cos:
          - <str>
        dscp:
          - <str>
        traffic_class:
          - <str>
      rewrite_dscp: <bool>
    ```
