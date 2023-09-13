<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>network_ports</samp>](## "network_ports") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- switches</samp>](## "network_ports.[].switches") | List, items: String |  |  |  | Regex matching the full hostname of one or more switches.<br>The regular expression must match the full hostname.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_ports.[].switches.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;switch_ports</samp>](## "network_ports.[].switch_ports") | List, items: String |  |  |  | List of ranges using AVD range_expand syntax.<br>For example:<br><br>switch_ports:<br>  - Ethernet1<br>  - Ethernet2-48<br><br>All switch_ports ranges are expanded into individual port configurations.<br><br>For more details and examples of the `range_expand` syntax, see the [arista.avd.range_expand documentation](../../../plugins/README.md#range_expand-filter)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_ports.[].switch_ports.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "network_ports.[].description") | String |  |  |  | Description to be used on all ports. |

=== "YAML"

    ```yaml
    network_ports:
      - switches:
          - <str>
        switch_ports:
          - <str>
        description: <str>
    ```
