<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# AVD Schema Explorer

A static, [sql.js](https://github.com/sql-js/sql.js)-based browser of the AVD
`eos_designs` and `eos_cli_config_gen` schemas, integrated into the AVD MkDocs
docs site. All queries run in the browser against a per-release SQLite file —
no backend, no managed runtime, no live database.

Tracked in `aristanetworks/avd-internal#503`.

## Components

The Schema Explorer is split between source (in `tools/`) and integration
points in the docs (`docs/`, `mkdocs.yml`, `Makefile`,
`development/entrypoint.sh`).

| Path | What it is |
|---|---|
| `tools/schema-explorer/generate.py` | CLI: loads both AVD schemas through pyavd's `schema_tools` resolver, flattens them, writes `schema.sqlite`, copies the SPA assets next to it. |
| `tools/schema-explorer/categories.py` | Human-readable category mapping used by the SPA's sidebar classifier (Categories ↔ Tables toggle). |
| `tools/schema-explorer/static/index.html` | SPA shell — sql.js loader, layout, navigation. |
| `tools/schema-explorer/static/css/style.css` | Bootstrap overrides + dark-mode rules. |
| `tools/schema-explorer/static/js/app.js` | Hash router and views (landing, module-browse, var-detail). |
| `tools/schema-explorer/mkdocs_hook.py` | MkDocs `on_post_build` hook — copies `tools/schema-explorer/build/` into `<site_dir>/docs/schema-explorer/`. |
| `tools/schema-explorer/build/` | **Gitignored.** Output of `make schema-explorer-build`: SPA assets + `data/<release>/schema.sqlite`. |
| `docs/schema-explorer.md` | Iframe-wrapped SPA page. The default integration. |
| `docs/schema-explorer-native.md` | Template-override variant — SPA renders inside Material's chrome natively (no iframe). |
| `docs/overrides/schema-explorer-page.html` | Material template used by the native variant. |
| `Makefile` (`schema-explorer-build`, `docs-serve`, `docs-serve-docker`) | Build + serve targets. |
| `development/entrypoint.sh` | Webdoc container entrypoint — runs the build with an mtime guard before `mkdocs serve`. |
| `mkdocs.yml` (`hooks:`, `exclude_docs:`) | Registers the build-time hook; excludes `tools/*` from the docs build. |
| `pyproject.toml` (`doc` dependency group) | Build-time deps for the generator: `pyyaml`, `referencing`, `deepmerge`, `pydantic`, `jsonschema_rs`. |

## Build pipeline

```text
                pyavd schema_tools resolver
                            │
                            ▼
   make schema-explorer-build  →  generate.py  ──►  tools/schema-explorer/build/
                                                     ├── index.html
                                                     ├── css/style.css
                                                     ├── js/app.js
                                                     └── data/<release>/schema.sqlite
                                                            │
                                                            │   mkdocs build
                                                            ▼
                                              mkdocs_hook.py (on_post_build)
                                                            │
                                                            ▼
                                              site/docs/schema-explorer/
                                              ├── index.html          (served at /docs/schema-explorer/index.html)
                                              ├── css/style.css
                                              ├── js/app.js
                                              └── data/<release>/schema.sqlite
```

Two key invariants:

- **Source `docs/` only contains documentation.** Generated SQLite + JS/CSS
  are produced under `tools/schema-explorer/build/` and copied into the
  *built* site by the hook. They never live under the source-controlled
  `docs/` tree.
- **Published URL space is rooted at `/docs/`.** Because `mkdocs.yml` sets
  `docs_dir: .`, every doc page lives at `/docs/<page>.html` in the built
  site. The hook mirrors this: it writes to `<site_dir>/docs/schema-explorer/`
  so wrapper pages and the template-override variant can reference
  `docs/schema-explorer/...` paths consistently.

### What `generate.py` does

Loads each schema through pyavd's `schema_tools` resolver so:

- `dynamic_keys` placeholders (`<node_type_keys.key>`,
  `<connected_endpoints_keys.key>`, …) are fully expanded.
- Same-schema `$ref` blocks are resolved.
- Cross-schema `$ref` (e.g. `eos_cli_config_gen#/...` from inside
  `eos_designs`) is stripped before resolution and surfaced as a `cross_ref`
  column on the leaf row, so the SQLite stays ~7.5 MB instead of materializing
  the whole `eos_cli_config_gen` tree under every `structured_config`.

`--avd-root` puts `python-avd/` on `PYTHONPATH` automatically. `--release`
embeds the version label in the SQLite and in the output path
(`data/<release>/schema.sqlite`). `--site-dir` is where to write the build
output (and where the SPA assets are copied to alongside the SQLite).

### What `mkdocs_hook.py` does

A single `on_post_build` callback. After MkDocs writes the rest of the site,
the hook copies `tools/schema-explorer/build/` into
`<site_dir>/docs/schema-explorer/`. If `build/` doesn't exist (e.g. someone
runs a bare `mkdocs build` without first building the explorer), the hook
no-ops so the rest of the site still publishes.

## Integration points in MkDocs

There are four places MkDocs needs to know about the explorer:

1. **`hooks:`** in `mkdocs.yml` — registers `mkdocs_hook.py`. This is what
   triggers the copy into `site/`.
2. **`exclude_docs:`** in `mkdocs.yml` — `tools/*` is in the exclude list so
   MkDocs doesn't try to render `tools/schema-explorer/README.md` and friends
   as documentation pages.
3. **Wrapper pages** (`docs/schema-explorer.md`,
   `docs/schema-explorer-native.md`) — these *are* documentation, live under
   `docs/`, and reference the built SPA via `docs/schema-explorer/...` URLs.
4. **Material template override** (`docs/overrides/schema-explorer-page.html`)
   — used by the native variant; pulls SPA assets in via
   `{{ 'docs/schema-explorer/css/style.css' | url }}` etc., which MkDocs
   resolves to the correct URL relative to whatever the page lives at.

### Link validation gotcha

MkDocs' strict-mode link validator can only resolve markdown links against
files it sees as documentation. Direct links to the SPA artifacts
(`docs/schema-explorer/index.html`) therefore have to use raw HTML
`<a href="...">` instead of markdown `[text](url)`, since the SPA isn't a
documentation file. See the two such links in `docs/data-models/README.md`
for the pattern. Markdown links to the wrapper pages
(`docs/schema-explorer.md`, `docs/schema-explorer-native.md`) work normally
because those are real docs.

## Integration variants

Four ways the SPA can be embedded in the docs site, presented in the
`docs/data-models/README.md` callout for team comparison:

| Variant | URL | How it works |
|---|---|---|
| Iframe wrapper | `/docs/schema-explorer.html` | `docs/schema-explorer.md` hosts the SPA in an iframe. AVD docs banner stays put; SPA's own chrome is hidden inside the iframe. |
| Banner-less SPA | `/docs/schema-explorer/index.html?style=none` | Direct hit on the SPA with the `?style=none` flag. No banner — relies on whatever brought the user there. |
| Restyled standalone | `/docs/schema-explorer/index.html` | Direct hit with the SPA's default header restyled to match AVD branding. |
| Native template override | `/docs/schema-explorer-native.html` | `docs/schema-explorer-native.md` + `docs/overrides/schema-explorer-page.html` render the SPA inside Material's chrome natively, no iframe. |

The variants share one set of static assets and one SQLite per release —
they're just different shells around the same SPA.

## Local development

```bash
# Build the SPA + SQLite, then `mkdocs serve`
make docs-serve

# Same, but inside the webdoc container (no host Python deps required)
make docs-serve-docker

# Just the build (e.g. as a CI step before `mkdocs build`)
make schema-explorer-build
```

`make docs-serve` always rebuilds the explorer first. The webdoc container
applies an mtime guard (rebuild only when `eos_designs.schema.yml` is newer
than the existing SQLite) so container restarts during iteration are fast.

URLs once `mkdocs serve` is up:

- `http://127.0.0.1:8000/docs/schema-explorer.html` — iframe wrapper
- `http://127.0.0.1:8000/docs/schema-explorer-native.html` — native template
- `http://127.0.0.1:8000/docs/schema-explorer/index.html` — raw SPA
- `http://127.0.0.1:8000/docs/schema-explorer/data/devel/schema.sqlite` —
  the SQLite the browser fetches

## Per-release refresh

The SPA expects one SQLite per supported AVD minor release (5.7+). The
publish pipeline runs the generator per release tag and drops each output
under `tools/schema-explorer/build/data/<release>/schema.sqlite`, which the
hook then copies into `site/docs/schema-explorer/data/<release>/`.

The SPA fetches the SQLite with `cache: "no-cache"` so newly published files
are picked up via a conditional GET on the next page load — no hard reload
required.

## Architecture decisions

See `aristanetworks/avd-internal#503` for the full thread. Short version:

- **MkDocs static + sql.js**, not App Engine — picked at the May 8th
  maintainers call. No managed-service patching, no LB URL map, no GCS bucket
  for data files; the SQLite ships under the docs bucket alongside everything
  else and the browser does the queries.
- **`schema_tools` resolver**, not raw `yaml.safe_load` — see
  `aristanetworks/avd-internal#539`. Closes the dynamic_keys hole (entire
  top-level subtrees like `<node_type_keys.key>` were missing) and the
  same-schema `$ref` hole, while keeping cross-schema refs as leaf
  annotations to bound the SQLite size.
- **Source and build output both under `tools/`**, copied into `site/` by
  `mkdocs_hook.py` — keeps `docs/` to documentation only (`.md`, images).
  (See PR thread for the four locations considered for source.)
