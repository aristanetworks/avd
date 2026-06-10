---
# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
hide: [toc]
title: Schema Explorer
---

# Schema Explorer

<style>
  /* Give the SPA the full content width and a stable scroll container.
     `hide: [toc]` already removes the right rail; Material keeps the left
     nav so this page still sits inside the docs tree. */
  .md-content__inner > #app { max-width: 100%; }
  #app { min-height: calc(100vh - 13rem); }
</style>

<div id="app" class="schema-spa-host container-fluid py-3">
  <div class="text-center py-5 text-muted">
    <span class="spinner-border spinner-border-sm" role="status"></span>
    <span class="ms-2 small">Loading schema database…</span>
  </div>
</div>
<select id="release-select" class="d-none">
  <option value="devel">devel</option>
</select>
