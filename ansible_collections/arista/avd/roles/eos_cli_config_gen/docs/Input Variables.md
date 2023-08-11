!!! warning
    This document describes the data model for AVD 4.x. It may or may not work in previous versions.

## AAA Accounting

### Variables

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

### YAML

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

### Variables

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

### YAML

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

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>aaa_authorization</samp>](## "aaa_authorization") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;exec</samp>](## "aaa_authorization.exec") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_authorization.exec.default") | String |  |  |  | Exec authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
| [<samp>&nbsp;&nbsp;config_commands</samp>](## "aaa_authorization.config_commands") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;serial_console</samp>](## "aaa_authorization.serial_console") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;commands</samp>](## "aaa_authorization.commands") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;all_default</samp>](## "aaa_authorization.commands.all_default") | String |  |  |  | Command authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group tacacs+ group MYGROUP local<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "aaa_authorization.commands.privilege") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- level</samp>](## "aaa_authorization.commands.privilege.[].level") | String |  |  |  | Privilege level(s) 0-15 |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_authorization.commands.privilege.[].default") | String |  |  |  | Command authorization method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group tacacs+ group MYGROUP local" |

### YAML

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

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>aaa_root</samp>](## "aaa_root") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;secret</samp>](## "aaa_root.secret") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp>](## "aaa_root.secret.sha512_password") | String |  |  |  |  |

### YAML

```yaml
aaa_root:
  secret:
    sha512_password: <str>
```

## AAA Server Groups

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>aaa_server_groups</samp>](## "aaa_server_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "aaa_server_groups.[].name") | String |  |  |  | Group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_server_groups.[].type") | String |  |  | Valid Values:<br>- tacacs+<br>- radius<br>- ldap |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;servers</samp>](## "aaa_server_groups.[].servers") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- server</samp>](## "aaa_server_groups.[].servers.[].server") | String |  |  |  | Hostname or IP address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "aaa_server_groups.[].servers.[].vrf") | String |  |  |  | VRF name |

### YAML

```yaml
aaa_server_groups:
  - name: <str>
    type: <str>
    servers:
      - server: <str>
        vrf: <str>
```

## IP Extended Access-Lists (legacy model)

### Description

AVD currently supports 2 different data models for extended ACLs:

- The legacy `access_lists` data model, for compatibility with existing deployments
- The improved `ip_access_lists` data model, for access to more EOS features

Both data models can coexists without conflicts, as different keys are used: `access_lists` vs `ip_access_lists`.
Access list names must be unique.

The legacy data model supports simplified ACL definition with `sequence` to `action` mapping:

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>access_lists</samp>](## "access_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "access_lists.[].name") | String | Required, Unique |  |  | Access-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "access_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "access_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "access_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string<br>Example: "deny ip any any" |

### YAML

```yaml
access_lists:
  - name: <str>
    counters_per_entry: <bool>
    sequence_numbers:
      - sequence: <int>
        action: <str>
```

## Aliases

### Description

Multi-line string with one or more alias commands.

Example:

```yaml
aliases: |
  alias wr copy running-config startup-config
  alias siib show ip interface brief
```
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>aliases</samp>](## "aliases") | String |  |  |  |  |

### YAML

```yaml
aliases: <str>
```

## ARP

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>arp</samp>](## "arp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;aging</samp>](## "arp.aging") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;timeout_default</samp>](## "arp.aging.timeout_default") | Integer |  |  | Min: 60<br>Max: 65535 | Timeout in seconds |

### YAML

```yaml
arp:
  aging:
    timeout_default: <int>
```

## As Path

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>as_path</samp>](## "as_path") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;regex_mode</samp>](## "as_path.regex_mode") | String |  |  | Valid Values:<br>- asn<br>- string |  |
| [<samp>&nbsp;&nbsp;access_lists</samp>](## "as_path.access_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "as_path.access_lists.[].name") | String |  |  |  | Access List Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "as_path.access_lists.[].entries") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- type</samp>](## "as_path.access_lists.[].entries.[].type") | String |  |  | Valid Values:<br>- permit<br>- deny |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match</samp>](## "as_path.access_lists.[].entries.[].match") | String |  |  |  | Regex To Match |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;origin</samp>](## "as_path.access_lists.[].entries.[].origin") | String |  | any | Valid Values:<br>- any<br>- egp<br>- igp<br>- incomplete |  |

### YAML

```yaml
as_path:
  regex_mode: <str>
  access_lists:
    - name: <str>
      entries:
        - type: <str>
          match: <str>
          origin: <str>
```

## Banners

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>banners</samp>](## "banners") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;login</samp>](## "banners.login") | String |  |  |  | Multiline string ending with EOF on the last line |
| [<samp>&nbsp;&nbsp;motd</samp>](## "banners.motd") | String |  |  |  | Multiline string ending with EOF on the last line |

### YAML

```yaml
banners:
  login: <str>
  motd: <str>
```

## BGP Groups

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>bgp_groups</samp>](## "bgp_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "bgp_groups.[].name") | String | Required, Unique |  |  | Group Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "bgp_groups.[].vrf") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "bgp_groups.[].neighbors") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "bgp_groups.[].neighbors.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_maintenance_profiles</samp>](## "bgp_groups.[].bgp_maintenance_profiles") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "bgp_groups.[].bgp_maintenance_profiles.[].&lt;str&gt;") | String |  |  |  | Profile Name |

### YAML

```yaml
bgp_groups:
  - name: <str>
    vrf: <str>
    neighbors:
      - <str>
    bgp_maintenance_profiles:
      - <str>
```

## System Boot Settings

### Description

Set the Aboot password

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>boot</samp>](## "boot") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;secret</samp>](## "boot.secret") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "boot.secret.hash_algorithm") | String |  | sha512 | Valid Values:<br>- md5<br>- sha512 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "boot.secret.key") | String |  |  |  | Hashed Password |

### YAML

```yaml
boot:
  secret:
    hash_algorithm: <str>
    key: <str>
```

## QOS Class-maps

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>class_maps</samp>](## "class_maps") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;pbr</samp>](## "class_maps.pbr") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "class_maps.pbr.[].name") | String | Required, Unique |  |  | Class-Map Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "class_maps.pbr.[].ip") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "class_maps.pbr.[].ip.access_group") | String |  |  |  | Standard Access-List Name |
| [<samp>&nbsp;&nbsp;qos</samp>](## "class_maps.qos") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "class_maps.qos.[].name") | String | Required, Unique |  |  | Class-Map Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "class_maps.qos.[].vlan") | Integer |  |  |  | VLAN value(s) or range(s) of VLAN values |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "class_maps.qos.[].cos") | Integer |  |  |  | CoS value(s) or range(s) of CoS values |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "class_maps.qos.[].ip") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "class_maps.qos.[].ip.access_group") | String |  |  |  | IPv4 Access-List Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "class_maps.qos.[].ipv6") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "class_maps.qos.[].ipv6.access_group") | String |  |  |  | IPv6 Access-List Name |

### YAML

```yaml
class_maps:
  pbr:
    - name: <str>
      ip:
        access_group: <str>
  qos:
    - name: <str>
      vlan: <int>
      cos: <int>
      ip:
        access_group: <str>
      ipv6:
        access_group: <str>
```

## Clock

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>clock</samp>](## "clock") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;timezone</samp>](## "clock.timezone") | String |  |  |  |  |

### YAML

```yaml
clock:
  timezone: <str>
```

## Community Lists (legacy model)

### Description

AVD supports 2 different data models for community lists:

- The legacy `community_lists` data model that can be used for compatibility with the existing deployments.
- The improved `ip_community_lists` data model.

Both data models can coexist without conflicts, as different keys are used: `community_lists` vs `ip_community_lists`.
Community list names must be unique.

The legacy data model supports simplified community list definition that only allows a single action to be defined as string:

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>community_lists</samp>](## "community_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "community_lists.[].name") | String | Required, Unique |  |  | Community-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "community_lists.[].action") | String | Required |  |  | Action as string<br>Example: "permit GSHUT 65123:123" |

### YAML

```yaml
community_lists:
  - name: <str>
    action: <str>
```

## Extensibility with Custom Templates

### Description

- Custom templates can be added below the playbook directory.
- If a location above the directory is desired, a symbolic link can be used.
- Example under the `playbooks` directory create symbolic link with the following command:

  ```bash
  ln -s ../../shared_repo/custom_avd_templates/ ./custom_avd_templates
  ```

- The output will be rendered at the end of the configuration.
- The order of custom templates in the list can be important if they overlap.
- It is recommenended to use a `!` delimiter at the top of each custom template.

Add `custom_templates` to group/host variables:

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>custom_templates</samp>](## "custom_templates") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "custom_templates.[].&lt;str&gt;") | String |  |  |  | Template relative path below playbook directory |

### YAML

```yaml
custom_templates:
  - <str>
```

## CVX

### Description

CVX server features are not supported on physical switches. See `management_cvx` for client configurations.
### Variables

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

### YAML

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

## Daemon TerminAttr

### Description

You can either provide a list of IPs/FQDNs to target on-premise Cloudvision cluster or use DNS name for your Cloudvision as a Service instance.
Streaming to multiple clusters both on-prem and cloud service is supported.
> Note For TerminAttr version recommendation and EOS compatibility matrix, please refer to the latest TerminAttr Release Notes
  which always contain the latest recommended versions and minimum required versions per EOS release.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>daemon_terminattr</samp>](## "daemon_terminattr") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;cvaddrs</samp>](## "daemon_terminattr.cvaddrs") | List, items: String |  |  |  | Streaming address(es) for CloudVision single cluster<br>- TCP 9910 is used for CV on-prem<br>- TCP 443 is used for CV as a Service<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "daemon_terminattr.cvaddrs.[].&lt;str&gt;") | String |  |  |  | Server address in the format `<ip/fqdn>:<port>` |
| [<samp>&nbsp;&nbsp;clusters</samp>](## "daemon_terminattr.clusters") | List, items: Dictionary |  |  |  | Multiple CloudVision clusters<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "daemon_terminattr.clusters.[].name") | String | Required, Unique |  |  | Cluster Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvaddrs</samp>](## "daemon_terminattr.clusters.[].cvaddrs") | List, items: String |  |  |  | Streaming address(es) for CloudVision cluster<br>- TCP 9910 is used for CV on-prem<br>- TCP 443 is used for CV as a Service<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "daemon_terminattr.clusters.[].cvaddrs.[].&lt;str&gt;") | String |  |  |  | Server address in the format `<ip/fqdn>:<port>` |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvauth</samp>](## "daemon_terminattr.clusters.[].cvauth") | Dictionary |  |  |  | Authentication scheme used to connect to CloudVision<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;method</samp>](## "daemon_terminattr.clusters.[].cvauth.method") | String |  |  | Valid Values:<br>- token<br>- token-secure<br>- key |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "daemon_terminattr.clusters.[].cvauth.key") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_file</samp>](## "daemon_terminattr.clusters.[].cvauth.token_file") | String |  |  |  | Token file path<br>e.g. "/tmp/token"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvobscurekeyfile</samp>](## "daemon_terminattr.clusters.[].cvobscurekeyfile") | Boolean |  |  |  | Encrypt the private key used for authentication to CloudVision<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvproxy</samp>](## "daemon_terminattr.clusters.[].cvproxy") | String |  |  |  | Proxy server through which CloudVision is reachable. Useful when the CloudVision server is hosted in the cloud.<br>The expected form is http://[user:password@]ip:port, e.g.: 'http://arista:arista@10.83.12.78:3128'. Available as of TerminAttr v1.13.0<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvsourceip</samp>](## "daemon_terminattr.clusters.[].cvsourceip") | String |  |  |  | Set source IP address in case of in-band managament<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cvvrf</samp>](## "daemon_terminattr.clusters.[].cvvrf") | String |  |  |  | The VRF to use to connect to CloudVision<br> |
| [<samp>&nbsp;&nbsp;cvauth</samp>](## "daemon_terminattr.cvauth") | Dictionary |  |  |  | Authentication scheme used to connect to CloudVision<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;method</samp>](## "daemon_terminattr.cvauth.method") | String |  |  | Valid Values:<br>- token<br>- token-secure<br>- key |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "daemon_terminattr.cvauth.key") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;token_file</samp>](## "daemon_terminattr.cvauth.token_file") | String |  |  |  | Token file path<br>e.g. "/tmp/token"<br> |
| [<samp>&nbsp;&nbsp;cvobscurekeyfile</samp>](## "daemon_terminattr.cvobscurekeyfile") | Boolean |  |  |  | Encrypt the private key used for authentication to CloudVision<br> |
| [<samp>&nbsp;&nbsp;cvproxy</samp>](## "daemon_terminattr.cvproxy") | String |  |  |  | Proxy server through which CloudVision is reachable. Useful when the CloudVision server is hosted in the cloud.<br>The expected form is http://[user:password@]ip:port, e.g.: 'http://arista:arista@10.83.12.78:3128'. Available as of TerminAttr v1.13.0<br> |
| [<samp>&nbsp;&nbsp;cvsourceip</samp>](## "daemon_terminattr.cvsourceip") | String |  |  |  | Set source IP address in case of in-band managament<br> |
| [<samp>&nbsp;&nbsp;cvvrf</samp>](## "daemon_terminattr.cvvrf") | String |  |  |  | The VRF to use to connect to CloudVision<br> |
| [<samp>&nbsp;&nbsp;cvgnmi</samp>](## "daemon_terminattr.cvgnmi") | Boolean |  |  |  | Stream states from EOS GNMI servers (Openconfig) to CloudVision. Available as of TerminAttr v1.13.1<br> |
| [<samp>&nbsp;&nbsp;disable_aaa</samp>](## "daemon_terminattr.disable_aaa") | Boolean |  |  |  | Disable AAA authorization and accounting.<br>When setting this flag, all commands pushed from CloudVision are applied directly to the CLI without authorization<br> |
| [<samp>&nbsp;&nbsp;grpcaddr</samp>](## "daemon_terminattr.grpcaddr") | String |  |  |  | Set the gRPC server address, the default is 127.0.0.1:6042<br>e.g. "MGMT/0.0.0.0:6042"<br> |
| [<samp>&nbsp;&nbsp;grpcreadonly</samp>](## "daemon_terminattr.grpcreadonly") | Boolean |  |  |  | gNMI read-only mode - Disable gnmi.Set()<br> |
| [<samp>&nbsp;&nbsp;ingestexclude</samp>](## "daemon_terminattr.ingestexclude") | String |  |  |  | Exclude paths from Sysdb on the ingest side.<br>e.g. "/Sysdb/cell/1/agent,/Sysdb/cell/2/agent"<br> |
| [<samp>&nbsp;&nbsp;smashexcludes</samp>](## "daemon_terminattr.smashexcludes") | String |  |  |  | Exclude paths from the shared memory table.<br>e.g. "ale,flexCounter,hardware,kni,pulse,strata"<br> |
| [<samp>&nbsp;&nbsp;taillogs</samp>](## "daemon_terminattr.taillogs") | String |  |  |  | Enable log file collection; /var/log/messages is streamed by default if no path is set.<br>e.g. "/var/log/messages"<br> |
| [<samp>&nbsp;&nbsp;ecodhcpaddr</samp>](## "daemon_terminattr.ecodhcpaddr") | String |  |  |  | ECO DHCP Collector address or ECO DHCP Fingerprint listening address in standalone mode (default "127.0.0.1:67")<br> |
| [<samp>&nbsp;&nbsp;ipfix</samp>](## "daemon_terminattr.ipfix") | Boolean |  |  |  | Enable IPFIX provider (TerminAttr default is true).<br>This flag is enabled by default and does not have to be added to the daemon configuration.<br> |
| [<samp>&nbsp;&nbsp;ipfixaddr</samp>](## "daemon_terminattr.ipfixaddr") | String |  |  |  | ECO IPFIX Collector address to listen on to receive IPFIX packets (TerminAttr default "127.0.0.1:4739").<br> |
| [<samp>&nbsp;&nbsp;sflow</samp>](## "daemon_terminattr.sflow") | Boolean |  |  |  | Enable sFlow provider (TerminAttr default is true).<br> |
| [<samp>&nbsp;&nbsp;sflowaddr</samp>](## "daemon_terminattr.sflowaddr") | String |  |  |  | ECO sFlow Collector address to listen on to receive sFlow packets (TerminAttr default "127.0.0.1:6343").<br> |
| [<samp>&nbsp;&nbsp;cvconfig</samp>](## "daemon_terminattr.cvconfig") | Boolean |  |  |  | Subscribe to dynamic device configuration from CloudVision (TerminAttr default is false).<br> |
| [<samp>&nbsp;&nbsp;cvcompression</samp>](## "daemon_terminattr.cvcompression") | String |  |  |  | The default compression scheme when streaming to CloudVision is gzip since TerminAttr 1.6.1 and CVP 2019.1.0.<br>There is no need to change the compression scheme.<br> |
| [<samp>&nbsp;&nbsp;ingestauth_key</samp>](## "daemon_terminattr.ingestauth_key") | String |  |  |  | Deprecated key. Use `cvauth` instead.<br> |
| [<samp>&nbsp;&nbsp;ingestgrpcurl</samp>](## "daemon_terminattr.ingestgrpcurl") | Dictionary |  |  |  | Deprecated key. Use `cvaddrs` instead.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ips</samp>](## "daemon_terminattr.ingestgrpcurl.ips") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "daemon_terminattr.ingestgrpcurl.ips.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "daemon_terminattr.ingestgrpcurl.port") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;ingestvrf</samp>](## "daemon_terminattr.ingestvrf") | String |  |  |  | Deprecated key. Use `cvvrf` instead.<br> |

### YAML

```yaml
daemon_terminattr:
  cvaddrs:
    - <str>
  clusters:
    - name: <str>
      cvaddrs:
        - <str>
      cvauth:
        method: <str>
        key: <str>
        token_file: <str>
      cvobscurekeyfile: <bool>
      cvproxy: <str>
      cvsourceip: <str>
      cvvrf: <str>
  cvauth:
    method: <str>
    key: <str>
    token_file: <str>
  cvobscurekeyfile: <bool>
  cvproxy: <str>
  cvsourceip: <str>
  cvvrf: <str>
  cvgnmi: <bool>
  disable_aaa: <bool>
  grpcaddr: <str>
  grpcreadonly: <bool>
  ingestexclude: <str>
  smashexcludes: <str>
  taillogs: <str>
  ecodhcpaddr: <str>
  ipfix: <bool>
  ipfixaddr: <str>
  sflow: <bool>
  sflowaddr: <str>
  cvconfig: <bool>
  cvcompression: <str>
  ingestauth_key: <str>
  ingestgrpcurl:
    ips:
      - <str>
    port: <int>
  ingestvrf: <str>
```

## Custom Daemons

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>daemons</samp>](## "daemons") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "daemons.[].name") | String | Required, Unique |  |  | Daemon Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;exec</samp>](## "daemons.[].exec") | String | Required |  |  | command to run as a daemon<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "daemons.[].enabled") | Boolean |  | True |  |  |

### YAML

```yaml
daemons:
  - name: <str>
    exec: <str>
    enabled: <bool>
```

## DHCP Relay

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>dhcp_relay</samp>](## "dhcp_relay") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;servers</samp>](## "dhcp_relay.servers") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "dhcp_relay.servers.[].&lt;str&gt;") | String |  |  |  | Server IP or Hostname |
| [<samp>&nbsp;&nbsp;tunnel_requests_disabled</samp>](## "dhcp_relay.tunnel_requests_disabled") | Boolean |  |  |  |  |

### YAML

```yaml
dhcp_relay:
  servers:
    - <str>
  tunnel_requests_disabled: <bool>
```

## DNS Domain

### Description

Domain Name
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>dns_domain</samp>](## "dns_domain") | String |  |  |  |  |

### YAML

```yaml
dns_domain: <str>
```

## Domain List

### Description

Search list of DNS domains
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>domain_list</samp>](## "domain_list") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "domain_list.[].&lt;str&gt;") | String |  |  |  | Domain name |

### YAML

```yaml
domain_list:
  - <str>
```

## Global 802.1x Authentication

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>dot1x</samp>](## "dot1x") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;system_auth_control</samp>](## "dot1x.system_auth_control") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;protocol_lldp_bypass</samp>](## "dot1x.protocol_lldp_bypass") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;dynamic_authorization</samp>](## "dot1x.dynamic_authorization") | Boolean |  |  |  |  |

### YAML

```yaml
dot1x:
  system_auth_control: <bool>
  protocol_lldp_bypass: <bool>
  dynamic_authorization: <bool>
```

## Dynamic Prefix Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>dynamic_prefix_lists</samp>](## "dynamic_prefix_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "dynamic_prefix_lists.[].name") | String |  |  |  | Dynamic prefix-list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;match_map</samp>](## "dynamic_prefix_lists.[].match_map") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "dynamic_prefix_lists.[].prefix_list") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "dynamic_prefix_lists.[].prefix_list.ipv4") | String |  |  |  | Prefix-list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "dynamic_prefix_lists.[].prefix_list.ipv6") | String |  |  |  | Prefix-list name |

### YAML

```yaml
dynamic_prefix_lists:
  - name: <str>
    match_map: <str>
    prefix_list:
      ipv4: <str>
      ipv6: <str>
```

## Enable Password

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>enable_password</samp>](## "enable_password") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;hash_algorithm</samp>](## "enable_password.hash_algorithm") | String |  |  | Valid Values:<br>- md5<br>- sha512 |  |
| [<samp>&nbsp;&nbsp;key</samp>](## "enable_password.key") | String |  |  |  | Must be the hash of the password using the specified algorithm.<br>By default EOS salts the password, so the simplest is to generate the hash on an EOS device. |

### YAML

```yaml
enable_password:
  hash_algorithm: <str>
  key: <str>
```

## EOS CLI

### Description

Multiline string with EOS CLI rendered directly on the root level of the final EOS configuration
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>eos_cli</samp>](## "eos_cli") | String |  |  |  |  |

### YAML

```yaml
eos_cli: <str>
```

## Errdisable

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>errdisable</samp>](## "errdisable") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;detect</samp>](## "errdisable.detect") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;causes</samp>](## "errdisable.detect.causes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "errdisable.detect.causes.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- acl<br>- arp-inspection<br>- dot1x<br>- link-change<br>- tapagg<br>- xcvr-misconfigured<br>- xcvr-overheat<br>- xcvr-power-unsupported |  |
| [<samp>&nbsp;&nbsp;recovery</samp>](## "errdisable.recovery") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;causes</samp>](## "errdisable.recovery.causes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "errdisable.recovery.causes.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- arp-inspection<br>- bpduguard<br>- dot1x<br>- hitless-reload-down<br>- lacp-rate-limit<br>- link-flap<br>- no-internal-vlan<br>- portchannelguard<br>- portsec<br>- speed-misconfigured<br>- tap-port-init<br>- tapagg<br>- uplink-failure-detection<br>- xcvr-misconfigured<br>- xcvr-overheat<br>- xcvr-power-unsupported<br>- xcvr-unsupported |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery.interval") | Integer |  | 300 | Min: 30<br>Max: 86400 | Interval in seconds |

### YAML

```yaml
errdisable:
  detect:
    causes:
      - <str>
  recovery:
    causes:
      - <str>
    interval: <int>
```

## Ethernet Interfaces

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ethernet_interfaces</samp>](## "ethernet_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ethernet_interfaces.[].name") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "ethernet_interfaces.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "ethernet_interfaces.[].shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "ethernet_interfaces.[].speed") | String |  |  |  | Speed can be interface_speed or forced interface_speed or auto interface_speed |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "ethernet_interfaces.[].mtu") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_mtu</samp>](## "ethernet_interfaces.[].l2_mtu") | Integer |  |  |  | "l2_mtu" should only be defined for platforms supporting the "l2 mtu" CLI<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "ethernet_interfaces.[].vlans") | String |  |  |  | List of switchport vlans as string<br>For a trunk port this would be a range like "1-200,300"<br>For an access port this would be a single vlan "123"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp>](## "ethernet_interfaces.[].native_vlan") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_tag</samp>](## "ethernet_interfaces.[].native_vlan_tag") | Boolean |  |  |  | If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "ethernet_interfaces.[].mode") | String |  |  | Valid Values:<br>- access<br>- dot1q-tunnel<br>- trunk<br>- trunk phone |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;phone</samp>](## "ethernet_interfaces.[].phone") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk</samp>](## "ethernet_interfaces.[].phone.trunk") | String |  |  | Valid Values:<br>- tagged<br>- untagged |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "ethernet_interfaces.[].phone.vlan") | Integer |  |  | Min: 1<br>Max: 4094 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_protocol</samp>](## "ethernet_interfaces.[].l2_protocol") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "ethernet_interfaces.[].l2_protocol.encapsulation_dot1q_vlan") | Integer |  |  |  | Vlan tag to configure on sub-interface |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "ethernet_interfaces.[].trunk_groups") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "ethernet_interfaces.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "ethernet_interfaces.[].type") | String |  |  | Valid Values:<br>- routed<br>- switched<br>- l3dot1q<br>- l2dot1q | l3dot1q and l2dot1q are used for sub-interfaces<br>The parent interface should be defined as routed<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;snmp_trap_link_change</samp>](## "ethernet_interfaces.[].snmp_trap_link_change") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;flowcontrol</samp>](## "ethernet_interfaces.[].flowcontrol") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;received</samp>](## "ethernet_interfaces.[].flowcontrol.received") | String |  |  | Valid Values:<br>- desired<br>- on<br>- off |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ethernet_interfaces.[].vrf") | String |  |  |  | VRF name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;flow_tracker</samp>](## "ethernet_interfaces.[].flow_tracker") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sampled</samp>](## "ethernet_interfaces.[].flow_tracker.sampled") | String |  |  |  | Flow tracker name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;error_correction_encoding</samp>](## "ethernet_interfaces.[].error_correction_encoding") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ethernet_interfaces.[].error_correction_encoding.enabled") | Boolean |  | True |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fire_code</samp>](## "ethernet_interfaces.[].error_correction_encoding.fire_code") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reed_solomon</samp>](## "ethernet_interfaces.[].error_correction_encoding.reed_solomon") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;link_tracking_groups</samp>](## "ethernet_interfaces.[].link_tracking_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "ethernet_interfaces.[].link_tracking_groups.[].name") | String | Required, Unique |  |  | Group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "ethernet_interfaces.[].link_tracking_groups.[].direction") | String |  |  | Valid Values:<br>- upstream<br>- downstream |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_ethernet_segment</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.identifier") | String |  |  |  | EVPN Ethernet Segment Identifier (Type 1 format) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redundancy</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.redundancy") | String |  |  | Valid Values:<br>- all-active<br>- single-active |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_election</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.algorithm") | String |  |  | Valid Values:<br>- modulus<br>- preference |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preference_value</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.preference_value") | Integer |  |  | Min: 0<br>Max: 65535 | Preference_value is only used when "algorithm" is "preference" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dont_preempt</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.dont_preempt") | Boolean |  |  |  | Dont_preempt is only used when "algorithm" is "preference" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hold_time</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.hold_time") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subsequent_hold_time</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.subsequent_hold_time") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;candidate_reachability_required</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.candidate_reachability_required") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.mpls") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_index</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.mpls.shared_index") | Integer |  |  | Min: 1<br>Max: 1024 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel_flood_filter_time</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.mpls.tunnel_flood_filter_time") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.route_target") | String |  |  |  | EVPN Route Target for ESI with format xx:xx:xx:xx:xx:xx |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "ethernet_interfaces.[].encapsulation_dot1q_vlan") | Integer |  |  |  | VLAN tag to configure on sub-interface |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_vlan</samp>](## "ethernet_interfaces.[].encapsulation_vlan") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client.dot1q") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client.dot1q.vlan") | Integer |  |  |  | Client VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client.dot1q.outer") | Integer |  |  |  | Client Outer VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client.dot1q.inner") | Integer |  |  |  | Client Inner VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unmatched</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client.unmatched") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;network</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network") | Dictionary |  |  |  | Network encapsulations are all optional and skipped if using client unmatched |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network.dot1q") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network.dot1q.vlan") | Integer |  |  |  | Network VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network.dot1q.outer") | Integer |  |  |  | Network outer VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network.dot1q.inner") | Integer |  |  |  | Network inner VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network.client") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_id</samp>](## "ethernet_interfaces.[].vlan_id") | Integer |  |  | Min: 1<br>Max: 4094 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "ethernet_interfaces.[].ip_address") | String |  |  |  | IPv4 address/mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_secondaries</samp>](## "ethernet_interfaces.[].ip_address_secondaries") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "ethernet_interfaces.[].ip_address_secondaries.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "ethernet_interfaces.[].ip_helpers") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "ethernet_interfaces.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "ethernet_interfaces.[].ip_helpers.[].source_interface") | String |  |  |  | Source interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ethernet_interfaces.[].ip_helpers.[].vrf") | String |  |  |  | VRF name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "ethernet_interfaces.[].ipv6_enable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "ethernet_interfaces.[].ipv6_address") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_link_local</samp>](## "ethernet_interfaces.[].ipv6_address_link_local") | String |  |  |  | Link local IPv6 address/mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_ra_disabled</samp>](## "ethernet_interfaces.[].ipv6_nd_ra_disabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_managed_config_flag</samp>](## "ethernet_interfaces.[].ipv6_nd_managed_config_flag") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_prefixes</samp>](## "ethernet_interfaces.[].ipv6_nd_prefixes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ipv6_prefix</samp>](## "ethernet_interfaces.[].ipv6_nd_prefixes.[].ipv6_prefix") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;valid_lifetime</samp>](## "ethernet_interfaces.[].ipv6_nd_prefixes.[].valid_lifetime") | String |  |  |  | Infinite or lifetime in seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preferred_lifetime</samp>](## "ethernet_interfaces.[].ipv6_nd_prefixes.[].preferred_lifetime") | String |  |  |  | Infinite or lifetime in seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_autoconfig_flag</samp>](## "ethernet_interfaces.[].ipv6_nd_prefixes.[].no_autoconfig_flag") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_in</samp>](## "ethernet_interfaces.[].access_group_in") | String |  |  |  | Access list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_out</samp>](## "ethernet_interfaces.[].access_group_out") | String |  |  |  | Access list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_in</samp>](## "ethernet_interfaces.[].ipv6_access_group_in") | String |  |  |  | IPv6 access list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_out</samp>](## "ethernet_interfaces.[].ipv6_access_group_out") | String |  |  |  | IPv6 access list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_access_group_in</samp>](## "ethernet_interfaces.[].mac_access_group_in") | String |  |  |  | MAC access list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_access_group_out</samp>](## "ethernet_interfaces.[].mac_access_group_out") | String |  |  |  | MAC access list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "ethernet_interfaces.[].multicast") | Dictionary |  |  |  | Boundaries can be either 1 ACL or a list of multicast IP address_range(s)/prefix but not combination of both |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "ethernet_interfaces.[].multicast.ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boundaries</samp>](## "ethernet_interfaces.[].multicast.ipv4.boundaries") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- boundary</samp>](## "ethernet_interfaces.[].multicast.ipv4.boundaries.[].boundary") | String |  |  |  | ACL name or multicast IP subnet |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;out</samp>](## "ethernet_interfaces.[].multicast.ipv4.boundaries.[].out") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "ethernet_interfaces.[].multicast.ipv4.static") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "ethernet_interfaces.[].multicast.ipv6") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boundaries</samp>](## "ethernet_interfaces.[].multicast.ipv6.boundaries") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- boundary</samp>](## "ethernet_interfaces.[].multicast.ipv6.boundaries.[].boundary") | String |  |  |  | ACL name or multicast IP subnet |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "ethernet_interfaces.[].multicast.ipv6.static") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_network_point_to_point</samp>](## "ethernet_interfaces.[].ospf_network_point_to_point") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_area</samp>](## "ethernet_interfaces.[].ospf_area") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_cost</samp>](## "ethernet_interfaces.[].ospf_cost") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication</samp>](## "ethernet_interfaces.[].ospf_authentication") | String |  |  | Valid Values:<br>- none<br>- simple<br>- message-digest |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication_key</samp>](## "ethernet_interfaces.[].ospf_authentication_key") | String |  |  |  | Encrypted password |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_message_digest_keys</samp>](## "ethernet_interfaces.[].ospf_message_digest_keys") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "ethernet_interfaces.[].ospf_message_digest_keys.[].id") | Integer | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "ethernet_interfaces.[].ospf_message_digest_keys.[].hash_algorithm") | String |  |  | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "ethernet_interfaces.[].ospf_message_digest_keys.[].key") | String |  |  |  | Encrypted password |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pim</samp>](## "ethernet_interfaces.[].pim") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "ethernet_interfaces.[].pim.ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dr_priority</samp>](## "ethernet_interfaces.[].pim.ipv4.dr_priority") | Integer |  |  | Min: 0<br>Max: 429467295 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sparse_mode</samp>](## "ethernet_interfaces.[].pim.ipv4.sparse_mode") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_security</samp>](## "ethernet_interfaces.[].mac_security") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "ethernet_interfaces.[].mac_security.profile") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;channel_group</samp>](## "ethernet_interfaces.[].channel_group") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "ethernet_interfaces.[].channel_group.id") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "ethernet_interfaces.[].channel_group.mode") | String |  |  | Valid Values:<br>- on<br>- active<br>- passive |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_enable</samp>](## "ethernet_interfaces.[].isis_enable") | String |  |  |  | ISIS instance |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_passive</samp>](## "ethernet_interfaces.[].isis_passive") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "ethernet_interfaces.[].isis_metric") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_network_point_to_point</samp>](## "ethernet_interfaces.[].isis_network_point_to_point") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "ethernet_interfaces.[].isis_circuit_type") | String |  |  | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "ethernet_interfaces.[].isis_hello_padding") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "ethernet_interfaces.[].isis_authentication_mode") | String |  |  | Valid Values:<br>- text<br>- md5 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "ethernet_interfaces.[].isis_authentication_key") | String |  |  |  | Type-7 encrypted password |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "ethernet_interfaces.[].ptp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "ethernet_interfaces.[].ptp.enable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "ethernet_interfaces.[].ptp.announce") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ethernet_interfaces.[].ptp.announce.interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "ethernet_interfaces.[].ptp.announce.timeout") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_req</samp>](## "ethernet_interfaces.[].ptp.delay_req") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_mechanism</samp>](## "ethernet_interfaces.[].ptp.delay_mechanism") | String |  |  | Valid Values:<br>- e2e<br>- p2p |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync_message</samp>](## "ethernet_interfaces.[].ptp.sync_message") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ethernet_interfaces.[].ptp.sync_message.interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "ethernet_interfaces.[].ptp.role") | String |  |  | Valid Values:<br>- master<br>- dynamic |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "ethernet_interfaces.[].ptp.vlan") | String |  |  |  | VLAN can be 'all' or list of vlans as string |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transport</samp>](## "ethernet_interfaces.[].ptp.transport") | String |  |  | Valid Values:<br>- ipv4<br>- ipv6<br>- layer2 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "ethernet_interfaces.[].profile") | String |  |  |  | Interface profile |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp>](## "ethernet_interfaces.[].storm_control") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "ethernet_interfaces.[].storm_control.all") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "ethernet_interfaces.[].storm_control.all.level") | String |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "ethernet_interfaces.[].storm_control.all.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional field and is hardware dependant |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;broadcast</samp>](## "ethernet_interfaces.[].storm_control.broadcast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "ethernet_interfaces.[].storm_control.broadcast.level") | String |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "ethernet_interfaces.[].storm_control.broadcast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional field and is hardware dependant |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "ethernet_interfaces.[].storm_control.multicast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "ethernet_interfaces.[].storm_control.multicast.level") | String |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "ethernet_interfaces.[].storm_control.multicast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional field and is hardware dependant |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unknown_unicast</samp>](## "ethernet_interfaces.[].storm_control.unknown_unicast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "ethernet_interfaces.[].storm_control.unknown_unicast.level") | String |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "ethernet_interfaces.[].storm_control.unknown_unicast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional field and is hardware dependant |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "ethernet_interfaces.[].logging") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event</samp>](## "ethernet_interfaces.[].logging.event") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_status</samp>](## "ethernet_interfaces.[].logging.event.link_status") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;congestion_drops</samp>](## "ethernet_interfaces.[].logging.event.congestion_drops") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lldp</samp>](## "ethernet_interfaces.[].lldp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transmit</samp>](## "ethernet_interfaces.[].lldp.transmit") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "ethernet_interfaces.[].lldp.receive") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ztp_vlan</samp>](## "ethernet_interfaces.[].lldp.ztp_vlan") | Integer |  |  |  | ZTP vlan number |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_private_vlan_secondary</samp>](## "ethernet_interfaces.[].trunk_private_vlan_secondary") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pvlan_mapping</samp>](## "ethernet_interfaces.[].pvlan_mapping") | String |  |  |  | List of vlans as string |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_translations</samp>](## "ethernet_interfaces.[].vlan_translations") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- from</samp>](## "ethernet_interfaces.[].vlan_translations.[].from") | String |  |  |  | List of vlans as string (only one vlan if direction is "both") |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to</samp>](## "ethernet_interfaces.[].vlan_translations.[].to") | Integer |  |  |  | VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "ethernet_interfaces.[].vlan_translations.[].direction") | String |  | both | Valid Values:<br>- in<br>- out<br>- both |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x</samp>](## "ethernet_interfaces.[].dot1x") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control</samp>](## "ethernet_interfaces.[].dot1x.port_control") | String |  |  | Valid Values:<br>- auto<br>- force-authorized<br>- force-unauthorized |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control_force_authorized_phone</samp>](## "ethernet_interfaces.[].dot1x.port_control_force_authorized_phone") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthentication</samp>](## "ethernet_interfaces.[].dot1x.reauthentication") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pae</samp>](## "ethernet_interfaces.[].dot1x.pae") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "ethernet_interfaces.[].dot1x.pae.mode") | String |  |  | Valid Values:<br>- authenticator |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_failure</samp>](## "ethernet_interfaces.[].dot1x.authentication_failure") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ethernet_interfaces.[].dot1x.authentication_failure.action") | String |  |  | Valid Values:<br>- allow<br>- drop |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_vlan</samp>](## "ethernet_interfaces.[].dot1x.authentication_failure.allow_vlan") | Integer |  |  | Min: 1<br>Max: 4094 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode</samp>](## "ethernet_interfaces.[].dot1x.host_mode") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "ethernet_interfaces.[].dot1x.host_mode.mode") | String |  |  | Valid Values:<br>- multi-host<br>- single-host |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multi_host_authenticated</samp>](## "ethernet_interfaces.[].dot1x.host_mode.multi_host_authenticated") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_based_authentication</samp>](## "ethernet_interfaces.[].dot1x.mac_based_authentication") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ethernet_interfaces.[].dot1x.mac_based_authentication.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "ethernet_interfaces.[].dot1x.mac_based_authentication.always") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode_common</samp>](## "ethernet_interfaces.[].dot1x.mac_based_authentication.host_mode_common") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "ethernet_interfaces.[].dot1x.timeout") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;idle_host</samp>](## "ethernet_interfaces.[].dot1x.timeout.idle_host") | Integer |  |  | Min: 10<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quiet_period</samp>](## "ethernet_interfaces.[].dot1x.timeout.quiet_period") | Integer |  |  | Min: 1<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_period</samp>](## "ethernet_interfaces.[].dot1x.timeout.reauth_period") | String |  |  |  | Value can be 60-4294967295 or 'server' |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_timeout_ignore</samp>](## "ethernet_interfaces.[].dot1x.timeout.reauth_timeout_ignore") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_period</samp>](## "ethernet_interfaces.[].dot1x.timeout.tx_period") | Integer |  |  | Min: 1<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthorization_request_limit</samp>](## "ethernet_interfaces.[].dot1x.reauthorization_request_limit") | Integer |  |  | Min: 1<br>Max: 10 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_profile</samp>](## "ethernet_interfaces.[].service_profile") | String |  |  |  | QOS profile |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "ethernet_interfaces.[].shape") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "ethernet_interfaces.[].shape.rate") | String |  |  |  | Rate in kbps, pps or percent<br>Supported options are platform dependent<br>Examples:<br>- "5000 kbps"<br>- "1000 pps"<br>- "20 percent"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;qos</samp>](## "ethernet_interfaces.[].qos") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trust</samp>](## "ethernet_interfaces.[].qos.trust") | String |  |  | Valid Values:<br>- dscp<br>- cos<br>- disabled |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "ethernet_interfaces.[].qos.dscp") | Integer |  |  |  | DSCP value |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "ethernet_interfaces.[].qos.cos") | Integer |  |  |  | COS value |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpdufilter</samp>](## "ethernet_interfaces.[].spanning_tree_bpdufilter") | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False<br>- true<br>- false |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpduguard</samp>](## "ethernet_interfaces.[].spanning_tree_bpduguard") | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False<br>- true<br>- false |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_guard</samp>](## "ethernet_interfaces.[].spanning_tree_guard") | String |  |  | Valid Values:<br>- loop<br>- root<br>- disabled |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_portfast</samp>](## "ethernet_interfaces.[].spanning_tree_portfast") | String |  |  | Valid Values:<br>- edge<br>- network |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vmtracer</samp>](## "ethernet_interfaces.[].vmtracer") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;priority_flow_control</samp>](## "ethernet_interfaces.[].priority_flow_control") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ethernet_interfaces.[].priority_flow_control.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priorities</samp>](## "ethernet_interfaces.[].priority_flow_control.priorities") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- priority</samp>](## "ethernet_interfaces.[].priority_flow_control.priorities.[].priority") | Integer | Required, Unique |  | Min: 0<br>Max: 7 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_drop</samp>](## "ethernet_interfaces.[].priority_flow_control.priorities.[].no_drop") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "ethernet_interfaces.[].bfd") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo</samp>](## "ethernet_interfaces.[].bfd.echo") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ethernet_interfaces.[].bfd.interval") | Integer |  |  |  | Interval in milliseconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "ethernet_interfaces.[].bfd.min_rx") | Integer |  |  |  | Rate in milliseconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "ethernet_interfaces.[].bfd.multiplier") | Integer |  |  | Min: 3<br>Max: 50 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_policy</samp>](## "ethernet_interfaces.[].service_policy") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pbr</samp>](## "ethernet_interfaces.[].service_policy.pbr") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp>](## "ethernet_interfaces.[].service_policy.pbr.input") | String |  |  |  | Policy-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "ethernet_interfaces.[].mpls") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "ethernet_interfaces.[].mpls.ip") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ldp</samp>](## "ethernet_interfaces.[].mpls.ldp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "ethernet_interfaces.[].mpls.ldp.interface") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igp_sync</samp>](## "ethernet_interfaces.[].mpls.ldp.igp_sync") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_timer</samp>](## "ethernet_interfaces.[].lacp_timer") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "ethernet_interfaces.[].lacp_timer.mode") | String |  |  | Valid Values:<br>- fast<br>- normal |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "ethernet_interfaces.[].lacp_timer.multiplier") | Integer |  |  | Min: 3<br>Max: 3000 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_port_priority</samp>](## "ethernet_interfaces.[].lacp_port_priority") | Integer |  |  | Min: 0<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;transceiver</samp>](## "ethernet_interfaces.[].transceiver") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;media</samp>](## "ethernet_interfaces.[].transceiver.media") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;override</samp>](## "ethernet_interfaces.[].transceiver.media.override") | String |  |  |  | Transceiver type |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_proxy_arp</samp>](## "ethernet_interfaces.[].ip_proxy_arp") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;traffic_policy</samp>](## "ethernet_interfaces.[].traffic_policy") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp>](## "ethernet_interfaces.[].traffic_policy.input") | String |  |  |  | Ingress traffic policy |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;output</samp>](## "ethernet_interfaces.[].traffic_policy.output") | String |  |  |  | Egress traffic policy |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "ethernet_interfaces.[].peer") | String |  |  |  | Key only used for documentation or validation purposes |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "ethernet_interfaces.[].peer_interface") | String |  |  |  | Key only used for documentation or validation purposes |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_type</samp>](## "ethernet_interfaces.[].peer_type") | String |  |  |  | Key only used for documentation or validation purposes |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "ethernet_interfaces.[].eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the ethernet interface in the final EOS configuration |

### YAML

```yaml
ethernet_interfaces:
  - name: <str>
    description: <str>
    shutdown: <bool>
    speed: <str>
    mtu: <int>
    l2_mtu: <int>
    vlans: <str>
    native_vlan: <int>
    native_vlan_tag: <bool>
    mode: <str>
    phone:
      trunk: <str>
      vlan: <int>
    l2_protocol:
      encapsulation_dot1q_vlan: <int>
    trunk_groups:
      - <str>
    type: <str>
    snmp_trap_link_change: <bool>
    flowcontrol:
      received: <str>
    vrf: <str>
    flow_tracker:
      sampled: <str>
    error_correction_encoding:
      enabled: <bool>
      fire_code: <bool>
      reed_solomon: <bool>
    link_tracking_groups:
      - name: <str>
        direction: <str>
    evpn_ethernet_segment:
      identifier: <str>
      redundancy: <str>
      designated_forwarder_election:
        algorithm: <str>
        preference_value: <int>
        dont_preempt: <bool>
        hold_time: <int>
        subsequent_hold_time: <int>
        candidate_reachability_required: <bool>
      mpls:
        shared_index: <int>
        tunnel_flood_filter_time: <int>
      route_target: <str>
    encapsulation_dot1q_vlan: <int>
    encapsulation_vlan:
      client:
        dot1q:
          vlan: <int>
          outer: <int>
          inner: <int>
        unmatched: <bool>
      network:
        dot1q:
          vlan: <int>
          outer: <int>
          inner: <int>
        client: <bool>
    vlan_id: <int>
    ip_address: <str>
    ip_address_secondaries:
      - <str>
    ip_helpers:
      - ip_helper: <str>
        source_interface: <str>
        vrf: <str>
    ipv6_enable: <bool>
    ipv6_address: <str>
    ipv6_address_link_local: <str>
    ipv6_nd_ra_disabled: <bool>
    ipv6_nd_managed_config_flag: <bool>
    ipv6_nd_prefixes:
      - ipv6_prefix: <str>
        valid_lifetime: <str>
        preferred_lifetime: <str>
        no_autoconfig_flag: <bool>
    access_group_in: <str>
    access_group_out: <str>
    ipv6_access_group_in: <str>
    ipv6_access_group_out: <str>
    mac_access_group_in: <str>
    mac_access_group_out: <str>
    multicast:
      ipv4:
        boundaries:
          - boundary: <str>
            out: <bool>
        static: <bool>
      ipv6:
        boundaries:
          - boundary: <str>
        static: <bool>
    ospf_network_point_to_point: <bool>
    ospf_area: <str>
    ospf_cost: <int>
    ospf_authentication: <str>
    ospf_authentication_key: <str>
    ospf_message_digest_keys:
      - id: <int>
        hash_algorithm: <str>
        key: <str>
    pim:
      ipv4:
        dr_priority: <int>
        sparse_mode: <bool>
    mac_security:
      profile: <str>
    channel_group:
      id: <int>
      mode: <str>
    isis_enable: <str>
    isis_passive: <bool>
    isis_metric: <int>
    isis_network_point_to_point: <bool>
    isis_circuit_type: <str>
    isis_hello_padding: <bool>
    isis_authentication_mode: <str>
    isis_authentication_key: <str>
    ptp:
      enable: <bool>
      announce:
        interval: <int>
        timeout: <int>
      delay_req: <int>
      delay_mechanism: <str>
      sync_message:
        interval: <int>
      role: <str>
      vlan: <str>
      transport: <str>
    profile: <str>
    storm_control:
      all:
        level: <str>
        unit: <str>
      broadcast:
        level: <str>
        unit: <str>
      multicast:
        level: <str>
        unit: <str>
      unknown_unicast:
        level: <str>
        unit: <str>
    logging:
      event:
        link_status: <bool>
        congestion_drops: <bool>
    lldp:
      transmit: <bool>
      receive: <bool>
      ztp_vlan: <int>
    trunk_private_vlan_secondary: <bool>
    pvlan_mapping: <str>
    vlan_translations:
      - from: <str>
        to: <int>
        direction: <str>
    dot1x:
      port_control: <str>
      port_control_force_authorized_phone: <bool>
      reauthentication: <bool>
      pae:
        mode: <str>
      authentication_failure:
        action: <str>
        allow_vlan: <int>
      host_mode:
        mode: <str>
        multi_host_authenticated: <bool>
      mac_based_authentication:
        enabled: <bool>
        always: <bool>
        host_mode_common: <bool>
      timeout:
        idle_host: <int>
        quiet_period: <int>
        reauth_period: <str>
        reauth_timeout_ignore: <bool>
        tx_period: <int>
      reauthorization_request_limit: <int>
    service_profile: <str>
    shape:
      rate: <str>
    qos:
      trust: <str>
      dscp: <int>
      cos: <int>
    spanning_tree_bpdufilter: <str>
    spanning_tree_bpduguard: <str>
    spanning_tree_guard: <str>
    spanning_tree_portfast: <str>
    vmtracer: <bool>
    priority_flow_control:
      enabled: <bool>
      priorities:
        - priority: <int>
          no_drop: <bool>
    bfd:
      echo: <bool>
      interval: <int>
      min_rx: <int>
      multiplier: <int>
    service_policy:
      pbr:
        input: <str>
    mpls:
      ip: <bool>
      ldp:
        interface: <bool>
        igp_sync: <bool>
    lacp_timer:
      mode: <str>
      multiplier: <int>
    lacp_port_priority: <int>
    transceiver:
      media:
        override: <str>
    ip_proxy_arp: <bool>
    traffic_policy:
      input: <str>
      output: <str>
    peer: <str>
    peer_interface: <str>
    peer_type: <str>
    eos_cli: <str>
```

## Event Handlers

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>event_handlers</samp>](## "event_handlers") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "event_handlers.[].name") | String | Required, Unique |  |  | Event Handler Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action_type</samp>](## "event_handlers.[].action_type") | String |  |  | Valid Values:<br>- bash<br>- increment<br>- log |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "event_handlers.[].action") | String |  |  |  | Command to execute<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "event_handlers.[].delay") | Integer |  |  |  | Event-handler delay in seconds<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger</samp>](## "event_handlers.[].trigger") | String |  |  | Valid Values:<br>- on-logging | Configure event trigger condition.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;regex</samp>](## "event_handlers.[].regex") | String |  |  |  | Regular expression to use for searching log messages. Required for on-logging trigger<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;asynchronous</samp>](## "event_handlers.[].asynchronous") | Boolean |  | False |  | Set the action to be non-blocking. |

### YAML

```yaml
event_handlers:
  - name: <str>
    action_type: <str>
    action: <str>
    delay: <int>
    trigger: <str>
    regex: <str>
    asynchronous: <bool>
```

## Event Monitor

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>event_monitor</samp>](## "event_monitor") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;enabled</samp>](## "event_monitor.enabled") | Boolean |  |  |  |  |

### YAML

```yaml
event_monitor:
  enabled: <bool>
```

## Flow Trackings

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>flow_trackings</samp>](## "flow_trackings") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- type</samp>](## "flow_trackings.[].type") | String | Required, Unique |  | Valid Values:<br>- sampled | Flow Tracking Type - only 'sampled' supported for now |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "flow_trackings.[].sample") | Integer |  |  | Min: 1<br>Max: 4294967295 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trackers</samp>](## "flow_trackings.[].trackers") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "flow_trackings.[].trackers.[].name") | String | Required, Unique |  |  | Tracker Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;record_export</samp>](## "flow_trackings.[].trackers.[].record_export") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_inactive_timeout</samp>](## "flow_trackings.[].trackers.[].record_export.on_inactive_timeout") | Integer |  |  | Min: 3000<br>Max: 900000 | Flow record inactive export timeout in milliseconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_interval</samp>](## "flow_trackings.[].trackers.[].record_export.on_interval") | Integer |  |  | Min: 1000<br>Max: 36000000 | Flow record export interval in milliseconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "flow_trackings.[].trackers.[].record_export.mpls") | Boolean |  |  |  | Export MPLS forwarding information |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exporters</samp>](## "flow_trackings.[].trackers.[].exporters") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "flow_trackings.[].trackers.[].exporters.[].name") | String | Required, Unique |  |  | Exporter Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;collector</samp>](## "flow_trackings.[].trackers.[].exporters.[].collector") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host</samp>](## "flow_trackings.[].trackers.[].exporters.[].collector.host") | String |  |  |  | Collector IPv4 address or IPv6 address or fully qualified domain name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "flow_trackings.[].trackers.[].exporters.[].collector.port") | Integer |  |  | Min: 1<br>Max: 65535 | Collector Port Number |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format</samp>](## "flow_trackings.[].trackers.[].exporters.[].format") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipfix_version</samp>](## "flow_trackings.[].trackers.[].exporters.[].format.ipfix_version") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "flow_trackings.[].trackers.[].exporters.[].local_interface") | String |  |  |  | Local Source Interface |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;template_interval</samp>](## "flow_trackings.[].trackers.[].exporters.[].template_interval") | Integer |  |  | Min: 5000<br>Max: 3600000 | Template interval in milliseconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "flow_trackings.[].shutdown") | Boolean |  | False |  |  |

### YAML

```yaml
flow_trackings:
  - type: <str>
    sample: <int>
    trackers:
      - name: <str>
        record_export:
          on_inactive_timeout: <int>
          on_interval: <int>
          mpls: <bool>
        exporters:
          - name: <str>
            collector:
              host: <str>
              port: <int>
            format:
              ipfix_version: <int>
            local_interface: <str>
            template_interval: <int>
    shutdown: <bool>
```

## Generate Default Config

### Description

The `generate_default_config` knob allows to omit default EOS configuration.
This can be useful when leveraging `eos_cli_config_gen` to generate configlets with CloudVision.

The following commands will be omitted when `generate_default_config` is set to `false`:

- RANCID Content Type
- Hostname
- Default configuration for `aaa`
- Default configuration for `enable password`
- Transceiver qsfp default mode
- End of configuration delimiter
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>generate_default_config</samp>](## "generate_default_config") | Boolean |  | True |  |  |

### YAML

```yaml
generate_default_config: <bool>
```

## Generate Device Documentation

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>generate_device_documentation</samp>](## "generate_device_documentation") | Boolean |  | True |  |  |

### YAML

```yaml
generate_device_documentation: <bool>
```

## Hardware

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>hardware</samp>](## "hardware") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;access_list</samp>](## "hardware.access_list") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mechanism</samp>](## "hardware.access_list.mechanism") | String |  |  | Valid Values:<br>- algomatch<br>- none<br>- tcam |  |
| [<samp>&nbsp;&nbsp;speed_groups</samp>](## "hardware.speed_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- speed_group</samp>](## "hardware.speed_groups.[].speed_group") | Integer | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serdes</samp>](## "hardware.speed_groups.[].serdes") | String |  |  |  | Serdes speed like "10g" or "25g" |

### YAML

```yaml
hardware:
  access_list:
    mechanism: <str>
  speed_groups:
    - speed_group: <int>
      serdes: <str>
```

## Hardware Counters

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>hardware_counters</samp>](## "hardware_counters") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;features</samp>](## "hardware_counters.features") | List, items: Dictionary |  |  |  |  |

### YAML

```yaml
hardware_counters:
  features:
```

## Interface Defaults

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>interface_defaults</samp>](## "interface_defaults") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;ethernet</samp>](## "interface_defaults.ethernet") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "interface_defaults.ethernet.shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;mtu</samp>](## "interface_defaults.mtu") | Integer |  |  |  |  |

### YAML

```yaml
interface_defaults:
  ethernet:
    shutdown: <bool>
  mtu: <int>
```

## Maintenance Interface Groups

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>interface_groups</samp>](## "interface_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "interface_groups.[].name") | String | Required, Unique |  |  | Interface-Group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "interface_groups.[].interfaces") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "interface_groups.[].interfaces.[].&lt;str&gt;") | String |  |  |  | Interface Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_maintenance_profiles</samp>](## "interface_groups.[].bgp_maintenance_profiles") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "interface_groups.[].bgp_maintenance_profiles.[].&lt;str&gt;") | String |  |  |  | Name of BGP Maintenance Profile |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_maintenance_profiles</samp>](## "interface_groups.[].interface_maintenance_profiles") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "interface_groups.[].interface_maintenance_profiles.[].&lt;str&gt;") | String |  |  |  | Name of Interface Maintenance Profile |

### YAML

```yaml
interface_groups:
  - name: <str>
    interfaces:
      - <str>
    bgp_maintenance_profiles:
      - <str>
    interface_maintenance_profiles:
      - <str>
```

## Interface Profiles

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>interface_profiles</samp>](## "interface_profiles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "interface_profiles.[].name") | String | Required, Unique |  |  | Interface-Profile Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;commands</samp>](## "interface_profiles.[].commands") | List, items: String | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "interface_profiles.[].commands.[].&lt;str&gt;") | String |  |  |  | EOS CLI interface command<br>Example: "switchport mode access" |

### YAML

```yaml
interface_profiles:
  - name: <str>
    commands:
      - <str>
```

## IP Extended Access-Lists (improved model)

### Description

AVD currently supports 2 different data models for extended ACLs:

- The legacy `access_lists` data model, for compatibility with existing deployments
- The improved `ip_access_lists` data model, for access to more EOS features

Both data models can coexists without conflicts, as different keys are used: `access_lists` vs `ip_access_lists`.
Access list names must be unique.

The improved data model has a more sophisticated design documented below:

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_access_lists</samp>](## "ip_access_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ip_access_lists.[].name") | String | Required, Unique |  |  | Access-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "ip_access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ip_access_lists.[].entries") | List, items: Dictionary |  |  |  | ACL Entries |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "ip_access_lists.[].entries.[].sequence") | Integer |  |  |  | ACL entry sequence number.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remark</samp>](## "ip_access_lists.[].entries.[].remark") | String |  |  |  | Comment up to 100 characters.<br>If remark is defined, other keys in acl entry will be ignored.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ip_access_lists.[].entries.[].action") | String |  |  | Valid Values:<br>- permit<br>- deny | ACL action.<br>Required for standard entry.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "ip_access_lists.[].entries.[].protocol") | String |  |  |  | ip, tcp, udp, icmp or other protocol name or number.<br>Required for standard entry.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "ip_access_lists.[].entries.[].source") | String |  |  |  | any, A.B.C.D/E or A.B.C.D.<br>A.B.C.D without a mask means host.<br>Required for standard entry.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ports_match</samp>](## "ip_access_lists.[].entries.[].source_ports_match") | String |  | eq | Valid Values:<br>- eq<br>- gt<br>- lt<br>- neq<br>- range |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ports</samp>](## "ip_access_lists.[].entries.[].source_ports") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "ip_access_lists.[].entries.[].source_ports.[].&lt;str&gt;") | String |  |  |  | TCP/UDP source port name or number. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "ip_access_lists.[].entries.[].destination") | String |  |  |  | any, A.B.C.D/E or A.B.C.D.<br>A.B.C.D without a mask means host.<br>Required for standard entry.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_ports_match</samp>](## "ip_access_lists.[].entries.[].destination_ports_match") | String |  | eq | Valid Values:<br>- eq<br>- gt<br>- lt<br>- neq<br>- range |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_ports</samp>](## "ip_access_lists.[].entries.[].destination_ports") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "ip_access_lists.[].entries.[].destination_ports.[].&lt;str&gt;") | String |  |  |  | TCP/UDP destination port name or number. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tcp_flags</samp>](## "ip_access_lists.[].entries.[].tcp_flags") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "ip_access_lists.[].entries.[].tcp_flags.[].&lt;str&gt;") | String |  |  |  | TCP Flag Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fragments</samp>](## "ip_access_lists.[].entries.[].fragments") | Boolean |  |  |  | Match non-head fragment packets. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log</samp>](## "ip_access_lists.[].entries.[].log") | Boolean |  |  |  | Log matches against this rule. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "ip_access_lists.[].entries.[].ttl") | Integer |  |  | Min: 0<br>Max: 254 | TTL value |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl_match</samp>](## "ip_access_lists.[].entries.[].ttl_match") | String |  | eq | Valid Values:<br>- eq<br>- gt<br>- lt<br>- neq |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_type</samp>](## "ip_access_lists.[].entries.[].icmp_type") | String |  |  |  | Message type name/number for ICMP packets. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_code</samp>](## "ip_access_lists.[].entries.[].icmp_code") | String |  |  |  | Message code for ICMP packets. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nexthop_group</samp>](## "ip_access_lists.[].entries.[].nexthop_group") | String |  |  |  | nexthop-group name. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tracked</samp>](## "ip_access_lists.[].entries.[].tracked") | Boolean |  |  |  | Match packets in existing ICMP/UDP/TCP connections. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "ip_access_lists.[].entries.[].dscp") | String |  |  |  | DSCP value or name. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_number</samp>](## "ip_access_lists.[].entries.[].vlan_number") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_inner</samp>](## "ip_access_lists.[].entries.[].vlan_inner") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_mask</samp>](## "ip_access_lists.[].entries.[].vlan_mask") | String |  |  |  | 0x000-0xFFF VLAN mask. |

### YAML

```yaml
ip_access_lists:
  - name: <str>
    counters_per_entry: <bool>
    entries:
      - sequence: <int>
        remark: <str>
        action: <str>
        protocol: <str>
        source: <str>
        source_ports_match: <str>
        source_ports:
          - <str>
        destination: <str>
        destination_ports_match: <str>
        destination_ports:
          - <str>
        tcp_flags:
          - <str>
        fragments: <bool>
        log: <bool>
        ttl: <int>
        ttl_match: <str>
        icmp_type: <str>
        icmp_code: <str>
        nexthop_group: <str>
        tracked: <bool>
        dscp: <str>
        vlan_number: <int>
        vlan_inner: <bool>
        vlan_mask: <str>
```

## IP Access Lists Max Entries

### Description

The `ip_access_lists` data model allows to limit the number of ACL entries that AVD is allowed to generate by defining `ip_access_lists_max_entries`.
Only normal entries under `ip_access_lists` will be counted, remarks will be ignored.
If the number is above the limit, the playbook will fail. This provides a simplified control over hardware utilization.
The numbers must be based on the hardware tests and AVD does not provide any guidance. Note that other EOS features may use the same hardware resources and affect the supported scale.
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_access_lists_max_entries</samp>](## "ip_access_lists_max_entries") | Integer |  |  |  |  |

### YAML

```yaml
ip_access_lists_max_entries: <int>
```

## IP Community Lists

### Description

AVD supports 2 different data models for community lists:

- The legacy `community_lists` data model that can be used for compatibility with the existing deployments.
- The improved `ip_community_lists` data model.

Both data models can coexist without conflicts, as different keys are used: `community_lists` vs `ip_community_lists`.
Community list names must be unique.

The improved data model has a better design documented below:

communities and regexp MUST not be configured together in the same entry
possible community strings are (case insensitive):
 - GSHUT
 - internet
 - local-as
 - no-advertise
 - no-export
 - <1-4294967040>
 - aa:nn

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_community_lists</samp>](## "ip_community_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ip_community_lists.[].name") | String | Required, Unique |  |  | IP Community-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ip_community_lists.[].entries") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- action</samp>](## "ip_community_lists.[].entries.[].action") | String | Required |  | Valid Values:<br>- permit<br>- deny |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;communities</samp>](## "ip_community_lists.[].entries.[].communities") | List, items: String |  |  |  | If defined, a standard community-list will be configured |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "ip_community_lists.[].entries.[].communities.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;regexp</samp>](## "ip_community_lists.[].entries.[].regexp") | String |  |  |  | Regular Expression<br>If defined, a regex community-list will be configured |

### YAML

```yaml
ip_community_lists:
  - name: <str>
    entries:
      - action: <str>
        communities:
          - <str>
        regexp: <str>
```

## IP DHCP Relay

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_dhcp_relay</samp>](## "ip_dhcp_relay") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;information_option</samp>](## "ip_dhcp_relay.information_option") | Boolean |  |  |  | Insert Option-82 information |

### YAML

```yaml
ip_dhcp_relay:
  information_option: <bool>
```

## IP Domain Lookup

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_domain_lookup</samp>](## "ip_domain_lookup") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;source_interfaces</samp>](## "ip_domain_lookup.source_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "ip_domain_lookup.source_interfaces.[].name") | String | Required, Unique |  |  | Source Interface<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_domain_lookup.source_interfaces.[].vrf") | String |  |  |  |  |

### YAML

```yaml
ip_domain_lookup:
  source_interfaces:
    - name: <str>
      vrf: <str>
```

## IP Extended Community Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_extcommunity_lists</samp>](## "ip_extcommunity_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ip_extcommunity_lists.[].name") | String | Required, Unique |  |  | Community-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ip_extcommunity_lists.[].entries") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- type</samp>](## "ip_extcommunity_lists.[].entries.[].type") | String | Required |  | Valid Values:<br>- permit<br>- deny |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;extcommunities</samp>](## "ip_extcommunity_lists.[].entries.[].extcommunities") | String | Required |  |  | Communities as string<br>Example: "65000:65000" |

### YAML

```yaml
ip_extcommunity_lists:
  - name: <str>
    entries:
      - type: <str>
        extcommunities: <str>
```

## IP Extended Community Lists RegExp

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_extcommunity_lists_regexp</samp>](## "ip_extcommunity_lists_regexp") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ip_extcommunity_lists_regexp.[].name") | String | Required, Unique |  |  | Community-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ip_extcommunity_lists_regexp.[].entries") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- type</samp>](## "ip_extcommunity_lists_regexp.[].entries.[].type") | String | Required |  | Valid Values:<br>- permit<br>- deny |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;regexp</samp>](## "ip_extcommunity_lists_regexp.[].entries.[].regexp") | String | Required |  |  | Regular Expression |

### YAML

```yaml
ip_extcommunity_lists_regexp:
  - name: <str>
    entries:
      - type: <str>
        regexp: <str>
```

## IP Hardware

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_hardware</samp>](## "ip_hardware") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;fib</samp>](## "ip_hardware.fib") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;optimize</samp>](## "ip_hardware.fib.optimize") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "ip_hardware.fib.optimize.prefixes") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "ip_hardware.fib.optimize.prefixes.profile") | String |  |  | Valid Values:<br>- internet<br>- urpf-internet |  |

### YAML

```yaml
ip_hardware:
  fib:
    optimize:
      prefixes:
        profile: <str>
```

## IP HTTP Client Source Interfaces

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_http_client_source_interfaces</samp>](## "ip_http_client_source_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ip_http_client_source_interfaces.[].name") | String |  |  |  | Interface Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_http_client_source_interfaces.[].vrf") | String |  |  |  |  |

### YAML

```yaml
ip_http_client_source_interfaces:
  - name: <str>
    vrf: <str>
```

## IP ICMP Redirect

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_icmp_redirect</samp>](## "ip_icmp_redirect") | Boolean |  |  |  |  |

### YAML

```yaml
ip_icmp_redirect: <bool>
```

## IP IGMP Snooping

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_igmp_snooping</samp>](## "ip_igmp_snooping") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;globally_enabled</samp>](## "ip_igmp_snooping.globally_enabled") | Boolean |  | True |  |  |
| [<samp>&nbsp;&nbsp;robustness_variable</samp>](## "ip_igmp_snooping.robustness_variable") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;restart_query_interval</samp>](## "ip_igmp_snooping.restart_query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;interface_restart_query</samp>](## "ip_igmp_snooping.interface_restart_query") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;fast_leave</samp>](## "ip_igmp_snooping.fast_leave") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;querier</samp>](## "ip_igmp_snooping.querier") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ip_igmp_snooping.querier.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "ip_igmp_snooping.querier.address") | String |  |  |  | IP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;query_interval</samp>](## "ip_igmp_snooping.querier.query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;max_response_time</samp>](## "ip_igmp_snooping.querier.max_response_time") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;last_member_query_interval</samp>](## "ip_igmp_snooping.querier.last_member_query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;last_member_query_count</samp>](## "ip_igmp_snooping.querier.last_member_query_count") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;startup_query_interval</samp>](## "ip_igmp_snooping.querier.startup_query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;startup_query_count</samp>](## "ip_igmp_snooping.querier.startup_query_count") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "ip_igmp_snooping.querier.version") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;proxy</samp>](## "ip_igmp_snooping.proxy") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;vlans</samp>](## "ip_igmp_snooping.vlans") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "ip_igmp_snooping.vlans.[].id") | Integer | Required, Unique |  |  | VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ip_igmp_snooping.vlans.[].enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;querier</samp>](## "ip_igmp_snooping.vlans.[].querier") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ip_igmp_snooping.vlans.[].querier.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "ip_igmp_snooping.vlans.[].querier.address") | String |  |  |  | IP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;query_interval</samp>](## "ip_igmp_snooping.vlans.[].querier.query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_response_time</samp>](## "ip_igmp_snooping.vlans.[].querier.max_response_time") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_member_query_interval</samp>](## "ip_igmp_snooping.vlans.[].querier.last_member_query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_member_query_count</samp>](## "ip_igmp_snooping.vlans.[].querier.last_member_query_count") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startup_query_interval</samp>](## "ip_igmp_snooping.vlans.[].querier.startup_query_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startup_query_count</samp>](## "ip_igmp_snooping.vlans.[].querier.startup_query_count") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "ip_igmp_snooping.vlans.[].querier.version") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_groups</samp>](## "ip_igmp_snooping.vlans.[].max_groups") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fast_leave</samp>](## "ip_igmp_snooping.vlans.[].fast_leave") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;proxy</samp>](## "ip_igmp_snooping.vlans.[].proxy") | Boolean |  |  |  | Global proxy settings should be enabled before enabling per-vlan |

### YAML

```yaml
ip_igmp_snooping:
  globally_enabled: <bool>
  robustness_variable: <int>
  restart_query_interval: <int>
  interface_restart_query: <int>
  fast_leave: <bool>
  querier:
    enabled: <bool>
    address: <str>
    query_interval: <int>
    max_response_time: <int>
    last_member_query_interval: <int>
    last_member_query_count: <int>
    startup_query_interval: <int>
    startup_query_count: <int>
    version: <int>
  proxy: <bool>
  vlans:
    - id: <int>
      enabled: <bool>
      querier:
        enabled: <bool>
        address: <str>
        query_interval: <int>
        max_response_time: <int>
        last_member_query_interval: <int>
        last_member_query_count: <int>
        startup_query_interval: <int>
        startup_query_count: <int>
        version: <int>
      max_groups: <int>
      fast_leave: <bool>
      proxy: <bool>
```

## IP Radius Source Interfaces

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_radius_source_interfaces</samp>](## "ip_radius_source_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ip_radius_source_interfaces.[].name") | String |  |  |  | Interface Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_radius_source_interfaces.[].vrf") | String |  |  |  | VRF Name |

### YAML

```yaml
ip_radius_source_interfaces:
  - name: <str>
    vrf: <str>
```

## IP Routing

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_routing</samp>](## "ip_routing") | Boolean |  |  |  |  |

### YAML

```yaml
ip_routing: <bool>
```

## IP Routing IPv6 Interfaces

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_routing_ipv6_interfaces</samp>](## "ip_routing_ipv6_interfaces") | Boolean |  |  |  |  |

### YAML

```yaml
ip_routing_ipv6_interfaces: <bool>
```

## IP SSH Client Source Interfaces

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_ssh_client_source_interfaces</samp>](## "ip_ssh_client_source_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ip_ssh_client_source_interfaces.[].name") | String |  |  |  | Interface Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_ssh_client_source_interfaces.[].vrf") | String |  | default |  |  |

### YAML

```yaml
ip_ssh_client_source_interfaces:
  - name: <str>
    vrf: <str>
```

## IP Tacacs Source Interfaces

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_tacacs_source_interfaces</samp>](## "ip_tacacs_source_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ip_tacacs_source_interfaces.[].name") | String |  |  |  | Interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_tacacs_source_interfaces.[].vrf") | String |  |  |  |  |

### YAML

```yaml
ip_tacacs_source_interfaces:
  - name: <str>
    vrf: <str>
```

## IP Virtual Router MAC Address

### Description

MAC address (hh:hh:hh:hh:hh:hh)
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ip_virtual_router_mac_address</samp>](## "ip_virtual_router_mac_address") | String |  |  |  |  |

### YAML

```yaml
ip_virtual_router_mac_address: <str>
```

## IPv6 Extended Access-Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ipv6_access_lists</samp>](## "ipv6_access_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ipv6_access_lists.[].name") | String | Required, Unique |  |  | IPv6 Access-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "ipv6_access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "ipv6_access_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "ipv6_access_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ipv6_access_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string<br>Example: "deny ipv6 any any" |

### YAML

```yaml
ipv6_access_lists:
  - name: <str>
    counters_per_entry: <bool>
    sequence_numbers:
      - sequence: <int>
        action: <str>
```

## IPv6 Hardware

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ipv6_hardware</samp>](## "ipv6_hardware") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;fib</samp>](## "ipv6_hardware.fib") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;optimize</samp>](## "ipv6_hardware.fib.optimize") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "ipv6_hardware.fib.optimize.prefixes") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "ipv6_hardware.fib.optimize.prefixes.profile") | String |  |  |  | Pre-defined profile 'internet' or user-defined profile name |

### YAML

```yaml
ipv6_hardware:
  fib:
    optimize:
      prefixes:
        profile: <str>
```

## IPv6 ICMP Redirect

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ipv6_icmp_redirect</samp>](## "ipv6_icmp_redirect") | Boolean |  |  |  |  |

### YAML

```yaml
ipv6_icmp_redirect: <bool>
```

## IPv6 Prefix Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ipv6_prefix_lists</samp>](## "ipv6_prefix_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ipv6_prefix_lists.[].name") | String | Required, Unique |  |  | Prefix-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "ipv6_prefix_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "ipv6_prefix_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ipv6_prefix_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string<br>Example: "permit 1b11:3a00:22b0:0082::/64 eq 128" |

### YAML

```yaml
ipv6_prefix_lists:
  - name: <str>
    sequence_numbers:
      - sequence: <int>
        action: <str>
```

## IPv6 Standard Access Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ipv6_standard_access_lists</samp>](## "ipv6_standard_access_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "ipv6_standard_access_lists.[].name") | String | Required, Unique |  |  | Access-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "ipv6_standard_access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "ipv6_standard_access_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "ipv6_standard_access_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ipv6_standard_access_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string<br>Example: "deny ipv6 any any" |

### YAML

```yaml
ipv6_standard_access_lists:
  - name: <str>
    counters_per_entry: <bool>
    sequence_numbers:
      - sequence: <int>
        action: <str>
```

## IPv6 Static Routes

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ipv6_static_routes</samp>](## "ipv6_static_routes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- vrf</samp>](## "ipv6_static_routes.[].vrf") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;destination_address_prefix</samp>](## "ipv6_static_routes.[].destination_address_prefix") | String |  |  |  | IPv6 Network/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "ipv6_static_routes.[].interface") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "ipv6_static_routes.[].gateway") | String |  |  |  | IPv6 Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;track_bfd</samp>](## "ipv6_static_routes.[].track_bfd") | Boolean |  |  |  | Track next-hop using BFD |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "ipv6_static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "ipv6_static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "ipv6_static_routes.[].name") | String |  |  |  | Description |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "ipv6_static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |

### YAML

```yaml
ipv6_static_routes:
  - vrf: <str>
    destination_address_prefix: <str>
    interface: <str>
    gateway: <str>
    track_bfd: <bool>
    distance: <int>
    tag: <int>
    name: <str>
    metric: <int>
```

## IPv6 Unicast Routing

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ipv6_unicast_routing</samp>](## "ipv6_unicast_routing") | Boolean |  |  |  |  |

### YAML

```yaml
ipv6_unicast_routing: <bool>
```

## LACP

### Description

Set Link Aggregation Control Protocol (LACP) parameters.
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>lacp</samp>](## "lacp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;port_id</samp>](## "lacp.port_id") | Dictionary |  |  |  | LACP port-ID range configuration. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;range</samp>](## "lacp.port_id.range") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;begin</samp>](## "lacp.port_id.range.begin") | Integer |  |  |  | Minimum LACP port-ID range. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;end</samp>](## "lacp.port_id.range.end") | Integer |  |  |  | Maximum LACP port-ID range. |
| [<samp>&nbsp;&nbsp;rate_limit</samp>](## "lacp.rate_limit") | Dictionary |  |  |  | Set LACPDU rate limit options. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "lacp.rate_limit.default") | Boolean |  |  |  | Enable LACPDU rate limiting by default on all ports. |
| [<samp>&nbsp;&nbsp;system_priority</samp>](## "lacp.system_priority") | Integer |  |  | Min: 0<br>Max: 65535 | Set local system LACP priority. |

### YAML

```yaml
lacp:
  port_id:
    range:
      begin: <int>
      end: <int>
  rate_limit:
    default: <bool>
  system_priority: <int>
```

## Link Tracking Groups

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>link_tracking_groups</samp>](## "link_tracking_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "link_tracking_groups.[].name") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;links_minimum</samp>](## "link_tracking_groups.[].links_minimum") | Integer |  |  | Min: 1<br>Max: 100000 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "link_tracking_groups.[].recovery_delay") | Integer |  |  | Min: 0<br>Max: 3600 |  |

### YAML

```yaml
link_tracking_groups:
  - name: <str>
    links_minimum: <int>
    recovery_delay: <int>
```

## LLDP

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>lldp</samp>](## "lldp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;timer</samp>](## "lldp.timer") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;timer_reinitialization</samp>](## "lldp.timer_reinitialization") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;holdtime</samp>](## "lldp.holdtime") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;management_address</samp>](## "lldp.management_address") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;vrf</samp>](## "lldp.vrf") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;receive_packet_tagged_drop</samp>](## "lldp.receive_packet_tagged_drop") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;tlvs</samp>](## "lldp.tlvs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "lldp.tlvs.[].name") | String | Required, Unique |  | Valid Values:<br>- link-aggregation<br>- management-address<br>- max-frame-size<br>- med<br>- port-description<br>- port-vlan<br>- power-via-mdi<br>- system-capabilities<br>- system-description<br>- system-name<br>- vlan-name |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transmit</samp>](## "lldp.tlvs.[].transmit") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;run</samp>](## "lldp.run") | Boolean |  |  |  |  |

### YAML

```yaml
lldp:
  timer: <int>
  timer_reinitialization: <str>
  holdtime: <int>
  management_address: <str>
  vrf: <str>
  receive_packet_tagged_drop: <str>
  tlvs:
    - name: <str>
      transmit: <bool>
  run: <bool>
```

## Load Interval

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>load_interval</samp>](## "load_interval") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;default</samp>](## "load_interval.default") | Integer |  |  |  | Default load interval in seconds |

### YAML

```yaml
load_interval:
  default: <int>
```

## Local Users

### Variables

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

### YAML

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

## Logging

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>logging</samp>](## "logging") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;console</samp>](## "logging.console") | String |  |  | Valid Values:<br>- debugging<br>- informational<br>- notifications<br>- warnings<br>- errors<br>- critical<br>- alerts<br>- emergencies<br>- disabled | Console logging severity level<br> |
| [<samp>&nbsp;&nbsp;monitor</samp>](## "logging.monitor") | String |  |  | Valid Values:<br>- debugging<br>- informational<br>- notifications<br>- warnings<br>- errors<br>- critical<br>- alerts<br>- emergencies<br>- disabled | Monitor logging severity level<br> |
| [<samp>&nbsp;&nbsp;buffered</samp>](## "logging.buffered") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "logging.buffered.size") | Integer |  |  | Min: 10<br>Max: 2147483647 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "logging.buffered.level") | String |  |  | Valid Values:<br>- alerts<br>- critical<br>- debugging<br>- emergencies<br>- errors<br>- informational<br>- notifications<br>- warnings<br>- disabled | Buffer logging severity level<br> |
| [<samp>&nbsp;&nbsp;trap</samp>](## "logging.trap") | String |  |  | Valid Values:<br>- alerts<br>- critical<br>- debugging<br>- emergencies<br>- errors<br>- informational<br>- notifications<br>- system<br>- warnings<br>- disabled | Trap logging severity level<br> |
| [<samp>&nbsp;&nbsp;synchronous</samp>](## "logging.synchronous") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "logging.synchronous.level") | String |  | critical | Valid Values:<br>- alerts<br>- all<br>- critical<br>- debugging<br>- emergencies<br>- errors<br>- informational<br>- notifications<br>- warnings<br>- disabled | Synchronous logging severity level<br> |
| [<samp>&nbsp;&nbsp;format</samp>](## "logging.format") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;timestamp</samp>](## "logging.format.timestamp") | String |  |  | Valid Values:<br>- high-resolution<br>- traditional<br>- traditional timezone<br>- traditional year<br>- traditional timezone year<br>- traditional year timezone | Timestamp format |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hostname</samp>](## "logging.format.hostname") | String |  |  | Valid Values:<br>- fqdn<br>- ipv4 | Hostname format |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "logging.format.sequence_numbers") | Boolean |  |  |  | Add sequence numbers to log messages<br> |
| [<samp>&nbsp;&nbsp;facility</samp>](## "logging.facility") | String |  |  | Valid Values:<br>- auth<br>- cron<br>- daemon<br>- kern<br>- local0<br>- local1<br>- local2<br>- local3<br>- local4<br>- local5<br>- local6<br>- local7<br>- lpr<br>- mail<br>- news<br>- sys9<br>- sys10<br>- sys11<br>- sys12<br>- sys13<br>- sys14<br>- syslog<br>- user<br>- uucp |  |
| [<samp>&nbsp;&nbsp;source_interface</samp>](## "logging.source_interface") | String |  |  |  | Source Interface Name |
| [<samp>&nbsp;&nbsp;vrfs</samp>](## "logging.vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "logging.vrfs.[].name") | String | Required, Unique |  |  | VRF name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "logging.vrfs.[].source_interface") | String |  |  |  | Source interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hosts</samp>](## "logging.vrfs.[].hosts") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "logging.vrfs.[].hosts.[].name") | String | Required, Unique |  |  | Syslog server name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "logging.vrfs.[].hosts.[].protocol") | String |  | udp | Valid Values:<br>- tcp<br>- udp |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ports</samp>](## "logging.vrfs.[].hosts.[].ports") | List, items: Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;int&gt;</samp>](## "logging.vrfs.[].hosts.[].ports.[].&lt;int&gt;") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;policy</samp>](## "logging.policy") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;match</samp>](## "logging.policy.match") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_lists</samp>](## "logging.policy.match.match_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "logging.policy.match.match_lists.[].name") | String | Required, Unique |  |  | Match list |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "logging.policy.match.match_lists.[].action") | String |  |  | Valid Values:<br>- discard |  |

### YAML

```yaml
logging:
  console: <str>
  monitor: <str>
  buffered:
    size: <int>
    level: <str>
  trap: <str>
  synchronous:
    level: <str>
  format:
    timestamp: <str>
    hostname: <str>
    sequence_numbers: <bool>
  facility: <str>
  source_interface: <str>
  vrfs:
    - name: <str>
      source_interface: <str>
      hosts:
        - name: <str>
          protocol: <str>
          ports:
            - <int>
  policy:
    match:
      match_lists:
        - name: <str>
          action: <str>
```

## Loopback Interfaces

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>loopback_interfaces</samp>](## "loopback_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "loopback_interfaces.[].name") | String | Required, Unique |  |  | Loopback interface name e.g. "Loopback0" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "loopback_interfaces.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "loopback_interfaces.[].shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "loopback_interfaces.[].vrf") | String |  |  |  | VRF name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "loopback_interfaces.[].ip_address") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_secondaries</samp>](## "loopback_interfaces.[].ip_address_secondaries") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "loopback_interfaces.[].ip_address_secondaries.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "loopback_interfaces.[].ipv6_enable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "loopback_interfaces.[].ipv6_address") | String |  |  |  | IPv6_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_proxy_arp</samp>](## "loopback_interfaces.[].ip_proxy_arp") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_area</samp>](## "loopback_interfaces.[].ospf_area") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "loopback_interfaces.[].mpls") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ldp</samp>](## "loopback_interfaces.[].mpls.ldp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "loopback_interfaces.[].mpls.ldp.interface") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_enable</samp>](## "loopback_interfaces.[].isis_enable") | String |  |  |  | ISIS instance name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_passive</samp>](## "loopback_interfaces.[].isis_passive") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "loopback_interfaces.[].isis_metric") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_network_point_to_point</samp>](## "loopback_interfaces.[].isis_network_point_to_point") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;node_segment</samp>](## "loopback_interfaces.[].node_segment") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_index</samp>](## "loopback_interfaces.[].node_segment.ipv4_index") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_index</samp>](## "loopback_interfaces.[].node_segment.ipv6_index") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "loopback_interfaces.[].eos_cli") | String |  |  |  | EOS CLI rendered directly on the loopback interface in the final EOS configuration |

### YAML

```yaml
loopback_interfaces:
  - name: <str>
    description: <str>
    shutdown: <bool>
    vrf: <str>
    ip_address: <str>
    ip_address_secondaries:
      - <str>
    ipv6_enable: <bool>
    ipv6_address: <str>
    ip_proxy_arp: <bool>
    ospf_area: <str>
    mpls:
      ldp:
        interface: <bool>
    isis_enable: <str>
    isis_passive: <bool>
    isis_metric: <int>
    isis_network_point_to_point: <bool>
    node_segment:
      ipv4_index: <int>
      ipv6_index: <int>
    eos_cli: <str>
```

## MAC Access Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mac_access_lists</samp>](## "mac_access_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "mac_access_lists.[].name") | String | Required, Unique |  |  | MAC Access-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "mac_access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "mac_access_lists.[].entries") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "mac_access_lists.[].entries.[].sequence") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "mac_access_lists.[].entries.[].action") | String |  |  |  |  |

### YAML

```yaml
mac_access_lists:
  - name: <str>
    counters_per_entry: <bool>
    entries:
      - sequence: <int>
        action: <str>
```

## MAC Address Table

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mac_address_table</samp>](## "mac_address_table") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;aging_time</samp>](## "mac_address_table.aging_time") | Integer |  |  |  | Aging time in seconds |
| [<samp>&nbsp;&nbsp;notification_host_flap</samp>](## "mac_address_table.notification_host_flap") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "mac_address_table.notification_host_flap.logging") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "mac_address_table.notification_host_flap.detection") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;window</samp>](## "mac_address_table.notification_host_flap.detection.window") | Integer |  |  | Min: 2<br>Max: 300 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;moves</samp>](## "mac_address_table.notification_host_flap.detection.moves") | Integer |  |  | Min: 2<br>Max: 10 |  |

### YAML

```yaml
mac_address_table:
  aging_time: <int>
  notification_host_flap:
    logging: <bool>
    detection:
      window: <int>
      moves: <int>
```

## MAC Security (MACsec)

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mac_security</samp>](## "mac_security") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;license</samp>](## "mac_security.license") | Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;license_name</samp>](## "mac_security.license.license_name") | String | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;license_key</samp>](## "mac_security.license.license_key") | String | Required |  |  |  |
| [<samp>&nbsp;&nbsp;fips_restrictions</samp>](## "mac_security.fips_restrictions") | Boolean | Required |  |  |  |
| [<samp>&nbsp;&nbsp;profiles</samp>](## "mac_security.profiles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "mac_security.profiles.[].name") | String | Required, Unique |  |  | Profile-Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cipher</samp>](## "mac_security.profiles.[].cipher") | String |  |  | Valid Values:<br>- aes128-gcm<br>- aes128-gcm-xpn<br>- aes256-gcm<br>- aes256-gcm-xpn |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connection_keys</samp>](## "mac_security.profiles.[].connection_keys") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "mac_security.profiles.[].connection_keys.[].id") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encrypted_key</samp>](## "mac_security.profiles.[].connection_keys.[].encrypted_key") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fallback</samp>](## "mac_security.profiles.[].connection_keys.[].fallback") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mka</samp>](## "mac_security.profiles.[].mka") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_server_priority</samp>](## "mac_security.profiles.[].mka.key_server_priority") | Integer |  |  | Min: 0<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session</samp>](## "mac_security.profiles.[].mka.session") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rekey_period</samp>](## "mac_security.profiles.[].mka.session.rekey_period") | Integer |  |  | Min: 30<br>Max: 100000 | Rekey period in seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sci</samp>](## "mac_security.profiles.[].sci") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l2_protocols</samp>](## "mac_security.profiles.[].l2_protocols") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ethernet_flow_control</samp>](## "mac_security.profiles.[].l2_protocols.ethernet_flow_control") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "mac_security.profiles.[].l2_protocols.ethernet_flow_control.mode") | String | Required |  | Valid Values:<br>- encrypt<br>- bypass |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lldp</samp>](## "mac_security.profiles.[].l2_protocols.lldp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "mac_security.profiles.[].l2_protocols.lldp.mode") | String | Required |  | Valid Values:<br>- bypass<br>- bypass unauthorized |  |

### YAML

```yaml
mac_security:
  license:
    license_name: <str>
    license_key: <str>
  fips_restrictions: <bool>
  profiles:
    - name: <str>
      cipher: <str>
      connection_keys:
        - id: <str>
          encrypted_key: <str>
          fallback: <bool>
      mka:
        key_server_priority: <int>
        session:
          rekey_period: <int>
      sci: <bool>
      l2_protocols:
        ethernet_flow_control:
          mode: <str>
        lldp:
          mode: <str>
```

## Maintenance Mode

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>maintenance</samp>](## "maintenance") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;default_interface_profile</samp>](## "maintenance.default_interface_profile") | String |  |  |  | Name of default Interface Profile<br> |
| [<samp>&nbsp;&nbsp;default_bgp_profile</samp>](## "maintenance.default_bgp_profile") | String |  |  |  | Name of default BGP Profile<br> |
| [<samp>&nbsp;&nbsp;default_unit_profile</samp>](## "maintenance.default_unit_profile") | String |  |  |  | Name of default Unit Profile<br> |
| [<samp>&nbsp;&nbsp;interface_profiles</samp>](## "maintenance.interface_profiles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "maintenance.interface_profiles.[].name") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_monitoring</samp>](## "maintenance.interface_profiles.[].rate_monitoring") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;load_interval</samp>](## "maintenance.interface_profiles.[].rate_monitoring.load_interval") | Integer |  |  |  | Load Interval in Seconds<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "maintenance.interface_profiles.[].rate_monitoring.threshold") | Integer |  |  |  | Threshold in kbps<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "maintenance.interface_profiles.[].shutdown") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_delay</samp>](## "maintenance.interface_profiles.[].shutdown.max_delay") | Integer |  |  |  | Max delay in seconds<br> |
| [<samp>&nbsp;&nbsp;bgp_profiles</samp>](## "maintenance.bgp_profiles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "maintenance.bgp_profiles.[].name") | String | Required, Unique |  |  | BGP Profile Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;initiator</samp>](## "maintenance.bgp_profiles.[].initiator") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_inout</samp>](## "maintenance.bgp_profiles.[].initiator.route_map_inout") | String |  |  |  | Route Map |
| [<samp>&nbsp;&nbsp;unit_profiles</samp>](## "maintenance.unit_profiles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "maintenance.unit_profiles.[].name") | String | Required, Unique |  |  | Unit Profile Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_boot</samp>](## "maintenance.unit_profiles.[].on_boot") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;duration</samp>](## "maintenance.unit_profiles.[].on_boot.duration") | Integer |  |  | Min: 300<br>Max: 3600 | On-boot in seconds<br> |
| [<samp>&nbsp;&nbsp;units</samp>](## "maintenance.units") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "maintenance.units.[].name") | String | Required, Unique |  |  | Unit Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quiesce</samp>](## "maintenance.units.[].quiesce") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "maintenance.units.[].profile") | String |  |  |  | Name of Unit Profile<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "maintenance.units.[].groups") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_groups</samp>](## "maintenance.units.[].groups.bgp_groups") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "maintenance.units.[].groups.bgp_groups.[].&lt;str&gt;") | String |  |  |  | Name of BGP Group<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface_groups</samp>](## "maintenance.units.[].groups.interface_groups") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "maintenance.units.[].groups.interface_groups.[].&lt;str&gt;") | String |  |  |  | Name of Interface Group |

### YAML

```yaml
maintenance:
  default_interface_profile: <str>
  default_bgp_profile: <str>
  default_unit_profile: <str>
  interface_profiles:
    - name: <str>
      rate_monitoring:
        load_interval: <int>
        threshold: <int>
      shutdown:
        max_delay: <int>
  bgp_profiles:
    - name: <str>
      initiator:
        route_map_inout: <str>
  unit_profiles:
    - name: <str>
      on_boot:
        duration: <int>
  units:
    - name: <str>
      quiesce: <bool>
      profile: <str>
      groups:
        bgp_groups:
          - <str>
        interface_groups:
          - <str>
```

## Management API Gnmi

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>management_api_gnmi</samp>](## "management_api_gnmi") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;provider</samp>](## "management_api_gnmi.provider") | String |  | eos-native |  |  |
| [<samp>&nbsp;&nbsp;transport</samp>](## "management_api_gnmi.transport") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;grpc</samp>](## "management_api_gnmi.transport.grpc") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_api_gnmi.transport.grpc.[].name") | String |  |  |  | Transport name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ssl_profile</samp>](## "management_api_gnmi.transport.grpc.[].ssl_profile") | String |  |  |  | SSL profile name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_api_gnmi.transport.grpc.[].vrf") | String |  |  |  | VRF name is optional |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;notification_timestamp</samp>](## "management_api_gnmi.transport.grpc.[].notification_timestamp") | String |  |  | Valid Values:<br>- send-time<br>- last-change-time | Per the GNMI specification, the default timestamp field of a notification message is set to be<br>the time at which the value of the underlying data source changes or when the reported event takes place.<br>In order to facilitate integration in legacy environments oriented around polling style operations,<br>an option to support overriding the timestamp field to the send-time is available from EOS 4.27.0F.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_access_group</samp>](## "management_api_gnmi.transport.grpc.[].ip_access_group") | String |  |  |  | ACL name |
| [<samp>&nbsp;&nbsp;enable_vrfs</samp>](## "management_api_gnmi.enable_vrfs") | List, items: Dictionary |  |  |  | Enable VRFs will be deprecated in AVD v4.0.<br>These should not be mixed with the new keys above.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_api_gnmi.enable_vrfs.[].name") | String | Required, Unique |  |  | VRF name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "management_api_gnmi.enable_vrfs.[].access_group") | String |  |  |  | Standard IPv4 ACL name |
| [<samp>&nbsp;&nbsp;octa</samp>](## "management_api_gnmi.octa") | Dictionary |  |  |  | Octa key will be deprecated in AVD v4.0.<br>These should not be mixed with the new keys above.<br>Octa activates `eos-native` provider and it is the only provider currently supported by EOS. |

### YAML

```yaml
management_api_gnmi:
  provider: <str>
  transport:
    grpc:
      - name: <str>
        ssl_profile: <str>
        vrf: <str>
        notification_timestamp: <str>
        ip_access_group: <str>
  enable_vrfs:
    - name: <str>
      access_group: <str>
  octa:
```

## Management API HTTP

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>management_api_http</samp>](## "management_api_http") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;enable_http</samp>](## "management_api_http.enable_http") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;enable_https</samp>](## "management_api_http.enable_https") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;https_ssl_profile</samp>](## "management_api_http.https_ssl_profile") | String |  |  |  | SSL Profile Name |
| [<samp>&nbsp;&nbsp;default_services</samp>](## "management_api_http.default_services") | Boolean |  |  |  | Enable default services: capi-doc and tapagg |
| [<samp>&nbsp;&nbsp;enable_vrfs</samp>](## "management_api_http.enable_vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_api_http.enable_vrfs.[].name") | String | Required, Unique |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "management_api_http.enable_vrfs.[].access_group") | String |  |  |  | Standard IPv4 ACL name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group</samp>](## "management_api_http.enable_vrfs.[].ipv6_access_group") | String |  |  |  | Standard IPv6 ACL name |
| [<samp>&nbsp;&nbsp;protocol_https_certificate</samp>](## "management_api_http.protocol_https_certificate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;certificate</samp>](## "management_api_http.protocol_https_certificate.certificate") | String |  |  |  | Name of certificate; private key must also be specified |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;private_key</samp>](## "management_api_http.protocol_https_certificate.private_key") | String |  |  |  | Name of private key; certificate must also be specified |

### YAML

```yaml
management_api_http:
  enable_http: <bool>
  enable_https: <bool>
  https_ssl_profile: <str>
  default_services: <bool>
  enable_vrfs:
    - name: <str>
      access_group: <str>
      ipv6_access_group: <str>
  protocol_https_certificate:
    certificate: <str>
    private_key: <str>
```

## Management API Models

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>management_api_models</samp>](## "management_api_models") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;providers</samp>](## "management_api_models.providers") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_api_models.providers.[].name") | String |  |  | Valid Values:<br>- sysdb<br>- smash |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;paths</samp>](## "management_api_models.providers.[].paths") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- path</samp>](## "management_api_models.providers.[].paths.[].path") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "management_api_models.providers.[].paths.[].disabled") | Boolean |  | False |  |  |

### YAML

```yaml
management_api_models:
  providers:
    - name: <str>
      paths:
        - path: <str>
          disabled: <bool>
```

## Management Console

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>management_console</samp>](## "management_console") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;idle_timeout</samp>](## "management_console.idle_timeout") | Integer |  |  | Min: 0<br>Max: 86400 |  |

### YAML

```yaml
management_console:
  idle_timeout: <int>
```

## Management CVX

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>management_cvx</samp>](## "management_cvx") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;shutdown</samp>](## "management_cvx.shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;server_hosts</samp>](## "management_cvx.server_hosts") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "management_cvx.server_hosts.[].&lt;str&gt;") | String |  |  |  | IP or hostname |
| [<samp>&nbsp;&nbsp;source_interface</samp>](## "management_cvx.source_interface") | String |  |  |  | Interface name |

### YAML

```yaml
management_cvx:
  shutdown: <bool>
  server_hosts:
    - <str>
  source_interface: <str>
```

## Management Defaults

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>management_defaults</samp>](## "management_defaults") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;secret</samp>](## "management_defaults.secret") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hash</samp>](## "management_defaults.secret.hash") | String |  |  | Valid Values:<br>- md5<br>- sha512 |  |

### YAML

```yaml
management_defaults:
  secret:
    hash: <str>
```

## Management Interfaces

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>management_interfaces</samp>](## "management_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "management_interfaces.[].name") | String | Required, Unique |  |  | Management Interface Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "management_interfaces.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "management_interfaces.[].shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "management_interfaces.[].mtu") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_interfaces.[].vrf") | String |  |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "management_interfaces.[].ip_address") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "management_interfaces.[].ipv6_enable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "management_interfaces.[].ipv6_address") | String |  |  |  | IPv6_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "management_interfaces.[].type") | String |  | oob | Valid Values:<br>- oob<br>- inband | For documentation purposes only |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "management_interfaces.[].gateway") | String |  |  |  | IPv4 address of default gateway in management VRF |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_gateway</samp>](## "management_interfaces.[].ipv6_gateway") | String |  |  |  | IPv6 address of default gateway in management VRF |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "management_interfaces.[].mac_address") | String |  |  |  | MAC address |

### YAML

```yaml
management_interfaces:
  - name: <str>
    description: <str>
    shutdown: <bool>
    mtu: <int>
    vrf: <str>
    ip_address: <str>
    ipv6_enable: <bool>
    ipv6_address: <str>
    type: <str>
    gateway: <str>
    ipv6_gateway: <str>
    mac_address: <str>
```

## Management Security

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>management_security</samp>](## "management_security") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;entropy_source</samp>](## "management_security.entropy_source") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;password</samp>](## "management_security.password") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;minimum_length</samp>](## "management_security.password.minimum_length") | Integer |  |  | Min: 1<br>Max: 32 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encryption_key_common</samp>](## "management_security.password.encryption_key_common") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encryption_reversible</samp>](## "management_security.password.encryption_reversible") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;ssl_profiles</samp>](## "management_security.ssl_profiles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_security.ssl_profiles.[].name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tls_versions</samp>](## "management_security.ssl_profiles.[].tls_versions") | String |  |  |  | List of allowed TLS versions as string<br>Examples:<br>  - "1.0"<br>  - "1.0 1.1"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cipher_list</samp>](## "management_security.ssl_profiles.[].cipher_list") | String |  |  |  | cipher_list syntax follows the openssl cipher strings format.<br>Colon (:) separated list of allowed ciphers as a string<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;certificate</samp>](## "management_security.ssl_profiles.[].certificate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;file</samp>](## "management_security.ssl_profiles.[].certificate.file") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "management_security.ssl_profiles.[].certificate.key") | String |  |  |  |  |

### YAML

```yaml
management_security:
  entropy_source: <str>
  password:
    minimum_length: <int>
    encryption_key_common: <bool>
    encryption_reversible: <str>
  ssl_profiles:
    - name: <str>
      tls_versions: <str>
      cipher_list: <str>
      certificate:
        file: <str>
        key: <str>
```

## Management SSH

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>management_ssh</samp>](## "management_ssh") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;access_groups</samp>](## "management_ssh.access_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_ssh.access_groups.[].name") | String |  |  |  | Standard ACL Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_ssh.access_groups.[].vrf") | String |  |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;ipv6_access_groups</samp>](## "management_ssh.ipv6_access_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_ssh.ipv6_access_groups.[].name") | String |  |  |  | Standard ACL Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_ssh.ipv6_access_groups.[].vrf") | String |  |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;idle_timeout</samp>](## "management_ssh.idle_timeout") | Integer |  |  | Min: 0<br>Max: 86400 | Idle timeout in minutes |
| [<samp>&nbsp;&nbsp;cipher</samp>](## "management_ssh.cipher") | List, items: String |  |  |  | Cryptographic ciphers for SSH to use |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "management_ssh.cipher.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;key_exchange</samp>](## "management_ssh.key_exchange") | List, items: String |  |  |  | Cryptographic key exchange methods for SSH to use |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "management_ssh.key_exchange.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;mac</samp>](## "management_ssh.mac") | List, items: String |  |  |  | Cryptographic MAC algorithms for SSH to use |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "management_ssh.mac.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;hostkey</samp>](## "management_ssh.hostkey") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;server</samp>](## "management_ssh.hostkey.server") | List, items: String |  |  |  | SSH host key settings |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "management_ssh.hostkey.server.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;enable</samp>](## "management_ssh.enable") | Boolean |  |  |  | Enable SSH daemon |
| [<samp>&nbsp;&nbsp;connection</samp>](## "management_ssh.connection") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "management_ssh.connection.limit") | Integer |  |  | Min: 1<br>Max: 100 | Maximum total number of SSH sessions to device |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;per_host</samp>](## "management_ssh.connection.per_host") | Integer |  |  | Min: 1<br>Max: 20 | Maximum number of SSH sessions to device from a single host |
| [<samp>&nbsp;&nbsp;vrfs</samp>](## "management_ssh.vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_ssh.vrfs.[].name") | String | Required, Unique |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "management_ssh.vrfs.[].enable") | Boolean |  |  |  | Enable SSH in VRF |
| [<samp>&nbsp;&nbsp;log_level</samp>](## "management_ssh.log_level") | String |  |  |  | SSH daemon log level |

### YAML

```yaml
management_ssh:
  access_groups:
    - name: <str>
      vrf: <str>
  ipv6_access_groups:
    - name: <str>
      vrf: <str>
  idle_timeout: <int>
  cipher:
    - <str>
  key_exchange:
    - <str>
  mac:
    - <str>
  hostkey:
    server:
      - <str>
  enable: <bool>
  connection:
    limit: <int>
    per_host: <int>
  vrfs:
    - name: <str>
      enable: <bool>
  log_level: <str>
```

## Management Tech Support

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>management_tech_support</samp>](## "management_tech_support") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;policy_show_tech_support</samp>](## "management_tech_support.policy_show_tech_support") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;exclude_commands</samp>](## "management_tech_support.policy_show_tech_support.exclude_commands") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- command</samp>](## "management_tech_support.policy_show_tech_support.exclude_commands.[].command") | String |  |  |  | Command to exclude from tech-support |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "management_tech_support.policy_show_tech_support.exclude_commands.[].type") | String |  | text | Valid Values:<br>- text<br>- json | The supported values for type are platform dependent. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;include_commands</samp>](## "management_tech_support.policy_show_tech_support.include_commands") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- command</samp>](## "management_tech_support.policy_show_tech_support.include_commands.[].command") | String |  |  |  | Command to include in tech-support |

### YAML

```yaml
management_tech_support:
  policy_show_tech_support:
    exclude_commands:
      - command: <str>
        type: <str>
    include_commands:
      - command: <str>
```

## Match Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>match_list_input</samp>](## "match_list_input") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;string</samp>](## "match_list_input.string") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "match_list_input.string.[].name") | String | Required, Unique |  |  | Match-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "match_list_input.string.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "match_list_input.string.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_regex</samp>](## "match_list_input.string.[].sequence_numbers.[].match_regex") | String | Required |  |  | Regular Expression |

### YAML

```yaml
match_list_input:
  string:
    - name: <str>
      sequence_numbers:
        - sequence: <int>
          match_regex: <str>
```

## MCS Client

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mcs_client</samp>](## "mcs_client") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;shutdown</samp>](## "mcs_client.shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;cvx_secondary</samp>](## "mcs_client.cvx_secondary") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "mcs_client.cvx_secondary.name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "mcs_client.cvx_secondary.shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;server_hosts</samp>](## "mcs_client.cvx_secondary.server_hosts") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "mcs_client.cvx_secondary.server_hosts.[].&lt;str&gt;") | String |  |  |  | IP or hostname |

### YAML

```yaml
mcs_client:
  shutdown: <bool>
  cvx_secondary:
    name: <str>
    shutdown: <bool>
    server_hosts:
      - <str>
```

## Multi-Chassis Link Aggregation (MLAG) Configuration

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mlag_configuration</samp>](## "mlag_configuration") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;domain_id</samp>](## "mlag_configuration.domain_id") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;heartbeat_interval</samp>](## "mlag_configuration.heartbeat_interval") | Integer |  |  |  | Heartbeat interval in milliseconds |
| [<samp>&nbsp;&nbsp;local_interface</samp>](## "mlag_configuration.local_interface") | String |  |  |  | Local Interface Name |
| [<samp>&nbsp;&nbsp;peer_address</samp>](## "mlag_configuration.peer_address") | String |  |  |  | IPv4 Address |
| [<samp>&nbsp;&nbsp;peer_address_heartbeat</samp>](## "mlag_configuration.peer_address_heartbeat") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_ip</samp>](## "mlag_configuration.peer_address_heartbeat.peer_ip") | String |  |  |  | IPv4 Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "mlag_configuration.peer_address_heartbeat.vrf") | String |  |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;dual_primary_detection_delay</samp>](## "mlag_configuration.dual_primary_detection_delay") | Integer |  |  | Min: 0<br>Max: 86400 | Delay in seconds |
| [<samp>&nbsp;&nbsp;dual_primary_recovery_delay_mlag</samp>](## "mlag_configuration.dual_primary_recovery_delay_mlag") | Integer |  |  | Min: 0<br>Max: 86400 | Delay in seconds |
| [<samp>&nbsp;&nbsp;dual_primary_recovery_delay_non_mlag</samp>](## "mlag_configuration.dual_primary_recovery_delay_non_mlag") | Integer |  |  | Min: 0<br>Max: 86400 | Delay in seconds |
| [<samp>&nbsp;&nbsp;peer_link</samp>](## "mlag_configuration.peer_link") | String |  |  |  | Port-Channel interface name |
| [<samp>&nbsp;&nbsp;reload_delay_mlag</samp>](## "mlag_configuration.reload_delay_mlag") | String |  |  |  | Delay in seconds <0-86400> or 'infinity' |
| [<samp>&nbsp;&nbsp;reload_delay_non_mlag</samp>](## "mlag_configuration.reload_delay_non_mlag") | String |  |  |  | Delay in seconds <0-86400> or 'infinity' |

### YAML

```yaml
mlag_configuration:
  domain_id: <str>
  heartbeat_interval: <int>
  local_interface: <str>
  peer_address: <str>
  peer_address_heartbeat:
    peer_ip: <str>
    vrf: <str>
  dual_primary_detection_delay: <int>
  dual_primary_recovery_delay_mlag: <int>
  dual_primary_recovery_delay_non_mlag: <int>
  peer_link: <str>
  reload_delay_mlag: <str>
  reload_delay_non_mlag: <str>
```

## Monitor Connectivity

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>monitor_connectivity</samp>](## "monitor_connectivity") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;shutdown</samp>](## "monitor_connectivity.shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;interval</samp>](## "monitor_connectivity.interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;interface_sets</samp>](## "monitor_connectivity.interface_sets") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "monitor_connectivity.interface_sets.[].name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "monitor_connectivity.interface_sets.[].interfaces") | String |  |  |  | Interface range(s) should be of same type, Ethernet, Loopback, Management etc.<br>Multiple interface ranges can be specified separated by ","<br> |
| [<samp>&nbsp;&nbsp;local_interfaces</samp>](## "monitor_connectivity.local_interfaces") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;hosts</samp>](## "monitor_connectivity.hosts") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "monitor_connectivity.hosts.[].name") | String |  |  |  | Host Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "monitor_connectivity.hosts.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "monitor_connectivity.hosts.[].ip") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp>](## "monitor_connectivity.hosts.[].local_interfaces") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "monitor_connectivity.hosts.[].url") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;vrfs</samp>](## "monitor_connectivity.vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "monitor_connectivity.vrfs.[].name") | String |  |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "monitor_connectivity.vrfs.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface_sets</samp>](## "monitor_connectivity.vrfs.[].interface_sets") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "monitor_connectivity.vrfs.[].interface_sets.[].name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "monitor_connectivity.vrfs.[].interface_sets.[].interfaces") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp>](## "monitor_connectivity.vrfs.[].local_interfaces") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hosts</samp>](## "monitor_connectivity.vrfs.[].hosts") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "monitor_connectivity.vrfs.[].hosts.[].name") | String |  |  |  | Host name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "monitor_connectivity.vrfs.[].hosts.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "monitor_connectivity.vrfs.[].hosts.[].ip") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp>](## "monitor_connectivity.vrfs.[].hosts.[].local_interfaces") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "monitor_connectivity.vrfs.[].hosts.[].url") | String |  |  |  |  |

### YAML

```yaml
monitor_connectivity:
  shutdown: <bool>
  interval: <int>
  interface_sets:
    - name: <str>
      interfaces: <str>
  local_interfaces: <str>
  hosts:
    - name: <str>
      description: <str>
      ip: <str>
      local_interfaces: <str>
      url: <str>
  vrfs:
    - name: <str>
      description: <str>
      interface_sets:
        - name: <str>
          interfaces: <str>
      local_interfaces: <str>
      hosts:
        - name: <str>
          description: <str>
          ip: <str>
          local_interfaces: <str>
          url: <str>
```

## Monitor Sessions

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>monitor_sessions</samp>](## "monitor_sessions") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "monitor_sessions.[].name") | String | Required |  |  | Session Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sources</samp>](## "monitor_sessions.[].sources") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "monitor_sessions.[].sources.[].name") | String |  |  |  | Interface name, range or comma separated list |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "monitor_sessions.[].sources.[].direction") | String |  |  | Valid Values:<br>- rx<br>- tx<br>- both |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "monitor_sessions.[].sources.[].access_group") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "monitor_sessions.[].sources.[].access_group.type") | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "monitor_sessions.[].sources.[].access_group.name") | String |  |  |  | ACL Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "monitor_sessions.[].sources.[].access_group.priority") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;destinations</samp>](## "monitor_sessions.[].destinations") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "monitor_sessions.[].destinations.[].&lt;str&gt;") | String |  |  |  | 'cpu' or interface name, range or comma separated list |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_gre_metadata_tx</samp>](## "monitor_sessions.[].encapsulation_gre_metadata_tx") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;header_remove_size</samp>](## "monitor_sessions.[].header_remove_size") | Integer |  |  |  | Number of bytes to remove from header |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "monitor_sessions.[].access_group") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "monitor_sessions.[].access_group.type") | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "monitor_sessions.[].access_group.name") | String |  |  |  | ACL Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_ingress_chip</samp>](## "monitor_sessions.[].rate_limit_per_ingress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_egress_chip</samp>](## "monitor_sessions.[].rate_limit_per_egress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "monitor_sessions.[].sample") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;truncate</samp>](## "monitor_sessions.[].truncate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "monitor_sessions.[].truncate.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "monitor_sessions.[].truncate.size") | Integer |  |  |  | Size in bytes |

### YAML

```yaml
monitor_sessions:
  - name: <str>
    sources:
      - name: <str>
        direction: <str>
        access_group:
          type: <str>
          name: <str>
          priority: <int>
    destinations:
      - <str>
    encapsulation_gre_metadata_tx: <bool>
    header_remove_size: <int>
    access_group:
      type: <str>
      name: <str>
    rate_limit_per_ingress_chip: <str>
    rate_limit_per_egress_chip: <str>
    sample: <int>
    truncate:
      enabled: <bool>
      size: <int>
```

## MPLS

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mpls</samp>](## "mpls") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;ip</samp>](## "mpls.ip") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;ldp</samp>](## "mpls.ldp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_disabled_default</samp>](## "mpls.ldp.interface_disabled_default") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "mpls.ldp.router_id") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "mpls.ldp.shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;transport_address_interface</samp>](## "mpls.ldp.transport_address_interface") | String |  |  |  | Interface Name |

### YAML

```yaml
mpls:
  ip: <bool>
  ldp:
    interface_disabled_default: <bool>
    router_id: <str>
    shutdown: <bool>
    transport_address_interface: <str>
```

## Name Server

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>name_server</samp>](## "name_server") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;source</samp>](## "name_server.source") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "name_server.source.vrf") | String |  |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;nodes</samp>](## "name_server.nodes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "name_server.nodes.[].&lt;str&gt;") | String |  |  |  |  |

### YAML

```yaml
name_server:
  source:
    vrf: <str>
  nodes:
    - <str>
```

## NTP

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ntp</samp>](## "ntp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;local_interface</samp>](## "ntp.local_interface") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "ntp.local_interface.name") | String |  |  |  | Source interface |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ntp.local_interface.vrf") | String |  |  |  | VRF name |
| [<samp>&nbsp;&nbsp;servers</samp>](## "ntp.servers") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "ntp.servers.[].name") | String |  |  |  | IP or hostname e.g., 2.2.2.55, ie.pool.ntp.org |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;burst</samp>](## "ntp.servers.[].burst") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iburst</samp>](## "ntp.servers.[].iburst") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "ntp.servers.[].key") | Integer |  |  | Min: 1<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "ntp.servers.[].local_interface") | String |  |  |  | Source interface |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maxpoll</samp>](## "ntp.servers.[].maxpoll") | Integer |  |  | Min: 3<br>Max: 17 | Value of maxpoll between 3 - 17 (Logarithmic) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minpoll</samp>](## "ntp.servers.[].minpoll") | Integer |  |  | Min: 3<br>Max: 17 | Value of minpoll between 3 - 17 (Logarithmic) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preferred</samp>](## "ntp.servers.[].preferred") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "ntp.servers.[].version") | Integer |  |  | Min: 1<br>Max: 4 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ntp.servers.[].vrf") | String |  |  |  | VRF name |
| [<samp>&nbsp;&nbsp;authenticate</samp>](## "ntp.authenticate") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;authenticate_servers_only</samp>](## "ntp.authenticate_servers_only") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;authentication_keys</samp>](## "ntp.authentication_keys") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "ntp.authentication_keys.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 65534 | Key identifier |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "ntp.authentication_keys.[].hash_algorithm") | String |  |  | Valid Values:<br>- md5<br>- sha1 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "ntp.authentication_keys.[].key") | String |  |  |  | Obfuscated key |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "ntp.authentication_keys.[].key_type") | String |  |  | Valid Values:<br>- 0<br>- 7<br>- 8a |  |
| [<samp>&nbsp;&nbsp;trusted_keys</samp>](## "ntp.trusted_keys") | String |  |  |  | List of trusted-keys as string ex. 10-12,15 |

### YAML

```yaml
ntp:
  local_interface:
    name: <str>
    vrf: <str>
  servers:
    - name: <str>
      burst: <bool>
      iburst: <bool>
      key: <int>
      local_interface: <str>
      maxpoll: <int>
      minpoll: <int>
      preferred: <bool>
      version: <int>
      vrf: <str>
  authenticate: <bool>
  authenticate_servers_only: <bool>
  authentication_keys:
    - id: <int>
      hash_algorithm: <str>
      key: <str>
      key_type: <str>
  trusted_keys: <str>
```

## Patch Panel

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>patch_panel</samp>](## "patch_panel") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;patches</samp>](## "patch_panel.patches") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "patch_panel.patches.[].name") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "patch_panel.patches.[].enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connectors</samp>](## "patch_panel.patches.[].connectors") | List, items: Dictionary |  |  | Min Length: 2<br>Max Length: 2 | Must have exactly two connectors to a patch of which at least one must be of type "interface" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "patch_panel.patches.[].connectors.[].id") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "patch_panel.patches.[].connectors.[].type") | String | Required |  | Valid Values:<br>- interface<br>- pseudowire |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endpoint</samp>](## "patch_panel.patches.[].connectors.[].endpoint") | String | Required |  |  | String with relevant endpoint depending on type.<br>Examples:<br>- "Ethernet1"<br>- "Ethernet1 dot1q vlan 123"<br>- "bgp vpws TENANT_A pseudowire VPWS_PW_1"<br>- "ldp LDP_PW_1"<br> |

### YAML

```yaml
patch_panel:
  patches:
    - name: <str>
      enabled: <bool>
      connectors:
        - id: <str>
          type: <str>
          endpoint: <str>
```

## Peer Filters

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>peer_filters</samp>](## "peer_filters") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "peer_filters.[].name") | String | Required, Unique |  |  | Peer-filter Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "peer_filters.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "peer_filters.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match</samp>](## "peer_filters.[].sequence_numbers.[].match") | String | Required |  |  | Match as string<br>Example: "as-range 1-100 result accept" |

### YAML

```yaml
peer_filters:
  - name: <str>
    sequence_numbers:
      - sequence: <int>
        match: <str>
```

## Platform

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>platform</samp>](## "platform") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;trident</samp>](## "platform.trident") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;forwarding_table_partition</samp>](## "platform.trident.forwarding_table_partition") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;sand</samp>](## "platform.sand") | Dictionary |  |  |  | Most of the platform sand options are hardware dependant and optional |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;qos_maps</samp>](## "platform.sand.qos_maps") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- traffic_class</samp>](## "platform.sand.qos_maps.[].traffic_class") | Integer |  |  | Min: 0<br>Max: 7 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to_network_qos</samp>](## "platform.sand.qos_maps.[].to_network_qos") | Integer |  |  | Min: 0<br>Max: 63 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lag</samp>](## "platform.sand.lag") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_only</samp>](## "platform.sand.lag.hardware_only") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "platform.sand.lag.mode") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;forwarding_mode</samp>](## "platform.sand.forwarding_mode") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;multicast_replication</samp>](## "platform.sand.multicast_replication") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "platform.sand.multicast_replication.default") | String |  |  | Valid Values:<br>- ingress<br>- egress |  |

### YAML

```yaml
platform:
  trident:
    forwarding_table_partition: <str>
  sand:
    qos_maps:
      - traffic_class: <int>
        to_network_qos: <int>
    lag:
      hardware_only: <bool>
      mode: <str>
    forwarding_mode: <str>
    multicast_replication:
      default: <str>
```

## Policy Maps

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>policy_maps</samp>](## "policy_maps") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;pbr</samp>](## "policy_maps.pbr") | List, items: Dictionary |  |  |  | PBR Policy-Maps |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "policy_maps.pbr.[].name") | String | Required, Unique |  |  | Policy-Map Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;classes</samp>](## "policy_maps.pbr.[].classes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "policy_maps.pbr.[].classes.[].name") | String | Required, Unique |  |  | Class Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index</samp>](## "policy_maps.pbr.[].classes.[].index") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "policy_maps.pbr.[].classes.[].drop") | Boolean |  |  |  | 'drop' and 'set' are mutually exclusive |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set</samp>](## "policy_maps.pbr.[].classes.[].set") | Dictionary |  |  |  | Set Nexthop<br>'drop' and 'set' are mutually exclusive<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nexthop</samp>](## "policy_maps.pbr.[].classes.[].set.nexthop") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "policy_maps.pbr.[].classes.[].set.nexthop.ip_address") | String |  |  |  | IPv4 or IPv6 Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recursive</samp>](## "policy_maps.pbr.[].classes.[].set.nexthop.recursive") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;qos</samp>](## "policy_maps.qos") | List, items: Dictionary |  |  |  | QOS Policy-Maps |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "policy_maps.qos.[].name") | String | Required, Unique |  |  | Policy-Map Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;classes</samp>](## "policy_maps.qos.[].classes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "policy_maps.qos.[].classes.[].name") | String | Required, Unique |  |  | Class Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set</samp>](## "policy_maps.qos.[].classes.[].set") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "policy_maps.qos.[].classes.[].set.cos") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "policy_maps.qos.[].classes.[].set.dscp") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "policy_maps.qos.[].classes.[].set.traffic_class") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop_precedence</samp>](## "policy_maps.qos.[].classes.[].set.drop_precedence") | Integer |  |  |  |  |

### YAML

```yaml
policy_maps:
  pbr:
    - name: <str>
      classes:
        - name: <str>
          index: <int>
          drop: <bool>
          set:
            nexthop:
              ip_address: <str>
              recursive: <bool>
  qos:
    - name: <str>
      classes:
        - name: <str>
          set:
            cos: <int>
            dscp: <str>
            traffic_class: <int>
            drop_precedence: <int>
```

## Port Channel Interfaces

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>port_channel_interfaces</samp>](## "port_channel_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "port_channel_interfaces.[].name") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "port_channel_interfaces.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "port_channel_interfaces.[].logging") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event</samp>](## "port_channel_interfaces.[].logging.event") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_status</samp>](## "port_channel_interfaces.[].logging.event.link_status") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "port_channel_interfaces.[].shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_mtu</samp>](## "port_channel_interfaces.[].l2_mtu") | Integer |  |  |  | "l2_mtu" should only be defined for platforms supporting the "l2 mtu" CLI<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "port_channel_interfaces.[].vlans") | String |  |  |  | List of switchport vlans as string<br>For a trunk port this would be a range like "1-200,300"<br>For an access port this would be a single vlan "123"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;snmp_trap_link_change</samp>](## "port_channel_interfaces.[].snmp_trap_link_change") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "port_channel_interfaces.[].type") | String |  |  | Valid Values:<br>- routed<br>- switched<br>- l3dot1q<br>- l2dot1q | l3dot1q and l2dot1q are used for sub-interfaces<br>The parent interface should be defined as routed<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "port_channel_interfaces.[].encapsulation_dot1q_vlan") | Integer |  |  |  | VLAN tag to configure on sub-interface |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "port_channel_interfaces.[].vrf") | String |  |  |  | VRF name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_vlan</samp>](## "port_channel_interfaces.[].encapsulation_vlan") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client.dot1q") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client.dot1q.vlan") | Integer |  |  |  | Client VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client.dot1q.outer") | Integer |  |  |  | Client Outer VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client.dot1q.inner") | Integer |  |  |  | Client Inner VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unmatched</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client.unmatched") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;network</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network") | Dictionary |  |  |  | Network encapsulation are all optional, and skipped if using client unmatched |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network.dot1q") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network.dot1q.vlan") | Integer |  |  |  | Network VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network.dot1q.outer") | Integer |  |  |  | Network Outer VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network.dot1q.inner") | Integer |  |  |  | Network Inner VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network.client") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_id</samp>](## "port_channel_interfaces.[].vlan_id") | Integer |  |  | Min: 1<br>Max: 4094 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "port_channel_interfaces.[].mode") | String |  |  | Valid Values:<br>- access<br>- dot1q-tunnel<br>- trunk<br>- trunk phone |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp>](## "port_channel_interfaces.[].native_vlan") | Integer |  |  |  | If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_tag</samp>](## "port_channel_interfaces.[].native_vlan_tag") | Boolean |  | False |  | If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;link_tracking_groups</samp>](## "port_channel_interfaces.[].link_tracking_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "port_channel_interfaces.[].link_tracking_groups.[].name") | String | Required, Unique |  |  | Group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "port_channel_interfaces.[].link_tracking_groups.[].direction") | String |  |  | Valid Values:<br>- upstream<br>- downstream |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;phone</samp>](## "port_channel_interfaces.[].phone") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk</samp>](## "port_channel_interfaces.[].phone.trunk") | String |  |  | Valid Values:<br>- tagged<br>- untagged |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "port_channel_interfaces.[].phone.vlan") | Integer |  |  | Min: 1<br>Max: 4094 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_protocol</samp>](## "port_channel_interfaces.[].l2_protocol") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "port_channel_interfaces.[].l2_protocol.encapsulation_dot1q_vlan") | Integer |  |  |  | Vlan tag to configure on sub-interface |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "port_channel_interfaces.[].mtu") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "port_channel_interfaces.[].mlag") | Integer |  |  | Min: 1<br>Max: 2000 | MLAG ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "port_channel_interfaces.[].trunk_groups") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "port_channel_interfaces.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_fallback_timeout</samp>](## "port_channel_interfaces.[].lacp_fallback_timeout") | Integer |  | 90 | Min: 0<br>Max: 300 | Timeout in seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_fallback_mode</samp>](## "port_channel_interfaces.[].lacp_fallback_mode") | String |  |  | Valid Values:<br>- individual<br>- static |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;qos</samp>](## "port_channel_interfaces.[].qos") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trust</samp>](## "port_channel_interfaces.[].qos.trust") | String |  |  | Valid Values:<br>- dscp<br>- cos<br>- disabled |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "port_channel_interfaces.[].qos.dscp") | Integer |  |  |  | DSCP value |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "port_channel_interfaces.[].qos.cos") | Integer |  |  |  | COS value |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "port_channel_interfaces.[].bfd") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo</samp>](## "port_channel_interfaces.[].bfd.echo") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "port_channel_interfaces.[].bfd.interval") | Integer |  |  |  | Interval in milliseconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "port_channel_interfaces.[].bfd.min_rx") | Integer |  |  |  | Rate in milliseconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "port_channel_interfaces.[].bfd.multiplier") | Integer |  |  | Min: 3<br>Max: 50 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_policy</samp>](## "port_channel_interfaces.[].service_policy") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pbr</samp>](## "port_channel_interfaces.[].service_policy.pbr") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp>](## "port_channel_interfaces.[].service_policy.pbr.input") | String |  |  |  | Policy-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "port_channel_interfaces.[].mpls") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "port_channel_interfaces.[].mpls.ip") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ldp</samp>](## "port_channel_interfaces.[].mpls.ldp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "port_channel_interfaces.[].mpls.ldp.interface") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igp_sync</samp>](## "port_channel_interfaces.[].mpls.ldp.igp_sync") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_private_vlan_secondary</samp>](## "port_channel_interfaces.[].trunk_private_vlan_secondary") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pvlan_mapping</samp>](## "port_channel_interfaces.[].pvlan_mapping") | String |  |  |  | List of vlans as string |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_translations</samp>](## "port_channel_interfaces.[].vlan_translations") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- from</samp>](## "port_channel_interfaces.[].vlan_translations.[].from") | String |  |  |  | List of vlans as string (only one vlan if direction is "both") |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to</samp>](## "port_channel_interfaces.[].vlan_translations.[].to") | Integer |  |  |  | VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "port_channel_interfaces.[].vlan_translations.[].direction") | String |  | both | Valid Values:<br>- in<br>- out<br>- both |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "port_channel_interfaces.[].shape") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "port_channel_interfaces.[].shape.rate") | String |  |  |  | Rate in kbps, pps or percent<br>Supported options are platform dependent<br>Examples:<br>- "5000 kbps"<br>- "1000 pps"<br>- "20 percent"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp>](## "port_channel_interfaces.[].storm_control") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "port_channel_interfaces.[].storm_control.all") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "port_channel_interfaces.[].storm_control.all.level") | String |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "port_channel_interfaces.[].storm_control.all.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional field and is hardware dependant |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;broadcast</samp>](## "port_channel_interfaces.[].storm_control.broadcast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "port_channel_interfaces.[].storm_control.broadcast.level") | String |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "port_channel_interfaces.[].storm_control.broadcast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional field and is hardware dependant |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "port_channel_interfaces.[].storm_control.multicast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "port_channel_interfaces.[].storm_control.multicast.level") | String |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "port_channel_interfaces.[].storm_control.multicast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional field and is hardware dependant |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unknown_unicast</samp>](## "port_channel_interfaces.[].storm_control.unknown_unicast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "port_channel_interfaces.[].storm_control.unknown_unicast.level") | String |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "port_channel_interfaces.[].storm_control.unknown_unicast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional field and is hardware dependant |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_proxy_arp</samp>](## "port_channel_interfaces.[].ip_proxy_arp") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_enable</samp>](## "port_channel_interfaces.[].isis_enable") | String |  |  |  | ISIS instance |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_passive</samp>](## "port_channel_interfaces.[].isis_passive") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "port_channel_interfaces.[].isis_metric") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_network_point_to_point</samp>](## "port_channel_interfaces.[].isis_network_point_to_point") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "port_channel_interfaces.[].isis_circuit_type") | String |  |  | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "port_channel_interfaces.[].isis_hello_padding") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "port_channel_interfaces.[].isis_authentication_mode") | String |  |  | Valid Values:<br>- text<br>- md5 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "port_channel_interfaces.[].isis_authentication_key") | String |  |  |  | Type-7 encrypted password |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;traffic_policy</samp>](## "port_channel_interfaces.[].traffic_policy") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp>](## "port_channel_interfaces.[].traffic_policy.input") | String |  |  |  | Ingress traffic policy |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;output</samp>](## "port_channel_interfaces.[].traffic_policy.output") | String |  |  |  | Egress traffic policy |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_ethernet_segment</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.identifier") | String |  |  |  | EVPN Ethernet Segment Identifier (Type 1 format) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redundancy</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.redundancy") | String |  |  | Valid Values:<br>- all-active<br>- single-active |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_election</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.algorithm") | String |  |  | Valid Values:<br>- modulus<br>- preference |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preference_value</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.preference_value") | Integer |  |  | Min: 0<br>Max: 65535 | Preference_value is only used when "algorithm" is "preference" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dont_preempt</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.dont_preempt") | Boolean |  | False |  | Dont_preempt is only used when "algorithm" is "preference" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hold_time</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.hold_time") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subsequent_hold_time</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.subsequent_hold_time") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;candidate_reachability_required</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.candidate_reachability_required") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.mpls") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_index</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.mpls.shared_index") | Integer |  |  | Min: 1<br>Max: 1024 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel_flood_filter_time</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.mpls.tunnel_flood_filter_time") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.route_target") | String |  |  |  | EVPN Route Target for ESI with format xx:xx:xx:xx:xx:xx |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;esi</samp>](## "port_channel_interfaces.[].esi") | String |  |  |  | EVPN Ethernet Segment Identifier (Type 1 format)<br>Will be deprecated in AVD 4.0 in favor of "evpn_ethernet_segment.identifier"<br>If both "esi" and "evpn_ethernet_segment.identifier" are defined, the new variable takes precedence<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rt</samp>](## "port_channel_interfaces.[].rt") | String |  |  |  | EVPN Route Target for ESI with format xx:xx:xx:xx:xx:xx<br>Will be deprecated in AVD 4.0 in favor of "evpn_ethernet_segment.route_target"<br>If both "rt" and "evpn_ethernet_segment.route_target" are defined, the new variable takes precedence<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_id</samp>](## "port_channel_interfaces.[].lacp_id") | String |  |  |  | LACP ID with format xxxx.xxxx.xxxx |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpdufilter</samp>](## "port_channel_interfaces.[].spanning_tree_bpdufilter") | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False<br>- true<br>- false |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpduguard</samp>](## "port_channel_interfaces.[].spanning_tree_bpduguard") | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False<br>- true<br>- false |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_guard</samp>](## "port_channel_interfaces.[].spanning_tree_guard") | String |  |  | Valid Values:<br>- loop<br>- root<br>- disabled |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_portfast</samp>](## "port_channel_interfaces.[].spanning_tree_portfast") | String |  |  | Valid Values:<br>- edge<br>- network |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vmtracer</samp>](## "port_channel_interfaces.[].vmtracer") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "port_channel_interfaces.[].ptp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "port_channel_interfaces.[].ptp.enable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "port_channel_interfaces.[].ptp.announce") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "port_channel_interfaces.[].ptp.announce.interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "port_channel_interfaces.[].ptp.announce.timeout") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_req</samp>](## "port_channel_interfaces.[].ptp.delay_req") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_mechanism</samp>](## "port_channel_interfaces.[].ptp.delay_mechanism") | String |  |  | Valid Values:<br>- e2e<br>- p2p |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync_message</samp>](## "port_channel_interfaces.[].ptp.sync_message") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "port_channel_interfaces.[].ptp.sync_message.interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "port_channel_interfaces.[].ptp.role") | String |  |  | Valid Values:<br>- master<br>- dynamic |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "port_channel_interfaces.[].ptp.vlan") | String |  |  |  | VLAN can be 'all' or list of vlans as string |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transport</samp>](## "port_channel_interfaces.[].ptp.transport") | String |  |  | Valid Values:<br>- ipv4<br>- ipv6<br>- layer2 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "port_channel_interfaces.[].ip_address") | String |  |  |  | IPv4 address/mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "port_channel_interfaces.[].ipv6_enable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "port_channel_interfaces.[].ipv6_address") | String |  |  |  | IPv6 address/mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_link_local</samp>](## "port_channel_interfaces.[].ipv6_address_link_local") | String |  |  |  | Link local IPv6 address/mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_ra_disabled</samp>](## "port_channel_interfaces.[].ipv6_nd_ra_disabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_managed_config_flag</samp>](## "port_channel_interfaces.[].ipv6_nd_managed_config_flag") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_prefixes</samp>](## "port_channel_interfaces.[].ipv6_nd_prefixes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ipv6_prefix</samp>](## "port_channel_interfaces.[].ipv6_nd_prefixes.[].ipv6_prefix") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;valid_lifetime</samp>](## "port_channel_interfaces.[].ipv6_nd_prefixes.[].valid_lifetime") | String |  |  |  | Infinite or lifetime in seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preferred_lifetime</samp>](## "port_channel_interfaces.[].ipv6_nd_prefixes.[].preferred_lifetime") | String |  |  |  | Infinite or lifetime in seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_autoconfig_flag</samp>](## "port_channel_interfaces.[].ipv6_nd_prefixes.[].no_autoconfig_flag") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_in</samp>](## "port_channel_interfaces.[].access_group_in") | String |  |  |  | Access list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_out</samp>](## "port_channel_interfaces.[].access_group_out") | String |  |  |  | Access list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_in</samp>](## "port_channel_interfaces.[].ipv6_access_group_in") | String |  |  |  | IPv6 access list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_out</samp>](## "port_channel_interfaces.[].ipv6_access_group_out") | String |  |  |  | IPv6 access list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_access_group_in</samp>](## "port_channel_interfaces.[].mac_access_group_in") | String |  |  |  | MAC access list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_access_group_out</samp>](## "port_channel_interfaces.[].mac_access_group_out") | String |  |  |  | MAC access list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pim</samp>](## "port_channel_interfaces.[].pim") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "port_channel_interfaces.[].pim.ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dr_priority</samp>](## "port_channel_interfaces.[].pim.ipv4.dr_priority") | Integer |  |  | Min: 0<br>Max: 429467295 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sparse_mode</samp>](## "port_channel_interfaces.[].pim.ipv4.sparse_mode") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_profile</samp>](## "port_channel_interfaces.[].service_profile") | String |  |  |  | QOS profile |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_network_point_to_point</samp>](## "port_channel_interfaces.[].ospf_network_point_to_point") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_area</samp>](## "port_channel_interfaces.[].ospf_area") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_cost</samp>](## "port_channel_interfaces.[].ospf_cost") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication</samp>](## "port_channel_interfaces.[].ospf_authentication") | String |  |  | Valid Values:<br>- none<br>- simple<br>- message-digest |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication_key</samp>](## "port_channel_interfaces.[].ospf_authentication_key") | String |  |  |  | Encrypted password |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_message_digest_keys</samp>](## "port_channel_interfaces.[].ospf_message_digest_keys") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "port_channel_interfaces.[].ospf_message_digest_keys.[].id") | Integer | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "port_channel_interfaces.[].ospf_message_digest_keys.[].hash_algorithm") | String |  |  | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "port_channel_interfaces.[].ospf_message_digest_keys.[].key") | String |  |  |  | Encrypted password |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;flow_tracker</samp>](## "port_channel_interfaces.[].flow_tracker") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sampled</samp>](## "port_channel_interfaces.[].flow_tracker.sampled") | String |  |  |  | Flow tracker name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "port_channel_interfaces.[].peer") | String |  |  |  | Key only used for documentation or validation purposes |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "port_channel_interfaces.[].peer_interface") | String |  |  |  | Key only used for documentation or validation purposes |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_type</samp>](## "port_channel_interfaces.[].peer_type") | String |  |  |  | Key only used for documentation or validation purposes |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "port_channel_interfaces.[].eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the port-channel interface in the final EOS configuration |

### YAML

```yaml
port_channel_interfaces:
  - name: <str>
    description: <str>
    logging:
      event:
        link_status: <bool>
    shutdown: <bool>
    l2_mtu: <int>
    vlans: <str>
    snmp_trap_link_change: <bool>
    type: <str>
    encapsulation_dot1q_vlan: <int>
    vrf: <str>
    encapsulation_vlan:
      client:
        dot1q:
          vlan: <int>
          outer: <int>
          inner: <int>
        unmatched: <bool>
      network:
        dot1q:
          vlan: <int>
          outer: <int>
          inner: <int>
        client: <bool>
    vlan_id: <int>
    mode: <str>
    native_vlan: <int>
    native_vlan_tag: <bool>
    link_tracking_groups:
      - name: <str>
        direction: <str>
    phone:
      trunk: <str>
      vlan: <int>
    l2_protocol:
      encapsulation_dot1q_vlan: <int>
    mtu: <int>
    mlag: <int>
    trunk_groups:
      - <str>
    lacp_fallback_timeout: <int>
    lacp_fallback_mode: <str>
    qos:
      trust: <str>
      dscp: <int>
      cos: <int>
    bfd:
      echo: <bool>
      interval: <int>
      min_rx: <int>
      multiplier: <int>
    service_policy:
      pbr:
        input: <str>
    mpls:
      ip: <bool>
      ldp:
        interface: <bool>
        igp_sync: <bool>
    trunk_private_vlan_secondary: <bool>
    pvlan_mapping: <str>
    vlan_translations:
      - from: <str>
        to: <int>
        direction: <str>
    shape:
      rate: <str>
    storm_control:
      all:
        level: <str>
        unit: <str>
      broadcast:
        level: <str>
        unit: <str>
      multicast:
        level: <str>
        unit: <str>
      unknown_unicast:
        level: <str>
        unit: <str>
    ip_proxy_arp: <bool>
    isis_enable: <str>
    isis_passive: <bool>
    isis_metric: <int>
    isis_network_point_to_point: <bool>
    isis_circuit_type: <str>
    isis_hello_padding: <bool>
    isis_authentication_mode: <str>
    isis_authentication_key: <str>
    traffic_policy:
      input: <str>
      output: <str>
    evpn_ethernet_segment:
      identifier: <str>
      redundancy: <str>
      designated_forwarder_election:
        algorithm: <str>
        preference_value: <int>
        dont_preempt: <bool>
        hold_time: <int>
        subsequent_hold_time: <int>
        candidate_reachability_required: <bool>
      mpls:
        shared_index: <int>
        tunnel_flood_filter_time: <int>
      route_target: <str>
    esi: <str>
    rt: <str>
    lacp_id: <str>
    spanning_tree_bpdufilter: <str>
    spanning_tree_bpduguard: <str>
    spanning_tree_guard: <str>
    spanning_tree_portfast: <str>
    vmtracer: <bool>
    ptp:
      enable: <bool>
      announce:
        interval: <int>
        timeout: <int>
      delay_req: <int>
      delay_mechanism: <str>
      sync_message:
        interval: <int>
      role: <str>
      vlan: <str>
      transport: <str>
    ip_address: <str>
    ipv6_enable: <bool>
    ipv6_address: <str>
    ipv6_address_link_local: <str>
    ipv6_nd_ra_disabled: <bool>
    ipv6_nd_managed_config_flag: <bool>
    ipv6_nd_prefixes:
      - ipv6_prefix: <str>
        valid_lifetime: <str>
        preferred_lifetime: <str>
        no_autoconfig_flag: <bool>
    access_group_in: <str>
    access_group_out: <str>
    ipv6_access_group_in: <str>
    ipv6_access_group_out: <str>
    mac_access_group_in: <str>
    mac_access_group_out: <str>
    pim:
      ipv4:
        dr_priority: <int>
        sparse_mode: <bool>
    service_profile: <str>
    ospf_network_point_to_point: <bool>
    ospf_area: <str>
    ospf_cost: <int>
    ospf_authentication: <str>
    ospf_authentication_key: <str>
    ospf_message_digest_keys:
      - id: <int>
        hash_algorithm: <str>
        key: <str>
    flow_tracker:
      sampled: <str>
    peer: <str>
    peer_interface: <str>
    peer_type: <str>
    eos_cli: <str>
```

## Prefix Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>prefix_lists</samp>](## "prefix_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "prefix_lists.[].name") | String | Required, Unique |  |  | Prefix-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "prefix_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "prefix_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "prefix_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string<br>Example: "permit 10.255.0.0/27 eq 32" |

### YAML

```yaml
prefix_lists:
  - name: <str>
    sequence_numbers:
      - sequence: <int>
        action: <str>
```

## Prompt

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>prompt</samp>](## "prompt") | String |  |  |  |  |

### YAML

```yaml
prompt: <str>
```

## PTP

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>ptp</samp>](## "ptp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;mode</samp>](## "ptp.mode") | String |  |  | Valid Values:<br>- boundary<br>- transparent |  |
| [<samp>&nbsp;&nbsp;forward_unicast</samp>](## "ptp.forward_unicast") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;clock_identity</samp>](## "ptp.clock_identity") | String |  |  |  | The clock-id in xx:xx:xx:xx:xx:xx format |
| [<samp>&nbsp;&nbsp;source</samp>](## "ptp.source") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "ptp.source.ip") | String |  |  |  | Source IP |
| [<samp>&nbsp;&nbsp;priority1</samp>](## "ptp.priority1") | Integer |  |  | Min: 0<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;priority2</samp>](## "ptp.priority2") | Integer |  |  | Min: 0<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;ttl</samp>](## "ptp.ttl") | Integer |  |  | Min: 1<br>Max: 254 |  |
| [<samp>&nbsp;&nbsp;domain</samp>](## "ptp.domain") | Integer |  |  | Min: 0<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;message_type</samp>](## "ptp.message_type") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;general</samp>](## "ptp.message_type.general") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "ptp.message_type.general.dscp") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;event</samp>](## "ptp.message_type.event") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "ptp.message_type.event.dscp") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;monitor</samp>](## "ptp.monitor") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ptp.monitor.enabled") | Boolean |  | True |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "ptp.monitor.threshold") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "ptp.monitor.threshold.offset_from_master") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "ptp.monitor.threshold.mean_path_delay") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "ptp.monitor.threshold.drop") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "ptp.monitor.threshold.drop.offset_from_master") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "ptp.monitor.threshold.drop.mean_path_delay") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;missing_message</samp>](## "ptp.monitor.missing_message") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "ptp.monitor.missing_message.intervals") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "ptp.monitor.missing_message.intervals.announce") | Integer |  |  | Min: 2<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "ptp.monitor.missing_message.intervals.follow_up") | Integer |  |  | Min: 2<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "ptp.monitor.missing_message.intervals.sync") | Integer |  |  | Min: 2<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_ids</samp>](## "ptp.monitor.missing_message.sequence_ids") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ptp.monitor.missing_message.sequence_ids.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "ptp.monitor.missing_message.sequence_ids.announce") | Integer |  |  | Min: 2<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_resp</samp>](## "ptp.monitor.missing_message.sequence_ids.delay_resp") | Integer |  |  | Min: 2<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "ptp.monitor.missing_message.sequence_ids.follow_up") | Integer |  |  | Min: 2<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "ptp.monitor.missing_message.sequence_ids.sync") | Integer |  |  | Min: 2<br>Max: 255 |  |

### YAML

```yaml
ptp:
  mode: <str>
  forward_unicast: <bool>
  clock_identity: <str>
  source:
    ip: <str>
  priority1: <int>
  priority2: <int>
  ttl: <int>
  domain: <int>
  message_type:
    general:
      dscp: <int>
    event:
      dscp: <int>
  monitor:
    enabled: <bool>
    threshold:
      offset_from_master: <int>
      mean_path_delay: <int>
      drop:
        offset_from_master: <int>
        mean_path_delay: <int>
    missing_message:
      intervals:
        announce: <int>
        follow_up: <int>
        sync: <int>
      sequence_ids:
        enabled: <bool>
        announce: <int>
        delay_resp: <int>
        follow_up: <int>
        sync: <int>
```

## QOS

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>qos</samp>](## "qos") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;map</samp>](## "qos.map") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "qos.map.cos") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "qos.map.cos.[].&lt;str&gt;") | String |  |  |  | Example: "0 1 to traffic-class 1"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "qos.map.dscp") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "qos.map.dscp.[].&lt;str&gt;") | String |  |  |  | Example: "8 9 10 to traffic-class 1"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "qos.map.traffic_class") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "qos.map.traffic_class.[].&lt;str&gt;") | String |  |  |  | Example: "1 to dscp 32"<br> |
| [<samp>&nbsp;&nbsp;rewrite_dscp</samp>](## "qos.rewrite_dscp") | Boolean |  |  |  |  |

### YAML

```yaml
qos:
  map:
    cos:
      - <str>
    dscp:
      - <str>
    traffic_class:
      - <str>
  rewrite_dscp: <bool>
```

## QOS Profiles

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>qos_profiles</samp>](## "qos_profiles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "qos_profiles.[].name") | String | Required, Unique |  |  | Profile-Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trust</samp>](## "qos_profiles.[].trust") | String |  |  | Valid Values:<br>- cos<br>- dscp<br>- disabled |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "qos_profiles.[].cos") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "qos_profiles.[].dscp") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "qos_profiles.[].shape") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "qos_profiles.[].shape.rate") | String |  |  |  | Supported options are platform dependent<br>Example: "< rate > kbps", "1-100 percent", "< rate > pps"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_policy</samp>](## "qos_profiles.[].service_policy") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "qos_profiles.[].service_policy.type") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_input</samp>](## "qos_profiles.[].service_policy.type.qos_input") | String |  |  |  | Policy-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tx_queues</samp>](## "qos_profiles.[].tx_queues") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "qos_profiles.[].tx_queues.[].id") | Integer | Required, Unique |  |  | TX-Queue ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_percent</samp>](## "qos_profiles.[].tx_queues.[].bandwidth_percent") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_guaranteed_percent</samp>](## "qos_profiles.[].tx_queues.[].bandwidth_guaranteed_percent") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "qos_profiles.[].tx_queues.[].priority") | String |  |  | Valid Values:<br>- priority strict<br>- no priority |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "qos_profiles.[].tx_queues.[].shape") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "qos_profiles.[].tx_queues.[].shape.rate") | String |  |  |  | Supported options are platform dependent<br>Example: "< rate > kbps", "1-100 percent", "< rate > pps"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uc_tx_queues</samp>](## "qos_profiles.[].uc_tx_queues") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "qos_profiles.[].uc_tx_queues.[].id") | Integer | Required, Unique |  |  | UC TX queue ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_percent</samp>](## "qos_profiles.[].uc_tx_queues.[].bandwidth_percent") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_guaranteed_percent</samp>](## "qos_profiles.[].uc_tx_queues.[].bandwidth_guaranteed_percent") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "qos_profiles.[].uc_tx_queues.[].priority") | String |  |  | Valid Values:<br>- priority strict<br>- no priority |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "qos_profiles.[].uc_tx_queues.[].shape") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "qos_profiles.[].uc_tx_queues.[].shape.rate") | String |  |  |  | Supported options are platform dependent<br>Example: "< rate > kbps", "1-100 percent", "< rate > pps"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mc_tx_queues</samp>](## "qos_profiles.[].mc_tx_queues") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "qos_profiles.[].mc_tx_queues.[].id") | Integer | Required, Unique |  |  | MC TX queue ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_percent</samp>](## "qos_profiles.[].mc_tx_queues.[].bandwidth_percent") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_guaranteed_percent</samp>](## "qos_profiles.[].mc_tx_queues.[].bandwidth_guaranteed_percent") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "qos_profiles.[].mc_tx_queues.[].priority") | String |  |  | Valid Values:<br>- priority strict<br>- no priority |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "qos_profiles.[].mc_tx_queues.[].shape") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "qos_profiles.[].mc_tx_queues.[].shape.rate") | String |  |  |  | Supported options are platform dependent<br>Example: "< rate > kbps", "1-100 percent", "< rate > pps" |

### YAML

```yaml
qos_profiles:
  - name: <str>
    trust: <str>
    cos: <int>
    dscp: <int>
    shape:
      rate: <str>
    service_policy:
      type:
        qos_input: <str>
    tx_queues:
      - id: <int>
        bandwidth_percent: <int>
        bandwidth_guaranteed_percent: <int>
        priority: <str>
        shape:
          rate: <str>
    uc_tx_queues:
      - id: <int>
        bandwidth_percent: <int>
        bandwidth_guaranteed_percent: <int>
        priority: <str>
        shape:
          rate: <str>
    mc_tx_queues:
      - id: <int>
        bandwidth_percent: <int>
        bandwidth_guaranteed_percent: <int>
        priority: <str>
        shape:
          rate: <str>
```

## Queue Monitor Length

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>queue_monitor_length</samp>](## "queue_monitor_length") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;enabled</samp>](## "queue_monitor_length.enabled") | Boolean |  |  |  | "enabled: true" will be required in AVD4.0.<br>In AVD3.x default is true as long as queue_monitor_length is defined and not None<br> |
| [<samp>&nbsp;&nbsp;log</samp>](## "queue_monitor_length.log") | Integer |  |  |  | Logging interval in seconds |
| [<samp>&nbsp;&nbsp;notifying</samp>](## "queue_monitor_length.notifying") | Boolean |  |  |  | should only be used for platforms supporting the "queue-monitor length notifying" CLI |
| [<samp>&nbsp;&nbsp;cpu</samp>](## "queue_monitor_length.cpu") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;thresholds</samp>](## "queue_monitor_length.cpu.thresholds") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;high</samp>](## "queue_monitor_length.cpu.thresholds.high") | Integer | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;low</samp>](## "queue_monitor_length.cpu.thresholds.low") | Integer |  |  |  |  |

### YAML

```yaml
queue_monitor_length:
  enabled: <bool>
  log: <int>
  notifying: <bool>
  cpu:
    thresholds:
      high: <int>
      low: <int>
```

## Queue Monitor Streaming

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>queue_monitor_streaming</samp>](## "queue_monitor_streaming") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;enable</samp>](## "queue_monitor_streaming.enable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;ip_access_group</samp>](## "queue_monitor_streaming.ip_access_group") | String |  |  |  | Name of IP ACL |
| [<samp>&nbsp;&nbsp;ipv6_access_group</samp>](## "queue_monitor_streaming.ipv6_access_group") | String |  |  |  | Name of IPv6 ACL |
| [<samp>&nbsp;&nbsp;max_connections</samp>](## "queue_monitor_streaming.max_connections") | Integer |  |  | Min: 1<br>Max: 100 |  |
| [<samp>&nbsp;&nbsp;vrf</samp>](## "queue_monitor_streaming.vrf") | String |  |  |  |  |

### YAML

```yaml
queue_monitor_streaming:
  enable: <bool>
  ip_access_group: <str>
  ipv6_access_group: <str>
  max_connections: <int>
  vrf: <str>
```

## Radius Servers

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>radius_servers</samp>](## "radius_servers") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- host</samp>](## "radius_servers.[].host") | String |  |  |  | Host IP address or name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "radius_servers.[].vrf") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "radius_servers.[].key") | String |  |  |  | Encrypted key |

### YAML

```yaml
radius_servers:
  - host: <str>
    vrf: <str>
    key: <str>
```

## Redundancy

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>redundancy</samp>](## "redundancy") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;protocol</samp>](## "redundancy.protocol") | String |  |  |  | Redundancy Protocol |

### YAML

```yaml
redundancy:
  protocol: <str>
```

## Roles

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>roles</samp>](## "roles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "roles.[].name") | String |  |  |  | Role name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "roles.[].sequence_numbers") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "roles.[].sequence_numbers.[].sequence") | Integer |  |  |  | Sequence number |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "roles.[].sequence_numbers.[].action") | String |  |  | Valid Values:<br>- permit<br>- deny |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "roles.[].sequence_numbers.[].mode") | String |  |  |  | "config", "config-all", "exec" or mode key as string<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;command</samp>](## "roles.[].sequence_numbers.[].command") | String |  |  |  | Command as string |

### YAML

```yaml
roles:
  - name: <str>
    sequence_numbers:
      - sequence: <int>
        action: <str>
        mode: <str>
        command: <str>
```

## Route Maps

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>route_maps</samp>](## "route_maps") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "route_maps.[].name") | String | Required, Unique |  |  | Route-map Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "route_maps.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "route_maps.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "route_maps.[].sequence_numbers.[].type") | String | Required |  | Valid Values:<br>- permit<br>- deny |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "route_maps.[].sequence_numbers.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match</samp>](## "route_maps.[].sequence_numbers.[].match") | List, items: String |  |  |  | List of "match" statements |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "route_maps.[].sequence_numbers.[].match.[].&lt;str&gt;") | String |  |  |  | Match as string<br>Example: "ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set</samp>](## "route_maps.[].sequence_numbers.[].set") | List, items: String |  |  |  | List of "set" statements |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "route_maps.[].sequence_numbers.[].set.[].&lt;str&gt;") | String |  |  |  | Set as string<br>Example: "origin incomplete"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sub_route_map</samp>](## "route_maps.[].sequence_numbers.[].sub_route_map") | String |  |  |  | Name of Sub-Route-map |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue</samp>](## "route_maps.[].sequence_numbers.[].continue") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "route_maps.[].sequence_numbers.[].continue.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_number</samp>](## "route_maps.[].sequence_numbers.[].continue.sequence_number") | Integer |  |  |  |  |

### YAML

```yaml
route_maps:
  - name: <str>
    sequence_numbers:
      - sequence: <int>
        type: <str>
        description: <str>
        match:
          - <str>
        set:
          - <str>
        sub_route_map: <str>
        continue:
          enabled: <bool>
          sequence_number: <int>
```

## Router BFD

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>router_bfd</samp>](## "router_bfd") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;interval</samp>](## "router_bfd.interval") | Integer |  |  |  | Rate in milliseconds |
| [<samp>&nbsp;&nbsp;min_rx</samp>](## "router_bfd.min_rx") | Integer |  |  |  | Rate in milliseconds |
| [<samp>&nbsp;&nbsp;multiplier</samp>](## "router_bfd.multiplier") | Integer |  |  | Min: 3<br>Max: 50 |  |
| [<samp>&nbsp;&nbsp;multihop</samp>](## "router_bfd.multihop") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "router_bfd.multihop.interval") | Integer |  |  |  | Rate in milliseconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "router_bfd.multihop.min_rx") | Integer |  |  |  | Rate in milliseconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "router_bfd.multihop.multiplier") | Integer |  |  | Min: 3<br>Max: 50 |  |
| [<samp>&nbsp;&nbsp;sbfd</samp>](## "router_bfd.sbfd") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "router_bfd.sbfd.local_interface") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "router_bfd.sbfd.local_interface.name") | String |  |  |  | Interface Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocols</samp>](## "router_bfd.sbfd.local_interface.protocols") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "router_bfd.sbfd.local_interface.protocols.ipv4") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "router_bfd.sbfd.local_interface.protocols.ipv6") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;initiator_interval</samp>](## "router_bfd.sbfd.initiator_interval") | Integer |  |  |  | Rate in milliseconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;initiator_multiplier</samp>](## "router_bfd.sbfd.initiator_multiplier") | Integer |  |  | Min: 3<br>Max: 50 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;reflector</samp>](## "router_bfd.sbfd.reflector") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "router_bfd.sbfd.reflector.min_rx") | Integer |  |  |  | Rate in milliseconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_discriminator</samp>](## "router_bfd.sbfd.reflector.local_discriminator") | String |  |  |  | IPv4 address or 32 bit integer |

### YAML

```yaml
router_bfd:
  interval: <int>
  min_rx: <int>
  multiplier: <int>
  multihop:
    interval: <int>
    min_rx: <int>
    multiplier: <int>
  sbfd:
    local_interface:
      name: <str>
      protocols:
        ipv4: <bool>
        ipv6: <bool>
    initiator_interval: <int>
    initiator_multiplier: <int>
    reflector:
      min_rx: <int>
      local_discriminator: <str>
```

## Router BGP

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>router_bgp</samp>](## "router_bgp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;as</samp>](## "router_bgp.as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
| [<samp>&nbsp;&nbsp;router_id</samp>](## "router_bgp.router_id") | String |  |  |  | In IP address format A.B.C.D |
| [<samp>&nbsp;&nbsp;distance</samp>](## "router_bgp.distance") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;external_routes</samp>](## "router_bgp.distance.external_routes") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;internal_routes</samp>](## "router_bgp.distance.internal_routes") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local_routes</samp>](## "router_bgp.distance.local_routes") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;graceful_restart</samp>](## "router_bgp.graceful_restart") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.graceful_restart.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;restart_time</samp>](## "router_bgp.graceful_restart.restart_time") | Integer |  |  | Min: 1<br>Max: 3600 | Number of seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;stalepath_time</samp>](## "router_bgp.graceful_restart.stalepath_time") | Integer |  |  | Min: 1<br>Max: 3600 | Number of seconds |
| [<samp>&nbsp;&nbsp;graceful_restart_helper</samp>](## "router_bgp.graceful_restart_helper") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.graceful_restart_helper.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;restart_time</samp>](## "router_bgp.graceful_restart_helper.restart_time") | Integer |  |  | Min: 1<br>Max: 100000000 | Number of seconds<br>graceful-restart-help long-lived and restart-time are mutually exclusive in CLI.<br>restart-time will take precedence if both are configured.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;long_lived</samp>](## "router_bgp.graceful_restart_helper.long_lived") | Boolean |  |  |  | graceful-restart-help long-lived and restart-time are mutually exclusive in CLI.<br>restart-time will take precedence if both are configured.<br> |
| [<samp>&nbsp;&nbsp;maximum_paths</samp>](## "router_bgp.maximum_paths") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;paths</samp>](## "router_bgp.maximum_paths.paths") | Integer |  |  | Min: 1<br>Max: 600 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ecmp</samp>](## "router_bgp.maximum_paths.ecmp") | Integer |  |  | Min: 1<br>Max: 600 |  |
| [<samp>&nbsp;&nbsp;updates</samp>](## "router_bgp.updates") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;wait_for_convergence</samp>](## "router_bgp.updates.wait_for_convergence") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;wait_install</samp>](## "router_bgp.updates.wait_install") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;bgp_cluster_id</samp>](## "router_bgp.bgp_cluster_id") | String |  |  |  | IP Address A.B.C.D |
| [<samp>&nbsp;&nbsp;bgp_defaults</samp>](## "router_bgp.bgp_defaults") | List, items: String |  |  |  | BGP command as string |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.bgp_defaults.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;bgp</samp>](## "router_bgp.bgp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bestpath</samp>](## "router_bgp.bgp.bestpath") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d_path</samp>](## "router_bgp.bgp.bestpath.d_path") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;listen_ranges</samp>](## "router_bgp.listen_ranges") | List, items: Dictionary |  |  |  | Improved "listen_ranges" data model to support multiple listen ranges and additional filter capabilities<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.listen_ranges.[].prefix") | String |  |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_id_include_router_id</samp>](## "router_bgp.listen_ranges.[].peer_id_include_router_id") | Boolean |  |  |  | Include router ID as part of peer filter |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "router_bgp.listen_ranges.[].peer_group") | String |  |  |  | Peer group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "router_bgp.listen_ranges.[].peer_filter") | String |  |  |  | Peer-filter name<br>note: `peer_filter` or `remote_as` is required but mutually exclusive.<br>If both are defined, `peer_filter` takes precedence<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.listen_ranges.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
| [<samp>&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.peer_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "router_bgp.peer_groups.[].type") | String |  |  |  | Key only used for documentation or validation purposes |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.peer_groups.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "router_bgp.peer_groups.[].local_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_bgp.peer_groups.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "router_bgp.peer_groups.[].shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as</samp>](## "router_bgp.peer_groups.[].remove_private_as") | Dictionary |  |  |  | Remove private AS numbers in outbound AS path |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.peer_groups.[].remove_private_as.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "router_bgp.peer_groups.[].remove_private_as.all") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "router_bgp.peer_groups.[].remove_private_as.replace_as") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as_ingress</samp>](## "router_bgp.peer_groups.[].remove_private_as_ingress") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.peer_groups.[].remove_private_as_ingress.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "router_bgp.peer_groups.[].remove_private_as_ingress.replace_as") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "router_bgp.peer_groups.[].peer_filter") | String |  |  |  | Peer-filter name<br>note: `bgp_listen_range_prefix` and `peer_filter` will be deprecated in AVD v4.0<br>These should not be mixed with the new `listen_ranges` key above to avoid conflicts.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_unchanged</samp>](## "router_bgp.peer_groups.[].next_hop_unchanged") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "router_bgp.peer_groups.[].update_source") | String |  |  |  | IP address or interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_reflector_client</samp>](## "router_bgp.peer_groups.[].route_reflector_client") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "router_bgp.peer_groups.[].bfd") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "router_bgp.peer_groups.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "router_bgp.peer_groups.[].next_hop_self") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "router_bgp.peer_groups.[].password") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "router_bgp.peer_groups.[].default_originate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.peer_groups.[].default_originate.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_bgp.peer_groups.[].default_originate.always") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.peer_groups.[].default_originate.route_map") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "router_bgp.peer_groups.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)' |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "router_bgp.peer_groups.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_limit</samp>](## "router_bgp.peer_groups.[].maximum_routes_warning_limit") | String |  |  |  | Maximum number of routes after which a warning is issued (0 means never warn) or<br>Percentage of maximum number of routes at which to warn ("<1-100> percent")<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_only</samp>](## "router_bgp.peer_groups.[].maximum_routes_warning_only") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_bandwidth</samp>](## "router_bgp.peer_groups.[].link_bandwidth") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.peer_groups.[].link_bandwidth.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "router_bgp.peer_groups.[].link_bandwidth.default") | String |  |  |  | nn.nn(K|M|G) link speed in bits/second |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowas_in</samp>](## "router_bgp.peer_groups.[].allowas_in") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.peer_groups.[].allowas_in.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;times</samp>](## "router_bgp.peer_groups.[].allowas_in.times") | Integer |  |  | Min: 1<br>Max: 10 | Number of local ASNs allowed in a BGP update |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "router_bgp.peer_groups.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "router_bgp.peer_groups.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rib_in_pre_policy_retain</samp>](## "router_bgp.peer_groups.[].rib_in_pre_policy_retain") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.peer_groups.[].rib_in_pre_policy_retain.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "router_bgp.peer_groups.[].rib_in_pre_policy_retain.all") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_listen_range_prefix</samp>](## "router_bgp.peer_groups.[].bgp_listen_range_prefix") | String |  |  |  | IP prefix range<br>note: `bgp_listen_range_prefix` and `peer_filter` will be deprecated in AVD v4.0<br>These should not be mixed with the new `listen_ranges` key above to avoid conflicts.<br> |
| [<samp>&nbsp;&nbsp;neighbors</samp>](## "router_bgp.neighbors") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "router_bgp.neighbors.[].peer_group") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.neighbors.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "router_bgp.neighbors.[].local_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_bgp.neighbors.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_reflector_client</samp>](## "router_bgp.neighbors.[].route_reflector_client") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "router_bgp.neighbors.[].shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "router_bgp.neighbors.[].update_source") | String |  |  |  | Source Interface |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "router_bgp.neighbors.[].bfd") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "router_bgp.neighbors.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "router_bgp.neighbors.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "router_bgp.neighbors.[].default_originate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.neighbors.[].default_originate.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_bgp.neighbors.[].default_originate.always") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.neighbors.[].default_originate.route_map") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "router_bgp.neighbors.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)' |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "router_bgp.neighbors.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_limit</samp>](## "router_bgp.neighbors.[].maximum_routes_warning_limit") | String |  |  |  | Maximum number of routes after which a warning is issued (0 means never warn) or<br>Percentage of maximum number of routes at which to warn ("<1-100> percent")<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_only</samp>](## "router_bgp.neighbors.[].maximum_routes_warning_only") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowas_in</samp>](## "router_bgp.neighbors.[].allowas_in") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.neighbors.[].allowas_in.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;times</samp>](## "router_bgp.neighbors.[].allowas_in.times") | Integer |  |  | Min: 1<br>Max: 10 | Number of local ASNs allowed in a BGP update |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "router_bgp.neighbors.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "router_bgp.neighbors.[].next_hop_self") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_bandwidth</samp>](## "router_bgp.neighbors.[].link_bandwidth") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.neighbors.[].link_bandwidth.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "router_bgp.neighbors.[].link_bandwidth.default") | String |  |  |  | nn.nn(K|M|G) link speed in bits/second |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rib_in_pre_policy_retain</samp>](## "router_bgp.neighbors.[].rib_in_pre_policy_retain") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.neighbors.[].rib_in_pre_policy_retain.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "router_bgp.neighbors.[].rib_in_pre_policy_retain.all") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as</samp>](## "router_bgp.neighbors.[].remove_private_as") | Dictionary |  |  |  | Remove private AS numbers in outbound AS path |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.neighbors.[].remove_private_as.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "router_bgp.neighbors.[].remove_private_as.all") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "router_bgp.neighbors.[].remove_private_as.replace_as") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as_ingress</samp>](## "router_bgp.neighbors.[].remove_private_as_ingress") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.neighbors.[].remove_private_as_ingress.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "router_bgp.neighbors.[].remove_private_as_ingress.replace_as") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;neighbor_interfaces</samp>](## "router_bgp.neighbor_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.neighbor_interfaces.[].name") | String | Required, Unique |  |  | Interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.neighbor_interfaces.[].remote_as") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "router_bgp.neighbor_interfaces.[].peer_group") | String |  | Peer-group name |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_bgp.neighbor_interfaces.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "router_bgp.neighbor_interfaces.[].peer_filter") | String |  |  |  | Peer-filter name |
| [<samp>&nbsp;&nbsp;aggregate_addresses</samp>](## "router_bgp.aggregate_addresses") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.aggregate_addresses.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;advertise_only</samp>](## "router_bgp.aggregate_addresses.[].advertise_only") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_set</samp>](## "router_bgp.aggregate_addresses.[].as_set") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary_only</samp>](## "router_bgp.aggregate_addresses.[].summary_only") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attribute_map</samp>](## "router_bgp.aggregate_addresses.[].attribute_map") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_map</samp>](## "router_bgp.aggregate_addresses.[].match_map") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.redistribute_routes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- source_protocol</samp>](## "router_bgp.redistribute_routes.[].source_protocol") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.redistribute_routes.[].route_map") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;vlan_aware_bundles</samp>](## "router_bgp.vlan_aware_bundles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.vlan_aware_bundles.[].name") | String | Required, Unique |  |  | VLAN aware bundle name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp>](## "router_bgp.vlan_aware_bundles.[].tenant") | String |  |  |  | Key only used for documentation or validation purposes |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_bgp.vlan_aware_bundles.[].description") | String |  |  |  | Key only used for documentation or validation purposes |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp>](## "router_bgp.vlan_aware_bundles.[].rd") | String |  |  |  | Route distinguisher |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd_evpn_domain</samp>](## "router_bgp.vlan_aware_bundles.[].rd_evpn_domain") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "router_bgp.vlan_aware_bundles.[].rd_evpn_domain.domain") | String |  |  | Valid Values:<br>- remote<br>- all |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp>](## "router_bgp.vlan_aware_bundles.[].rd_evpn_domain.rd") | String |  |  |  | Route distinguisher |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;both</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.both") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.both.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.export") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.export.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_evpn_domains</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import_evpn_domains") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- domain</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import_evpn_domains.[].domain") | String |  |  | Valid Values:<br>- remote<br>- all |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import_evpn_domains.[].route_target") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export_evpn_domains</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.export_evpn_domains") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- domain</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.export_evpn_domains.[].domain") | String |  |  | Valid Values:<br>- remote<br>- all |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.export_evpn_domains.[].route_target") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_export_evpn_domains</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import_export_evpn_domains") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- domain</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import_export_evpn_domains.[].domain") | String |  |  | Valid Values:<br>- remote<br>- all |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import_export_evpn_domains.[].route_target") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.vlan_aware_bundles.[].redistribute_routes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vlan_aware_bundles.[].redistribute_routes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_redistribute_routes</samp>](## "router_bgp.vlan_aware_bundles.[].no_redistribute_routes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vlan_aware_bundles.[].no_redistribute_routes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "router_bgp.vlan_aware_bundles.[].vlan") | String |  |  |  | VLAN range as string. Example "100-200,300" |
| [<samp>&nbsp;&nbsp;vlans</samp>](## "router_bgp.vlans") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "router_bgp.vlans.[].id") | Integer | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp>](## "router_bgp.vlans.[].tenant") | String |  |  |  | Key only used for documentation or validation purposes |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp>](## "router_bgp.vlans.[].rd") | String |  |  |  | Route distinguisher |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd_evpn_domain</samp>](## "router_bgp.vlans.[].rd_evpn_domain") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "router_bgp.vlans.[].rd_evpn_domain.domain") | String |  |  | Valid Values:<br>- remote<br>- all |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp>](## "router_bgp.vlans.[].rd_evpn_domain.rd") | String |  |  |  | Route distinguisher |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "router_bgp.vlans.[].eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp>](## "router_bgp.vlans.[].route_targets") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;both</samp>](## "router_bgp.vlans.[].route_targets.both") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vlans.[].route_targets.both.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import</samp>](## "router_bgp.vlans.[].route_targets.import") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vlans.[].route_targets.import.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export</samp>](## "router_bgp.vlans.[].route_targets.export") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vlans.[].route_targets.export.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_evpn_domains</samp>](## "router_bgp.vlans.[].route_targets.import_evpn_domains") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- domain</samp>](## "router_bgp.vlans.[].route_targets.import_evpn_domains.[].domain") | String |  |  | Valid Values:<br>- remote<br>- all |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "router_bgp.vlans.[].route_targets.import_evpn_domains.[].route_target") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export_evpn_domains</samp>](## "router_bgp.vlans.[].route_targets.export_evpn_domains") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- domain</samp>](## "router_bgp.vlans.[].route_targets.export_evpn_domains.[].domain") | String |  |  | Valid Values:<br>- remote<br>- all |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "router_bgp.vlans.[].route_targets.export_evpn_domains.[].route_target") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_export_evpn_domains</samp>](## "router_bgp.vlans.[].route_targets.import_export_evpn_domains") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- domain</samp>](## "router_bgp.vlans.[].route_targets.import_export_evpn_domains.[].domain") | String |  |  | Valid Values:<br>- remote<br>- all |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "router_bgp.vlans.[].route_targets.import_export_evpn_domains.[].route_target") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.vlans.[].redistribute_routes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vlans.[].redistribute_routes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_redistribute_routes</samp>](## "router_bgp.vlans.[].no_redistribute_routes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vlans.[].no_redistribute_routes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;vpws</samp>](## "router_bgp.vpws") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.vpws.[].name") | String | Required, Unique |  |  | VPWS instance name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp>](## "router_bgp.vpws.[].rd") | String |  |  |  | Route distinguisher |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp>](## "router_bgp.vpws.[].route_targets") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_export</samp>](## "router_bgp.vpws.[].route_targets.import_export") | String |  |  |  | Route Target |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_control_word</samp>](## "router_bgp.vpws.[].mpls_control_word") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label_flow</samp>](## "router_bgp.vpws.[].label_flow") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "router_bgp.vpws.[].mtu") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pseudowires</samp>](## "router_bgp.vpws.[].pseudowires") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.vpws.[].pseudowires.[].name") | String | Required, Unique |  |  | Pseudowire name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id_local</samp>](## "router_bgp.vpws.[].pseudowires.[].id_local") | Integer |  |  |  | Must match id_remote on other pe |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id_remote</samp>](## "router_bgp.vpws.[].pseudowires.[].id_remote") | Integer |  |  |  | Must match id_local on other pe |
| [<samp>&nbsp;&nbsp;address_family_evpn</samp>](## "router_bgp.address_family_evpn") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;domain_identifier</samp>](## "router_bgp.address_family_evpn.domain_identifier") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbor_default</samp>](## "router_bgp.address_family_evpn.neighbor_default") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation</samp>](## "router_bgp.address_family_evpn.neighbor_default.encapsulation") | String |  |  | Valid Values:<br>- vxlan<br>- mpls |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self_source_interface</samp>](## "router_bgp.address_family_evpn.neighbor_default.next_hop_self_source_interface") | String |  |  |  | Source interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self_received_evpn_routes</samp>](## "router_bgp.address_family_evpn.neighbor_default.next_hop_self_received_evpn_routes") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "router_bgp.address_family_evpn.neighbor_default.next_hop_self_received_evpn_routes.enable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "router_bgp.address_family_evpn.neighbor_default.next_hop_self_received_evpn_routes.inter_domain") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_evpn.peer_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.address_family_evpn.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_evpn.peer_groups.[].activate") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_evpn.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_evpn.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain_remote</samp>](## "router_bgp.address_family_evpn.peer_groups.[].domain_remote") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_hostflap_detection</samp>](## "router_bgp.address_family_evpn.evpn_hostflap_detection") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_evpn.evpn_hostflap_detection.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;window</samp>](## "router_bgp.address_family_evpn.evpn_hostflap_detection.window") | Integer |  |  | Min: 0<br>Max: 4294967295 | Time (in seconds) to detect a MAC duplication issue |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "router_bgp.address_family_evpn.evpn_hostflap_detection.threshold") | Integer |  |  | Min: 0<br>Max: 4294967295 | Minimum number of MAC moves that indicate a MAC Duplication issue |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expiry_timeout</samp>](## "router_bgp.address_family_evpn.evpn_hostflap_detection.expiry_timeout") | Integer |  |  | Min: 0<br>Max: 4294967295 | Time (in seconds) to purge a MAC duplication issue |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;route</samp>](## "router_bgp.address_family_evpn.route") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_match_failure_action</samp>](## "router_bgp.address_family_evpn.route.import_match_failure_action") | String |  |  | Valid Values:<br>- discard |  |
| [<samp>&nbsp;&nbsp;address_family_rtc</samp>](## "router_bgp.address_family_rtc") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_rtc.peer_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.address_family_rtc.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_rtc.peer_groups.[].activate") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_route_target</samp>](## "router_bgp.address_family_rtc.peer_groups.[].default_route_target") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;only</samp>](## "router_bgp.address_family_rtc.peer_groups.[].default_route_target.only") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encoding_origin_as_omit</samp>](## "router_bgp.address_family_rtc.peer_groups.[].default_route_target.encoding_origin_as_omit") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;address_family_ipv4</samp>](## "router_bgp.address_family_ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.address_family_ipv4.networks") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.address_family_ipv4.networks.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.networks.[].route_map") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_ipv4.peer_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].activate") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].default_originate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].default_originate.always") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].default_originate.route_map") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].next_hop") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6_originate</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].next_hop.address_family_ipv6_originate") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].prefix_list_in") | String |  |  |  | Inbound prefix-list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].prefix_list_out") | String |  |  |  | Outbound prefix-list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_ipv4.neighbors") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.address_family_ipv4.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv4.neighbors.[].activate") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv4.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv4.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "router_bgp.address_family_ipv4.neighbors.[].prefix_list_in") | String |  |  |  | Inbound prefix-list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "router_bgp.address_family_ipv4.neighbors.[].prefix_list_out") | String |  |  |  | Prefix-list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "router_bgp.address_family_ipv4.neighbors.[].default_originate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_bgp.address_family_ipv4.neighbors.[].default_originate.always") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.neighbors.[].default_originate.route_map") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;address_family_ipv4_multicast</samp>](## "router_bgp.address_family_ipv4_multicast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_ipv4_multicast.peer_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.address_family_ipv4_multicast.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv4_multicast.peer_groups.[].activate") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv4_multicast.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv4_multicast.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_ipv4_multicast.neighbors") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.address_family_ipv4_multicast.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv4_multicast.neighbors.[].activate") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv4_multicast.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv4_multicast.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute_routes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- source_protocol</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute_routes.[].source_protocol") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute_routes.[].route_map") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;address_family_ipv6</samp>](## "router_bgp.address_family_ipv6") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.address_family_ipv6.networks") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.address_family_ipv6.networks.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6.networks.[].route_map") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_ipv6.peer_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].activate") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].prefix_list_in") | String |  |  |  | Inbound prefix-list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].prefix_list_out") | String |  |  |  | Outbound prefix-list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_ipv6.neighbors") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.address_family_ipv6.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv6.neighbors.[].activate") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv6.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv6.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "router_bgp.address_family_ipv6.neighbors.[].prefix_list_in") | String |  |  |  | Inbound prefix-list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "router_bgp.address_family_ipv6.neighbors.[].prefix_list_out") | String |  |  |  | Outbound prefix-list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.address_family_ipv6.redistribute_routes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- source_protocol</samp>](## "router_bgp.address_family_ipv6.redistribute_routes.[].source_protocol") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6.redistribute_routes.[].route_map") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;address_family_vpn_ipv4</samp>](## "router_bgp.address_family_vpn_ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;domain_identifier</samp>](## "router_bgp.address_family_vpn_ipv4.domain_identifier") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups.[].activate") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;route</samp>](## "router_bgp.address_family_vpn_ipv4.route") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_match_failure_action</samp>](## "router_bgp.address_family_vpn_ipv4.route.import_match_failure_action") | String |  |  | Valid Values:<br>- discard |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors.[].activate") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbor_default_encapsulation_mpls_next_hop_self</samp>](## "router_bgp.address_family_vpn_ipv4.neighbor_default_encapsulation_mpls_next_hop_self") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "router_bgp.address_family_vpn_ipv4.neighbor_default_encapsulation_mpls_next_hop_self.source_interface") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;address_family_vpn_ipv6</samp>](## "router_bgp.address_family_vpn_ipv6") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;domain_identifier</samp>](## "router_bgp.address_family_vpn_ipv6.domain_identifier") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups.[].activate") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;route</samp>](## "router_bgp.address_family_vpn_ipv6.route") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_match_failure_action</samp>](## "router_bgp.address_family_vpn_ipv6.route.import_match_failure_action") | String |  |  | Valid Values:<br>- discard |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors.[].activate") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbor_default_encapsulation_mpls_next_hop_self</samp>](## "router_bgp.address_family_vpn_ipv6.neighbor_default_encapsulation_mpls_next_hop_self") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "router_bgp.address_family_vpn_ipv6.neighbor_default_encapsulation_mpls_next_hop_self.source_interface") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_bgp.vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.vrfs.[].name") | String | Required, Unique |  |  | VRF name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp>](## "router_bgp.vrfs.[].rd") | String |  |  |  | Route distinguisher |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_multicast</samp>](## "router_bgp.vrfs.[].evpn_multicast") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_multicast_address_family</samp>](## "router_bgp.vrfs.[].evpn_multicast_address_family") | Dictionary |  |  |  | Enable per-AF EVPN multicast settings |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "router_bgp.vrfs.[].evpn_multicast_address_family.ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transit</samp>](## "router_bgp.vrfs.[].evpn_multicast_address_family.ipv4.transit") | Boolean |  |  |  | Enable EVPN multicast transit mode |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp>](## "router_bgp.vrfs.[].route_targets") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import</samp>](## "router_bgp.vrfs.[].route_targets.import") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address_family</samp>](## "router_bgp.vrfs.[].route_targets.import.[].address_family") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp>](## "router_bgp.vrfs.[].route_targets.import.[].route_targets") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vrfs.[].route_targets.import.[].route_targets.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export</samp>](## "router_bgp.vrfs.[].route_targets.export") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address_family</samp>](## "router_bgp.vrfs.[].route_targets.export.[].address_family") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp>](## "router_bgp.vrfs.[].route_targets.export.[].route_targets") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vrfs.[].route_targets.export.[].route_targets.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "router_bgp.vrfs.[].router_id") | String |  |  |  | in IP address format A.B.C.D |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "router_bgp.vrfs.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.vrfs.[].networks") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.vrfs.[].networks.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].networks.[].route_map") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;listen_ranges</samp>](## "router_bgp.vrfs.[].listen_ranges") | List, items: Dictionary |  |  |  | Improved "listen_ranges" data model to support multiple listen ranges and additional filter capabilities<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.vrfs.[].listen_ranges.[].prefix") | String |  |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_id_include_router_id</samp>](## "router_bgp.vrfs.[].listen_ranges.[].peer_id_include_router_id") | Boolean |  |  |  | Include router ID as part of peer filter |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "router_bgp.vrfs.[].listen_ranges.[].peer_group") | String |  |  |  | Peer-group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "router_bgp.vrfs.[].listen_ranges.[].peer_filter") | String |  |  |  | Peer-filter name<br>note: `peer_filter`` or `remote_as` is required but mutually exclusive.<br>If both are defined, peer_filter takes precedence<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.vrfs.[].listen_ranges.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.vrfs.[].neighbors") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.vrfs.[].neighbors.[].ip_address") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "router_bgp.vrfs.[].neighbors.[].peer_group") | String |  |  |  | Peer-group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.vrfs.[].neighbors.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "router_bgp.vrfs.[].neighbors.[].password") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as") | Dictionary |  |  |  | Remove private AS numbers in outbound AS path |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as.all") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as.replace_as") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as_ingress</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as_ingress") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as_ingress.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as_ingress.replace_as") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "router_bgp.vrfs.[].neighbors.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "router_bgp.vrfs.[].neighbors.[].local_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_bgp.vrfs.[].neighbors.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "router_bgp.vrfs.[].neighbors.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "router_bgp.vrfs.[].neighbors.[].next_hop_self") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "router_bgp.vrfs.[].neighbors.[].shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "router_bgp.vrfs.[].neighbors.[].bfd") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "router_bgp.vrfs.[].neighbors.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rib_in_pre_policy_retain</samp>](## "router_bgp.vrfs.[].neighbors.[].rib_in_pre_policy_retain") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].neighbors.[].rib_in_pre_policy_retain.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "router_bgp.vrfs.[].neighbors.[].rib_in_pre_policy_retain.all") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "router_bgp.vrfs.[].neighbors.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)' |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "router_bgp.vrfs.[].neighbors.[].maximum_routes") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_limit</samp>](## "router_bgp.vrfs.[].neighbors.[].maximum_routes_warning_limit") | String |  |  |  | Maximum number of routes after which a warning is issued (0 means never warn) or<br>Percentage of maximum number of routes at which to warn ("<1-100> percent")<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_only</samp>](## "router_bgp.vrfs.[].neighbors.[].maximum_routes_warning_only") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowas_in</samp>](## "router_bgp.vrfs.[].neighbors.[].allowas_in") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].neighbors.[].allowas_in.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;times</samp>](## "router_bgp.vrfs.[].neighbors.[].allowas_in.times") | Integer |  |  | Min: 1<br>Max: 10 | Number of local ASNs allowed in a BGP update |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "router_bgp.vrfs.[].neighbors.[].default_originate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].neighbors.[].default_originate.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_bgp.vrfs.[].neighbors.[].default_originate.always") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].neighbors.[].default_originate.route_map") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "router_bgp.vrfs.[].neighbors.[].update_source") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.vrfs.[].neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.vrfs.[].neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "router_bgp.vrfs.[].neighbors.[].prefix_list_in") | String |  |  |  | Inbound prefix-list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "router_bgp.vrfs.[].neighbors.[].prefix_list_out") | String |  |  |  | Outbound prefix-list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbor_interfaces</samp>](## "router_bgp.vrfs.[].neighbor_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.vrfs.[].neighbor_interfaces.[].name") | String | Required, Unique |  |  | Interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.vrfs.[].neighbor_interfaces.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "router_bgp.vrfs.[].neighbor_interfaces.[].peer_group") | String |  |  |  | Peer-group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "router_bgp.vrfs.[].neighbor_interfaces.[].peer_filter") | String |  |  |  | Peer-filter name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_bgp.vrfs.[].neighbor_interfaces.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.vrfs.[].redistribute_routes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- source_protocol</samp>](## "router_bgp.vrfs.[].redistribute_routes.[].source_protocol") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].redistribute_routes.[].route_map") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;aggregate_addresses</samp>](## "router_bgp.vrfs.[].aggregate_addresses") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;advertise_only</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].advertise_only") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_set</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].as_set") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary_only</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].summary_only") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attribute_map</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].attribute_map") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_map</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].match_map") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "router_bgp.vrfs.[].address_families") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address_family</samp>](## "router_bgp.vrfs.[].address_families.[].address_family") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.vrfs.[].address_families.[].bgp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.vrfs.[].address_families.[].bgp.missing_policy") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.vrfs.[].address_families.[].bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.vrfs.[].address_families.[].bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.vrfs.[].address_families.[].bgp.additional_paths") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vrfs.[].address_families.[].bgp.additional_paths.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.vrfs.[].address_families.[].neighbors") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.vrfs.[].address_families.[].neighbors.[].ip_address") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.vrfs.[].address_families.[].neighbors.[].activate") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.vrfs.[].address_families.[].neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.vrfs.[].address_families.[].neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.vrfs.[].address_families.[].peer_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.vrfs.[].address_families.[].peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.vrfs.[].address_families.[].peer_groups.[].activate") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop</samp>](## "router_bgp.vrfs.[].address_families.[].peer_groups.[].next_hop") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6_originate</samp>](## "router_bgp.vrfs.[].address_families.[].peer_groups.[].next_hop.address_family_ipv6_originate") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.vrfs.[].address_families.[].networks") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.vrfs.[].address_families.[].networks.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_families.[].networks.[].route_map") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "router_bgp.vrfs.[].eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the Router BGP, VRF definition in the final EOS configuration |

### YAML

```yaml
router_bgp:
  as: <str>
  router_id: <str>
  distance:
    external_routes: <int>
    internal_routes: <int>
    local_routes: <int>
  graceful_restart:
    enabled: <bool>
    restart_time: <int>
    stalepath_time: <int>
  graceful_restart_helper:
    enabled: <bool>
    restart_time: <int>
    long_lived: <bool>
  maximum_paths:
    paths: <int>
    ecmp: <int>
  updates:
    wait_for_convergence: <bool>
    wait_install: <bool>
  bgp_cluster_id: <str>
  bgp_defaults:
    - <str>
  bgp:
    bestpath:
      d_path: <bool>
  listen_ranges:
    - prefix: <str>
      peer_id_include_router_id: <bool>
      peer_group: <str>
      peer_filter: <str>
      remote_as: <str>
  peer_groups:
    - name: <str>
      type: <str>
      remote_as: <str>
      local_as: <str>
      description: <str>
      shutdown: <bool>
      remove_private_as:
        enabled: <bool>
        all: <bool>
        replace_as: <bool>
      remove_private_as_ingress:
        enabled: <bool>
        replace_as: <bool>
      peer_filter: <str>
      next_hop_unchanged: <bool>
      update_source: <str>
      route_reflector_client: <bool>
      bfd: <bool>
      ebgp_multihop: <int>
      next_hop_self: <bool>
      password: <str>
      default_originate:
        enabled: <bool>
        always: <bool>
        route_map: <str>
      send_community: <str>
      maximum_routes: <int>
      maximum_routes_warning_limit: <str>
      maximum_routes_warning_only: <bool>
      link_bandwidth:
        enabled: <bool>
        default: <str>
      allowas_in:
        enabled: <bool>
        times: <int>
      weight: <int>
      timers: <str>
      rib_in_pre_policy_retain:
        enabled: <bool>
        all: <bool>
      route_map_in: <str>
      route_map_out: <str>
      bgp_listen_range_prefix: <str>
  neighbors:
    - ip_address: <str>
      peer_group: <str>
      remote_as: <str>
      local_as: <str>
      description: <str>
      route_reflector_client: <bool>
      shutdown: <bool>
      update_source: <str>
      bfd: <bool>
      weight: <int>
      timers: <str>
      route_map_in: <str>
      route_map_out: <str>
      default_originate:
        enabled: <bool>
        always: <bool>
        route_map: <str>
      send_community: <str>
      maximum_routes: <int>
      maximum_routes_warning_limit: <str>
      maximum_routes_warning_only: <bool>
      allowas_in:
        enabled: <bool>
        times: <int>
      ebgp_multihop: <int>
      next_hop_self: <bool>
      link_bandwidth:
        enabled: <bool>
        default: <str>
      rib_in_pre_policy_retain:
        enabled: <bool>
        all: <bool>
      remove_private_as:
        enabled: <bool>
        all: <bool>
        replace_as: <bool>
      remove_private_as_ingress:
        enabled: <bool>
        replace_as: <bool>
  neighbor_interfaces:
    - name: <str>
      remote_as: <str>
      peer_group: <str>
      description: <str>
      peer_filter: <str>
  aggregate_addresses:
    - prefix: <str>
      advertise_only: <bool>
      as_set: <bool>
      summary_only: <bool>
      attribute_map: <str>
      match_map: <str>
  redistribute_routes:
    - source_protocol: <str>
      route_map: <str>
  vlan_aware_bundles:
    - name: <str>
      tenant: <str>
      description: <str>
      rd: <str>
      rd_evpn_domain:
        domain: <str>
        rd: <str>
      route_targets:
        both:
          - <str>
        import:
          - <str>
        export:
          - <str>
        import_evpn_domains:
          - domain: <str>
            route_target: <str>
        export_evpn_domains:
          - domain: <str>
            route_target: <str>
        import_export_evpn_domains:
          - domain: <str>
            route_target: <str>
      redistribute_routes:
        - <str>
      no_redistribute_routes:
        - <str>
      vlan: <str>
  vlans:
    - id: <int>
      tenant: <str>
      rd: <str>
      rd_evpn_domain:
        domain: <str>
        rd: <str>
      eos_cli: <str>
      route_targets:
        both:
          - <str>
        import:
          - <str>
        export:
          - <str>
        import_evpn_domains:
          - domain: <str>
            route_target: <str>
        export_evpn_domains:
          - domain: <str>
            route_target: <str>
        import_export_evpn_domains:
          - domain: <str>
            route_target: <str>
      redistribute_routes:
        - <str>
      no_redistribute_routes:
        - <str>
  vpws:
    - name: <str>
      rd: <str>
      route_targets:
        import_export: <str>
      mpls_control_word: <bool>
      label_flow: <bool>
      mtu: <int>
      pseudowires:
        - name: <str>
          id_local: <int>
          id_remote: <int>
  address_family_evpn:
    domain_identifier: <str>
    neighbor_default:
      encapsulation: <str>
      next_hop_self_source_interface: <str>
      next_hop_self_received_evpn_routes:
        enable: <bool>
        inter_domain: <bool>
    peer_groups:
      - name: <str>
        activate: <bool>
        route_map_in: <str>
        route_map_out: <str>
        domain_remote: <bool>
    evpn_hostflap_detection:
      enabled: <bool>
      window: <int>
      threshold: <int>
      expiry_timeout: <int>
    route:
      import_match_failure_action: <str>
  address_family_rtc:
    peer_groups:
      - name: <str>
        activate: <bool>
        default_route_target:
          only: <bool>
          encoding_origin_as_omit: <str>
  address_family_ipv4:
    networks:
      - prefix: <str>
        route_map: <str>
    peer_groups:
      - name: <str>
        activate: <bool>
        route_map_in: <str>
        route_map_out: <str>
        default_originate:
          always: <bool>
          route_map: <str>
        next_hop:
          address_family_ipv6_originate: <bool>
        prefix_list_in: <str>
        prefix_list_out: <str>
    neighbors:
      - ip_address: <str>
        activate: <bool>
        route_map_in: <str>
        route_map_out: <str>
        prefix_list_in: <str>
        prefix_list_out: <str>
        default_originate:
          always: <bool>
          route_map: <str>
  address_family_ipv4_multicast:
    peer_groups:
      - name: <str>
        activate: <bool>
        route_map_in: <str>
        route_map_out: <str>
    neighbors:
      - ip_address: <str>
        activate: <bool>
        route_map_in: <str>
        route_map_out: <str>
    redistribute_routes:
      - source_protocol: <str>
        route_map: <str>
  address_family_ipv6:
    networks:
      - prefix: <str>
        route_map: <str>
    peer_groups:
      - name: <str>
        activate: <bool>
        route_map_in: <str>
        route_map_out: <str>
        prefix_list_in: <str>
        prefix_list_out: <str>
    neighbors:
      - ip_address: <str>
        activate: <bool>
        route_map_in: <str>
        route_map_out: <str>
        prefix_list_in: <str>
        prefix_list_out: <str>
    redistribute_routes:
      - source_protocol: <str>
        route_map: <str>
  address_family_vpn_ipv4:
    domain_identifier: <str>
    peer_groups:
      - name: <str>
        activate: <bool>
        route_map_in: <str>
        route_map_out: <str>
    route:
      import_match_failure_action: <str>
    neighbors:
      - ip_address: <str>
        activate: <bool>
        route_map_in: <str>
        route_map_out: <str>
    neighbor_default_encapsulation_mpls_next_hop_self:
      source_interface: <str>
  address_family_vpn_ipv6:
    domain_identifier: <str>
    peer_groups:
      - name: <str>
        activate: <bool>
        route_map_in: <str>
        route_map_out: <str>
    route:
      import_match_failure_action: <str>
    neighbors:
      - ip_address: <str>
        activate: <bool>
        route_map_in: <str>
        route_map_out: <str>
    neighbor_default_encapsulation_mpls_next_hop_self:
      source_interface: <str>
  vrfs:
    - name: <str>
      rd: <str>
      evpn_multicast: <bool>
      evpn_multicast_address_family:
        ipv4:
          transit: <bool>
      route_targets:
        import:
          - address_family: <str>
            route_targets:
              - <str>
        export:
          - address_family: <str>
            route_targets:
              - <str>
      router_id: <str>
      timers: <str>
      networks:
        - prefix: <str>
          route_map: <str>
      listen_ranges:
        - prefix: <str>
          peer_id_include_router_id: <bool>
          peer_group: <str>
          peer_filter: <str>
          remote_as: <str>
      neighbors:
        - ip_address: <str>
          peer_group: <str>
          remote_as: <str>
          password: <str>
          remove_private_as:
            enabled: <bool>
            all: <bool>
            replace_as: <bool>
          remove_private_as_ingress:
            enabled: <bool>
            replace_as: <bool>
          weight: <int>
          local_as: <str>
          description: <str>
          ebgp_multihop: <int>
          next_hop_self: <bool>
          shutdown: <bool>
          bfd: <bool>
          timers: <str>
          rib_in_pre_policy_retain:
            enabled: <bool>
            all: <bool>
          send_community: <str>
          maximum_routes: <int>
          maximum_routes_warning_limit: <str>
          maximum_routes_warning_only: <bool>
          allowas_in:
            enabled: <bool>
            times: <int>
          default_originate:
            enabled: <bool>
            always: <bool>
            route_map: <str>
          update_source: <str>
          route_map_in: <str>
          route_map_out: <str>
          prefix_list_in: <str>
          prefix_list_out: <str>
      neighbor_interfaces:
        - name: <str>
          remote_as: <str>
          peer_group: <str>
          peer_filter: <str>
          description: <str>
      redistribute_routes:
        - source_protocol: <str>
          route_map: <str>
      aggregate_addresses:
        - prefix: <str>
          advertise_only: <bool>
          as_set: <bool>
          summary_only: <bool>
          attribute_map: <str>
          match_map: <str>
      address_families:
        - address_family: <str>
          bgp:
            missing_policy:
              direction_in_action: <str>
              direction_out_action: <str>
            additional_paths:
              - <str>
          neighbors:
            - ip_address: <str>
              activate: <bool>
              route_map_in: <str>
              route_map_out: <str>
          peer_groups:
            - name: <str>
              activate: <bool>
              next_hop:
                address_family_ipv6_originate: <bool>
          networks:
            - prefix: <str>
              route_map: <str>
      eos_cli: <str>
```

## Router General configuration

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>router_general</samp>](## "router_general") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;router_id</samp>](## "router_general.router_id") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "router_general.router_id.ipv4") | String |  |  |  | IPv4 Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "router_general.router_id.ipv6") | String |  |  |  | IPv6 Address |
| [<samp>&nbsp;&nbsp;nexthop_fast_failover</samp>](## "router_general.nexthop_fast_failover") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_general.vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_general.vrfs.[].name") | String | Required, Unique |  |  | Destination-VRF |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;leak_routes</samp>](## "router_general.vrfs.[].leak_routes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- source_vrf</samp>](## "router_general.vrfs.[].leak_routes.[].source_vrf") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subscribe_policy</samp>](## "router_general.vrfs.[].leak_routes.[].subscribe_policy") | String |  |  |  | Route-Map Policy |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routes</samp>](## "router_general.vrfs.[].routes") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic_prefix_lists</samp>](## "router_general.vrfs.[].routes.dynamic_prefix_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_general.vrfs.[].routes.dynamic_prefix_lists.[].name") | String |  |  |  | Dynamic Prefix List Name |

### YAML

```yaml
router_general:
  router_id:
    ipv4: <str>
    ipv6: <str>
  nexthop_fast_failover: <bool>
  vrfs:
    - name: <str>
      leak_routes:
        - source_vrf: <str>
          subscribe_policy: <str>
      routes:
        dynamic_prefix_lists:
          - name: <str>
```

## Router IGMP Configuration

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>router_igmp</samp>](## "router_igmp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;ssm_aware</samp>](## "router_igmp.ssm_aware") | Boolean |  |  |  |  |

### YAML

```yaml
router_igmp:
  ssm_aware: <bool>
```

## Router ISIS

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>router_isis</samp>](## "router_isis") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;instance</samp>](## "router_isis.instance") | String |  |  |  | ISIS Instance Name |
| [<samp>&nbsp;&nbsp;net</samp>](## "router_isis.net") | String |  |  |  | CLNS Address like "49.0001.0001.0000.0001.00" |
| [<samp>&nbsp;&nbsp;router_id</samp>](## "router_isis.router_id") | String |  |  |  | IPv4 Address |
| [<samp>&nbsp;&nbsp;is_type</samp>](## "router_isis.is_type") | String |  |  | Valid Values:<br>- level-1<br>- level-1-2<br>- level-2 |  |
| [<samp>&nbsp;&nbsp;log_adjacency_changes</samp>](## "router_isis.log_adjacency_changes") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;mpls_ldp_sync_default</samp>](## "router_isis.mpls_ldp_sync_default") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;timers</samp>](## "router_isis.timers") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local_convergence</samp>](## "router_isis.timers.local_convergence") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protected_prefixes</samp>](## "router_isis.timers.local_convergence.protected_prefixes") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "router_isis.timers.local_convergence.delay") | Integer |  | 10000 |  | Delay in milliseconds. |
| [<samp>&nbsp;&nbsp;advertise</samp>](## "router_isis.advertise") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;passive_only</samp>](## "router_isis.advertise.passive_only") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;address_family</samp>](## "router_isis.address_family") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_isis.address_family.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- ipv4<br>- ipv6<br>- ipv4 unicast<br>- ipv6 unicast | Address Family |
| [<samp>&nbsp;&nbsp;isis_af_defaults</samp>](## "router_isis.isis_af_defaults") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_isis.isis_af_defaults.[].&lt;str&gt;") | String |  |  |  | EOS CLI rendered under the address families<br>Example "maximum-paths 64"<br> |
| [<samp>&nbsp;&nbsp;redistribute_routes</samp>](## "router_isis.redistribute_routes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- source_protocol</samp>](## "router_isis.redistribute_routes.[].source_protocol") | String | Required |  | Valid Values:<br>- bgp<br>- connected<br>- isis<br>- ospf<br>- ospfv3<br>- static |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_isis.redistribute_routes.[].route_map") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_isis.redistribute_routes.[].include_leaked") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf_route_type</samp>](## "router_isis.redistribute_routes.[].ospf_route_type") | String |  |  | Valid Values:<br>- external<br>- internal<br>- nssa-external | ospf_route_type is required with source_protocols 'ospf' and 'ospfv3' |
| [<samp>&nbsp;&nbsp;address_family_ipv4</samp>](## "router_isis.address_family_ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;maximum_paths</samp>](## "router_isis.address_family_ipv4.maximum_paths") | Integer |  |  | Min: 1<br>Max: 128 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fast_reroute_ti_lfa</samp>](## "router_isis.address_family_ipv4.fast_reroute_ti_lfa") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "router_isis.address_family_ipv4.fast_reroute_ti_lfa.mode") | String |  |  | Valid Values:<br>- link-protection<br>- node-protection |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "router_isis.address_family_ipv4.fast_reroute_ti_lfa.level") | String |  |  | Valid Values:<br>- level-1<br>- level-2 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;srlg</samp>](## "router_isis.address_family_ipv4.fast_reroute_ti_lfa.srlg") | Dictionary |  |  |  | Shared Risk Link Group |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "router_isis.address_family_ipv4.fast_reroute_ti_lfa.srlg.enable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;strict</samp>](## "router_isis.address_family_ipv4.fast_reroute_ti_lfa.srlg.strict") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tunnel_source_labeled_unicast</samp>](## "router_isis.address_family_ipv4.tunnel_source_labeled_unicast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_isis.address_family_ipv4.tunnel_source_labeled_unicast.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_isis.address_family_ipv4.tunnel_source_labeled_unicast.rcf") | String |  |  |  | Route Control Function |
| [<samp>&nbsp;&nbsp;address_family_ipv6</samp>](## "router_isis.address_family_ipv6") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;maximum_paths</samp>](## "router_isis.address_family_ipv6.maximum_paths") | Integer |  |  | Min: 1<br>Max: 128 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fast_reroute_ti_lfa</samp>](## "router_isis.address_family_ipv6.fast_reroute_ti_lfa") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "router_isis.address_family_ipv6.fast_reroute_ti_lfa.mode") | String |  |  | Valid Values:<br>- link-protection<br>- node-protection |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "router_isis.address_family_ipv6.fast_reroute_ti_lfa.level") | String |  |  | Valid Values:<br>- level-1<br>- level-2 | Optional, default is to protect all levels |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;srlg</samp>](## "router_isis.address_family_ipv6.fast_reroute_ti_lfa.srlg") | Dictionary |  |  |  | Shared Risk Link Group |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "router_isis.address_family_ipv6.fast_reroute_ti_lfa.srlg.enable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;strict</samp>](## "router_isis.address_family_ipv6.fast_reroute_ti_lfa.srlg.strict") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;segment_routing_mpls</samp>](## "router_isis.segment_routing_mpls") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_isis.segment_routing_mpls.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "router_isis.segment_routing_mpls.router_id") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;prefix_segments</samp>](## "router_isis.segment_routing_mpls.prefix_segments") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_isis.segment_routing_mpls.prefix_segments.[].prefix") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index</samp>](## "router_isis.segment_routing_mpls.prefix_segments.[].index") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;no_passive_interfaces</samp>](## "router_isis.no_passive_interfaces") | List |  |  |  | Unused key - to be removed from eos_designs. |

### YAML

```yaml
router_isis:
  instance: <str>
  net: <str>
  router_id: <str>
  is_type: <str>
  log_adjacency_changes: <bool>
  mpls_ldp_sync_default: <bool>
  timers:
    local_convergence:
      protected_prefixes: <bool>
      delay: <int>
  advertise:
    passive_only: <bool>
  address_family:
    - <str>
  isis_af_defaults:
    - <str>
  redistribute_routes:
    - source_protocol: <str>
      route_map: <str>
      include_leaked: <bool>
      ospf_route_type: <str>
  address_family_ipv4:
    maximum_paths: <int>
    fast_reroute_ti_lfa:
      mode: <str>
      level: <str>
      srlg:
        enable: <bool>
        strict: <bool>
    tunnel_source_labeled_unicast:
      enabled: <bool>
      rcf: <str>
  address_family_ipv6:
    maximum_paths: <int>
    fast_reroute_ti_lfa:
      mode: <str>
      level: <str>
      srlg:
        enable: <bool>
        strict: <bool>
  segment_routing_mpls:
    enabled: <bool>
    router_id: <str>
    prefix_segments:
      - prefix: <str>
        index: <int>
  no_passive_interfaces:
```

## Router L2 VPN

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>router_l2_vpn</samp>](## "router_l2_vpn") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;nd_rs_flooding_disabled</samp>](## "router_l2_vpn.nd_rs_flooding_disabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;virtual_router_nd_ra_flooding_disabled</samp>](## "router_l2_vpn.virtual_router_nd_ra_flooding_disabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;arp_selective_install</samp>](## "router_l2_vpn.arp_selective_install") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;arp_proxy</samp>](## "router_l2_vpn.arp_proxy") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "router_l2_vpn.arp_proxy.prefix_list") | String |  |  |  | Prefix-list Name |

### YAML

```yaml
router_l2_vpn:
  nd_rs_flooding_disabled: <bool>
  virtual_router_nd_ra_flooding_disabled: <bool>
  arp_selective_install: <bool>
  arp_proxy:
    prefix_list: <str>
```

## Router Msdp

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>router_msdp</samp>](## "router_msdp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;originator_id_local_interface</samp>](## "router_msdp.originator_id_local_interface") | String |  |  |  | Interface to use for originator ID |
| [<samp>&nbsp;&nbsp;rejected_limit</samp>](## "router_msdp.rejected_limit") | Integer |  |  | Min: 0<br>Max: 40000 | Maximum number of rejected SA messages allowed in cache |
| [<samp>&nbsp;&nbsp;forward_register_packets</samp>](## "router_msdp.forward_register_packets") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;connection_retry_interval</samp>](## "router_msdp.connection_retry_interval") | Integer |  |  | Min: 1<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;group_limits</samp>](## "router_msdp.group_limits") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- source_prefix</samp>](## "router_msdp.group_limits.[].source_prefix") | String | Required, Unique |  |  | Source address prefix |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "router_msdp.group_limits.[].limit") | Integer | Required |  | Min: 0<br>Max: 40000 | Limit for SAs matching the source address prefix |
| [<samp>&nbsp;&nbsp;peers</samp>](## "router_msdp.peers") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- ipv4_address</samp>](## "router_msdp.peers.[].ipv4_address") | String | Required, Unique |  |  | Peer IP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_peer</samp>](## "router_msdp.peers.[].default_peer") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_msdp.peers.[].default_peer.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "router_msdp.peers.[].default_peer.prefix_list") | String |  |  |  | Prefix list to filter source of SA messages |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "router_msdp.peers.[].local_interface") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_msdp.peers.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "router_msdp.peers.[].disabled") | Boolean |  |  |  | Disable the MSDP peer |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sa_limit</samp>](## "router_msdp.peers.[].sa_limit") | Integer |  |  | Min: 0<br>Max: 40000 | Maximum number of SA messages allowed in cache |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mesh_groups</samp>](## "router_msdp.peers.[].mesh_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_msdp.peers.[].mesh_groups.[].name") | String | Required, Unique |  |  | Mesh group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keepalive</samp>](## "router_msdp.peers.[].keepalive") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keepalive_timer</samp>](## "router_msdp.peers.[].keepalive.keepalive_timer") | Integer | Required |  | Min: 1<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hold_timer</samp>](## "router_msdp.peers.[].keepalive.hold_timer") | Integer | Required |  | Min: 1<br>Max: 65535 | Must be greater than keepalive timer |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sa_filter</samp>](## "router_msdp.peers.[].sa_filter") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;in_list</samp>](## "router_msdp.peers.[].sa_filter.in_list") | String |  |  |  | ACL to filter inbound SA messages |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;out_list</samp>](## "router_msdp.peers.[].sa_filter.out_list") | String |  |  |  | ACL to filter outbound SA messages |
| [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_msdp.vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_msdp.vrfs.[].name") | String | Required, Unique |  |  | VRF name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;originator_id_local_interface</samp>](## "router_msdp.vrfs.[].originator_id_local_interface") | String |  |  |  | Interface to use for originator ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rejected_limit</samp>](## "router_msdp.vrfs.[].rejected_limit") | Integer |  |  | Min: 0<br>Max: 40000 | Maximum number of rejected SA messages allowed in cache |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward_register_packets</samp>](## "router_msdp.vrfs.[].forward_register_packets") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connection_retry_interval</samp>](## "router_msdp.vrfs.[].connection_retry_interval") | Integer |  |  | Min: 1<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group_limits</samp>](## "router_msdp.vrfs.[].group_limits") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- source_prefix</samp>](## "router_msdp.vrfs.[].group_limits.[].source_prefix") | String | Required, Unique |  |  | Source address prefix |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "router_msdp.vrfs.[].group_limits.[].limit") | Integer | Required |  | Min: 0<br>Max: 40000 | Limit for SAs matching the source address prefix |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peers</samp>](## "router_msdp.vrfs.[].peers") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ipv4_address</samp>](## "router_msdp.vrfs.[].peers.[].ipv4_address") | String | Required, Unique |  |  | Peer IP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_peer</samp>](## "router_msdp.vrfs.[].peers.[].default_peer") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_msdp.vrfs.[].peers.[].default_peer.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "router_msdp.vrfs.[].peers.[].default_peer.prefix_list") | String |  |  |  | Prefix list to filter source of SA messages |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "router_msdp.vrfs.[].peers.[].local_interface") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_msdp.vrfs.[].peers.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "router_msdp.vrfs.[].peers.[].disabled") | Boolean |  |  |  | Disable the MSDP peer |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sa_limit</samp>](## "router_msdp.vrfs.[].peers.[].sa_limit") | Integer |  |  | Min: 0<br>Max: 40000 | Maximum number of SA messages allowed in cache |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mesh_groups</samp>](## "router_msdp.vrfs.[].peers.[].mesh_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_msdp.vrfs.[].peers.[].mesh_groups.[].name") | String | Required, Unique |  |  | Mesh group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keepalive</samp>](## "router_msdp.vrfs.[].peers.[].keepalive") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keepalive_timer</samp>](## "router_msdp.vrfs.[].peers.[].keepalive.keepalive_timer") | Integer | Required |  | Min: 1<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hold_timer</samp>](## "router_msdp.vrfs.[].peers.[].keepalive.hold_timer") | Integer | Required |  | Min: 1<br>Max: 65535 | Must be greater than keepalive timer |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sa_filter</samp>](## "router_msdp.vrfs.[].peers.[].sa_filter") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;in_list</samp>](## "router_msdp.vrfs.[].peers.[].sa_filter.in_list") | String |  |  |  | ACL to filter inbound SA messages |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;out_list</samp>](## "router_msdp.vrfs.[].peers.[].sa_filter.out_list") | String |  |  |  | ACL to filter outbound SA messages |

### YAML

```yaml
router_msdp:
  originator_id_local_interface: <str>
  rejected_limit: <int>
  forward_register_packets: <bool>
  connection_retry_interval: <int>
  group_limits:
    - source_prefix: <str>
      limit: <int>
  peers:
    - ipv4_address: <str>
      default_peer:
        enabled: <bool>
        prefix_list: <str>
      local_interface: <str>
      description: <str>
      disabled: <bool>
      sa_limit: <int>
      mesh_groups:
        - name: <str>
      keepalive:
        keepalive_timer: <int>
        hold_timer: <int>
      sa_filter:
        in_list: <str>
        out_list: <str>
  vrfs:
    - name: <str>
      originator_id_local_interface: <str>
      rejected_limit: <int>
      forward_register_packets: <bool>
      connection_retry_interval: <int>
      group_limits:
        - source_prefix: <str>
          limit: <int>
      peers:
        - ipv4_address: <str>
          default_peer:
            enabled: <bool>
            prefix_list: <str>
          local_interface: <str>
          description: <str>
          disabled: <bool>
          sa_limit: <int>
          mesh_groups:
            - name: <str>
          keepalive:
            keepalive_timer: <int>
            hold_timer: <int>
          sa_filter:
            in_list: <str>
            out_list: <str>
```

## Router Multicast

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>router_multicast</samp>](## "router_multicast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;ipv4</samp>](## "router_multicast.ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters</samp>](## "router_multicast.ipv4.counters") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_period_decay</samp>](## "router_multicast.ipv4.counters.rate_period_decay") | Integer |  |  | Min: 0<br>Max: 600 | Rate in seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;routing</samp>](## "router_multicast.ipv4.routing") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;multipath</samp>](## "router_multicast.ipv4.multipath") | String |  |  | Valid Values:<br>- none<br>- deterministic<br>- deterministic color<br>- deterministic router-id |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;software_forwarding</samp>](## "router_multicast.ipv4.software_forwarding") | String |  |  | Valid Values:<br>- kernel<br>- sfe |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rpf</samp>](## "router_multicast.ipv4.rpf") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routes</samp>](## "router_multicast.ipv4.rpf.routes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- source_prefix</samp>](## "router_multicast.ipv4.rpf.routes.[].source_prefix") | String | Required |  |  | Source address A.B.C.D or Source prefix A.B.C.D/E |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destinations</samp>](## "router_multicast.ipv4.rpf.routes.[].destinations") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- nexthop</samp>](## "router_multicast.ipv4.rpf.routes.[].destinations.[].nexthop") | String | Required |  |  | Next-hop IP address or interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "router_multicast.ipv4.rpf.routes.[].destinations.[].distance") | Integer |  |  | Min: 1<br>Max: 255 | Administrative distance for this route |
| [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_multicast.vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_multicast.vrfs.[].name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "router_multicast.vrfs.[].ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routing</samp>](## "router_multicast.vrfs.[].ipv4.routing") | Boolean |  |  |  |  |

### YAML

```yaml
router_multicast:
  ipv4:
    counters:
      rate_period_decay: <int>
    routing: <bool>
    multipath: <str>
    software_forwarding: <str>
    rpf:
      routes:
        - source_prefix: <str>
          destinations:
            - nexthop: <str>
              distance: <int>
  vrfs:
    - name: <str>
      ipv4:
        routing: <bool>
```

## Router OSPF Configuration

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>router_ospf</samp>](## "router_ospf") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;process_ids</samp>](## "router_ospf.process_ids") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "router_ospf.process_ids.[].id") | Integer | Required, Unique |  |  | OSPF Process ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "router_ospf.process_ids.[].vrf") | String |  |  |  | VRF Name for OSPF Process |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive_interface_default</samp>](## "router_ospf.process_ids.[].passive_interface_default") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "router_ospf.process_ids.[].router_id") | String |  |  |  | IPv4 Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "router_ospf.process_ids.[].distance") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;external</samp>](## "router_ospf.process_ids.[].distance.external") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_area</samp>](## "router_ospf.process_ids.[].distance.inter_area") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intra_area</samp>](## "router_ospf.process_ids.[].distance.intra_area") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log_adjacency_changes_detail</samp>](## "router_ospf.process_ids.[].log_adjacency_changes_detail") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;network_prefixes</samp>](## "router_ospf.process_ids.[].network_prefixes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ipv4_prefix</samp>](## "router_ospf.process_ids.[].network_prefixes.[].ipv4_prefix") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "router_ospf.process_ids.[].network_prefixes.[].area") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd_enable</samp>](## "router_ospf.process_ids.[].bfd_enable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd_adjacency_state_any</samp>](## "router_ospf.process_ids.[].bfd_adjacency_state_any") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_passive_interfaces</samp>](## "router_ospf.process_ids.[].no_passive_interfaces") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_ospf.process_ids.[].no_passive_interfaces.[].&lt;str&gt;") | String |  |  |  | Interface Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distribute_list_in</samp>](## "router_ospf.process_ids.[].distribute_list_in") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospf.process_ids.[].distribute_list_in.route_map") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_lsa</samp>](## "router_ospf.process_ids.[].max_lsa") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "router_ospf.process_ids.[].timers") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lsa</samp>](## "router_ospf.process_ids.[].timers.lsa") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rx_min_interval</samp>](## "router_ospf.process_ids.[].timers.lsa.rx_min_interval") | Integer |  |  | Min: 0<br>Max: 600000 | Min interval in msecs between accepting the same LSA |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_delay</samp>](## "router_ospf.process_ids.[].timers.lsa.tx_delay") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;initial</samp>](## "router_ospf.process_ids.[].timers.lsa.tx_delay.initial") | Integer |  |  | Min: 0<br>Max: 600000 | Delay to generate first occurrence of LSA in msecs |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min</samp>](## "router_ospf.process_ids.[].timers.lsa.tx_delay.min") | Integer |  |  | Min: 1<br>Max: 600000 | Min delay between originating the same LSA in msecs |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max</samp>](## "router_ospf.process_ids.[].timers.lsa.tx_delay.max") | Integer |  |  | Min: 1<br>Max: 600000 | 1-600000 Maximum delay between originating the same LSA in msec |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spf_delay</samp>](## "router_ospf.process_ids.[].timers.spf_delay") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;initial</samp>](## "router_ospf.process_ids.[].timers.spf_delay.initial") | Integer |  |  | Min: 0<br>Max: 600000 | Initial SPF schedule delay in msecs |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min</samp>](## "router_ospf.process_ids.[].timers.spf_delay.min") | Integer |  |  | Min: 0<br>Max: 65535000 | Min Hold time between two SPFs in msecs |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max</samp>](## "router_ospf.process_ids.[].timers.spf_delay.max") | Integer |  |  | Min: 0<br>Max: 65535000 | Max wait time between two SPFs in msecs |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_information_originate</samp>](## "router_ospf.process_ids.[].default_information_originate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_ospf.process_ids.[].default_information_originate.always") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary_addresses</samp>](## "router_ospf.process_ids.[].summary_addresses") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_ospf.process_ids.[].summary_addresses.[].prefix") | String | Required, Unique |  |  | Summary Prefix Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "router_ospf.process_ids.[].summary_addresses.[].tag") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attribute_map</samp>](## "router_ospf.process_ids.[].summary_addresses.[].attribute_map") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;not_advertise</samp>](## "router_ospf.process_ids.[].summary_addresses.[].not_advertise") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute</samp>](## "router_ospf.process_ids.[].redistribute") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "router_ospf.process_ids.[].redistribute.static") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospf.process_ids.[].redistribute.static.route_map") | String |  |  |  | Route Map Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected</samp>](## "router_ospf.process_ids.[].redistribute.connected") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospf.process_ids.[].redistribute.connected.route_map") | String |  |  |  | Route Map Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_ospf.process_ids.[].redistribute.bgp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospf.process_ids.[].redistribute.bgp.route_map") | String |  |  |  | Route Map Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_cost_reference_bandwidth</samp>](## "router_ospf.process_ids.[].auto_cost_reference_bandwidth") | Integer |  |  |  | Bandwidth in mbps |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;areas</samp>](## "router_ospf.process_ids.[].areas") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "router_ospf.process_ids.[].areas.[].id") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "router_ospf.process_ids.[].areas.[].filter") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_ospf.process_ids.[].areas.[].filter.networks") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_ospf.process_ids.[].areas.[].filter.networks.[].&lt;str&gt;") | String |  |  |  | IPv4 Prefix |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "router_ospf.process_ids.[].areas.[].filter.prefix_list") | String |  |  |  | Prefix-List Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "router_ospf.process_ids.[].areas.[].type") | String |  | normal | Valid Values:<br>- normal<br>- stub<br>- nssa |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_summary</samp>](## "router_ospf.process_ids.[].areas.[].no_summary") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_only</samp>](## "router_ospf.process_ids.[].areas.[].nssa_only") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_information_originate</samp>](## "router_ospf.process_ids.[].areas.[].default_information_originate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "router_ospf.process_ids.[].areas.[].default_information_originate.metric") | Integer |  |  | Min: 1<br>Max: 65535 | Metric for default route |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric_type</samp>](## "router_ospf.process_ids.[].areas.[].default_information_originate.metric_type") | Integer |  |  | Valid Values:<br>- 1<br>- 2 | OSPF metric type for default route |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_paths</samp>](## "router_ospf.process_ids.[].maximum_paths") | Integer |  |  | Min: 1<br>Max: 128 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_metric</samp>](## "router_ospf.process_ids.[].max_metric") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_lsa</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;external_lsa</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa.external_lsa") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;override_metric</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa.external_lsa.override_metric") | Integer |  |  | Min: 1<br>Max: 16777215 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_stub</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa.include_stub") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_startup</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa.on_startup") | String |  |  |  | "wait-for-bgp" or Integer 5-86400<br>Example: "wait-for-bgp" Or "222"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary_lsa</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa.summary_lsa") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;override_metric</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa.summary_lsa.override_metric") | Integer |  |  | Min: 1<br>Max: 16777215 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ldp_sync_default</samp>](## "router_ospf.process_ids.[].mpls_ldp_sync_default") | Boolean |  |  |  |  |

### YAML

```yaml
router_ospf:
  process_ids:
    - id: <int>
      vrf: <str>
      passive_interface_default: <bool>
      router_id: <str>
      distance:
        external: <int>
        inter_area: <int>
        intra_area: <int>
      log_adjacency_changes_detail: <bool>
      network_prefixes:
        - ipv4_prefix: <str>
          area: <str>
      bfd_enable: <bool>
      bfd_adjacency_state_any: <bool>
      no_passive_interfaces:
        - <str>
      distribute_list_in:
        route_map: <str>
      max_lsa: <int>
      timers:
        lsa:
          rx_min_interval: <int>
          tx_delay:
            initial: <int>
            min: <int>
            max: <int>
        spf_delay:
          initial: <int>
          min: <int>
          max: <int>
      default_information_originate:
        always: <bool>
      summary_addresses:
        - prefix: <str>
          tag: <int>
          attribute_map: <str>
          not_advertise: <bool>
      redistribute:
        static:
          route_map: <str>
        connected:
          route_map: <str>
        bgp:
          route_map: <str>
      auto_cost_reference_bandwidth: <int>
      areas:
        - id: <str>
          filter:
            networks:
              - <str>
            prefix_list: <str>
          type: <str>
          no_summary: <bool>
          nssa_only: <bool>
          default_information_originate:
            metric: <int>
            metric_type: <int>
      maximum_paths: <int>
      max_metric:
        router_lsa:
          external_lsa:
            override_metric: <int>
          include_stub: <bool>
          on_startup: <str>
          summary_lsa:
            override_metric: <int>
      mpls_ldp_sync_default: <bool>
```

## Router PIM Sparse Mode

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>router_pim_sparse_mode</samp>](## "router_pim_sparse_mode") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;ipv4</samp>](## "router_pim_sparse_mode.ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "router_pim_sparse_mode.ipv4.bfd") | Boolean |  |  |  | Enable/Disable BFD |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssm_range</samp>](## "router_pim_sparse_mode.ipv4.ssm_range") | String |  |  |  | IPv4 Prefix associated with SSM |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rp_addresses</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].address") | String | Required, Unique |  |  | RP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].groups") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].groups.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_lists</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].access_lists") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].access_lists.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].priority") | Integer |  |  | Min: 0<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hashmask</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].hashmask") | Integer |  |  | Min: 0<br>Max: 32 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;override</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].override") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;anycast_rps</samp>](## "router_pim_sparse_mode.ipv4.anycast_rps") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address</samp>](## "router_pim_sparse_mode.ipv4.anycast_rps.[].address") | String | Required, Unique |  |  | Anycast RP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;other_anycast_rp_addresses</samp>](## "router_pim_sparse_mode.ipv4.anycast_rps.[].other_anycast_rp_addresses") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address</samp>](## "router_pim_sparse_mode.ipv4.anycast_rps.[].other_anycast_rp_addresses.[].address") | String | Required, Unique |  |  | Other Anycast RP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;register_count</samp>](## "router_pim_sparse_mode.ipv4.anycast_rps.[].other_anycast_rp_addresses.[].register_count") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_pim_sparse_mode.vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_pim_sparse_mode.vrfs.[].name") | String |  |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.bfd") | Boolean |  |  |  | Enable/Disable BFD |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rp_addresses</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].address") | String | Required |  |  | RP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].groups") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].groups.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_lists</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].access_lists") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].access_lists.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].priority") | Integer |  |  | Min: 0<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hashmask</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].hashmask") | Integer |  |  | Min: 0<br>Max: 32 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;override</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].override") | Boolean |  |  |  |  |

### YAML

```yaml
router_pim_sparse_mode:
  ipv4:
    bfd: <bool>
    ssm_range: <str>
    rp_addresses:
      - address: <str>
        groups:
          - <str>
        access_lists:
          - <str>
        priority: <int>
        hashmask: <int>
        override: <bool>
    anycast_rps:
      - address: <str>
        other_anycast_rp_addresses:
          - address: <str>
            register_count: <int>
  vrfs:
    - name: <str>
      ipv4:
        bfd: <bool>
        rp_addresses:
          - address: <str>
            groups:
              - <str>
            access_lists:
              - <str>
            priority: <int>
            hashmask: <int>
            override: <bool>
```

## Router Traffic Engineering

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>router_traffic_engineering</samp>](## "router_traffic_engineering") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;router_id</samp>](## "router_traffic_engineering.router_id") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "router_traffic_engineering.router_id.ipv4") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "router_traffic_engineering.router_id.ipv6") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;segment_routing</samp>](## "router_traffic_engineering.segment_routing") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;colored_tunnel_rib</samp>](## "router_traffic_engineering.segment_routing.colored_tunnel_rib") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;policy_endpoints</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].address") | String |  |  |  | IPv4 or IPv6 address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;colors</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- value</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].value") | Integer | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;binding_sid</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].binding_sid") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sbfd_remote_discriminator</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].sbfd_remote_discriminator") | String |  |  |  | IPv4 address or 32 bit integer |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path_group</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].path_group") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- preference</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].path_group.[].preference") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;explicit_null</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].path_group.[].explicit_null") | String |  |  | Valid Values:<br>- ipv4<br>- ipv6<br>- ipv4 ipv6<br>- none |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;segment_list</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].path_group.[].segment_list") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- label_stack</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].path_group.[].segment_list.[].label_stack") | String |  |  |  | Label Stack as string.<br>Example: "100 2000 30"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].path_group.[].segment_list.[].weight") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].path_group.[].segment_list.[].index") | Integer |  |  |  |  |

### YAML

```yaml
router_traffic_engineering:
  router_id:
    ipv4: <str>
    ipv6: <str>
  segment_routing:
    colored_tunnel_rib: <bool>
    policy_endpoints:
      - address: <str>
        colors:
          - value: <int>
            binding_sid: <int>
            description: <str>
            name: <str>
            sbfd_remote_discriminator: <str>
            path_group:
              - preference: <int>
                explicit_null: <str>
                segment_list:
                  - label_stack: <str>
                    weight: <int>
                    index: <int>
```

## Service Routing Configuration BGP

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>service_routing_configuration_bgp</samp>](## "service_routing_configuration_bgp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;no_equals_default</samp>](## "service_routing_configuration_bgp.no_equals_default") | Boolean |  |  |  |  |

### YAML

```yaml
service_routing_configuration_bgp:
  no_equals_default: <bool>
```

## Service Routing Protocols Model

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>service_routing_protocols_model</samp>](## "service_routing_protocols_model") | String |  |  | Valid Values:<br>- multi-agent<br>- ribd |  |

### YAML

```yaml
service_routing_protocols_model: <str>
```

## Service Unsupported Transceiver

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>service_unsupported_transceiver</samp>](## "service_unsupported_transceiver") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;license_name</samp>](## "service_unsupported_transceiver.license_name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;license_key</samp>](## "service_unsupported_transceiver.license_key") | String |  |  |  |  |

### YAML

```yaml
service_unsupported_transceiver:
  license_name: <str>
  license_key: <str>
```

## Sflow

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>sflow</samp>](## "sflow") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;sample</samp>](## "sflow.sample") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;dangerous</samp>](## "sflow.dangerous") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;polling_interval</samp>](## "sflow.polling_interval") | Integer |  |  |  | Polling interval in seconds |
| [<samp>&nbsp;&nbsp;vrfs</samp>](## "sflow.vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "sflow.vrfs.[].name") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destinations</samp>](## "sflow.vrfs.[].destinations") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- destination</samp>](## "sflow.vrfs.[].destinations.[].destination") | String | Required, Unique |  |  | Sflow Destination IP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "sflow.vrfs.[].destinations.[].port") | Integer |  |  |  | Port Number |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "sflow.vrfs.[].source") | String |  |  |  | Source IP Address.<br>"source" and "source_interface" are mutually exclusive. If both are defined, "source_interface" takes precedence.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "sflow.vrfs.[].source_interface") | String |  |  |  | Source Interface |
| [<samp>&nbsp;&nbsp;destinations</samp>](## "sflow.destinations") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- destination</samp>](## "sflow.destinations.[].destination") | String | Required, Unique |  |  | Sflow Destination IP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "sflow.destinations.[].port") | Integer |  |  |  | Port Number |
| [<samp>&nbsp;&nbsp;source</samp>](## "sflow.source") | String |  |  |  | Source IP Address.<br>"source" and "source_interface" are mutually exclusive. If both are defined, "source_interface" takes precedence.<br> |
| [<samp>&nbsp;&nbsp;source_interface</samp>](## "sflow.source_interface") | String |  |  |  | Source Interface |
| [<samp>&nbsp;&nbsp;extensions</samp>](## "sflow.extensions") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "sflow.extensions.[].name") | String | Required, Unique |  |  | Extension Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "sflow.extensions.[].enabled") | Boolean | Required |  |  | Enable or Disable Extension |
| [<samp>&nbsp;&nbsp;interface</samp>](## "sflow.interface") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;disable</samp>](## "sflow.interface.disable") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "sflow.interface.disable.default") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;run</samp>](## "sflow.run") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;hardware_acceleration</samp>](## "sflow.hardware_acceleration") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "sflow.hardware_acceleration.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "sflow.hardware_acceleration.sample") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;modules</samp>](## "sflow.hardware_acceleration.modules") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "sflow.hardware_acceleration.modules.[].name") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "sflow.hardware_acceleration.modules.[].enabled") | Boolean |  | True |  |  |

### YAML

```yaml
sflow:
  sample: <int>
  dangerous: <bool>
  polling_interval: <int>
  vrfs:
    - name: <str>
      destinations:
        - destination: <str>
          port: <int>
      source: <str>
      source_interface: <str>
  destinations:
    - destination: <str>
      port: <int>
  source: <str>
  source_interface: <str>
  extensions:
    - name: <str>
      enabled: <bool>
  interface:
    disable:
      default: <bool>
  run: <bool>
  hardware_acceleration:
    enabled: <bool>
    sample: <int>
    modules:
      - name: <str>
        enabled: <bool>
```

## Snmp Server

### Description

SNMP settings
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>snmp_server</samp>](## "snmp_server") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;engine_ids</samp>](## "snmp_server.engine_ids") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local</samp>](## "snmp_server.engine_ids.local") | String |  |  |  | Engine ID in hexadecimal<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;remotes</samp>](## "snmp_server.engine_ids.remotes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "snmp_server.engine_ids.remotes.[].id") | String |  |  |  | Remote engine ID in hexadecimal<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "snmp_server.engine_ids.remotes.[].address") | String |  |  |  | Hostname or IP of remote engine<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_port</samp>](## "snmp_server.engine_ids.remotes.[].udp_port") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;contact</samp>](## "snmp_server.contact") | String |  |  |  | SNMP contact |
| [<samp>&nbsp;&nbsp;location</samp>](## "snmp_server.location") | String |  |  |  | SNMP location |
| [<samp>&nbsp;&nbsp;communities</samp>](## "snmp_server.communities") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.communities.[].name") | String | Required, Unique |  |  | Community name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access</samp>](## "snmp_server.communities.[].access") | String |  |  | Valid Values:<br>- ro<br>- rw |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_list_ipv4</samp>](## "snmp_server.communities.[].access_list_ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "snmp_server.communities.[].access_list_ipv4.name") | String |  |  |  | IPv4 access list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_list_ipv6</samp>](## "snmp_server.communities.[].access_list_ipv6") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "snmp_server.communities.[].access_list_ipv6.name") | String |  |  |  | IPv6 access list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;view</samp>](## "snmp_server.communities.[].view") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;ipv4_acls</samp>](## "snmp_server.ipv4_acls") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.ipv4_acls.[].name") | String |  |  |  | IPv4 access list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_server.ipv4_acls.[].vrf") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;ipv6_acls</samp>](## "snmp_server.ipv6_acls") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.ipv6_acls.[].name") | String |  |  |  | IPv6 access list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_server.ipv6_acls.[].vrf") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;local_interfaces</samp>](## "snmp_server.local_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.local_interfaces.[].name") | String | Required, Unique |  |  | Interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_server.local_interfaces.[].vrf") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;views</samp>](## "snmp_server.views") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.views.[].name") | String |  |  |  | SNMP view name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MIB_family_name</samp>](## "snmp_server.views.[].MIB_family_name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;included</samp>](## "snmp_server.views.[].included") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;groups</samp>](## "snmp_server.groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.groups.[].name") | String |  |  |  | Group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_server.groups.[].version") | String |  |  | Valid Values:<br>- v1<br>- v2c<br>- v3 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "snmp_server.groups.[].authentication") | String |  |  | Valid Values:<br>- auth<br>- noauth<br>- priv |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;read</samp>](## "snmp_server.groups.[].read") | String |  |  |  | Read view |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;write</samp>](## "snmp_server.groups.[].write") | String |  |  |  | Write view |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;notify</samp>](## "snmp_server.groups.[].notify") | String |  |  |  | Notify view |
| [<samp>&nbsp;&nbsp;users</samp>](## "snmp_server.users") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.users.[].name") | String |  |  |  | Username |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "snmp_server.users.[].group") | String |  |  |  | Group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_address</samp>](## "snmp_server.users.[].remote_address") | String |  |  |  | Hostname or ip of remote engine<br>The remote_address and udp_port are used for remote users<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_port</samp>](## "snmp_server.users.[].udp_port") | Integer |  |  |  | udp_port will not be used if no remote_address is configured<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_server.users.[].version") | String |  |  | Valid Values:<br>- v1<br>- v2c<br>- v3 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;localized</samp>](## "snmp_server.users.[].localized") | String |  |  |  | Engine ID in hexadecimal for localizing auth and/or priv<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth</samp>](## "snmp_server.users.[].auth") | String |  |  |  | Hash algorithm<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_passphrase</samp>](## "snmp_server.users.[].auth_passphrase") | String |  |  |  | Hashed authentication passphrase if localized is used else cleartext authentication passphrase<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv</samp>](## "snmp_server.users.[].priv") | String |  |  |  | Encryption algorithm<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv_passphrase</samp>](## "snmp_server.users.[].priv_passphrase") | String |  |  |  | Hashed privacy passphrase if localized is used else cleartext privacy passphrase<br> |
| [<samp>&nbsp;&nbsp;hosts</samp>](## "snmp_server.hosts") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- host</samp>](## "snmp_server.hosts.[].host") | String |  |  |  | Host IP address or name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_server.hosts.[].vrf") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_server.hosts.[].version") | String |  |  | Valid Values:<br>- 1<br>- 2c<br>- 3 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;community</samp>](## "snmp_server.hosts.[].community") | String |  |  |  | Community name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;users</samp>](## "snmp_server.hosts.[].users") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- username</samp>](## "snmp_server.hosts.[].users.[].username") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_level</samp>](## "snmp_server.hosts.[].users.[].authentication_level") | String |  |  | Valid Values:<br>- auth<br>- noauth<br>- priv |  |
| [<samp>&nbsp;&nbsp;traps</samp>](## "snmp_server.traps") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "snmp_server.traps.enable") | Boolean |  | False |  | Enable or disable all snmp-traps<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;snmp_traps</samp>](## "snmp_server.traps.snmp_traps") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.traps.snmp_traps.[].name") | String |  |  |  | Enable or disable specific snmp-traps and their sub_traps<br>Examples:<br>- "bgp"<br>- "bgp established"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "snmp_server.traps.snmp_traps.[].enabled") | Boolean |  | True |  |  |
| [<samp>&nbsp;&nbsp;vrfs</samp>](## "snmp_server.vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_server.vrfs.[].name") | String |  |  |  | VRF name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "snmp_server.vrfs.[].enable") | Boolean |  |  |  |  |

### YAML

```yaml
snmp_server:
  engine_ids:
    local: <str>
    remotes:
      - id: <str>
        address: <str>
        udp_port: <int>
  contact: <str>
  location: <str>
  communities:
    - name: <str>
      access: <str>
      access_list_ipv4:
        name: <str>
      access_list_ipv6:
        name: <str>
      view: <str>
  ipv4_acls:
    - name: <str>
      vrf: <str>
  ipv6_acls:
    - name: <str>
      vrf: <str>
  local_interfaces:
    - name: <str>
      vrf: <str>
  views:
    - name: <str>
      MIB_family_name: <str>
      included: <bool>
  groups:
    - name: <str>
      version: <str>
      authentication: <str>
      read: <str>
      write: <str>
      notify: <str>
  users:
    - name: <str>
      group: <str>
      remote_address: <str>
      udp_port: <int>
      version: <str>
      localized: <str>
      auth: <str>
      auth_passphrase: <str>
      priv: <str>
      priv_passphrase: <str>
  hosts:
    - host: <str>
      vrf: <str>
      version: <str>
      community: <str>
      users:
        - username: <str>
          authentication_level: <str>
  traps:
    enable: <bool>
    snmp_traps:
      - name: <str>
        enabled: <bool>
  vrfs:
    - name: <str>
      enable: <bool>
```

## Spanning Tree

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>spanning_tree</samp>](## "spanning_tree") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;root_super</samp>](## "spanning_tree.root_super") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;edge_port</samp>](## "spanning_tree.edge_port") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bpdufilter_default</samp>](## "spanning_tree.edge_port.bpdufilter_default") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bpduguard_default</samp>](## "spanning_tree.edge_port.bpduguard_default") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;mode</samp>](## "spanning_tree.mode") | String |  |  | Valid Values:<br>- mstp<br>- rstp<br>- rapid-pvst<br>- none |  |
| [<samp>&nbsp;&nbsp;bpduguard_rate_limit</samp>](## "spanning_tree.bpduguard_rate_limit") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "spanning_tree.bpduguard_rate_limit.default") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "spanning_tree.bpduguard_rate_limit.count") | Integer |  |  |  | Maximum number of BPDUs per timer interval |
| [<samp>&nbsp;&nbsp;rstp_priority</samp>](## "spanning_tree.rstp_priority") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;mst</samp>](## "spanning_tree.mst") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pvst_border</samp>](## "spanning_tree.mst.pvst_border") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;configuration</samp>](## "spanning_tree.mst.configuration") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "spanning_tree.mst.configuration.name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;revision</samp>](## "spanning_tree.mst.configuration.revision") | Integer |  |  |  | 0-65535 |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;instances</samp>](## "spanning_tree.mst.configuration.instances") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "spanning_tree.mst.configuration.instances.[].id") | Integer | Required, Unique |  |  | Instance ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "spanning_tree.mst.configuration.instances.[].vlans") | String |  |  |  | "< vlan_id >, < vlan_id >-< vlan_id >"<br>Example: 15,16,17,18<br> |
| [<samp>&nbsp;&nbsp;mst_instances</samp>](## "spanning_tree.mst_instances") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "spanning_tree.mst_instances.[].id") | String | Required, Unique |  |  | Instance ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "spanning_tree.mst_instances.[].priority") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;no_spanning_tree_vlan</samp>](## "spanning_tree.no_spanning_tree_vlan") | String |  |  |  | "< vlan_id >, < vlan_id >-< vlan_id >"<br>Example: 105,202,505-506<br> |
| [<samp>&nbsp;&nbsp;rapid_pvst_instances</samp>](## "spanning_tree.rapid_pvst_instances") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "spanning_tree.rapid_pvst_instances.[].id") | String | Required, Unique |  |  | "< vlan_id >, < vlan_id >-< vlan_id >"<br>Example: 105,202,505-506<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "spanning_tree.rapid_pvst_instances.[].priority") | Integer |  |  |  |  |

### YAML

```yaml
spanning_tree:
  root_super: <bool>
  edge_port:
    bpdufilter_default: <bool>
    bpduguard_default: <bool>
  mode: <str>
  bpduguard_rate_limit:
    default: <bool>
    count: <int>
  rstp_priority: <int>
  mst:
    pvst_border: <bool>
    configuration:
      name: <str>
      revision: <int>
      instances:
        - id: <int>
          vlans: <str>
  mst_instances:
    - id: <str>
      priority: <int>
  no_spanning_tree_vlan: <str>
  rapid_pvst_instances:
    - id: <str>
      priority: <int>
```

## Standard Access Lists

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>standard_access_lists</samp>](## "standard_access_lists") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "standard_access_lists.[].name") | String | Required, Unique |  |  | Access-list Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "standard_access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "standard_access_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "standard_access_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "standard_access_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string<br>Example: "deny ip any any" |

### YAML

```yaml
standard_access_lists:
  - name: <str>
    counters_per_entry: <bool>
    sequence_numbers:
      - sequence: <int>
        action: <str>
```

## Static Routes

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>static_routes</samp>](## "static_routes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- vrf</samp>](## "static_routes.[].vrf") | String |  |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;destination_address_prefix</samp>](## "static_routes.[].destination_address_prefix") | String |  |  |  | IPv4_network/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "static_routes.[].interface") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "static_routes.[].gateway") | String |  |  |  | IPv4 Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;track_bfd</samp>](## "static_routes.[].track_bfd") | Boolean |  |  |  | Track next-hop using BFD |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "static_routes.[].name") | String |  |  |  | Description |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |

### YAML

```yaml
static_routes:
  - vrf: <str>
    destination_address_prefix: <str>
    interface: <str>
    gateway: <str>
    track_bfd: <bool>
    distance: <int>
    tag: <int>
    name: <str>
    metric: <int>
```

## Switchport Default

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>switchport_default</samp>](## "switchport_default") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;mode</samp>](## "switchport_default.mode") | String |  |  | Valid Values:<br>- routed<br>- access |  |
| [<samp>&nbsp;&nbsp;phone</samp>](## "switchport_default.phone") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "switchport_default.phone.cos") | Integer |  |  | Min: 0<br>Max: 7 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk</samp>](## "switchport_default.phone.trunk") | String |  |  | Valid Values:<br>- tagged<br>- untagged |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "switchport_default.phone.vlan") | Integer |  |  | Min: 1<br>Max: 4094 | VLAN ID |

### YAML

```yaml
switchport_default:
  mode: <str>
  phone:
    cos: <int>
    trunk: <str>
    vlan: <int>
```

## System

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>system</samp>](## "system") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;control_plane</samp>](## "system.control_plane") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tcp_mss</samp>](## "system.control_plane.tcp_mss") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "system.control_plane.tcp_mss.ipv4") | Integer |  |  |  | Segment size |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "system.control_plane.tcp_mss.ipv6") | Integer |  |  |  | Segment size |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_access_groups</samp>](## "system.control_plane.ipv4_access_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- acl_name</samp>](## "system.control_plane.ipv4_access_groups.[].acl_name") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "system.control_plane.ipv4_access_groups.[].vrf") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_groups</samp>](## "system.control_plane.ipv6_access_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- acl_name</samp>](## "system.control_plane.ipv6_access_groups.[].acl_name") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "system.control_plane.ipv6_access_groups.[].vrf") | String |  |  |  |  |

### YAML

```yaml
system:
  control_plane:
    tcp_mss:
      ipv4: <int>
      ipv6: <int>
    ipv4_access_groups:
      - acl_name: <str>
        vrf: <str>
    ipv6_access_groups:
      - acl_name: <str>
        vrf: <str>
```

## Tacacs Servers

### Variables

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

### YAML

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

## Tap Aggregation

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>tap_aggregation</samp>](## "tap_aggregation") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;mode</samp>](## "tap_aggregation.mode") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;exclusive</samp>](## "tap_aggregation.mode.exclusive") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "tap_aggregation.mode.exclusive.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "tap_aggregation.mode.exclusive.profile") | String |  |  |  | Profile Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_errdisable</samp>](## "tap_aggregation.mode.exclusive.no_errdisable") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "tap_aggregation.mode.exclusive.no_errdisable.[].&lt;str&gt;") | String |  |  |  | Interface name e.g Ethernet1, Port-Channel1 |
| [<samp>&nbsp;&nbsp;encapsulation_dot1br_strip</samp>](## "tap_aggregation.encapsulation_dot1br_strip") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;encapsulation_vn_tag_strip</samp>](## "tap_aggregation.encapsulation_vn_tag_strip") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;protocol_lldp_trap</samp>](## "tap_aggregation.protocol_lldp_trap") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;truncation_size</samp>](## "tap_aggregation.truncation_size") | Integer |  |  |  | Allowed truncation_size values vary depending on the platform<br> |
| [<samp>&nbsp;&nbsp;mac</samp>](## "tap_aggregation.mac") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;timestamp</samp>](## "tap_aggregation.mac.timestamp") | Dictionary |  |  |  | mac.timestamp.replace_source_mac and mac.timestamp.header.format are mutually exclsuive. If both are defined, replace_source_mac takes precedence<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_source_mac</samp>](## "tap_aggregation.mac.timestamp.replace_source_mac") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;header</samp>](## "tap_aggregation.mac.timestamp.header") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format</samp>](## "tap_aggregation.mac.timestamp.header.format") | String |  |  | Valid Values:<br>- 48-bit<br>- 64-bit |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eth_type</samp>](## "tap_aggregation.mac.timestamp.header.eth_type") | Integer |  |  |  | EtherType |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fcs_append</samp>](## "tap_aggregation.mac.fcs_append") | Boolean |  |  |  | mac.fcs_append and mac.fcs_error are mutually exclusive. If both are defined, mac.fcs_append takes precedence<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fcs_error</samp>](## "tap_aggregation.mac.fcs_error") | String |  |  | Valid Values:<br>- correct<br>- discard<br>- pass-through |  |

### YAML

```yaml
tap_aggregation:
  mode:
    exclusive:
      enabled: <bool>
      profile: <str>
      no_errdisable:
        - <str>
  encapsulation_dot1br_strip: <bool>
  encapsulation_vn_tag_strip: <bool>
  protocol_lldp_trap: <bool>
  truncation_size: <int>
  mac:
    timestamp:
      replace_source_mac: <bool>
      header:
        format: <str>
        eth_type: <int>
    fcs_append: <bool>
    fcs_error: <str>
```

## Hardware TCAM Profiles

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>tcam_profile</samp>](## "tcam_profile") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;system</samp>](## "tcam_profile.system") | String |  |  |  | TCAM profile name to activate<br> |
| [<samp>&nbsp;&nbsp;profiles</samp>](## "tcam_profile.profiles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "tcam_profile.profiles.[].name") | String | Required, Unique |  |  | Tcam-Profile Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;config</samp>](## "tcam_profile.profiles.[].config") | String | Required |  |  | TCAM Profile Config. Since these can be very long, it is often a good idea to import the config from a file.<br>Example: "{{lookup('file', '{{ root_dir }}/inventory/TCAM_TRAFFIC_POLICY.conf')}}" |

### YAML

```yaml
tcam_profile:
  system: <str>
  profiles:
    - name: <str>
      config: <str>
```

## Terminal Settings

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>terminal</samp>](## "terminal") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;length</samp>](## "terminal.length") | Integer |  |  | Min: 0<br>Max: 32767 |  |
| [<samp>&nbsp;&nbsp;width</samp>](## "terminal.width") | Integer |  |  | Min: 10<br>Max: 32767 |  |

### YAML

```yaml
terminal:
  length: <int>
  width: <int>
```

## Trackers

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>trackers</samp>](## "trackers") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "trackers.[].name") | String | Required, Unique |  |  | Name of tracker object |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "trackers.[].interface") | String | Required |  |  | Name of tracked interface |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tracked_property</samp>](## "trackers.[].tracked_property") | String |  | line-protocol |  | Property to track |

### YAML

```yaml
trackers:
  - name: <str>
    interface: <str>
    tracked_property: <str>
```

## Traffic Policies

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>traffic_policies</samp>](## "traffic_policies") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;options</samp>](## "traffic_policies.options") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counter_per_interface</samp>](## "traffic_policies.options.counter_per_interface") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;field_sets</samp>](## "traffic_policies.field_sets") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "traffic_policies.field_sets.ipv4") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "traffic_policies.field_sets.ipv4.[].name") | String | Required, Unique |  |  | IPv4 Prefix Field Set Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "traffic_policies.field_sets.ipv4.[].prefixes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "traffic_policies.field_sets.ipv4.[].prefixes.[].&lt;str&gt;") | String |  |  |  | IPv4 Prefix |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "traffic_policies.field_sets.ipv6") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "traffic_policies.field_sets.ipv6.[].name") | String | Required, Unique |  |  | IPv6 Prefix Field Set Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "traffic_policies.field_sets.ipv6.[].prefixes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "traffic_policies.field_sets.ipv6.[].prefixes.[].&lt;str&gt;") | String |  |  |  | IPv6 Prefix |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ports</samp>](## "traffic_policies.field_sets.ports") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "traffic_policies.field_sets.ports.[].name") | String | Required, Unique |  |  | L4 Port Field Set Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_range</samp>](## "traffic_policies.field_sets.ports.[].port_range") | String |  |  |  | Example: '10,20,80,440-450' |
| [<samp>&nbsp;&nbsp;policies</samp>](## "traffic_policies.policies") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "traffic_policies.policies.[].name") | String | Required, Unique |  |  | Traffic Policy Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;matches</samp>](## "traffic_policies.policies.[].matches") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "traffic_policies.policies.[].matches.[].name") | String | Required, Unique |  |  | Traffic Policy Item |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "traffic_policies.policies.[].matches.[].type") | String |  |  | Valid Values:<br>- ipv4<br>- ipv6 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "traffic_policies.policies.[].matches.[].source") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "traffic_policies.policies.[].matches.[].source.prefixes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "traffic_policies.policies.[].matches.[].source.prefixes.[].&lt;str&gt;") | String |  |  |  | IP address or prefix |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_lists</samp>](## "traffic_policies.policies.[].matches.[].source.prefix_lists") | List, items: String |  |  |  | Field-set prefix lists |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "traffic_policies.policies.[].matches.[].source.prefix_lists.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "traffic_policies.policies.[].matches.[].destination") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "traffic_policies.policies.[].matches.[].destination.prefixes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "traffic_policies.policies.[].matches.[].destination.prefixes.[].&lt;str&gt;") | String |  |  |  | IP address or prefix |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_lists</samp>](## "traffic_policies.policies.[].matches.[].destination.prefix_lists") | List, items: String |  |  |  | Field-set prefix lists |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "traffic_policies.policies.[].matches.[].destination.prefix_lists.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "traffic_policies.policies.[].matches.[].ttl") | String |  |  |  | TTL range |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fragment</samp>](## "traffic_policies.policies.[].matches.[].fragment") | Dictionary |  |  |  | The 'fragment' command is not supported when 'source port'<br>or 'destination port' command is configured<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset</samp>](## "traffic_policies.policies.[].matches.[].fragment.offset") | String |  |  |  | Fragment offset range |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocols</samp>](## "traffic_policies.policies.[].matches.[].protocols") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- protocol</samp>](## "traffic_policies.policies.[].matches.[].protocols.[].protocol") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;src_port</samp>](## "traffic_policies.policies.[].matches.[].protocols.[].src_port") | String |  |  |  | Port range |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dst_port</samp>](## "traffic_policies.policies.[].matches.[].protocols.[].dst_port") | String |  |  |  | Port range |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;src_field</samp>](## "traffic_policies.policies.[].matches.[].protocols.[].src_field") | String |  |  |  | L4 port range field set |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dst_field</samp>](## "traffic_policies.policies.[].matches.[].protocols.[].dst_field") | String |  |  |  | L4 port range field set |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flags</samp>](## "traffic_policies.policies.[].matches.[].protocols.[].flags") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "traffic_policies.policies.[].matches.[].protocols.[].flags.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- established<br>- initial |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_type</samp>](## "traffic_policies.policies.[].matches.[].protocols.[].icmp_type") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "traffic_policies.policies.[].matches.[].protocols.[].icmp_type.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;actions</samp>](## "traffic_policies.policies.[].matches.[].actions") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "traffic_policies.policies.[].matches.[].actions.dscp") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "traffic_policies.policies.[].matches.[].actions.traffic_class") | Integer |  |  |  | Traffic class ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "traffic_policies.policies.[].matches.[].actions.count") | String |  |  |  | Counter name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "traffic_policies.policies.[].matches.[].actions.drop") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log</samp>](## "traffic_policies.policies.[].matches.[].actions.log") | Boolean |  |  |  | Only supported when action is set to drop |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_actions</samp>](## "traffic_policies.policies.[].default_actions") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "traffic_policies.policies.[].default_actions.ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "traffic_policies.policies.[].default_actions.ipv4.dscp") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "traffic_policies.policies.[].default_actions.ipv4.traffic_class") | Integer |  |  |  | Traffic class ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "traffic_policies.policies.[].default_actions.ipv4.count") | String |  |  |  | Counter name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "traffic_policies.policies.[].default_actions.ipv4.drop") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log</samp>](## "traffic_policies.policies.[].default_actions.ipv4.log") | Boolean |  |  |  | Only supported when action is set to drop |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "traffic_policies.policies.[].default_actions.ipv6") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "traffic_policies.policies.[].default_actions.ipv6.dscp") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "traffic_policies.policies.[].default_actions.ipv6.traffic_class") | Integer |  |  |  | Traffic class ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "traffic_policies.policies.[].default_actions.ipv6.count") | String |  |  |  | Counter name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "traffic_policies.policies.[].default_actions.ipv6.drop") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log</samp>](## "traffic_policies.policies.[].default_actions.ipv6.log") | Boolean |  |  |  | Only supported when action is set to drop |

### YAML

```yaml
traffic_policies:
  options:
    counter_per_interface: <bool>
  field_sets:
    ipv4:
      - name: <str>
        prefixes:
          - <str>
    ipv6:
      - name: <str>
        prefixes:
          - <str>
    ports:
      - name: <str>
        port_range: <str>
  policies:
    - name: <str>
      matches:
        - name: <str>
          type: <str>
          source:
            prefixes:
              - <str>
            prefix_lists:
              - <str>
          destination:
            prefixes:
              - <str>
            prefix_lists:
              - <str>
          ttl: <str>
          fragment:
            offset: <str>
          protocols:
            - protocol: <str>
              src_port: <str>
              dst_port: <str>
              src_field: <str>
              dst_field: <str>
              flags:
                - <str>
              icmp_type:
                - <str>
          actions:
            dscp: <int>
            traffic_class: <int>
            count: <str>
            drop: <bool>
            log: <bool>
      default_actions:
        ipv4:
          dscp: <int>
          traffic_class: <int>
          count: <str>
          drop: <bool>
          log: <bool>
        ipv6:
          dscp: <int>
          traffic_class: <int>
          count: <str>
          drop: <bool>
          log: <bool>
```

## Tunnel Interfaces

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>tunnel_interfaces</samp>](## "tunnel_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "tunnel_interfaces.[].name") | String | Required, Unique |  |  | Tunnel Interface Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "tunnel_interfaces.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "tunnel_interfaces.[].shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "tunnel_interfaces.[].mtu") | Integer |  |  | Min: 68<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "tunnel_interfaces.[].vrf") | String |  |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "tunnel_interfaces.[].ip_address") | String |  |  | Format: ipv4_cidr | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "tunnel_interfaces.[].ipv6_enable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "tunnel_interfaces.[].ipv6_address") | String |  |  | Format: ipv6_cidr | IPv6_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_in</samp>](## "tunnel_interfaces.[].access_group_in") | String |  |  |  | IPv4 ACL Name for ingress |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_out</samp>](## "tunnel_interfaces.[].access_group_out") | String |  |  |  | IPv4 ACL Name for egress |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_in</samp>](## "tunnel_interfaces.[].ipv6_access_group_in") | String |  |  |  | IPv6 ACL Name for ingress |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_out</samp>](## "tunnel_interfaces.[].ipv6_access_group_out") | String |  |  |  | IPv6 ACL Name for egress |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tcp_mss_ceiling</samp>](## "tunnel_interfaces.[].tcp_mss_ceiling") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "tunnel_interfaces.[].tcp_mss_ceiling.ipv4") | Integer |  |  | Min: 64<br>Max: 65495 | Segment Size for IPv4 |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "tunnel_interfaces.[].tcp_mss_ceiling.ipv6") | Integer |  |  | Min: 64<br>Max: 65475 | Segment Size for IPv6 |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "tunnel_interfaces.[].tcp_mss_ceiling.direction") | String |  |  | Valid Values:<br>- ingress<br>- egress | Optional direction ('ingress', 'egress')  for tcp mss ceiling<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "tunnel_interfaces.[].source_interface") | String |  |  |  | Tunnel Source Interface Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "tunnel_interfaces.[].destination") | String |  |  |  | IPv4 or IPv6 Address Tunnel Destination |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;path_mtu_discovery</samp>](## "tunnel_interfaces.[].path_mtu_discovery") | Boolean |  |  |  | Enable Path MTU Discovery On Tunnel |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "tunnel_interfaces.[].eos_cli") | String |  |  |  | Multiline String with EOS CLI rendered directly on the Tunnel interface in the final EOS configuration. |

### YAML

```yaml
tunnel_interfaces:
  - name: <str>
    description: <str>
    shutdown: <bool>
    mtu: <int>
    vrf: <str>
    ip_address: <str>
    ipv6_enable: <bool>
    ipv6_address: <str>
    access_group_in: <str>
    access_group_out: <str>
    ipv6_access_group_in: <str>
    ipv6_access_group_out: <str>
    tcp_mss_ceiling:
      ipv4: <int>
      ipv6: <int>
      direction: <str>
    source_interface: <str>
    destination: <str>
    path_mtu_discovery: <bool>
    eos_cli: <str>
```

## Virtual Source Nat VRFs

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>virtual_source_nat_vrfs</samp>](## "virtual_source_nat_vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "virtual_source_nat_vrfs.[].name") | String | Required, Unique |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "virtual_source_nat_vrfs.[].ip_address") | String |  |  |  | IPv4 Address |

### YAML

```yaml
virtual_source_nat_vrfs:
  - name: <str>
    ip_address: <str>
```

## VLAN Interfaces

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>vlan_interfaces</samp>](## "vlan_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "vlan_interfaces.[].name") | String | Required, Unique |  |  | VLAN interface name like "Vlan123" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "vlan_interfaces.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "vlan_interfaces.[].shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "vlan_interfaces.[].vrf") | String |  |  |  | VRF name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;arp_aging_timeout</samp>](## "vlan_interfaces.[].arp_aging_timeout") | Integer |  |  | Min: 1<br>Max: 65535 | In seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;arp_cache_dynamic_capacity</samp>](## "vlan_interfaces.[].arp_cache_dynamic_capacity") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;arp_gratuitous_accept</samp>](## "vlan_interfaces.[].arp_gratuitous_accept") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;arp_monitor_mac_address</samp>](## "vlan_interfaces.[].arp_monitor_mac_address") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_proxy_arp</samp>](## "vlan_interfaces.[].ip_proxy_arp") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_directed_broadcast</samp>](## "vlan_interfaces.[].ip_directed_broadcast") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "vlan_interfaces.[].ip_address") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_secondaries</samp>](## "vlan_interfaces.[].ip_address_secondaries") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "vlan_interfaces.[].ip_address_secondaries.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "vlan_interfaces.[].ip_virtual_router_addresses") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "vlan_interfaces.[].ip_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  | IPv4 address or IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "vlan_interfaces.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "vlan_interfaces.[].ip_address_virtual_secondaries") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "vlan_interfaces.[].ip_address_virtual_secondaries.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_igmp</samp>](## "vlan_interfaces.[].ip_igmp") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "vlan_interfaces.[].ip_helpers") | List, items: Dictionary |  |  |  | List of DHCP servers |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "vlan_interfaces.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IP address or hostname of DHCP server |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "vlan_interfaces.[].ip_helpers.[].source_interface") | String |  |  |  | Interface used as source for forwarded DHCP packets |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "vlan_interfaces.[].ip_helpers.[].vrf") | String |  |  |  | VRF where DHCP server can be reached |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "vlan_interfaces.[].ipv6_enable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "vlan_interfaces.[].ipv6_address") | String |  |  |  | IPv6_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp>](## "vlan_interfaces.[].ipv6_address_virtual") | String |  |  |  | IPv6_address/Mask<br>"ipv6_address_virtual" key will be deprecated in AVD v4.0 in favor of the new "ipv6_address_virtuals"<br>If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtuals</samp>](## "vlan_interfaces.[].ipv6_address_virtuals") | List, items: String |  |  |  | The new "ipv6_address_virtuals" key support multiple virtual ipv6 addresses. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "vlan_interfaces.[].ipv6_address_virtuals.[].&lt;str&gt;") | String |  |  |  | IPv6_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_link_local</samp>](## "vlan_interfaces.[].ipv6_address_link_local") | String |  |  |  | IPv6_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_address</samp>](## "vlan_interfaces.[].ipv6_virtual_router_address") | String |  |  |  | "ipv6_virtual_router_address" key will be deprecated in AVD v4.0<br>This should not be mixed with the new "ipv6_virtual_router_addresses" key below to avoid conflicts.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_addresses</samp>](## "vlan_interfaces.[].ipv6_virtual_router_addresses") | List, items: String |  |  |  | Improved "VARPv6" data model to support multiple VARPv6 addresses. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "vlan_interfaces.[].ipv6_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  | IPv6 address or IPv6_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_ra_disabled</samp>](## "vlan_interfaces.[].ipv6_nd_ra_disabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_managed_config_flag</samp>](## "vlan_interfaces.[].ipv6_nd_managed_config_flag") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_prefixes</samp>](## "vlan_interfaces.[].ipv6_nd_prefixes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ipv6_prefix</samp>](## "vlan_interfaces.[].ipv6_nd_prefixes.[].ipv6_prefix") | String | Required, Unique |  |  | IPv6_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;valid_lifetime</samp>](## "vlan_interfaces.[].ipv6_nd_prefixes.[].valid_lifetime") | String |  |  |  | In seconds <0-4294967295> or infinite |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preferred_lifetime</samp>](## "vlan_interfaces.[].ipv6_nd_prefixes.[].preferred_lifetime") | String |  |  |  | In seconds <0-4294967295> or infinite |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_autoconfig_flag</samp>](## "vlan_interfaces.[].ipv6_nd_prefixes.[].no_autoconfig_flag") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_in</samp>](## "vlan_interfaces.[].access_group_in") | String |  |  |  | IPv4 access-list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_out</samp>](## "vlan_interfaces.[].access_group_out") | String |  |  |  | IPv4 access-list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_in</samp>](## "vlan_interfaces.[].ipv6_access_group_in") | String |  |  |  | IPv6 access-list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_out</samp>](## "vlan_interfaces.[].ipv6_access_group_out") | String |  |  |  | IPv6 access-list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "vlan_interfaces.[].multicast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "vlan_interfaces.[].multicast.ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boundaries</samp>](## "vlan_interfaces.[].multicast.ipv4.boundaries") | List, items: Dictionary |  |  |  | Boundaries can be either 1 ACL or a list of multicast IP address_range(s)/prefix but not combination of both |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- boundary</samp>](## "vlan_interfaces.[].multicast.ipv4.boundaries.[].boundary") | String | Required, Unique |  |  | IPv4 access-list name or IPv4 multicast group prefix with mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;out</samp>](## "vlan_interfaces.[].multicast.ipv4.boundaries.[].out") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_route_export</samp>](## "vlan_interfaces.[].multicast.ipv4.source_route_export") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "vlan_interfaces.[].multicast.ipv4.source_route_export.enabled") | Boolean | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;administrative_distance</samp>](## "vlan_interfaces.[].multicast.ipv4.source_route_export.administrative_distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "vlan_interfaces.[].multicast.ipv4.static") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "vlan_interfaces.[].multicast.ipv6") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boundaries</samp>](## "vlan_interfaces.[].multicast.ipv6.boundaries") | List, items: Dictionary |  |  |  | Boundaries can be either 1 ACL or a list of multicast IP address_range(s)/prefix but not combination of both |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- boundary</samp>](## "vlan_interfaces.[].multicast.ipv6.boundaries.[].boundary") | String | Required, Unique |  |  | IPv6 access-list name or IPv6 multicast group prefix with mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_route_export</samp>](## "vlan_interfaces.[].multicast.ipv6.source_route_export") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "vlan_interfaces.[].multicast.ipv6.source_route_export.enabled") | Boolean | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;administrative_distance</samp>](## "vlan_interfaces.[].multicast.ipv6.source_route_export.administrative_distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "vlan_interfaces.[].multicast.ipv6.static") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_network_point_to_point</samp>](## "vlan_interfaces.[].ospf_network_point_to_point") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_area</samp>](## "vlan_interfaces.[].ospf_area") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_cost</samp>](## "vlan_interfaces.[].ospf_cost") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication</samp>](## "vlan_interfaces.[].ospf_authentication") | String |  |  | Valid Values:<br>- none<br>- simple<br>- message-digest |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication_key</samp>](## "vlan_interfaces.[].ospf_authentication_key") | String |  |  |  | Encrypted password used for simple authentication |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_message_digest_keys</samp>](## "vlan_interfaces.[].ospf_message_digest_keys") | List, items: Dictionary |  |  |  | Keys used for message-digest authentication |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "vlan_interfaces.[].ospf_message_digest_keys.[].id") | Integer | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "vlan_interfaces.[].ospf_message_digest_keys.[].hash_algorithm") | String |  |  | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "vlan_interfaces.[].ospf_message_digest_keys.[].key") | String |  |  |  | Encrypted password |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pim</samp>](## "vlan_interfaces.[].pim") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "vlan_interfaces.[].pim.ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dr_priority</samp>](## "vlan_interfaces.[].pim.ipv4.dr_priority") | Integer |  |  | Min: 0<br>Max: 429467295 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sparse_mode</samp>](## "vlan_interfaces.[].pim.ipv4.sparse_mode") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "vlan_interfaces.[].pim.ipv4.local_interface") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_enable</samp>](## "vlan_interfaces.[].isis_enable") | String |  |  |  | ISIS instance name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_passive</samp>](## "vlan_interfaces.[].isis_passive") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "vlan_interfaces.[].isis_metric") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_network_point_to_point</samp>](## "vlan_interfaces.[].isis_network_point_to_point") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "vlan_interfaces.[].mtu") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;no_autostate</samp>](## "vlan_interfaces.[].no_autostate") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrrp_ids</samp>](## "vlan_interfaces.[].vrrp_ids") | List, items: Dictionary |  |  |  | Improved "vrrp" data model to support multiple VRRP IDs |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "vlan_interfaces.[].vrrp_ids.[].id") | Integer | Required, Unique |  |  | VRID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority_level</samp>](## "vlan_interfaces.[].vrrp_ids.[].priority_level") | Integer |  |  |  | Instance priority |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;advertisement</samp>](## "vlan_interfaces.[].vrrp_ids.[].advertisement") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "vlan_interfaces.[].vrrp_ids.[].advertisement.interval") | Integer |  |  |  | Interval in seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preempt</samp>](## "vlan_interfaces.[].vrrp_ids.[].preempt") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "vlan_interfaces.[].vrrp_ids.[].preempt.enabled") | Boolean | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "vlan_interfaces.[].vrrp_ids.[].preempt.delay") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "vlan_interfaces.[].vrrp_ids.[].preempt.delay.minimum") | Integer |  |  |  | Minimum preempt delay in seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reload</samp>](## "vlan_interfaces.[].vrrp_ids.[].preempt.delay.reload") | Integer |  |  |  | Reload preempt delay in seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "vlan_interfaces.[].vrrp_ids.[].timers") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "vlan_interfaces.[].vrrp_ids.[].timers.delay") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reload</samp>](## "vlan_interfaces.[].vrrp_ids.[].timers.delay.reload") | Integer |  |  |  | Delay after reload in seconds. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tracked_object</samp>](## "vlan_interfaces.[].vrrp_ids.[].tracked_object") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "vlan_interfaces.[].vrrp_ids.[].tracked_object.[].name") | String | Required, Unique |  |  | Tracked object name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decrement</samp>](## "vlan_interfaces.[].vrrp_ids.[].tracked_object.[].decrement") | Integer |  |  | Min: 1<br>Max: 254 | Decrement VRRP priority by 1-254 |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "vlan_interfaces.[].vrrp_ids.[].tracked_object.[].shutdown") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "vlan_interfaces.[].vrrp_ids.[].ipv4") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "vlan_interfaces.[].vrrp_ids.[].ipv4.address") | String | Required |  |  | Virtual IPv4 address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "vlan_interfaces.[].vrrp_ids.[].ipv4.version") | Integer |  |  | Valid Values:<br>- 2<br>- 3 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "vlan_interfaces.[].vrrp_ids.[].ipv6") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "vlan_interfaces.[].vrrp_ids.[].ipv6.address") | String | Required |  |  | Virtual IPv6 address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrrp</samp>](## "vlan_interfaces.[].vrrp") | Dictionary |  |  |  | "vrrp" key will be deprecated in AVD v4.0<br>This should not be mixed with the new "vrrp_ids" key above to avoid conflicts.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;virtual_router</samp>](## "vlan_interfaces.[].vrrp.virtual_router") | String |  |  |  | Virtual Router ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "vlan_interfaces.[].vrrp.priority") | Integer |  |  |  | Instance priority |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;advertisement_interval</samp>](## "vlan_interfaces.[].vrrp.advertisement_interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preempt_delay_minimum</samp>](## "vlan_interfaces.[].vrrp.preempt_delay_minimum") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "vlan_interfaces.[].vrrp.ipv4") | String |  |  |  | Virtual IPv4 address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "vlan_interfaces.[].vrrp.ipv6") | String |  |  |  | Virtual IPv6 address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_attached_host_route_export</samp>](## "vlan_interfaces.[].ip_attached_host_route_export") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "vlan_interfaces.[].ip_attached_host_route_export.distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "vlan_interfaces.[].bfd") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo</samp>](## "vlan_interfaces.[].bfd.echo") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "vlan_interfaces.[].bfd.interval") | Integer |  |  |  | Rate in milliseconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "vlan_interfaces.[].bfd.min_rx") | Integer |  |  |  | Minimum RX hold time in milliseconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "vlan_interfaces.[].bfd.multiplier") | Integer |  |  | Min: 3<br>Max: 50 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_policy</samp>](## "vlan_interfaces.[].service_policy") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pbr</samp>](## "vlan_interfaces.[].service_policy.pbr") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp>](## "vlan_interfaces.[].service_policy.pbr.input") | String |  |  |  | Name of policy-map used for policy based routing |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pvlan_mapping</samp>](## "vlan_interfaces.[].pvlan_mapping") | String |  |  |  | List of VLANs as string |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp>](## "vlan_interfaces.[].tenant") | String |  |  |  | Key only used for documentation or validation purposes |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "vlan_interfaces.[].tags") | List, items: String |  |  |  | Key only used for documentation or validation purposes |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "vlan_interfaces.[].tags.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "vlan_interfaces.[].type") | String |  |  |  | Key only used for documentation or validation purposes |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "vlan_interfaces.[].eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the VLAN interface in the final EOS configuration |

### YAML

```yaml
vlan_interfaces:
  - name: <str>
    description: <str>
    shutdown: <bool>
    vrf: <str>
    arp_aging_timeout: <int>
    arp_cache_dynamic_capacity: <int>
    arp_gratuitous_accept: <bool>
    arp_monitor_mac_address: <bool>
    ip_proxy_arp: <bool>
    ip_directed_broadcast: <bool>
    ip_address: <str>
    ip_address_secondaries:
      - <str>
    ip_virtual_router_addresses:
      - <str>
    ip_address_virtual: <str>
    ip_address_virtual_secondaries:
      - <str>
    ip_igmp: <bool>
    ip_helpers:
      - ip_helper: <str>
        source_interface: <str>
        vrf: <str>
    ipv6_enable: <bool>
    ipv6_address: <str>
    ipv6_address_virtual: <str>
    ipv6_address_virtuals:
      - <str>
    ipv6_address_link_local: <str>
    ipv6_virtual_router_address: <str>
    ipv6_virtual_router_addresses:
      - <str>
    ipv6_nd_ra_disabled: <bool>
    ipv6_nd_managed_config_flag: <bool>
    ipv6_nd_prefixes:
      - ipv6_prefix: <str>
        valid_lifetime: <str>
        preferred_lifetime: <str>
        no_autoconfig_flag: <bool>
    access_group_in: <str>
    access_group_out: <str>
    ipv6_access_group_in: <str>
    ipv6_access_group_out: <str>
    multicast:
      ipv4:
        boundaries:
          - boundary: <str>
            out: <bool>
        source_route_export:
          enabled: <bool>
          administrative_distance: <int>
        static: <bool>
      ipv6:
        boundaries:
          - boundary: <str>
        source_route_export:
          enabled: <bool>
          administrative_distance: <int>
        static: <bool>
    ospf_network_point_to_point: <bool>
    ospf_area: <str>
    ospf_cost: <int>
    ospf_authentication: <str>
    ospf_authentication_key: <str>
    ospf_message_digest_keys:
      - id: <int>
        hash_algorithm: <str>
        key: <str>
    pim:
      ipv4:
        dr_priority: <int>
        sparse_mode: <bool>
        local_interface: <str>
    isis_enable: <str>
    isis_passive: <bool>
    isis_metric: <int>
    isis_network_point_to_point: <bool>
    mtu: <int>
    no_autostate: <bool>
    vrrp_ids:
      - id: <int>
        priority_level: <int>
        advertisement:
          interval: <int>
        preempt:
          enabled: <bool>
          delay:
            minimum: <int>
            reload: <int>
        timers:
          delay:
            reload: <int>
        tracked_object:
          - name: <str>
            decrement: <int>
            shutdown: <bool>
        ipv4:
          address: <str>
          version: <int>
        ipv6:
          address: <str>
    vrrp:
      virtual_router: <str>
      priority: <int>
      advertisement_interval: <int>
      preempt_delay_minimum: <int>
      ipv4: <str>
      ipv6: <str>
    ip_attached_host_route_export:
      distance: <int>
    bfd:
      echo: <bool>
      interval: <int>
      min_rx: <int>
      multiplier: <int>
    service_policy:
      pbr:
        input: <str>
    pvlan_mapping: <str>
    tenant: <str>
    tags:
      - <str>
    type: <str>
    eos_cli: <str>
```

## VLAN Internal Order

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>vlan_internal_order</samp>](## "vlan_internal_order") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;allocation</samp>](## "vlan_internal_order.allocation") | String | Required |  | Valid Values:<br>- ascending<br>- descending |  |
| [<samp>&nbsp;&nbsp;range</samp>](## "vlan_internal_order.range") | Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;beginning</samp>](## "vlan_internal_order.range.beginning") | Integer | Required |  | Min: 1<br>Max: 4094 | Vlan ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ending</samp>](## "vlan_internal_order.range.ending") | Integer | Required |  | Min: 1<br>Max: 4094 | Vlan ID |

### YAML

```yaml
vlan_internal_order:
  allocation: <str>
  range:
    beginning: <int>
    ending: <int>
```

## VLANs

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>vlans</samp>](## "vlans") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- id</samp>](## "vlans.[].id") | Integer | Required, Unique |  |  | VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "vlans.[].name") | String |  |  |  | VLAN Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;state</samp>](## "vlans.[].state") | String |  |  | Valid Values:<br>- active<br>- suspend |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "vlans.[].trunk_groups") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "vlans.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk Group Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;private_vlan</samp>](## "vlans.[].private_vlan") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "vlans.[].private_vlan.type") | String |  |  | Valid Values:<br>- community<br>- isolated |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary_vlan</samp>](## "vlans.[].private_vlan.primary_vlan") | Integer |  |  |  | Primary VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp>](## "vlans.[].tenant") | String |  |  |  | Key only used for documentation or validation purposes |

### YAML

```yaml
vlans:
  - id: <int>
    name: <str>
    state: <str>
    trunk_groups:
      - <str>
    private_vlan:
      type: <str>
      primary_vlan: <int>
    tenant: <str>
```

## VMTracer Sessions

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>vmtracer_sessions</samp>](## "vmtracer_sessions") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "vmtracer_sessions.[].name") | String | Required, Unique |  |  | Vmtracer Session Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "vmtracer_sessions.[].url") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;username</samp>](## "vmtracer_sessions.[].username") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "vmtracer_sessions.[].password") | String |  |  |  | Type 7 Password Hash |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;autovlan_disable</samp>](## "vmtracer_sessions.[].autovlan_disable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "vmtracer_sessions.[].source_interface") | String |  |  |  |  |

### YAML

```yaml
vmtracer_sessions:
  - name: <str>
    url: <str>
    username: <str>
    password: <str>
    autovlan_disable: <bool>
    source_interface: <str>
```

## VRFs

### Description

These keys are ignored if the name of the vrf is 'default'

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>vrfs</samp>](## "vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "vrfs.[].name") | String | Required, Unique |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "vrfs.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_routing</samp>](## "vrfs.[].ip_routing") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_routing</samp>](## "vrfs.[].ipv6_routing") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_routing_ipv6_interfaces</samp>](## "vrfs.[].ip_routing_ipv6_interfaces") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp>](## "vrfs.[].tenant") | String |  |  |  | Key only used for documentation or validation purposes |

### YAML

```yaml
vrfs:
  - name: <str>
    description: <str>
    ip_routing: <bool>
    ipv6_routing: <bool>
    ip_routing_ipv6_interfaces: <bool>
    tenant: <str>
```

## VxLAN Interface

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>vxlan_interface</samp>](## "vxlan_interface") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;Vxlan1</samp>](## "vxlan_interface.Vxlan1") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "vxlan_interface.Vxlan1.description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "vxlan_interface.Vxlan1.vxlan") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "vxlan_interface.Vxlan1.vxlan.source_interface") | String |  |  |  | Source Interface Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_source_interface</samp>](## "vxlan_interface.Vxlan1.vxlan.mlag_source_interface") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_port</samp>](## "vxlan_interface.Vxlan1.vxlan.udp_port") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;virtual_router_encapsulation_mac_address</samp>](## "vxlan_interface.Vxlan1.vxlan.virtual_router_encapsulation_mac_address") | String |  |  |  | "mlag-system-id" or ethernet_address (H.H.H)<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd_vtep_evpn</samp>](## "vxlan_interface.Vxlan1.vxlan.bfd_vtep_evpn") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "vxlan_interface.Vxlan1.vxlan.bfd_vtep_evpn.interval") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "vxlan_interface.Vxlan1.vxlan.bfd_vtep_evpn.min_rx") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "vxlan_interface.Vxlan1.vxlan.bfd_vtep_evpn.multiplier") | Integer |  |  | Min: 3<br>Max: 50 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "vxlan_interface.Vxlan1.vxlan.bfd_vtep_evpn.prefix_list") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos</samp>](## "vxlan_interface.Vxlan1.vxlan.qos") | Dictionary |  |  |  | For the Traffic Class to be derived based on the outer DSCP field of the incoming VxLan packet, the core ports must be in "DSCP Trust" mode.<br>!!!Warning, only few hardware types with software version >= 4.26.0 support the below knobs to configure Vxlan DSCP mapping.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp_propagation_encapsulation</samp>](## "vxlan_interface.Vxlan1.vxlan.qos.dscp_propagation_encapsulation") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;map_dscp_to_traffic_class_decapsulation</samp>](## "vxlan_interface.Vxlan1.vxlan.qos.map_dscp_to_traffic_class_decapsulation") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "vxlan_interface.Vxlan1.vxlan.vlans") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "vxlan_interface.Vxlan1.vxlan.vlans.[].id") | Integer | Required, Unique |  |  | VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni</samp>](## "vxlan_interface.Vxlan1.vxlan.vlans.[].vni") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast_group</samp>](## "vxlan_interface.Vxlan1.vxlan.vlans.[].multicast_group") | String |  |  |  | IP Multicast Group Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flood_vteps</samp>](## "vxlan_interface.Vxlan1.vxlan.vlans.[].flood_vteps") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "vxlan_interface.Vxlan1.vxlan.vlans.[].flood_vteps.[].&lt;str&gt;") | String |  |  |  | Remote VTEP IP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "vxlan_interface.Vxlan1.vxlan.vrfs") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "vxlan_interface.Vxlan1.vxlan.vrfs.[].name") | String | Required, Unique |  |  | VRF Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni</samp>](## "vxlan_interface.Vxlan1.vxlan.vrfs.[].vni") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast_group</samp>](## "vxlan_interface.Vxlan1.vxlan.vrfs.[].multicast_group") | String |  |  |  | IP Multicast Group Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flood_vteps</samp>](## "vxlan_interface.Vxlan1.vxlan.flood_vteps") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "vxlan_interface.Vxlan1.vxlan.flood_vteps.[].&lt;str&gt;") | String |  |  |  | Remote VTEP IP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flood_vtep_learned_data_plane</samp>](## "vxlan_interface.Vxlan1.vxlan.flood_vtep_learned_data_plane") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "vxlan_interface.Vxlan1.eos_cli") | String |  |  |  | Multiline String with EOS CLI rendered directly on the Vxlan interface in the final EOS configuration. |

### YAML

```yaml
vxlan_interface:
  Vxlan1:
    description: <str>
    vxlan:
      source_interface: <str>
      mlag_source_interface: <str>
      udp_port: <int>
      virtual_router_encapsulation_mac_address: <str>
      bfd_vtep_evpn:
        interval: <int>
        min_rx: <int>
        multiplier: <int>
        prefix_list: <str>
      qos:
        dscp_propagation_encapsulation: <bool>
        map_dscp_to_traffic_class_decapsulation: <bool>
      vlans:
        - id: <int>
          vni: <int>
          multicast_group: <str>
          flood_vteps:
            - <str>
      vrfs:
        - name: <str>
          vni: <int>
          multicast_group: <str>
      flood_vteps:
        - <str>
      flood_vtep_learned_data_plane: <bool>
    eos_cli: <str>
```
