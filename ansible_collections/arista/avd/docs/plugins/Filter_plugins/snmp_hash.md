# arista.avd.snmp_hash

Compute localized SNMP passphrases

## Synopsis

Key localization as described in [RFC 2574 section 2\.6](https://www.rfc-editor.org/rfc/rfc2574.html#section-2.6)

## Parameters

| Argument | Type | Required | Default | Description |
| -------- | ---- | -------- | ------- | ----------- |
| _input | dictionary | True | None | Dictionary with snmp passphrase details\. |
|   passphrase | string | True | None | The passphrase to localize\, if <em>priv</em> is not set it is the \"auth\" passphrase else it is the \"priv\" passphrase\. |
|   auth | string | True | None | Auth type |
|   engine_id | string | True | None | A hexadecimal string containing the engine\_id to be used to localize the passphrase |
|   priv | string | optional | None | Priv type |

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | string | The localized key generated from the passphrase using <em>auth</em> type\.<br>If required the key is truncated to match the appropriate keylength for the <em>priv</em> type\. |

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
