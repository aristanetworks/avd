<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>application_traffic_recognition</samp>](## "application_traffic_recognition") | Dictionary |  |  |  | Application traffic recognition configuration. |
    | [<samp>&nbsp;&nbsp;categories</samp>](## "application_traffic_recognition.categories") | List, items: Dictionary |  |  |  | List of categories. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.categories.[].name") | String | Required, Unique |  |  | Category name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;applications</samp>](## "application_traffic_recognition.categories.[].applications") | List, items: Dictionary |  |  |  | List of applications. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.categories.[].applications.[].name") | String |  |  |  | Application name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;service</samp>](## "application_traffic_recognition.categories.[].applications.[].service") | String |  |  | Valid Values:<br>- <code>audio-video</code><br>- <code>chat</code><br>- <code>default</code><br>- <code>file-transfer</code><br>- <code>networking-protocols</code><br>- <code>peer-to-peer</code><br>- <code>software-update</code> | If no service is specified, all supported services of the application are considered. |
    | [<samp>&nbsp;&nbsp;field_sets</samp>](## "application_traffic_recognition.field_sets") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l4_ports</samp>](## "application_traffic_recognition.field_sets.l4_ports") | List, items: Dictionary |  |  |  | L4 port field-set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.field_sets.l4_ports.[].name") | String | Required, Unique |  |  | L4 port field-set name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_values</samp>](## "application_traffic_recognition.field_sets.l4_ports.[].port_values") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "application_traffic_recognition.field_sets.l4_ports.[].port_values.[]") | String |  |  | Pattern: ^\d+(\-\d+)?$ | Port values or range of port values.<br>Port values are between 0 and 65535. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefixes</samp>](## "application_traffic_recognition.field_sets.ipv4_prefixes") | List, items: Dictionary |  |  |  | Ipv4 prefix field set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.field_sets.ipv4_prefixes.[].name") | String | Required, Unique |  |  | IPv4 prefix field-set name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_values</samp>](## "application_traffic_recognition.field_sets.ipv4_prefixes.[].prefix_values") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "application_traffic_recognition.field_sets.ipv4_prefixes.[].prefix_values.[]") | String |  |  | Pattern: ^\(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]{1,2}$ | IP prefix (ex- 1.2.3.0/24). |
    | [<samp>&nbsp;&nbsp;applications</samp>](## "application_traffic_recognition.applications") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_applications</samp>](## "application_traffic_recognition.applications.ipv4_applications") | List, items: Dictionary |  |  |  | List of user defined ipv4 applications. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].name") | String | Required, Unique |  |  | Application name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;src_prefix_set_name</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].src_prefix_set_name") | String |  |  |  | Source prefix set name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dest_prefix_set_name</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].dest_prefix_set_name") | String |  |  |  | Destination prefix set name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].protocol") | String |  |  |  | Protocol name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;src_port_set_name</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].src_port_set_name") | String |  |  |  | Source l4 port field set name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dest_port_set_name</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].dest_port_set_name") | String |  |  |  | Destination l4 port field set name. |
    | [<samp>&nbsp;&nbsp;application_profiles</samp>](## "application_traffic_recognition.application_profiles") | List, items: Dictionary |  |  |  | Group of applications. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.application_profiles.[].name") | String |  |  |  | Application Profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;applications</samp>](## "application_traffic_recognition.application_profiles.[].applications") | List, items: Dictionary |  |  |  | List of applications part of the application profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.application_profiles.[].applications.[].name") | String |  |  |  | Application Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;service</samp>](## "application_traffic_recognition.application_profiles.[].applications.[].service") | String |  |  | Valid Values:<br>- <code>audio-video</code><br>- <code>chat</code><br>- <code>default</code><br>- <code>file-transfer</code><br>- <code>networking-protocols</code><br>- <code>peer-to-peer</code><br>- <code>software-update</code> | Service Name.<br>Actual supported services for an application are subset of<br>mentioned valid values and is application dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transports</samp>](## "application_traffic_recognition.application_profiles.[].transports") | List, items: String |  |  |  | List of transport protocols. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "application_traffic_recognition.application_profiles.[].transports.[]") | String |  |  | Valid Values:<br>- <code>http</code><br>- <code>https</code><br>- <code>udp</code><br>- <code>tcp</code><br>- <code>ip</code><br>- <code>ip6</code><br>- <code>ssl</code><br>- <code>rtp</code><br>- <code>sctp</code><br>- <code>quic</code> | Transport name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;categories</samp>](## "application_traffic_recognition.application_profiles.[].categories") | List, items: Dictionary |  |  |  | Categories under this application profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.application_profiles.[].categories.[].name") | String |  |  |  | Name of a category. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;service</samp>](## "application_traffic_recognition.application_profiles.[].categories.[].service") | String |  |  | Valid Values:<br>- <code>audio-video</code><br>- <code>chat</code><br>- <code>default</code><br>- <code>file-transfer</code><br>- <code>networking-protocols</code><br>- <code>peer-to-peer</code><br>- <code>software-update</code> | Service name.<br>Actual supported services for an application are subset of<br>mentioned valid values and is application dependent. |

=== "YAML"

    ```yaml
    # Application traffic recognition configuration.
    application_traffic_recognition:

      # List of categories.
      categories:

          # Category name.
        - name: <str; required; unique>

          # List of applications.
          applications:

              # Application name.
            - name: <str>

              # If no service is specified, all supported services of the application are considered.
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

        # Ipv4 prefix field set.
        ipv4_prefixes:

            # IPv4 prefix field-set name.
          - name: <str; required; unique>
            prefix_values:

                # IP prefix (ex- 1.2.3.0/24).
              - <str>
      applications:

        # List of user defined ipv4 applications.
        ipv4_applications:

            # Application name.
          - name: <str; required; unique>

            # Source prefix set name.
            src_prefix_set_name: <str>

            # Destination prefix set name.
            dest_prefix_set_name: <str>

            # Protocol name.
            protocol: <str>

            # Source l4 port field set name.
            src_port_set_name: <str>

            # Destination l4 port field set name.
            dest_port_set_name: <str>

      # Group of applications.
      application_profiles:

          # Application Profile name.
        - name: <str>

          # List of applications part of the application profile.
          applications:

              # Application Name.
            - name: <str>

              # Service Name.
              # Actual supported services for an application are subset of
              # mentioned valid values and is application dependent.
              service: <str; "audio-video" | "chat" | "default" | "file-transfer" | "networking-protocols" | "peer-to-peer" | "software-update">

          # List of transport protocols.
          transports:

              # Transport name.
            - <str; "http" | "https" | "udp" | "tcp" | "ip" | "ip6" | "ssl" | "rtp" | "sctp" | "quic">

          # Categories under this application profile.
          categories:

              # Name of a category.
            - name: <str>

              # Service name.
              # Actual supported services for an application are subset of
              # mentioned valid values and is application dependent.
              service: <str; "audio-video" | "chat" | "default" | "file-transfer" | "networking-protocols" | "peer-to-peer" | "software-update">
    ```
