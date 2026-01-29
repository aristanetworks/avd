# Glossary

## Table of Contents

- [I](#i)

## I

### is_deployed

**Type**: Boolean  
**Path**: `is_deployed`  
**Default**: `True`  

If the device is already deployed in the fabric.
When set to false:
  - The `cv_deploy` role will not apply configurations to this device.
  - Peer interfaces toward this device may be shutdown based on the `shutdown_interfaces_towards_undeployed_peers` setting.
  - BGP peerings toward this device may be shutdown based on the `shutdown_bgp_towards_undeployed_peers` setting.
  - Validation tests by the `anta_runner` role are automatically skipped for this device.

---
