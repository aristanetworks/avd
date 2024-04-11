<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>zscaler_endpoints</samp>](## "zscaler_endpoints") | Dictionary |  |  |  | PREVIEW: These keys are in preview mode.<br><br>Special data model used for WAN internet-exit integration with Zscaler.<br>The model is supposed to be autofilled per-device using the `arista.avd.zscaler_endpoints` Ansible lookup plugin.<br>Example:<br>```yaml<br>zscaler_endpoints: "{{ lookup('arista.avd.zscaler_endpoints', !!!!TBD!!!!) }}"<br>``` |
    | [<samp>&nbsp;&nbsp;primary</samp>](## "zscaler_endpoints.primary") | Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "zscaler_endpoints.primary.ip_address") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;datacenter</samp>](## "zscaler_endpoints.primary.datacenter") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;city</samp>](## "zscaler_endpoints.primary.city") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;country</samp>](## "zscaler_endpoints.primary.country") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;latitude</samp>](## "zscaler_endpoints.primary.latitude") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;longitude</samp>](## "zscaler_endpoints.primary.longitude") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;secondary</samp>](## "zscaler_endpoints.secondary") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "zscaler_endpoints.secondary.ip_address") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;datacenter</samp>](## "zscaler_endpoints.secondary.datacenter") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;city</samp>](## "zscaler_endpoints.secondary.city") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;country</samp>](## "zscaler_endpoints.secondary.country") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;latitude</samp>](## "zscaler_endpoints.secondary.latitude") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;longitude</samp>](## "zscaler_endpoints.secondary.longitude") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;tertiary</samp>](## "zscaler_endpoints.tertiary") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "zscaler_endpoints.tertiary.ip_address") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;datacenter</samp>](## "zscaler_endpoints.tertiary.datacenter") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;city</samp>](## "zscaler_endpoints.tertiary.city") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;country</samp>](## "zscaler_endpoints.tertiary.country") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;latitude</samp>](## "zscaler_endpoints.tertiary.latitude") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;longitude</samp>](## "zscaler_endpoints.tertiary.longitude") | String | Required |  |  |  |

=== "YAML"

    ```yaml
    # PREVIEW: These keys are in preview mode.
    #
    # Special data model used for WAN internet-exit integration with Zscaler.
    # The model is supposed to be autofilled per-device using the `arista.avd.zscaler_endpoints` Ansible lookup plugin.
    # Example:
    # ```yaml
    # zscaler_endpoints: "{{ lookup('arista.avd.zscaler_endpoints', !!!!TBD!!!!) }}"
    # ```
    zscaler_endpoints:
      primary: # required
        ip_address: <str; required>
        datacenter: <str; required>
        city: <str; required>
        country: <str; required>
        latitude: <str; required>
        longitude: <str; required>
      secondary:
        ip_address: <str; required>
        datacenter: <str; required>
        city: <str; required>
        country: <str; required>
        latitude: <str; required>
        longitude: <str; required>
      tertiary:
        ip_address: <str; required>
        datacenter: <str; required>
        city: <str; required>
        country: <str; required>
        latitude: <str; required>
        longitude: <str; required>
    ```
