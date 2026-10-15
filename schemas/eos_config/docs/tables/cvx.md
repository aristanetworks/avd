<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cvx</samp>](## "cvx") | Dictionary |  |  |  | CVX server features are not supported on physical switches. See `management_cvx` for client configurations. |
    | [<samp>&nbsp;&nbsp;shutdown</samp>](## "cvx.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;peer_hosts</samp>](## "cvx.peer_hosts") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "cvx.peer_hosts.[]") | String |  |  |  | IP address or hostname. |
    | [<samp>&nbsp;&nbsp;services</samp>](## "cvx.services") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mcs</samp>](## "cvx.services.mcs") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redis</samp>](## "cvx.services.mcs.redis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "cvx.services.mcs.redis.password") | String |  |  |  | Hashed password using the password_type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password_type</samp>](## "cvx.services.mcs.redis.password_type") | String |  | `7` | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "cvx.services.mcs.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "cvx.services.vxlan") | Dictionary |  |  |  | VXLAN Controller service. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "cvx.services.vxlan.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_mac_learning</samp>](## "cvx.services.vxlan.vtep_mac_learning") | String |  |  | Valid Values:<br>- <code>control-plane</code><br>- <code>data-plane</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;openstack</samp>](## "cvx.services.openstack") | Dictionary |  |  |  | OpenStack services. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "cvx.services.openstack.authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "cvx.services.openstack.authentication.role") | String |  |  |  | API authentication user role. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;grace_period</samp>](## "cvx.services.openstack.grace_period") | Integer |  |  | Min: 0<br>Max: 14400 | Set the grace period in seconds for which the OpenStack agent waits for OpenStack region data. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_access_group_name</samp>](## "cvx.services.openstack.ip_access_group_name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_name</samp>](## "cvx.services.openstack.ipv6_access_group_name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name_resolution</samp>](## "cvx.services.openstack.name_resolution") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;force</samp>](## "cvx.services.openstack.name_resolution.force") | Boolean |  |  |  | Get the tenant and VM names from OpenStack immediately. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "cvx.services.openstack.name_resolution.interval") | Integer |  |  | Min: 0<br>Max: 86400 | Set the time interval in seconds between name updates, 0 to disable. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;network_type_driver</samp>](## "cvx.services.openstack.network_type_driver") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "cvx.services.openstack.network_type_driver.vlan") | String |  |  | Valid Values:<br>- <code>arista</code><br>- <code>default</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;regions</samp>](## "cvx.services.openstack.regions") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cvx.services.openstack.regions.[].name") | String | Required, Unique |  |  | The name of the region. This must match what is in use in the ML2 driver configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;username</samp>](## "cvx.services.openstack.regions.[].username") | String |  |  |  | 'admin' or valid keystone user. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "cvx.services.openstack.regions.[].password") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password_type</samp>](## "cvx.services.openstack.regions.[].password_type") | String |  | `7` | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp>](## "cvx.services.openstack.regions.[].tenant") | String |  |  |  | Tenant name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keystone</samp>](## "cvx.services.openstack.regions.[].keystone") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_url</samp>](## "cvx.services.openstack.regions.[].keystone.auth_url") | String |  |  | Pattern: `^https?://(?:(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+[A-Za-z]{2,6}\.?|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?::\d+)?/v(2\.0|3)/$` |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "cvx.services.openstack.shutdown") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    # CVX server features are not supported on physical switches. See `management_cvx` for client configurations.
    cvx:
      shutdown: <bool>
      peer_hosts:

          # IP address or hostname.
        - <str>
      services:
        mcs:
          redis:

            # Hashed password using the password_type.
            password: <str>
            password_type: <str; "0" | "7" | "8a"; default="7">
          shutdown: <bool>

        # VXLAN Controller service.
        vxlan:
          shutdown: <bool>
          vtep_mac_learning: <str; "control-plane" | "data-plane">

        # OpenStack services.
        openstack:
          authentication:

            # API authentication user role.
            role: <str>

          # Set the grace period in seconds for which the OpenStack agent waits for OpenStack region data.
          grace_period: <int; 0-14400>
          ip_access_group_name: <str>
          ipv6_access_group_name: <str>
          name_resolution:

            # Get the tenant and VM names from OpenStack immediately.
            force: <bool>

            # Set the time interval in seconds between name updates, 0 to disable.
            interval: <int; 0-86400>
          network_type_driver:
            vlan: <str; "arista" | "default">
          regions: # >=1 items

              # The name of the region. This must match what is in use in the ML2 driver configuration.
            - name: <str; required; unique>

              # 'admin' or valid keystone user.
              username: <str>
              password: <str>
              password_type: <str; "0" | "7" | "8a"; default="7">

              # Tenant name.
              tenant: <str>
              keystone:
                auth_url: <str>
          shutdown: <bool>
    ```
