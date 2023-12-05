<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>sdwan_regions</samp>](## "sdwan_regions") | List, items: Dictionary |  |  |  | PREVIEW: This key is currently not supported<br>Define the SDWAN hierarchy for the device. |
    | [<samp>&nbsp;&nbsp;-&nbsp;description</samp>](## "sdwan_regions.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;zones</samp>](## "sdwan_regions.[].zones") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;description</samp>](## "sdwan_regions.[].zones.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sites</samp>](## "sdwan_regions.[].zones.[].sites") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;description</samp>](## "sdwan_regions.[].zones.[].sites.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;location</samp>](## "sdwan_regions.[].zones.[].sites.[].location") | String |  |  |  | Will be interpreted |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;site_contact</samp>](## "sdwan_regions.[].zones.[].sites.[].site_contact") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;site_after_hours_contact</samp>](## "sdwan_regions.[].zones.[].sites.[].site_after_hours_contact") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "sdwan_regions.[].zones.[].sites.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "sdwan_regions.[].zones.[].sites.[].id") | Integer | Required |  | Min: 1<br>Max: 10000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "sdwan_regions.[].zones.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "sdwan_regions.[].zones.[].id") | Integer | Required |  | Min: 1<br>Max: 10000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "sdwan_regions.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "sdwan_regions.[].id") | Integer | Required |  | Min: 1<br>Max: 255 |  |

=== "YAML"

    ```yaml
    # PREVIEW: This key is currently not supported
    # Define the SDWAN hierarchy for the device.
    sdwan_regions:
      - description: <str>
        zones:
          - description: <str>
            sites:
              - description: <str>

                # Will be interpreted
                location: <str>
                site_contact: <str>
                site_after_hours_contact: <str>
                name: <str; required; unique>
                id: <int; 1-10000; required>
            name: <str; required; unique>
            id: <int; 1-10000; required>
        name: <str; required; unique>
        id: <int; 1-255; required>
    ```
