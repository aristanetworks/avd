---
hide:
  - navigation
  - toc
title: Schema Explorer
---

<!--
  ~ Copyright (c) 2024-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Schema Explorer

<style>
  /* Hide Material's left nav and right TOC for this page only — the iframe
     uses every pixel and doesn't need the sub-nav. The `hide:` frontmatter
     should also do this on Material 9+; this CSS is a belt-and-braces fix. */
  .md-sidebar { display: none !important; }
  .md-content { max-width: 100% !important; margin: 0 !important; }
  .md-main__inner { margin: 0 !important; max-width: 100% !important; }
  .md-grid { max-width: none !important; }
  /* Squash MkDocs' default page chrome so the iframe sits flush under the
     AVD docs banner. The SPA's own content already shows "AVD Design" / "EOS
     Config" headers, so the wrapper's h1 is visually redundant — keep it for
     MkDocs nav/breadcrumb metadata but hide it on the page. */
  .md-content__inner { padding: 0 !important; margin: 0 !important; }
  .md-content__inner > h1:first-child {
    position: absolute;
    width: 1px; height: 1px;
    padding: 0; margin: -1px;
    overflow: hidden; clip: rect(0,0,0,0);
    white-space: nowrap; border: 0;
  }
</style>

<iframe id="schema-explorer-frame"
        src="schema-explorer/index.html"
        title="AVD Schema Explorer"
        style="display: block; width: 100%; height: calc(100vh - 100px); min-height: 600px; border: 0;">
</iframe>

<script>
// Forward the hash from this MkDocs page into the iframe so deep links like
// `schema-explorer.html#/eos_designs` land on the right module inside the SPA.
(function () {
  const frame = document.getElementById("schema-explorer-frame");
  function syncHash() {
    if (!window.location.hash) return;
    const target = "schema-explorer/index.html" + window.location.hash;
    // Only reload the iframe if the target actually changed — avoids a refresh
    // loop when the SPA itself updates its inner hash.
    try {
      const inner = frame.contentWindow.location;
      if (inner && inner.pathname.endsWith("/schema-explorer/index.html")
          && inner.hash === window.location.hash) return;
    } catch (e) { /* cross-origin guard, harmless */ }
    frame.src = target;
  }
  syncHash();
  window.addEventListener("hashchange", syncHash);
})();

// Forward Material's color scheme to the SPA inside the iframe. The SPA uses
// Bootstrap's `data-bs-theme` on <html>; Material puts `data-md-color-scheme`
// ("default" | "slate") on <body>. Re-applies on every Material toggle and
// on iframe reload.
(function () {
  const frame = document.getElementById("schema-explorer-frame");
  function currentTheme() {
    return document.body.getAttribute("data-md-color-scheme") === "slate" ? "dark" : "light";
  }
  function applyTheme() {
    try {
      const doc = frame.contentDocument;
      if (doc && doc.documentElement) {
        doc.documentElement.setAttribute("data-bs-theme", currentTheme());
      }
    } catch (e) { /* cross-origin guard */ }
  }
  frame.addEventListener("load", applyTheme);
  new MutationObserver(applyTheme).observe(document.body, {
    attributes: true,
    attributeFilter: ["data-md-color-scheme"],
  });
  applyTheme();
})();
</script>
