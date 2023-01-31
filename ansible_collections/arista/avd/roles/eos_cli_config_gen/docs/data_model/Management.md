---
search:
  boost: 2
---

# Management

## Clock

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>clock</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;timezone</samp> | String |  |  |  |  |

=== "YAML"

    ```yaml
    clock:
      timezone: <str>
    ```

## DNS Domain

Domain Name
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>dns_domain</samp> | String |  |  |  |  |

=== "YAML"

    ```yaml
    dns_domain: <str>
    ```

## Domain List

Search list of DNS domains
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>domain_list</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Domain name |

=== "YAML"

    ```yaml
    domain_list:
      - <str>
    ```

## IP Domain Lookup

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ip_domain_lookup</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;source_interfaces</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Source Interface<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  |  |

=== "YAML"

    ```yaml
    ip_domain_lookup:
      source_interfaces:
        - name: <str>
          vrf: <str>
    ```

## IP HTTP Client Source Interfaces

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ip_http_client_source_interfaces</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String |  |  |  | Interface Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  |  |

=== "YAML"

    ```yaml
    ip_http_client_source_interfaces:
      - name: <str>
        vrf: <str>
    ```

## IP SSH Client Source Interfaces

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ip_ssh_client_source_interfaces</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String |  |  |  | Interface Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  | default |  |  |

=== "YAML"

    ```yaml
    ip_ssh_client_source_interfaces:
      - name: <str>
        vrf: <str>
    ```

## Management API Gnmi

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>management_api_gnmi</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;provider</samp> | String |  | eos-native |  |  |
    | <samp>&nbsp;&nbsp;transport</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;grpc</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  | Transport name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ssl_profile</samp> | String |  |  |  | SSL profile name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  | VRF name is optional |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;notification_timestamp</samp> | String |  |  | Valid Values:<br>- send-time<br>- last-change-time | Per the GNMI specification, the default timestamp field of a notification message is set to be<br>the time at which the value of the underlying data source changes or when the reported event takes place.<br>In order to facilitate integration in legacy environments oriented around polling style operations,<br>an option to support overriding the timestamp field to the send-time is available from EOS 4.27.0F.<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_access_group</samp> | String |  |  |  | ACL name |
    | <samp>&nbsp;&nbsp;enable_vrfs</samp> | List, items: Dictionary |  |  |  | Enable VRFs will be deprecated in AVD v4.0.<br>These should not be mixed with the new keys above.<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | VRF name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp> | String |  |  |  | Standard IPv4 ACL name |
    | <samp>&nbsp;&nbsp;octa</samp> | Dictionary |  |  |  | Octa key will be deprecated in AVD v4.0.<br>These should not be mixed with the new keys above.<br>Octa activates `eos-native` provider and it is the only provider currently supported by EOS. |

=== "YAML"

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

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>management_api_http</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;enable_http</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;enable_https</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;https_ssl_profile</samp> | String |  |  |  | SSL Profile Name |
    | <samp>&nbsp;&nbsp;default_services</samp> | Boolean |  |  |  | Enable default services: capi-doc and tapagg |
    | <samp>&nbsp;&nbsp;enable_vrfs</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | VRF Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp> | String |  |  |  | Standard IPv4 ACL name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group</samp> | String |  |  |  | Standard IPv6 ACL name |
    | <samp>&nbsp;&nbsp;protocol_https_certificate</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;certificate</samp> | String |  |  |  | Name of certificate; private key must also be specified |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;private_key</samp> | String |  |  |  | Name of private key; certificate must also be specified |

=== "YAML"

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

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>management_api_models</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;providers</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  | Valid Values:<br>- sysdb<br>- smash |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;paths</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- path</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp> | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    management_api_models:
      providers:
        - name: <str>
          paths:
            - path: <str>
              disabled: <bool>
    ```

## Management Console

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>management_console</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;idle_timeout</samp> | Integer |  |  | Min: 0<br>Max: 86400 |  |

=== "YAML"

    ```yaml
    management_console:
      idle_timeout: <int>
    ```

## Management CVX

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>management_cvx</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;shutdown</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;server_hosts</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | IP or hostname |
    | <samp>&nbsp;&nbsp;source_interface</samp> | String |  |  |  | Interface name |

=== "YAML"

    ```yaml
    management_cvx:
      shutdown: <bool>
      server_hosts:
        - <str>
      source_interface: <str>
    ```

## Management Defaults

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>management_defaults</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;secret</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;hash</samp> | String |  |  | Valid Values:<br>- md5<br>- sha512 |  |

=== "YAML"

    ```yaml
    management_defaults:
      secret:
        hash: <str>
    ```

## Management Interfaces

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>management_interfaces</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Management Interface Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  | VRF Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp> | String |  |  |  | IPv4_address/Mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp> | String |  |  |  | IPv6_address/Mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp> | String |  | oob | Valid Values:<br>- oob<br>- inband | For documentation purposes only |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp> | String |  |  |  | IPv4 address of default gateway in management VRF |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_gateway</samp> | String |  |  |  | IPv6 address of default gateway in management VRF |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp> | String |  |  |  | MAC address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp> | String |  |  |  | Multiline EOS CLI rendered directly on the management interface in the final EOS configuration |

=== "YAML"

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
        eos_cli: <str>
    ```

## Management Security

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>management_security</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;entropy_source</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;password</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;minimum_length</samp> | Integer |  |  | Min: 1<br>Max: 32 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;encryption_key_common</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;encryption_reversible</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;ssl_profiles</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tls_versions</samp> | String |  |  |  | List of allowed TLS versions as string<br>Examples:<br>  - "1.0"<br>  - "1.0 1.1"<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cipher_list</samp> | String |  |  |  | cipher_list syntax follows the openssl cipher strings format.<br>Colon (:) separated list of allowed ciphers as a string<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;certificate</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;file</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp> | String |  |  |  |  |

=== "YAML"

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

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>management_ssh</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;access_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  | Standard ACL Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  | VRF Name |
    | <samp>&nbsp;&nbsp;ipv6_access_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  | Standard ACL Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  | VRF Name |
    | <samp>&nbsp;&nbsp;idle_timeout</samp> | Integer |  |  | Min: 0<br>Max: 86400 | Idle timeout in minutes |
    | <samp>&nbsp;&nbsp;cipher</samp> | List, items: String |  |  |  | Cryptographic ciphers for SSH to use |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;key_exchange</samp> | List, items: String |  |  |  | Cryptographic key exchange methods for SSH to use |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;mac</samp> | List, items: String |  |  |  | Cryptographic MAC algorithms for SSH to use |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;hostkey</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;server</samp> | List, items: String |  |  |  | SSH host key settings |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;enable</samp> | Boolean |  |  |  | Enable SSH daemon |
    | <samp>&nbsp;&nbsp;connection</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;limit</samp> | Integer |  |  | Min: 1<br>Max: 100 | Maximum total number of SSH sessions to device |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;per_host</samp> | Integer |  |  | Min: 1<br>Max: 20 | Maximum number of SSH sessions to device from a single host |
    | <samp>&nbsp;&nbsp;vrfs</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | VRF Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp> | Boolean |  |  |  | Enable SSH in VRF |
    | <samp>&nbsp;&nbsp;log_level</samp> | String |  |  |  | SSH daemon log level |

=== "YAML"

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

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>management_tech_support</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;policy_show_tech_support</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;exclude_commands</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- command</samp> | String |  |  |  | Command to exclude from tech-support |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp> | String |  | text | Valid Values:<br>- text<br>- json | The supported values for type are platform dependent. |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;include_commands</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- command</samp> | String |  |  |  | Command to include in tech-support |

=== "YAML"

    ```yaml
    management_tech_support:
      policy_show_tech_support:
        exclude_commands:
          - command: <str>
            type: <str>
        include_commands:
          - command: <str>
    ```

## Name Server

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>name_server</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;source</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  | VRF Name |
    | <samp>&nbsp;&nbsp;nodes</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |

=== "YAML"

    ```yaml
    name_server:
      source:
        vrf: <str>
      nodes:
        - <str>
    ```

## NTP

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ntp</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;local_interface</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp> | String |  |  |  | Source interface |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  | VRF name |
    | <samp>&nbsp;&nbsp;servers</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  | IP or hostname e.g., 2.2.2.55, ie.pool.ntp.org |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;burst</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iburst</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp> | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp> | String |  |  |  | Source interface |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maxpoll</samp> | Integer |  |  | Min: 3<br>Max: 17 | Value of maxpoll between 3 - 17 (Logarithmic) |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minpoll</samp> | Integer |  |  | Min: 3<br>Max: 17 | Value of minpoll between 3 - 17 (Logarithmic) |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preferred</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp> | Integer |  |  | Min: 1<br>Max: 4 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  | VRF name |
    | <samp>&nbsp;&nbsp;authenticate</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;authenticate_servers_only</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;authentication_keys</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp> | Integer | Required, Unique |  | Min: 1<br>Max: 65534 | Key identifier |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp> | String |  |  | Valid Values:<br>- md5<br>- sha1 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp> | String |  |  |  | Obfuscated key |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp> | String |  |  | Valid Values:<br>- 0<br>- 7<br>- 8a |  |
    | <samp>&nbsp;&nbsp;trusted_keys</samp> | String |  |  |  | List of trusted-keys as string ex. 10-12,15 |

=== "YAML"

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
