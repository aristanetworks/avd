# Glossary

## Table of Contents

- [I](#i)

## I

### ipv4_prefix_list_catalog

**Type**: List, items: Dictionary  
**Path**: `ipv4_prefix_list_catalog`  

IPv4 prefix-list catalog.
Note: Entries defined in `ipv4_prefix_list_catalog` are only rendered in the configuration when
they are explicitly referenced in one of the following node config keys:
- `l3_interfaces.[].bgp.ipv4_prefix_list_in`
- `l3_interfaces.[].bgp.ipv4_prefix_list_out`
- `l3_port_channels.[].bgp.ipv4_prefix_list_in`
- `l3_port_channels.[].bgp.ipv4_prefix_list_out`.

---
