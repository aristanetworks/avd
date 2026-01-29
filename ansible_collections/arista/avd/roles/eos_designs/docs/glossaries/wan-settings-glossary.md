# Glossary

## Table of Contents

- [I](#i)
- [W](#w)

## I

### ipsec_settings

**Type**: Dictionary  
**Path**: `ipsec_settings`  

Settings applicable to all IPsec connections.

---

## W

### wan_encapsulation

**Type**: String  
**Path**: `wan_encapsulation`  
**Default**: `path-selection`  
**Valid Values**: `path-selection`, `vxlan`  

Select the encapsulation to use for EVPN peerings for WAN BGP peers.

---

### wan_ipsec_profiles

**Type**: Dictionary  
**Path**: `wan_ipsec_profiles`  

Define IPsec profiles parameters for WAN configuration.

---

### wan_mode

**Type**: String  
**Path**: `wan_mode`  
**Default**: `cv-pathfinder`  
**Valid Values**: `cv-pathfinder`, `legacy-autovpn`  

Select if the WAN should be run using CV Pathfinder or AutoVPN only.

---

### wan_stun_dtls_disable

**Type**: Boolean  
**Path**: `wan_stun_dtls_disable`  
**Default**: `False`  

WAN STUN connections are authenticated and secured with DTLS by default.
For CV Pathfinder deployments CloudVision will automatically deploy certificates on the devices.
In case of AutoVPN the certificates must be deployed manually to all devices.

For LAB environments this can be disabled, if there are no certificates available.
This should NOT be disabled for a WAN network connected to the internet, since it will leave the STUN service exposed with no authentication.

---

### wan_stun_dtls_profile_name

**Type**: String  
**Path**: `wan_stun_dtls_profile_name`  
**Default**: `STUN-DTLS`  

Name of the SSL profile used for DTLS on WAN STUN connections.
When using automatic ceritficate deployment via CloudVision this name must be the same on all WAN routers.

---

### wan_use_agent_env_var_for_kernel_software_forwarding_ecmp

**Type**: Boolean  
**Path**: `wan_use_agent_env_var_for_kernel_software_forwarding_ecmp`  
**Default**: `False`  

For EOS kernel forwarding, ECMP programming can be enabled in two different ways depending on the EOS version.

- `true`: For older EOS versions use an agent environment variable. Changing this requires a restart of the KernelFib agent.
- `false`: For newer EOS versions (starting 4.33.2) use the proper CLI.

---
