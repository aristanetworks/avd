# daemon-terminattr
# Table of Contents

- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)

# Monitoring

## TerminAttr Daemon

### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | 10.20.20.1:9910 | mgt | key,arista | - | - | False |
| gzip | 10.30.30.1:9910 | mgt | token,/tmp/tokenDC2 | - | - | False |

### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvopt DC1.addr=10.20.20.1:9910 -cvopt DC1.auth=key,arista -cvopt DC1.vrf=mgt -cvopt DC2.addr=10.30.30.1:9910 -cvopt DC2.auth=token,/tmp/tokenDC2 -cvopt DC2.vrf=mgt -taillogs
   no shutdown
```
