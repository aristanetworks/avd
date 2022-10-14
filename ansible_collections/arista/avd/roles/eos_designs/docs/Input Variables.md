---
search:
  boost: 2
---

# Input Variables

## CVP Ingestauth Key

CloudVision ingest authentication key is required for on-prem CVP

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cvp_ingestauth_key</samp>](## "cvp_ingestauth_key") | String |  |  |  |  |

=== "YAML"

    ```yaml
    cvp_ingestauth_key: <str>
    ```

## CVP Instance IP

IPv4 address.
CloudVision - Telemetry Agent (TerminAttr) configuration is optional
You can either provide a list of IPs to target on-premise CloudVision cluster or
use DNS name for your CloudVision as a Service instance. If you have both on-prem and
CVaaS defined, only on-prem is going to be configured.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cvp_instance_ip</samp>](## "cvp_instance_ip") | String |  |  |  |  |

=== "YAML"

    ```yaml
    cvp_instance_ip: <str>
    ```

## CVP Instance Ips

You can either provide a list of IPs to target on-premise CloudVision cluster or
use DNS name for your CloudVision as a Service instance. If you have both on-prem and
CVaaS defined, only on-prem is going to be configured.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cvp_instance_ips</samp>](## "cvp_instance_ips") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "cvp_instance_ips.[].&lt;str&gt;") | String |  |  |  | IPv4 address or CV as a Service hostname |

=== "YAML"

    ```yaml
    cvp_instance_ips:
      - <str>
    ```

## CVP Token File

CVP token file is path to token file on switch and is only applicable to CV as a Service

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cvp_token_file</samp>](## "cvp_token_file") | String |  | /tmp/cv-onboarding-token |  |  |

=== "YAML"

    ```yaml
    cvp_token_file: <str>
    ```

## TerminAttr Disable AAA

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>terminattr_disable_aaa</samp>](## "terminattr_disable_aaa") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    terminattr_disable_aaa: <bool>
    ```

## TerminAttr Ingestexclude

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>terminattr_ingestexclude</samp>](## "terminattr_ingestexclude") | String |  | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent |  |  |

=== "YAML"

    ```yaml
    terminattr_ingestexclude: <str>
    ```

## TerminAttr Ingestgrpcurl Port

Port number

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>terminattr_ingestgrpcurl_port</samp>](## "terminattr_ingestgrpcurl_port") | Integer |  | 9910 |  |  |

=== "YAML"

    ```yaml
    terminattr_ingestgrpcurl_port: <int>
    ```

## TerminAttr Smashexcludes

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>terminattr_smashexcludes</samp>](## "terminattr_smashexcludes") | String |  | ale,flexCounter,hardware,kni,pulse,strata |  |  |

=== "YAML"

    ```yaml
    terminattr_smashexcludes: <str>
    ```
