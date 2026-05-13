<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>monitor_connectivity</samp>](## "monitor_connectivity") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;shutdown</samp>](## "monitor_connectivity.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;interval</samp>](## "monitor_connectivity.interval") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;interface_sets</samp>](## "monitor_connectivity.interface_sets") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_connectivity.interface_sets.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "monitor_connectivity.interface_sets.[].interfaces") | List, items: String | Required |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "monitor_connectivity.interface_sets.[].interfaces.[]") | String |  |  |  | Multiple interfaces should be of same type, Ethernet, Loopback, Management etc.<br>Multiple interfaces can be specified by separate elements. |
    | [<samp>&nbsp;&nbsp;local_interfaces</samp>](## "monitor_connectivity.local_interfaces") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;address_only</samp>](## "monitor_connectivity.address_only") | Boolean |  | `False` |  | When address-only is configured, the source IP of the packet is set to the interface<br>IP but the packet may exit the device via a different interface.<br>When set to `false`, the probe uses the interface to exit the device. |
    | [<samp>&nbsp;&nbsp;hosts</samp>](## "monitor_connectivity.hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_connectivity.hosts.[].name") | String | Required, Unique |  |  | Host Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "monitor_connectivity.hosts.[].description") | String |  |  |  | Description in the form of<br>```<br>description<br><description><br>``` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single_line_description</samp>](## "monitor_connectivity.hosts.[].single_line_description") | String |  |  |  | Description in the form of `description <description>`.<br>Supported in EOS versions 4.32.2F and above. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "monitor_connectivity.hosts.[].ip") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_echo_size</samp>](## "monitor_connectivity.hosts.[].icmp_echo_size") | Integer |  |  | Min: 36<br>Max: 18024 | Size of ICMP probe in bytes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp>](## "monitor_connectivity.hosts.[].local_interfaces") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_only</samp>](## "monitor_connectivity.hosts.[].address_only") | Boolean |  | `False` |  | When address-only is configured, the source IP of the packet is set to the interface<br>IP but the packet may exit the device via a different interface.<br>When set to `false`, the probe uses the interface to exit the device. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "monitor_connectivity.hosts.[].url") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;name_server_group</samp>](## "monitor_connectivity.name_server_group") | String |  |  |  | Set name-server group. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "monitor_connectivity.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_connectivity.vrfs.[].name") | String | Required, Unique |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "monitor_connectivity.vrfs.[].description") | String |  |  |  | Description in the form of<br>```<br>description<br><description><br>``` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single_line_description</samp>](## "monitor_connectivity.vrfs.[].single_line_description") | String |  |  |  | Description in the form of `description <description>`.<br>Supported in EOS versions 4.32.2F and above. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface_sets</samp>](## "monitor_connectivity.vrfs.[].interface_sets") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_connectivity.vrfs.[].interface_sets.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "monitor_connectivity.vrfs.[].interface_sets.[].interfaces") | List, items: String | Required |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "monitor_connectivity.vrfs.[].interface_sets.[].interfaces.[]") | String |  |  |  | Multiple interfaces should be of same type, Ethernet, Loopback, Management etc.<br>Multiple interfaces can be specified by separate elements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp>](## "monitor_connectivity.vrfs.[].local_interfaces") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_only</samp>](## "monitor_connectivity.vrfs.[].address_only") | Boolean |  | `False` |  | When address-only is configured, the source IP of the packet is set to the interface<br>IP but the packet may exit the device via a different interface.<br>When set to `false`, the probe uses the interface to exit the device. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hosts</samp>](## "monitor_connectivity.vrfs.[].hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_connectivity.vrfs.[].hosts.[].name") | String | Required, Unique |  |  | Host name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "monitor_connectivity.vrfs.[].hosts.[].description") | String |  |  |  | Description in the form of<br>```<br>description<br><description><br>``` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single_line_description</samp>](## "monitor_connectivity.vrfs.[].hosts.[].single_line_description") | String |  |  |  | Description in the form of `description <description>`.<br>Supported in EOS versions 4.32.2F and above. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "monitor_connectivity.vrfs.[].hosts.[].ip") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_echo_size</samp>](## "monitor_connectivity.vrfs.[].hosts.[].icmp_echo_size") | Integer |  |  | Min: 36<br>Max: 18024 | Size of ICMP probe in bytes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp>](## "monitor_connectivity.vrfs.[].hosts.[].local_interfaces") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_only</samp>](## "monitor_connectivity.vrfs.[].hosts.[].address_only") | Boolean |  | `False` |  | When address-only is configured, the source IP of the packet is set to the interface<br>IP but the packet may exit the device via a different interface.<br>When set to `false`, the probe uses the interface to exit the device. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "monitor_connectivity.vrfs.[].hosts.[].url") | String |  |  |  |  |

=== "YAML"

    ```yaml
    monitor_connectivity:
      shutdown: <bool>
      interval: <int>
      interface_sets:
        - name: <str; required; unique>
          interfaces: # >=1 items; required

              # Multiple interfaces should be of same type, Ethernet, Loopback, Management etc.
              # Multiple interfaces can be specified by separate elements.
            - <str>
      local_interfaces: <str>

      # When address-only is configured, the source IP of the packet is set to the interface
      # IP but the packet may exit the device via a different interface.
      # When set to `false`, the probe uses the interface to exit the device.
      address_only: <bool; default=False>
      hosts:

          # Host Name.
        - name: <str; required; unique>

          # Description in the form of
          # ```
          # description
          # <description>
          # ```
          description: <str>

          # Description in the form of `description <description>`.
          # Supported in EOS versions 4.32.2F and above.
          single_line_description: <str>
          ip: <str>

          # Size of ICMP probe in bytes.
          icmp_echo_size: <int; 36-18024>
          local_interfaces: <str>

          # When address-only is configured, the source IP of the packet is set to the interface
          # IP but the packet may exit the device via a different interface.
          # When set to `false`, the probe uses the interface to exit the device.
          address_only: <bool; default=False>
          url: <str>

      # Set name-server group.
      name_server_group: <str>
      vrfs:

          # VRF Name.
        - name: <str; required; unique>

          # Description in the form of
          # ```
          # description
          # <description>
          # ```
          description: <str>

          # Description in the form of `description <description>`.
          # Supported in EOS versions 4.32.2F and above.
          single_line_description: <str>
          interface_sets:
            - name: <str; required; unique>
              interfaces: # >=1 items; required

                  # Multiple interfaces should be of same type, Ethernet, Loopback, Management etc.
                  # Multiple interfaces can be specified by separate elements.
                - <str>
          local_interfaces: <str>

          # When address-only is configured, the source IP of the packet is set to the interface
          # IP but the packet may exit the device via a different interface.
          # When set to `false`, the probe uses the interface to exit the device.
          address_only: <bool; default=False>
          hosts:

              # Host name.
            - name: <str; required; unique>

              # Description in the form of
              # ```
              # description
              # <description>
              # ```
              description: <str>

              # Description in the form of `description <description>`.
              # Supported in EOS versions 4.32.2F and above.
              single_line_description: <str>
              ip: <str>

              # Size of ICMP probe in bytes.
              icmp_echo_size: <int; 36-18024>
              local_interfaces: <str>

              # When address-only is configured, the source IP of the packet is set to the interface
              # IP but the packet may exit the device via a different interface.
              # When set to `false`, the probe uses the interface to exit the device.
              address_only: <bool; default=False>
              url: <str>
    ```
