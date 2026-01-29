# Glossary

## Table of Contents

- [D](#d)
- [M](#m)

## D

### daemon_terminattr

**Type**: Dictionary  
**Path**: `daemon_terminattr`  

You can either provide a list of IPs/FQDNs to target on-premise Cloudvision cluster or use DNS name for your Cloudvision as a Service instance.
Streaming to multiple clusters both on-prem and cloud service is supported.

!!! note
    For TerminAttr version recommendation and EOS compatibility matrix, please refer to the latest TerminAttr Release Notes
    which always contain the latest recommended versions and minimum required versions per EOS release.


---

## M

### method

**Type**: String  
**Path**: `daemon_terminattr.clusters.[].cvauth.method`  
**Valid Values**: `token`, `token-secure`, `key`, `certs`  
---

### method

**Type**: String  
**Path**: `daemon_terminattr.cvauth.method`  
**Valid Values**: `token`, `token-secure`, `key`, `certs`  
---
