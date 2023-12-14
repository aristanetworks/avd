<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dns_settings</samp>](## "dns_settings") | Dictionary |  |  |  | DNS settings<br>For DNS source-interfaces see "source_interfaces.domain_lookup" |
    | [<samp>&nbsp;&nbsp;domain</samp>](## "dns_settings.domain") | String |  |  |  | DNS domain name like 'fabric.local' |
    | [<samp>&nbsp;&nbsp;servers</samp>](## "dns_settings.servers") | List, items: Dictionary |  |  |  | This key replaces the deprecated `name_servers`. Both keys should not be used at the same time. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- vrf</samp>](## "dns_settings.servers.[].vrf") | String |  |  |  | VRF Name.<br>Can be used in combination with "use_mgmt_interface_vrf" and "use_inband_mgmt_vrf" to configure the DNS server under multiple VRFs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_mgmt_interface_vrf</samp>](## "dns_settings.servers.[].use_mgmt_interface_vrf") | Boolean |  |  |  | Configure the DNS server under the VRF set with "mgmt_interface_vrf". Ignored if 'mgmt_ip' or 'ipv6_mgmt_ip' are not configured for the device, so if the host is only configured with this VRF, the server will not be configured at all. Can be used in combination with "vrf" and "use_inband_mgmt_vrf" to configure the DNS server under multiple VRFs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_inband_mgmt_vrf</samp>](## "dns_settings.servers.[].use_inband_mgmt_vrf") | Boolean |  |  |  | Configure the DNS server under the VRF set with "inband_mgmt_vrf". Ignored if inband management is not configured for the device, so if the host is only configured with this VRF, the server will not be configured at all. Can be used in combination with "vrf" and "use_mgmt_interface_vrf" to configure the DNS server under multiple VRFs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "dns_settings.servers.[].ip_address") | String |  |  |  | IPv4 or IPv6 address for DNS server |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "dns_settings.servers.[].priority") | Integer |  |  | Min: 0<br>Max: 4 | Priority value (lower is first) |
    | [<samp>event_handlers</samp>](## "event_handlers") | List, items: Dictionary |  |  |  | Gives the ability to monitor and react to Syslog messages.<br>Event Handlers provide a powerful and flexible tool that can be used to apply self-healing actions,<br>customize the system behavior, and implement workarounds to problems discovered in the field.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "event_handlers.[].name") | String | Required, Unique |  |  | Event Handler Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action_type</samp>](## "event_handlers.[].action_type") | String |  |  | Valid Values:<br>- <code>bash</code><br>- <code>increment</code><br>- <code>log</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "event_handlers.[].action") | String |  |  |  | Command to execute<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "event_handlers.[].delay") | Integer |  |  |  | Event-handler delay in seconds<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger</samp>](## "event_handlers.[].trigger") | String |  |  | Valid Values:<br>- <code>on-boot</code><br>- <code>on-logging</code><br>- <code>on-startup-config</code> | Configure event trigger condition.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;regex</samp>](## "event_handlers.[].regex") | String |  |  |  | Regular expression to use for searching log messages. Required for on-logging trigger<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;asynchronous</samp>](## "event_handlers.[].asynchronous") | Boolean |  | `False` |  | Set the action to be non-blocking. |
    | [<samp>ipv6_mgmt_destination_networks</samp>](## "ipv6_mgmt_destination_networks") | List, items: String |  |  |  | List of IPv6 prefixes to configure as static routes towards the OOB IPv6 Management interface gateway.<br>Replaces the default route.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ipv6_mgmt_destination_networks.[]") | String |  |  |  | IPv6_network/Mask. |
    | [<samp>ipv6_mgmt_gateway</samp>](## "ipv6_mgmt_gateway") | String |  |  | Format: ipv6 | OOB Management interface gateway in IPv6 format.<br>Used as next-hop for default gateway or static routes defined under 'ipv6_mgmt_destination_networks'. |
    | [<samp>local_users</samp>](## "local_users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "local_users.[].name") | String | Required, Unique |  |  | Username |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "local_users.[].disabled") | Boolean |  |  |  | If true, the user will be removed and all other settings are ignored.<br>Useful for removing the default "admin" user.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "local_users.[].privilege") | Integer |  |  | Min: 0<br>Max: 15 | Initial privilege level with local EXEC authorization.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "local_users.[].role") | String |  |  |  | EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp>](## "local_users.[].sha512_password") | String |  |  |  | SHA512 Hash of Password<br>Must be the hash of the password. By default EOS salts the password with the username, so the simplest is to generate the hash on an EOS device using the same username.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;no_password</samp>](## "local_users.[].no_password") | Boolean |  |  |  | If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssh_key</samp>](## "local_users.[].ssh_key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shell</samp>](## "local_users.[].shell") | String |  |  | Valid Values:<br>- <code>/bin/bash</code><br>- <code>/bin/sh</code><br>- <code>/sbin/nologin</code> | Specify shell for the user<br> |
    | [<samp>management_eapi</samp>](## "management_eapi") | Dictionary |  |  |  | Default is HTTPS management eAPI enabled.<br>The VRF is set to < mgmt_interface_vrf >.<br> |
    | [<samp>&nbsp;&nbsp;enable_http</samp>](## "management_eapi.enable_http") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;enable_https</samp>](## "management_eapi.enable_https") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;default_services</samp>](## "management_eapi.default_services") | Boolean |  |  |  |  |
    | [<samp>name_servers</samp>](## "name_servers") <span style="color:red">deprecated</span> | List, items: String |  |  |  | List of DNS servers. The VRF is set to < mgmt_interface_vrf >.<span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>dns_settings.servers</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "name_servers.[].&lt;str&gt;") | String |  |  |  | IPv4 address |
    | [<samp>timezone</samp>](## "timezone") | String |  |  |  | Clock timezone like "CET" or "US/Pacific". |

=== "YAML"

    ```yaml
    dns_settings:
      domain: <str>
      servers:
        - vrf: <str>
          use_mgmt_interface_vrf: <bool>
          use_inband_mgmt_vrf: <bool>
          ip_address: <str>
          priority: <int>
  
    # Gives the ability to monitor and react to Syslog messages.
    # Event Handlers provide a powerful and flexible tool that can be used to apply self-healing actions,
    # customize the system behavior, and implement workarounds to problems discovered in the field.
    event_handlers:

        # Event Handler Name
      - name: <str; required; unique>
        action_type: <str; "bash" | "increment" | "log">

        # Command to execute
        action: <str>

        # Event-handler delay in seconds
        delay: <int>

        # Configure event trigger condition.
        trigger: <str; "on-boot" | "on-logging" | "on-startup-config">

        # Regular expression to use for searching log messages. Required for on-logging trigger
        regex: <str>

        # Set the action to be non-blocking.
        asynchronous: <bool; default=False>

    # List of IPv6 prefixes to configure as static routes towards the OOB IPv6 Management interface gateway.
    # Replaces the default route.
    ipv6_mgmt_destination_networks:

        # IPv6_network/Mask.
      - <str>

    # OOB Management interface gateway in IPv6 format.
    # Used as next-hop for default gateway or static routes defined under 'ipv6_mgmt_destination_networks'.
    ipv6_mgmt_gateway: <str>
    local_users:

        # Username
      - name: <str; required; unique>

        # If true, the user will be removed and all other settings are ignored.
        # Useful for removing the default "admin" user.
        disabled: <bool>

        # Initial privilege level with local EXEC authorization.
        privilege: <int; 0-15>

        # EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator"
        role: <str>

        # SHA512 Hash of Password
        # Must be the hash of the password. By default EOS salts the password with the username, so the simplest is to generate the hash on an EOS device using the same username.
        sha512_password: <str>

        # If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user.
        no_password: <bool>
        ssh_key: <str>

        # Specify shell for the user
        shell: <str; "/bin/bash" | "/bin/sh" | "/sbin/nologin">

    # Default is HTTPS management eAPI enabled.
    # The VRF is set to < mgmt_interface_vrf >.
    management_eapi:
      enable_http: <bool; default=False>
      enable_https: <bool; default=True>
      default_services: <bool>

    # List of DNS servers. The VRF is set to < mgmt_interface_vrf >.
    name_servers:

        # IPv4 address
      - <str>

    # Clock timezone like "CET" or "US/Pacific".
    timezone: <str>
    ```
