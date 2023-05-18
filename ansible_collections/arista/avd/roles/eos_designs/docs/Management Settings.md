---
search:
  boost: 2
---

# Management Settings

## CloudVision Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cvp_ingestauth_key</samp>](## "cvp_ingestauth_key") | String |  |  |  | On-premise CVP ingest auth key. If set, TerminAttr will be configured with key-based authentication for on-premise CVP.<br>If not set, TerminAttr will be configured with certificate based authentication:<br>- On-premise using token onboarding. Default token path is '/tmp/token'.<br>- CVaaS using token-secure onboarding. Default token path is '/tmp/cv-onboarding-token'.<br>Token must be copied to the device first. |
    | [<samp>cvp_instance_ip</samp>](## "cvp_instance_ip") | String |  |  |  | IPv4 address or DNS name for CloudVision.<br>This variable only supports an on-premise single-node cluster or the DNS name of a CloudVision as a Service instance. |
    | [<samp>cvp_instance_ips</samp>](## "cvp_instance_ips") | List, items: String |  |  |  | List of IPv4 addresses or DNS names for CloudVision.<br>For on-premise CloudVision enter all the nodes of the cluster.<br>For CloudVision as a Service enter the DNS name of the instance.<br>`eos_designs` only supports one CloudVision cluster.<br> |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "cvp_instance_ips.[].&lt;str&gt;") | String |  |  |  | IPv4 address or DNS name for CloudVision |
    | [<samp>cvp_token_file</samp>](## "cvp_token_file") | String |  |  |  | cvp_token_file is the path to the token file on the switch.<br>If not set the default locations for on-premise or CVaaS will be used.<br>See cvp_ingestauth_key for details. |
    | [<samp>terminattr_disable_aaa</samp>](## "terminattr_disable_aaa") | Boolean |  | False |  |  |
    | [<samp>terminattr_ingestexclude</samp>](## "terminattr_ingestexclude") | String |  | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent |  |  |
    | [<samp>terminattr_ingestgrpcurl_port</samp>](## "terminattr_ingestgrpcurl_port") | Integer |  | 9910 |  | Port number used for Terminattr connection to an on-premise CloudVision cluster.<br>The port number is always 443 when using CloudVision as a Service, so this value is ignored. |
    | [<samp>terminattr_smashexcludes</samp>](## "terminattr_smashexcludes") | String |  | ale,flexCounter,hardware,kni,pulse,strata |  |  |

=== "YAML"

    ```yaml
    cvp_ingestauth_key: <str>
    cvp_instance_ip: <str>
    cvp_instance_ips:
      - <str>
    cvp_token_file: <str>
    terminattr_disable_aaa: <bool>
    terminattr_ingestexclude: <str>
    terminattr_ingestgrpcurl_port: <int>
    terminattr_smashexcludes: <str>
    ```

## IPv6 Mgmt Destination Networks

IPv6_network/Mask

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ipv6_mgmt_destination_networks</samp>](## "ipv6_mgmt_destination_networks") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "ipv6_mgmt_destination_networks.[].&lt;str&gt;") | String |  |  |  |  |

=== "YAML"

    ```yaml
    ipv6_mgmt_destination_networks:
      - <str>
    ```

## IPv6 Mgmt Gateway

IPv6 address

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ipv6_mgmt_gateway</samp>](## "ipv6_mgmt_gateway") | String |  |  | Format: ipv6 |  |

=== "YAML"

    ```yaml
    ipv6_mgmt_gateway: <str>
    ```
