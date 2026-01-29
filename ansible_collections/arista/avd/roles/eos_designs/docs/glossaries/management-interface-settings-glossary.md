# Glossary

## Table of Contents

- [D](#d)
- [I](#i)
- [M](#m)

## D

### default_mgmt_method

**Type**: String  
**Path**: `default_mgmt_method`  
**Default**: `oob`  
**Valid Values**: `oob`, `inband`, `none`  

`default_mgmt_method` controls the default VRF and source interface used for the following management and monitoring protocols configured with AVD Design:
  - `aaa_settings`
  - `cv_settings`
  - `logging_settings`
  - `management_eapi`
  - `ntp_settings`
  - `sflow_settings`
  - `snmp_settings`
  - `ssh_settings`

`oob` means the protocols will be configured with the VRF set by `mgmt_interface_vrf` and `mgmt_interface` as the source interface.
`inband` means the protocols will be configured with the VRF set by `inband_mgmt_vrf` and `inband_mgmt_interface` as the source interface.
`none` means the VRF and or interface must be manually set for each protocol.
This can be overridden under the settings for each protocol.


---

## I

### ipv6_mgmt_destination_networks

**Type**: List, items: String  
**Path**: `ipv6_mgmt_destination_networks`  

List of IPv6 prefixes to configure as static routes towards the OOB IPv6 Management interface gateway.
Replaces the default route.


---

### ipv6_mgmt_gateway

**Type**: String  
**Path**: `ipv6_mgmt_gateway`  

OOB Management interface gateway in IPv6 format.
Used as next-hop for default gateway or static routes defined under 'ipv6_mgmt_destination_networks'.


---

## M

### mgmt_destination_networks

**Type**: List, items: String  
**Path**: `mgmt_destination_networks`  

List of IPv4 prefixes to configure as static routes towards the OOB Management interface gateway.
Replaces the default route.

---

### mgmt_gateway

**Type**: String  
**Path**: `mgmt_gateway`  

OOB Management interface gateway in IPv4 format.
Used as next-hop for default gateway or static routes defined under 'mgmt_destination_networks'.


---

### mgmt_interface

**Type**: String  
**Path**: `mgmt_interface`  
**Default**: `Management1`  

OOB Management interface.

---

### mgmt_interface_description

**Type**: String  
**Path**: `mgmt_interface_description`  
**Default**: `OOB_MANAGEMENT`  

Management interface description.


---

### mgmt_interface_vrf

**Type**: String  
**Path**: `mgmt_interface_vrf`  
**Default**: `MGMT`  

OOB Management VRF.

---

### mgmt_vrf_routing

**Type**: Boolean  
**Path**: `mgmt_vrf_routing`  
**Default**: `False`  

Configure IP routing for the OOB Management VRF.

---
