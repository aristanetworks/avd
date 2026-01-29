# Glossary

## Table of Contents

- [W](#w)

## W

### wan_route_servers

**Type**: List, items: Dictionary  
**Path**: `wan_route_servers`  

List of the AutoVPN RRs when using `wan_mode: legacy-autovpn`, or the Pathfinders
when using `wan_mode: cv-pathfinder`, to which the device should connect to.
This is also used to establish iBGP sessions between WAN route servers.

When the route server is part of the same inventory as the WAN routers,
only the name is required.

---
