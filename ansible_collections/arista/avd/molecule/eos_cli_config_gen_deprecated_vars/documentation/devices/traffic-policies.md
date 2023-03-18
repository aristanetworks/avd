# traffic-policies
# Table of Contents

- [Traffic Policies information](#traffic-policies-information)

## Traffic Policies information

**IPv4 Field sets**

| Field Set Name | Values |
| -------------- | ------ |
| DEMO-01 | 10.0.0.0/8<br/>192.168.0.0/16 |
| DEMO-02 | 172.16.0.0/12<br/>224.0.0.0/8 |

**IPv6 Field sets**

| Field Set Name | Values |
| -------------- | ------ |
| DEMO-03 | aaaa::/64<br/>bbbb::/64 |

**L4 Port Field sets**

| Field Set Name | Values |
| -------------- | ------ |
| SERVICE-DEMO | 10,20,80,440-450|

### Traffic Policies

**BLUE-C1-POLICY:**

| Match set | Type | Sources | Destinations | Protocol | Source Port(s) | Destination port(s) | Action |
| --------- | ---- | ------- | ------------ | -------- | -------------- | ------------------- | ------ |
| BLUE-C1-POLICY-02 | ipv4 | DEMO-01<br/>DEMO-02 | ANY | tcp<br/>icmp | ANY | SERVICE-DEMO | action: PASS<br/>counter: DEMO-TRAFFIC<br/>dscp marking: 60 |

### Traffic Policies Device Configuration

```eos
!
traffic-policies
   field-set ipv4 prefix DEMO-01
      10.0.0.0/8 192.168.0.0/16
   !
   field-set ipv4 prefix DEMO-02
      172.16.0.0/12 224.0.0.0/8
   !
   field-set ipv6 prefix DEMO-03
      aaaa::/64 bbbb::/64
   !
   field-set l4-port SERVICE-DEMO
      10,20,80,440-450
   !
   traffic-policy BLUE-C1-POLICY
      counter DEMO-TRAFFIC
      match BLUE-C1-POLICY-02 ipv4
         source prefix field-set DEMO-01 DEMO-02
         protocol tcp flags established destination port field-set SERVICE-DEMO
         protocol icmp
         actions
            count DEMO-TRAFFIC
            set dscp 60
         !
      !
   !
```
