# Schema Explorer maintenance rules

These rules apply to `tools/schema-explorer/`, `tools/schema_explorer_markdown.py`,
and any MkDocs or CI wiring that publishes Schema Explorer assets.

1. Keep the explorer **static and read-only**. Do not add a backend, API service,
   auth flow, telemetry endpoint, or server-side query path.
2. Treat all schema, database, hash, and attribute values as **untrusted when
   rendering HTML**.
3. Prefer DOM APIs for new interactive rendering. If string templates are used,
   every dynamic value must pass through `escapeHtml`, `escapeAttr`, or URL
   encoding as appropriate (`static/js/sanitize.js`).
4. Do not use raw `innerHTML` with unescaped dynamic values.
5. Do not load new third-party runtime assets from CDNs without explicit
   maintainer review and SECURITY.md updates.
6. Do not globally import Bootstrap CSS into MkDocs Material pages (Bootstrap is
   scoped to the SPA host / embed mount paths only).
7. Publish **only allowlisted** generated files via `mkdocs_hook.py`; extend the
   allowlist and tests together when new public artifacts are required.
8. Keep Markdown authoring constrained to the **`schema-explorer` fence**. Do not
   ask docs authors to paste raw HTML embeds.
9. Add or update automated tests (`tools/schema-explorer/tests/`, `test_sanitize.mjs`)
   for any new view, route, renderer, or dependency.
10. Any new external dependency must document **why** it is needed, **where** it
    is loaded from, and **how** it is updated (README vendored inventory +
    SECURITY.md).

Before opening a PR, read [SECURITY.md](SECURITY.md) and run:

```bash
make schema-explorer-check
```
