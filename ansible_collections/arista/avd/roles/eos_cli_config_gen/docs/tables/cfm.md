<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cfm</samp>](## "cfm") | Dictionary |  |  |  | Configure connectivity fault management (CFM).<br>CFM is a network protocol for monitoring and troubleshooting Ethernet networks. |
    | [<samp>&nbsp;&nbsp;continuity_check_loc_state_action_disable_interface_routing</samp>](## "cfm.continuity_check_loc_state_action_disable_interface_routing") | Boolean |  |  |  | Disable routing on interfaces where a loss of connectivity (LOC) defect is detected.<br>This prevents traffic from being routed to a faulty link. |
    | [<samp>&nbsp;&nbsp;domains</samp>](## "cfm.domains") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cfm.domains.[].name") | String | Required, Unique |  |  | CFM domain name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "cfm.domains.[].level") | Integer | Required |  | Min: 0<br>Max: 7 | Maintenance domain level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;associations</samp>](## "cfm.domains.[].associations") | List, items: Dictionary |  |  |  | List of maintenance associations. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "cfm.domains.[].associations.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 65535 | Maintenance association ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "cfm.domains.[].associations.[].direction") | String |  |  | Valid Values:<br>- <code>up</code><br>- <code>down</code> | Local maintenance endpoint direction. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;end_points</samp>](## "cfm.domains.[].associations.[].end_points") | List, items: Dictionary |  |  |  | Configure the maintenance endpoint(MEP). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "cfm.domains.[].associations.[].end_points.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 8191 | Local maintenance endpoint ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_end_point</samp>](## "cfm.domains.[].associations.[].end_points.[].remote_end_point") | String |  |  |  | Remote maintenance endpoint ID(s) or range(s) of remote maintenance endpoint ID(s).<br>The range is from 1 to 8191. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "cfm.domains.[].associations.[].end_points.[].interface") | String |  |  |  | Specifies the interface on which to configure the local maintenance endpoint.<br>Supported types include Ethernet sub-interfaces, InternalRecirc, and Port-Channel link aggregation groups (LAGs). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "cfm.domains.[].associations.[].profile") | String |  |  |  | Apply connectivity fault management profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_end_points</samp>](## "cfm.domains.[].associations.[].remote_end_points") | List, items: Dictionary |  |  |  | Configure the remote maintenance endpoint(RMEP). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "cfm.domains.[].associations.[].remote_end_points.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 8191 | Configure remote maintenance endpoint ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "cfm.domains.[].associations.[].remote_end_points.[].mac_address") | String |  |  |  | MAC address of the RMEP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "cfm.domains.[].associations.[].vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Set VLAN in the maintenance association. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intermediate_point</samp>](## "cfm.domains.[].intermediate_point") | Boolean |  |  |  | Configure the device as a maintenance intermediate point. |
    | [<samp>&nbsp;&nbsp;measurement_loss</samp>](## "cfm.measurement_loss") | Dictionary |  |  |  | Configure Ethernet OAM loss measurement functions. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband</samp>](## "cfm.measurement_loss.inband") | Boolean |  |  |  | Enable hardware-assisted support for OAM loss measurement. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;synthetic</samp>](## "cfm.measurement_loss.synthetic") | Boolean |  |  |  | Enable hardware-assisted support for OAM synthetic loss measurement. |
    | [<samp>&nbsp;&nbsp;profiles</samp>](## "cfm.profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cfm.profiles.[].name") | String | Required, Unique |  |  | CFM profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;alarm_indication</samp>](## "cfm.profiles.[].alarm_indication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "cfm.profiles.[].alarm_indication.enabled") | Boolean |  |  |  | Enable sending of alarm indication signal (AIS) packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client_domain_level</samp>](## "cfm.profiles.[].alarm_indication.client_domain_level") | Integer |  |  | Min: 0<br>Max: 7 | Client maintenance domain level for which to send AIS packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_interval</samp>](## "cfm.profiles.[].alarm_indication.tx_interval") | String |  |  | Valid Values:<br>- <code>1 seconds</code><br>- <code>1 minutes</code> | Transmission interval for AIS packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continuity_check</samp>](## "cfm.profiles.[].continuity_check") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "cfm.profiles.[].continuity_check.enabled") | Boolean |  |  |  | Enable the continuity check protocol to monitor connectivity. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_cos</samp>](## "cfm.profiles.[].continuity_check.qos_cos") | Integer |  |  | Min: 0<br>Max: 7 | Set the class of service (CoS) value for CFM frames. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_interval</samp>](## "cfm.profiles.[].continuity_check.tx_interval") | String |  |  | Valid Values:<br>- <code>3.33 milliseconds</code><br>- <code>10 milliseconds</code><br>- <code>100 milliseconds</code><br>- <code>1 seconds</code><br>- <code>10 seconds</code><br>- <code>1 minutes</code><br>- <code>10 minutes</code> | Set the transmission interval for continuity check messages (CCMs). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;alarm_defects</samp>](## "cfm.profiles.[].continuity_check.alarm_defects") | List, items: String |  |  | Min Length: 1 | Defines alarm indication signal protocol parameters. Supported options:<br>- rdi-ccm: Raise alarms on continuity check messages (CCMs) with the remote defect indication (RDI) bit set.<br>- loc-state: Raise alarms on loss of connectivity (LOC).<br>- error-ccm: Raise alarms on invalid continuity check messages (CCMs).<br>- cross-connection: Raise alarms on cross-connection defects. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "cfm.profiles.[].continuity_check.alarm_defects.[]") | String |  |  | Valid Values:<br>- <code>rdi-ccm</code><br>- <code>loc-state</code><br>- <code>error-ccm</code><br>- <code>cross-connection</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;measurement</samp>](## "cfm.profiles.[].measurement") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "cfm.profiles.[].measurement.delay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single_ended</samp>](## "cfm.profiles.[].measurement.delay.single_ended") | Boolean |  |  |  | Enable single-ended delay measurement. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_cos</samp>](## "cfm.profiles.[].measurement.delay.qos_cos") | Integer |  |  | Min: 0<br>Max: 7 | Set the class of service (CoS) value for CFM frames. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_interval</samp>](## "cfm.profiles.[].measurement.delay.tx_interval") | String |  |  |  | Interval in milliseconds between successive measurement frames.<br>The range is from 3.33 to 600000. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loss</samp>](## "cfm.profiles.[].measurement.loss") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single_ended</samp>](## "cfm.profiles.[].measurement.loss.single_ended") | Boolean |  |  |  | Enable single-ended loss measurement. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_cos</samp>](## "cfm.profiles.[].measurement.loss.qos_cos") | Integer |  |  | Min: 0<br>Max: 7 | Set the class of service (CoS) value for CFM frames. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_interval</samp>](## "cfm.profiles.[].measurement.loss.tx_interval") | String |  |  |  | Interval in milliseconds between successive measurement frames.<br>The range is from 3.33 to 600000. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;synthetic</samp>](## "cfm.profiles.[].measurement.loss.synthetic") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single_ended</samp>](## "cfm.profiles.[].measurement.loss.synthetic.single_ended") | Boolean |  |  |  | Enable single-ended synthetic loss measurement. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_cos</samp>](## "cfm.profiles.[].measurement.loss.synthetic.qos_cos") | String |  |  |  | Set the class of service (CoS) value or a range of values (0-7) for synthetic loss measurement. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_interval</samp>](## "cfm.profiles.[].measurement.loss.synthetic.tx_interval") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "cfm.profiles.[].measurement.loss.synthetic.tx_interval.interval") | String | Required |  |  | Interval in milliseconds between successive measurement frames.<br>The range is from 3.33 to 600000. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;period_frames</samp>](## "cfm.profiles.[].measurement.loss.synthetic.tx_interval.period_frames") | Integer |  |  | Min: 1<br>Max: 65535 | Synthetic loss measurement transmission frames. |

=== "YAML"

    ```yaml
    # Configure connectivity fault management (CFM).
    # CFM is a network protocol for monitoring and troubleshooting Ethernet networks.
    cfm:

      # Disable routing on interfaces where a loss of connectivity (LOC) defect is detected.
      # This prevents traffic from being routed to a faulty link.
      continuity_check_loc_state_action_disable_interface_routing: <bool>
      domains:

          # CFM domain name.
        - name: <str; required; unique>

          # Maintenance domain level.
          level: <int; 0-7; required>

          # List of maintenance associations.
          associations:

              # Maintenance association ID.
            - id: <int; 1-65535; required; unique>

              # Local maintenance endpoint direction.
              direction: <str; "up" | "down">

              # Configure the maintenance endpoint(MEP).
              end_points:

                  # Local maintenance endpoint ID.
                - id: <int; 1-8191; required; unique>

                  # Remote maintenance endpoint ID(s) or range(s) of remote maintenance endpoint ID(s).
                  # The range is from 1 to 8191.
                  remote_end_point: <str>

                  # Specifies the interface on which to configure the local maintenance endpoint.
                  # Supported types include Ethernet sub-interfaces, InternalRecirc, and Port-Channel link aggregation groups (LAGs).
                  interface: <str>

              # Apply connectivity fault management profile.
              profile: <str>

              # Configure the remote maintenance endpoint(RMEP).
              remote_end_points:

                  # Configure remote maintenance endpoint ID.
                - id: <int; 1-8191; required; unique>

                  # MAC address of the RMEP.
                  mac_address: <str>

              # Set VLAN in the maintenance association.
              vlan: <int; 1-4094>

          # Configure the device as a maintenance intermediate point.
          intermediate_point: <bool>

      # Configure Ethernet OAM loss measurement functions.
      measurement_loss:

        # Enable hardware-assisted support for OAM loss measurement.
        inband: <bool>

        # Enable hardware-assisted support for OAM synthetic loss measurement.
        synthetic: <bool>
      profiles:

          # CFM profile name.
        - name: <str; required; unique>
          alarm_indication:

            # Enable sending of alarm indication signal (AIS) packets.
            enabled: <bool>

            # Client maintenance domain level for which to send AIS packets.
            client_domain_level: <int; 0-7>

            # Transmission interval for AIS packets.
            tx_interval: <str; "1 seconds" | "1 minutes">
          continuity_check:

            # Enable the continuity check protocol to monitor connectivity.
            enabled: <bool>

            # Set the class of service (CoS) value for CFM frames.
            qos_cos: <int; 0-7>

            # Set the transmission interval for continuity check messages (CCMs).
            tx_interval: <str; "3.33 milliseconds" | "10 milliseconds" | "100 milliseconds" | "1 seconds" | "10 seconds" | "1 minutes" | "10 minutes">

            # Defines alarm indication signal protocol parameters. Supported options:
            # - rdi-ccm: Raise alarms on continuity check messages (CCMs) with the remote defect indication (RDI) bit set.
            # - loc-state: Raise alarms on loss of connectivity (LOC).
            # - error-ccm: Raise alarms on invalid continuity check messages (CCMs).
            # - cross-connection: Raise alarms on cross-connection defects.
            alarm_defects: # >=1 items
              - <str; "rdi-ccm" | "loc-state" | "error-ccm" | "cross-connection">
          measurement:
            delay:

              # Enable single-ended delay measurement.
              single_ended: <bool>

              # Set the class of service (CoS) value for CFM frames.
              qos_cos: <int; 0-7>

              # Interval in milliseconds between successive measurement frames.
              # The range is from 3.33 to 600000.
              tx_interval: <str>
            loss:

              # Enable single-ended loss measurement.
              single_ended: <bool>

              # Set the class of service (CoS) value for CFM frames.
              qos_cos: <int; 0-7>

              # Interval in milliseconds between successive measurement frames.
              # The range is from 3.33 to 600000.
              tx_interval: <str>
              synthetic:

                # Enable single-ended synthetic loss measurement.
                single_ended: <bool>

                # Set the class of service (CoS) value or a range of values (0-7) for synthetic loss measurement.
                qos_cos: <str>
                tx_interval:

                  # Interval in milliseconds between successive measurement frames.
                  # The range is from 3.33 to 600000.
                  interval: <str; required>

                  # Synthetic loss measurement transmission frames.
                  period_frames: <int; 1-65535>
    ```
