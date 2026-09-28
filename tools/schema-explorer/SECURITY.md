# Schema Explorer security notes

The Schema Explorer is a **static, read-only** docs application: build-time
schema flattening, a generated SQLite file, client-side `sql.js` queries, and
HTML rendering in the browser. There is no backend, authentication, telemetry,
or write path.

Parent tracking: [aristanetworks/avd-internal#503](https://github.com/aristanetworks/avd-internal/issues/503),
security review: [aristanetworks/avd-internal#641](https://github.com/aristanetworks/avd-internal/issues/641).

## Threat model

| Actor | Capability | Goal |
| ----- | ---------- | ---- |
| Docs visitor | Controls URL hash fragments and browser environment | Browse schema data shipped with the docs build |
| Docs author | Writes `schema-explorer` fenced blocks | Embed scoped explorers in MkDocs pages |
| Maintainer | Changes generator, hook, SPA, or vendored assets | Ship schema updates and UI fixes |

**Out of scope:** multi-tenant isolation, secret handling, server-side query
injection (there is no server query surface).

## Invariants (must stay true)

1. **Static and same-origin** — Runtime JS, CSS, fonts, WASM, and `schema.sqlite`
   are served from `<site>/_assets/schema-explorer/` (or equivalent) on the same
   origin as the docs. No runtime CDN loads without explicit maintainer review.
2. **Read-only data** — The browser never writes to SQLite; schema sources are
   trusted repo files at build time only.
3. **Constrained authoring** — Docs authors use the `schema-explorer` SuperFences
   formatter, not raw HTML embeds. Fence YAML is parsed with `yaml.safe_load` and
   only allowlisted keys become element attributes (HTML-escaped).
4. **Allowlisted publishing** — `mkdocs_hook._copy_expected_build_artifacts()`
   copies only `index.html`, `css/`, `js/`, `vendor/`, and `data/schema.sqlite`.
   No broad directory sync from the build cache into the public site.
5. **Parameterized SQL** — Client queries use bound parameters, not string
   concatenation of user input into SQL text.
6. **Escaped dynamic HTML** — Schema-derived strings, search highlights, fence
   attributes, and cross-schema links must pass through `escapeHtml` /
   `escapeAttr` (see `static/js/sanitize.js`) or safe URL encoding before
   assignment to `innerHTML` or attribute templates.

## Untrusted inputs at render time

Treat these as untrusted when producing HTML or navigable URLs:

- Schema descriptions, defaults, deprecation text, and key paths from SQLite
- User search strings and hash-route segments
- Fence option values (`module`, `root`, `view`, `height`, `chrome`)
- Cross-schema `$ref` strings converted into hash links

## Regression risks

The highest long-term risk is **XSS through `innerHTML` drift**: new table cells,
tooltips, markdown paths, or links added without escaping. Secondary risks are
**CDN sprawl**, **global Bootstrap CSS** on normal docs pages, and **accidental
broad artifact publishing** from the MkDocs hook.

## Vendored runtime dependencies

See the inventory table in [README.md](README.md#vendored-runtime-dependencies).
Updates must refresh Subresource Integrity (`integrity=` attributes in
`static/index.html` and lazy-load metadata in `app.js`) and re-run
`make schema-explorer-check`.

## Verification

Local maintainer check:

```bash
make schema-explorer-check
```

CI runs the same target when Schema Explorer paths change. Maintainer rules for
agents and contributors: [AGENTS.md](AGENTS.md).
