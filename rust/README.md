<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

> [!WARNING]
> This code is work-in-progress and is not currently being used by AVD.

```mermaid
---
title: Rust crate layout
---
graph LR
validation["crate validation"]
avdschema["crate avdschema"]
avdschema_macros["crate avdschema_macros"]
included_store["crate included_store"]
avdschema_macros --->|depends on| avdschema
included_store --->|depends on| avdschema
included_store --->|depends on| avdschema_macros
validation --->|depends on| avdschema
validation --->|depends on| avdschema_macros
```
