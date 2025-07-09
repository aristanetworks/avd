---
# This title is used for search results
title: arista.avd.encrypt
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# encrypt

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.encrypt` when using this plugin.

Encrypt supported EOS passwords

## Synopsis

- The filter encrypts a clear text password into EOS passwords.
- It is intended to be used with Ansible Vault to load a password and have it encrypted on the fly by AVD in `eos_designs`.
- The filter only supports encryption for type `7` and not type `8a` for BGP, ISIS, NTP, OSPF, RADIUS and TACACS+ passwords.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>_input</samp> | string | True | None |  | Clear text password to be encrypted. |
| <samp>passwd_type</samp> | string | True | None | Valid values:<br>- <code>bgp</code><br>- <code>isis</code><br>- <code>ntp</code><br>- <code>ospf_message_digest</code><br>- <code>ospf_simple</code><br>- <code>radius</code><br>- <code>tacacs</code> | Type of password to encrypt.<br>`bgp` and `ospf_simple` requires the `password` and `key` inputs.<br>`isis` requires the `password`, `key` and `mode` inputs.<br>`ospf_message_digest` requires the `password`, `key`, `hash_algorithm`, `key_id` inputs.<br>`ntp`, `radius` and `tacacs` require the `password` and `salt` inputs. |
| <samp>key</samp> | string | optional | None |  | Encryption key. The value depends on the type of password.<br>For BGP passwords, the key is the Neighbor IP or the BGP Peer Group Name in EOS.<br>For OSPF passwords, the key is the interface name (e.g., `Ethernet1`).<br>For ISIS passwords the key is the ISIS instance name (from `router isis &lt;instance name&gt;` or `isis enable &lt;instance name&gt;`). |
| <samp>hash_algorithm</samp> | string | optional | None | Valid values:<br>- <code>md5</code><br>- <code>sha1</code><br>- <code>sha256</code><br>- <code>sha384</code><br>- <code>sha512</code> | Hash algorithm to use with `passwd_type=ospf_message_digest`. |
| <samp>key_id</samp> | integer | optional | None | Min value: <code>1</code><br>Max value: <code>255</code> | Key ID to use with `passwd_type=ospf_message_digest`. |
| <samp>mode</samp> | string | optional | None | Valid values:<br>- <code>none</code><br>- <code>text</code><br>- <code>md5</code><br>- <code>sha</code><br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha1-512</code> | ISIS encryption mode (`none`, `text`, `md5`, `sha`) or shared-secret algorithm (`sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha1-512`). |
| <samp>salt</samp> | integer | optional | None | Max value: <code>15</code> | Salt used for simple type-7 obfuscation. Required when `passwd_type` is `ntp`, `radius` or `tacacs`. |

## Examples

```yaml
---
- # Encrypt the vaulted BGP password for peer group "IPv4-UNDERLAY-PEERS"
  bgp_peer_groups:
    ipv4_underlay_peers:
      name: IPv4-UNDERLAY-PEERS
      password: "{{ bgp_vault_password | arista.avd.encrypt(passwd_type='bgp', key='IPv4-UNDERLAY-PEERS') }}"

- # Encrypt the vaulted OSPF simple password for interface "Ethernet1"
  ethernet_interfaces:
    - name: Ethernet1
      ospf_authentication: simple
      ospf_authentication_key: "{{ ospf_vault_password | arista.avd.encrypt(passwd_type='ospf_simple', key='Ethernet1') }}"

- # Encrypt the vaulted OSPF message digest password for Ethernet1, MD5 and key id 1
  ethernet_interfaces:
    - name: Ethernet1
      ospf_authentication: message-digest
      ospf_message_digest_keys:
        - id: 1
          hash_algorithm: md5
          key: "{{ ospf_vault_password | arista.avd.encrypt(passwd_type='ospf_message_digest', key='Ethernet1', hash_algorithm='md5', key_id='1') }}"

- # Encrypt the vaulted ISIS password for instance EVPN-UNDERLAY using sha-512
  router_isis:
    instance: EVPN_UNDERLAY
    authentication:
      both:
        key_ids:
          - id: 1
            algorithm: sha-512
            key_type: 7
            key: "{{ isis_vault_password | arista.avd.encrypt(passwd_type='isis', key='EVPN_UNDERLAY', mode='sha-512') }}"

- # Encrypt the vaulted NTP password for NTP authentication key
  ntp:
    authentication_keys:
      - id: 1
        hash_algorithm: "md5"
        key: "{{ ntp_vault_key | arista.avd.encrypt(passwd_type='ntp', salt=12) }}"

- # Encrypt the vaulted TACACS+ password
  tacacs_servers:
    hosts:
      - host: 10.10.10.159
        vrf: default
        key: "{{ tacacs_vault_password | arista.avd.encrypt(passwd_type='tacacs', salt = 6) }}"

- # Encrypt the vaulted RADIUS password
  radius_servers:
    hosts:
      - host: 10.10.10.159
        vrf: default
        key: "{{ radius_vault_password | arista.avd.encrypt(passwd_type='radius', salt = 6) }}"
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | string | Encrypted EOS password string. |

## Authors

- Arista Ansible Team (@aristanetworks)
