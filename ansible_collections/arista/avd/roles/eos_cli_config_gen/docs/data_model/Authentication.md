---
search:
  boost: 2
---

# Authentication

## AAA Accounting

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>aaa_accounting</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;exec</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;console</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp> | String |  |  | Valid Values:<br>- none<br>- start-stop<br>- stop-only |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp> | String |  |  |  | Group Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp> | String |  |  | Valid Values:<br>- none<br>- start-stop<br>- stop-only |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp> | String |  |  |  | Group Name |
    | <samp>&nbsp;&nbsp;system</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp> | String |  |  | Valid Values:<br>- none<br>- start-stop<br>- stop-only |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp> | String |  |  |  | Group Name |
    | <samp>&nbsp;&nbsp;commands</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;console</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- commands</samp> | String |  |  |  | Privelege level 'all' or 0-15 |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp> | String |  |  | Valid Values:<br>- none<br>- start-stop<br>- stop-only |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp> | String |  |  |  | Group Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- commands</samp> | String |  |  |  | Privelege level 'all' or 0-15 |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp> | String |  |  | Valid Values:<br>- none<br>- start-stop<br>- stop-only |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp> | String |  |  |  | Group Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;commands_default</samp> | List |  |  |  | Deprecated and removed key from AVD 2.x |

=== "YAML"

    ```yaml
    aaa_accounting:
      exec:
        console:
          type: <str>
          group: <str>
        default:
          type: <str>
          group: <str>
      system:
        default:
          type: <str>
          group: <str>
      commands:
        console:
          - commands: <str>
            type: <str>
            group: <str>
            logging: <bool>
        default:
          - commands: <str>
            type: <str>
            group: <str>
            logging: <bool>
        commands_default:
    ```

## AAA Authentication

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>aaa_authentication</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;login</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp> | String |  |  |  | Login authentication method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;console</samp> | String |  |  |  | Console authentication method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
    | <samp>&nbsp;&nbsp;enable</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp> | String |  |  |  | Enable authentication method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
    | <samp>&nbsp;&nbsp;dot1x</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp> | String |  |  |  | 802.1x authentication method(s) as a string.<br>Examples:<br>- "group radius"<br>- "group MYGROUP group radius"<br> |
    | <samp>&nbsp;&nbsp;policies</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;on_failure_log</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;on_success_log</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;local</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_nopassword</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;lockout</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;failure</samp> | Integer |  |  | Min: 1<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;duration</samp> | Integer |  |  | Min: 1<br>Max: 4294967295 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;window</samp> | Integer |  |  | Min: 1<br>Max: 4294967295 |  |

=== "YAML"

    ```yaml
    aaa_authentication:
      login:
        default: <str>
        console: <str>
      enable:
        default: <str>
      dot1x:
        default: <str>
      policies:
        on_failure_log: <bool>
        on_success_log: <bool>
        local:
          allow_nopassword: <bool>
        lockout:
          failure: <int>
          duration: <int>
          window: <int>
    ```

## AAA Authorization

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>aaa_authorization</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;exec</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp> | String |  |  |  | Exec authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
    | <samp>&nbsp;&nbsp;config_commands</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;serial_console</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;commands</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;all_default</samp> | String |  |  |  | Command authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group tacacs+ group MYGROUP local<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- level</samp> | String |  |  |  | Privilege level(s) 0-15 |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp> | String |  |  |  | Command authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group tacacs+ group MYGROUP local" |

=== "YAML"

    ```yaml
    aaa_authorization:
      exec:
        default: <str>
      config_commands: <bool>
      serial_console: <bool>
      commands:
        all_default: <str>
        privilege:
          - level: <str>
            default: <str>
    ```

## AAA Root

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>aaa_root</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;secret</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp> | String |  |  |  |  |

=== "YAML"

    ```yaml
    aaa_root:
      secret:
        sha512_password: <str>
    ```

## AAA Server Groups

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>aaa_server_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String |  |  |  | Group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp> | String |  |  | Valid Values:<br>- tacacs+<br>- radius<br>- ldap |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;servers</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- server</samp> | String |  |  |  | Hostname or IP address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  | VRF name |

=== "YAML"

    ```yaml
    aaa_server_groups:
      - name: <str>
        type: <str>
        servers:
          - server: <str>
            vrf: <str>
    ```

## CVX

CVX server features are not supported on physical switches. See `management_cvx` for client configurations.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>cvx</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;shutdown</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;peer_hosts</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | IP address or hostname |
    | <samp>&nbsp;&nbsp;services</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;mcs</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redis</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp> | String |  |  |  | Hashed password using the password_type |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password_type</samp> | String |  | 7 | Valid Values:<br>- 0<br>- 7<br>- 8a |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp> | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    cvx:
      shutdown: <bool>
      peer_hosts:
        - <str>
      services:
        mcs:
          redis:
            password: <str>
            password_type: <str>
          shutdown: <bool>
    ```

## Enable Password

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>enable_password</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;hash_algorithm</samp> | String |  |  | Valid Values:<br>- md5<br>- sha512 |  |
    | <samp>&nbsp;&nbsp;key</samp> | String |  |  |  | Must be the hash of the password using the specified algorithm.<br>By default EOS salts the password, so the simplest is to generate the hash on an EOS device. |

=== "YAML"

    ```yaml
    enable_password:
      hash_algorithm: <str>
      key: <str>
    ```

## IP Radius Source Interfaces

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ip_radius_source_interfaces</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String |  |  |  | Interface Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  | VRF Name |

=== "YAML"

    ```yaml
    ip_radius_source_interfaces:
      - name: <str>
        vrf: <str>
    ```

## IP Tacacs Source Interfaces

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ip_tacacs_source_interfaces</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String |  |  |  | Interface name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  |  |

=== "YAML"

    ```yaml
    ip_tacacs_source_interfaces:
      - name: <str>
        vrf: <str>
    ```

## Local Users

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>local_users</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Username |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp> | Boolean |  |  |  | If true, the user will be removed and all other settings are ignored.<br>Useful for removing the default "admin" user.<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp> | Integer |  |  | Min: 1<br>Max: 15 | Initial privilege level with local EXEC authorization.<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;role</samp> | String |  |  |  | EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator"<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp> | String |  |  |  | SHA512 Hash of Password<br>Must be the hash of the password. By default EOS salts the password with the username, so the simplest is to generate the hash on an EOS device using the same username.<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;no_password</samp> | Boolean |  |  |  | If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user.<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ssh_key</samp> | String |  |  |  |  |

=== "YAML"

    ```yaml
    local_users:
      - name: <str>
        disabled: <bool>
        privilege: <int>
        role: <str>
        sha512_password: <str>
        no_password: <bool>
        ssh_key: <str>
    ```

## Radius Servers

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>radius_servers</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- host</samp> | String |  |  |  | Host IP address or name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;key</samp> | String |  |  |  | Encrypted key |

=== "YAML"

    ```yaml
    radius_servers:
      - host: <str>
        vrf: <str>
        key: <str>
    ```

## Roles

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>roles</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String |  |  |  | Role name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp> | Integer |  |  |  | Sequence number |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp> | String |  |  | Valid Values:<br>- permit<br>- deny |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp> | String |  |  |  | "config", "config-all", "exec" or mode key as string<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;command</samp> | String |  |  |  | Command as string |

=== "YAML"

    ```yaml
    roles:
      - name: <str>
        sequence_numbers:
          - sequence: <int>
            action: <str>
            mode: <str>
            command: <str>
    ```

## Tacacs Servers

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>tacacs_servers</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;hosts</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- host</samp> | String |  |  |  | Host IP address or name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp> | String |  |  |  | Encrypted key |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp> | String |  | 7 | Valid Values:<br>- 0<br>- 7<br>- 8a |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single_connection</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;policy_unknown_mandatory_attribute_ignore</samp> | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    tacacs_servers:
      hosts:
        - host: <str>
          vrf: <str>
          key: <str>
          key_type: <str>
          single_connection: <bool>
          timeout: <int>
      policy_unknown_mandatory_attribute_ignore: <bool>
    ```
