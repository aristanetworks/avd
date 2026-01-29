# Glossary

## Table of Contents

- [A](#a)

## A

### action

**Type**: String  
**Path**: `router_segment_security.policies.[].sequence_numbers.[].action`  
**Valid Values**: `forward`, `drop`, `redirect`  

The action to take - note that platform support for the redirect action is limited. The "redirect" action also requires the 'next_hop' to be configured.

---

### address_family

**Type**: String  
**Path**: `router_segment_security.vrfs.[].segments.[].definition.match_lists.[].address_family`  
**Valid Values**: `ipv4`, `ipv6`  

Indicate which address-family the match list belongs to e.g. ipv4 or ipv6.

---
