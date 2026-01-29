# Glossary

## Table of Contents

- [C](#c)
- [R](#r)

## C

### cv_settings

**Type**: Dictionary  
**Path**: `cv_settings`  

Settings for CloudVision telemetry streaming and provisioning.

---

## R

### region

**Type**: String  
**Path**: `cv_settings.cvaas.clusters.[].region`  
**Default**: `auto`  
**Valid Values**: `auto`, `us-central1-a`, `us-central1-b`, `us-central1-c`, `apnortheast-1`, `euwest-2`, `ausoutheast-1`, `na-northeast1-b`, `uk-1`, `india-1`, `staging`, `dev`, `play`  

Optionally set the region to stream to.
The "auto" region will use 'apiserver.arista.io:443' which will redirect to the correct region based on the device's serial number.
"staging", "dev" and "play" are for internal Arista use.

---
