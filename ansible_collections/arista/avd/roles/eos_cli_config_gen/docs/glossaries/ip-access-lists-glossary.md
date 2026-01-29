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
**Path**: `ip_access_lists.[].entries.[].action`  
**Valid Values**: `permit`, `deny`  

ACL action.
Required except for remarks.

---

## D

### destination_ports_match

**Type**: String  
**Path**: `ip_access_lists.[].entries.[].destination_ports_match`  
**Default**: `eq`  
**Valid Values**: `eq`, `gt`, `lt`, `neq`, `range`  
---

## I

### IP Extended Access-Lists (improved model)

**Type**: List, items: Dictionary  
**Path**: `ip_access_lists`  
---

## P

### permit_response_traffic

**Type**: String  
**Path**: `ip_access_lists.[].permit_response_traffic`  
**Valid Values**: `nat`  

Permit response traffic automatically based on NAT translations.
Minimum EOS version requirement 4.32.2F.

---

## S

### source_ports_match

**Type**: String  
**Path**: `ip_access_lists.[].entries.[].source_ports_match`  
**Default**: `eq`  
**Valid Values**: `eq`, `gt`, `lt`, `neq`, `range`  
---

## T

### ttl_match

**Type**: String  
**Path**: `ip_access_lists.[].entries.[].ttl_match`  
**Default**: `eq`  
**Valid Values**: `eq`, `gt`, `lt`, `neq`  
---
