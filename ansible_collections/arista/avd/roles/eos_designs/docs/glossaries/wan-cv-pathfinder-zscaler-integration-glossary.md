# Glossary

## Table of Contents

- [C](#c)

## C

### cv_server

**Type**: String  
**Path**: `cv_server`  

PREVIEW: These keys are in preview mode.

Hostname or IP address of CloudVision host. Ex. "www.arista.io" for CVaaS.
For AVD Design data models this variable is only used for the WAN Internet-exit integration with Zscaler.
The same variable name is also used by the `cv_deploy` role, and will override the value of `ansible_host` on inventory 'cloudvision' host.
Make sure to set it in a common group_vars file.

---

### cv_token

**Type**: String  
**Path**: `cv_token`  

PREVIEW: These keys are in preview mode.

Service account token as defined on CloudVision. This value should be using Ansible Vault.
For AVD Design data models this variable is only used for the WAN Internet-exit integration with Zscaler.
The same variable name is also used by the `cv_deploy` role, and will override the value of `ansible_password` on inventory 'cloudvision' host.
Make sure to set it in a common group_vars file.

---
