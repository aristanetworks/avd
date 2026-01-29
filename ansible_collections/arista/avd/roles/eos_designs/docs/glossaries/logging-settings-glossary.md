# Glossary

## Table of Contents

- [A](#a)
- [C](#c)
- [F](#f)
- [H](#h)
- [L](#l)
- [M](#m)
- [P](#p)
- [S](#s)
- [T](#t)

## A

### action

**Type**: String  
**Path**: `logging_settings.policy.match.match_lists.[].action`  
**Valid Values**: `discard`  
---

## C

### console

**Type**: String  
**Path**: `logging_settings.console`  
**Valid Values**: `debugging`, `informational`, `notifications`, `warnings`, `errors`, `critical`, `alerts`, `emergencies`, `disabled`  

Console logging severity level.

---

## F

### facility

**Type**: String  
**Path**: `logging_settings.facility`  
**Valid Values**: `auth`, `cron`, `daemon`, `kern`, `local0`, `local1`, `local2`, `local3`, `local4`, `local5`, `local6`, `local7`, `lpr`, `mail`, `news`, `sys9`, `sys10`, `sys11`, `sys12`, `sys13`, `sys14`, `syslog`, `user`, `uucp`  
---

## H

### hostname

**Type**: String  
**Path**: `logging_settings.format.hostname`  
**Valid Values**: `fqdn`, `ipv4`  

Hostname format in syslogs. For hostname _only_, remove the line. (default EOS CLI behaviour).

---

## L

### level

**Type**: String  
**Path**: `logging_settings.buffered.level`  
**Valid Values**: `alerts`, `critical`, `debugging`, `emergencies`, `errors`, `informational`, `notifications`, `warnings`, `disabled`  

Buffer logging severity level.

---

### level

**Type**: String  
**Path**: `logging_settings.synchronous.level`  
**Default**: `critical`  
**Valid Values**: `alerts`, `all`, `critical`, `debugging`, `emergencies`, `errors`, `informational`, `notifications`, `warnings`, `disabled`  

Synchronous logging severity level.

---

### logging_settings

**Type**: Dictionary  
**Path**: `logging_settings`  

Logging settings

---

## M

### monitor

**Type**: String  
**Path**: `logging_settings.monitor`  
**Valid Values**: `debugging`, `informational`, `notifications`, `warnings`, `errors`, `critical`, `alerts`, `emergencies`, `disabled`  

Monitor logging severity level.

---

## P

### protocol

**Type**: String  
**Path**: `logging_settings.hosts.[].protocol`  
**Default**: `udp`  
**Valid Values**: `tcp`, `udp`, `tls`  
---

## S

### severity

**Type**: String  
**Path**: `logging_settings.level.[].severity`  
**Valid Values**: `alerts`, `critical`, `debugging`, `emergencies`, `errors`, `informational`, `notifications`, `warnings`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`  

Severity of facility. Below are the supported severities.
emergencies    System is unusable                (severity=0)
alerts         Immediate action needed           (severity=1)
critical       Critical conditions               (severity=2)
errors         Error conditions                  (severity=3)
warnings       Warning conditions                (severity=4)
notifications  Normal but significant conditions (severity=5)
informational  Informational messages            (severity=6)
debugging      Debugging messages                (severity=7)
<0-7>          Severity level value

---

## T

### timestamp

**Type**: String  
**Path**: `logging_settings.format.timestamp`  
**Valid Values**: `high-resolution`, `traditional`, `traditional timezone`, `traditional year`, `traditional timezone year`, `traditional year timezone`  

Timestamp format.

---

### trap

**Type**: String  
**Path**: `logging_settings.trap`  
**Valid Values**: `alerts`, `critical`, `debugging`, `emergencies`, `errors`, `informational`, `notifications`, `system`, `warnings`, `disabled`  

Trap logging severity level.

---
