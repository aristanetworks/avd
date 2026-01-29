# Glossary

## Table of Contents

- [A](#a)
- [R](#r)

## A

### avd_eos_cli_config_gen_validate_inputs_batch_size

**Type**: Integer  
**Path**: `avd_eos_cli_config_gen_validate_inputs_batch_size`  
**Default**: `10`  

The number of hosts to process in each batch when validating inputs.
Depending on your inventory size and the available resources, you may want to adjust this number.

---

### avd_structured_config_file_format

**Type**: String  
**Path**: `avd_structured_config_file_format`  
**Default**: `yml`  
**Valid Values**: `yml`, `yaml`, `json`  

The file format to use when loading structured configuration files.


---

## R

### read_structured_config_from_file

**Type**: Boolean  
**Path**: `read_structured_config_from_file`  
**Default**: `True`  

Read structured configuration from files in `structured_dir` (default directory also used by the `eos_designs` role).
If set to false, `eos_cli_config_gen` will read structured configuration from hostvars.


---
