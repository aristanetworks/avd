---
hide: [toc]
title: Schema Explorer
---
<!--
  ~ Copyright (c) 2024-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Schema Explorer

<style>
  /* Give the SPA the full content width and a stable scroll container.
     `hide: [toc]` already removes the right rail; Material keeps the left
     nav so this page still sits inside the docs tree. */
  .md-content__inner > h1:first-of-type { margin-bottom: 0.75rem; }
  .md-content__inner > #app { max-width: 100%; margin-top: 0; padding-top: 0 !important; }
  #app { min-height: 0; }
  .md-source-file { display: none !important; }
</style>

<div id="app" class="schema-spa-host container-fluid py-3">
  <div class="text-center py-5 text-muted">
    <span class="spinner-border spinner-border-sm" role="status"></span>
    <span class="ms-2 small">Loading schema database…</span>
  </div>
</div>
