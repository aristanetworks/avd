# Glossary

## Table of Contents

- [A](#a)
- [S](#s)

## A

### application_classification

**Type**: Dictionary  
**Path**: `application_classification`  

Application traffic recognition configuration.

---

## S

### service

**Type**: String  
**Path**: `application_classification.categories.[].applications.[].service`  
**Valid Values**: `audio-video`, `chat`, `default`, `file-transfer`, `networking-protocols`, `peer-to-peer`, `software-update`  

Service Name.
Specific service to target for this application.
If no service is specified, all supported services of the application are matched.
Not all valid values are valid for all applications, check on EOS CLI.

---

### service

**Type**: String  
**Path**: `application_classification.application_profiles.[].applications.[].service`  
**Valid Values**: `audio-video`, `chat`, `default`, `file-transfer`, `networking-protocols`, `peer-to-peer`, `software-update`  

Service Name.
Specific service to target for this application.
If no service is specified, all supported services of the application are matched.
Not all valid values are valid for all applications, check on EOS CLI.

---

### service

**Type**: String  
**Path**: `application_classification.application_profiles.[].categories.[].service`  
**Valid Values**: `audio-video`, `chat`, `default`, `file-transfer`, `networking-protocols`, `peer-to-peer`, `software-update`  

Service Name.
Specific service to target for this application.
If no service is specified, all supported services of the application are matched.
Not all valid values are valid for all applications, check on EOS CLI.

---
