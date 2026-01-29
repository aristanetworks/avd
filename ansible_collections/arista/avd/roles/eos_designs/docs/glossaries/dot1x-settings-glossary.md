# Glossary

## Table of Contents

- [D](#d)
- [L](#l)
- [M](#m)

## D

### delimiter

**Type**: String  
**Path**: `dot1x_settings.mac_based_authentication.username_format.delimiter`  
**Valid Values**: `colon`, `hyphen`, `none`, `period`  

RADIUS User-Name attribute delimiter to use on the MAC address.

---

### dot1x_settings

**Type**: Dictionary  
**Path**: `dot1x_settings`  

Settings for 802.1X deployments.

---

## L

### letter_case

**Type**: String  
**Path**: `dot1x_settings.mac_based_authentication.username_format.letter_case`  
**Valid Values**: `lowercase`, `uppercase`  

RADIUS User-Name attribute letter case to use on the MAC address.

---

## M

### mode

**Type**: String  
**Path**: `dot1x_settings.accounting.mode`  
**Default**: `start-stop`  
**Valid Values**: `start-stop`, `stop-only`  

Determines whether to send accounting records when a session is established and
when it ends (`start-stop`), or only when the session ends (`stop-only`).

---
