<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>application_traffic_recognition</samp>](## "application_traffic_recognition") | Dictionary |  |  |  | PREVIEW: WAN Preview<br><br>TODO |
    | [<samp>&nbsp;&nbsp;categories</samp>](## "application_traffic_recognition.categories") | List, items: Dictionary |  |  |  | List of categories. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.categories.[].name") | String | Required, Unique |  |  | Category name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;applications</samp>](## "application_traffic_recognition.categories.[].applications") | List, items: Dictionary |  |  |  | List of applications. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.categories.[].applications.[].name") | String |  |  |  | Application name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;service</samp>](## "application_traffic_recognition.categories.[].applications.[].service") | String |  |  | Valid Values:<br>- <code>audio-video</code><br>- <code>chat</code><br>- <code>default</code><br>- <code>file-transfer</code><br>- <code>networking-protocols</code><br>- <code>peer-to-peer</code><br>- <code>software-update</code> | Service Name.<br>Specific service to target for this application.<br>If no service is specified, all supported services of the application are matched.<br>Not all valid values are valid for all applications, check on EOS CLI. |
    | [<samp>&nbsp;&nbsp;field_sets</samp>](## "application_traffic_recognition.field_sets") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l4_ports</samp>](## "application_traffic_recognition.field_sets.l4_ports") | List, items: Dictionary |  |  |  | L4 port field-set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.field_sets.l4_ports.[].name") | String | Required, Unique |  |  | L4 port field-set name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_values</samp>](## "application_traffic_recognition.field_sets.l4_ports.[].port_values") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "application_traffic_recognition.field_sets.l4_ports.[].port_values.[]") | String |  |  |  | Port values or range of port values.<br>Port values are between 0 and 65535. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefixes</samp>](## "application_traffic_recognition.field_sets.ipv4_prefixes") | List, items: Dictionary |  |  |  | IPv4 prefix field set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.field_sets.ipv4_prefixes.[].name") | String | Required, Unique |  |  | IPv4 prefix field-set name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_values</samp>](## "application_traffic_recognition.field_sets.ipv4_prefixes.[].prefix_values") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "application_traffic_recognition.field_sets.ipv4_prefixes.[].prefix_values.[]") | String |  |  |  | IP prefix (ex 1.2.3.0/24). |
    | [<samp>&nbsp;&nbsp;applications</samp>](## "application_traffic_recognition.applications") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_applications</samp>](## "application_traffic_recognition.applications.ipv4_applications") | List, items: Dictionary |  |  |  | List of user defined IPv4 applications. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].name") | String | Required, Unique |  |  | Application name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;src_prefix_set_name</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].src_prefix_set_name") | String |  |  |  | Source prefix set name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dest_prefix_set_name</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].dest_prefix_set_name") | String |  |  |  | Destination prefix set name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocols</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].protocols") | List, items: String |  |  |  | List of protocols to consider for this application.<br><br>To use port field-sets (source, destination or both), the list<br>must contain only one or two protocols, either `tcp` or `udp`.<br>When using both protocols, one line is rendered for each in the configuration,<br>hence the field-sets must have the same value for `tcp_src_port_set_name` and<br>`udp_src_port_set_name` and for `tcp_dest_port_set_name` and `udp_dest_port_set_name`<br>if set in order to generate valid configuration in EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].protocols.[]") | String |  |  | Valid Values:<br>- <code>ahp</code><br>- <code>esp</code><br>- <code>icmp</code><br>- <code>igmp</code><br>- <code>ospf</code><br>- <code>pim</code><br>- <code>rsvp</code><br>- <code>tcp</code><br>- <code>udp</code><br>- <code>vrrp</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol_ranges</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].protocol_ranges") | List, items: String |  |  |  | Acccept protocol value(s) or range(s).<br>Protocol values can be between 1 and 255. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].protocol_ranges.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_src_port_set_name</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].udp_src_port_set_name") | String |  |  |  | Name of field set for UDP source ports.<br><br>When the `protocols` list contain both `tcp` and `udp`, this key value<br>must be the same as `tcp_src_port_set_name`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tcp_src_port_set_name</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].tcp_src_port_set_name") | String |  |  |  | Name of field set for TCP source ports.<br><br>When the `protocols` list contain both `tcp` and `udp`, this key value<br>must be the same as `udp_src_port_set_name`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_dest_port_set_name</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].udp_dest_port_set_name") | String |  |  |  | Name of field set for UDP destination ports.<br><br>When the `protocols` list contain both `tcp` and `udp`, this key value<br>must be the same as `tcp_dest_port_set_name`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tcp_dest_port_set_name</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].tcp_dest_port_set_name") | String |  |  |  | Name of field set for TCP destination ports.<br><br>When the `protocols` list contain both `tcp` and `udp`, this key value<br>must be the same as `udp_dest_port_set_name`. |
    | [<samp>&nbsp;&nbsp;application_profiles</samp>](## "application_traffic_recognition.application_profiles") | List, items: Dictionary |  |  |  | Group of applications. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.application_profiles.[].name") | String |  |  |  | Application Profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;applications</samp>](## "application_traffic_recognition.application_profiles.[].applications") | List, items: Dictionary |  |  |  | List of applications part of the application profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.application_profiles.[].applications.[].name") | String |  |  |  | Application Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;service</samp>](## "application_traffic_recognition.application_profiles.[].applications.[].service") | String |  |  | Valid Values:<br>- <code>audio-video</code><br>- <code>chat</code><br>- <code>default</code><br>- <code>file-transfer</code><br>- <code>networking-protocols</code><br>- <code>peer-to-peer</code><br>- <code>software-update</code> | Service Name.<br>Specific service to target for this application.<br>If no service is specified, all supported services of the application are matched.<br>Not all valid values are valid for all applications, check on EOS CLI. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;application_transports</samp>](## "application_traffic_recognition.application_profiles.[].application_transports") | List, items: String |  |  |  | List of transport protocols. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "application_traffic_recognition.application_profiles.[].application_transports.[]") | String |  |  | Valid Values:<br>- <code>http</code><br>- <code>https</code><br>- <code>udp</code><br>- <code>tcp</code><br>- <code>ip</code><br>- <code>ip6</code><br>- <code>ssl</code><br>- <code>rtp</code><br>- <code>sctp</code><br>- <code>quic</code> | Transport name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;categories</samp>](## "application_traffic_recognition.application_profiles.[].categories") | List, items: Dictionary |  |  |  | Categories under this application profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.application_profiles.[].categories.[].name") | String |  |  |  | Name of a category. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;service</samp>](## "application_traffic_recognition.application_profiles.[].categories.[].service") | String |  |  | Valid Values:<br>- <code>audio-video</code><br>- <code>chat</code><br>- <code>default</code><br>- <code>file-transfer</code><br>- <code>networking-protocols</code><br>- <code>peer-to-peer</code><br>- <code>software-update</code> | Service Name.<br>Specific service to target for this application.<br>If no service is specified, all supported services of the application are matched.<br>Not all valid values are valid for all applications, check on EOS CLI. |
    | [<samp>virtual_topologies</samp>](## "virtual_topologies") | Dictionary |  |  |  | PREVIEW: WAN Preview<br><br>Configure AVTs for CV Pathfinder and AutoVPN. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "virtual_topologies.vrfs") | List, items: Dictionary |  |  |  | Map a VRF that exists in network_services to an AVT policy.<br>Auto create a control plane profile/policy/application and enforce it being first. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "virtual_topologies.vrfs.[].name") | String | Required, Unique |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policy</samp>](## "virtual_topologies.vrfs.[].policy") | String |  |  |  | Name of the AVT policy to apply to this VRF. |
    | [<samp>&nbsp;&nbsp;control_plane_virtual_topology</samp>](## "virtual_topologies.control_plane_virtual_topology") | Dictionary |  |  |  | Always injected into the default VRF policy as the first entry.<br>Defaults will prefer all path groups where pathfinders can be reached. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "virtual_topologies.control_plane_virtual_topology.name") | String |  |  |  | Default is `<avt_policy_name>_control_plane_default` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "virtual_topologies.control_plane_virtual_topology.id") | Integer |  |  |  | TODO min/max<br><br>ID of the control plane AVT in the default VRFs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;path_groups</samp>](## "virtual_topologies.control_plane_virtual_topology.path_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;names</samp>](## "virtual_topologies.control_plane_virtual_topology.path_groups.[].names") | List, items: String | Required |  | Min Length: 1 | List of path-group names. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "virtual_topologies.control_plane_virtual_topology.path_groups.[].names.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "virtual_topologies.control_plane_virtual_topology.path_groups.[].priority") | String | Required, Unique |  |  | Valid values are 1-255 | preferred | alternate.<br><br>preferred is converted to priority 1.<br>alternate is converted to priority 2. |
    | [<samp>&nbsp;&nbsp;policies</samp>](## "virtual_topologies.policies") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "virtual_topologies.policies.[].name") | String | Required, Unique |  |  | Name of the AVT policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;application_policies</samp>](## "virtual_topologies.policies.[].application_policies") | List, items: Dictionary |  |  |  | List of application specific policies. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;application_profile</samp>](## "virtual_topologies.policies.[].application_policies.[].application_profile") | String | Required, Unique |  |  | The application profile to use for this policy. It must be a defined `application_profile`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "virtual_topologies.policies.[].application_policies.[].name") | String |  |  |  | Optional name, if not set `<policy_name>_<application_profile>` is used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "virtual_topologies.policies.[].application_policies.[].id") | Integer |  |  |  | TODO min/max<br><br>ID of the default AVT in each VRFs. ID must be unique across all policies. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "virtual_topologies.policies.[].application_policies.[].traffic_class") | Integer |  |  | Min: 0<br>Max: 7 | Set traffic-class for matched traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "virtual_topologies.policies.[].application_policies.[].dscp") | Integer |  |  | Min: 0<br>Max: 63 | Set DSCP for matched traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path_groups</samp>](## "virtual_topologies.policies.[].application_policies.[].path_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;names</samp>](## "virtual_topologies.policies.[].application_policies.[].path_groups.[].names") | List, items: String | Required |  | Min Length: 1 | List of path-group names. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "virtual_topologies.policies.[].application_policies.[].path_groups.[].names.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "virtual_topologies.policies.[].application_policies.[].path_groups.[].priority") | String | Required, Unique |  |  | Valid values are 1-255 | preferred | alternate.<br><br>preferred is converted to priority 1.<br>alternate is converted to priority 2. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_policy</samp>](## "virtual_topologies.policies.[].default_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "virtual_topologies.policies.[].default_policy.name") | String |  |  |  | Optional name, if not set `<policy_name>_default` is used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "virtual_topologies.policies.[].default_policy.id") | Integer |  |  |  | TODO min/max<br><br>ID of the default AVT in each VRFs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path_groups</samp>](## "virtual_topologies.policies.[].default_policy.path_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;names</samp>](## "virtual_topologies.policies.[].default_policy.path_groups.[].names") | List, items: String | Required |  | Min Length: 1 | List of path-group names. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "virtual_topologies.policies.[].default_policy.path_groups.[].names.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "virtual_topologies.policies.[].default_policy.path_groups.[].priority") | String | Required, Unique |  |  | Valid values are 1-255 | preferred | alternate.<br><br>preferred is converted to priority 1.<br>alternate is converted to priority 2. |

=== "YAML"

    ```yaml
    # PREVIEW: WAN Preview

    # TODO
    application_traffic_recognition:

      # List of categories.
      categories:

          # Category name.
        - name: <str; required; unique>

          # List of applications.
          applications:

              # Application name.
            - name: <str>

              # Service Name.
              # Specific service to target for this application.
              # If no service is specified, all supported services of the application are matched.
              # Not all valid values are valid for all applications, check on EOS CLI.
              service: <str; "audio-video" | "chat" | "default" | "file-transfer" | "networking-protocols" | "peer-to-peer" | "software-update">
      field_sets:

        # L4 port field-set.
        l4_ports:

            # L4 port field-set name.
          - name: <str; required; unique>
            port_values:

                # Port values or range of port values.
                # Port values are between 0 and 65535.
              - <str>

        # IPv4 prefix field set.
        ipv4_prefixes:

            # IPv4 prefix field-set name.
          - name: <str; required; unique>
            prefix_values:

                # IP prefix (ex 1.2.3.0/24).
              - <str>
      applications:

        # List of user defined IPv4 applications.
        ipv4_applications:

            # Application name.
          - name: <str; required; unique>

            # Source prefix set name.
            src_prefix_set_name: <str>

            # Destination prefix set name.
            dest_prefix_set_name: <str>

            # List of protocols to consider for this application.

            # To use port field-sets (source, destination or both), the list
            # must contain only one or two protocols, either `tcp` or `udp`.
            # When using both protocols, one line is rendered for each in the configuration,
            # hence the field-sets must have the same value for `tcp_src_port_set_name` and
            # `udp_src_port_set_name` and for `tcp_dest_port_set_name` and `udp_dest_port_set_name`
            # if set in order to generate valid configuration in EOS.
            protocols:
              - <str; "ahp" | "esp" | "icmp" | "igmp" | "ospf" | "pim" | "rsvp" | "tcp" | "udp" | "vrrp">

            # Acccept protocol value(s) or range(s).
            # Protocol values can be between 1 and 255.
            protocol_ranges:
              - <str>

            # Name of field set for UDP source ports.

            # When the `protocols` list contain both `tcp` and `udp`, this key value
            # must be the same as `tcp_src_port_set_name`.
            udp_src_port_set_name: <str>

            # Name of field set for TCP source ports.

            # When the `protocols` list contain both `tcp` and `udp`, this key value
            # must be the same as `udp_src_port_set_name`.
            tcp_src_port_set_name: <str>

            # Name of field set for UDP destination ports.

            # When the `protocols` list contain both `tcp` and `udp`, this key value
            # must be the same as `tcp_dest_port_set_name`.
            udp_dest_port_set_name: <str>

            # Name of field set for TCP destination ports.

            # When the `protocols` list contain both `tcp` and `udp`, this key value
            # must be the same as `udp_dest_port_set_name`.
            tcp_dest_port_set_name: <str>

      # Group of applications.
      application_profiles:

          # Application Profile name.
        - name: <str>

          # List of applications part of the application profile.
          applications:

              # Application Name.
            - name: <str>

              # Service Name.
              # Specific service to target for this application.
              # If no service is specified, all supported services of the application are matched.
              # Not all valid values are valid for all applications, check on EOS CLI.
              service: <str; "audio-video" | "chat" | "default" | "file-transfer" | "networking-protocols" | "peer-to-peer" | "software-update">

          # List of transport protocols.
          application_transports:

              # Transport name.
            - <str; "http" | "https" | "udp" | "tcp" | "ip" | "ip6" | "ssl" | "rtp" | "sctp" | "quic">

          # Categories under this application profile.
          categories:

              # Name of a category.
            - name: <str>

              # Service Name.
              # Specific service to target for this application.
              # If no service is specified, all supported services of the application are matched.
              # Not all valid values are valid for all applications, check on EOS CLI.
              service: <str; "audio-video" | "chat" | "default" | "file-transfer" | "networking-protocols" | "peer-to-peer" | "software-update">

    # PREVIEW: WAN Preview

    # Configure AVTs for CV Pathfinder and AutoVPN.
    virtual_topologies:

      # Map a VRF that exists in network_services to an AVT policy.
      # Auto create a control plane profile/policy/application and enforce it being first.
      vrfs:

          # VRF name.
        - name: <str; required; unique>

          # Name of the AVT policy to apply to this VRF.
          policy: <str>

      # Always injected into the default VRF policy as the first entry.
      # Defaults will prefer all path groups where pathfinders can be reached.
      control_plane_virtual_topology:

        # Default is `<avt_policy_name>_control_plane_default`
        name: <str>

        # TODO min/max

        # ID of the control plane AVT in the default VRFs.
        id: <int>
        path_groups:

            # List of path-group names.
          - names: # >=1 items; required
              - <str>

            # Valid values are 1-255 | preferred | alternate.

            # preferred is converted to priority 1.
            # alternate is converted to priority 2.
            priority: <str; required; unique>
      policies:

          # Name of the AVT policy.
        - name: <str; required; unique>

          # List of application specific policies.
          application_policies:

              # The application profile to use for this policy. It must be a defined `application_profile`.
            - application_profile: <str; required; unique>

              # Optional name, if not set `<policy_name>_<application_profile>` is used.
              name: <str>

              # TODO min/max

              # ID of the default AVT in each VRFs. ID must be unique across all policies.
              id: <int>

              # Set traffic-class for matched traffic.
              traffic_class: <int; 0-7>

              # Set DSCP for matched traffic.
              dscp: <int; 0-63>
              path_groups:

                  # List of path-group names.
                - names: # >=1 items; required
                    - <str>

                  # Valid values are 1-255 | preferred | alternate.

                  # preferred is converted to priority 1.
                  # alternate is converted to priority 2.
                  priority: <str; required; unique>
          default_policy:

            # Optional name, if not set `<policy_name>_default` is used.
            name: <str>

            # TODO min/max

            # ID of the default AVT in each VRFs.
            id: <int>
            path_groups:

                # List of path-group names.
              - names: # >=1 items; required
                  - <str>

                # Valid values are 1-255 | preferred | alternate.

                # preferred is converted to priority 1.
                # alternate is converted to priority 2.
                priority: <str; required; unique>
    ```
