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

## Two ways to consume it

| Mode | URL | When to use |
|---|---|---|
| **Standalone SPA** | `/_assets/schema-explorer/index.html` | Full-screen browser experience: landing → module → variable detail, with the SPA's own chrome. Reached from the Data Models overview card. |
| **Embedded view** | `<schema-explorer ...></schema-explorer>` in any docs page | Drop a focused, scoped tree (e.g. just `router_bgp`) inline next to the prose that explains it. Material's header, left nav, and right-rail TOC stay intact. |

Both modes share one set of static assets and one SQLite per release.

### `<schema-explorer>` embed attributes

| Attribute | Default | Notes |
|---|---|---|
| `release` | `devel` | Schema release tag. |
| `module` | `eos_designs` | `eos_designs` \| `eos_cli_config_gen` \| `all`. |
| `root` | *(none)* | Optional key_path prefix; only render that subtree (e.g. `router_bgp`). |
| `view` | `tree` | `tree` \| `flat`. |
| `height` | `600px` | CSS max-height for the embed's scroll container. |
| `chrome` | `compact` | `compact` shows the per-tree expand/collapse bar; `none` hides it. |

Example:

```html
<schema-explorer module="eos_cli_config_gen" root="router_bgp" height="500px"></schema-explorer>
```

## Components

| Path | What it is |
|---|---|
| `tools/schema-explorer/generate.py` | CLI: loads both AVD schemas through pyavd's `schema_tools` resolver, flattens them, writes `schema.sqlite`, copies the SPA assets next to it. |
| `tools/schema-explorer/categories.py` | Human-readable category mapping used by the SPA's sidebar classifier. |
| `tools/schema-explorer/static/index.html` | Standalone SPA shell — sql.js loader, layout, navigation. |
| `tools/schema-explorer/static/css/style.css` | Bootstrap overrides + dark-mode rules. Body-level styles are scoped to `.schema-spa-host` / `.schema-embed`. |
| `tools/schema-explorer/static/js/app.js` | Hash router + views for standalone mode; embed mounter for any `<schema-explorer>` element on the page. |
| `tools/schema-explorer/mkdocs_hook.py` | MkDocs `on_config` + `on_post_build` hook — registers Bootstrap + the SPA CSS/JS into `extra_css`/`extra_javascript`, and copies the prebuilt SPA into `<site_dir>/_assets/schema-explorer/`. |
| `tools/schema-explorer/build/` | **Gitignored.** Output of `make schema-explorer-build`. |
| `Makefile` (`schema-explorer-build`, `docs-serve`, `docs-serve-docker`) | Build + serve targets. |
| `development/entrypoint.sh` | Webdoc container entrypoint — runs the build with an mtime guard before `mkdocs serve`. |
| `mkdocs.yml` (`hooks:`, `exclude_docs:`) | Registers the hook; excludes `tools/*` from the docs build. |
| `pyproject.toml` (`doc` group) | Build-time deps for the generator. |

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
                                            site/_assets/schema-explorer/
                                            ├── index.html         (/_assets/schema-explorer/index.html)
                                            ├── css/style.css
                                            ├── js/app.js
                                            └── data/<release>/schema.sqlite
```

Two key invariants:

- **Source `docs/` only contains documentation.** Generated SQLite + JS/CSS
  are produced under `tools/schema-explorer/build/` and copied into the
  *built* site by the hook. They never live under the source-controlled
  `docs/` tree.
- **Assets live under `_assets/`, not `docs/`.** The explorer is a shared
  site-wide resource embedded across many doc pages, so it lives at a path
  that says so. The hook also registers the SPA's CSS/JS globally — every
  page can host an embed without per-page wiring.

### What `generate.py` does

Loads each schema through pyavd's `schema_tools` resolver so:

- `dynamic_keys` placeholders (`<node_type_keys.key>`,
  `<connected_endpoints_keys.key>`, …) are fully expanded.
- Same-schema `$ref` blocks are resolved.
- Cross-schema `$ref` (e.g. `eos_cli_config_gen#/...` from inside
  `eos_designs`) is stripped before resolution and surfaced as a `cross_ref`
  column on the leaf row, so the SQLite stays ~7.5 MB instead of materializing
  the whole `eos_cli_config_gen` tree under every `structured_config`.

### What `mkdocs_hook.py` does

Two callbacks:

- **`on_config`** — appends Bootstrap 5, Bootstrap Icons, the SPA's `style.css`,
  sql.js, and `app.js` to `extra_css` / `extra_javascript`. Every page gets the
  loader; `app.js` no-ops on pages without a `<schema-explorer>` element or a
  standalone `#app` mount, so the per-page runtime cost is just the unfired
  script bytes.
- **`on_post_build`** — copies `tools/schema-explorer/build/` into
  `<site_dir>/_assets/schema-explorer/`. If `build/` doesn't exist (someone
  ran a bare `mkdocs build` without first building the explorer), the hook
  no-ops so the rest of the site still publishes.

## Local development

```bash
# Build the SPA + SQLite, then `mkdocs serve`
make docs-serve

# Same, but inside the webdoc container (no host Python deps required)
make docs-serve-docker

# Just the build (e.g. as a CI step before `mkdocs build`)
make schema-explorer-build
```

URLs once `mkdocs serve` is up:

- `http://127.0.0.1:8000/_assets/schema-explorer/index.html` — standalone SPA
- `http://127.0.0.1:8000/docs/data-models/README.html` — page with embed demo
- `http://127.0.0.1:8000/_assets/schema-explorer/data/devel/schema.sqlite` —
  the SQLite the browser fetches

## Per-release refresh

The SPA expects one SQLite per supported AVD minor release (5.7+). The
publish pipeline runs the generator per release tag and drops each output
under `tools/schema-explorer/build/data/<release>/schema.sqlite`, which the
hook copies into `site/_assets/schema-explorer/data/<release>/`.

The SPA fetches the SQLite with `cache: "no-cache"` so newly published files
are picked up via a conditional GET on the next page load — no hard reload
required.

## Architecture decisions

See `aristanetworks/avd-internal#503` for the full thread. Short version:

- **MkDocs static + sql.js**, not App Engine — picked at the May 8th
  maintainers call.
- **`schema_tools` resolver**, not raw `yaml.safe_load` — see
  `aristanetworks/avd-internal#539`. Closes the dynamic_keys hole and the
  same-schema `$ref` hole, while keeping cross-schema refs as leaf
  annotations to bound the SQLite size.
- **Embedded views via custom HTML element**, not iframe / template override
  — picked at the May 15th maintainers call. Each embed is a single DOM node
  to MkDocs, so Material's TOC, headings nav, and search stay native. Earlier
  iframe and Jinja-override variants (`docs/schema-explorer.md`,
  `docs/schema-explorer-native.md`, `docs/overrides/schema-explorer-page.html`)
  are removed.
- **Source and build output both under `tools/`**, copied into `site/_assets/`
  by `mkdocs_hook.py` — keeps `docs/` to documentation only (`.md`, images).
