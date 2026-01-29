# Glossary

## Table of Contents

- [A](#a)
- [D](#d)
- [I](#i)
- [P](#p)
- [S](#s)
- [T](#t)

## A

### action

**Type**: String  
**Path**: `ipv4_acls.[].entries.[].action`  
**Valid Values**: `permit`, `deny`  

ACL action.
Required except for remarks.

---

## D

### destination_ports_match

**Type**: String  
**Path**: `ipv4_acls.[].entries.[].destination_ports_match`  
**Default**: `eq`  
**Valid Values**: `eq`, `gt`, `lt`, `neq`, `range`  
---

## I

### ipv4_acls

**Type**: List, items: Dictionary  
**Path**: `ipv4_acls`  

IPv4 extended access-lists supporting substitution on certain fields.
These access-lists can be referenced under node settings `l3_interfaces`, and will only be configured on devices where they are in use.

The substitution is useful when assigning the same access-list on multiple interfaces,
but where certain fields require unique values like the "interface_ip" or "peer_ip".
When using substitution, the interface name will be appended to the ACL name.

---

## P

### permit_response_traffic

**Type**: String  
**Path**: `ipv4_acls.[].permit_response_traffic`  
**Valid Values**: `nat`  

Permit response traffic automatically based on NAT translations.
Minimum EOS version requirement 4.32.2F.

---

## S

### source_ports_match

**Type**: String  
**Path**: `ipv4_acls.[].entries.[].source_ports_match`  
**Default**: `eq`  
**Valid Values**: `eq`, `gt`, `lt`, `neq`, `range`  
---

## T

### ttl_match

**Type**: String  
**Path**: `ipv4_acls.[].entries.[].ttl_match`  
**Default**: `eq`  
**Valid Values**: `eq`, `gt`, `lt`, `neq`  
---
