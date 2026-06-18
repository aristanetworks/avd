<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Schema Explorer Issues

## Fixed in this branch

- Bootstrap CSS was lazy-loaded by `app.js` into Material-hosted docs pages. Since Bootstrap CSS has global element rules, opening the Schema Explorer could change surrounding docs typography such as headings, links, and line-height. `app.js` now avoids injecting `bootstrap.min.css`; the standalone SPA still loads Bootstrap CSS from `static/index.html`, where it owns the full page.
- The "All Modules" tree view used `key_path` as the identity key even though rows are unique by `(release, module, key_path)`. Tree state now uses module-aware row, parent, and group identities so duplicate key paths across modules do not overwrite each other.

## Open

- `renderModule()` attaches a delegated classifier click handler to `document` every time the module view renders. Repeated navigation can leave stale handlers active; scope the handler to the current view container or make it abortable.
- Some README and MkDocs comments still describe older hook behavior, including global Bootstrap/sql.js injection and missing-build no-op behavior.
