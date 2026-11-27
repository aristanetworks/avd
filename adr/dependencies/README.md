<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Dependency Decision Backlog

This domain covers dependency ownership, constraints, upgrades, exceptions, and immutable CI references.

| ID | Proposed decision question | Why it is architecturally significant |
| -- | -------------------------- | ------------------------------------- |
| `dependencies/0001` | Use `pyproject.toml` declarations as dependency sources of truth | Prevent generated collection and documentation requirement files from drifting. |
| `dependencies/0002` | Prefer ranges and justify exact pins | Remain composable in larger Python environments while controlling tightly coupled components. |
| `dependencies/0003` | Manage patched and coupled dependencies as explicit exceptions | Give exceptions such as patched integrations and exact companion-package pins an owner and exit condition. |
| `dependencies/0004` | Group automated upgrades and apply a cooldown | Reduce update noise and avoid consuming unstable upstream releases immediately. |
| `dependencies/0005` | Pin CI actions to immutable commits | Prevent mutable tags from changing trusted CI code without repository review. |
