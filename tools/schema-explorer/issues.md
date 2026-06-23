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
- Key detail sidebars showed broad module totals and generic peer/root-key lists, which consumed space and made details harder to read. Detail pages now use the full width, and dynamic-key context is shown as a compact property row.
- Large defaults such as `platform_settings` rendered inline in Default columns and made browse/detail pages unreadable. Tables now show compact summaries only for genuinely large defaults, while detail pages extract structured defaults into readable sections with raw JSON still available.

## Open

1. Improve search as the primary UX fix
   - Search should be interactive while the user types, not only after a full refresh or manual navigation step.
   - Show useful in-flight matches or previews so users can tell whether the query is working.
   - Matching keys should be reachable without forcing users to expand every ancestor manually.
   - Pressing Enter should expand or reveal matching keys in tree mode.
   - Flat view is somewhat better today, but the overall search UI still needs improvement.

2. Remove scroll-in-scroll friction
   - Avoid nested scroll containers inside MkDocs pages.
   - For embedded explorers, let the explorer content participate in the page scroll wherever possible.
   - Keep only lightweight internal scrolling where unavoidable, such as short filter dropdowns/popups.

3. Align styles with Material for MkDocs
   - The Schema Explorer styling still reads as foreign to the generated docs page.
   - Spacing, typography, controls, table treatment, colors, and interaction states should feel native to the surrounding Material theme.
   - Embedded and full-page views should share the same visual language as the docs site instead of looking like an imported app.

4. Revisit categories versus tables selector
   - It is not clear why both selector concepts are necessary.
   - Remove or hide selectors that do not map directly to reader workflows.
   - Keep navigation focused on the schema lookup task.

5. Hide low-value summary counts
   - The number-of-variables summary should likely be hidden.
   - It adds visual noise without helping readers complete schema lookup tasks.

6. Treat Data Models versus Schema Explorer as temporary
   - The goal is for Schema Explorer to replace the existing manual.
   - The Data Models / Schema Explorer selector should not become permanent navigation.
   - Migration UI should disappear once the Schema Explorer can cover the manual use cases.

## Implementation order

1. Make search interactive and show live results or previews while typing.
2. Expand or reveal matching tree keys on Enter and make filtered tree results navigable without manual ancestor expansion.
3. Fix the scroll model so embedded explorers use the MkDocs page scroll.
4. Bring Schema Explorer styles in line with Material for MkDocs.
5. Remove or simplify the categories/tables selector path.
6. Hide the variables count and remove temporary migration selectors when no longer needed.

## Validation

- Typing in search updates visible results without extra navigation.
- Pressing Enter on a search reveals matching keys in tree mode.
- Users do not have to expand every parent manually to inspect search matches.
- Embedded explorers do not create nested-scroll friction on desktop or mobile.
- Schema Explorer controls and tables visually match the surrounding MkDocs page.
- Category/table selector behavior is either clearly useful or removed.
- Variable counts are hidden unless there is a concrete reader need for them.
- The Data Models / Schema Explorer selector is tracked as temporary migration UI.
