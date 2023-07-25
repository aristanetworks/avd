# arista.avd.encrypt

Encrypt supported EOS passwords

## Synopsis

The filter is used to encrypt clear text password into EOS passwords\.

To be used in conjunction with Ansible Vault to be able to load a password and have it encrypted on the fly by AVD in <code>eos\_designs</code>\.

Note \- For now this filter only supports encryption from type <code>7</code> and not type <code>8a</code> for OSPF and BGP passwords\.

## Parameters

  _input (True, string, None)
    Clear text password to be encrypted\.

  passwd_type (True, string, None)
    Type of password to encrypt\.
    <code>bgp</code> and <code>ospf\_simple</code> requires the <em>password</em> and <em>key</em> inputs\.
    <code>ospf\_message\_digest</code> requires the <em>password</em>\, <em>key</em>\, <em>hash\_algorithm</em>\, <em>key\_id</em> inputs\.

  key (True, string, None)
    Encryption key\. The value depends on the type of password\.
    For BGP passwords the key is the Neighbor IP or the BGP Peer Group Name in EOS\.
    For OSPF passwords the key is the interface name \(e\.g\.\, <code>Ethernet1</code>\)\.

  hash_algorithm (optional, string, None)
    Hash algorithm to use with <em>passwd\_type\=\"ospf\_message\_digest\"</em>\.

  key_id (optional, integer, None)
    Key ID to use with <em>passwd\_type\=\"ospf\_message\_digest\"</em>\.

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

  _value (, string, )
    Encrypted EOS password string\.

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
