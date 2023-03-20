# vmtracer-sessions
# Table of Contents

- [Monitoring](#monitoring)
  - [VM Tracer Sessions](#vm-tracer-sessions)

# Monitoring

## VM Tracer Sessions

### VM Tracer Summary

| Session | URL | Username | Autovlan | Source Interface |
| ------- | --- | -------- | -------- | ---------------- |
| session_1 | https://192.168.0.10 | user1 | disabled | Management1 |
| session_2 | https://192.168.0.10 | user1 | enabled | - |

### VM Tracer Device Configuration

```eos
!
vmtracer session session_1
   url https://192.168.0.10
   username user1
   password 7 encrypted_password
   autovlan disable
   source-interface Management1
!
vmtracer session session_2
   url https://192.168.0.10
   username user1
   password 7 encrypted_password
```
