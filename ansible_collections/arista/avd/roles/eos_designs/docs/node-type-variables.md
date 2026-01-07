<!--
  ~ Copyright (c) 2025-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

| Node Type Key      | Underlay Router | Uplink Type  | EVPN Role | MPLS Role   | L2 Network Services | L3 Network Services | VTEP | MLAG Support | Connected Endpoints | WAN Role | Underlay Routing Protocol | Overlay Routing Protocol | Notes |
| ------------------ | --------------- | ------------ | ----------| ------------| ------------------- | ------------------- | ---- | ------------ | ------------------- | -------- | ------------------------- | ------------------------ | |
| spine              | ✅              | p2p          | server    | ✘           | ✘                   | ✘                   | ✘    | ✘            | ✘                   | ✘        | eBGP                      | eBGP                     | |
| l3leaf             | ✅              | p2p          | client    | ✘           | ✅                  | ✅                  | ✅   | ✅           | ✅                  | ✘        | eBGP                      | eBGP                     | |
| l2leaf             | ✘               | port-channel | N/A       | ✘           | ✅                  | ✘                   | ✘    | ✅           | ✅                  | ✘        | ✘                         | ✘                        | |
| l3spine            | ✅              | p2p          | none      | ✘           | ✅                  | ✅                  | ✘    | ✅           | ✅                  | ✘        | none                      | none                     | |
| l2spine            | ✘               | port-channel | none      | ✘           | ✅                  | ✘                   | ✘    | ✅           | ✅                  | ✘        | ✘                         | ✘                        | |
| super_spine        | ✅              | p2p          | none      | ✘           | ✘                   | ✘                   | ✘    | ✘            | ✘                   | ✘        | eBGP                      | eBGP                     | |
| overlay_controller | ✅              | p2p          | server    | ✘           | ✘                   | ✘                   | ✘    | ✘            | ✘                   | ✘        | eBGP                      | eBGP                     | |
| wan_rr             | ✅              | p2p          | server    | ✘           | ✘                   | ✅                  | ✅   | ✘            | ✘                   | server   | none                      | iBGP                     | AutoVPN RR or Pathfinder depending on the `wan_mode` value. |
| wan_router         | ✅              | p2p          | client    | ✘           | ✘                   | ✅                  | ✅   | ✘            | ✘                   | client   | none                      | iBGP                     | Edge routers for AutoVPN or Edge and Transit routers for CV Pathfinder on the `wan_mode` value. |
| p                  | ✅              | p2p          | none      | none, LSR   | ✘                   | ✘                   | ✘    | ✘            | ✘                   | ✘        | ISIS-SR                   | iBGP                     | |
| rr                 | ✅              | p2p          | server    | server, LSR | ✘                   | ✘                   | ✘    | ✘            | ✘                   | ✘        | ISIS-SR                   | iBGP                     | EVPN with MPLS encapsulation |
| pe                 | ✅              | p2p          | client    | client, LSR | ✅                  | ✅                  | ✘    | ✘            | ✅                  | ✘        | ISIS-SR                   | iBGP                     | EVPN with MPLS encapsulation, L1 Network Services (PW) |
