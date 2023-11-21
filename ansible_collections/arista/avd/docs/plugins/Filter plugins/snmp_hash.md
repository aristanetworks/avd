---
# This title is used for search results
title: arista.avd.snmp_hash
---
<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# snmp_hash

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.snmp_hash` when using this plugin.

Compute localized SNMP passphrases

## Synopsis

Key localization as described in [RFC 2574 section 2.6](https://www.rfc-editor.org/rfc/rfc2574.html#section-2.6)

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| _input | dictionary | True | None |  | Dictionary with SNMP passphrase details. |
|     passphrase | string | True | None |  | The passphrase to localize.<br>This is the \"auth\" passphrase when the <em>priv</em> argument is not set.<br>If <em>priv</em> is set, it is the \"priv\" passphrase. |
|     auth | string | True | None | Valid values:<br>- <code>md5</code><br>- <code>sha</code><br>- <code>sha224</code><br>- <code>sha256</code><br>- <code>sha384</code><br>- <code>sha512</code> | Auth type |
|     engine_id | string | True | None |  | A hexadecimal string containing the engine\_id to be used to localize the passphrase |
|     priv | string | optional | None | Valid values:<br>- <code>des</code><br>- <code>aes</code><br>- <code>aes192</code><br>- <code>aes256</code> | Priv type |

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | string | The localized key generated from the passphrase using <em>auth</em> type.<br>If required the key is truncated to match the appropriate keylength for the <em>priv</em> type. |

## Authors

- Arista Ansible Team (@aristanetworks)
