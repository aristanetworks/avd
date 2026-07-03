<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# AVD Schema Explorer

A static, [sql.js](https://github.com/sql-js/sql.js)-based browser of the AVD
`eos_designs` and `eos_cli_config_gen` schemas, integrated into the AVD MkDocs
docs site. All queries run in the browser against a local SQLite file —
no backend, no managed runtime, no live database.

Tracked in `aristanetworks/avd-internal#503`.

## Two ways to consume it

| Mode | Syntax / URL | When to use |
| ---- | ------------ | ----------- |
| **Standalone SPA** | `/_assets/schema-explorer/index.html` | Full-screen browser experience: landing -> module -> variable detail, with the SPA's own chrome. Reached from the Data Models overview card. |
| **Markdown embed** | ```` ```schema-explorer ```` fenced block | Drop a focused, scoped reference such as `router_bgp` or `platform_settings` inline next to the prose that explains it. Material header, left nav, and right-rail TOC stay intact. |

Both modes share one set of static assets and one SQLite for the current docs build.

### Markdown embed syntax

Use a `schema-explorer` fenced block in any MkDocs page:

````markdown
```schema-explorer
module: eos_designs
root: platform_settings
height: 500px
```
````

The Markdown formatter renders the block as a `<schema-explorer>` custom element, and the browser-side app mounts the interactive explorer into that element.

| Option | Default | Notes |
| ------ | ------- | ----- |
| `module` | `eos_designs` | `eos_designs`, `eos_cli_config_gen`, or `all`. |
| `root` | *(none)* | Optional key_path prefix; only render that subtree, for example `router_bgp` or `platform_settings`. |
| `view` | `reference` | `reference` or `yaml`. |
| `height` | `600px` | CSS max-height for the embed scroll container. |
| `chrome` | `compact` | `compact` shows the embed filters; `none` hides the results toolbar. |

## Components

| Path                                                                    | What it is                                                                                                                                                                    |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tools/schema-explorer/generate.py`                                     | CLI: loads both AVD schemas through pyavd's `schema_tools` resolver, flattens them, writes `schema.sqlite`, copies the SPA assets next to it.                                 |
| `tools/schema-explorer/static/index.html`                               | Standalone SPA shell — sql.js loader, layout, navigation.                                                                                                                     |
| `tools/schema-explorer/static/css/style.css`                            | Schema Explorer styles + dark-mode rules. Body-level styles are scoped to `.schema-spa-host` / `.schema-embed`.                                                               |
| `tools/schema-explorer/static/js/app.js`                                | Hash router + views for standalone mode; embed mounter for any `<schema-explorer>` element on the page. Lazy-loads runtime JS and icon CSS only when the explorer mounts.     |
| `tools/schema-explorer/mkdocs_hook.py`                                  | MkDocs `on_config` + `on_post_build` hook — auto-builds missing assets, registers the SPA CSS/JS loader, and copies the built SPA into `<site_dir>/_assets/schema-explorer/`. |
| `tools/schema_explorer_markdown.py`                                     | Markdown formatter registered through `pymdownx.superfences`; converts `schema-explorer` fenced blocks into `<schema-explorer>` custom elements.                              |
| `tools/schema-explorer/build/`                                          | **Gitignored.** Output of `make schema-explorer-build`.                                                                                                                       |
| `Makefile` (`schema-explorer-build`, `docs-serve`, `docs-serve-docker`) | Build + serve targets.                                                                                                                                                        |
| `development/entrypoint.sh`                                             | Webdoc container entrypoint — runs the build with an mtime guard before `mkdocs serve`.                                                                                       |
| `mkdocs.yml` (`markdown_extensions:`, `hooks:`, `exclude_docs:`)        | Registers the Markdown formatter and hook; excludes `tools/*` from the docs build.                                                                                            |
| `pyproject.toml` (`doc` group)                                          | Build-time deps for the generator.                                                                                                                                            |

## Build pipeline

```text
              pyavd schema_tools resolver
                          │
                          ▼
 make schema-explorer-build  →  generate.py  ──►  tools/schema-explorer/build/
                                                   ├── index.html
                                                   ├── css/style.css
                                                   ├── js/app.js
                                                   └── data/schema.sqlite
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
                                            └── data/schema.sqlite
```

Two key invariants:

- **Source `docs/` only contains documentation.** Generated SQLite + JS/CSS
  are produced under `tools/schema-explorer/build/` and copied into the
  *built* site by the hook. They never live under the source-controlled
  `docs/` tree.
- **Assets live under `_assets/`, not `docs/`.** The explorer is a shared
  site-wide resource embedded across many doc pages, so it lives at a path
  that says so. The hook registers only the SPA's own CSS and JS loader globally;
  Bootstrap Icons, Bootstrap JS, and sql.js are lazy-loaded only when the
  explorer actually mounts.

### What `generate.py` does

Loads each schema through pyavd's `schema_tools` resolver so:

- `dynamic_keys` placeholders (`<node_type_keys.key>`,
  `<connected_endpoints_keys.key>`, …) are fully expanded.
- Same-schema `$ref` blocks are resolved.
- Cross-schema `$ref` (e.g. `eos_cli_config_gen#/...` from inside
  `eos_designs`) is stripped before resolution and surfaced as a `cross_ref`
  column on the leaf row, so the SQLite stays ~7.5 MB instead of materializing
  the whole `eos_cli_config_gen` hierarchy under every `structured_config`.

### What the Markdown formatter does

`tools/schema_explorer_markdown.py` is registered as a `pymdownx.superfences` custom formatter for `schema-explorer` fenced blocks. It validates the supported options and emits a `<schema-explorer>` custom element. This gives docs authors a reusable Markdown-native interface while keeping the browser runtime in one JavaScript component.

### What `mkdocs_hook.py` does

Two callbacks:

- **`on_config`** — auto-builds `tools/schema-explorer/build/` when the default
  SQLite artifact is missing, then appends the SPA's `style.css` and `app.js` to
  `extra_css` / `extra_javascript`. Every page gets the lightweight loader;
  `app.js` no-ops on pages without a `<schema-explorer>` element or a standalone
  `#app` mount. Bootstrap Icons, Bootstrap JS, and sql.js are lazy-loaded only
  when the explorer mounts, and Bootstrap's full CSS is kept to the standalone
  `static/index.html` page.
- **`on_post_build`** — copies `tools/schema-explorer/build/` into
  `<site_dir>/_assets/schema-explorer/` so the generated site serves the SPA,
  static assets, and SQLite database from one shared location.

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
- `http://127.0.0.1:8000/data-models/` — page with embed demo
- `http://127.0.0.1:8000/_assets/schema-explorer/data/schema.sqlite` —
  the SQLite the browser fetches

## Schema refresh

The docs publishing workflow builds each docs version from the relevant branch.
Schema Explorer publishes one SQLite bundle for that docs build under
`tools/schema-explorer/build/data/schema.sqlite`, which the hook copies into
`site/_assets/schema-explorer/data/`.

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
- **Embedded views via a Markdown fence**, not iframe / template override
  — picked at the May 15th maintainers call. Docs authors use
  `schema-explorer` fenced blocks, which the Markdown formatter renders into
  custom elements. Each embed is a single DOM node to MkDocs, so Material
  TOC, headings nav, and search stay native. Earlier iframe and
  Jinja-override variants were collapsed into the current Material-hosted
  entry page, `docs/schema-explorer.md`.
- **Source and build output both under `tools/`**, copied into `site/_assets/`
  by `mkdocs_hook.py` — keeps `docs/` to documentation only (`.md`, images).
