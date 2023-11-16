---
# This title is used for search results
title: arista.avd.encrypt
---
<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# encrypt

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.encrypt` when using this plugin.

Encrypt supported EOS passwords

## Synopsis

The filter encrypts a clear text password into EOS passwords.

To be used with Ansible Vault to load a password and have it encrypted on the fly by AVD in <code>eos\_designs</code>.

Note \- For now this filter only supports encryption from type <code>7</code> and not type <code>8a</code> for OSPF and BGP passwords.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| _input | string | True | None |  | Clear text password to be encrypted. |
| passwd_type | string | True | None | Valid values:<br>- <code>bgp</code><br>- <code>ospf_simple</code><br>- <code>ospf_message_digest</code> | Type of password to encrypt.<br><code>bgp</code> and <code>ospf\_simple</code> requires the <em>password</em> and <em>key</em> inputs.<br><code>ospf\_message\_digest</code> requires the <em>password</em>, <em>key</em>, <em>hash\_algorithm</em>, <em>key\_id</em> inputs. |
| key | string | True | None |  | Encryption key. The value depends on the type of password.<br>For BGP passwords, the key is the Neighbor IP or the BGP Peer Group Name in EOS.<br>For OSPF passwords, the key is the interface name \(e.g., <code>Ethernet1</code>\). |
| hash_algorithm | string | optional | None | Valid values:<br>- <code>md5</code><br>- <code>sha1</code><br>- <code>sha256</code><br>- <code>sha384</code><br>- <code>sha512</code> | Hash algorithm to use with <em>passwd\_type\=\"ospf\_message\_digest\"</em>. |
| key_id | integer | optional | None | Min value: <code>1</code><br>Max value: <code>255</code> | Key ID to use with <em>passwd\_type\=\"ospf\_message\_digest\"</em>. |

## Examples

```yaml
---
# Encrypt the vaulted BGP password for peer group "IPv4-UNDERLAY-PEERS"
bgp_peer_groups:
  ipv4_underlay_peers:
    name: IPv4-UNDERLAY-PEERS
    password: "{{ bgp_vault_password | arista.avd.encrypt(passwd_type='bgp', key='IPv4-UNDERLAY-PEERS') }}"

# Encrypt the vaulted OSPF simple password for interface "Ethernet1"
ethernet_interfaces:
  - name: Ethernet1
    ospf_authentication: simple
    ospf_authentication_key: "{{ ospf_vault_password | arista.avd.encrypt(passwd_type='ospf_simple', key='Ethernet1') }}"

# Encrypt the vaulted OSPF message digest password for Ethernet1, MD5 and key id 1
ethernet_interfaces:
  - name: Ethernet1
    ospf_authentication: message-digest
    ospf_message_digest_keys:
      - id: 1
        hash_algorithm: md5
        key: "{{ ospf_vault_password | arista.avd.encrypt(passwd_type='ospf_message_digest', key='Ethernet1', hash_algorithm='md5', key_id='1') }}"
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | string | Encrypted EOS password string. |

## Authors

- Arista Ansible Team (@aristanetworks)
