# router-pim-sparse-mode
# Table of Contents

- [Multicast](#multicast)
  - [PIM Sparse Mode](#pim-sparse-mode)

# Multicast

## PIM Sparse Mode

### Router PIM Sparse Mode

#### IP Sparse Mode Information

BFD enabled: True

##### IP Rendezvous Information

| Rendezvous Point Address | Group Address | Access Lists | Priority | Hashmask | Override |
| ------------------------ | ------------- | ------------ | -------- | -------- | -------- |
| 10.238.1.161 | 239.12.12.12/32, 239.12.12.13/32 | - | - | - | - |

##### IP Anycast Information

| IP Anycast Address | Other Rendezvous Point Address | Register Count |
| ------------------ | ------------------------------ | -------------- |
| 10.38.1.161 | 10.50.64.16 | 15 |

#### Router Multicast Device Configuration

```eos
!
router pim sparse-mode
   ipv4
      bfd
      rp address 10.238.1.161 239.12.12.12/32
      rp address 10.238.1.161 239.12.12.13/32
      anycast-rp 10.38.1.161 10.50.64.16 register-count 15
```
