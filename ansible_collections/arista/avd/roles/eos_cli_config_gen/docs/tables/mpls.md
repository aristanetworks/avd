<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mpls</samp>](## "mpls") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ip</samp>](## "mpls.ip") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ldp</samp>](## "mpls.ldp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_disabled_default</samp>](## "mpls.ldp.interface_disabled_default") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "mpls.ldp.router_id") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "mpls.ldp.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;transport_address_interface</samp>](## "mpls.ldp.transport_address_interface") | String |  |  |  | Interface Name. |
    | [<samp>&nbsp;&nbsp;icmp</samp>](## "mpls.icmp") | Dictionary |  |  |  | Enables the LSRs to generate ICMP reply messages and deliver them to the originating host. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fragmentation_needed_tunneling</samp>](## "mpls.icmp.fragmentation_needed_tunneling") | Boolean |  |  |  | Enables the MPLS tunneling of MTU exceeded ICMP replies (fragmentation needed, packet too big). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ttl_exceeded_tunneling</samp>](## "mpls.icmp.ttl_exceeded_tunneling") | Boolean |  |  |  | Enables the MPLS tunneling of TTL exceeded ICMP replies. |
    | [<samp>&nbsp;&nbsp;rsvp</samp>](## "mpls.rsvp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;refresh</samp>](## "mpls.rsvp.refresh") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "mpls.rsvp.refresh.interval") | Integer |  |  | Min: 1<br>Max: 65535 | Time between refreshes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;method</samp>](## "mpls.rsvp.refresh.method") | String |  |  | Valid Values:<br>- <code>bundled</code><br>- <code>explicit</code> | Neighbor refresh mechanism.<br>bundled: Refresh states using message identifier lists.<br>explicit: Send each message individually. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "mpls.rsvp.authentication") | Dictionary |  |  |  | Cryptographic authentication. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password_indexes</samp>](## "mpls.rsvp.authentication.password_indexes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;index</samp>](## "mpls.rsvp.authentication.password_indexes.[].index") | Integer | Required, Unique |  | Min: 1<br>Max: 4294967295 | Password index. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password_type</samp>](## "mpls.rsvp.authentication.password_indexes.[].password_type") | String |  | `7` | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Authentication password type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "mpls.rsvp.authentication.password_indexes.[].password") | String |  |  |  | Password string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;active_index</samp>](## "mpls.rsvp.authentication.active_index") | Integer |  |  |  | Use index as active password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_number_window</samp>](## "mpls.rsvp.authentication.sequence_number_window") | Integer |  |  | Min: 1<br>Max: 255 | Size of reorder window for index in the sequence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "mpls.rsvp.authentication.type") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>none</code> | Authentication mechanism. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "mpls.rsvp.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "mpls.rsvp.neighbors.[].ip_address") | String |  |  |  | Neighbor's interface IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "mpls.rsvp.neighbors.[].ipv6_address") | String |  |  |  | Neighbor's interface IPv6 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "mpls.rsvp.neighbors.[].authentication") | Dictionary |  |  |  | Cryptographic authentication. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index</samp>](## "mpls.rsvp.neighbors.[].authentication.index") | Integer |  |  | Min: 1<br>Max: 4294967295 | Password index. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "mpls.rsvp.neighbors.[].authentication.type") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>none</code> | Authentication mechanism. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_access_group</samp>](## "mpls.rsvp.ip_access_group") | String |  |  |  | IPv4 Access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group</samp>](## "mpls.rsvp.ipv6_access_group") | String |  |  |  | IPv6 access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fast_reroute</samp>](## "mpls.rsvp.fast_reroute") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "mpls.rsvp.fast_reroute.mode") | String |  |  | Valid Values:<br>- <code>link-protection</code><br>- <code>node-protection</code><br>- <code>none</code> | Fast reroute mode.<br>link-protection: Protect against failure of the next link.<br>node-protection: Protect against failure of the next node.<br>none: Disable fast reroute. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reversion</samp>](## "mpls.rsvp.fast_reroute.reversion") | String |  |  | Valid Values:<br>- <code>global</code><br>- <code>local</code> | Reversion behavior.<br>Global revertive repair.<br>Local revertive repair. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bypass_tunnel_optimization_interval</samp>](## "mpls.rsvp.fast_reroute.bypass_tunnel_optimization_interval") | Integer |  |  | Min: 1<br>Max: 65535 | Fast-reroute bypass configuration.<br>Interval between each re-optimization attempt in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;srlg</samp>](## "mpls.rsvp.srlg") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "mpls.rsvp.srlg.enabled") | Boolean |  |  |  | Select SRLG behavior. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;strict</samp>](## "mpls.rsvp.srlg.strict") | Boolean |  |  |  | Apply strict SRLG constraint. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;label_local_termination</samp>](## "mpls.rsvp.label_local_termination") | String |  |  | Valid Values:<br>- <code>implicit-null</code><br>- <code>explicit-null</code> | Local termination label to be advertised. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;preemption_method</samp>](## "mpls.rsvp.preemption_method") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preemption</samp>](## "mpls.rsvp.preemption_method.preemption") | String |  |  | Valid Values:<br>- <code>hard</code><br>- <code>soft</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timer</samp>](## "mpls.rsvp.preemption_method.timer") | Integer |  |  | Min: 1<br>Max: 65535 | Timer value in units of seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu_signaling</samp>](## "mpls.rsvp.mtu_signaling") | Boolean |  |  |  | Enable MTU signaling. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;graceful_restart</samp>](## "mpls.rsvp.graceful_restart") | Dictionary |  |  |  | RSVP graceful restart. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role_helper</samp>](## "mpls.rsvp.graceful_restart.role_helper") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "mpls.rsvp.graceful_restart.role_helper.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timer_recovery</samp>](## "mpls.rsvp.graceful_restart.role_helper.timer_recovery") | Integer |  |  | Min: 1<br>Max: 320 | Maximum recovery timer value in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timer_restart</samp>](## "mpls.rsvp.graceful_restart.role_helper.timer_restart") | Integer |  |  | Min: 1<br>Max: 320 | Maximum restart timer value in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role_speaker</samp>](## "mpls.rsvp.graceful_restart.role_speaker") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "mpls.rsvp.graceful_restart.role_speaker.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timer_recovery</samp>](## "mpls.rsvp.graceful_restart.role_speaker.timer_recovery") | Integer |  |  | Min: 1<br>Max: 320 | Maximum recovery timer value in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timer_restart</samp>](## "mpls.rsvp.graceful_restart.role_speaker.timer_restart") | Integer |  |  | Min: 1<br>Max: 320 | Maximum restart timer value in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hello</samp>](## "mpls.rsvp.hello") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "mpls.rsvp.hello.interval") | Integer |  |  | Min: 1<br>Max: 60 | Time between hello messages in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "mpls.rsvp.hello.multiplier") | Integer |  |  | Min: 1<br>Max: 255 | Number of missed hellos after which the neighbor is expired. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hitless_restart</samp>](## "mpls.rsvp.hitless_restart") | Dictionary |  |  |  | RSVP hitless restart. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "mpls.rsvp.hitless_restart.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timer_recovery</samp>](## "mpls.rsvp.hitless_restart.timer_recovery") | Integer |  |  | Min: 1<br>Max: 320 | Time stale states will be preserved after restart.<br>Value in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;p2mp</samp>](## "mpls.rsvp.p2mp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "mpls.rsvp.p2mp.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "mpls.rsvp.shutdown") | Boolean |  |  |  | Make `shutdown` key false for `no shutdown` cli. |
    | [<samp>&nbsp;&nbsp;label_ranges</samp>](## "mpls.label_ranges") | Dictionary |  |  |  | MPLS label ranges configuration.<br>Few configured MPLS ranges for various categories could overlap.<br>Requires EOS 4.31.1F or later. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_sr</samp>](## "mpls.label_ranges.bgp_sr") | Dictionary |  |  |  | Label range for BGP SR global segment identifiers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;base</samp>](## "mpls.label_ranges.bgp_sr.base") | Integer | Required |  | Min: 16<br>Max: 1048575 | First label of range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "mpls.label_ranges.bgp_sr.size") | Integer | Required |  | Min: 0<br>Max: 1048560 | Size of range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "mpls.label_ranges.dynamic") | Dictionary |  |  |  | Label range for dynamic assignment. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;base</samp>](## "mpls.label_ranges.dynamic.base") | Integer | Required |  | Min: 16<br>Max: 1048575 | First label of range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "mpls.label_ranges.dynamic.size") | Integer | Required |  | Min: 131072<br>Max: 1048560 | Size of range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_sr</samp>](## "mpls.label_ranges.isis_sr") | Dictionary |  |  |  | Label range for IS-IS SR global segment identifiers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;base</samp>](## "mpls.label_ranges.isis_sr.base") | Integer | Required |  | Min: 16<br>Max: 1048575 | First label of range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "mpls.label_ranges.isis_sr.size") | Integer | Required |  | Min: 0<br>Max: 1048560 | Size of range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2evpn</samp>](## "mpls.label_ranges.l2evpn") | Dictionary |  |  |  | Label range for L2 EVPN routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;base</samp>](## "mpls.label_ranges.l2evpn.base") | Integer | Required |  | Min: 16<br>Max: 1048575 | First label of range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "mpls.label_ranges.l2evpn.size") | Integer | Required |  | Min: 0<br>Max: 1048560 | Size of range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2evpn_ethernet_segment</samp>](## "mpls.label_ranges.l2evpn_ethernet_segment") | Dictionary |  |  |  | Labels reserved for L2 EVPN A-D per ES routes for split-horizon filtering. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;base</samp>](## "mpls.label_ranges.l2evpn_ethernet_segment.base") | Integer | Required |  | Min: 16<br>Max: 1048575 | First label of range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "mpls.label_ranges.l2evpn_ethernet_segment.size") | Integer | Required |  | Min: 0<br>Max: 1048560 | Size of range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_sr</samp>](## "mpls.label_ranges.ospf_sr") | Dictionary |  |  |  | Label range for OSPF Segment Routing Global Block (SRGB). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;base</samp>](## "mpls.label_ranges.ospf_sr.base") | Integer | Required |  | Min: 16<br>Max: 1048575 | First label of range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "mpls.label_ranges.ospf_sr.size") | Integer | Required |  | Min: 0<br>Max: 1048560 | Size of range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;srlb</samp>](## "mpls.label_ranges.srlb") | Dictionary |  |  |  | Label range for SR local segment identifiers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;base</samp>](## "mpls.label_ranges.srlb.base") | Integer | Required |  | Min: 16<br>Max: 1048575 | First label of range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "mpls.label_ranges.srlb.size") | Integer | Required |  | Min: 0<br>Max: 1048560 | Size of range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "mpls.label_ranges.static") | Dictionary |  |  |  | Label range for static MPLS routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;base</samp>](## "mpls.label_ranges.static.base") | Integer | Required |  | Min: 16<br>Max: 1048575 | First label of range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "mpls.label_ranges.static.size") | Integer | Required |  | Min: 0<br>Max: 1048560 | Size of range. |
    | [<samp>&nbsp;&nbsp;tunnel</samp>](## "mpls.tunnel") | Dictionary |  |  |  | Configure MPLS tunnel. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;termination</samp>](## "mpls.tunnel.termination") | Dictionary |  |  |  | Controls selection of the TTL/DSCP values by LER when decapsulating MPLS packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;model</samp>](## "mpls.tunnel.termination.model") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "mpls.tunnel.termination.model.ttl") | String | Required |  | Valid Values:<br>- <code>pipe</code><br>- <code>uniform</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "mpls.tunnel.termination.model.dscp") | String | Required |  | Valid Values:<br>- <code>pipe</code><br>- <code>uniform</code> | The DSCP model `uniform` is supported only on specific hardware platforms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;php_model</samp>](## "mpls.tunnel.termination.php_model") | Dictionary |  |  |  | Used on PHP router in the absence of any VPN routes and explicit null VRF labels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "mpls.tunnel.termination.php_model.ttl") | String | Required |  | Valid Values:<br>- <code>pipe</code><br>- <code>uniform</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "mpls.tunnel.termination.php_model.dscp") | String | Required |  | Valid Values:<br>- <code>pipe</code><br>- <code>uniform</code> | The DSCP model `uniform` is supported only on specific hardware platforms. |

=== "YAML"

    ```yaml
    mpls:
      ip: <bool>
      ldp:
        interface_disabled_default: <bool>
        router_id: <str>
        shutdown: <bool>

        # Interface Name.
        transport_address_interface: <str>

      # Enables the LSRs to generate ICMP reply messages and deliver them to the originating host.
      icmp:

        # Enables the MPLS tunneling of MTU exceeded ICMP replies (fragmentation needed, packet too big).
        fragmentation_needed_tunneling: <bool>

        # Enables the MPLS tunneling of TTL exceeded ICMP replies.
        ttl_exceeded_tunneling: <bool>
      rsvp:
        refresh:

          # Time between refreshes.
          interval: <int; 1-65535>

          # Neighbor refresh mechanism.
          # bundled: Refresh states using message identifier lists.
          # explicit: Send each message individually.
          method: <str; "bundled" | "explicit">

        # Cryptographic authentication.
        authentication:
          password_indexes:

              # Password index.
            - index: <int; 1-4294967295; required; unique>

              # Authentication password type.
              password_type: <str; "0" | "7" | "8a"; default="7">

              # Password string.
              password: <str>

          # Use index as active password.
          active_index: <int>

          # Size of reorder window for index in the sequence.
          sequence_number_window: <int; 1-255>

          # Authentication mechanism.
          type: <str; "md5" | "none">
        neighbors:

            # Neighbor's interface IPv4 address.
          - ip_address: <str>

            # Neighbor's interface IPv6 address.
            ipv6_address: <str>

            # Cryptographic authentication.
            authentication:

              # Password index.
              index: <int; 1-4294967295>

              # Authentication mechanism.
              type: <str; "md5" | "none">

        # IPv4 Access list name.
        ip_access_group: <str>

        # IPv6 access list name.
        ipv6_access_group: <str>
        fast_reroute:

          # Fast reroute mode.
          # link-protection: Protect against failure of the next link.
          # node-protection: Protect against failure of the next node.
          # none: Disable fast reroute.
          mode: <str; "link-protection" | "node-protection" | "none">

          # Reversion behavior.
          # Global revertive repair.
          # Local revertive repair.
          reversion: <str; "global" | "local">

          # Fast-reroute bypass configuration.
          # Interval between each re-optimization attempt in seconds.
          bypass_tunnel_optimization_interval: <int; 1-65535>
        srlg:

          # Select SRLG behavior.
          enabled: <bool>

          # Apply strict SRLG constraint.
          strict: <bool>

        # Local termination label to be advertised.
        label_local_termination: <str; "implicit-null" | "explicit-null">
        preemption_method:
          preemption: <str; "hard" | "soft">

          # Timer value in units of seconds.
          timer: <int; 1-65535>

        # Enable MTU signaling.
        mtu_signaling: <bool>

        # RSVP graceful restart.
        graceful_restart:
          role_helper:
            enabled: <bool>

            # Maximum recovery timer value in seconds.
            timer_recovery: <int; 1-320>

            # Maximum restart timer value in seconds.
            timer_restart: <int; 1-320>
          role_speaker:
            enabled: <bool>

            # Maximum recovery timer value in seconds.
            timer_recovery: <int; 1-320>

            # Maximum restart timer value in seconds.
            timer_restart: <int; 1-320>
        hello:

          # Time between hello messages in seconds.
          interval: <int; 1-60>

          # Number of missed hellos after which the neighbor is expired.
          multiplier: <int; 1-255>

        # RSVP hitless restart.
        hitless_restart:
          enabled: <bool>

          # Time stale states will be preserved after restart.
          # Value in seconds.
          timer_recovery: <int; 1-320>
        p2mp:
          enabled: <bool>

        # Make `shutdown` key false for `no shutdown` cli.
        shutdown: <bool>

      # MPLS label ranges configuration.
      # Few configured MPLS ranges for various categories could overlap.
      # Requires EOS 4.31.1F or later.
      label_ranges:

        # Label range for BGP SR global segment identifiers.
        bgp_sr:

          # First label of range.
          base: <int; 16-1048575; required>

          # Size of range.
          size: <int; 0-1048560; required>

        # Label range for dynamic assignment.
        dynamic:

          # First label of range.
          base: <int; 16-1048575; required>

          # Size of range.
          size: <int; 131072-1048560; required>

        # Label range for IS-IS SR global segment identifiers.
        isis_sr:

          # First label of range.
          base: <int; 16-1048575; required>

          # Size of range.
          size: <int; 0-1048560; required>

        # Label range for L2 EVPN routes.
        l2evpn:

          # First label of range.
          base: <int; 16-1048575; required>

          # Size of range.
          size: <int; 0-1048560; required>

        # Labels reserved for L2 EVPN A-D per ES routes for split-horizon filtering.
        l2evpn_ethernet_segment:

          # First label of range.
          base: <int; 16-1048575; required>

          # Size of range.
          size: <int; 0-1048560; required>

        # Label range for OSPF Segment Routing Global Block (SRGB).
        ospf_sr:

          # First label of range.
          base: <int; 16-1048575; required>

          # Size of range.
          size: <int; 0-1048560; required>

        # Label range for SR local segment identifiers.
        srlb:

          # First label of range.
          base: <int; 16-1048575; required>

          # Size of range.
          size: <int; 0-1048560; required>

        # Label range for static MPLS routes.
        static:

          # First label of range.
          base: <int; 16-1048575; required>

          # Size of range.
          size: <int; 0-1048560; required>

      # Configure MPLS tunnel.
      tunnel:

        # Controls selection of the TTL/DSCP values by LER when decapsulating MPLS packets.
        termination:
          model:
            ttl: <str; "pipe" | "uniform"; required>

            # The DSCP model `uniform` is supported only on specific hardware platforms.
            dscp: <str; "pipe" | "uniform"; required>

          # Used on PHP router in the absence of any VPN routes and explicit null VRF labels.
          php_model:
            ttl: <str; "pipe" | "uniform"; required>

            # The DSCP model `uniform` is supported only on specific hardware platforms.
            dscp: <str; "pipe" | "uniform"; required>
    ```
