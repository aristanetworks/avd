# Glossary

## Table of Contents

- [S](#s)

## S

### source_interfaces

**Type**: Dictionary  
**Path**: `source_interfaces`  

Configure source-interfaces based on the management interfaces set for other AVD Design data models.
By default, no source-interfaces will be configured. They can still be configured manually using `eos_cli_config_gen` and custom structured configuration.
EOS supports a single source-interface per VRF, so an error will be raised in case of conflicts.
Errors will also be raised if an interface is not found for a device.

---
