<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cv_pathfinder_regions</samp>](## "cv_pathfinder_regions") | List, items: Dictionary |  |  |  | Define the CV Pathfinder hierarchy. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_pathfinder_regions.[].name") | String | Required, Unique |  |  | The region name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "cv_pathfinder_regions.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "cv_pathfinder_regions.[].id") | Integer | Required |  | Min: 1<br>Max: 255 | The region ID must be unique for the whole WAN deployment. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sites</samp>](## "cv_pathfinder_regions.[].sites") | List, items: Dictionary |  |  |  | All sites are placed in a default zone "<region_name>-ZONE" with ID 1. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_pathfinder_regions.[].sites.[].name") | String | Required, Unique |  |  | The site name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "cv_pathfinder_regions.[].sites.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "cv_pathfinder_regions.[].sites.[].id") | Integer | Required |  | Min: 1<br>Max: 10000 | The site ID must be unique within a zone.<br>Given that all the sites are placed in a zone named after the region, the site ID must be unique within a region. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;location</samp>](## "cv_pathfinder_regions.[].sites.[].location") | String |  |  |  | Location as a sring is resolved on Cloudvision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;site_contact</samp>](## "cv_pathfinder_regions.[].sites.[].site_contact") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;site_after_hours_contact</samp>](## "cv_pathfinder_regions.[].sites.[].site_after_hours_contact") | String |  |  |  |  |

=== "YAML"

    ```yaml
    # Define the CV Pathfinder hierarchy.
    cv_pathfinder_regions:

        # The region name.
      - name: <str; required; unique>
        description: <str>

        # The region ID must be unique for the whole WAN deployment.
        id: <int; 1-255; required>

        # All sites are placed in a default zone "<region_name>-ZONE" with ID 1.
        sites:

            # The site name.
          - name: <str; required; unique>
            description: <str>

            # The site ID must be unique within a zone.
            # Given that all the sites are placed in a zone named after the region, the site ID must be unique within a region.
            id: <int; 1-10000; required>

            # Location as a sring is resolved on Cloudvision.
            location: <str>
            site_contact: <str>
            site_after_hours_contact: <str>
    ```
