---
search:
  boost: 2
---

# Management

## Clock

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>clock</samp>](## "clock") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;timezone</samp>](## "clock.timezone") | String |  |  |  |  |

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
    | [<samp>dns_domain</samp>](## "dns_domain") | String |  |  |  |  |

=== "YAML"

    ```yaml
    dns_domain: <str>
    ```

## Domain List

Search list of DNS domains

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>domain_list</samp>](## "domain_list") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "domain_list.[].&lt;str&gt;") | String |  |  |  | Domain name |

=== "YAML"

    ```yaml
    domain_list:
      - <str>
    ```

## IP Domain Lookup

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_domain_lookup</samp>](## "ip_domain_lookup") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;source_interfaces</samp>](## "ip_domain_lookup.source_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "ip_domain_lookup.source_interfaces.[].name") | String | Required, Unique |  |  | Source Interface<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_domain_lookup.source_interfaces.[].vrf") | String |  |  |  |  |

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
    | [<samp>ip_http_client_source_interfaces</samp>](## "ip_http_client_source_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "ip_http_client_source_interfaces.[].name") | String |  |  |  | Interface Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_http_client_source_interfaces.[].vrf") | String |  |  |  |  |

=== "YAML"

    ```yaml
    ip_http_client_source_interfaces:
      - name: <str>
        vrf: <str>
    ```

## IP Name Servers

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_name_servers</samp>](## "ip_name_servers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- ip_address</samp>](## "ip_name_servers.[].ip_address") | String |  |  |  | IPv4 or IPv6 address for DNS server |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_name_servers.[].vrf") | String |  |  |  | VRF Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "ip_name_servers.[].priority") | Integer |  |  | Min: 0<br>Max: 4 | Priority value (lower is first) |

=== "YAML"

    ```yaml
    ip_name_servers:
      - ip_address: <str>
        vrf: <str>
        priority: <int>
    ```

## IP SSH Client Source Interfaces

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_ssh_client_source_interfaces</samp>](## "ip_ssh_client_source_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "ip_ssh_client_source_interfaces.[].name") | String |  |  |  | Interface Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_ssh_client_source_interfaces.[].vrf") | String |  | default |  |  |

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
    | [<samp>management_api_gnmi</samp>](## "management_api_gnmi") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;provider</samp>](## "management_api_gnmi.provider") | String |  | eos-native |  |  |
    | [<samp>&nbsp;&nbsp;transport</samp>](## "management_api_gnmi.transport") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;grpc</samp>](## "management_api_gnmi.transport.grpc") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_api_gnmi.transport.grpc.[].name") | String |  |  |  | Transport name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ssl_profile</samp>](## "management_api_gnmi.transport.grpc.[].ssl_profile") | String |  |  |  | SSL profile name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_api_gnmi.transport.grpc.[].vrf") | String |  |  |  | VRF name is optional |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;notification_timestamp</samp>](## "management_api_gnmi.transport.grpc.[].notification_timestamp") | String |  |  | Valid Values:<br>- send-time<br>- last-change-time | Per the GNMI specification, the default timestamp field of a notification message is set to be<br>the time at which the value of the underlying data source changes or when the reported event takes place.<br>In order to facilitate integration in legacy environments oriented around polling style operations,<br>an option to support overriding the timestamp field to the send-time is available from EOS 4.27.0F.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_access_group</samp>](## "management_api_gnmi.transport.grpc.[].ip_access_group") | String |  |  |  | ACL name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;grpc_tunnels</samp>](## "management_api_gnmi.transport.grpc_tunnels") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].name") | String | Required, Unique |  |  | Transport name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].shutdown") | Boolean |  |  |  | Operational status of the gRPC tunnel |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel_ssl_profile</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].tunnel_ssl_profile") | String |  |  |  | Tunnel SSL profile name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gnmi_ssl_profile</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].gnmi_ssl_profile") | String |  |  |  | gNMI SSL profile name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].vrf") | String |  |  |  | VRF name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].destination") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].destination.address") | String | Required |  |  | IP address or hostname |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].destination.port") | Integer | Required |  | Min: 1<br>Max: 65535 | TCP Port |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].local_interface") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].local_interface.name") | String | Required |  |  | Interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].local_interface.port") | Integer | Required |  | Min: 1<br>Max: 65535 | TCP Port |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;target</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].target") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_serial_number</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].target.use_serial_number") | Boolean |  |  |  | Use serial number as the Target ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;target_ids</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].target.target_ids") | List, items: String |  |  |  | Target IDs as a list.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].target.target_ids.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable_vrfs</samp>](## "management_api_gnmi.enable_vrfs") | List, items: Dictionary |  |  |  | Enable VRFs will be deprecated in AVD v4.0.<br>These should not be mixed with the new keys above.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_api_gnmi.enable_vrfs.[].name") | String | Required, Unique |  |  | VRF name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "management_api_gnmi.enable_vrfs.[].access_group") | String |  |  |  | Standard IPv4 ACL name |
    | [<samp>&nbsp;&nbsp;octa</samp>](## "management_api_gnmi.octa") | Dictionary |  |  |  | Octa key will be deprecated in AVD v4.0.<br>These should not be mixed with the new keys above.<br>Octa activates `eos-native` provider and it is the only provider currently supported by EOS. |

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
        grpc_tunnels:
          - name: <str>
            shutdown: <bool>
            tunnel_ssl_profile: <str>
            gnmi_ssl_profile: <str>
            vrf: <str>
            destination:
              address: <str>
              port: <int>
            local_interface:
              name: <str>
              port: <int>
            target:
              use_serial_number: <bool>
              target_ids:
                - <str>
      enable_vrfs:
        - name: <str>
          access_group: <str>
      octa:
    ```

## Management API HTTP

=== "Table"

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
    | [<samp>management_api_models</samp>](## "management_api_models") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;providers</samp>](## "management_api_models.providers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "management_api_models.providers.[].name") | String |  |  | Valid Values:<br>- sysdb<br>- smash |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;paths</samp>](## "management_api_models.providers.[].paths") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- path</samp>](## "management_api_models.providers.[].paths.[].path") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "management_api_models.providers.[].paths.[].disabled") | Boolean |  | False |  |  |

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
    | [<samp>management_console</samp>](## "management_console") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;idle_timeout</samp>](## "management_console.idle_timeout") | Integer |  |  | Min: 0<br>Max: 86400 |  |

=== "YAML"

    ```yaml
    management_console:
      idle_timeout: <int>
    ```

## Management CVX

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_cvx</samp>](## "management_cvx") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;shutdown</samp>](## "management_cvx.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;server_hosts</samp>](## "management_cvx.server_hosts") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "management_cvx.server_hosts.[].&lt;str&gt;") | String |  |  |  | IP or hostname |
    | [<samp>&nbsp;&nbsp;source_interface</samp>](## "management_cvx.source_interface") | String |  |  |  | Interface name |
    | [<samp>&nbsp;&nbsp;vrf</samp>](## "management_cvx.vrf") | String |  |  |  | VRF Name |

=== "YAML"

    ```yaml
    management_cvx:
      shutdown: <bool>
      server_hosts:
        - <str>
      source_interface: <str>
      vrf: <str>
    ```

## Management Defaults

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_defaults</samp>](## "management_defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;secret</samp>](## "management_defaults.secret") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hash</samp>](## "management_defaults.secret.hash") | String |  |  | Valid Values:<br>- md5<br>- sha512 |  |

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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "management_interfaces.[].eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the management interface in the final EOS configuration |

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
    | [<samp>management_tech_support</samp>](## "management_tech_support") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;policy_show_tech_support</samp>](## "management_tech_support.policy_show_tech_support") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;exclude_commands</samp>](## "management_tech_support.policy_show_tech_support.exclude_commands") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- command</samp>](## "management_tech_support.policy_show_tech_support.exclude_commands.[].command") | String |  |  |  | Command to exclude from tech-support |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "management_tech_support.policy_show_tech_support.exclude_commands.[].type") | String |  | text | Valid Values:<br>- text<br>- json | The supported values for type are platform dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;include_commands</samp>](## "management_tech_support.policy_show_tech_support.include_commands") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- command</samp>](## "management_tech_support.policy_show_tech_support.include_commands.[].command") | String |  |  |  | Command to include in tech-support |

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
    | [<samp>name_server</samp>](## "name_server") <span style="color:red">deprecated</span> | Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version v5.0.0. Use <samp>ip_name_servers</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;source</samp>](## "name_server.source") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "name_server.source.vrf") | String |  |  |  | VRF Name |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "name_server.nodes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "name_server.nodes.[].&lt;str&gt;") | String |  |  |  |  |

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
