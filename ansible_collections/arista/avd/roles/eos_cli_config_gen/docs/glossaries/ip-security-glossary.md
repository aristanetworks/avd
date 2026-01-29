# Glossary

## Table of Contents

- [A](#a)
- [C](#c)
- [D](#d)
- [E](#e)
- [I](#i)
- [M](#m)
- [P](#p)
- [U](#u)

## A

### action

**Type**: String  
**Path**: `ip_security.profiles.[].dpd.action`  
**Valid Values**: `clear`, `hold`, `restart`  

Action to apply.

* 'clear': Delete all connections
* 'hold': Re-negotiate connection on demand
* 'restart': Restart connection immediately


---

## C

### connection

**Type**: String  
**Path**: `ip_security.profiles.[].connection`  
**Valid Values**: `add`, `start`, `route`  

IPsec connection (Initiator/Responder/Dynamic).

---

## D

### dh_group

**Type**: Integer  
**Path**: `ip_security.ike_policies.[].dh_group`  
**Valid Values**: `1`, `2`, `5`, `14`, `15`, `16`, `17`, `19`, `20`, `21`, `24`  

Diffie-Hellman group for the key exchange.

---

## E

### encryption

**Type**: String  
**Path**: `ip_security.ike_policies.[].encryption`  
**Valid Values**: `3des`, `aes128`, `aes256`  

IKE encryption algorithm.

---

### encryption

**Type**: String  
**Path**: `ip_security.sa_policies.[].esp.encryption`  
**Valid Values**: `disabled`, `aes128`, `aes128gcm128`, `aes128gcm64`, `aes256`, `aes256gcm128`, `3des`  
---

## I

### integrity

**Type**: String  
**Path**: `ip_security.ike_policies.[].integrity`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  

Integrity algorithm.

---

### integrity

**Type**: String  
**Path**: `ip_security.sa_policies.[].esp.integrity`  
**Valid Values**: `disabled`, `sha1`, `sha256`, `sha384`, `sha512`, `md5`  
---

## M

### mode

**Type**: String  
**Path**: `ip_security.profiles.[].mode`  
**Valid Values**: `transport`, `tunnel`  

Ipsec mode type.

---

## P

### pfs_dh_group

**Type**: Integer  
**Path**: `ip_security.sa_policies.[].pfs_dh_group`  
**Valid Values**: `1`, `2`, `5`, `14`, `15`, `16`, `17`, `19`, `20`, `21`, `24`  
---

## U

### unit

**Type**: String  
**Path**: `ip_security.sa_policies.[].sa_lifetime.unit`  
**Default**: `hours`  
**Valid Values**: `gigabytes`, `hours`, `megabytes`, `thousand-packets`  
---
