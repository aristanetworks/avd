---
# This title is used for search results
title: arista.avd.decrypt
---
<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# decrypt

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.decrypt` when using this plugin.

Decrypt supported EOS passwords.

## Synopsis

The filter is used to decrypt supported EOS passwords into clear text.

Note \- For now this filter only supports decryption from type <code>7</code> and not type <code>8a</code> for OSPF and BGP passwords.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| _input | string | True | None |  | Encrypted EOS password. |
| passwd_type | string | True | None | Valid values:<br>- <code>bgp</code><br>- <code>ospf_simple</code><br>- <code>ospf_message_digest</code> | Type of password to decrypt.<br><code>bgp</code> and <code>ospf\_simple</code> requires the <em>password</em> and <em>key</em> inputs.<br><code>ospf\_message\_digest</code> requires the <em>password</em>, <em>key</em>, <em>hash\_algorithm</em>, <em>key\_id</em> inputs. |
| key | string | True | None |  | Encryption key. The value depends on the type of password.<br>For BGP passwords the key is the Neighbor IP or the BGP Peer Group Name in EOS.<br>For OSPF passwords the key is the interface name \(e.g., <code>Ethernet1</code>\). |
| hash_algorithm | string | optional | None | Valid values:<br>- <code>md5</code><br>- <code>sha1</code><br>- <code>sha256</code><br>- <code>sha384</code><br>- <code>sha512</code> | Hash algorithm to use with <em>passwd\_type\=\"ospf\_message\_digest\"</em>. |
| key_id | integer | optional | None | Min value: <code>1</code><br>Max value: <code>255</code> | Key ID to use with <em>passwd\_type\=\"ospf\_message\_digest\"</em>. |

## Examples

```yaml
---
# Decrypt BGP password for peer group "IPv4-UNDERLAY-PEERS"
cleartext: "{{ encrypted_password | arista.avd.decrypt(passwd_type='bgp', key='IPv4-UNDERLAY-PEERS') }}"

# Decrypt OSPF simple password for interface "Ethernet1"
cleartext: "{{ encrypted_password | arista.avd.decrypt(passwd_type='ospf_simple', key='Ethernet1') }}"

# Decrypt OSPF message digest password for Ethernet1, MD5 and key id 1
cleartext: "{{ encrypted_password | arista.avd.decrypt(passwd_type='ospf_message_digest', key='Ethernet1', hash_algorithm='md5', key_id='1') }}"
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | string | Decrypted cleartext password. |

## Authors

- Arista Ansible Team (@aristanetworks)
