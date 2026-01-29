# Glossary

## Table of Contents

- [A](#a)

## A

### avd_data_validation_mode

**Type**: String  
**Path**: `avd_data_validation_mode`  
**Default**: `error`  
**Valid Values**: `error`, `warning`  

Validation Mode for AVD input data validation.
Input data validation will validate the input variables according to the schema.
During validation, messages will be generated with information about the host(s) and key(s) which failed validation.
"error" will produce error messages and fail the task.
"warning" will produce warning messages.


---
