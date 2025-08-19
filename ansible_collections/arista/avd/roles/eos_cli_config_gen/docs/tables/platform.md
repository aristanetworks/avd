<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>platform</samp>](## "platform") | Dictionary |  |  |  | Every key below this point is platform dependent. |
    | [<samp>&nbsp;&nbsp;trident</samp>](## "platform.trident") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;forwarding_table_partition</samp>](## "platform.trident.forwarding_table_partition") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l3</samp>](## "platform.trident.l3") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routing_mac_address_per_vlan</samp>](## "platform.trident.l3.routing_mac_address_per_vlan") | Boolean |  |  |  | Enable bridging of packets with destination MAC being a Router MAC in VLANs without routing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mmu</samp>](## "platform.trident.mmu") | Dictionary |  |  |  | Memory Management Unit settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;active_profile</samp>](## "platform.trident.mmu.active_profile") | String |  |  |  | The queue profile to be applied to the platform.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;headroom_pool</samp>](## "platform.trident.mmu.headroom_pool") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "platform.trident.mmu.headroom_pool.unit") | String |  |  | Valid Values:<br>- <code>bytes</code><br>- <code>cells</code> | Unit to be used for the `headroom_pool` value.<br>If not specified, default is bytes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "platform.trident.mmu.headroom_pool.limit") | Integer |  |  |  | Max limit on headroom pool size. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;queue_profiles</samp>](## "platform.trident.mmu.queue_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "platform.trident.mmu.queue_profiles.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ingress</samp>](## "platform.trident.mmu.queue_profiles.[].ingress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority_groups</samp>](## "platform.trident.mmu.queue_profiles.[].ingress.priority_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "platform.trident.mmu.queue_profiles.[].ingress.priority_groups.[].id") | Integer | Required, Unique |  | Min: 0<br>Max: 7 | Priority-group group number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "platform.trident.mmu.queue_profiles.[].ingress.priority_groups.[].threshold") | String |  |  | Valid Values:<br>- <code>1</code><br>- <code>1/128</code><br>- <code>1/16</code><br>- <code>1/2</code><br>- <code>1/32</code><br>- <code>1/4</code><br>- <code>1/64</code><br>- <code>1/8</code><br>- <code>2</code><br>- <code>4</code><br>- <code>8</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reserved</samp>](## "platform.trident.mmu.queue_profiles.[].ingress.priority_groups.[].reserved") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "platform.trident.mmu.queue_profiles.[].ingress.priority_groups.[].reserved.unit") | String |  |  | Valid Values:<br>- <code>bytes</code><br>- <code>cells</code> | Unit to be used for the `priority_groups` `reserved` value.<br>If not specified, default is bytes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;memory</samp>](## "platform.trident.mmu.queue_profiles.[].ingress.priority_groups.[].reserved.memory") | Integer |  |  |  | Specify the amount of memory that should be reserved. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "platform.trident.mmu.queue_profiles.[].ingress.threshold") | String |  |  | Valid Values:<br>- <code>1</code><br>- <code>1/128</code><br>- <code>1/16</code><br>- <code>1/2</code><br>- <code>1/32</code><br>- <code>1/4</code><br>- <code>1/64</code><br>- <code>1/8</code><br>- <code>2</code><br>- <code>4</code><br>- <code>8</code> | Specify the dynamic shared memory threshold. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reserved</samp>](## "platform.trident.mmu.queue_profiles.[].ingress.reserved") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "platform.trident.mmu.queue_profiles.[].ingress.reserved.unit") | String |  |  | Valid Values:<br>- <code>bytes</code><br>- <code>cells</code> | Unit to be used for the `reserved` value.<br>If not specified, default is bytes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;memory</samp>](## "platform.trident.mmu.queue_profiles.[].ingress.reserved.memory") | Integer |  |  |  | Specify the amount of memory that should be reserved. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;headroom</samp>](## "platform.trident.mmu.queue_profiles.[].ingress.headroom") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "platform.trident.mmu.queue_profiles.[].ingress.headroom.unit") | String |  |  | Valid Values:<br>- <code>bytes</code><br>- <code>cells</code> | Unit to be used for the headroom value.<br>If not specified, default is bytes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;memory</samp>](## "platform.trident.mmu.queue_profiles.[].ingress.headroom.memory") | Integer |  |  |  | Specify the amount of memory that should be reserved. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;resume</samp>](## "platform.trident.mmu.queue_profiles.[].ingress.resume") | Integer |  |  |  | Amount of memory that should be reserved (in bytes) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast_queues</samp>](## "platform.trident.mmu.queue_profiles.[].multicast_queues") | List, items: Dictionary |  |  |  | Egress multicast queues. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "platform.trident.mmu.queue_profiles.[].multicast_queues.[].id") | Integer | Required, Unique |  | Min: 0<br>Max: 7 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "platform.trident.mmu.queue_profiles.[].multicast_queues.[].unit") | String |  |  | Valid Values:<br>- <code>bytes</code><br>- <code>cells</code> | Unit to be used for the reservation value. If not specified, default is bytes.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reserved</samp>](## "platform.trident.mmu.queue_profiles.[].multicast_queues.[].reserved") | Integer |  |  |  | Amount of memory that should be reserved for this<br>queue.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "platform.trident.mmu.queue_profiles.[].multicast_queues.[].threshold") | String |  |  | Valid Values:<br>- <code>1</code><br>- <code>1/128</code><br>- <code>1/16</code><br>- <code>1/2</code><br>- <code>1/32</code><br>- <code>1/4</code><br>- <code>1/64</code><br>- <code>1/8</code><br>- <code>2</code><br>- <code>4</code><br>- <code>8</code> | Dynamic Shared Memory threshold.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "platform.trident.mmu.queue_profiles.[].multicast_queues.[].drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;precedence</samp>](## "platform.trident.mmu.queue_profiles.[].multicast_queues.[].drop.precedence") | Integer | Required |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "platform.trident.mmu.queue_profiles.[].multicast_queues.[].drop.threshold") | String | Required |  |  | Drop Threshold. This value may also be fractions.<br>Example: 7/8 or 3/4 or 1/2<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unicast_queues</samp>](## "platform.trident.mmu.queue_profiles.[].unicast_queues") | List, items: Dictionary |  |  |  | Egress unicast queues. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "platform.trident.mmu.queue_profiles.[].unicast_queues.[].id") | Integer | Required, Unique |  | Min: 0<br>Max: 7 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "platform.trident.mmu.queue_profiles.[].unicast_queues.[].unit") | String |  |  | Valid Values:<br>- <code>bytes</code><br>- <code>cells</code> | Unit to be used for the reservation value. If not specified, default is bytes.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reserved</samp>](## "platform.trident.mmu.queue_profiles.[].unicast_queues.[].reserved") | Integer |  |  |  | Amount of memory that should be reserved for this<br>queue.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "platform.trident.mmu.queue_profiles.[].unicast_queues.[].threshold") | String |  |  | Valid Values:<br>- <code>1</code><br>- <code>1/128</code><br>- <code>1/16</code><br>- <code>1/2</code><br>- <code>1/32</code><br>- <code>1/4</code><br>- <code>1/64</code><br>- <code>1/8</code><br>- <code>2</code><br>- <code>4</code><br>- <code>8</code> | Dynamic Shared Memory threshold.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "platform.trident.mmu.queue_profiles.[].unicast_queues.[].drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;precedence</samp>](## "platform.trident.mmu.queue_profiles.[].unicast_queues.[].drop.precedence") | Integer | Required |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "platform.trident.mmu.queue_profiles.[].unicast_queues.[].drop.threshold") | String | Required |  |  | Drop Threshold. This value may also be fractions.<br>Example: 7/8 or 3/4 or 1/2<br> |
    | [<samp>&nbsp;&nbsp;sand</samp>](## "platform.sand") | Dictionary |  |  |  | Most of the platform sand options are hardware dependent and optional. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;qos_maps</samp>](## "platform.sand.qos_maps") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;traffic_class</samp>](## "platform.sand.qos_maps.[].traffic_class") | Integer |  |  | Min: 0<br>Max: 7 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to_network_qos</samp>](## "platform.sand.qos_maps.[].to_network_qos") | Integer |  |  | Min: 0<br>Max: 63 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lag</samp>](## "platform.sand.lag") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_only</samp>](## "platform.sand.lag.hardware_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "platform.sand.lag.mode") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;forwarding_mode</samp>](## "platform.sand.forwarding_mode") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;multicast_replication</samp>](## "platform.sand.multicast_replication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "platform.sand.multicast_replication.default") | String |  |  | Valid Values:<br>- <code>ingress</code><br>- <code>egress</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mdb_profile</samp>](## "platform.sand.mdb_profile") | String |  |  | Valid Values:<br>- <code>balanced</code><br>- <code>balanced-xl</code><br>- <code>l3</code><br>- <code>l3-xl</code><br>- <code>l3-xxl</code><br>- <code>l3-xxxl</code> | Sand platforms MDB Profile configuration. Note: l3-xxxl does not support MLAG. |
    | [<samp>&nbsp;&nbsp;sfe</samp>](## "platform.sfe") | Dictionary |  |  |  | Sfe (Software Forwarding Engine) settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;data_plane_cpu_allocation_max</samp>](## "platform.sfe.data_plane_cpu_allocation_max") | Integer |  |  | Min: 1<br>Max: 128 | Maximum number of CPUs used for data plane traffic forwarding. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "platform.sfe.interface") | Dictionary |  |  |  | Configure interface related settings for Sfe platform. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profiles</samp>](## "platform.sfe.interface.profiles") | List, items: Dictionary |  |  |  | Configure one or more Receive Side Scaling (RSS) interface profiles.<br>This is supported on specific platforms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "platform.sfe.interface.profiles.[].name") | String | Required, Unique |  |  | RSS interface profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "platform.sfe.interface.profiles.[].interfaces") | List, items: Dictionary |  |  |  | Interfaces within RSS profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "platform.sfe.interface.profiles.[].interfaces.[].name") | String | Required, Unique |  |  | Interface name such as 'Ethernet2'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rx_queue</samp>](## "platform.sfe.interface.profiles.[].interfaces.[].rx_queue") | Dictionary |  |  |  | Receive queue parameters for the selected interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "platform.sfe.interface.profiles.[].interfaces.[].rx_queue.count") | Integer |  |  | Min: 1 | Number of receive queues.<br>The maximum value is platform dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;worker</samp>](## "platform.sfe.interface.profiles.[].interfaces.[].rx_queue.worker") | String |  |  |  | Worker ids specified as combination of range and/or comma separated values<br>such as 0-4,7. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "platform.sfe.interface.profiles.[].interfaces.[].rx_queue.mode") | String |  |  | Valid Values:<br>- <code>shared</code><br>- <code>exclusive</code> | Mode applicable to the workers. Default mode is 'shared'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface_profile</samp>](## "platform.sfe.interface.interface_profile") | String |  |  |  | RSS interface profile name to apply for the platform.<br>Needs system reload or Sfe agent restart for change to take effect. |
    | [<samp>&nbsp;&nbsp;fap</samp>](## "platform.fap") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;buffering_egress</samp>](## "platform.fap.buffering_egress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "platform.fap.buffering_egress.profile") | String |  |  | Valid Values:<br>- <code>unicast</code><br>- <code>balanced</code> | Preferred traffic profile for egress fap buffering. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;voq</samp>](## "platform.fap.voq") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;credit_rates_unified</samp>](## "platform.fap.voq.credit_rates_unified") | Boolean |  |  |  | Set Unified credit rates for all port speeds. |

=== "YAML"

    ```yaml
    # Every key below this point is platform dependent.
    platform:
      trident:
        forwarding_table_partition: <str>
        l3:

          # Enable bridging of packets with destination MAC being a Router MAC in VLANs without routing.
          routing_mac_address_per_vlan: <bool>

        # Memory Management Unit settings.
        mmu:

          # The queue profile to be applied to the platform.
          active_profile: <str>
          headroom_pool:

            # Unit to be used for the `headroom_pool` value.
            # If not specified, default is bytes.
            unit: <str; "bytes" | "cells">

            # Max limit on headroom pool size.
            limit: <int>
          queue_profiles:
            - name: <str; required; unique>
              ingress:
                priority_groups:

                    # Priority-group group number.
                  - id: <int; 0-7; required; unique>
                    threshold: <str; "1" | "1/128" | "1/16" | "1/2" | "1/32" | "1/4" | "1/64" | "1/8" | "2" | "4" | "8">
                    reserved:

                      # Unit to be used for the `priority_groups` `reserved` value.
                      # If not specified, default is bytes.
                      unit: <str; "bytes" | "cells">

                      # Specify the amount of memory that should be reserved.
                      memory: <int>

                # Specify the dynamic shared memory threshold.
                threshold: <str; "1" | "1/128" | "1/16" | "1/2" | "1/32" | "1/4" | "1/64" | "1/8" | "2" | "4" | "8">
                reserved:

                  # Unit to be used for the `reserved` value.
                  # If not specified, default is bytes.
                  unit: <str; "bytes" | "cells">

                  # Specify the amount of memory that should be reserved.
                  memory: <int>
                headroom:

                  # Unit to be used for the headroom value.
                  # If not specified, default is bytes.
                  unit: <str; "bytes" | "cells">

                  # Specify the amount of memory that should be reserved.
                  memory: <int>

                # Amount of memory that should be reserved (in bytes)
                resume: <int>

              # Egress multicast queues.
              multicast_queues:
                - id: <int; 0-7; required; unique>

                  # Unit to be used for the reservation value. If not specified, default is bytes.
                  unit: <str; "bytes" | "cells">

                  # Amount of memory that should be reserved for this
                  # queue.
                  reserved: <int>

                  # Dynamic Shared Memory threshold.
                  threshold: <str; "1" | "1/128" | "1/16" | "1/2" | "1/32" | "1/4" | "1/64" | "1/8" | "2" | "4" | "8">
                  drop:
                    precedence: <int; 1 | 2; required>

                    # Drop Threshold. This value may also be fractions.
                    # Example: 7/8 or 3/4 or 1/2
                    threshold: <str; required>

              # Egress unicast queues.
              unicast_queues:
                - id: <int; 0-7; required; unique>

                  # Unit to be used for the reservation value. If not specified, default is bytes.
                  unit: <str; "bytes" | "cells">

                  # Amount of memory that should be reserved for this
                  # queue.
                  reserved: <int>

                  # Dynamic Shared Memory threshold.
                  threshold: <str; "1" | "1/128" | "1/16" | "1/2" | "1/32" | "1/4" | "1/64" | "1/8" | "2" | "4" | "8">
                  drop:
                    precedence: <int; 1 | 2; required>

                    # Drop Threshold. This value may also be fractions.
                    # Example: 7/8 or 3/4 or 1/2
                    threshold: <str; required>

      # Most of the platform sand options are hardware dependent and optional.
      sand:
        qos_maps:
          - traffic_class: <int; 0-7>
            to_network_qos: <int; 0-63>
        lag:
          hardware_only: <bool>
          mode: <str>
        forwarding_mode: <str>
        multicast_replication:
          default: <str; "ingress" | "egress">

        # Sand platforms MDB Profile configuration. Note: l3-xxxl does not support MLAG.
        mdb_profile: <str; "balanced" | "balanced-xl" | "l3" | "l3-xl" | "l3-xxl" | "l3-xxxl">

      # Sfe (Software Forwarding Engine) settings.
      sfe:

        # Maximum number of CPUs used for data plane traffic forwarding.
        data_plane_cpu_allocation_max: <int; 1-128>

        # Configure interface related settings for Sfe platform.
        interface:

          # Configure one or more Receive Side Scaling (RSS) interface profiles.
          # This is supported on specific platforms.
          profiles:

              # RSS interface profile name.
            - name: <str; required; unique>

              # Interfaces within RSS profile.
              interfaces:

                  # Interface name such as 'Ethernet2'.
                - name: <str; required; unique>

                  # Receive queue parameters for the selected interface.
                  rx_queue:

                    # Number of receive queues.
                    # The maximum value is platform dependent.
                    count: <int; >=1>

                    # Worker ids specified as combination of range and/or comma separated values
                    # such as 0-4,7.
                    worker: <str>

                    # Mode applicable to the workers. Default mode is 'shared'.
                    mode: <str; "shared" | "exclusive">

          # RSS interface profile name to apply for the platform.
          # Needs system reload or Sfe agent restart for change to take effect.
          interface_profile: <str>
      fap:
        buffering_egress:

          # Preferred traffic profile for egress fap buffering.
          profile: <str; "unicast" | "balanced">
        voq:

          # Set Unified credit rates for all port speeds.
          credit_rates_unified: <bool>
    ```
