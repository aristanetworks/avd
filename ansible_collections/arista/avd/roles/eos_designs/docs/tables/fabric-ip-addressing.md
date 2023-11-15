<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>fabric_ip_addressing</samp>](## "fabric_ip_addressing") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mlag</samp>](## "fabric_ip_addressing.mlag") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "fabric_ip_addressing.mlag.algorithm") | String |  | `first_id` | Valid Values:<br>- <code>first_id</code><br>- <code>odd_id</code><br>- <code>same_subnet</code> | This variable defines the Multi-chassis Link Aggregation (MLAG) algorithm used.<br>Each MLAG link will have a /31 subnet with each subnet allocated from the relevant MLAG pool via a calculated offset.<br>The offset is calculated using one of the following algorithms:<br>  - first_id: `(mlag_primary_id - 1) * 2` where `mlag_primary_id` is the ID of the first node defined under the node_group.<br>    This allocation method will skip every other /31 subnet making it less space efficient than `odd_id`.<br>  - odd_id: `(odd_id - 1) / 2`. Requires the node_group to have a node with an odd ID and a node with an even ID.<br>  - same_subnet: the offset will always be zero.<br>    This allocation method will cause every MLAG link to be addressed with the same /31 subnet.<br> |

=== "YAML"

    ```yaml
    fabric_ip_addressing:
      mlag:

        # This variable defines the Multi-chassis Link Aggregation (MLAG) algorithm used.
        # Each MLAG link will have a /31 subnet with each subnet allocated from the relevant MLAG pool via a calculated offset.
        # The offset is calculated using one of the following algorithms:
        #   - first_id: `(mlag_primary_id - 1) * 2` where `mlag_primary_id` is the ID of the first node defined under the node_group.
        #     This allocation method will skip every other /31 subnet making it less space efficient than `odd_id`.
        #   - odd_id: `(odd_id - 1) / 2`. Requires the node_group to have a node with an odd ID and a node with an even ID.
        #   - same_subnet: the offset will always be zero.
        #     This allocation method will cause every MLAG link to be addressed with the same /31 subnet.
        algorithm: <str; "first_id" | "odd_id" | "same_subnet"; default="first_id">
    ```
