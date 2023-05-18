---
search:
  boost: 2
---

# Authentication

## AAA Accounting

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>aaa_accounting</samp>](## "aaa_accounting") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;exec</samp>](## "aaa_accounting.exec") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;console</samp>](## "aaa_accounting.exec.console") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.exec.console.type") | String |  |  | Valid Values:<br>- none<br>- start-stop<br>- stop-only |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.exec.console.group") | String |  |  |  | Group Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_accounting.exec.default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.exec.default.type") | String |  |  | Valid Values:<br>- none<br>- start-stop<br>- stop-only |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.exec.default.group") | String |  |  |  | Group Name |
    | [<samp>&nbsp;&nbsp;system</samp>](## "aaa_accounting.system") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_accounting.system.default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.system.default.type") | String |  |  | Valid Values:<br>- none<br>- start-stop<br>- stop-only |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.system.default.group") | String |  |  |  | Group Name |
    | [<samp>&nbsp;&nbsp;dot1x</samp>](## "aaa_accounting.dot1x") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_accounting.dot1x.default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.dot1x.default.type") | String |  |  | Valid Values:<br>- start-stop<br>- stop-only |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.dot1x.default.group") | String |  |  |  | Group Name |
    | [<samp>&nbsp;&nbsp;commands</samp>](## "aaa_accounting.commands") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;console</samp>](## "aaa_accounting.commands.console") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- commands</samp>](## "aaa_accounting.commands.console.[].commands") | String |  |  |  | Privelege level 'all' or 0-15 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.commands.console.[].type") | String |  |  | Valid Values:<br>- none<br>- start-stop<br>- stop-only |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.commands.console.[].group") | String |  |  |  | Group Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "aaa_accounting.commands.console.[].logging") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_accounting.commands.default") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- commands</samp>](## "aaa_accounting.commands.default.[].commands") | String |  |  |  | Privelege level 'all' or 0-15 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.commands.default.[].type") | String |  |  | Valid Values:<br>- none<br>- start-stop<br>- stop-only |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.commands.default.[].group") | String |  |  |  | Group Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "aaa_accounting.commands.default.[].logging") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;commands_default</samp>](## "aaa_accounting.commands.commands_default") | List |  |  |  | Deprecated and removed key from AVD 2.x |

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
      dot1x:
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
    | [<samp>aaa_authentication</samp>](## "aaa_authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;login</samp>](## "aaa_authentication.login") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_authentication.login.default") | String |  |  |  | Login authentication method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;console</samp>](## "aaa_authentication.login.console") | String |  |  |  | Console authentication method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
    | [<samp>&nbsp;&nbsp;enable</samp>](## "aaa_authentication.enable") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_authentication.enable.default") | String |  |  |  | Enable authentication method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
    | [<samp>&nbsp;&nbsp;dot1x</samp>](## "aaa_authentication.dot1x") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_authentication.dot1x.default") | String |  |  |  | 802.1x authentication method(s) as a string.<br>Examples:<br>- "group radius"<br>- "group MYGROUP group radius"<br> |
    | [<samp>&nbsp;&nbsp;policies</samp>](## "aaa_authentication.policies") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;on_failure_log</samp>](## "aaa_authentication.policies.on_failure_log") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;on_success_log</samp>](## "aaa_authentication.policies.on_success_log") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local</samp>](## "aaa_authentication.policies.local") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_nopassword</samp>](## "aaa_authentication.policies.local.allow_nopassword") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lockout</samp>](## "aaa_authentication.policies.lockout") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;failure</samp>](## "aaa_authentication.policies.lockout.failure") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;duration</samp>](## "aaa_authentication.policies.lockout.duration") | Integer |  |  | Min: 1<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;window</samp>](## "aaa_authentication.policies.lockout.window") | Integer |  |  | Min: 1<br>Max: 4294967295 |  |

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
    | [<samp>aaa_authorization</samp>](## "aaa_authorization") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;policy</samp>](## "aaa_authorization.policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local_default_role</samp>](## "aaa_authorization.policy.local_default_role") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;exec</samp>](## "aaa_authorization.exec") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_authorization.exec.default") | String |  |  |  | Exec authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
    | [<samp>&nbsp;&nbsp;config_commands</samp>](## "aaa_authorization.config_commands") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;serial_console</samp>](## "aaa_authorization.serial_console") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;dynamic</samp>](## "aaa_authorization.dynamic") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x_additional_groups</samp>](## "aaa_authorization.dynamic.dot1x_additional_groups") | List, items: String |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "aaa_authorization.dynamic.dot1x_additional_groups.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;commands</samp>](## "aaa_authorization.commands") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;all_default</samp>](## "aaa_authorization.commands.all_default") | String |  |  |  | Command authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group tacacs+ group MYGROUP local<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "aaa_authorization.commands.privilege") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- level</samp>](## "aaa_authorization.commands.privilege.[].level") | String |  |  |  | Privilege level(s) 0-15 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_authorization.commands.privilege.[].default") | String |  |  |  | Command authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group tacacs+ group MYGROUP local" |

=== "YAML"

    ```yaml
    aaa_authorization:
      policy:
        local_default_role: <str>
      exec:
        default: <str>
      config_commands: <bool>
      serial_console: <bool>
      dynamic:
        dot1x_additional_groups:
          - <str>
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
    | [<samp>aaa_root</samp>](## "aaa_root") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;secret</samp>](## "aaa_root.secret") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp>](## "aaa_root.secret.sha512_password") | String |  |  |  |  |

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
    | [<samp>aaa_server_groups</samp>](## "aaa_server_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "aaa_server_groups.[].name") | String |  |  |  | Group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_server_groups.[].type") | String |  |  | Valid Values:<br>- tacacs+<br>- radius<br>- ldap |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;servers</samp>](## "aaa_server_groups.[].servers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- server</samp>](## "aaa_server_groups.[].servers.[].server") | String |  |  |  | Hostname or IP address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "aaa_server_groups.[].servers.[].vrf") | String |  |  |  | VRF name |

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
    | [<samp>cvx</samp>](## "cvx") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;shutdown</samp>](## "cvx.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;peer_hosts</samp>](## "cvx.peer_hosts") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "cvx.peer_hosts.[].&lt;str&gt;") | String |  |  |  | IP address or hostname |
    | [<samp>&nbsp;&nbsp;services</samp>](## "cvx.services") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mcs</samp>](## "cvx.services.mcs") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redis</samp>](## "cvx.services.mcs.redis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "cvx.services.mcs.redis.password") | String |  |  |  | Hashed password using the password_type |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password_type</samp>](## "cvx.services.mcs.redis.password_type") | String |  | 7 | Valid Values:<br>- 0<br>- 7<br>- 8a |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "cvx.services.mcs.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "cvx.services.vxlan") | Dictionary |  |  |  | VXLAN Controller service |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "cvx.services.vxlan.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_mac_learning</samp>](## "cvx.services.vxlan.vtep_mac_learning") | String |  |  | Valid Values:<br>- control-plane<br>- data-plane |  |

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
        vxlan:
          shutdown: <bool>
          vtep_mac_learning: <str>
    ```

## Enable Password

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>enable_password</samp>](## "enable_password") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;hash_algorithm</samp>](## "enable_password.hash_algorithm") | String |  |  | Valid Values:<br>- md5<br>- sha512 |  |
    | [<samp>&nbsp;&nbsp;key</samp>](## "enable_password.key") | String |  |  |  | Must be the hash of the password using the specified algorithm.<br>By default EOS salts the password, so the simplest is to generate the hash on an EOS device. |

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
    | [<samp>ip_radius_source_interfaces</samp>](## "ip_radius_source_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "ip_radius_source_interfaces.[].name") | String |  |  |  | Interface Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_radius_source_interfaces.[].vrf") | String |  |  |  | VRF Name |

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
    | [<samp>ip_tacacs_source_interfaces</samp>](## "ip_tacacs_source_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "ip_tacacs_source_interfaces.[].name") | String |  |  |  | Interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_tacacs_source_interfaces.[].vrf") | String |  |  |  |  |

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
    | [<samp>local_users</samp>](## "local_users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "local_users.[].name") | String | Required, Unique |  |  | Username |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "local_users.[].disabled") | Boolean |  |  |  | If true, the user will be removed and all other settings are ignored.<br>Useful for removing the default "admin" user.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "local_users.[].privilege") | Integer |  |  | Min: 0<br>Max: 15 | Initial privilege level with local EXEC authorization.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "local_users.[].role") | String |  |  |  | EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp>](## "local_users.[].sha512_password") | String |  |  |  | SHA512 Hash of Password<br>Must be the hash of the password. By default EOS salts the password with the username, so the simplest is to generate the hash on an EOS device using the same username.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;no_password</samp>](## "local_users.[].no_password") | Boolean |  |  |  | If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssh_key</samp>](## "local_users.[].ssh_key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shell</samp>](## "local_users.[].shell") | String |  |  | Valid Values:<br>- /bin/bash<br>- /bin/sh<br>- /sbin/nologin | Specify shell for the user<br> |

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
        shell: <str>
    ```

## Radius Server

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>radius_server</samp>](## "radius_server") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;attribute_32_include_in_access_req</samp>](## "radius_server.attribute_32_include_in_access_req") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hostname</samp>](## "radius_server.attribute_32_include_in_access_req.hostname") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;format</samp>](## "radius_server.attribute_32_include_in_access_req.format") | String |  |  |  | Specify the format of the NAS-Identifier. If 'hostname' is set, this is ignored. |
    | [<samp>&nbsp;&nbsp;dynamic_authorization</samp>](## "radius_server.dynamic_authorization") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "radius_server.dynamic_authorization.port") | Integer |  |  | Min: 0<br>Max: 65535 | TCP Port |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tls_ssl_profile</samp>](## "radius_server.dynamic_authorization.tls_ssl_profile") | String |  |  |  | Name of TLS profile |
    | [<samp>&nbsp;&nbsp;hosts</samp>](## "radius_server.hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- host</samp>](## "radius_server.hosts.[].host") | String | Required, Unique |  |  | Host IP address or name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "radius_server.hosts.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "radius_server.hosts.[].timeout") | Integer |  |  | Min: 1<br>Max: 1000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;retransmit</samp>](## "radius_server.hosts.[].retransmit") | Integer |  |  | Min: 0<br>Max: 100 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "radius_server.hosts.[].key") | String |  |  |  | Encrypted key |

=== "YAML"

    ```yaml
    radius_server:
      attribute_32_include_in_access_req:
        hostname: <bool>
        format: <str>
      dynamic_authorization:
        port: <int>
        tls_ssl_profile: <str>
      hosts:
        - host: <str>
          vrf: <str>
          timeout: <int>
          retransmit: <int>
          key: <str>
    ```

## Radius Servers

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>radius_servers</samp>](## "radius_servers") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version v5.0.0. Use <samp>radius_server.hosts</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;- host</samp>](## "radius_servers.[].host") | String |  |  |  | Host IP address or name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "radius_servers.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "radius_servers.[].key") | String |  |  |  | Encrypted key |

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
    | [<samp>roles</samp>](## "roles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "roles.[].name") | String |  |  |  | Role name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "roles.[].sequence_numbers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "roles.[].sequence_numbers.[].sequence") | Integer |  |  |  | Sequence number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "roles.[].sequence_numbers.[].action") | String |  |  | Valid Values:<br>- permit<br>- deny |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "roles.[].sequence_numbers.[].mode") | String |  |  |  | "config", "config-all", "exec" or mode key as string<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;command</samp>](## "roles.[].sequence_numbers.[].command") | String |  |  |  | Command as string |

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
    | [<samp>tacacs_servers</samp>](## "tacacs_servers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;hosts</samp>](## "tacacs_servers.hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- host</samp>](## "tacacs_servers.hosts.[].host") | String |  |  |  | Host IP address or name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "tacacs_servers.hosts.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "tacacs_servers.hosts.[].key") | String |  |  |  | Encrypted key |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "tacacs_servers.hosts.[].key_type") | String |  | 7 | Valid Values:<br>- 0<br>- 7<br>- 8a |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single_connection</samp>](## "tacacs_servers.hosts.[].single_connection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "tacacs_servers.hosts.[].timeout") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;policy_unknown_mandatory_attribute_ignore</samp>](## "tacacs_servers.policy_unknown_mandatory_attribute_ignore") | Boolean |  |  |  |  |

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
