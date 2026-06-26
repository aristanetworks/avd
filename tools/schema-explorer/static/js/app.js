/* AVD Schema Explorer — static / sql.js variant.
 *
 * Loads schema.sqlite into the browser via sql.js (WASM), then renders
 * landing / module-browse / var-detail views via hash routing. No backend.
 */

// Split a key_path on "." while treating `<...>` placeholders as atomic, so
// `<connected_endpoints_keys.key>.foo.bar` → ["<connected_endpoints_keys.key>", "foo", "bar"]
// instead of the naive split's ["<connected_endpoints_keys", "key>", "foo", "bar"].
function splitKeyPath(keyPath) {
  const out = [];
  let buf = "";
  let depth = 0;
  for (const c of keyPath) {
    if (c === "<") { depth++; buf += c; }
    else if (c === ">") { depth = Math.max(0, depth - 1); buf += c; }
    else if (c === "." && depth === 0) { out.push(buf); buf = ""; }
    else { buf += c; }
  }
  if (buf || out.length === 0) out.push(buf);
  return out;
}
function rootSegment(keyPath) {
  return stripPlaceholderBrackets(splitKeyPath(keyPath)[0].replace("[]", ""));
}
function leafSegment(keyPath) {
  return stripPlaceholderBrackets(splitKeyPath(keyPath).pop());
}
function yamlKeySegment(keyPath) {
  return splitKeyPath(keyPath).pop().replace("[]", "");
}
function dynamicKeySource(keyPath) {
  const match = String(keyPath).match(/^<([^>]+)>/);
  return match ? match[1] : "";
}
// Pyavd's docs convention wraps dynamic_keys placeholders in `<...>`
// (e.g. <connected_endpoints_keys.key>). Brackets are noise once the user is
// inside the explorer — strip them for display only. URL hashes and DB
// lookups still use the canonical bracketed form.
function stripPlaceholderBrackets(s) {
  return String(s).replace(/^<(.+)>$/, "$1");
}
function displayPath(keyPath) {
  return splitKeyPath(keyPath).map(stripPlaceholderBrackets).join(".");
}
function formatDefaultSummary(parsed, raw) {
  if (Array.isArray(parsed)) return `list, ${parsed.length} item${parsed.length === 1 ? "" : "s"}`;
  if (parsed && typeof parsed === "object") {
    const count = Object.keys(parsed).length;
    return `dict, ${count} key${count === 1 ? "" : "s"}`;
  }
  return raw.length > 160 ? "large default" : raw;
}
function defaultValueParts(value, noneLabel = "-") {
  if (!value) return { hasValue: false, summary: noneLabel, full: noneLabel, large: false, parsed: null, parseOk: false };
  const raw = String(value);
  let parsed = null;
  let parseOk = false;
  try {
    parsed = JSON.parse(raw);
    parseOk = true;
  } catch {
    // Keep non-JSON defaults as plain text.
  }
  const full = parseOk ? JSON.stringify(parsed, null, 2) : raw;
  const large = raw.length > 160 || full.length > 240 || full.includes("\n");
  return {
    hasValue: true,
    summary: large ? formatDefaultSummary(parseOk ? parsed : null, raw) : raw,
    full,
    large,
    parsed,
    parseOk,
  };
}
function renderDefaultScalar(value) {
  if (value === null) return `<code>null</code>`;
  if (value === undefined) return `<code>-</code>`;
  if (typeof value === "boolean" || typeof value === "number") return `<code>${escapeHtml(String(value))}</code>`;
  return `<code>${escapeHtml(String(value))}</code>`;
}
function renderDefaultFieldValue(value) {
  if (Array.isArray(value)) {
    if (!value.length) return `<code>[]</code>`;
    if (value.every(item => item === null || ["string", "number", "boolean"].includes(typeof item))) {
      return `<div class="schema-default-pill-list">${value.map(item => `<code>${escapeHtml(String(item))}</code>`).join("")}</div>`;
    }
    return `<pre class="schema-default-inline-json"><code>${escapeHtml(JSON.stringify(value, null, 2))}</code></pre>`;
  }
  if (value && typeof value === "object") {
    return renderDefaultObjectTable(value, "schema-default-nested-table");
  }
  return renderDefaultScalar(value);
}
function renderDefaultObjectTable(obj, className = "schema-default-field-table") {
  const rowsHtml = Object.entries(obj).map(([key, value]) => `
    <tr>
      <td class="schema-default-field-key"><code>${escapeHtml(key)}</code></td>
      <td>${renderDefaultFieldValue(value)}</td>
    </tr>`).join("");
  return `<table class="table table-sm align-middle mb-0 ${className}"><tbody>${rowsHtml}</tbody></table>`;
}
function renderStructuredDefault(parts) {
  if (!parts.parseOk) return "";
  if (Array.isArray(parts.parsed) && parts.parsed.every(item => item && typeof item === "object" && !Array.isArray(item))) {
    const idPrefix = `d${++_treeRenderSeq}`;
    const itemsHtml = parts.parsed.map((item, idx) => {
      const fields = Object.fromEntries(Object.entries(item).filter(([key]) => key !== "platforms"));
      const platforms = Array.isArray(item.platforms) && item.platforms.length
        ? item.platforms.join(", ")
        : `Item ${idx + 1}`;
      const settingsCount = Object.keys(fields).length;
      const id = `${idPrefix}-item-${idx}`;
      return `
        <div class="schema-group schema-default-group">
          <div class="schema-group-header" data-bs-toggle="collapse" data-bs-target="#${id}" aria-expanded="false" aria-controls="${id}">
            <i class="bi bi-chevron-right collapse-icon"></i>
            <code class="schema-key-code fw-bold" style="font-size: 0.82rem;">${escapeHtml(platforms)}</code>
            <span class="badge bg-secondary ms-1" style="font-size: 0.6rem;">${settingsCount} setting${settingsCount === 1 ? "" : "s"}</span>
          </div>
          <div class="collapse" id="${id}">
            ${renderDefaultObjectTable(fields)}
          </div>
        </div>`;
    }).join("");
    return `<div class="schema-default-structured schema-default-groups">${itemsHtml}</div>`;
  }
  if (parts.parsed && typeof parts.parsed === "object" && !Array.isArray(parts.parsed)) {
    return `<div class="schema-default-structured">${renderDefaultObjectTable(parts.parsed)}</div>`;
  }
  return "";
}
function renderDefaultValue(value, options = {}) {
  const parts = defaultValueParts(value, options.noneLabel || "-");
  if (!parts.hasValue || !parts.large) return `<code>${escapeHtml(parts.summary)}</code>`;
  if (options.compact) return `<code class="schema-default-compact" title="${escapeAttr(parts.summary)}">${escapeHtml(parts.summary)}</code>`;
  const structuredHtml = renderStructuredDefault(parts);
  if (structuredHtml) {
    return `
      <div class="schema-default-details">
        ${structuredHtml}
        <details class="schema-default-raw"><summary class="schema-default-summary"><span class="small">Raw JSON</span></summary><pre class="schema-default-full"><code>${escapeHtml(parts.full)}</code></pre></details>
      </div>`;
  }
  const openAttr = options.open ? " open" : "";
  return `
    <details class="schema-default-details"${openAttr}>
      <summary class="schema-default-summary"><code>${escapeHtml(parts.summary)}</code></summary>
      <pre class="schema-default-full"><code>${escapeHtml(parts.full)}</code></pre>
    </details>`;
}
function rowModule(row, currentModule) {
  return currentModule === "all" ? row.module : currentModule;
}
function treeRowId(row, currentModule) {
  return `${rowModule(row, currentModule)}:${row.key_path}`;
}
function treeParentId(row, currentModule) {
  return row.parent_path ? `${rowModule(row, currentModule)}:${row.parent_path}` : "";
}
function parentPathCandidates(row) {
  const parentPath = String(row.parent_path || "");
  if (!parentPath) return [];
  const candidates = [parentPath];
  if (parentPath.endsWith("[]")) candidates.push(parentPath.slice(0, -2));
  const collapsedListPath = parentPath.replace(/\[\](?=\.|$)/g, "");
  if (collapsedListPath !== parentPath) candidates.push(collapsedListPath);
  return [...new Set(candidates)];
}
function resolvedTreeParentId(row, currentModule, rowIds) {
  const directParentId = treeParentId(row, currentModule);
  if (!directParentId || !rowIds || rowIds.has(directParentId)) return directParentId;

  const rowModuleId = rowModule(row, currentModule);
  const candidates = parentPathCandidates(row).slice(1).map(keyPath => `${rowModuleId}:${keyPath}`);
  return candidates.find(candidate => rowIds.has(candidate)) || directParentId;
}
function orderedTreeRows(vars, currentModule) {
  const sortedVars = [...vars].sort((a, b) => `${rowModule(a, currentModule)}:${a.key_path}`.localeCompare(`${rowModule(b, currentModule)}:${b.key_path}`));
  const rowIds = new Set(sortedVars.map(row => treeRowId(row, currentModule)));
  const childCount = new Map();
  const childrenByParent = new Map();
  const parentIds = new Map();
  const rootRows = [];

  for (const row of sortedVars) {
    const rowId = treeRowId(row, currentModule);
    const resolvedParentId = resolvedTreeParentId(row, currentModule, rowIds);
    const visibleParentId = resolvedParentId && rowIds.has(resolvedParentId) ? resolvedParentId : "";
    parentIds.set(rowId, visibleParentId);
    if (!visibleParentId) {
      rootRows.push(row);
      continue;
    }
    if (!childrenByParent.has(visibleParentId)) childrenByParent.set(visibleParentId, []);
    childrenByParent.get(visibleParentId).push(row);
    childCount.set(visibleParentId, (childCount.get(visibleParentId) || 0) + 1);
  }

  const orderedRows = [];
  const visited = new Set();
  function visit(row) {
    const rowId = treeRowId(row, currentModule);
    if (visited.has(rowId)) return;
    visited.add(rowId);
    orderedRows.push(row);
    (childrenByParent.get(rowId) || []).forEach(visit);
  }
  rootRows.forEach(visit);
  sortedVars.forEach(visit);
  return { rows: orderedRows, childCount, parentIds, rowIds };
}
function treeGroupId(row, currentModule) {
  const root = rootSegment(row.key_path);
  return currentModule === "all" ? `${rowModule(row, currentModule)}:${root}` : root;
}

// Where the SPA fetches `schema.sqlite` from. Resolution order:
//   1. `window.SCHEMA_BASE_OVERRIDE` — explicit opt-out for hosts that already
//      know exactly where the data lives.
//   2. The directory containing this script, with `/data` appended. Works for
//      both the standalone `_assets/schema-explorer/index.html` page (script
//      lives under `_assets/schema-explorer/js/app.js`) and arbitrary MkDocs
//      pages that embed `<schema-explorer>` — fetches must be absolute since
//      the page URL is unrelated to the asset location.
//   3. Plain `data/` — last-resort relative path, kept for hand-rolled hosts.
function inferSchemaBase() {
  if (typeof window !== "undefined" && window.SCHEMA_BASE_OVERRIDE) return window.SCHEMA_BASE_OVERRIDE;
  const scripts = document.getElementsByTagName("script");
  for (const s of scripts) {
    if (s.src && /\/schema-explorer\/js\/app\.js(\?|$)/.test(s.src)) {
      return s.src.replace(/\/js\/app\.js.*$/, "/data");
    }
  }
  return "data";
}
const SCHEMA_BASE = inferSchemaBase();
const DEFAULT_RELEASE = "devel";
const RELEASE_PATTERN = /^[A-Za-z0-9._-]+$/;

function normalizeRelease(value) {
  const release = String(value || DEFAULT_RELEASE);
  if (RELEASE_PATTERN.test(release)) return release;
  throw new Error("Invalid schema release: " + escapeHtml(release));
}

function releaseParam(release) {
  return encodeURIComponent(release);
}

// SCHEMA_MODULES keys are the canonical module IDs stored in SQLite and used
// in URL hashes; `name` is the user-visible label rendered in the UI.
const SCHEMA_MODULES = {
  eos_designs: {
    name: "AVD Design",
    icon: "bi-diagram-3",
    description: "Fabric design data model — topology, addressing, network services, connected endpoints, and tenants.",
  },
  eos_cli_config_gen: {
    name: "EOS Config",
    icon: "bi-file-earmark-code",
    description: "Device configuration data model — interfaces, routing, ACLs, AAA, management, and platform settings.",
  },
};

const dbCache = new Map();    // release -> sql.js Database
let SQL = null;
const app = document.getElementById("app");

// ── boot ─────────────────────────────────────────────────────────────────────
//
// Two mount modes share this script:
//
//   * **Standalone**: a page declares `<main id="app">` + `<select id="release-select">`
//     (the SPA's own `index.html` at `/_assets/schema-explorer/index.html`).
//     Uses the URL hash for routing — landing / module / var-detail views.
//
//   * **Embed**: any docs page drops one or more `<schema-explorer>` custom
//     elements. Each embed is self-contained, scoped to a (release, module,
//     root) tuple via data attributes, and never touches `location.hash`.
//     Multiple embeds on the same page share `dbCache`.
//
// Both modes can coexist — embeds work even when `#app` is also present.

// CDN dependencies are lazy-loaded so docs pages that never host an embed
// do not pay for the extra script/font requests. Do not inject Bootstrap CSS
// here: it contains global element rules for headings, links, body line-height,
// etc. that leak into Material chrome. The standalone SPA owns the whole page
// and loads Bootstrap CSS directly from static/index.html.
const CDN_DEPS = {
  css: [
    {
      href: "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css",
      integrity: "sha384-XGjxtQfXaH2tnPFa9x+ruJTuLE3Aa6LhHSWRr1XeTyhezb4abCG4ccI5AkVDxqC+",
    },
  ],
  js: [
    {
      src: "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js",
      global: "bootstrap",
      integrity: "sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz",
    },
    {
      src: "https://cdn.jsdelivr.net/npm/sql.js@1.10.3/dist/sql-wasm.js",
      global: "initSqlJs",
      integrity: "sha384-8D3Rsfo535FqoC1pHCCQMrNf75UgzyoG/HQm9zOzITRrz3QKzecc2E7JXKGCXoWu",
    },
  ],
};

function _hasTagWithUrl(selector, attr, url) {
  for (const el of document.querySelectorAll(selector)) {
    if (el.getAttribute(attr) === url) return true;
  }
  return false;
}

function _loadCss(dep) {
  const href = typeof dep === "string" ? dep : dep.href;
  if (_hasTagWithUrl("link[rel='stylesheet']", "href", href)) return Promise.resolve();
  return new Promise((resolve, reject) => {
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = href;
    if (dep.integrity) {
      link.integrity = dep.integrity;
      link.crossOrigin = "anonymous";
    }
    link.onload = resolve;
    link.onerror = () => reject(new Error("Failed to load " + href));
    document.head.appendChild(link);
  });
}

function _globalExists(name) {
  return !name || typeof window[name] !== "undefined";
}

function _scriptWithUrl(src) {
  for (const el of document.querySelectorAll("script")) {
    if (el.src === src || el.getAttribute("src") === src) return el;
  }
  return null;
}

function _loadScript(dep) {
  const { src, global: globalName, integrity } = dep;
  if (_globalExists(globalName)) return Promise.resolve();

  const existing = _scriptWithUrl(src);
  if (existing?.dataset.schemaExplorerLoaded === "1" && !_globalExists(globalName)) {
    existing.remove();
  }

  return new Promise((resolve, reject) => {
    const script = _scriptWithUrl(src) || document.createElement("script");
    const finish = () => {
      script.dataset.schemaExplorerLoaded = "1";
      delete script.dataset.schemaExplorerLoading;
      if (_globalExists(globalName)) {
        resolve();
      } else {
        reject(new Error("Loaded " + src + ", but " + globalName + " is not defined. Check browser access to the CDN asset."));
      }
    };

    script.addEventListener("load", finish, { once: true });
    script.addEventListener("error", () => reject(new Error("Failed to load " + src)), { once: true });

    if (!script.dataset.schemaExplorerLoading) {
      script.dataset.schemaExplorerLoading = "1";
      script.src = src;
      script.async = false;
      if (integrity) {
        script.integrity = integrity;
        script.crossOrigin = "anonymous";
      }
      if (!script.parentNode) document.head.appendChild(script);
    }
  });
}

async function ensureDeps() {
  await Promise.all(CDN_DEPS.css.map(_loadCss));
  // Scripts must load in order — Bootstrap before sql.js doesn't strictly
  // matter, but doing them sequentially makes ordering predictable.
  for (const dep of CDN_DEPS.js) await _loadScript(dep);
}

async function ensureSqlJs() {
  if (SQL) return SQL;
  await ensureDeps();
  SQL = await window.initSqlJs({
    locateFile: f => `https://cdn.jsdelivr.net/npm/sql.js@1.10.3/dist/${f}`,
  });
  return SQL;
}

(async function boot() {
  const embeds = document.querySelectorAll("schema-explorer");
  const hasStandalone = !!app;
  if (!embeds.length && !hasStandalone) return;   // page doesn't host the explorer

  await ensureSqlJs();

  if (hasStandalone) {
    window.addEventListener("hashchange", route);
    const releaseSelect = document.getElementById("release-select");
    if (releaseSelect) {
      releaseSelect.addEventListener("change", e => {
        const path = location.hash.slice(1) || "/";
        location.hash = path + (path.includes("?") ? "&" : "?") + "release=" + encodeURIComponent(e.target.value);
      });
    }
    await route();
  }

  for (const el of embeds) {
    try { await mountEmbed(el); }
    catch (err) { failEmbed(el, err.message); }
  }
})().catch(err => {
  if (app) fail("Failed to initialise: " + err.message);
  document.querySelectorAll("schema-explorer").forEach(el => failEmbed(el, "Failed to initialise: " + err.message));
  console.error("Schema Explorer init failed:", err);
});

// Per-group tree visibility — a row is shown iff every ancestor along its
// parent_path chain has data-expanded="1". Used by the chevron handler and
// by the group-level Expand/Collapse all buttons.
function setTreeRowExpanded(row, expanded) {
  row.dataset.expanded = expanded ? "1" : "0";
  const icon = row.querySelector(".tree-toggle-icon");
  if (icon) {
    icon.classList.toggle("bi-chevron-right", !expanded);
    icon.classList.toggle("bi-chevron-down", expanded);
  }
}

function expandGroupRootRows(groupEl) {
  if (!groupEl) return;
  const rows = groupEl.querySelectorAll("tr.schema-tree-row");
  const byPath = new Map();
  for (const r of rows) byPath.set(r.dataset.rowId, r);
  for (const r of rows) {
    if (r.dataset.isBranch !== "1") continue;
    const parentId = r.dataset.parentId;
    if (!parentId || !byPath.has(parentId)) setTreeRowExpanded(r, true);
  }
}

function applyTreeVisibility(groupEl) {
  if (!groupEl) return;
  const rows = groupEl.querySelectorAll("tr.schema-tree-row");
  const byPath = new Map();
  const metadataByPath = new Map();
  for (const detailRow of groupEl.querySelectorAll("tr.schema-row-metadata")) {
    metadataByPath.set(detailRow.dataset.detailFor, detailRow);
  }
  for (const r of rows) byPath.set(r.dataset.rowId, r);
  for (const r of rows) {
    const depth = parseInt(r.dataset.depth, 10);
    let visible = true;
    if (depth !== 1) {
      let p = r.dataset.parentId;
      while (p) {
        const parentRow = byPath.get(p);
        if (!parentRow) break;
        if (parentRow.dataset.expanded !== "1") { visible = false; break; }
        p = parentRow.dataset.parentId;
      }
    }
    r.style.display = visible ? "" : "none";
    const detailRow = metadataByPath.get(r.dataset.rowId);
    if (detailRow) detailRow.style.display = visible && detailRow.dataset.open === "1" ? "" : "none";
  }
}

// Delegated handler for tree-row chevron clicks. Lives at document level so
// it survives every renderResults innerHTML refresh and works across multiple
// embed roots on the same page.
document.addEventListener("click", e => {
  const metadataToggle = e.target.closest(".schema-row-info-toggle");
  if (metadataToggle) {
    e.preventDefault();
    e.stopPropagation();
    const detailRow = document.getElementById(metadataToggle.dataset.detailTarget || "");
    if (!detailRow) return;
    const parentRow = metadataToggle.closest("tr");
    const open = detailRow.dataset.open !== "1";
    detailRow.dataset.open = open ? "1" : "0";
    detailRow.style.display = open && parentRow?.style.display !== "none" ? "" : "none";
    metadataToggle.setAttribute("aria-expanded", open ? "true" : "false");
    return;
  }

  const header = e.target.closest(".schema-group-header");
  if (header) {
    const groupEl = header.closest(".schema-group");
    expandGroupRootRows(groupEl);
    applyTreeVisibility(groupEl);
    return;
  }

  const toggle = e.target.closest("[data-tree-action='toggle-row'], .tree-toggle-icon");
  if (!toggle) return;
  e.preventDefault();
  e.stopPropagation();
  const row = toggle.closest("tr.schema-tree-row");
  if (!row) return;
  const groupEl = row.closest(".schema-group");
  const shouldExpand = row.dataset.expanded !== "1";
  setTreeRowExpanded(row, shouldExpand);
  applyTreeVisibility(groupEl);
});

// ── hash router ──────────────────────────────────────────────────────────────

function parseHash() {
  const raw = location.hash.slice(1) || "/";
  const [pathPart, queryPart] = raw.split("?");
  const params = new URLSearchParams(queryPart || "");
  // Decode each segment so a key_path like `aaa_accounting.commands.default[].commands`
  // (which sits in the URL as `aaa_accounting.commands.default%5B%5D.commands`)
  // matches the literal value stored in SQLite.
  const segments = pathPart.split("/").filter(Boolean).map(s => {
    try { return decodeURIComponent(s); } catch { return s; }
  });
  return { segments, params };
}

async function route() {
  const { segments, params } = parseHash();
  const release = normalizeRelease(params.get("release") || DEFAULT_RELEASE);
  const releaseSelect = document.getElementById("release-select");
  if (releaseSelect) releaseSelect.value = release;
  try {
    const db = await getDb(release);
    if (segments.length === 0)             return renderLanding(db, release);
    if (segments.length === 1)             return renderModule(db, release, segments[0], { view: params.get("view") || "" });
    return renderVarDetail(db, release, segments[0], segments.slice(1).join("/"));
  } catch (err) {
    fail(err.message);
  }
}

function fail(msg) {
  app.innerHTML = `<div class="alert alert-danger m-3"><i class="bi bi-exclamation-triangle me-2"></i>${escapeHtml(msg)}</div>`;
}

// ── sqlite loader ────────────────────────────────────────────────────────────

async function getDb(release) {
  if (dbCache.has(release)) return dbCache.get(release);
  if (app) {
    app.innerHTML = `<div class="text-center py-5 text-muted">
      <span class="spinner-border spinner-border-sm"></span>
      <span class="ms-2 small">Loading ${escapeHtml(release)} schema…</span>
    </div>`;
  }
  const url = `${SCHEMA_BASE}/${releaseParam(release)}/schema.sqlite`;
  // cache: "no-cache" forces a conditional GET so the browser revalidates
  // against the server's Last-Modified / ETag every page load. Keeps the
  // bytes cached locally when nothing changed (304), but picks up a freshly
  // regenerated SQLite immediately without a hard reload.
  const buf = await fetch(url, { cache: "no-cache" }).then(r => {
    if (!r.ok) throw new Error(`Could not load ${url} (${r.status})`);
    return r.arrayBuffer();
  });
  const db = new SQL.Database(new Uint8Array(buf));
  dbCache.set(release, db);
  return db;
}

// ── query helpers ────────────────────────────────────────────────────────────

function rows(db, sql, params = []) {
  const stmt = db.prepare(sql);
  stmt.bind(params);
  const out = [];
  while (stmt.step()) out.push(stmt.getAsObject());
  stmt.free();
  return out;
}

function getStats(db, release) {
  return rows(db, "SELECT module, var_count, loaded_at FROM schema_meta WHERE release = ?", [release]);
}

function getCategoryCounts(db, release, module) {
  if (module === "all") {
    return rows(db, "SELECT category, COUNT(*) AS count FROM schema_vars WHERE release = ? GROUP BY category ORDER BY category", [release]);
  }
  return rows(db, "SELECT category, COUNT(*) AS count FROM schema_vars WHERE release = ? AND module = ? GROUP BY category ORDER BY category", [release, module]);
}

function escapeSqlLike(value) {
  return String(value).replace(/[\\%_]/g, "\\$&");
}

const SEARCH_SCOPE_LABELS = {
  both: "Path + description",
  path: "Path",
  description: "Description",
};

function normalizeSearchScope(scope) {
  return Object.prototype.hasOwnProperty.call(SEARCH_SCOPE_LABELS, scope) ? scope : "both";
}

function searchScopeLabel(scope) {
  return SEARCH_SCOPE_LABELS[normalizeSearchScope(scope)];
}

function searchVars(db, release, module, opts = {}) {
  const conds = ["release = ?"];
  const ps = [release];
  if (module !== "all") { conds.push("module = ?"); ps.push(module); }
  if (opts.rootModule && module === "all") { conds.push("module = ?"); ps.push(opts.rootModule); }
  if (opts.root) {
    const escapedRoot = escapeSqlLike(opts.root);
    conds.push("(key_path = ? OR key_path LIKE ? ESCAPE '\\' OR key_path LIKE ? ESCAPE '\\')");
    ps.push(opts.root, `${escapedRoot}.%`, `${escapedRoot}[]%`);
  }
  if (opts.q) {
    const pattern = `%${opts.q}%`;
    const searchScope = normalizeSearchScope(opts.searchScope);
    if (searchScope === "path") {
      conds.push("key_path LIKE ?");
      ps.push(pattern);
    } else if (searchScope === "description") {
      conds.push("description LIKE ?");
      ps.push(pattern);
    } else {
      conds.push("(key_path LIKE ? OR description LIKE ?)");
      ps.push(pattern, pattern);
    }
  }
  if (opts.category) { conds.push("category = ?"); ps.push(opts.category); }
  if (opts.docTable) { conds.push("doc_table = ?"); ps.push(opts.docTable); }
  const orderBy = opts.order === "id" ? "id" : "key_path";
  const sql = `SELECT * FROM schema_vars WHERE ${conds.join(" AND ")} ORDER BY ${orderBy} LIMIT ${opts.limit || 500}`;
  return rows(db, sql, ps);
}

function getDocTableCounts(db, release, module) {
  if (module === "all") {
    return rows(db, "SELECT doc_table, COUNT(*) AS count FROM schema_vars WHERE release = ? GROUP BY doc_table ORDER BY doc_table", [release]);
  }
  return rows(db, "SELECT doc_table, COUNT(*) AS count FROM schema_vars WHERE release = ? AND module = ? GROUP BY doc_table ORDER BY doc_table", [release, module]);
}

function getRootOptions(db, release, module) {
  const conds = ["release = ?", "depth = 1"];
  const ps = [release];
  if (module !== "all") { conds.push("module = ?"); ps.push(module); }
  return rows(db, `SELECT module, key_path FROM schema_vars WHERE ${conds.join(" AND ")} ORDER BY module, key_path`, ps);
}

function rootOptionValue(row, module) {
  return module === "all" ? `${row.module}:${row.key_path}` : row.key_path;
}

function parseRootSelection(value, module) {
  if (!value) return { root: "", rootModule: "" };
  if (module !== "all") return { root: value, rootModule: module };
  const idx = value.indexOf(":");
  if (idx < 0) return { root: value, rootModule: "" };
  return { rootModule: value.slice(0, idx), root: value.slice(idx + 1) };
}

function defaultRootState(rootOptions, defaultRoot, module) {
  if (!defaultRoot) return { root: "", rootModule: "", selection: "" };
  if (module !== "all") return { root: defaultRoot, rootModule: module, selection: defaultRoot };
  const parsed = parseRootSelection(defaultRoot, module);
  if (parsed.rootModule) return { ...parsed, selection: defaultRoot };
  const match = rootOptions.find(row => row.key_path === defaultRoot);
  if (!match) return { root: defaultRoot, rootModule: "", selection: defaultRoot };
  return { root: match.key_path, rootModule: match.module, selection: rootOptionValue(match, module) };
}

function isFilterActive(state) {
  return !!(state.root || state.q || state.category || state.docTable);
}

function lifecycleBadge(v) {
  if (v.removed) return `<span class="badge bg-danger">removed</span>`;
  if (v.deprecated) return `<span class="badge bg-warning text-dark">deprecated</span>`;
  return `<span class="badge bg-light text-dark border">${escapeHtml(v.var_type || "-")}</span>`;
}

function requiredMarker(row) {
  return row.required ? `<span class="text-success" title="Required"><i class="bi bi-check-circle-fill"></i></span>` : `<span class="text-muted">-</span>`;
}

function constraintsSummary(row) {
  const constraints = yamlConstraints(row);
  const parts = yamlRestrictionParts(row, constraints);
  if (!parts.length) return `<span class="text-muted">-</span>`;
  return `<span class="schema-constraints-summary" title="${escapeAttr(parts.join("; "))}">${escapeHtml(parts.slice(0, 2).join("; "))}${parts.length > 2 ? "..." : ""}</span>`;
}

function rowHasMetadata(row) {
  const constraints = yamlRestrictionParts(row, yamlConstraints(row));
  return !!(row.default_value || constraints.length || row.category || row.doc_table || row.deprecated || row.removed || row.cross_ref);
}

function rowMetadataButton(row, detailId) {
  if (!rowHasMetadata(row)) return "";
  return `<button type="button" class="schema-row-info-toggle" data-detail-target="${escapeAttr(detailId)}" title="Show key metadata"><i class="bi bi-info-circle"></i></button>`;
}

function renderRowMetadata(row, release, visibleColumns, detailId) {
  if (!rowHasMetadata(row)) return "";
  const constraints = yamlRestrictionParts(row, yamlConstraints(row));
  const lifecycle = row.removed
    ? `<span class="badge bg-danger">removed</span>`
    : row.deprecated
      ? `<span class="badge bg-warning text-dark">deprecated</span>`
      : `<span class="text-muted">active</span>`;
  return `
    <tr class="schema-row-metadata" id="${escapeAttr(detailId)}" data-detail-for="${escapeAttr(treeRowId(row, row.module))}" data-open="0" style="display: none;">
      <td colspan="${visibleColumns}">
        <div class="schema-row-metadata-panel">
          <div><span class="schema-meta-label">Default</span>${renderDefaultValue(row.default_value, { compact: true })}</div>
          <div><span class="schema-meta-label">Valid / constraints</span>${constraints.length ? escapeHtml(constraints.join("; ")) : `<span class="text-muted">-</span>`}</div>
          <div><span class="schema-meta-label">Category</span>${row.category ? `<span class="badge schema-category-badge">${escapeHtml(row.category)}</span>` : `<span class="text-muted">-</span>`}</div>
          <div><span class="schema-meta-label">Doc table</span>${row.doc_table ? `<span class="badge schema-category-badge">${escapeHtml(row.doc_table)}</span>` : `<span class="text-muted">-</span>`}</div>
          <div><span class="schema-meta-label">Lifecycle</span>${lifecycle}</div>
          ${row.cross_ref ? `<div><span class="schema-meta-label">Cross-schema</span>${renderCrossRefRow(row.cross_ref, release).replace(/^<tr><td[^>]*>Cross-schema<\/td><td>|<\/td><\/tr>$/g, "")}</div>` : ""}
        </div>
      </td>
    </tr>`;
}

function treeKeyControl(row, release, module, state, isBranch, leaf, indent, initiallyExpanded) {
  const link = `#/${module}/${encodeURI(row.key_path)}?release=${releaseParam(release)}`;
  const chevron = isBranch
    ? `<i class="bi ${initiallyExpanded ? "bi-chevron-down" : "bi-chevron-right"} tree-toggle-icon"></i>`
    : `<span class="tree-toggle-spacer"></span>`;
  const keyHtml = `<code class="schema-key-code fw-bold" style="font-size: 0.82rem;">${highlight(leaf, state.q)}</code>`;
  const detailsLink = `<a href="${link}" class="schema-row-detail-link link-brand text-decoration-none" title="Open details for ${escapeAttr(row.key_path)}"><i class="bi bi-box-arrow-up-right"></i></a>`;
  if (isBranch) {
    return `
      <span class="schema-tree-indent" style="padding-left: ${indent}rem;">
        ${chevron}
        <button type="button" class="schema-key-toggle link-brand" data-tree-action="toggle-row" title="${escapeAttr(row.key_path)}">${keyHtml}</button>
        ${detailsLink}
      </span>`;
  }
  return `
    <span class="schema-tree-indent" style="padding-left: ${indent}rem;">
      ${chevron}
      <a href="${link}" class="link-brand text-decoration-none" title="${escapeAttr(row.key_path)}">${keyHtml}</a>
    </span>`;
}

function getVar(db, release, module, key_path) {
  const r = rows(db, "SELECT * FROM schema_vars WHERE release = ? AND module = ? AND key_path = ?", [release, module, key_path]);
  return r[0] || null;
}

function getChildren(db, release, module, parent_path) {
  return rows(db, "SELECT * FROM schema_vars WHERE release = ? AND module = ? AND parent_path = ? ORDER BY key_path", [release, module, parent_path]);
}

function getSiblings(db, release, module, parent_path, exclude_key) {
  return rows(db, "SELECT key_path, var_type FROM schema_vars WHERE release = ? AND module = ? AND parent_path = ? AND key_path != ? ORDER BY key_path", [release, module, parent_path, exclude_key]);
}

function getDescendants(db, release, module, key_path) {
  const escapedPath = escapeSqlLike(key_path);
  return rows(
    db,
    "SELECT * FROM schema_vars WHERE release = ? AND module = ? AND (key_path LIKE ? ESCAPE '\\' OR key_path LIKE ? ESCAPE '\\') ORDER BY id LIMIT 2000",
    [release, module, `${escapedPath}.%`, `${escapedPath}[]%`],
  );
}

// ── views ────────────────────────────────────────────────────────────────────

function renderLanding(db, release) {
  const stats = Object.fromEntries(getStats(db, release).map(s => [s.module, s]));
  const cards = Object.entries(SCHEMA_MODULES).map(([id, mod]) => {
    const s = stats[id] || {};
    const count = s.var_count || 0;
    return `
      <div class="col">
        <a href="#/${id}?release=${releaseParam(release)}" class="text-decoration-none d-block h-100">
          <div class="card h-100 border-0 shadow-sm module-card">
            <div class="card-body d-flex flex-column">
              <div class="d-flex align-items-start mb-2">
                <span class="fs-3 me-2 brand-color"><i class="bi ${mod.icon}"></i></span>
                <div class="me-auto">
                  <h6 class="mb-0 fw-semibold">${escapeHtml(mod.name)}</h6>
                  <div class="text-muted" style="font-size:0.7rem;"><code>${id}</code></div>
                  <span class="badge mt-1" style="background-color:#198754; font-size:0.65rem;">${count} variables</span>
                </div>
              </div>
              <p class="text-muted small mb-0">${escapeHtml(mod.description)}</p>
            </div>
          </div>
        </a>
      </div>`;
  }).join("");

  app.innerHTML = `
    <div class="d-flex align-items-center mb-3">
      <h4 class="fw-bold mb-0 brand-color"><i class="bi bi-search me-2"></i>Schema Explorer</h4>
      <span class="badge ms-2" style="background-color: #16325B;">aristanetworks/avd</span>
    </div>
    <p class="text-muted small mb-3">
      Browse the AVD data model schemas. Select a module to explore variables, search by key path, and view detailed documentation.
    </p>
    <div class="row row-cols-1 row-cols-md-2 g-3 mb-4">${cards}</div>
    <div class="row mb-4"><div class="col">
      <a href="#/all?release=${releaseParam(release)}" class="text-decoration-none d-block">
        <div class="card border-0 shadow-sm module-card">
          <div class="card-body d-flex align-items-center">
            <span class="fs-3 me-3 brand-color"><i class="bi bi-search"></i></span>
            <div>
              <h6 class="mb-0 fw-semibold">Search All Modules</h6>
              <p class="text-muted small mb-0">Search across both AVD Design and EOS Config schemas</p>
            </div>
          </div>
        </div>
      </a>
    </div></div>`;
}

function renderModule(db, release, module, options = {}) {
  const host = options.target || app;
  const embedded = !!options.embed;
  const defaultRoot = options.root || "";
  const initialView = ["tree", "flat", "yaml", "docs"].includes(options.view) ? options.view : "tree";
  const chrome = options.chrome || "compact";
  const isAll = module === "all";
  if (!isAll && !SCHEMA_MODULES[module]) {
    host.innerHTML = `<div class="alert alert-danger m-3"><i class="bi bi-exclamation-triangle me-2"></i>Module not found: ${escapeHtml(module)}</div>`;
    return;
  }

  const stats = getStats(db, release);
  const moduleStats = isAll
    ? { var_count: stats.reduce((sum, item) => sum + item.var_count, 0) }
    : stats.find(item => item.module === module) || {};
  const info = isAll
    ? { name: "All Modules", icon: "bi-search", description: "Search across both AVD Design and EOS Config schemas." }
    : SCHEMA_MODULES[module];

  const total = moduleStats.var_count || 0;
  const headerHtml = chrome === "none" ? "" : `
    <div class="d-flex align-items-center mb-3 schema-browser-heading">
      ${embedded ? "" : `<a href="#/?release=${releaseParam(release)}" class="link-brand me-3"><i class="bi bi-arrow-left fs-4"></i></a>`}
      <div>
        <h4 class="mb-1 fw-bold brand-color"><i class="bi ${info.icon} me-2"></i>${escapeHtml(info.name)}${isAll ? "" : ` <small class="text-muted fw-normal" style="font-size:0.6em;"><code>${escapeHtml(module)}</code></small>`}</h4>
        ${total ? `<span class="badge" style="background-color:#198754; font-size:0.65rem;">${total} variables</span>` : ""}
      </div>
    </div>
    <p class="text-muted small mb-3">${escapeHtml(info.description)}</p>`;

  host.innerHTML = `
    ${headerHtml}
    <form id="filter-form" class="mb-3 schema-filter-sticky" onsubmit="return false">
      <div class="d-flex flex-wrap align-items-start gap-3">
        <div class="flex-grow-1 schema-filter-field">
          <label class="schema-filter-label" for="q">Search</label>
          <div class="input-group input-group-sm">
            <span class="input-group-text"><i class="bi bi-search"></i></span>
            <input type="search" class="form-control schema-search-input" id="q" placeholder="Search key paths or descriptions...">
            <select class="form-control schema-search-scope" id="search-scope" aria-label="Search scope">
              <option value="both" selected>Both</option>
              <option value="path">Path</option>
              <option value="description">Description</option>
            </select>
          </div>
          <div class="schema-view-mode-row">
            <div class="btn-group btn-group-sm" role="group" aria-label="View mode">
              <button type="button" class="btn btn-outline-secondary schema-view-mode-button" id="btn-view-tree">Tree</button>
              <button type="button" class="btn btn-outline-secondary schema-view-mode-button" id="btn-view-flat">Table</button>
              <button type="button" class="btn btn-outline-secondary schema-view-mode-button" id="btn-view-yaml">YAML</button>
              <button type="button" class="btn btn-outline-secondary schema-view-mode-button" id="btn-view-docs">Docs</button>
            </div>
          </div>
        </div>
      </div>
      <div class="schema-active-filters mt-2 small text-muted" id="active-filters"></div>
    </form>

    <div class="schema-module-layout">
      <div class="card border-0 shadow-sm schema-results-card"><div id="results"></div></div>
    </div>`;

  const state = {
    q: "",
    root: "",
    defaultRoot: "",
    defaultRootSelection: "",
    rootModule: "",
    category: "",
    docTable: "",
    searchScope: "both",
    view: initialView,
    target: host.querySelector("#results"),
  };
  const refresh = debounce(() => renderResults(db, release, module, state), 250);

  const qInput = host.querySelector("#q");
  const scopeInput = host.querySelector("#search-scope");
  const activeFilters = host.querySelector("#active-filters");
  function updateActiveFilters() {
    const filters = [];
    if (state.q) filters.push(`Search (${escapeHtml(searchScopeLabel(state.searchScope))}): <code>${escapeHtml(state.q)}</code>`);
    if (state.category) filters.push(`Category: <code>${escapeHtml(state.category)}</code>`);
    if (state.docTable) filters.push(`Table: <code>${escapeHtml(state.docTable)}</code>`);
    activeFilters.innerHTML = filters.length ? filters.join(" <span class=\"mx-1\">|</span> ") : "No filters applied";
  }

  qInput.addEventListener("input", e => { state.q = e.target.value.trim(); updateActiveFilters(); refresh(); });
  scopeInput.addEventListener("change", e => {
    state.searchScope = normalizeSearchScope(e.target.value);
    updateActiveFilters();
    renderResults(db, release, module, state);
  });
  const viewButtons = {
    tree: host.querySelector("#btn-view-tree"),
    flat: host.querySelector("#btn-view-flat"),
    yaml: host.querySelector("#btn-view-yaml"),
    docs: host.querySelector("#btn-view-docs"),
  };
  function setViewMode(view) {
    state.view = view;
    for (const [mode, button] of Object.entries(viewButtons)) button.classList.toggle("active", mode === view);
    renderResults(db, release, module, state);
  }
  viewButtons.tree.addEventListener("click", () => setViewMode("tree"));
  viewButtons.flat.addEventListener("click", () => setViewMode("flat"));
  viewButtons.yaml.addEventListener("click", () => setViewMode("yaml"));
  viewButtons.docs.addEventListener("click", () => setViewMode("docs"));

  updateActiveFilters();
  setViewMode(initialView);
}

function renderResults(db, release, module, state) {
  const target = state.target || document.getElementById("results");
  // Tree and YAML views need every row in the active scope so the hierarchy is
  // complete — anything dropped at the SQL boundary disappears from the output
  // entirely (eos_cli_config_gen has 6.4k rows; "all modules" hits ~12.6k).
  // Flat list view caps at 500 since users only consume the head visibly.
  const hierarchical = state.view === "tree" || state.view === "yaml" || state.view === "docs";
  const limit = hierarchical ? 20000 : 500;
  const results = state.rows || searchVars(db, release, module, { ...state, limit, order: state.view === "yaml" ? "id" : "key_path" });
  if (!results.length) {
    target.innerHTML = `<div class="text-center py-5 text-muted"><i class="bi bi-inbox fs-3 d-block mb-2"></i><span class="small">No variables match.</span></div>`;
    return;
  }
  if (state.view === "tree") return renderTreeResults(target, db, release, module, state, results);
  if (state.view === "yaml") return renderYamlResults(target, module, results);
  if (state.view === "docs") return renderDocsResults(target, release, module, state, results);
  const isAll = module === "all";
  if (state.embedCompact) {
    const flatColumns = isAll ? `<col style="width: 9rem;"><col style="width: 30%;"><col>` : `<col style="width: 34%;"><col>`;
    const rowsHtml = results.map(v => {
      const mod = isAll ? v.module : module;
      const link = `#/${mod}/${encodeURI(v.key_path)}?release=${releaseParam(release)}`;
      const modBadge = isAll ? `<td><span class="badge ${v.module === "eos_designs" ? "bg-primary" : "bg-success"}">${escapeHtml(SCHEMA_MODULES[v.module]?.name || v.module)}</span></td>` : "";
      return `
        <tr>
          ${modBadge}
          <td class="px-3"><a href="${link}" class="link-brand text-decoration-none"><code class="schema-key-code fw-bold" style="font-size: 0.82rem;">${highlight(displayPath(v.key_path), state.q)}</code></a></td>
          <td class="schema-description-text text-muted small">${formatMarkdownInline(v.description || "-", state.q)}</td>
        </tr>`;
    }).join("");
    target.innerHTML = `
      <div class="schema-results-toolbar card-header bg-light text-muted small">${results.length} variable${results.length === 1 ? "" : "s"} ${results.length >= 500 ? "(showing first 500)" : "found"}</div>
      <div class="schema-results-scroll">
        <div class="table-responsive">
        <table class="table table-sm table-hover align-middle mb-0" style="table-layout: fixed; width: 100%;">
          <colgroup>${flatColumns}</colgroup>
          <thead class="table-light"><tr>
            ${isAll ? `<th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Module</th>` : ""}
            <th class="text-muted small text-uppercase px-3" style="font-size: 0.72rem;">Key Path</th>
            <th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Description</th>
          </tr></thead>
          <tbody>${rowsHtml}</tbody>
        </table>
        </div>
      </div>`;
    return;
  }
  const visibleColumns = isAll ? 5 : 4;
  const rowsHtml = results.map(v => {
    const mod = isAll ? v.module : module;
    const link = `#/${mod}/${encodeURI(v.key_path)}?release=${releaseParam(release)}`;
    const detailId = `m${++_treeRenderSeq}`;
    const modBadge = isAll ? `<td data-label="Module"><span class="badge ${v.module === "eos_designs" ? "bg-primary" : "bg-success"}">${escapeHtml(SCHEMA_MODULES[v.module]?.name || v.module)}</span></td>` : "";
    return `
      <tr>
        ${modBadge}
        <td class="schema-key-cell px-3" data-label="Key"><a href="${link}" class="link-brand text-decoration-none"><code class="schema-key-code fw-bold" style="font-size: 0.82rem;">${highlight(displayPath(v.key_path), state.q)}</code></a></td>
        <td class="schema-type-cell" data-label="Type">${lifecycleBadge(v)}</td>
        <td class="schema-required-cell text-center" data-label="Req">${requiredMarker(v)}</td>
        <td class="schema-description-text text-muted small" data-label="Description"><div class="schema-description-cell">${rowMetadataButton(v, detailId)}<span>${formatMarkdownInline(v.description || "-", state.q)}</span></div></td>
      </tr>${renderRowMetadata(v, release, visibleColumns, detailId)}`;
  }).join("");
  target.innerHTML = `
    <div class="schema-results-toolbar card-header bg-light text-muted small">${results.length} variable${results.length === 1 ? "" : "s"} ${results.length >= 500 ? "(showing first 500)" : "found"}</div>
    <div class="schema-results-scroll">
      <div class="table-responsive">
      <table class="table table-sm table-hover align-middle mb-0 schema-var-table schema-flat-table">
        <colgroup>
          ${isAll ? `<col class="schema-col-module">` : ""}
          <col class="schema-col-key"><col class="schema-col-type"><col class="schema-col-required"><col class="schema-col-description">
        </colgroup>
        <thead class="table-light"><tr>
          ${isAll ? `<th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Module</th>` : ""}
          <th class="text-muted small text-uppercase px-3" style="font-size: 0.72rem;">Key</th>
          <th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Type</th>
          <th class="text-muted small text-uppercase text-center" style="font-size: 0.72rem;">Req</th>
          <th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Description</th>
        </tr></thead>
        <tbody>${rowsHtml}</tbody>
      </table>
      </div>
    </div>`;
}

let _treeRenderSeq = 0;

function renderTreeResults(target, db, release, module, state, matches) {
  const isAll = module === "all";
  const filtered = isFilterActive(state);
  const idPrefix = `t${++_treeRenderSeq}`;

  // When a filter is active, walk parent chains via the parent_path column
  // and emit ancestor rows (tagged is_context) so the hierarchical structure
  // stays intact. Fetched in batched DB queries — the previous "load up to
  // 5000 vars and filter in JS" approach silently dropped any group whose
  // root sorts past the 5000th alphabetical key (e.g. `vlan_interfaces` in
  // eos_cli_config_gen).
  let rowsForGroups;
  if (filtered && matches.length) {
    const knownByPath = new Map(matches.map(v => [treeRowId(v, module), v]));
    const ancestorRows = [];
    let toFetch = [];
    for (const v of matches) {
      const fetchModule = rowModule(v, module);
      for (const keyPath of parentPathCandidates(v)) {
        if (!knownByPath.has(`${fetchModule}:${keyPath}`)) toFetch.push({ module: fetchModule, keyPath });
      }
    }
    toFetch = [...new Map(toFetch.map(v => [`${v.module}:${v.keyPath}`, v])).values()];
    while (toFetch.length) {
      const fetched = [];
      const fetchByModule = new Map();
      for (const item of toFetch) {
        if (!fetchByModule.has(item.module)) fetchByModule.set(item.module, []);
        fetchByModule.get(item.module).push(item.keyPath);
      }
      for (const [fetchModule, keyPaths] of fetchByModule.entries()) {
        const placeholders = keyPaths.map(() => "?").join(",");
        fetched.push(...rows(db, `SELECT * FROM schema_vars WHERE release = ? AND module = ? AND key_path IN (${placeholders})`, [release, fetchModule, ...keyPaths]));
      }
      ancestorRows.push(...fetched);
      const next = [];
      for (const a of fetched) {
        knownByPath.set(treeRowId(a, module), a);
        const fetchModule = rowModule(a, module);
        for (const keyPath of parentPathCandidates(a)) {
          if (!knownByPath.has(`${fetchModule}:${keyPath}`)) next.push({ module: fetchModule, keyPath });
        }
      }
      toFetch = [...new Map(next.map(v => [`${v.module}:${v.keyPath}`, v])).values()];
    }
    rowsForGroups = [
      ...matches.map(v => ({ ...v, is_context: false })),
      ...ancestorRows.map(v => ({ ...v, is_context: true })),
    ];
  } else {
    rowsForGroups = matches.map(v => ({ ...v, is_context: false }));
  }

  const groups = new Map();
  const matchCounts = new Map();
  for (const v of rowsForGroups) {
    const groupId = treeGroupId(v, module);
    const root = rootSegment(v.key_path);
    if (!groups.has(groupId)) groups.set(groupId, { root, module: rowModule(v, module), vars: [] });
    groups.get(groupId).vars.push(v);
    if (!v.is_context) matchCounts.set(groupId, (matchCounts.get(groupId) || 0) + 1);
  }
  const sorted = [...groups.entries()].sort(([, a], [, b]) => `${a.module}:${a.root}`.localeCompare(`${b.module}:${b.root}`));
  const total = matches.length;
  const visibleColumns = isAll ? 5 : 4;

  const groupRowsHtml = sorted.map(([groupId, group], idx) => {
    const tree = orderedTreeRows(group.vars, module);
    const { childCount, parentIds } = tree;

    const rootDepth = state.root ? splitKeyPath(state.root).length : 1;
    return tree.rows.map(v => {
      const mod = isAll ? v.module : module;
      const leaf = state.root && v.key_path === state.root ? displayPath(v.key_path) : leafSegment(v.key_path);
      const depth = Math.max(1, (v.depth || 1) - (state.root ? rootDepth - 1 : 0));
      const indent = (depth - 1) * 1.25;
      const modBadge = isAll ? `<td data-label="Module"><span class="badge ${v.module === "eos_designs" ? "bg-primary" : "bg-success"}">${escapeHtml(SCHEMA_MODULES[v.module]?.name || v.module)}</span></td>` : "";
      const rowId = treeRowId(v, module);
      const parentId = parentIds.get(rowId) || "";
      const isBranch = (childCount.get(rowId) || 0) > 0;
      const isNestedRoot = !parentId;
      const initiallyExpanded = v.is_context || (state.root && (v.key_path === state.root || isNestedRoot));
      const styleAttr = v.is_context
        ? ` style="opacity: 0.55;"`
        : (depth > 1 && !isNestedRoot ? ` style="display: none;"` : "");
      const groupStartAttr = isNestedRoot ? ` data-group-start="1"` : "";

      if (state.embedCompact) {
        const link = `#/${mod}/${encodeURI(v.key_path)}?release=${releaseParam(release)}`;
        const chevron = isBranch
          ? `<i class="bi ${initiallyExpanded ? "bi-chevron-down" : "bi-chevron-right"} tree-toggle-icon"></i>`
          : `<span class="tree-toggle-spacer"></span>`;
        return `
          <tr class="schema-tree-row${v.is_context ? " schema-row-context" : ""}"
              data-row-id="${escapeAttr(rowId)}"
              data-parent-id="${escapeAttr(parentId)}"
              data-is-branch="${isBranch ? "1" : "0"}"
              data-depth="${depth}"
              data-expanded="${initiallyExpanded ? "1" : "0"}"${groupStartAttr}${styleAttr}>
            ${modBadge}
            <td class="schema-key-cell px-3" data-label="Key">
              <span class="schema-tree-indent" style="padding-left: ${indent}rem;">${chevron}<a href="${link}" class="link-brand text-decoration-none" title="${escapeAttr(v.key_path)}"><code class="schema-key-code fw-bold" style="font-size: 0.82rem;">${highlight(leaf, state.q)}</code></a></span>
            </td>
            <td class="schema-type-cell" data-label="Type">${lifecycleBadge(v)}</td>
            <td class="schema-required-cell text-center" data-label="Req">${requiredMarker(v)}</td>
            <td class="schema-description-text text-muted small" data-label="Description">${formatMarkdownInline(v.description || "-", state.q)}</td>
          </tr>`;
      }

      const detailId = `m${++_treeRenderSeq}`;
      return `
        <tr class="schema-tree-row${v.is_context ? " schema-row-context" : ""}"
            data-row-id="${escapeAttr(rowId)}"
            data-parent-id="${escapeAttr(parentId)}"
            data-is-branch="${isBranch ? "1" : "0"}"
            data-depth="${depth}"
            data-expanded="${initiallyExpanded ? "1" : "0"}"${groupStartAttr}${styleAttr}>
          ${modBadge}
          <td class="schema-key-cell px-3" data-label="Key">${treeKeyControl(v, release, mod, state, isBranch, leaf, indent, initiallyExpanded)}</td>
          <td class="schema-type-cell" data-label="Type">${lifecycleBadge(v)}</td>
          <td class="schema-required-cell text-center" data-label="Req">${requiredMarker(v)}</td>
          <td class="schema-description-text text-muted small" data-label="Description"><div class="schema-description-cell">${rowMetadataButton(v, detailId)}<span>${formatMarkdownInline(v.description || "-", state.q)}</span></div></td>
        </tr>${renderRowMetadata(v, release, visibleColumns, detailId)}`;
    }).join("");
  }).join("");

  const tableClass = state.embedCompact ? "schema-embed-table" : "schema-tree-table";
  const tableHtml = `
    <div class="table-responsive">
      <table class="table table-sm table-hover align-middle mb-0 schema-var-table ${tableClass}">
        <colgroup>
          ${isAll ? `<col class="schema-col-module">` : ""}
          <col class="schema-col-key"><col class="schema-col-type"><col class="schema-col-required"><col class="schema-col-description">
        </colgroup>
        <thead class="table-light"><tr>
          ${isAll ? `<th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Module</th>` : ""}
          <th class="text-muted small text-uppercase px-3" style="font-size: 0.72rem;">Key</th>
          <th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Type</th>
          <th class="text-muted small text-uppercase text-center" style="font-size: 0.72rem;">Req</th>
          <th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Description</th>
        </tr></thead>
        <tbody>${groupRowsHtml}</tbody>
      </table>
    </div>`;

  target.innerHTML = `
    <div class="schema-results-toolbar card-header bg-light d-flex align-items-center justify-content-between">
      <span class="text-muted small">${total} variable${total === 1 ? "" : "s"} in ${sorted.length} group${sorted.length === 1 ? "" : "s"}</span>
      <div>
        <button type="button" class="btn btn-sm btn-link text-muted p-0 me-2" data-tree-action="expand-all"><i class="bi bi-arrows-expand"></i> <span class="small">Expand all</span></button>
        <button type="button" class="btn btn-sm btn-link text-muted p-0" data-tree-action="collapse-all"><i class="bi bi-arrows-collapse"></i> <span class="small">Collapse all</span></button>
      </div>
    </div>
    <div class="schema-results-scroll">
      <div class="schema-group schema-root-table" data-group-id="${idPrefix}-all">${tableHtml}</div>
    </div>`;

  target.querySelectorAll(".schema-group").forEach(group => {
    if (state.root) expandGroupRootRows(group);
    applyTreeVisibility(group);
  });

  function setAllTreeRows(expanded) {
    target.querySelectorAll("tr.schema-tree-row").forEach(r => {
      if (r.dataset.isBranch === "1") {
        r.dataset.expanded = expanded ? "1" : "0";
        const icon = r.querySelector(".tree-toggle-icon");
        if (icon) {
          icon.classList.toggle("bi-chevron-right", !expanded);
          icon.classList.toggle("bi-chevron-down", expanded);
        }
      }
    });
    target.querySelectorAll(".schema-group").forEach(applyTreeVisibility);
  }

  target.querySelector("[data-tree-action='expand-all']")?.addEventListener("click", () => setAllTreeRows(true));
  target.querySelector("[data-tree-action='collapse-all']")?.addEventListener("click", () => setAllTreeRows(false));
}

function renderDetailChildrenTree(release, module, rootPath, children, descendants) {
  const childRows = [...children, ...descendants].filter((row, index, arr) => arr.findIndex(item => item.key_path === row.key_path) === index);
  const tree = orderedTreeRows(childRows, module);
  const { childCount, parentIds } = tree;

  const rowsHtml = tree.rows.map(row => {
    const rowId = treeRowId(row, module);
    const parentId = parentIds.get(rowId) || "";
    const depth = Math.max(1, (row.depth || 1) - splitKeyPath(rootPath).length);
    const indent = (depth - 1) * 1.25;
    const isBranch = (childCount.get(rowId) || 0) > 0;
    const isNestedRoot = !parentId;
    const initiallyExpanded = isNestedRoot;
    const chevron = isBranch
      ? `<i class="bi ${initiallyExpanded ? "bi-chevron-down" : "bi-chevron-right"} tree-toggle-icon" style="cursor: pointer; width: 1rem; display: inline-block; margin-right: 0.15rem;"></i>`
      : `<span style="display: inline-block; width: 1.15rem;"></span>`;
    const styleAttr = depth > 1 && !isNestedRoot ? ` style="display: none;"` : "";
    return `
      <tr class="schema-tree-row"
          data-row-id="${escapeAttr(rowId)}"
          data-parent-id="${escapeAttr(parentId)}"
          data-is-branch="${isBranch ? "1" : "0"}"
          data-depth="${depth}"
          data-expanded="${initiallyExpanded ? "1" : "0"}"${styleAttr}>
        <td class="px-3">
          <span class="schema-tree-indent" style="padding-left: ${indent}rem;">${chevron}<a href="#/${module}/${encodeURI(row.key_path)}?release=${releaseParam(release)}" class="link-brand text-decoration-none" title="${escapeAttr(row.key_path)}"><code class="schema-key-code fw-bold" style="font-size:0.82rem;">${escapeHtml(leafSegment(row.key_path))}</code></a></span>
        </td>
        <td>${lifecycleBadge(row)}</td>
        <td class="text-center">${row.required ? `<i class="bi bi-check-circle-fill text-success"></i>` : ""}</td>
        <td class="schema-description-text text-muted small">${formatMarkdownInline(row.description || "-")}</td>
      </tr>`;
  }).join("");

  return `
    <h5 class="fw-bold brand-color mb-2"><i class="bi bi-diagram-2 me-2"></i>Child Variables
      <span class="badge bg-secondary ms-1" style="font-size: 0.65rem; vertical-align: middle;">${childRows.length}</span>
    </h5>
    <div class="card border-0 shadow-sm mb-4 schema-detail-children">
      <div class="table-responsive">
        <table class="table table-sm table-hover align-middle mb-0" style="table-layout: fixed; width: 100%;">
          <colgroup>
            <col style="width: 32%;">
            <col style="width: 8rem;">
            <col style="width: 4rem;">
            <col>
          </colgroup>
          <thead class="table-light"><tr>
            <th class="text-muted small text-uppercase px-3" style="font-size: 0.72rem;">Key</th>
            <th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Type</th>
            <th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Req</th>
            <th class="text-muted small text-uppercase" style="font-size: 0.72rem;">Description</th>
          </tr></thead>
          <tbody>${rowsHtml}</tbody>
        </table>
      </div>
    </div>`;
}

function renderVarDetail(db, release, module, key_path) {
  if (!SCHEMA_MODULES[module]) return fail(`Module not found: ${module}`);
  const v = getVar(db, release, module, key_path);
  if (!v) return fail(`Variable not found: ${module}/${key_path}`);

  const constraints = v.constraints ? JSON.parse(v.constraints) : {};
  const children = getChildren(db, release, module, key_path);
  const dynamicSource = dynamicKeySource(v.key_path);

  const validValuesHtml = constraints.valid_values ? `
    <h5 class="fw-bold brand-color mb-2"><i class="bi bi-list-check me-2"></i>Valid Values</h5>
    <div class="card border-0 shadow-sm mb-4"><div class="card-body p-0">
      ${constraints.valid_values.map((val, i, arr) => `
        <div class="d-flex align-items-start px-3 py-2 ${i < arr.length - 1 ? "border-bottom" : ""}">
          <div class="me-3" style="min-width: 3.5rem;"><code class="schema-valid-value">${escapeHtml(String(val))}</code></div>
        </div>`).join("")}
    </div></div>` : "";

  const otherCons = ["min", "max", "min_length", "max_length", "pattern", "format"]
    .filter(k => constraints[k] !== undefined)
    .map(k => `<tr><td class="px-3 fw-semibold small text-muted" style="width:140px;">${k}</td><td><code>${escapeHtml(String(constraints[k]))}</code></td></tr>`)
    .join("");

  const descendants = children.length ? getDescendants(db, release, module, key_path) : [];
  const childrenHtml = children.length ? renderDetailChildrenTree(release, module, key_path, children, descendants) : "";

  const lifecycleHeader = v.removed
    ? `<span class="badge bg-danger ms-1">removed</span>`
    : v.deprecated
      ? `<span class="badge bg-warning text-dark ms-1">deprecated</span>`
      : "";
  app.innerHTML = `
    <div class="d-flex align-items-center mb-4">
      <a href="#/${module}?release=${releaseParam(release)}" class="link-brand me-3"><i class="bi bi-arrow-left fs-4"></i></a>
      <div>
        <h4 class="mb-1 fw-bold brand-color"><code class="schema-key-code">${escapeHtml(displayPath(v.key_path))}</code></h4>
        <span class="badge bg-light text-dark border">${escapeHtml(v.var_type || "unknown")}</span>
        ${lifecycleHeader}
        <span class="text-muted small ms-2">${escapeHtml(SCHEMA_MODULES[module]?.name || module)}</span>
      </div>
    </div>
    <div class="row g-3">
      <div class="col-12">
        ${v.description ? `
          <h5 class="fw-bold brand-color mb-2"><i class="bi bi-info-circle me-2"></i>Description</h5>
          <div class="card border-0 shadow-sm mb-4"><div class="card-body schema-description">${formatDescriptionMarkdown(v.description)}</div></div>` : ""}

        <h5 class="fw-bold brand-color mb-2"><i class="bi bi-list-check me-2"></i>Properties</h5>
        <div class="card border-0 shadow-sm mb-4"><div class="table-responsive">
          <table class="table table-sm align-middle mb-0"><tbody>
            <tr><td class="px-3 fw-semibold small text-muted" style="width:140px;">Type</td><td><span class="badge bg-light text-dark border">${escapeHtml(v.var_type || "-")}</span></td></tr>
            ${(v.removed || v.deprecated) ? `<tr><td class="px-3 fw-semibold small text-muted">Status</td><td>${v.removed ? `<span class="badge bg-danger">removed</span>` : `<span class="badge bg-warning text-dark">deprecated</span>`}</td></tr>` : ""}
            <tr><td class="px-3 fw-semibold small text-muted">Default</td><td>${renderDefaultValue(v.default_value, { noneLabel: "none", open: true })}</td></tr>
            <tr><td class="px-3 fw-semibold small text-muted">Required</td><td>${v.required ? `<span class="text-success"><i class="bi bi-check-circle-fill me-1"></i>Yes</span>` : `<span class="text-muted">No</span>`}</td></tr>
            ${v.category ? `<tr><td class="px-3 fw-semibold small text-muted">Category</td><td><span class="badge schema-category-badge">${escapeHtml(v.category)}</span></td></tr>` : ""}
            ${v.doc_table ? `<tr><td class="px-3 fw-semibold small text-muted">Doc table</td><td><span class="badge schema-category-badge" title="documentation_options.table from the AVD schema">${escapeHtml(v.doc_table)}</span></td></tr>` : ""}
            ${v.cross_ref ? renderCrossRefRow(v.cross_ref, release) : ""}
            ${v.parent_path ? `<tr><td class="px-3 fw-semibold small text-muted">Parent</td><td><a href="#/${module}/${encodeURI(v.parent_path)}?release=${releaseParam(release)}" class="link-brand"><code class="schema-key-code">${escapeHtml(displayPath(v.parent_path))}</code></a></td></tr>` : ""}
            ${dynamicSource ? `<tr><td class="px-3 fw-semibold small text-muted">Dynamic key</td><td><code class="schema-key-code">${escapeHtml(dynamicSource)}</code></td></tr>` : ""}
          </tbody></table>
        </div></div>

        ${validValuesHtml}
        ${otherCons ? `<h5 class="fw-bold brand-color mb-2"><i class="bi bi-check2-square me-2"></i>Constraints</h5>
          <div class="card border-0 shadow-sm mb-4"><div class="table-responsive">
            <table class="table table-sm align-middle mb-0"><tbody>${otherCons}</tbody></table>
          </div></div>` : ""}
        ${childrenHtml}
      </div>
    </div>`;
}

// ── cross-schema reference helper ───────────────────────────────────────────
// Schema $ref strings look like "eos_cli_config_gen#/keys/foo/keys/bar".
// Convert into a SchemaExplorer hash link to the equivalent flattened key_path
// in the target module so users can jump straight there.
function renderCrossRefRow(ref, release) {
  const [target, jsonPointer] = String(ref).split("#", 2);
  if (!target || !jsonPointer) return "";
  const segments = jsonPointer.split("/").filter(Boolean);
  const parts = [];
  for (let i = 0; i < segments.length; i++) {
    const seg = segments[i];
    if (seg === "keys") {
      // skip — next segment is the key name
    } else if (seg === "items") {
      if (parts.length) parts[parts.length - 1] += "[]";
    } else {
      parts.push(seg);
    }
  }
  const keyPath = parts.join(".");
  const link = keyPath
    ? `#/${target}/${encodeURI(keyPath)}?release=${releaseParam(release)}`
    : `#/${target}?release=${releaseParam(release)}`;
  return `<tr><td class="px-3 fw-semibold small text-muted">Cross-schema</td><td><a href="${link}" class="link-brand"><code>${escapeHtml(target)}</code> → <code>${escapeHtml(keyPath || "(root)")}</code></a></td></tr>`;
}

// ── utils ────────────────────────────────────────────────────────────────────

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;", "'": "&#39;" }[c]));
}
function escapeAttr(s) { return escapeHtml(s).replace(/"/g, "&quot;"); }

function highlight(text, q) {
  if (!q || q.length < 2 || !text) return escapeHtml(text || "-");
  const lower = text.toLowerCase();
  const ql = q.toLowerCase();
  let out = "";
  let i = 0;
  while (i < text.length) {
    const idx = lower.indexOf(ql, i);
    if (idx < 0) { out += escapeHtml(text.slice(i)); break; }
    out += escapeHtml(text.slice(i, idx));
    out += `<mark class="schema-search-match">${escapeHtml(text.slice(idx, idx + q.length))}</mark>`;
    i = idx + q.length;
  }
  return out;
}

function formatMarkdownInline(text, q = "") {
  if (!text) return escapeHtml("-");
  const raw = String(text);
  let out = "";
  let last = 0;
  for (const match of raw.matchAll(/`([^`\n]+)`/g)) {
    out += highlight(raw.slice(last, match.index), q);
    out += "<code>" + escapeHtml(match[1]) + "</code>";
    last = match.index + match[0].length;
  }
  out += highlight(raw.slice(last), q);
  return out || escapeHtml("-");
}

function formatDescriptionMarkdown(text, q = "") {
  if (!text) return escapeHtml("-");
  const blocks = String(text).trim().split(/\n{2,}/);
  return blocks.map(block => {
    const lines = block.split(/\n/).map(line => line.trim()).filter(Boolean);
    if (!lines.length) return "";
    if (lines.every(line => /^[-*]\s+/.test(line))) {
      return '<ul class="mb-0">' + lines.map(line => "<li>" + formatMarkdownInline(line.replace(/^[-*]\s+/, ""), q) + "</li>").join("") + "</ul>";
    }
    return '<p class="mb-0">' + formatMarkdownInline(lines.join(" "), q) + "</p>";
  }).join("");
}

function debounce(fn, ms) {
  let t;
  return (...args) => { clearTimeout(t); t = setTimeout(() => fn(...args), ms); };
}

// ── Documentation view ───────────────────────────────────────────────────────

function docsPath(row) {
  return `.${displayPath(row.key_path)}`;
}

function renderDocsDetail(row, release, module, isAll) {
  const mod = isAll ? row.module : module;
  const constraints = yamlConstraints(row);
  const constraintsText = yamlRestrictionParts(row, constraints).join("; ");
  const lifecycle = row.removed
    ? `<span class="badge bg-danger ms-1">removed</span>`
    : row.deprecated
      ? `<span class="badge bg-warning text-dark ms-1">deprecated</span>`
      : "";
  const validValues = Array.isArray(constraints.valid_values) && constraints.valid_values.length
    ? `<h3>Valid Values</h3><div class="schema-docs-prose"><ul>${constraints.valid_values.map(value => `<li><code>${escapeHtml(String(value))}</code></li>`).join("")}</ul></div>`
    : "";
  const defaultHtml = row.default_value ? `<tr><th>Default</th><td>${renderDefaultValue(row.default_value, { compact: true })}</td></tr>` : "";
  const constraintsHtml = constraintsText ? `<tr><th>Constraints</th><td>${escapeHtml(constraintsText)}</td></tr>` : "";
  const moduleHtml = isAll ? `<tr><th>Module</th><td><code>${escapeHtml(mod)}</code></td></tr>` : "";
  return `
    <div class="schema-docs-detail-inner">
      <div class="schema-docs-breadcrumb"><code>${escapeHtml(displayPath(row.key_path))}</code></div>
      <h2>Key ${lifecycle}</h2>
      <div class="schema-docs-key-table-wrap">
        <table class="schema-docs-key-table">
          <thead><tr><th>Key Name</th><th>Type</th><th>Required</th></tr></thead>
          <tbody><tr>
            <td><code>${escapeHtml(leafSegment(row.key_path))}</code></td>
            <td>${escapeHtml(row.var_type || "-")}</td>
            <td>${row.required ? "Yes" : "None"}</td>
          </tr></tbody>
        </table>
      </div>
      <h2>Description</h2>
      <div class="schema-docs-prose">${formatDescriptionMarkdown(row.description || "-")}</div>
      <h2>Path</h2>
      <blockquote class="schema-docs-note">NOTE: The path is shown in jq-style notation.</blockquote>
      <p><code>${escapeHtml(docsPath(row))}</code></p>
      ${(row.default_value || constraintsText || isAll) ? `
        <h2>Properties</h2>
        <div class="schema-docs-key-table-wrap"><table class="schema-docs-key-table"><tbody>
          ${moduleHtml}
          ${defaultHtml}
          ${constraintsHtml}
          ${row.category ? `<tr><th>Category</th><td>${escapeHtml(row.category)}</td></tr>` : ""}
          ${row.doc_table ? `<tr><th>Table</th><td>${escapeHtml(row.doc_table)}</td></tr>` : ""}
        </tbody></table></div>` : ""}
      ${validValues}
    </div>`;
}

function renderDocsResults(target, release, module, state, inputRows) {
  const isAll = module === "all";
  const rowsById = new Map(inputRows.map(row => [treeRowId(row, module), row]));

  const groups = new Map();
  for (const row of inputRows) {
    const groupId = treeGroupId(row, module);
    if (!groups.has(groupId)) groups.set(groupId, { module: rowModule(row, module), root: rootSegment(row.key_path), rows: [] });
    groups.get(groupId).rows.push(row);
  }
  const orderedGroups = [...groups.values()].sort((a, b) => `${a.module}:${a.root}`.localeCompare(`${b.module}:${b.root}`));
  const orderedNavRows = orderedGroups.flatMap(group => orderedTreeRows(group.rows, module).rows);
  if (!state.docsSelectedId || !rowsById.has(state.docsSelectedId)) {
    state.docsSelectedId = treeRowId(orderedNavRows[0] || inputRows[0], module);
  }
  const selected = rowsById.get(state.docsSelectedId) || orderedNavRows[0] || inputRows[0];

  const navRows = orderedGroups.map(group => {
    const tree = orderedTreeRows(group.rows, module);
    return tree.rows.map(row => {
      const rowId = treeRowId(row, module);
      const parentId = tree.parentIds.get(rowId) || "";
      const depth = row.depth || 1;
      const isBranch = (tree.childCount.get(rowId) || 0) > 0;
      const expanded = false;
      const hidden = depth > 1 ? ` style="display: none;"` : "";
      const selectedClass = rowId === state.docsSelectedId ? " active" : "";
      const moduleBadge = isAll && depth === 1 ? `<span class="schema-docs-module">${escapeHtml(SCHEMA_MODULES[row.module]?.name || row.module)}</span>` : "";
      return `
        <div class="schema-docs-nav-row${selectedClass}"
             data-row-id="${escapeAttr(rowId)}"
             data-parent-id="${escapeAttr(parentId)}"
             data-is-branch="${isBranch ? "1" : "0"}"
             data-expanded="${expanded ? "1" : "0"}"
             data-depth="${depth}"${hidden}>
          <button type="button" class="schema-docs-toggle" ${isBranch ? "" : "disabled"}>${isBranch ? `<i class="bi ${expanded ? "bi-chevron-down" : "bi-chevron-right"}"></i>` : ""}</button>
          <button type="button" class="schema-docs-nav-key" data-docs-select="${escapeAttr(rowId)}" style="padding-left: ${Math.max(0, depth - 1) * 1.05}rem;">
            <span class="schema-docs-file-icon"><i class="bi bi-file-earmark-text"></i></span>
            <span>${highlight(leafSegment(row.key_path), state.q)}</span>
            ${moduleBadge}
          </button>
        </div>`;
    }).join("");
  }).join("");

  target.innerHTML = `
    <div class="schema-docs-view">
      <aside class="schema-docs-nav" aria-label="Schema documentation navigation">
        ${navRows}
      </aside>
      <section class="schema-docs-detail" aria-live="polite">${renderDocsDetail(selected, release, module, isAll)}</section>
    </div>`;

  function applyDocsVisibility() {
    const nav = target.querySelector(".schema-docs-nav");
    const rows = [...nav.querySelectorAll(".schema-docs-nav-row")];
    const byId = new Map(rows.map(row => [row.dataset.rowId, row]));
    for (const row of rows) {
      let visible = true;
      let parentId = row.dataset.parentId;
      while (parentId) {
        const parent = byId.get(parentId);
        if (!parent) break;
        if (parent.dataset.expanded !== "1") { visible = false; break; }
        parentId = parent.dataset.parentId;
      }
      row.style.display = visible ? "" : "none";
    }
  }

  target.querySelector(".schema-docs-nav")?.addEventListener("click", event => {
    const toggle = event.target.closest(".schema-docs-toggle");
    if (toggle && !toggle.disabled) {
      const row = toggle.closest(".schema-docs-nav-row");
      const open = row.dataset.expanded !== "1";
      row.dataset.expanded = open ? "1" : "0";
      toggle.innerHTML = `<i class="bi ${open ? "bi-chevron-down" : "bi-chevron-right"}"></i>`;
      applyDocsVisibility();
      return;
    }
    const select = event.target.closest("[data-docs-select]");
    if (!select) return;
    state.docsSelectedId = select.dataset.docsSelect;
    target.querySelectorAll(".schema-docs-nav-row.active").forEach(row => row.classList.remove("active"));
    select.closest(".schema-docs-nav-row")?.classList.add("active");
    const selectedRow = rowsById.get(state.docsSelectedId);
    if (selectedRow) {
      const detail = target.querySelector(".schema-docs-detail");
      detail.innerHTML = renderDocsDetail(selectedRow, release, module, isAll);
      detail.scrollTop = 0;
    }
  });
  applyDocsVisibility();
}

// ── YAML view ────────────────────────────────────────────────────────────────

function yamlBaseType(row) {
  return String(row.var_type || "").replace(/\(deprecated\)$/, "");
}

function yamlConstraints(row) {
  if (!row.constraints) return {};
  try { return JSON.parse(row.constraints); }
  catch { return {}; }
}

function yamlRestrictionParts(row, constraints) {
  const type = yamlBaseType(row);
  const parts = [];
  if (Array.isArray(constraints.valid_values) && constraints.valid_values.length) {
    const values = constraints.valid_values.map(value => type === "str" ? `"${value}"` : String(value));
    parts.push(values.join(" | "));
  }
  if (constraints.min !== undefined || constraints.max !== undefined) {
    if (constraints.min !== undefined && constraints.max !== undefined) parts.push(`${constraints.min}-${constraints.max}`);
    else if (constraints.min !== undefined) parts.push(`>=${constraints.min}`);
    else parts.push(`<=${constraints.max}`);
  }
  if (constraints.min_length !== undefined || constraints.max_length !== undefined) {
    if (type === "list") {
      if (constraints.min_length !== undefined && constraints.max_length !== undefined) parts.push(`${constraints.min_length}-${constraints.max_length} items`);
      else if (constraints.min_length !== undefined) parts.push(`>=${constraints.min_length} items`);
      else parts.push(`<=${constraints.max_length} items`);
    } else {
      if (constraints.min_length !== undefined && constraints.max_length !== undefined) parts.push(`length ${constraints.min_length}-${constraints.max_length}`);
      else if (constraints.min_length !== undefined) parts.push(`length >=${constraints.min_length}`);
      else parts.push(`length <=${constraints.max_length}`);
    }
  }
  return parts;
}

function yamlDefaultPart(row) {
  if (!row.default_value) return "";
  try {
    const value = JSON.parse(row.default_value);
    if (Array.isArray(value) || (value && typeof value === "object")) return "";
    if (yamlBaseType(row) === "str") return `default="${value}"`;
    return `default=${value}`;
  } catch {
    return "";
  }
}

function yamlValueParts(row, includeType) {
  const constraints = yamlConstraints(row);
  const parts = includeType ? [yamlBaseType(row) || "any"] : [];
  parts.push(...yamlRestrictionParts(row, constraints));
  const defaultPart = yamlDefaultPart(row);
  if (defaultPart) parts.push(defaultPart);
  if (row.required) parts.push(row.unique_key ? "required; unique" : "required");
  return parts.filter(Boolean);
}

function yamlDescriptionLines(row, indentCount, listItem) {
  if (!row.description) return [];
  const commentIndent = " ".repeat(listItem ? indentCount + 2 : indentCount);
  const lines = String(row.description).trim().split(/\n/).map(line => `${commentIndent}# ${line.trimEnd()}`);
  return ["", ...lines];
}

function yamlHighlightValue(rawValue) {
  const commentIndex = rawValue.indexOf(" #");
  const valuePart = commentIndex === -1 ? rawValue : rawValue.slice(0, commentIndex);
  const commentPart = commentIndex === -1 ? "" : rawValue.slice(commentIndex);
  const html = escapeHtml(valuePart).replace(/(&lt;.*?&gt;)/g, '<span class="se-yaml-placeholder">$1</span>')
    .replace(/(&quot;[^&]*?&quot;)/g, '<span class="se-yaml-string">$1</span>')
    .replace(/\b(true|false|null)\b/g, '<span class="se-yaml-literal">$1</span>')
    .replace(/(?<![-\w])(-?\d+(?:\.\d+)?)(?![-\w])/g, '<span class="se-yaml-number">$1</span>');
  return html + (commentPart ? `<span class="se-yaml-comment">${escapeHtml(commentPart)}</span>` : "");
}

function yamlHighlightLine(line) {
  if (!line) return "";
  const commentMatch = line.match(/^(\s*#.*)$/);
  if (commentMatch) return `<span class="se-yaml-comment">${escapeHtml(line)}</span>`;

  const fieldMatch = line.match(/^(\s*)(-\s*)?([^:#]+:)(.*)$/);
  if (!fieldMatch) return escapeHtml(line);
  const [, indent, listMarker = "", key, value] = fieldMatch;
  return `${escapeHtml(indent)}${listMarker ? `<span class="se-yaml-marker">${escapeHtml(listMarker)}</span>` : ""}<span class="se-yaml-key">${escapeHtml(key)}</span>${yamlHighlightValue(value)}`;
}

function yamlHighlightBlock(text) {
  return String(text).split("\n").map(yamlHighlightLine).join("\n");
}

function renderYamlResults(target, module, inputRows) {
  const sourceRows = inputRows.filter(row => !row.removed);
  const rowsByPath = new Map(sourceRows.map(row => [`${row.module}:${row.key_path}`, row]));
  const childrenByParent = new Map();
  for (const row of sourceRows) {
    if (!row.parent_path) continue;
    const parentKey = `${row.module}:${row.parent_path}`;
    if (!childrenByParent.has(parentKey)) childrenByParent.set(parentKey, []);
    childrenByParent.get(parentKey).push(row);
  }

  function rowKey(row) { return `${row.module}:${row.key_path}`; }
  function childrenOf(row) { return childrenByParent.get(rowKey(row)) || []; }
  function yamlLinePrefix(indentCount, listItem) { return " ".repeat(indentCount) + (listItem ? "- " : ""); }
  function yamlFieldName(row) { return yamlKeySegment(row.key_path); }
  function yamlPropertiesComment(row) {
    const parts = yamlValueParts(row, false);
    return parts.length ? ` # ${parts.join("; ")}` : "";
  }

  function renderListChildren(lines, childRows, listIndent) {
    childRows.forEach((child, idx) => {
      if (idx === 0) renderYamlRow(lines, child, listIndent + 2, true);
      else renderYamlRow(lines, child, listIndent + 4, false);
    });
  }

  function renderYamlRow(lines, row, indentCount, listItem = false) {
    const type = yamlBaseType(row);
    const childRows = childrenOf(row);
    lines.push(...yamlDescriptionLines(row, indentCount, listItem));
    const prefix = yamlLinePrefix(indentCount, listItem);
    const fieldName = yamlFieldName(row);

    if (type === "list") {
      const fallback = childRows.length ? "" : " <list>";
      lines.push(`${prefix}${fieldName}:${fallback}${yamlPropertiesComment(row)}`);
      renderListChildren(lines, childRows, indentCount);
      return;
    }

    if (type === "dict") {
      const fallback = childRows.length ? "" : " <dict>";
      lines.push(`${prefix}${fieldName}:${fallback}${yamlPropertiesComment(row)}`);
      childRows.forEach(child => renderYamlRow(lines, child, indentCount + (listItem ? 4 : 2)));
      return;
    }

    lines.push(`${prefix}${fieldName}: <${yamlValueParts(row, true).join("; ")}>`);
  }

  const topRows = sourceRows.filter(row => !row.parent_path || !rowsByPath.has(`${row.module}:${row.parent_path}`));
  const groupedRows = new Map();
  const groupCounts = new Map();
  for (const row of sourceRows) {
    const groupId = treeGroupId(row, module);
    groupCounts.set(groupId, (groupCounts.get(groupId) || 0) + 1);
  }
  for (const row of topRows) {
    const groupId = treeGroupId(row, module);
    if (!groupedRows.has(groupId)) {
      groupedRows.set(groupId, { root: rootSegment(row.key_path), module: rowModule(row, module), rows: [] });
    }
    groupedRows.get(groupId).rows.push(row);
  }

  const idPrefix = `y${++_treeRenderSeq}`;
  const groupsHtml = [...groupedRows.entries()].sort(([, a], [, b]) => `${a.module}:${a.root}`.localeCompare(`${b.module}:${b.root}`)).map(([groupId, group], idx) => {
    const lines = [];
    group.rows.forEach(row => renderYamlRow(lines, row, 0));
    const yamlText = lines.join("\n").trim() || "# No YAML fields match.";
    const id = `${idPrefix}-group-${idx}`;
    const groupModuleBadge = module === "all" ? `<span class="badge ${group.module === "eos_designs" ? "bg-primary" : "bg-success"} ms-1" style="font-size: 0.6rem;">${escapeHtml(SCHEMA_MODULES[group.module]?.name || group.module)}</span>` : "";
    return `
      <div class="schema-group" data-group-id="${id}">
        <div class="schema-group-header" data-bs-toggle="collapse" data-bs-target="#${id}" aria-expanded="false" aria-controls="${id}">
          <i class="bi bi-chevron-right collapse-icon"></i>
          <code class="schema-key-code fw-bold" style="font-size: 0.88rem;">${escapeHtml(group.root)}</code>
          ${groupModuleBadge}
          <span class="badge bg-secondary ms-1" style="font-size: 0.6rem;">${groupCounts.get(groupId) || group.rows.length}</span>
        </div>
        <div class="collapse" id="${id}">
          <pre class="schema-yaml-block"><code>${yamlHighlightBlock(yamlText)}</code></pre>
        </div>
      </div>`;
  }).join("");

  target.innerHTML = `
    <div class="schema-results-toolbar card-header bg-light d-flex align-items-center justify-content-between">
      <span class="text-muted small">YAML preview for ${sourceRows.length} variable${sourceRows.length === 1 ? "" : "s"} in ${groupedRows.size} group${groupedRows.size === 1 ? "" : "s"}</span>
    </div>
    <div class="schema-results-scroll">
      ${groupsHtml}
    </div>`;
}

// ── embed mounting ──────────────────────────────────────────────────────────
//
// Renders a scoped tree view inside any <schema-explorer> element on the page.
// The element is treated like a sealed component: docs author drops the tag,
// the SPA fills it in.
//
// Supported data attributes:
//   release  — schema release tag (default: "devel")
//   module   — "eos_designs" | "eos_cli_config_gen" | "all" (default: "eos_designs")
//   root     — key_path prefix; only show that subtree (e.g. "router_bgp"). Optional.
//   view     — "tree" | "flat" | "yaml" | "docs" (default: "tree")
//   height   — CSS max-height for the scroll container (default: "600px")
//   chrome   — "compact" | "none" (default: "compact"). "none" hides the
//              "N variables in M groups" / expand-all bar.

function _embedAttr(el, name, fallback) {
  return el.getAttribute(`data-${name}`) || el.getAttribute(name) || fallback;
}

function failEmbed(el, msg) {
  el.innerHTML = `<div class="alert alert-danger m-2 small"><i class="bi bi-exclamation-triangle me-1"></i>${escapeHtml(msg)}</div>`;
}

async function mountEmbed(el) {
  const release = normalizeRelease(_embedAttr(el, "release", DEFAULT_RELEASE));
  const module  = _embedAttr(el, "module", "eos_designs");
  const root    = _embedAttr(el, "root", "");
  const view    = _embedAttr(el, "view", "tree");
  if (!["tree", "flat", "yaml", "docs"].includes(view)) throw new Error("Unsupported schema explorer view: " + view);
  const height  = _embedAttr(el, "height", "600px");
  const chrome  = _embedAttr(el, "chrome", "compact");

  // <schema-explorer> is an unknown HTML element -> defaults to inline. Force
  // block + scroll container so the embed actually takes up space.
  Object.assign(el.style, {
    display: "block",
    maxHeight: height,
    overflow: "auto",
    border: "1px solid var(--md-default-fg-color--lightest, #e1e4e8)",
    borderRadius: "4px",
    margin: "0.75rem 0",
  });
  el.classList.add("schema-embed");
  el.innerHTML = `<div class="text-muted small p-3">
    <span class="spinner-border spinner-border-sm" role="status"></span>
    <span class="ms-2">Loading <code>${escapeHtml(module)}</code> schema...</span>
  </div>`;

  const db = await getDb(release);
  const rootOptions = getRootOptions(db, release, module);
  const defaultRootStateValue = defaultRootState(rootOptions, root, module);
  const defaultRootSelection = defaultRootStateValue.selection;
  const rootOptionsHtml = rootOptions.map(row => {
    const value = rootOptionValue(row, module);
    const label = module === "all" ? `${SCHEMA_MODULES[row.module]?.name || row.module}: ${displayPath(row.key_path)}` : displayPath(row.key_path);
    return `<option value="${escapeAttr(value)}"${value === defaultRootSelection ? " selected" : ""}>${escapeHtml(label)}</option>`;
  }).join("");
  const hasDefaultRootOption = !defaultRootSelection || rootOptions.some(row => rootOptionValue(row, module) === defaultRootSelection);
  const rootFallbackOption = hasDefaultRootOption ? "" : `<option value="${escapeAttr(defaultRootSelection)}" selected>${escapeHtml(displayPath(defaultRootStateValue.root))}</option>`;
  const idPrefix = `embed-${++_treeRenderSeq}`;

  el.innerHTML = `
    <form class="schema-embed-filters p-3 border-bottom" onsubmit="return false">
      <div class="d-flex flex-wrap align-items-center gap-3">
        <div class="flex-grow-1 schema-filter-field">
          <label class="schema-filter-label" for="${idPrefix}-q">Search</label>
          <div class="input-group input-group-sm">
            <span class="input-group-text"><i class="bi bi-search"></i></span>
            <input type="search" class="form-control schema-search-input" id="${idPrefix}-q" placeholder="Search key paths or descriptions...">
            <select class="form-control schema-search-scope" id="${idPrefix}-search-scope" aria-label="Search scope">
              <option value="both" selected>Both</option>
              <option value="path">Path</option>
              <option value="description">Description</option>
            </select>
          </div>
        </div>
        <div class="schema-root-filter-field">
          <label class="schema-filter-label" for="${idPrefix}-root">Root filter</label>
          <div class="input-group input-group-sm">
            <span class="input-group-text"><i class="bi bi-funnel"></i></span>
            <select class="form-control schema-root-select" id="${idPrefix}-root">
              <option value="">All root keys</option>
              ${rootFallbackOption}
              ${rootOptionsHtml}
            </select>
            ${root ? `<button type="button" class="btn btn-outline-secondary" id="${idPrefix}-root-reset" title="Reset root filter"><i class="bi bi-arrow-counterclockwise"></i></button>` : ""}
            <button type="button" class="btn btn-outline-secondary" id="${idPrefix}-root-clear" title="Clear root filter"><i class="bi bi-x-lg"></i></button>
          </div>
        </div>
      </div>
    </form>
    <div class="schema-embed-results"></div>`;

  const state = {
    q: "",
    root: defaultRootStateValue.root,
    defaultRoot: root,
    defaultRootSelection,
    rootModule: defaultRootStateValue.rootModule,
    category: "",
    docTable: "",
    searchScope: "both",
    view,
    target: el.querySelector(".schema-embed-results"),
    embedCompact: true,
  };

  function renderEmbedResults() {
    renderResults(db, release, module, state);
    if (chrome === "none") {
      const header = state.target.querySelector(".schema-results-toolbar");
      if (header) header.style.display = "none";
    }
    const firstCollapse = state.target.querySelector(".collapse");
    if (firstCollapse && typeof bootstrap !== "undefined") {
      bootstrap.Collapse.getOrCreateInstance(firstCollapse, { toggle: false }).show();
      state.target.querySelector(".schema-group-header")?.setAttribute("aria-expanded", "true");
    }
  }

  const refresh = debounce(renderEmbedResults, 250);
  el.querySelector(`#${CSS.escape(idPrefix)}-q`).addEventListener("input", e => {
    state.q = e.target.value.trim();
    refresh();
  });
  el.querySelector(`#${CSS.escape(idPrefix)}-search-scope`).addEventListener("change", e => {
    state.searchScope = normalizeSearchScope(e.target.value);
    renderEmbedResults();
  });
  const rootInput = el.querySelector(`#${CSS.escape(idPrefix)}-root`);
  rootInput.addEventListener("change", e => {
    const selection = parseRootSelection(e.target.value, module);
    state.root = selection.root;
    state.rootModule = selection.rootModule;
    renderEmbedResults();
  });
  el.querySelector(`#${CSS.escape(idPrefix)}-root-clear`).addEventListener("click", () => {
    state.root = "";
    state.rootModule = "";
    rootInput.value = "";
    renderEmbedResults();
  });
  el.querySelector(`#${CSS.escape(idPrefix)}-root-reset`)?.addEventListener("click", () => {
    const selection = parseRootSelection(state.defaultRootSelection, module);
    state.root = selection.root;
    state.rootModule = selection.rootModule;
    rootInput.value = state.defaultRootSelection;
    renderEmbedResults();
  });

  renderEmbedResults();
}
