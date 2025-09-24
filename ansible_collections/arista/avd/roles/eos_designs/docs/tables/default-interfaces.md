<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_interfaces</samp>](## "default_interfaces") | List, items: Dictionary |  |  |  | Default uplink, downlink, and MLAG interfaces, which will be used if these interfaces are not defined on a device (either directly or through inheritance).<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;types</samp>](## "default_interfaces.[].types") | List, items: String | Required |  |  | List of node type keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "default_interfaces.[].types.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;platforms</samp>](## "default_interfaces.[].platforms") | List, items: String | Required |  |  | List of platform families.<br>This is defined as a Python regular expression that matches the full platform type.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "default_interfaces.[].platforms.[]") | String |  |  |  | Arista platform family regular expression. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "default_interfaces.[].uplink_interfaces") | List, items: String |  |  |  | List of uplink interfaces or uplink interface ranges. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "default_interfaces.[].uplink_interfaces.[]") | String |  |  |  | Interface range or interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "default_interfaces.[].mlag_interfaces") | List, items: String |  |  |  | List of MLAG interfaces or MLAG interface ranges. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "default_interfaces.[].mlag_interfaces.[]") | String |  |  |  | Interface range or interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces_speed</samp>](## "default_interfaces.[].mlag_interfaces_speed") | String |  |  | Valid Values:<br>- <code>100full</code><br>- <code>100g</code><br>- <code>100g-1</code><br>- <code>100g-2</code><br>- <code>100g-4</code><br>- <code>100half</code><br>- <code>10full</code><br>- <code>10g</code><br>- <code>10half</code><br>- <code>1g</code><br>- <code>200g</code><br>- <code>200g-2</code><br>- <code>200g-4</code><br>- <code>25g</code><br>- <code>400g</code><br>- <code>400g-4</code><br>- <code>400g-8</code><br>- <code>40g</code><br>- <code>50g</code><br>- <code>50g-1</code><br>- <code>50g-2</code><br>- <code>800g-8</code><br>- <code>sfp-1000baset auto 100full</code><br>- <code>1.6t-8</code><br>- <code>100mfull</code><br>- <code>100mhalf</code><br>- <code>10mfull</code><br>- <code>10mhalf</code><br>- <code>200g-1</code><br>- <code>400g-2</code><br>- <code>40g-4</code><br>- <code>800g-4</code><br>- <code>auto</code><br>- <code>auto 10000full</code><br>- <code>auto 1000full</code><br>- <code>auto 100full</code><br>- <code>auto 100g-1</code><br>- <code>auto 100g-2</code><br>- <code>auto 100g-4</code><br>- <code>auto 100gfull</code><br>- <code>auto 100half</code><br>- <code>auto 10full</code><br>- <code>auto 10gfull</code><br>- <code>auto 10half</code><br>- <code>auto 1gfull</code><br>- <code>auto 2.5gfull</code><br>- <code>auto 200g-2</code><br>- <code>auto 200g-4</code><br>- <code>auto 25gfull</code><br>- <code>auto 400g-4</code><br>- <code>auto 400g-8</code><br>- <code>auto 40gfull</code><br>- <code>auto 50g-1</code><br>- <code>auto 50g-2</code><br>- <code>auto 50gfull</code><br>- <code>auto 5gfull</code><br>- <code>auto 800g-8</code><br>- <code>auto 1.6t-8</code><br>- <code>auto 100mfull</code><br>- <code>auto 100mhalf</code><br>- <code>auto 10g</code><br>- <code>auto 10mfull</code><br>- <code>auto 10mhalf</code><br>- <code>auto 1g</code><br>- <code>auto 2.5g</code><br>- <code>auto 200g-1</code><br>- <code>auto 25g</code><br>- <code>auto 400g-2</code><br>- <code>auto 40g-4</code><br>- <code>auto 5g</code><br>- <code>auto 800g-4</code><br>- <code>forced 10000full</code><br>- <code>forced 1000full</code><br>- <code>forced 1000half</code><br>- <code>forced 100full</code><br>- <code>forced 100gfull</code><br>- <code>forced 100half</code><br>- <code>forced 10full</code><br>- <code>forced 10half</code><br>- <code>forced 25gfull</code><br>- <code>forced 40gfull</code><br>- <code>forced 50gfull</code> | Set MLAG interfaces speed.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;downlink_interfaces</samp>](## "default_interfaces.[].downlink_interfaces") | List, items: String |  |  |  | List of downlink interfaces or downlink interface ranges. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "default_interfaces.[].downlink_interfaces.[]") | String |  |  |  | Interface range or interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_interface_speed</samp>](## "default_interfaces.[].uplink_interface_speed") | String |  |  | Valid Values:<br>- <code>100full</code><br>- <code>100g</code><br>- <code>100g-1</code><br>- <code>100g-2</code><br>- <code>100g-4</code><br>- <code>100half</code><br>- <code>10full</code><br>- <code>10g</code><br>- <code>10half</code><br>- <code>1g</code><br>- <code>200g</code><br>- <code>200g-2</code><br>- <code>200g-4</code><br>- <code>25g</code><br>- <code>400g</code><br>- <code>400g-4</code><br>- <code>400g-8</code><br>- <code>40g</code><br>- <code>50g</code><br>- <code>50g-1</code><br>- <code>50g-2</code><br>- <code>800g-8</code><br>- <code>sfp-1000baset auto 100full</code><br>- <code>1.6t-8</code><br>- <code>100mfull</code><br>- <code>100mhalf</code><br>- <code>10mfull</code><br>- <code>10mhalf</code><br>- <code>200g-1</code><br>- <code>400g-2</code><br>- <code>40g-4</code><br>- <code>800g-4</code><br>- <code>auto</code><br>- <code>auto 10000full</code><br>- <code>auto 1000full</code><br>- <code>auto 100full</code><br>- <code>auto 100g-1</code><br>- <code>auto 100g-2</code><br>- <code>auto 100g-4</code><br>- <code>auto 100gfull</code><br>- <code>auto 100half</code><br>- <code>auto 10full</code><br>- <code>auto 10gfull</code><br>- <code>auto 10half</code><br>- <code>auto 1gfull</code><br>- <code>auto 2.5gfull</code><br>- <code>auto 200g-2</code><br>- <code>auto 200g-4</code><br>- <code>auto 25gfull</code><br>- <code>auto 400g-4</code><br>- <code>auto 400g-8</code><br>- <code>auto 40gfull</code><br>- <code>auto 50g-1</code><br>- <code>auto 50g-2</code><br>- <code>auto 50gfull</code><br>- <code>auto 5gfull</code><br>- <code>auto 800g-8</code><br>- <code>auto 1.6t-8</code><br>- <code>auto 100mfull</code><br>- <code>auto 100mhalf</code><br>- <code>auto 10g</code><br>- <code>auto 10mfull</code><br>- <code>auto 10mhalf</code><br>- <code>auto 1g</code><br>- <code>auto 2.5g</code><br>- <code>auto 200g-1</code><br>- <code>auto 25g</code><br>- <code>auto 400g-2</code><br>- <code>auto 40g-4</code><br>- <code>auto 5g</code><br>- <code>auto 800g-4</code><br>- <code>forced 10000full</code><br>- <code>forced 1000full</code><br>- <code>forced 1000half</code><br>- <code>forced 100full</code><br>- <code>forced 100gfull</code><br>- <code>forced 100half</code><br>- <code>forced 10full</code><br>- <code>forced 10half</code><br>- <code>forced 25gfull</code><br>- <code>forced 40gfull</code><br>- <code>forced 50gfull</code> | Set point-to-Point uplink interface speed. |

=== "YAML"

    ```yaml
    # Default uplink, downlink, and MLAG interfaces, which will be used if these interfaces are not defined on a device (either directly or through inheritance).
    default_interfaces:

        # List of node type keys.
      - types: # required
          - <str>

        # List of platform families.
        # This is defined as a Python regular expression that matches the full platform type.
        platforms: # required

            # Arista platform family regular expression.
          - <str>

        # List of uplink interfaces or uplink interface ranges.
        uplink_interfaces:

            # Interface range or interface.
          - <str>

        # List of MLAG interfaces or MLAG interface ranges.
        mlag_interfaces:

            # Interface range or interface.
          - <str>

        # Set MLAG interfaces speed.
        mlag_interfaces_speed: <str; "100full" | "100g" | "100g-1" | "100g-2" | "100g-4" | "100half" | "10full" | "10g" | "10half" | "1g" | "200g" | "200g-2" | "200g-4" | "25g" | "400g" | "400g-4" | "400g-8" | "40g" | "50g" | "50g-1" | "50g-2" | "800g-8" | "sfp-1000baset auto 100full" | "1.6t-8" | "100mfull" | "100mhalf" | "10mfull" | "10mhalf" | "200g-1" | "400g-2" | "40g-4" | "800g-4" | "auto" | "auto 10000full" | "auto 1000full" | "auto 100full" | "auto 100g-1" | "auto 100g-2" | "auto 100g-4" | "auto 100gfull" | "auto 100half" | "auto 10full" | "auto 10gfull" | "auto 10half" | "auto 1gfull" | "auto 2.5gfull" | "auto 200g-2" | "auto 200g-4" | "auto 25gfull" | "auto 400g-4" | "auto 400g-8" | "auto 40gfull" | "auto 50g-1" | "auto 50g-2" | "auto 50gfull" | "auto 5gfull" | "auto 800g-8" | "auto 1.6t-8" | "auto 100mfull" | "auto 100mhalf" | "auto 10g" | "auto 10mfull" | "auto 10mhalf" | "auto 1g" | "auto 2.5g" | "auto 200g-1" | "auto 25g" | "auto 400g-2" | "auto 40g-4" | "auto 5g" | "auto 800g-4" | "forced 10000full" | "forced 1000full" | "forced 1000half" | "forced 100full" | "forced 100gfull" | "forced 100half" | "forced 10full" | "forced 10half" | "forced 25gfull" | "forced 40gfull" | "forced 50gfull">

        # List of downlink interfaces or downlink interface ranges.
        downlink_interfaces:

            # Interface range or interface.
          - <str>

        # Set point-to-Point uplink interface speed.
        uplink_interface_speed: <str; "100full" | "100g" | "100g-1" | "100g-2" | "100g-4" | "100half" | "10full" | "10g" | "10half" | "1g" | "200g" | "200g-2" | "200g-4" | "25g" | "400g" | "400g-4" | "400g-8" | "40g" | "50g" | "50g-1" | "50g-2" | "800g-8" | "sfp-1000baset auto 100full" | "1.6t-8" | "100mfull" | "100mhalf" | "10mfull" | "10mhalf" | "200g-1" | "400g-2" | "40g-4" | "800g-4" | "auto" | "auto 10000full" | "auto 1000full" | "auto 100full" | "auto 100g-1" | "auto 100g-2" | "auto 100g-4" | "auto 100gfull" | "auto 100half" | "auto 10full" | "auto 10gfull" | "auto 10half" | "auto 1gfull" | "auto 2.5gfull" | "auto 200g-2" | "auto 200g-4" | "auto 25gfull" | "auto 400g-4" | "auto 400g-8" | "auto 40gfull" | "auto 50g-1" | "auto 50g-2" | "auto 50gfull" | "auto 5gfull" | "auto 800g-8" | "auto 1.6t-8" | "auto 100mfull" | "auto 100mhalf" | "auto 10g" | "auto 10mfull" | "auto 10mhalf" | "auto 1g" | "auto 2.5g" | "auto 200g-1" | "auto 25g" | "auto 400g-2" | "auto 40g-4" | "auto 5g" | "auto 800g-4" | "forced 10000full" | "forced 1000full" | "forced 1000half" | "forced 100full" | "forced 100gfull" | "forced 100half" | "forced 10full" | "forced 10half" | "forced 25gfull" | "forced 40gfull" | "forced 50gfull">
    ```
