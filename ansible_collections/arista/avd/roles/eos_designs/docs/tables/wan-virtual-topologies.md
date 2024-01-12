<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>wan_virtual_topologies</samp>](## "wan_virtual_topologies") | Dictionary |  |  |  | PREVIEW: WAN Preview<br><br>Configure Virtual Topologies for CV Pathfinder and AutoVPN.<br><br>Auto create a control plane profile/policy/application and enforce it being first in the default VRF. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "wan_virtual_topologies.vrfs") | List, items: Dictionary |  |  |  | Map a VRF that exists in network_services to an AVT policy.<br>TODO: missing default VRF behavior |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "wan_virtual_topologies.vrfs.[].name") | String | Required, Unique |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policy</samp>](## "wan_virtual_topologies.vrfs.[].policy") | String |  |  |  | Name of the AVT policy to apply to this VRF. |
    | [<samp>&nbsp;&nbsp;control_plane_virtual_topology</samp>](## "wan_virtual_topologies.control_plane_virtual_topology") | Dictionary |  |  |  | Always injected into the default VRF policy as the first entry.<br><br>By default, if no path-groups are specified, all locally available path-groups<br>are used in the generated load-balance policy.<br>ID is hardcoded to 254 for the AVT profile in CV Pathfinder mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.name") | String |  |  |  | Optional name, if not set `CONTROL-PLANE-PROFILE` is used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.traffic_class") | Integer |  |  | Min: 0<br>Max: 7 | Set traffic-class for matched traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.dscp") | Integer |  |  | Min: 0<br>Max: 63 | Set DSCP for matched traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;path_groups</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.path_groups") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;names</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.path_groups.[].names") | List, items: String | Required |  | Min Length: 1 | List of path-group names. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.path_groups.[].names.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preference</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.path_groups.[].preference") | String | Required, Unique |  |  | Valid values are 1-255 | preferred | alternate.<br><br>preferred is converted to priority 1.<br>alternate is converted to priority 2. |
    | [<samp>&nbsp;&nbsp;policies</samp>](## "wan_virtual_topologies.policies") | List, items: Dictionary |  |  |  | List of virtual toplogies policies.<br><br>For AutoVPN, each item in the list creates:<br>  * one policy with:<br>      * one `match` entry per `application_virtual_topologies` item<br>        they are indexed using `10 * <list_index>` where `list_index` starts at `1`.<br>      * one `default-match`<br>  * one load-balance policy per `application_virtual_topologies` and one for the `default_virtual_topology`.<br>  * if the policy is associated with the default VRF, a special control-plane rule is injected<br>    in the policy with index `1` referring to a control-plane load-balance policy as defined under<br>    `control_plane_virtual_topology`.<br><br><br>For CV Pathfinder, each item in the list creates:<br>  * one policy with:<br>      * one `match` entry per `application_virtual_topologies` item ordered as in the model.<br>      * one last match entry for the `default` application-profile using `default_virtual_topology` information.<br>  * one profile per `application_virtual_topologies` item.<br>  * one profile for the `default_virtual_topology`..<br>  * one load-balance policy per `application_virtual_topologies`.<br>  * one load_balance policy for the `default_virtual_topology`.<br>  * if the policy is associated with the default VRF, a special control-plane profile is configured<br>    and injected first in the policy assigned to the `default` VRF. This profile points to a<br>    control-plane load-balance policy as defined under `control_plane_virtual_topology`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "wan_virtual_topologies.policies.[].name") | String | Required, Unique |  |  | Name of the AVT policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;application_virtual_topologies</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies") | List, items: Dictionary |  |  |  | List of application specific virtual topologies. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;application_profile</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].application_profile") | String | Required, Unique |  |  | The application profile to use for this virtual topology. It must be a defined `application_profile`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].name") | String |  |  |  | Optional name, if not set `<policy_name>_<application_profile>` is used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].id") | Integer | Required |  | Min: 2<br>Max: 253 | ID of the AVT in each VRFs. ID must be unique across all virtual topologies in a policy.<br>ID 1 is reserved for the default_virtual_toplogy.<br>ID 254 is reserved for the control_plane_virtual_topology. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].traffic_class") | Integer |  |  | Min: 0<br>Max: 7 | Set traffic-class for matched traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].dscp") | Integer |  |  | Min: 0<br>Max: 63 | Set DSCP for matched traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path_groups</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].path_groups") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;names</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].path_groups.[].names") | List, items: String | Required |  | Min Length: 1 | List of path-group names. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].path_groups.[].names.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preference</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].path_groups.[].preference") | String | Required, Unique |  |  | Valid values are 1-255 | preferred | alternate.<br><br>preferred is converted to priority 1.<br>alternate is converted to priority 2. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_virtual_topology</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology") | Dictionary | Required |  |  | Default match for the policy.<br>If defined, ID is hardcoded to 1 for the AVT profile in CV Pathfinder mode.<br>If no default match should be configured, set `drop_unmatched` to `true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.name") | String |  |  |  | Optional name, if not set `<policy_name>_default` is used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop_unmatched</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.drop_unmatched") | Boolean |  | `False` |  | When set, no `catch-all` match is configured for the policy and unmatched traffic is dropped. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.traffic_class") | Integer |  |  | Min: 0<br>Max: 7 | Set traffic-class for matched traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.dscp") | Integer |  |  | Min: 0<br>Max: 63 | Set DSCP for matched traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path_groups</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.path_groups") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;names</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.path_groups.[].names") | List, items: String | Required |  | Min Length: 1 | List of path-group names. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.path_groups.[].names.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preference</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.path_groups.[].preference") | String | Required, Unique |  |  | Valid values are 1-255 | preferred | alternate.<br><br>preferred is converted to priority 1.<br>alternate is converted to priority 2. |

=== "YAML"

    ```yaml
    # PREVIEW: WAN Preview

    # Configure Virtual Topologies for CV Pathfinder and AutoVPN.

    # Auto create a control plane profile/policy/application and enforce it being first in the default VRF.
    wan_virtual_topologies:

      # Map a VRF that exists in network_services to an AVT policy.
      # TODO: missing default VRF behavior
      vrfs:

          # VRF name.
        - name: <str; required; unique>

          # Name of the AVT policy to apply to this VRF.
          policy: <str>

      # Always injected into the default VRF policy as the first entry.

      # By default, if no path-groups are specified, all locally available path-groups
      # are used in the generated load-balance policy.
      # ID is hardcoded to 254 for the AVT profile in CV Pathfinder mode.
      control_plane_virtual_topology:

        # Optional name, if not set `CONTROL-PLANE-PROFILE` is used.
        name: <str>

        # Set traffic-class for matched traffic.
        traffic_class: <int; 0-7>

        # Set DSCP for matched traffic.
        dscp: <int; 0-63>
        path_groups: # >=1 items

            # List of path-group names.
          - names: # >=1 items; required
              - <str>

            # Valid values are 1-255 | preferred | alternate.

            # preferred is converted to priority 1.
            # alternate is converted to priority 2.
            preference: <str; required; unique>

      # List of virtual toplogies policies.

      # For AutoVPN, each item in the list creates:
      #   * one policy with:
      #       * one `match` entry per `application_virtual_topologies` item
      #         they are indexed using `10 * <list_index>` where `list_index` starts at `1`.
      #       * one `default-match`
      #   * one load-balance policy per `application_virtual_topologies` and one for the `default_virtual_topology`.
      #   * if the policy is associated with the default VRF, a special control-plane rule is injected
      #     in the policy with index `1` referring to a control-plane load-balance policy as defined under
      #     `control_plane_virtual_topology`.


      # For CV Pathfinder, each item in the list creates:
      #   * one policy with:
      #       * one `match` entry per `application_virtual_topologies` item ordered as in the model.
      #       * one last match entry for the `default` application-profile using `default_virtual_topology` information.
      #   * one profile per `application_virtual_topologies` item.
      #   * one profile for the `default_virtual_topology`..
      #   * one load-balance policy per `application_virtual_topologies`.
      #   * one load_balance policy for the `default_virtual_topology`.
      #   * if the policy is associated with the default VRF, a special control-plane profile is configured
      #     and injected first in the policy assigned to the `default` VRF. This profile points to a
      #     control-plane load-balance policy as defined under `control_plane_virtual_topology`.
      policies:

          # Name of the AVT policy.
        - name: <str; required; unique>

          # List of application specific virtual topologies.
          application_virtual_topologies:

              # The application profile to use for this virtual topology. It must be a defined `application_profile`.
            - application_profile: <str; required; unique>

              # Optional name, if not set `<policy_name>_<application_profile>` is used.
              name: <str>

              # ID of the AVT in each VRFs. ID must be unique across all virtual topologies in a policy.
              # ID 1 is reserved for the default_virtual_toplogy.
              # ID 254 is reserved for the control_plane_virtual_topology.
              id: <int; 2-253; required>

              # Set traffic-class for matched traffic.
              traffic_class: <int; 0-7>

              # Set DSCP for matched traffic.
              dscp: <int; 0-63>
              path_groups: # >=1 items

                  # List of path-group names.
                - names: # >=1 items; required
                    - <str>

                  # Valid values are 1-255 | preferred | alternate.

                  # preferred is converted to priority 1.
                  # alternate is converted to priority 2.
                  preference: <str; required; unique>

          # Default match for the policy.
          # If defined, ID is hardcoded to 1 for the AVT profile in CV Pathfinder mode.
          # If no default match should be configured, set `drop_unmatched` to `true`.
          default_virtual_topology: # required

            # Optional name, if not set `<policy_name>_default` is used.
            name: <str>

            # When set, no `catch-all` match is configured for the policy and unmatched traffic is dropped.
            drop_unmatched: <bool; default=False>

            # Set traffic-class for matched traffic.
            traffic_class: <int; 0-7>

            # Set DSCP for matched traffic.
            dscp: <int; 0-63>
            path_groups: # >=1 items

                # List of path-group names.
              - names: # >=1 items; required
                  - <str>

                # Valid values are 1-255 | preferred | alternate.

                # preferred is converted to priority 1.
                # alternate is converted to priority 2.
                preference: <str; required; unique>
    ```
