# Glossary

## Table of Contents

- [D](#d)
- [M](#m)
- [P](#p)
- [T](#t)
- [U](#u)

## D

### default

**Type**: String  
**Path**: `platform.sand.multicast_replication.default`  
**Valid Values**: `ingress`, `egress`  
---

## M

### mdb_profile

**Type**: String  
**Path**: `platform.sand.mdb_profile`  
**Valid Values**: `balanced`, `balanced-xl`, `l3`, `l3-xl`, `l3-xxl`, `l3-xxxl`  

Sand platforms MDB Profile configuration. Note: l3-xxxl does not support MLAG.

---

### mode

**Type**: String  
**Path**: `platform.sfe.interface.profiles.[].interfaces.[].rx_queue.mode`  
**Valid Values**: `shared`, `exclusive`  

Mode applicable to the workers. Default mode is 'shared'.

---

## P

### platform

**Type**: Dictionary  
**Path**: `platform`  

Every key below this point is platform dependent.

---

### precedence

**Type**: Integer  
**Path**: `platform.trident.mmu.queue_profiles.[].multicast_queues.[].drop.precedence`  
**Valid Values**: `1`, `2`  
---

### precedence

**Type**: Integer  
**Path**: `platform.trident.mmu.queue_profiles.[].unicast_queues.[].drop.precedence`  
**Valid Values**: `1`, `2`  
---

### profile

**Type**: String  
**Path**: `platform.fap.buffering_egress.profile`  
**Valid Values**: `unicast`, `balanced`  

Preferred traffic profile for egress fap buffering.

---

## T

### threshold

**Type**: String  
**Path**: `platform.trident.mmu.queue_profiles.[].ingress.priority_groups.[].threshold`  
**Valid Values**: `1`, `1/128`, `1/16`, `1/2`, `1/32`, `1/4`, `1/64`, `1/8`, `2`, `4`, `8`  
---

### threshold

**Type**: String  
**Path**: `platform.trident.mmu.queue_profiles.[].ingress.threshold`  
**Valid Values**: `1`, `1/128`, `1/16`, `1/2`, `1/32`, `1/4`, `1/64`, `1/8`, `2`, `4`, `8`  

Specify the dynamic shared memory threshold.

---

### threshold

**Type**: String  
**Path**: `platform.trident.mmu.queue_profiles.[].multicast_queues.[].threshold`  
**Valid Values**: `1`, `1/128`, `1/16`, `1/2`, `1/32`, `1/4`, `1/64`, `1/8`, `2`, `4`, `8`  

Dynamic Shared Memory threshold.


---

### threshold

**Type**: String  
**Path**: `platform.trident.mmu.queue_profiles.[].unicast_queues.[].threshold`  
**Valid Values**: `1`, `1/128`, `1/16`, `1/2`, `1/32`, `1/4`, `1/64`, `1/8`, `2`, `4`, `8`  

Dynamic Shared Memory threshold.


---

## U

### unit

**Type**: String  
**Path**: `platform.trident.mmu.headroom_pool.unit`  
**Valid Values**: `bytes`, `cells`  

Unit to be used for the `headroom_pool` value.
If not specified, default is bytes.

---

### unit

**Type**: String  
**Path**: `platform.trident.mmu.queue_profiles.[].ingress.priority_groups.[].reserved.unit`  
**Valid Values**: `bytes`, `cells`  

Unit to be used for the `priority_groups` `reserved` value.
If not specified, default is bytes.

---

### unit

**Type**: String  
**Path**: `platform.trident.mmu.queue_profiles.[].ingress.reserved.unit`  
**Valid Values**: `bytes`, `cells`  

Unit to be used for the `reserved` value.
If not specified, default is bytes.

---

### unit

**Type**: String  
**Path**: `platform.trident.mmu.queue_profiles.[].ingress.headroom.unit`  
**Valid Values**: `bytes`, `cells`  

Unit to be used for the headroom value.
If not specified, default is bytes.

---

### unit

**Type**: String  
**Path**: `platform.trident.mmu.queue_profiles.[].multicast_queues.[].unit`  
**Valid Values**: `bytes`, `cells`  

Unit to be used for the reservation value. If not specified, default is bytes.


---

### unit

**Type**: String  
**Path**: `platform.trident.mmu.queue_profiles.[].unicast_queues.[].unit`  
**Valid Values**: `bytes`, `cells`  

Unit to be used for the reservation value. If not specified, default is bytes.


---
