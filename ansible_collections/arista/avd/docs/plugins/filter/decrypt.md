# arista.avd.decrypt

Decrypt supported EOS passwords

## Synopsis

The filter is used to decrypt supported EOS passwords into clear text\.

Note \- For now this filter only supports decryption from type <code>7</code> and not type <code>8a</code> for OSPF and BGP passwords\.

## Parameters

  _input (True, string, None)
    Encrypted EOS password\.

  passwd_type (True, string, None)
    Type of password to decrypt\.
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
# Decrypt BGP password for peer group "IPv4-UNDERLAY-PEERS"
cleartext: "{{ encrypted_password | arista.avd.decrypt(passwd_type='bgp', key='IPv4-UNDERLAY-PEERS') }}"

# Decrypt OSPF simple password for interface "Ethernet1"
cleartext: "{{ encrypted_password | arista.avd.decrypt(passwd_type='ospf_simple', key='Ethernet1') }}"

# Decrypt OSPF message digest password for Ethernet1, MD5 and key id 1
cleartext: "{{ encrypted_password | arista.avd.decrypt(passwd_type='ospf_message_digest', key='Ethernet1', hash_algorithm='md5', key_id='1') }}"
```

## Return Values

  _value (, string, )
    Decrypted cleartext password\.

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
