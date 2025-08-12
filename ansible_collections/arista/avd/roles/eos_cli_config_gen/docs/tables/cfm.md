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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cfm.domains.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "cfm.domains.[].level") | Integer | Required |  | Min: 1<br>Max: 7 | Maintenance domain level (0-7). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;associations</samp>](## "cfm.domains.[].associations") | List, items: Dictionary |  |  |  | List of maintenance associations. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "cfm.domains.[].associations.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 65535 | Maintenance association ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "cfm.domains.[].associations.[].direction") | String |  |  | Valid Values:<br>- <code>up</code><br>- <code>down</code> | Direction of the maintenance end point. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;end_points</samp>](## "cfm.domains.[].associations.[].end_points") | List, items: Dictionary |  |  |  | Configure the maintenance end point(MEP). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "cfm.domains.[].associations.[].end_points.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 8191 | MEP ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_end_point</samp>](## "cfm.domains.[].associations.[].end_points.[].remote_end_point") | String |  |  |  | Remote MEP ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "cfm.domains.[].associations.[].profile") | String |  |  |  | Profile name for the MEP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_end_points</samp>](## "cfm.domains.[].associations.[].remote_end_points") | List, items: Dictionary |  |  |  | Configure the remote maintenance end point(RMEP). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "cfm.domains.[].associations.[].remote_end_points.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 8191 | RMEP ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "cfm.domains.[].associations.[].remote_end_points.[].mac_address") | String |  |  |  | MAC address of the RMEP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "cfm.domains.[].associations.[].vlan") | Integer |  |  |  | VLAN ID for the MEP. |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;alarm_defects</samp>](## "cfm.profiles.[].continuity_check.alarm_defects") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rdi_ccm</samp>](## "cfm.profiles.[].continuity_check.alarm_defects.rdi_ccm") | Boolean |  |  |  | Allow continuity check messages (CCMs) with the remote defect indication (RDI) bit set to raise alarms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loc_state</samp>](## "cfm.profiles.[].continuity_check.alarm_defects.loc_state") | Boolean |  |  |  | Allow loss of connectivity (LOC) to raise alarms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;error_ccm</samp>](## "cfm.profiles.[].continuity_check.alarm_defects.error_ccm") | Boolean |  |  |  | Allow invalid continuity check messages (CCMs) to raise alarms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cross_connection</samp>](## "cfm.profiles.[].continuity_check.alarm_defects.cross_connection") | Boolean |  |  |  | Allow cross-connection defects to raise alarms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;measurement</samp>](## "cfm.profiles.[].measurement") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "cfm.profiles.[].measurement.delay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single_ended</samp>](## "cfm.profiles.[].measurement.delay.single_ended") | Boolean |  |  |  | Enable single-ended delay measurement. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_cos</samp>](## "cfm.profiles.[].measurement.delay.qos_cos") | Integer |  |  | Min: 0<br>Max: 7 | Set the class of service (CoS) value for CFM frames. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_interval</samp>](## "cfm.profiles.[].measurement.delay.tx_interval") | Integer |  |  |  | Interval in milliseconds between successive measurement frames.<br>The range is from 3.33 to 600000.00. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loss</samp>](## "cfm.profiles.[].measurement.loss") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "cfm.profiles.[].measurement.loss.enabled") | Boolean |  |  |  | Enable Ethernet OAM loss measurement. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single_ended</samp>](## "cfm.profiles.[].measurement.loss.single_ended") | Boolean |  |  |  | Enable single-ended loss measurement. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_cos</samp>](## "cfm.profiles.[].measurement.loss.qos_cos") | Integer |  |  | Min: 0<br>Max: 7 | Set the class of service (CoS) value for CFM frames. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_interval</samp>](## "cfm.profiles.[].measurement.loss.tx_interval") | Integer |  |  |  | Interval in milliseconds between successive measurement frames.<br>The range is from 3.33 to 600000.00. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;synthetic</samp>](## "cfm.profiles.[].measurement.loss.synthetic") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "cfm.profiles.[].measurement.loss.synthetic.enabled") | Boolean |  |  |  | Enable synthetic loss measurement for Ethernet OAM. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single_ended</samp>](## "cfm.profiles.[].measurement.loss.synthetic.single_ended") | Boolean |  |  |  | Enable single-ended synthetic loss measurement. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_cos</samp>](## "cfm.profiles.[].measurement.loss.synthetic.qos_cos") | String |  |  |  | Set the class of service (CoS) value or a range of values for synthetic loss measurement. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_interval</samp>](## "cfm.profiles.[].measurement.loss.synthetic.tx_interval") | Integer |  |  |  | Interval in milliseconds between successive measurement frames.<br>The range is from 3.33 to 600000.00. |

=== "YAML"

    ```yaml
    # Configure connectivity fault management (CFM).
    # CFM is a network protocol for monitoring and troubleshooting Ethernet networks.
    cfm:

      # Disable routing on interfaces where a loss of connectivity (LOC) defect is detected.
      # This prevents traffic from being routed to a faulty link.
      continuity_check_loc_state_action_disable_interface_routing: <bool>
      domains:
        - name: <str; required; unique>

          # Maintenance domain level (0-7).
          level: <int; 1-7; required>

          # List of maintenance associations.
          associations:

              # Maintenance association ID.
            - id: <int; 1-65535; required; unique>

              # Direction of the maintenance end point.
              direction: <str; "up" | "down">

              # Configure the maintenance end point(MEP).
              end_points:

                  # MEP ID.
                - id: <int; 1-8191; required; unique>

                  # Remote MEP ID.
                  remote_end_point: <str>

              # Profile name for the MEP.
              profile: <str>

              # Configure the remote maintenance end point(RMEP).
              remote_end_points:

                  # RMEP ID.
                - id: <int; 1-8191; required; unique>

                  # MAC address of the RMEP.
                  mac_address: <str>

              # VLAN ID for the MEP.
              vlan: <int>

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
            alarm_defects:

              # Allow continuity check messages (CCMs) with the remote defect indication (RDI) bit set to raise alarms.
              rdi_ccm: <bool>

              # Allow loss of connectivity (LOC) to raise alarms.
              loc_state: <bool>

              # Allow invalid continuity check messages (CCMs) to raise alarms.
              error_ccm: <bool>

              # Allow cross-connection defects to raise alarms.
              cross_connection: <bool>
          measurement:
            delay:

              # Enable single-ended delay measurement.
              single_ended: <bool>

              # Set the class of service (CoS) value for CFM frames.
              qos_cos: <int; 0-7>

              # Interval in milliseconds between successive measurement frames.
              # The range is from 3.33 to 600000.00.
              tx_interval: <int>
            loss:

              # Enable Ethernet OAM loss measurement.
              enabled: <bool>

              # Enable single-ended loss measurement.
              single_ended: <bool>

              # Set the class of service (CoS) value for CFM frames.
              qos_cos: <int; 0-7>

              # Interval in milliseconds between successive measurement frames.
              # The range is from 3.33 to 600000.00.
              tx_interval: <int>
              synthetic:

                # Enable synthetic loss measurement for Ethernet OAM.
                enabled: <bool>

                # Enable single-ended synthetic loss measurement.
                single_ended: <bool>

                # Set the class of service (CoS) value or a range of values for synthetic loss measurement.
                qos_cos: <str>

                # Interval in milliseconds between successive measurement frames.
                # The range is from 3.33 to 600000.00.
                tx_interval: <int>
    ```
