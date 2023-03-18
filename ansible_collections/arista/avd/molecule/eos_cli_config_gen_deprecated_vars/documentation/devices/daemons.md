# daemons
# Table of Contents

- [Monitoring](#monitoring)
  - [Custom daemons](#custom-daemons)

# Monitoring

## Custom daemons

### Custom Daemons Device Configuration

```eos
!
daemon ocprometheus
   exec /usr/bin/ocprometheus -config /usr/bin/ocprometheus.yml -addr localhost:6042
   no shutdown
!
daemon random
   exec /usr/bin/random
   shutdown
```
