<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>application_traffic_recognition</samp>](## "application_traffic_recognition") | Dictionary |  |  |  | Application traffic recognition configuration. |
    | [<samp>&nbsp;&nbsp;categories</samp>](## "application_traffic_recognition.categories") | List, items: Dictionary |  |  |  | Space to add new categories or modify existing categories. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.categories.[].name") | String | Required, Unique |  |  | Name of the category. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;applications_and_services</samp>](## "application_traffic_recognition.categories.[].applications_and_services") | List, items: Dictionary |  |  |  | Application and service pair. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.categories.[].applications_and_services.[].name") | String |  |  |  | Name of the application. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;service</samp>](## "application_traffic_recognition.categories.[].applications_and_services.[].service") | String |  |  |  | Supported service of the application. |
    | [<samp>&nbsp;&nbsp;port_range_sets</samp>](## "application_traffic_recognition.port_range_sets") | List, items: Dictionary |  |  |  | Define range of ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.port_range_sets.[].name") | String | Required, Unique |  |  | Name of the port set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ports</samp>](## "application_traffic_recognition.port_range_sets.[].ports") | List, items: String |  |  |  | Set of port ranges. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "application_traffic_recognition.port_range_sets.[].ports.[]") | String |  |  |  | Port range formatted as start-end ( ex - 2400-2500 ). |
    | [<samp>&nbsp;&nbsp;prefix_sets</samp>](## "application_traffic_recognition.prefix_sets") | List, items: Dictionary |  |  |  | Define prefix sets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.prefix_sets.[].name") | String | Required, Unique |  |  | Name of the prefix set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "application_traffic_recognition.prefix_sets.[].prefixes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "application_traffic_recognition.prefix_sets.[].prefixes.[]") | String |  |  |  | Ip prefix to match against the source/destination IP in packets (ex- 1.2.3.0/24). |
    | [<samp>&nbsp;&nbsp;user_defined_ipv4_applications</samp>](## "application_traffic_recognition.user_defined_ipv4_applications") | List, items: Dictionary |  |  |  | List of user defined ipv4 applications. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.user_defined_ipv4_applications.[].name") | String | Required, Unique |  |  | Name of the application. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;src_prefix_set_name</samp>](## "application_traffic_recognition.user_defined_ipv4_applications.[].src_prefix_set_name") | String |  |  |  | Specify a defined prefix set name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dest_prefix_set_name</samp>](## "application_traffic_recognition.user_defined_ipv4_applications.[].dest_prefix_set_name") | String |  |  |  | Specify a defined prefix set name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "application_traffic_recognition.user_defined_ipv4_applications.[].protocol") | String |  |  |  | Protocol to match the packets against. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;src_port_set_name</samp>](## "application_traffic_recognition.user_defined_ipv4_applications.[].src_port_set_name") | String |  |  |  | Specify a defined port range name. Used to match against the src port in packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dest_port_set_name</samp>](## "application_traffic_recognition.user_defined_ipv4_applications.[].dest_port_set_name") | String |  |  |  | Specify a defined port range name. Used to match against the dest port in packets. |
    | [<samp>&nbsp;&nbsp;application_profiles</samp>](## "application_traffic_recognition.application_profiles") | List, items: Dictionary |  |  |  | Profiles is a collection of applications and categories with/without services. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.application_profiles.[].name") | String |  |  |  | Name of the application profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;applications</samp>](## "application_traffic_recognition.application_profiles.[].applications") | List, items: Dictionary |  |  |  | Specify list of application and service pair to be part of the application profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.application_profiles.[].applications.[].name") | String |  |  |  | Name of an application. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;service</samp>](## "application_traffic_recognition.application_profiles.[].applications.[].service") | String |  |  |  | One of the supported services of the application. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transports</samp>](## "application_traffic_recognition.application_profiles.[].transports") | List, items: String |  |  |  | List of transport protocols. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "application_traffic_recognition.application_profiles.[].transports.[]") | String |  |  |  | Transport name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;categories</samp>](## "application_traffic_recognition.application_profiles.[].categories") | List, items: Dictionary |  |  |  | Categories under this application profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.application_profiles.[].categories.[].name") | String |  |  |  | Name of a category. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;service</samp>](## "application_traffic_recognition.application_profiles.[].categories.[].service") | String |  |  |  | Service name. Matches applications supporting the service. |

=== "YAML"

    ```yaml
    # Application traffic recognition configuration.
    application_traffic_recognition:

      # Space to add new categories or modify existing categories.
      categories:

          # Name of the category.
        - name: <str; required; unique>

          # Application and service pair.
          applications_and_services:

              # Name of the application.
            - name: <str>

              # Supported service of the application.
              service: <str>

      # Define range of ports.
      port_range_sets:

          # Name of the port set.
        - name: <str; required; unique>

          # Set of port ranges.
          ports:

              # Port range formatted as start-end ( ex - 2400-2500 ).
            - <str>

      # Define prefix sets.
      prefix_sets:

          # Name of the prefix set.
        - name: <str; required; unique>
          prefixes:

              # Ip prefix to match against the source/destination IP in packets (ex- 1.2.3.0/24).
            - <str>

      # List of user defined ipv4 applications.
      user_defined_ipv4_applications:

          # Name of the application.
        - name: <str; required; unique>

          # Specify a defined prefix set name.
          src_prefix_set_name: <str>

          # Specify a defined prefix set name.
          dest_prefix_set_name: <str>

          # Protocol to match the packets against.
          protocol: <str>

          # Specify a defined port range name. Used to match against the src port in packets.
          src_port_set_name: <str>

          # Specify a defined port range name. Used to match against the dest port in packets.
          dest_port_set_name: <str>

      # Profiles is a collection of applications and categories with/without services.
      application_profiles:

          # Name of the application profile.
        - name: <str>

          # Specify list of application and service pair to be part of the application profile.
          applications:

              # Name of an application.
            - name: <str>

              # One of the supported services of the application.
              service: <str>

          # List of transport protocols.
          transports:

              # Transport name.
            - <str>

          # Categories under this application profile.
          categories:

              # Name of a category.
            - name: <str>

              # Service name. Matches applications supporting the service.
              service: <str>
    ```
