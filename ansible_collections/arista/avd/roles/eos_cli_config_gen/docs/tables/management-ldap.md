<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_ldap</samp>](## "management_ldap") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;server_defaults</samp>](## "management_ldap.server_defaults") | Dictionary |  |  |  | Default LDAP options applied to all servers unless overridden per host. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;base_dn</samp>](## "management_ldap.server_defaults.base_dn") | String |  |  |  | Base Distinguished Name used for LDAP searches (e.g., dc=example,dc=com). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rdn_attribute_user</samp>](## "management_ldap.server_defaults.rdn_attribute_user") | String |  |  |  | Relative Distinguished Name attribute(s) for user lookup (e.g., cn). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssl_profile</samp>](## "management_ldap.server_defaults.ssl_profile") | String |  |  |  | SSL profile name to secure LDAP connections. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;authorization_group_policy</samp>](## "management_ldap.server_defaults.authorization_group_policy") | String |  |  |  | LDAP group policy name to use for user authorization. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "management_ldap.server_defaults.timeout") | Integer |  |  | Min: 1<br>Max: 1000 | Time in seconds (EOS default 30 seconds) to wait for a response from this LDAP server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;search</samp>](## "management_ldap.server_defaults.search") | Dictionary |  |  |  | Credentials used by the switch to perform LDAP search bind operations. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;username</samp>](## "management_ldap.server_defaults.search.username") | String | Required |  |  | LDAP username (full DN) for search bind operations (e.g., cn=ldap-admin,dc=example,dc=com). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "management_ldap.server_defaults.search.password") | String | Required |  |  | Password for the search bind user. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password_type</samp>](## "management_ldap.server_defaults.search.password_type") | String |  |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Password encryption type.<br>- 0 = clear text<br>- 7 = obfuscated<br>- 8a = AES-256-GCM encrypted.<br>Omit to provide an unobfuscated string (EOS will store it obfuscated). |
    | [<samp>&nbsp;&nbsp;server_hosts</samp>](## "management_ldap.server_hosts") | List, items: Dictionary |  |  |  | List of LDAP server hosts. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;host</samp>](## "management_ldap.server_hosts.[].host") | String | Required, Unique |  |  | Hostname or IP address of the LDAP server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "management_ldap.server_hosts.[].port") | Integer |  |  | Min: 0<br>Max: 65535 | Port of LDAP server (EOS default 389). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_ldap.server_hosts.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;base_dn</samp>](## "management_ldap.server_hosts.[].base_dn") | String |  |  |  | Base Distinguished Name used for LDAP searches (e.g., dc=example,dc=com). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rdn_attribute_user</samp>](## "management_ldap.server_hosts.[].rdn_attribute_user") | String |  |  |  | Relative Distinguished Name attribute(s) for user lookup (e.g., cn). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ssl_profile</samp>](## "management_ldap.server_hosts.[].ssl_profile") | String |  |  |  | SSL profile name to secure LDAP connections. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authorization_group_policy</samp>](## "management_ldap.server_hosts.[].authorization_group_policy") | String |  |  |  | LDAP group policy name to use for user authorization. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "management_ldap.server_hosts.[].timeout") | Integer |  |  | Min: 1<br>Max: 1000 | Time in seconds (EOS default 30 seconds) to wait for a response from this LDAP server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;search</samp>](## "management_ldap.server_hosts.[].search") | Dictionary |  |  |  | Credentials used by the switch to perform LDAP search bind operations. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;username</samp>](## "management_ldap.server_hosts.[].search.username") | String | Required |  |  | LDAP username (full DN) for search bind operations (e.g., cn=ldap-admin,dc=example,dc=com). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "management_ldap.server_hosts.[].search.password") | String | Required |  |  | Password for the search bind user. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password_type</samp>](## "management_ldap.server_hosts.[].search.password_type") | String |  |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Password encryption type.<br>- 0 = clear text<br>- 7 = obfuscated<br>- 8a = AES-256-GCM encrypted.<br>Omit to provide an unobfuscated string (EOS will store it obfuscated). |
    | [<samp>&nbsp;&nbsp;group_policies</samp>](## "management_ldap.group_policies") | List, items: Dictionary |  |  |  | Named LDAP group policies that map LDAP groups to EOS roles and privilege levels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;policy</samp>](## "management_ldap.group_policies.[].policy") | String | Required, Unique |  |  | Group policy name. Referenced by server authorization_group_policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;search_filter</samp>](## "management_ldap.group_policies.[].search_filter") | Dictionary |  |  |  | LDAP search filter used to enumerate group membership. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;objectclass</samp>](## "management_ldap.group_policies.[].search_filter.objectclass") | String | Required |  |  | LDAP objectclass value to match (e.g., group). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attribute</samp>](## "management_ldap.group_policies.[].search_filter.attribute") | String | Required |  |  | LDAP attribute that holds group member DNs (e.g., member). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "management_ldap.group_policies.[].groups") | List, items: Dictionary |  |  |  | List of LDAP group-to-role mappings within this policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_ldap.group_policies.[].groups.[].name") | String | Required, Unique |  |  | LDAP group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "management_ldap.group_policies.[].groups.[].role") | String | Required |  |  | EOS role assigned to members of this LDAP group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "management_ldap.group_policies.[].groups.[].privilege") | Integer |  |  | Min: 0<br>Max: 15 | Optional privilege level (0-15) assigned alongside the role. |

=== "YAML"

    ```yaml
    management_ldap:

      # Default LDAP options applied to all servers unless overridden per host.
      server_defaults:

        # Base Distinguished Name used for LDAP searches (e.g., dc=example,dc=com).
        base_dn: <str>

        # Relative Distinguished Name attribute(s) for user lookup (e.g., cn).
        rdn_attribute_user: <str>

        # SSL profile name to secure LDAP connections.
        ssl_profile: <str>

        # LDAP group policy name to use for user authorization.
        authorization_group_policy: <str>

        # Time in seconds (EOS default 30 seconds) to wait for a response from this LDAP server.
        timeout: <int; 1-1000>

        # Credentials used by the switch to perform LDAP search bind operations.
        search:

          # LDAP username (full DN) for search bind operations (e.g., cn=ldap-admin,dc=example,dc=com).
          username: <str; required>

          # Password for the search bind user.
          password: <str; required>

          # Password encryption type.
          # - 0 = clear text
          # - 7 = obfuscated
          # - 8a = AES-256-GCM encrypted.
          # Omit to provide an unobfuscated string (EOS will store it obfuscated).
          password_type: <str; "0" | "7" | "8a">

      # List of LDAP server hosts.
      server_hosts:

          # Hostname or IP address of the LDAP server.
        - host: <str; required; unique>

          # Port of LDAP server (EOS default 389).
          port: <int; 0-65535>
          vrf: <str>

          # Base Distinguished Name used for LDAP searches (e.g., dc=example,dc=com).
          base_dn: <str>

          # Relative Distinguished Name attribute(s) for user lookup (e.g., cn).
          rdn_attribute_user: <str>

          # SSL profile name to secure LDAP connections.
          ssl_profile: <str>

          # LDAP group policy name to use for user authorization.
          authorization_group_policy: <str>

          # Time in seconds (EOS default 30 seconds) to wait for a response from this LDAP server.
          timeout: <int; 1-1000>

          # Credentials used by the switch to perform LDAP search bind operations.
          search:

            # LDAP username (full DN) for search bind operations (e.g., cn=ldap-admin,dc=example,dc=com).
            username: <str; required>

            # Password for the search bind user.
            password: <str; required>

            # Password encryption type.
            # - 0 = clear text
            # - 7 = obfuscated
            # - 8a = AES-256-GCM encrypted.
            # Omit to provide an unobfuscated string (EOS will store it obfuscated).
            password_type: <str; "0" | "7" | "8a">

      # Named LDAP group policies that map LDAP groups to EOS roles and privilege levels.
      group_policies:

          # Group policy name. Referenced by server authorization_group_policy.
        - policy: <str; required; unique>

          # LDAP search filter used to enumerate group membership.
          search_filter:

            # LDAP objectclass value to match (e.g., group).
            objectclass: <str; required>

            # LDAP attribute that holds group member DNs (e.g., member).
            attribute: <str; required>

          # List of LDAP group-to-role mappings within this policy.
          groups:

              # LDAP group name.
            - name: <str; required; unique>

              # EOS role assigned to members of this LDAP group.
              role: <str; required>

              # Optional privilege level (0-15) assigned alongside the role.
              privilege: <int; 0-15>
    ```
