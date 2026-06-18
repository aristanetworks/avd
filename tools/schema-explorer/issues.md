<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Schema Explorer Issues

## Fixed in this branch

- Bootstrap CSS was lazy-loaded by `app.js` into Material-hosted docs pages. Since Bootstrap CSS has global element rules, opening the Schema Explorer could change surrounding docs typography such as headings, links, and line-height. `app.js` now avoids injecting `bootstrap.min.css`; the standalone SPA still loads Bootstrap CSS from `static/index.html`, where it owns the full page.
- The "All Modules" tree view used `key_path` as the identity key even though rows are unique by `(release, module, key_path)`. Tree state now uses module-aware row, parent, and group identities so duplicate key paths across modules do not overwrite each other.
- `renderModule()` attached a delegated classifier click handler to `document` every time the module view rendered. The listener is now scoped to the classifier container created by the current render, so navigation discards old handlers with the old DOM.
- README and MkDocs comments described older hook behavior, including global Bootstrap/sql.js injection and missing-build no-op behavior. They now describe the current auto-build, global SPA loader, and runtime lazy-loading behavior.
- The Material-hosted Schema Explorer lost Bootstrap grid/list/card styling after global Bootstrap CSS was removed. The stylesheet now includes a scoped compatibility layer under `.schema-spa-host` / `.schema-embed` for the Bootstrap utilities used by the explorer.
- Filtered tree views rendered matching child rows before their fetched ancestor context rows, so expanding groups such as `cv_settings` showed subkeys above their parents. Group rows are now sorted parent-first after context rows are merged.

## Open

No known review issues remain in this note.
