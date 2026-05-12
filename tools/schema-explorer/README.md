<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# AVD Schema Explorer — source

Source for the static, sql.js-based browser of the AVD `eos_designs` and
`eos_cli_config_gen` schemas. Source and build output both live under
`tools/`; `mkdocs_hook.py` copies the built tree into
`site/docs/schema-explorer/` on every `mkdocs build`, so no application code
or generated data ever lives under the source-controlled `docs/` tree.

Tracked in `aristanetworks/avd-internal#503`.

## Layout

```text
tools/schema-explorer/
├── generate.py          # CLI: schemas → SQLite + copies static assets to --site-dir
├── categories.py        # Category mapping for the sidebar classifier
├── mkdocs_hook.py       # MkDocs hook: copies build/ into site/schema-explorer/
├── README.md            # this file
├── static/              # SPA source — copied verbatim into --site-dir
│   ├── index.html       # SPA shell — sql.js loader + nav
│   ├── css/style.css    # Bootstrap overrides + dark-mode rules
│   └── js/app.js        # Hash router + landing/module/var-detail views
└── build/               # gitignored build output (see Build below)
```

## Build

From the repo root:

```bash
make schema-explorer-build
# or directly:
python tools/schema-explorer/generate.py \
    --avd-root . --release devel --site-dir tools/schema-explorer/build
```

Output:

```text
tools/schema-explorer/build/             # gitignored — built artifact
├── index.html
├── css/style.css
├── js/app.js
└── data/devel/schema.sqlite             # generated; ~7.5 MB
```

`mkdocs build` then runs `mkdocs_hook.py`, which copies that tree into
`<site_dir>/docs/schema-explorer/`. The MkDocs wrapper page
`docs/schema-explorer.md` references that path in the published site
(matching the `docs/`-rooted URL space the rest of the site uses).

`make docs-serve` runs the build before `mkdocs serve`. The webdoc container
(`docker compose -f development/docker-compose.yml up`) does the same via
`development/entrypoint.sh`, with an mtime guard so restarts are fast.

## What `generate.py` does

Loads each schema through pyavd's `schema_tools` resolver so:

- `dynamic_keys` placeholders (`<node_type_keys.key>`,
  `<connected_endpoints_keys.key>`, …) are fully expanded.
- Same-schema `$ref` blocks are resolved.
- Cross-schema `$ref` (e.g. `eos_cli_config_gen#/...` from inside
  `eos_designs`) is stripped before resolution and surfaced as a `cross_ref`
  column on the leaf row, so the SQLite stays ~7.5 MB instead of materializing
  the whole `eos_cli_config_gen` tree under every `structured_config`.

Required Python packages (already in the `doc` dependency group of
`pyproject.toml`): `pyyaml`, `referencing`, `deepmerge`, `pydantic`,
`jsonschema_rs`. `--avd-root` puts `python-avd/` on `PYTHONPATH`
automatically.

Repeat per supported AVD release (5.7+); the publish pipeline drops each
output under `tools/schema-explorer/build/data/<release>/schema.sqlite`,
which `mkdocs_hook.py` then copies into
`site/docs/schema-explorer/data/<release>/`.

## Architecture decisions

See aristanetworks/avd-internal#503 for the full thread. Short version:

- **MkDocs static + sql.js**, not App Engine — picked at the May 8th
  maintainers call. No managed-service patching, no LB URL map, no GCS bucket
  for data files; the SQLite ships under the docs bucket alongside everything
  else and the browser does the queries.
- **`schema_tools` resolver**, not raw `yaml.safe_load` — see
  aristanetworks/avd-internal#539. Closes the dynamic_keys hole (entire
  top-level subtrees like `<node_type_keys.key>` were missing) and the
  same-schema `$ref` hole, while keeping cross-schema refs as leaf
  annotations to bound the SQLite size.
- **Source and build output both under `tools/`**, copied into `site/` by
  `mkdocs_hook.py` — keeps `docs/` to documentation only (`.md`, images).
  (See PR thread for the four locations considered for source.)
