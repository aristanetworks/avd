# Glossary

## Table of Contents

- [A](#a)
- [E](#e)

## A

### avd_digital_twin_mode

**Type**: Boolean  
**Path**: `avd_digital_twin_mode`  
**Default**: `False`  

PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
Enable generation of the Digital Twin version of the fabric (Digital Twin topology, adjusted configuration, etc.).
By default, Digital Twin artifacts (such as the topology file, adjusted structured and EOS configuration, device and fabric documentation) will replace original fabric artifacts.
To keep Digital Twin artifacts separate, adjust the `output_dir_name` and `documentation_dir_name` variables for both `eos_designs` and `eos_cli_config_gen` to point to a dedicated output location.

---

### avd_eos_designs_return_structured_config

**Type**: Boolean  
**Path**: `avd_eos_designs_return_structured_config`  
**Default**: `False`  

Return structured configuration as ansible_facts per device.

---

### avd_eos_designs_structured_config

**Type**: Boolean  
**Path**: `avd_eos_designs_structured_config`  
**Default**: `True`  

Generate structured configuration per device.

---

### avd_eos_designs_validate_inputs_batch_size

**Type**: Integer  
**Path**: `avd_eos_designs_validate_inputs_batch_size`  
**Default**: `10`  

The number of hosts to process in each batch when validating inputs.
Depending on your inventory size and the available resources, you may want to adjust this number.

---

### avd_structured_config_file_format

**Type**: String  
**Path**: `avd_structured_config_file_format`  
**Default**: `yml`  
**Valid Values**: `yml`, `yaml`, `json`  

The file format to use when dumping structured configuration files.


---

## E

### eos_designs_documentation

**Type**: Dictionary  
**Path**: `eos_designs_documentation`  

Control fabric documentation generation.


---
