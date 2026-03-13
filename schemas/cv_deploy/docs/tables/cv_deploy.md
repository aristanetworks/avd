<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>is_deployed</samp>](## "is_deployed") | Boolean |  | `True` |  | When set to `false`, the device will be skipped from all operations performed by the `cv_deploy` role. |
    | [<samp>serial_number</samp>](## "serial_number") | String |  |  |  | Serial number of the device used to identify the device in CloudVision.<br>Takes precedence over `system_mac_address` and `inventory_hostname`.<br><br>Device identification precedence:<br>  1. `serial_number` (highest priority)<br>  2. `system_mac_address`<br>  3. `inventory_hostname` (lowest priority, used only if neither of the above is set) |
    | [<samp>system_mac_address</samp>](## "system_mac_address") | String |  |  |  | System MAC address of the device used to identify the device in CloudVision.<br>Should match the MAC address shown in "show version" on the device.<br>Used when `serial_number` is not set.<br><br>Device identification precedence:<br>  1. `serial_number` (highest priority)<br>  2. `system_mac_address`<br>  3. `inventory_hostname` (lowest priority, used only if neither of the above is set) |
    | [<samp>cv_device_tags</samp>](## "cv_device_tags") | List, items: Dictionary |  |  |  | List of CloudVision device tags to be assigned to this device. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_device_tags.[].name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "cv_device_tags.[].value") | String | Required |  |  |  |
    | [<samp>cv_interface_tags</samp>](## "cv_interface_tags") | List, items: Dictionary |  |  |  | List of CloudVision interface tags to be assigned to interfaces on this device. |
    | [<samp>&nbsp;&nbsp;-&nbsp;interface</samp>](## "cv_interface_tags.[].interface") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "cv_interface_tags.[].tags") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_interface_tags.[].tags.[].name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "cv_interface_tags.[].tags.[].value") | String | Required |  |  |  |
    | [<samp>cv_pathfinder_metadata</samp>](## "cv_pathfinder_metadata") | Dictionary |  |  |  | Metadata used for CV Pathfinder visualization on CloudVision. |
    | [<samp>&nbsp;&nbsp;role</samp>](## "cv_pathfinder_metadata.role") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;region</samp>](## "cv_pathfinder_metadata.region") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;zone</samp>](## "cv_pathfinder_metadata.zone") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;site</samp>](## "cv_pathfinder_metadata.site") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;vtep_ip</samp>](## "cv_pathfinder_metadata.vtep_ip") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ssl_profile</samp>](## "cv_pathfinder_metadata.ssl_profile") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;address</samp>](## "cv_pathfinder_metadata.address") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;pathfinders</samp>](## "cv_pathfinder_metadata.pathfinders") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;vtep_ip</samp>](## "cv_pathfinder_metadata.pathfinders.[].vtep_ip") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;interfaces</samp>](## "cv_pathfinder_metadata.interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_pathfinder_metadata.interfaces.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;carrier</samp>](## "cv_pathfinder_metadata.interfaces.[].carrier") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;circuit_id</samp>](## "cv_pathfinder_metadata.interfaces.[].circuit_id") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pathgroup</samp>](## "cv_pathfinder_metadata.interfaces.[].pathgroup") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;public_ip</samp>](## "cv_pathfinder_metadata.interfaces.[].public_ip") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;pathgroups</samp>](## "cv_pathfinder_metadata.pathgroups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_pathfinder_metadata.pathgroups.[].name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;carriers</samp>](## "cv_pathfinder_metadata.pathgroups.[].carriers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_pathfinder_metadata.pathgroups.[].carriers.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;imported_carriers</samp>](## "cv_pathfinder_metadata.pathgroups.[].imported_carriers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_pathfinder_metadata.pathgroups.[].imported_carriers.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;regions</samp>](## "cv_pathfinder_metadata.regions") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "cv_pathfinder_metadata.regions.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "cv_pathfinder_metadata.regions.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;zones</samp>](## "cv_pathfinder_metadata.regions.[].zones") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "cv_pathfinder_metadata.regions.[].zones.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "cv_pathfinder_metadata.regions.[].zones.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sites</samp>](## "cv_pathfinder_metadata.regions.[].zones.[].sites") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "cv_pathfinder_metadata.regions.[].zones.[].sites.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "cv_pathfinder_metadata.regions.[].zones.[].sites.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;location</samp>](## "cv_pathfinder_metadata.regions.[].zones.[].sites.[].location") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "cv_pathfinder_metadata.regions.[].zones.[].sites.[].location.address") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "cv_pathfinder_metadata.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_pathfinder_metadata.vrfs.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni</samp>](## "cv_pathfinder_metadata.vrfs.[].vni") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;avts</samp>](## "cv_pathfinder_metadata.vrfs.[].avts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;constraints</samp>](## "cv_pathfinder_metadata.vrfs.[].avts.[].constraints") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;jitter</samp>](## "cv_pathfinder_metadata.vrfs.[].avts.[].constraints.jitter") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;latency</samp>](## "cv_pathfinder_metadata.vrfs.[].avts.[].constraints.latency") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lossrate</samp>](## "cv_pathfinder_metadata.vrfs.[].avts.[].constraints.lossrate") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hop_count</samp>](## "cv_pathfinder_metadata.vrfs.[].avts.[].constraints.hop_count") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "cv_pathfinder_metadata.vrfs.[].avts.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "cv_pathfinder_metadata.vrfs.[].avts.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "cv_pathfinder_metadata.vrfs.[].avts.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pathgroups</samp>](## "cv_pathfinder_metadata.vrfs.[].avts.[].pathgroups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_pathfinder_metadata.vrfs.[].avts.[].pathgroups.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preference</samp>](## "cv_pathfinder_metadata.vrfs.[].avts.[].pathgroups.[].preference") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;application_profiles</samp>](## "cv_pathfinder_metadata.vrfs.[].avts.[].application_profiles") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "cv_pathfinder_metadata.vrfs.[].avts.[].application_profiles.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;internet_exit_policies</samp>](## "cv_pathfinder_metadata.internet_exit_policies") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].type") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;city</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].city") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;country</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].country") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;upload_bandwidth</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].upload_bandwidth") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;download_bandwidth</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].download_bandwidth") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;firewall</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].firewall") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ips_control</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].ips_control") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;acceptable_use_policy</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].acceptable_use_policy") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vpn_credentials</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].vpn_credentials") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;fqdn</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].vpn_credentials.[].fqdn") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vpn_type</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].vpn_credentials.[].vpn_type") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pre_shared_key</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].vpn_credentials.[].pre_shared_key") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnels</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].tunnels") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].tunnels.[].name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preference</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].tunnels.[].preference") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endpoint</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].tunnels.[].endpoint") | Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].tunnels.[].endpoint.ip_address") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;datacenter</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].tunnels.[].endpoint.datacenter") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;city</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].tunnels.[].endpoint.city") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;country</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].tunnels.[].endpoint.country") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;region</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].tunnels.[].endpoint.region") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;latitude</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].tunnels.[].endpoint.latitude") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;longitude</samp>](## "cv_pathfinder_metadata.internet_exit_policies.[].tunnels.[].endpoint.longitude") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;applications</samp>](## "cv_pathfinder_metadata.applications") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profiles</samp>](## "cv_pathfinder_metadata.applications.profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_pathfinder_metadata.applications.profiles.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;builtin_applications</samp>](## "cv_pathfinder_metadata.applications.profiles.[].builtin_applications") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_pathfinder_metadata.applications.profiles.[].builtin_applications.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;services</samp>](## "cv_pathfinder_metadata.applications.profiles.[].builtin_applications.[].services") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "cv_pathfinder_metadata.applications.profiles.[].builtin_applications.[].services.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;user_defined_applications</samp>](## "cv_pathfinder_metadata.applications.profiles.[].user_defined_applications") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_pathfinder_metadata.applications.profiles.[].user_defined_applications.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;categories</samp>](## "cv_pathfinder_metadata.applications.profiles.[].categories") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;category</samp>](## "cv_pathfinder_metadata.applications.profiles.[].categories.[].category") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;services</samp>](## "cv_pathfinder_metadata.applications.profiles.[].categories.[].services") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "cv_pathfinder_metadata.applications.profiles.[].categories.[].services.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transport_protocols</samp>](## "cv_pathfinder_metadata.applications.profiles.[].transport_protocols") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "cv_pathfinder_metadata.applications.profiles.[].transport_protocols.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;categories</samp>](## "cv_pathfinder_metadata.applications.categories") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;builtin_applications</samp>](## "cv_pathfinder_metadata.applications.categories.builtin_applications") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_pathfinder_metadata.applications.categories.builtin_applications.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;category</samp>](## "cv_pathfinder_metadata.applications.categories.builtin_applications.[].category") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;services</samp>](## "cv_pathfinder_metadata.applications.categories.builtin_applications.[].services") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "cv_pathfinder_metadata.applications.categories.builtin_applications.[].services.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;user_defined_applications</samp>](## "cv_pathfinder_metadata.applications.categories.user_defined_applications") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_pathfinder_metadata.applications.categories.user_defined_applications.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;category</samp>](## "cv_pathfinder_metadata.applications.categories.user_defined_applications.[].category") | String |  |  |  |  |

=== "YAML"

    ```yaml
    # When set to `false`, the device will be skipped from all operations performed by the `cv_deploy` role.
    is_deployed: <bool; default=True>

    # Serial number of the device used to identify the device in CloudVision.
    # Takes precedence over `system_mac_address` and `inventory_hostname`.
    #
    # Device identification precedence:
    #   1. `serial_number` (highest priority)
    #   2. `system_mac_address`
    #   3. `inventory_hostname` (lowest priority, used only if neither of the above is set)
    serial_number: <str>

    # System MAC address of the device used to identify the device in CloudVision.
    # Should match the MAC address shown in "show version" on the device.
    # Used when `serial_number` is not set.
    #
    # Device identification precedence:
    #   1. `serial_number` (highest priority)
    #   2. `system_mac_address`
    #   3. `inventory_hostname` (lowest priority, used only if neither of the above is set)
    system_mac_address: <str>

    # List of CloudVision device tags to be assigned to this device.
    cv_device_tags:
      - name: <str; required>
        value: <str; required>

    # List of CloudVision interface tags to be assigned to interfaces on this device.
    cv_interface_tags:
      - interface: <str; required>
        tags:
          - name: <str; required>
            value: <str; required>

    # Metadata used for CV Pathfinder visualization on CloudVision.
    cv_pathfinder_metadata:
      role: <str>
      region: <str>
      zone: <str>
      site: <str>
      vtep_ip: <str>
      ssl_profile: <str>
      address: <str>
      pathfinders:
        - vtep_ip: <str; required>
      interfaces:
        - name: <str>
          carrier: <str>
          circuit_id: <str>
          pathgroup: <str>
          public_ip: <str>
      pathgroups:
        - name: <str; required>
          carriers:
            - name: <str>
          imported_carriers:
            - name: <str>
      regions:
        - id: <int>
          name: <str>
          zones:
            - id: <int>
              name: <str>
              sites:
                - id: <int>
                  name: <str>
                  location:
                    address: <str>
      vrfs:
        - name: <str>
          vni: <int>
          avts:
            - constraints:
                jitter: <int>
                latency: <int>
                lossrate: <str>
                hop_count: <str>
              description: <str>
              id: <int>
              name: <str>
              pathgroups:
                - name: <str>
                  preference: <str>
              application_profiles:
                - <str>
      internet_exit_policies:
        - name: <str; required>
          type: <str; required>
          city: <str; required>
          country: <str; required>
          upload_bandwidth: <int>
          download_bandwidth: <int>
          firewall: <bool; required>
          ips_control: <bool; required>
          acceptable_use_policy: <bool; required>
          vpn_credentials: # required
            - fqdn: <str; required>
              vpn_type: <str; required>
              pre_shared_key: <str; required>
          tunnels: # required
            - name: <str; required>
              preference: <str; required>
              endpoint: # required
                ip_address: <str; required>
                datacenter: <str; required>
                city: <str; required>
                country: <str; required>
                region: <str; required>
                latitude: <str; required>
                longitude: <str; required>
      applications:
        profiles:
          - name: <str>
            builtin_applications:
              - name: <str>
                services:
                  - <str>
            user_defined_applications:
              - name: <str>
            categories:
              - category: <str>
                services:
                  - <str>
            transport_protocols:
              - <str>
        categories:
          builtin_applications:
            - name: <str>
              category: <str>
              services:
                - <str>
          user_defined_applications:
            - name: <str>
              category: <str>
    ```
