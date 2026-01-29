# Glossary

## Table of Contents

- [A](#a)
- [S](#s)

## A

### application_traffic_recognition

**Type**: Dictionary  
**Path**: `application_traffic_recognition`  

Application traffic recognition configuration.

---

## S

### service

**Type**: String  
**Path**: `application_traffic_recognition.categories.[].applications.[].service`  
**Valid Values**: `audio-video`, `chat`, `default`, `file-transfer`, `networking-protocols`, `peer-to-peer`, `software-update`  

Service Name.
Specific service to target for this application.
If no service is specified, all supported services of the application are matched.
Not all valid values are valid for all applications, check on EOS CLI.

---

### service

**Type**: String  
**Path**: `application_traffic_recognition.application_profiles.[].applications.[].service`  
**Valid Values**: `audio-video`, `chat`, `default`, `file-transfer`, `networking-protocols`, `peer-to-peer`, `software-update`  

Service Name.
Specific service to target for this application.
If no service is specified, all supported services of the application are matched.
Not all valid values are valid for all applications, check on EOS CLI.

---

### service

**Type**: String  
**Path**: `application_traffic_recognition.application_profiles.[].categories.[].service`  
**Valid Values**: `audio-video`, `chat`, `default`, `file-transfer`, `networking-protocols`, `peer-to-peer`, `software-update`  

Service Name.
Specific service to target for this application.
If no service is specified, all supported services of the application are matched.
Not all valid values are valid for all applications, check on EOS CLI.

---
