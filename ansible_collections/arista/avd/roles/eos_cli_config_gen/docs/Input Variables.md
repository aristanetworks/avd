---
search:
  boost: 2
---

# Input Variables

## Attribute 32 Include In Access Req

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>attribute_32_include_in_access_req</samp>](## "attribute_32_include_in_access_req") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;hostname</samp>](## "attribute_32_include_in_access_req.hostname") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;format</samp>](## "attribute_32_include_in_access_req.format") | String |  |  |  | Name of ACL |

=== "YAML"

    ```yaml
    attribute_32_include_in_access_req:
      hostname: <bool>
      format: <str>
    ```

## Dynamic Authorization

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dynamic_authorization</samp>](## "dynamic_authorization") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;port</samp>](## "dynamic_authorization.port") | Integer |  |  | Min: 0<br>Max: 65535 | TCP Port |
    | [<samp>&nbsp;&nbsp;tls_ssl_profile</samp>](## "dynamic_authorization.tls_ssl_profile") | String |  |  |  | Name of TLS profile |

=== "YAML"

    ```yaml
    dynamic_authorization:
      port: <int>
      tls_ssl_profile: <str>
    ```

## Hosts

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>hosts</samp>](## "hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- host</samp>](## "hosts.[].host") | String | Required, Unique |  |  | Host IP address or name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "hosts.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "hosts.[].timeout") | Integer |  |  | Min: 1<br>Max: 1000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;retransmit</samp>](## "hosts.[].retransmit") | Integer |  |  | Min: 0<br>Max: 100 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "hosts.[].key") | String |  |  |  | Encrypted key |

=== "YAML"

    ```yaml
    hosts:
      - host: <str>
        vrf: <str>
        timeout: <int>
        retransmit: <int>
        key: <str>
    ```
