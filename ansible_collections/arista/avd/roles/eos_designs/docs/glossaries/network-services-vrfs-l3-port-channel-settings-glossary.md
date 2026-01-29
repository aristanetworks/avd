# Glossary

## Table of Contents

- [A](#a)
- [H](#h)
- [M](#m)
- [N](#n)
- [S](#s)

## A

### authentication

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].ospf.authentication`  
**Valid Values**: `simple`, `message-digest`  
---

## H

### hash_algorithm

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].ospf.message_digest_keys.[].hash_algorithm`  
**Default**: `sha512`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
---

## M

### mode

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].mode`  
**Default**: `active`  
**Valid Values**: `active`, `passive`, `on`  

Port-Channel mode.
Should not be set on Port-Channel subinterfaces.

---

## N

### Network Services

**Type**: List, items: Dictionary  
**Path**: `<network_services_keys.name>`  
---

## S

### speed

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].member_interfaces.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---
