# Glossary

## Table of Contents

- [M](#m)
- [P](#p)
- [S](#s)
- [T](#t)

## M

### method

**Type**: String  
**Path**: `aaa_settings.accounting.exec.console.methods.[].method`  
**Valid Values**: `logging`, `group`  
---

### method

**Type**: String  
**Path**: `aaa_settings.accounting.exec.default.methods.[].method`  
**Valid Values**: `logging`, `group`  
---

### method

**Type**: String  
**Path**: `aaa_settings.accounting.system.default.methods.[].method`  
**Valid Values**: `logging`, `group`  
---

### method

**Type**: String  
**Path**: `aaa_settings.accounting.commands.console.[].methods.[].method`  
**Valid Values**: `logging`, `group`  
---

### method

**Type**: String  
**Path**: `aaa_settings.accounting.commands.default.[].methods.[].method`  
**Valid Values**: `logging`, `group`  
---

## P

### password_type

**Type**: String  
**Path**: `aaa_settings.enable_password.password_type`  
**Default**: `sha512`  
**Valid Values**: `sha512`  
---

### password_type

**Type**: String  
**Path**: `aaa_settings.local_users.[].password_type`  
**Default**: `sha512`  
**Valid Values**: `sha512`  
---

## S

### shell

**Type**: String  
**Path**: `aaa_settings.local_users.[].shell`  
**Valid Values**: `/bin/bash`, `/bin/sh`, `/sbin/nologin`  

Specify shell for the user.


---

## T

### type

**Type**: String  
**Path**: `aaa_settings.accounting.exec.console.type`  
**Valid Values**: `none`, `start-stop`, `stop-only`  
---

### type

**Type**: String  
**Path**: `aaa_settings.accounting.exec.default.type`  
**Valid Values**: `none`, `start-stop`, `stop-only`  
---

### type

**Type**: String  
**Path**: `aaa_settings.accounting.system.default.type`  
**Valid Values**: `none`, `start-stop`, `stop-only`  
---

### type

**Type**: String  
**Path**: `aaa_settings.accounting.commands.console.[].type`  
**Valid Values**: `none`, `start-stop`, `stop-only`  
---

### type

**Type**: String  
**Path**: `aaa_settings.accounting.commands.default.[].type`  
**Valid Values**: `none`, `start-stop`, `stop-only`  
---
