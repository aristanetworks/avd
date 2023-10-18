# event-handlers

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [Event Handler](#event-handler)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.255.122/24
```

## Monitoring

### Event Handler

#### Event Handler Summary

| Handler | Action Type | Action | Trigger |
| ------- | ----------- | ------ | ------- |
| CONFIG_VERSIONING | bash | <code>FN=/mnt/flash/startup-config; LFN="`ls -1 $FN.*-* \| tail -n 1`"; if [ -z "$LFN" -o -n "`diff -I 'last modified' $FN $LFN`" ]; then cp $FN $FN.`date +%Y%m%d-%H%M%S`; ls -1r $FN.*-* \| tail -n +11 \| xargs -I % rm %; fi</code> | on-startup-config |
| evpn-blacklist-recovery | bash | <code>FastCli -p 15 -c "clear bgp evpn host-flap"</code> | on-logging |
| trigger-on-boot | bash | <code>echo "on-boot"</code> | on-boot |
| trigger-on-config | bash | <code>echo "on-config"</code> | on-config |
| trigger-on-counters | bash | <code>echo "on-counters"</code> | on-counters |
| trigger-on-intf | bash | <code>echo "on-intf"</code> | on-intf |
| trigger-on-maintenance | bash | <code>echo "on-maintenance"</code> | on-maintenance |
| trigger-vm-tracer | bash | <code>echo "vm-tracer"</code> | vm-tracer |

#### Event Handler Device Configuration

```eos
!
event-handler CONFIG_VERSIONING
   trigger on-startup-config
   action bash FN=/mnt/flash/startup-config; LFN="`ls -1 $FN.*-* | tail -n 1`"; if [ -z "$LFN" -o -n "`diff -I 'last modified' $FN $LFN`" ]; then cp $FN $FN.`date +%Y%m%d-%H%M%S`; ls -1r $FN.*-* | tail -n +11 | xargs -I % rm %; fi
   delay 0
!
event-handler evpn-blacklist-recovery
   trigger on-logging
      regex EVPN-3-BLACKLISTED_DUPLICATE_MAC
   action bash FastCli -p 15 -c "clear bgp evpn host-flap"
   delay 300
   asynchronous
!
event-handler trigger-on-boot
   trigger on-boot
   action bash echo "on-boot"
!
event-handler trigger-on-config
   trigger on-config
   action bash echo "on-config"
!
event-handler trigger-on-counters
   trigger on-counters
   action bash echo "on-counters"
!
event-handler trigger-on-intf
   trigger on-intf
   action bash echo "on-intf"
!
event-handler trigger-on-maintenance
   trigger on-maintenance
   action bash echo "on-maintenance"
!
event-handler trigger-vm-tracer
   trigger vm-tracer
   action bash echo "vm-tracer"
```
