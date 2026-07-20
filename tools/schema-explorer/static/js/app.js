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
    const idPrefix = `d${++_schemaRenderSeq}`;
    const itemsHtml = parts.parsed.map((item, idx) => {
      const fields = Object.fromEntries(Object.entries(item).filter(([key]) => key !== "platforms"));
      const platforms = Array.isArray(item.platforms) && item.platforms.length
        ? item.platforms.join(", ")
        : `Item ${idx + 1}`;
      const id = `${idPrefix}-item-${idx}`;
      return `
        <div class="schema-group schema-default-group">
          <div class="schema-group-header" data-bs-toggle="collapse" data-bs-target="#${id}" aria-expanded="false" aria-controls="${id}">
            <i class="bi bi-chevron-right collapse-icon"></i>
            <code class="schema-key-code">${escapeHtml(platforms)}</code>
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
function schemaRowId(row, currentModule) {
  return `${rowModule(row, currentModule)}:${row.key_path}`;
}
function schemaParentId(row, currentModule) {
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
function resolvedSchemaParentId(row, currentModule, rowIds) {
  const directParentId = schemaParentId(row, currentModule);
  if (!directParentId || !rowIds || rowIds.has(directParentId)) return directParentId;

  const rowModuleId = rowModule(row, currentModule);
  const candidates = parentPathCandidates(row).slice(1).map(keyPath => `${rowModuleId}:${keyPath}`);
  return candidates.find(candidate => rowIds.has(candidate)) || directParentId;
}
function orderedSchemaRows(vars, currentModule) {
  const sourceVars = [...vars];
  const rowIds = new Set(sourceVars.map(row => schemaRowId(row, currentModule)));
  const childCount = new Map();
  const childrenByParent = new Map();
  const parentIds = new Map();
  const rootRows = [];

  for (const row of sourceVars) {
    const rowId = schemaRowId(row, currentModule);
    const resolvedParentId = resolvedSchemaParentId(row, currentModule, rowIds);
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
    const rowId = schemaRowId(row, currentModule);
    if (visited.has(rowId)) return;
    visited.add(rowId);
    orderedRows.push(row);
    (childrenByParent.get(rowId) || []).forEach(visit);
  }
  rootRows.forEach(visit);
  sourceVars.forEach(visit);
  return { rows: orderedRows, childCount, parentIds, rowIds };
}
function schemaGroupId(row, currentModule) {
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
function inferSchemaAssetBase() {
  if (SCHEMA_BASE === "data") return ".";
  if (SCHEMA_BASE.endsWith("/data")) return SCHEMA_BASE.slice(0, -5);
  return SCHEMA_BASE;
}
const SCHEMA_ASSET_BASE = inferSchemaAssetBase();
const SCHEMA_VENDOR_BASE = `${SCHEMA_ASSET_BASE}/vendor`;
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

let dbCache = null;    // sql.js Database
let SQL = null;
const app = document.getElementById("app");

// ── boot ─────────────────────────────────────────────────────────────────────
//
// Two mount modes share this script:
//
//   * **Standalone**: a page declares `<main id="app">`
//     (the SPA's own `index.html` at `/_assets/schema-explorer/index.html`).
//     Uses the URL hash for routing — landing / module / var-detail views.
//
//   * **Embed**: any docs page drops one or more `<schema-explorer>` custom
//     elements. Each embed is self-contained, scoped to a (module, root) tuple via data attributes, and never touches `location.hash`.
//     Multiple embeds on the same page share `dbCache`.
//
// Both modes can coexist — embeds work even when `#app` is also present.

// Runtime dependencies are lazy-loaded from same-origin vendored assets so docs
// pages that never host an embed do not pay for the extra script/font requests. Do not inject Bootstrap CSS
// here: it contains global element rules for headings, links, body line-height,
// etc. that leak into Material chrome. The standalone SPA owns the whole page
// and loads Bootstrap CSS directly from static/index.html.
const RUNTIME_DEPS = {
  css: [
    {
      href: `${SCHEMA_VENDOR_BASE}/bootstrap-icons/font/bootstrap-icons.min.css`,
      integrity: "sha384-L8JisW7yet65STBdXyiV6LpfJHTE34WQ6uNxndBGg1lcc3tseozYGsBw6W6KzXVv",
    },
  ],
  js: [
    {
      src: `${SCHEMA_VENDOR_BASE}/bootstrap/bootstrap.bundle.min.js`,
      global: "bootstrap",
      integrity: "sha384-WfVzX9hAUBOBjMptWY54rUnWRI1Tn/ZCUAT52D/05VTiszOwsM+TM5o0sB4Kv44M",
    },
    {
      src: `${SCHEMA_VENDOR_BASE}/sql.js/dist/sql-wasm.js`,
      global: "initSqlJs",
      integrity: "sha384-8D3Rsfo535FqoC1pHCCQMrNf75UgzyoG/HQm9zOzITRrz3QKzecc2E7JXKGCXoWu",
    },
  ],
};
const SQL_WASM = {
  src: `${SCHEMA_VENDOR_BASE}/sql.js/dist/sql-wasm.wasm`,
  integrity: "sha384-kSm0AH9ho89napVfNFf/kCRTH6xBoCS3qf/ATGJeYFQFKiegBMLhQ3aUIZBlYLpa",
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
        reject(new Error("Loaded " + src + ", but " + globalName + " is not defined. Check browser access to the Schema Explorer asset."));
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
  await Promise.all(RUNTIME_DEPS.css.map(_loadCss));
  // Scripts must load in order — Bootstrap before sql.js doesn't strictly
  // matter, but doing them sequentially makes ordering predictable.
  for (const dep of RUNTIME_DEPS.js) await _loadScript(dep);
}

async function _verifiedWasmBinary(dep) {
  const response = await fetch(dep.src);
  if (!response.ok) {
    throw new Error("Failed to load " + dep.src + " (" + response.status + ")");
  }
  const wasmBinary = await response.arrayBuffer();
  if (!globalThis.crypto?.subtle) {
    throw new Error("Unable to verify " + dep.src + ": Web Crypto is unavailable.");
  }
  const digest = await globalThis.crypto.subtle.digest("SHA-384", wasmBinary);
  const digestBytes = String.fromCharCode(...new Uint8Array(digest));
  const actualIntegrity = "sha384-" + btoa(digestBytes);
  if (actualIntegrity !== dep.integrity) {
    throw new Error("Integrity check failed for " + dep.src);
  }
  return wasmBinary;
}

async function ensureSqlJs() {
  if (SQL) return SQL;
  await ensureDeps();
  const wasmBinary = await _verifiedWasmBinary(SQL_WASM);
  SQL = await window.initSqlJs({
    wasmBinary,
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

document.addEventListener("change", e => {
  const select = e.target.closest("[data-reference-default-select]");
  if (!select) return;
  const target = document.getElementById(select.dataset.referenceDefaultTarget || "");
  if (!target) return;
  target.querySelectorAll("[data-reference-default-item]").forEach(item => {
    item.hidden = item.dataset.referenceDefaultItem !== select.value;
  });
});

document.addEventListener("click", e => {
  const yamlAnnotationToggle = e.target.closest("[data-yaml-annotation-target]");
  if (yamlAnnotationToggle) {
    e.preventDefault();
    e.stopPropagation();
    const annotation = document.getElementById(yamlAnnotationToggle.dataset.yamlAnnotationTarget || "");
    if (!annotation) return;
    annotation.scrollIntoView({ block: "nearest" });
    annotation.classList.add("schema-yaml-annotation-active");
    setTimeout(() => annotation.classList.remove("schema-yaml-annotation-active"), 1200);
    return;
  }
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
  try {
    const db = await getDb();
    if (segments.length === 0)             return renderLanding(db);
    if (segments.length === 1)             return renderModule(db, segments[0], { view: params.get("view") || "" });
    return renderVarDetail(db, segments[0], segments.slice(1).join("/"));
  } catch (err) {
    fail(err.message);
  }
}

function fail(msg) {
  app.innerHTML = `<div class="alert alert-danger m-3"><i class="bi bi-exclamation-triangle me-2"></i>${escapeHtml(msg)}</div>`;
}

// ── sqlite loader ────────────────────────────────────────────────────────────

async function getDb() {
  if (dbCache) return dbCache;
  if (app) {
    app.innerHTML = `<div class="text-center py-5 text-muted">
      <span class="spinner-border spinner-border-sm"></span>
      <span class="ms-2 small">Loading schema…</span>
    </div>`;
  }
  const url = `${SCHEMA_BASE}/schema.sqlite`;
  // cache: "no-cache" forces a conditional GET so the browser revalidates
  // against the server's Last-Modified / ETag every page load. Keeps the
  // bytes cached locally when nothing changed (304), but picks up a freshly
  // regenerated SQLite immediately without a hard reload.
  const buf = await fetch(url, { cache: "no-cache" }).then(r => {
    if (!r.ok) throw new Error(`Could not load ${url} (${r.status})`);
    return r.arrayBuffer();
  });
  const db = new SQL.Database(new Uint8Array(buf));
  dbCache = db;
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

function searchVars(db, module, opts = {}) {
  const conds = [];
  const ps = [];
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
  if (opts.docTable) { conds.push("doc_table = ?"); ps.push(opts.docTable); }
  const orderBy = opts.order === "id" ? "id" : "key_path";
  const whereClause = conds.length ? conds.join(" AND ") : "1=1";
  const sql = `SELECT * FROM schema_vars WHERE ${whereClause} ORDER BY ${orderBy} LIMIT ${opts.limit || 500}`;
  return rows(db, sql, ps);
}

function getDocTableCounts(db, module) {
  if (module === "all") {
    return rows(db, "SELECT doc_table, COUNT(*) AS count FROM schema_vars GROUP BY doc_table ORDER BY doc_table");
  }
  return rows(db, "SELECT doc_table, COUNT(*) AS count FROM schema_vars WHERE module = ? GROUP BY doc_table ORDER BY doc_table", [module]);
}

function getRootOptions(db, module) {
  const conds = ["depth = 1"];
  const ps = [];
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

function getVar(db, module, key_path) {
  const r = rows(db, "SELECT * FROM schema_vars WHERE module = ? AND key_path = ?", [module, key_path]);
  return r[0] || null;
}

// ── views ────────────────────────────────────────────────────────────────────

function renderDevelopmentNotice() {
  return `
    <div class="schema-development-notice" role="note">
      <div class="schema-development-notice-title"><i class="bi bi-tools"></i> Under construction</div>
      <div>This Schema Explorer is still in development. Please use <a href="https://github.com/aristanetworks/avd/discussions/7186" target="_blank" rel="noopener">GitHub Discussion</a> to share comments, concerns, and feature requests.</div>
    </div>`;
}

function renderLanding(db) {
  const cards = Object.entries(SCHEMA_MODULES).map(([id, mod]) => {
    return `
      <div class="col">
        <a href="#/${id}" class="text-decoration-none d-block h-100">
          <div class="card h-100 border-0 shadow-sm module-card">
            <div class="card-body d-flex flex-column">
              <div class="d-flex align-items-start mb-2">
                <span class="fs-3 me-2 brand-color"><i class="bi ${mod.icon}"></i></span>
                <div class="me-auto">
                  <h6 class="mb-0 fw-semibold">${escapeHtml(mod.name)}</h6>
                  <div class="text-muted" style="font-size:0.7rem;"><code>${id}</code></div>
                </div>
              </div>
              <p class="text-muted small mb-0">${escapeHtml(mod.description)}</p>
            </div>
          </div>
        </a>
      </div>`;
  }).join("");

  app.innerHTML = `
    <p class="text-muted small mb-3">
      Browse the AVD data model schemas. Select a module to explore variables, search by key path, and view detailed documentation.
    </p>
    ${renderDevelopmentNotice()}
    <div class="row row-cols-1 row-cols-md-2 g-3 mb-4">${cards}</div>
    <div class="row mb-4"><div class="col">
      <a href="#/all" class="text-decoration-none d-block">
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

function renderModule(db, module, options = {}) {
  const host = options.target || app;
  const embedded = !!options.embed;
  const defaultRoot = options.root || "";
  const initialView = ["reference", "yaml"].includes(options.view) ? options.view : "reference";
  const chrome = options.chrome || "compact";
  const isAll = module === "all";
  if (!isAll && !SCHEMA_MODULES[module]) {
    host.innerHTML = `<div class="alert alert-danger m-3"><i class="bi bi-exclamation-triangle me-2"></i>Module not found: ${escapeHtml(module)}</div>`;
    return;
  }

  const info = isAll
    ? { name: "All Modules", icon: "bi-search", description: "Search across both AVD Design and EOS Config schemas." }
    : SCHEMA_MODULES[module];

  const headerHtml = chrome === "none" ? "" : `
    <div class="d-flex align-items-center mb-3 schema-browser-heading">
      ${embedded ? "" : `<a href="#/" class="link-brand me-3"><i class="bi bi-arrow-left fs-4"></i></a>`}
      <div>
        <h4 class="mb-1 fw-bold brand-color"><i class="bi ${info.icon} me-2"></i>${escapeHtml(info.name)}${isAll ? "" : ` <small class="text-muted fw-normal" style="font-size:0.6em;"><code>${escapeHtml(module)}</code></small>`}</h4>
      </div>
    </div>
    <p class="text-muted small mb-3">${escapeHtml(info.description)}</p>`;
  const developmentNoticeHtml = chrome === "none" ? "" : renderDevelopmentNotice();

  host.innerHTML = `
    ${headerHtml}
    ${developmentNoticeHtml}
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
              <button type="button" class="btn btn-outline-secondary schema-view-mode-button" id="btn-view-reference">Reference</button>
              <button type="button" class="btn btn-outline-secondary schema-view-mode-button" id="btn-view-yaml">YAML</button>
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
    docTable: "",
    searchScope: "both",
    view: initialView,
    target: host.querySelector("#results"),
  };
  const refresh = debounce(() => renderResults(db, module, state), 250);

  const qInput = host.querySelector("#q");
  const scopeInput = host.querySelector("#search-scope");
  const activeFilters = host.querySelector("#active-filters");
  function updateActiveFilters() {
    const filters = [];
    if (state.q) filters.push(`Search (${escapeHtml(searchScopeLabel(state.searchScope))}): <code>${escapeHtml(state.q)}</code>`);
    if (state.docTable) filters.push(`Table: <code>${escapeHtml(state.docTable)}</code>`);
    activeFilters.innerHTML = filters.length ? filters.join(" <span class=\"mx-1\">|</span> ") : "No filters applied";
  }

  qInput.addEventListener("input", e => { state.q = e.target.value.trim(); updateActiveFilters(); refresh(); });
  scopeInput.addEventListener("change", e => {
    state.searchScope = normalizeSearchScope(e.target.value);
    updateActiveFilters();
    renderResults(db, module, state);
  });
  const viewButtons = {
    yaml: host.querySelector("#btn-view-yaml"),
    reference: host.querySelector("#btn-view-reference"),
  };
  function setViewMode(view) {
    state.view = view;
    for (const [mode, button] of Object.entries(viewButtons)) button.classList.toggle("active", mode === view);
    renderResults(db, module, state);
  }
  viewButtons.yaml.addEventListener("click", () => setViewMode("yaml"));
  viewButtons.reference.addEventListener("click", () => setViewMode("reference"));

  updateActiveFilters();
  setViewMode(initialView);
}

function renderResults(db, module, state) {
  const target = state.target || document.getElementById("results");
  // Reference and YAML views need every row in the active scope so the hierarchy is complete.
  // Anything dropped at the SQL boundary disappears from the output entirely.
  const results = state.rows || searchVars(db, module, { ...state, limit: 20000, order: "id" });
  if (!results.length) {
    target.innerHTML = `<div class="text-center py-5 text-muted"><i class="bi bi-inbox fs-3 d-block mb-2"></i><span class="small">No variables match.</span></div>`;
    return;
  }
  if (state.view === "yaml") return renderYamlResults(target, module, state, results);
  if (state.view === "reference") return renderReferenceResults(target, module, state, results);
  return renderReferenceResults(target, module, { ...state, view: "reference" }, results);
}

let _schemaRenderSeq = 0;

function schemaBool(value) {
  return value === true || value === 1 || value === "1";
}

function isPrimaryKey(row) {
  return schemaBool(row.primary_key) || schemaBool(row.unique_key);
}

function renderPropertyRows(rows, headerTag = "td") {
  return rows.filter(row => row.show !== false).map(row => {
    const labelCell = headerTag === "th"
      ? `<th>${escapeHtml(row.label)}</th>`
      : `<td class="px-3 fw-semibold small text-muted"${row.width ? ` style="width:${escapeAttr(row.width)};"` : ""}>${escapeHtml(row.label)}</td>`;
    return `<tr>${labelCell}<td>${row.value}</td></tr>`;
  }).join("");
}

function renderVarDetail(db, module, key_path) {
  if (!SCHEMA_MODULES[module]) return fail(`Module not found: ${module}`);
  const v = getVar(db, module, key_path);
  if (!v) return fail(`Variable not found: ${module}/${key_path}`);

  const constraints = v.constraints ? JSON.parse(v.constraints) : {};
  const constraintsText = yamlRestrictionParts(v, constraints).join("; ");
  const dynamicSource = dynamicKeySource(v.key_path);
  const primaryKey = isPrimaryKey(v);

  const validValuesHtml = constraints.valid_values ? `
    <h5 class="fw-bold brand-color mb-2"><i class="bi bi-list-check me-2"></i>Valid Values</h5>
    <div class="card border-0 shadow-sm mb-4"><div class="card-body p-0">
      ${constraints.valid_values.map((val, i, arr) => `
        <div class="d-flex align-items-start px-3 py-2 ${i < arr.length - 1 ? "border-bottom" : ""}">
          <div class="me-3" style="min-width: 3.5rem;"><span class="schema-valid-value">${escapeHtml(String(val))}</span></div>
        </div>`).join("")}
    </div></div>` : "";

  const otherCons = ["min", "max", "min_length", "max_length", "pattern", "format"]
    .filter(k => constraints[k] !== undefined)
    .map(k => `<tr><td class="px-3 fw-semibold small text-muted" style="width:140px;">${k}</td><td><code>${escapeHtml(String(constraints[k]))}</code></td></tr>`)
    .join("");

  const lifecycleHeader = v.removed
    ? `<span class="schema-detail-status text-muted ms-1">removed</span>`
    : v.deprecated
      ? `<span class="schema-detail-status text-muted ms-1">deprecated</span>`
      : "";
  const propertyRows = renderPropertyRows([
    { label: "Type", width: "140px", value: `<span class="schema-type-label">${escapeHtml(v.var_type || "-")}</span>` },
    { label: "Status", value: `<span class="schema-detail-status text-muted">${v.removed ? "removed" : "deprecated"}</span>`, show: v.removed || v.deprecated },
    { label: "Primary Key", value: `<span class="text-success"><i class="bi bi-key-fill me-1"></i>Yes</span>`, show: primaryKey },
    { label: "Required", value: `<span class="text-success"><i class="bi bi-check-circle-fill me-1"></i>Yes</span>`, show: schemaBool(v.required) && !primaryKey },
    { label: "Default", value: renderDefaultValue(v.default_value, { noneLabel: "none", open: true }), show: v.default_value !== null && v.default_value !== undefined && v.default_value !== "" },
    { label: "Value Restrictions", value: escapeHtml(constraintsText), show: !!constraintsText },
  ]);
  app.innerHTML = `
    <div class="d-flex align-items-center mb-4 schema-detail-heading">
      <a href="#/${module}" class="link-brand me-3"><i class="bi bi-arrow-left fs-4"></i></a>
      <div>
        <h4 class="mb-1 fw-bold brand-color"><code class="schema-key-code">${escapeHtml(displayPath(v.key_path))}</code></h4>
        <span class="schema-type-label">${escapeHtml(v.var_type || "unknown")}</span>
        ${lifecycleHeader}
        <span class="text-muted small ms-2">${escapeHtml(SCHEMA_MODULES[module]?.name || module)}</span>
      </div>
    </div>
    <div class="row g-3 schema-detail-page">
      <div class="col-12">
        ${v.description ? `<h5 class="fw-bold brand-color mb-2"><i class="bi bi-info-circle me-2"></i>Description</h5>
        <div class="card border-0 shadow-sm mb-4"><div class="card-body schema-description">${formatDescriptionMarkdown(v.description)}</div></div>` : ""}

        <h5 class="fw-bold brand-color mb-2"><i class="bi bi-list-check me-2"></i>Properties</h5>
        <div class="card border-0 shadow-sm mb-4"><div class="table-responsive">
          <table class="table table-sm align-middle mb-0"><tbody>
            ${propertyRows}
            ${v.cross_ref ? renderCrossRefRow(v.cross_ref) : ""}
            ${v.parent_path ? `<tr><td class="px-3 fw-semibold small text-muted">Parent</td><td><a href="#/${module}/${encodeURI(v.parent_path)}" class="link-brand"><code class="schema-key-code">${escapeHtml(displayPath(v.parent_path))}</code></a></td></tr>` : ""}
            ${dynamicSource ? `<tr><td class="px-3 fw-semibold small text-muted">Dynamic key</td><td><code class="schema-key-code">${escapeHtml(dynamicSource)}</code></td></tr>` : ""}
          </tbody></table>
        </div></div>

        ${validValuesHtml}
        ${otherCons ? `<h5 class="fw-bold brand-color mb-2"><i class="bi bi-check2-square me-2"></i>Constraints</h5>
          <div class="card border-0 shadow-sm mb-4"><div class="table-responsive">
            <table class="table table-sm align-middle mb-0"><tbody>${otherCons}</tbody></table>
          </div></div>` : ""}
      </div>
    </div>`;
}

// ── cross-schema reference helper ───────────────────────────────────────────
// Schema $ref strings look like "eos_cli_config_gen#/keys/foo/keys/bar".
// Convert into a SchemaExplorer hash link to the equivalent flattened key_path
// in the target module so users can jump straight there.
function renderCrossRefRow(ref) {
  const [target, jsonPointer] = String(ref).split("#", 2);
  if (!target || !jsonPointer) return "";
  if (!Object.prototype.hasOwnProperty.call(SCHEMA_MODULES, target)) return "";
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
  const encodedTarget = encodeURIComponent(target);
  const encodedKeyPath = keyPath.split("/").map(encodeURIComponent).join("/");
  const link = keyPath
    ? `#/${encodedTarget}/${encodedKeyPath}`
    : `#/${encodedTarget}`;
  return `<tr><td class="px-3 fw-semibold small text-muted">Cross-schema</td><td><a href="${escapeAttr(link)}" class="link-brand"><code>${escapeHtml(target)}</code> → <code>${escapeHtml(keyPath || "(root)")}</code></a></td></tr>`;
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
  const lines = String(text).trim().split(/\n/);
  const parts = [];
  let paragraph = [];
  let list = [];

  function flushParagraph() {
    if (!paragraph.length) return;
    parts.push("<p class=\"mb-0\">" + formatMarkdownInline(paragraph.join(" "), q) + "</p>");
    paragraph = [];
  }

  function flushList() {
    if (!list.length) return;
    parts.push("<ul class=\"mb-0\">" + list.map(item => "<li>" + formatMarkdownInline(item, q) + "</li>").join("") + "</ul>");
    list = [];
  }

  for (const rawLine of lines) {
    const line = rawLine.trim();
    if (!line) {
      flushParagraph();
      flushList();
      continue;
    }
    const listMatch = line.match(/^[-*]\s+(.*)$/);
    if (listMatch) {
      flushParagraph();
      list.push(listMatch[1]);
    } else {
      flushList();
      paragraph.push(line);
    }
  }
  flushParagraph();
  flushList();
  return parts.join("") || escapeHtml("-");
}

function debounce(fn, ms) {
  let t;
  return (...args) => { clearTimeout(t); t = setTimeout(() => fn(...args), ms); };
}

// ── Reference view ───────────────────────────────────────────────────────

function referencePath(row) {
  return `.${displayPath(row.key_path)}`;
}

function referenceDefaultOptionLabel(item, idx) {
  if (item && typeof item === "object" && !Array.isArray(item)) {
    if (Array.isArray(item.platforms) && item.platforms.length) return item.platforms.join(", ");
    for (const key of ["name", "key", "type", "platform"]) {
      const value = item[key];
      if (value === null || value === undefined || typeof value === "object") continue;
      return String(value);
    }
  }
  return `Item ${idx + 1}`;
}

function referenceDefaultItemFields(item) {
  if (!(item && typeof item === "object") || Array.isArray(item)) return item;
  const fields = Object.fromEntries(Object.entries(item).filter(([key]) => key !== "platforms"));
  return Object.keys(fields).length ? fields : item;
}

function renderReferenceDefaultItem(item) {
  const fields = referenceDefaultItemFields(item);
  if (fields && typeof fields === "object" && !Array.isArray(fields)) {
    return renderDefaultObjectTable(fields, "schema-reference-default-table");
  }
  return renderDefaultFieldValue(fields);
}

function renderReferenceScalarList(items) {
  return `<ul class="schema-reference-default-list">${items.map(item => `<li>${renderDefaultScalar(item)}</li>`).join("")}</ul>`;
}

function renderReferenceDefaultContent(parts, id) {
  if (Array.isArray(parts.parsed)) {
    const allObjects = parts.parsed.every(item => item && typeof item === "object" && !Array.isArray(item));
    if (allObjects && parts.parsed.length > 1) {
      const options = parts.parsed.map((item, idx) => `<option value="${idx}">${escapeHtml(referenceDefaultOptionLabel(item, idx))}</option>`).join("");
      const items = parts.parsed.map((item, idx) => `
        <div class="schema-reference-default-item" data-reference-default-item="${idx}"${idx === 0 ? "" : " hidden"}>
          ${renderReferenceDefaultItem(item)}
        </div>`).join("");
      return `
        <label class="schema-reference-default-label" for="${id}-select">Option</label>
        <select class="schema-reference-default-select" id="${id}-select" data-reference-default-select data-reference-default-target="${id}-items">
          ${options}
        </select>
        <div class="schema-reference-default-items" id="${id}-items">
          ${items}
        </div>`;
    }
    if (allObjects && parts.parsed.length === 1) return `<div class="schema-reference-default-items">${renderReferenceDefaultItem(parts.parsed[0])}</div>`;
    return renderReferenceScalarList(parts.parsed);
  }

  if (parts.parsed && typeof parts.parsed === "object") {
    return `<div class="schema-reference-default-items">${renderReferenceDefaultItem(parts.parsed)}</div>`;
  }

  return "";
}

function renderReferenceDefaultValue(row) {
  const parts = defaultValueParts(row.default_value);
  if (!parts.hasValue || !parts.large || !parts.parseOk) return "";

  const id = `reference-default-${++_schemaRenderSeq}`;
  const content = renderReferenceDefaultContent(parts, id);
  if (!content) return "";

  return `
    <section class="schema-reference-default-browser" aria-labelledby="${id}-heading">
      <h2 id="${id}-heading">Default Value</h2>
      ${content}
    </section>`;
}

function renderReferenceDetail(row, module, isAll) {
  const constraints = yamlConstraints(row);
  const constraintsText = yamlRestrictionParts(row, constraints).join("; ");
  const primaryKey = isPrimaryKey(row);
  const lifecycle = row.removed
    ? `<span class="schema-detail-status text-muted ms-1">removed</span>`
    : row.deprecated
      ? `<span class="schema-detail-status text-muted ms-1">deprecated</span>`
      : "";
  const validValues = Array.isArray(constraints.valid_values) && constraints.valid_values.length
    ? `<h3>Valid Values</h3><div class="schema-reference-prose"><ul>${constraints.valid_values.map(value => `<li><code>${escapeHtml(String(value))}</code></li>`).join("")}</ul></div>`
    : "";
  const propertyRows = renderPropertyRows([
    { label: "Key Name", value: `<code>${escapeHtml(leafSegment(row.key_path))}</code>` },
    { label: "Type", value: escapeHtml(row.var_type || "-") },
    { label: "Primary Key", value: "Yes", show: primaryKey },
    { label: "Required", value: "Yes", show: schemaBool(row.required) && !primaryKey },
    { label: "Default", value: renderDefaultValue(row.default_value, { compact: true }), show: row.default_value !== null && row.default_value !== undefined && row.default_value !== "" },
    { label: "Value Restrictions", value: escapeHtml(constraintsText), show: !!constraintsText },
  ], "th");
  const descriptionHtml = row.description
    ? `<h2>Description</h2><div class="schema-reference-prose">${formatDescriptionMarkdown(row.description)}</div>`
    : "";
  return `
    <div class="schema-reference-detail-inner">
      <div class="schema-reference-breadcrumb"><code>${escapeHtml(displayPath(row.key_path))}</code></div>
      <h2>Key ${lifecycle}</h2>
      <div class="schema-reference-key-table-wrap">
        <table class="schema-reference-key-table">
          <tbody>
            ${propertyRows}
          </tbody>
        </table>
      </div>
      ${descriptionHtml}
      ${renderReferenceDefaultValue(row)}
      ${validValues}
    </div>`;
}

function renderReferenceResults(target, module, state, inputRows) {
  const isAll = module === "all";
  const rowsById = new Map(inputRows.map(row => [schemaRowId(row, module), row]));

  const groups = new Map();
  for (const row of inputRows) {
    const groupId = schemaGroupId(row, module);
    if (!groups.has(groupId)) groups.set(groupId, { module: rowModule(row, module), root: rootSegment(row.key_path), rows: [] });
    groups.get(groupId).rows.push(row);
  }
  const orderedGroups = [...groups.values()].sort((a, b) => `${a.module}:${a.root}`.localeCompare(`${b.module}:${b.root}`));
  const orderedRows = orderedGroups.flatMap(group => orderedSchemaRows(group.rows, module).rows);
  if (state.currentRowId && rowsById.has(state.currentRowId)) {
    state.referenceSelectedId = state.currentRowId;
  }
  if (!state.referenceSelectedId || !rowsById.has(state.referenceSelectedId)) {
    state.referenceSelectedId = schemaRowId(orderedRows[0] || inputRows[0], module);
  }
  const selected = rowsById.get(state.referenceSelectedId) || orderedRows[0] || inputRows[0];
  state.currentRowId = schemaRowId(selected, module);
  state.referenceSelectedId = state.currentRowId;

  const navRows = orderedGroups.map(group => {
    const hierarchy = orderedSchemaRows(group.rows, module);
    return hierarchy.rows.map(row => {
      const rowId = schemaRowId(row, module);
      const parentId = hierarchy.parentIds.get(rowId) || "";
      const depth = row.depth || 1;
      const isBranch = (hierarchy.childCount.get(rowId) || 0) > 0;
      const expanded = false;
      const rowStyle = `--schema-reference-depth: ${Math.max(0, depth - 1)};${depth > 1 ? " display: none;" : ""}`;
      const selectedClass = rowId === state.referenceSelectedId ? " active" : "";
      const moduleBadge = isAll && depth === 1 ? `<span class="schema-reference-module">${escapeHtml(SCHEMA_MODULES[row.module]?.name || row.module)}</span>` : "";
      return `
        <div class="schema-reference-nav-row${selectedClass}"
             data-row-id="${escapeAttr(rowId)}"
             data-parent-id="${escapeAttr(parentId)}"
             data-is-branch="${isBranch ? "1" : "0"}"
             data-expanded="${expanded ? "1" : "0"}"
             data-depth="${depth}"
             style="${rowStyle}">
          <button type="button" class="schema-reference-toggle" ${isBranch ? "" : "disabled"}>${isBranch ? `<i class="bi ${expanded ? "bi-chevron-down" : "bi-chevron-right"}"></i>` : ""}</button>
          <button type="button" class="schema-reference-nav-key" data-reference-select="${escapeAttr(rowId)}">
            <span class="schema-reference-file-icon"><i class="bi bi-file-earmark-text"></i></span>
            <span>${highlight(leafSegment(row.key_path), state.q)}</span>
            ${moduleBadge}
          </button>
        </div>`;
    }).join("");
  }).join("");

  target.innerHTML = `
    <div class="schema-reference-view">
      <aside class="schema-reference-nav" aria-label="Schema documentation navigation">
        ${navRows}
      </aside>
      <section class="schema-reference-detail" aria-live="polite">${renderReferenceDetail(selected, module, isAll)}</section>
    </div>`;

  function applyReferenceVisibility() {
    const nav = target.querySelector(".schema-reference-nav");
    const rows = [...nav.querySelectorAll(".schema-reference-nav-row")];
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

  function referenceRowById(rowId) {
    return [...target.querySelectorAll(".schema-reference-nav-row")].find(row => row.dataset.rowId === rowId) || null;
  }

  function setReferenceRowExpanded(row, expanded) {
    row.dataset.expanded = expanded ? "1" : "0";
    const toggle = row.querySelector(".schema-reference-toggle");
    if (toggle && !toggle.disabled) {
      toggle.innerHTML = `<i class="bi ${expanded ? "bi-chevron-down" : "bi-chevron-right"}"></i>`;
    }
  }

  function revealReferenceSelection() {
    const selectedRow = referenceRowById(state.referenceSelectedId);
    let parentId = selectedRow?.dataset.parentId || "";
    while (parentId) {
      const parent = referenceRowById(parentId);
      if (!parent) break;
      setReferenceRowExpanded(parent, true);
      parentId = parent.dataset.parentId;
    }
    applyReferenceVisibility();
    selectedRow?.scrollIntoView({ block: "nearest" });
  }

  target.querySelector(".schema-reference-nav")?.addEventListener("click", event => {
    const toggle = event.target.closest(".schema-reference-toggle");
    if (toggle && !toggle.disabled) {
      const row = toggle.closest(".schema-reference-nav-row");
      const open = row.dataset.expanded !== "1";
      row.dataset.expanded = open ? "1" : "0";
      toggle.innerHTML = `<i class="bi ${open ? "bi-chevron-down" : "bi-chevron-right"}"></i>`;
      applyReferenceVisibility();
      return;
    }
    const select = event.target.closest("[data-reference-select]");
    if (!select) return;
    state.referenceSelectedId = select.dataset.referenceSelect;
    state.currentRowId = state.referenceSelectedId;
    target.querySelectorAll(".schema-reference-nav-row.active").forEach(row => row.classList.remove("active"));
    select.closest(".schema-reference-nav-row")?.classList.add("active");
    const selectedRow = rowsById.get(state.referenceSelectedId);
    if (selectedRow) {
      const detail = target.querySelector(".schema-reference-detail");
      detail.innerHTML = renderReferenceDetail(selectedRow, module, isAll);
      detail.scrollTop = 0;
    }
  });
  revealReferenceSelection();
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

function yamlAnnotationScalar(value) {
  if (value === null) return "null";
  if (typeof value === "boolean") return value ? "true" : "false";
  if (typeof value === "number") return Number.isFinite(value) ? String(value) : `"${String(value)}"`;
  const stringValue = String(value);
  if (!stringValue) return '""';
  if (/^[A-Za-z0-9_./:@+-]+$/.test(stringValue) && !/^(true|false|null|yes|no|on|off)$/i.test(stringValue)) return stringValue;
  return JSON.stringify(stringValue);
}

function yamlAnnotationKey(key) {
  return /^[A-Za-z0-9_.-]+$/.test(key) ? key : JSON.stringify(key);
}

function yamlAnnotationDump(value, indentCount = 0) {
  const indent = " ".repeat(indentCount);
  if (Array.isArray(value)) {
    if (!value.length) return `${indent}[]\n`;
    return value.map(item => {
      if (item && typeof item === "object") {
        return `${indent}-\n${yamlAnnotationDump(item, indentCount + 2)}`;
      }
      return `${indent}- ${yamlAnnotationScalar(item)}\n`;
    }).join("");
  }
  if (value && typeof value === "object") {
    const entries = Object.entries(value);
    if (!entries.length) return `${indent}{}\n`;
    return entries.map(([key, item]) => {
      const renderedKey = yamlAnnotationKey(key);
      if (item && typeof item === "object") {
        return `${indent}${renderedKey}:\n${yamlAnnotationDump(item, indentCount + 2)}`;
      }
      return `${indent}${renderedKey}: ${yamlAnnotationScalar(item)}\n`;
    }).join("");
  }
  return `${indent}${yamlAnnotationScalar(value)}\n`;
}

function yamlDefaultAnnotation(row) {
  if (!row.default_value) return "";
  try {
    const value = JSON.parse(row.default_value);
    const isCollection = Array.isArray(value) || (value && typeof value === "object");
    if (!isCollection) return "";
    const collectionLength = Array.isArray(value) ? value.length : Object.keys(value).length;
    if (collectionLength <= 1 && String(row.default_value).length <= 40) return "";
    return yamlAnnotationDump({ [yamlKeySegment(row.key_path)]: value }).trimEnd();
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
  if (isPrimaryKey(row)) parts.push(row.unique_key ? "primary key; unique" : "primary key");
  else if (row.required) parts.push("required");
  return parts.filter(Boolean);
}

function yamlListItemParts(row) {
  const itemConstraints = yamlConstraints(row).items || {};
  const itemType = itemConstraints.type || "any";
  const itemRow = { ...row, var_type: itemType };
  const parts = [itemType];
  parts.push(...yamlRestrictionParts(itemRow, itemConstraints));
  return parts.filter(Boolean);
}

function yamlDescriptionLines(row, indentCount) {
  if (!row.description) return [];
  const commentIndent = " ".repeat(indentCount);
  const lines = String(row.description).trim().split(/\n/).map(line => `${commentIndent}# ${line.trimEnd()}`);
  return ["", ...lines];
}

function yamlHighlightYamlAnnotationComment(commentPart, annotationIdPrefix) {
  const escapedComment = escapeHtml(commentPart);
  if (!annotationIdPrefix) return escapedComment;
  return escapedComment.replace(/\((\d+)\)!$/, (_match, number) => {
    const targetId = `${annotationIdPrefix}-annotation-${number}`;
    return `<button type="button" class="se-yaml-annotation-link" data-yaml-annotation-target="${escapeAttr(targetId)}" aria-label="Show default value annotation ${escapeAttr(number)}">+</button>`;
  });
}

function yamlHighlightValue(rawValue, annotationIdPrefix = "") {
  const commentIndex = rawValue.indexOf(" #");
  const valuePart = commentIndex === -1 ? rawValue : rawValue.slice(0, commentIndex);
  const commentPart = commentIndex === -1 ? "" : rawValue.slice(commentIndex);
  const html = escapeHtml(valuePart).replace(/(&lt;.*?&gt;)/g, '<span class="se-yaml-placeholder">$1</span>')
    .replace(/(&quot;[^&]*?&quot;)/g, '<span class="se-yaml-string">$1</span>')
    .replace(/\b(true|false|null)\b/g, '<span class="se-yaml-literal">$1</span>')
    .replace(/(?<![-\w])(-?\d+(?:\.\d+)?)(?![-\w])/g, '<span class="se-yaml-number">$1</span>');
  return html + (commentPart ? `<span class="se-yaml-comment">${yamlHighlightYamlAnnotationComment(commentPart, annotationIdPrefix)}</span>` : "");
}

function yamlHighlightLine(line, annotationIdPrefix = "") {
  if (!line) return "";
  const commentMatch = line.match(/^(\s*#.*)$/);
  if (commentMatch) return `<span class="se-yaml-comment">${escapeHtml(line)}</span>`;

  const fieldMatch = line.match(/^(\s*)(-\s*)?([^:#]+:)(.*)$/);
  if (!fieldMatch) return escapeHtml(line);
  const [, indent, listMarker = "", key, value] = fieldMatch;
  return `${escapeHtml(indent)}${listMarker ? `<span class="se-yaml-marker">${escapeHtml(listMarker)}</span>` : ""}<span class="se-yaml-key">${escapeHtml(key)}</span>${yamlHighlightValue(value, annotationIdPrefix)}`;
}

function yamlHighlightBlock(text, annotationIdPrefix = "") {
  return String(text).split("\n").map(line => yamlHighlightLine(line, annotationIdPrefix)).join("\n");
}

function renderYamlResults(target, module, state, inputRows) {
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
  function yamlLine(text, row = null) { return row ? { text, rowId: schemaRowId(row, module) } : text; }
  function yamlLineHtml(line, annotationIdPrefix) {
    const text = typeof line === "string" ? line : line.text;
    const rowId = typeof line === "string" ? "" : line.rowId;
    const activeClass = rowId && rowId === state.currentRowId ? " active" : "";
    const rowAttr = rowId ? ` data-yaml-row-id="${escapeAttr(rowId)}"` : "";
    return `<span class="schema-yaml-line${activeClass}"${rowAttr}>${yamlHighlightLine(text, annotationIdPrefix)}</span>`;
  }
  function registerYamlAnnotation(context, row) {
    const content = yamlDefaultAnnotation(row);
    if (!content) return "";
    const number = context.annotations.length + 1;
    context.annotations.push({ number, content });
    return number;
  }
  function yamlPropertiesComment(row, annotationNumber = "") {
    const parts = yamlValueParts(row, false);
    if (annotationNumber && parts.length) return ` # ${parts.join("; ")} (${annotationNumber})!`;
    if (annotationNumber) return ` # (${annotationNumber})!`;
    return parts.length ? ` # ${parts.join("; ")}` : "";
  }

  function renderListChildren(context, lines, childRows, listIndent) {
    childRows.forEach((child, idx) => {
      if (idx === 0) renderYamlRow(context, lines, child, listIndent + 2, true);
      else renderYamlRow(context, lines, child, listIndent + 4, false);
    });
  }

  function renderYamlRow(context, lines, row, indentCount, listItem = false) {
    const type = yamlBaseType(row);
    const childRows = childrenOf(row);
    lines.push(...yamlDescriptionLines(row, indentCount));
    const prefix = yamlLinePrefix(indentCount, listItem);
    const fieldName = yamlFieldName(row);
    const annotationNumber = registerYamlAnnotation(context, row);

    if (type === "list") {
      lines.push(yamlLine(prefix + fieldName + ":" + yamlPropertiesComment(row, annotationNumber), row));
      if (childRows.length) renderListChildren(context, lines, childRows, indentCount);
      else lines.push(yamlLine(" ".repeat(indentCount + 2) + "- <" + yamlListItemParts(row).join("; ") + ">", row));
      return;
    }

    if (type === "dict") {
      const fallback = childRows.length ? "" : " <dict>";
      lines.push(yamlLine(`${prefix}${fieldName}:${fallback}${yamlPropertiesComment(row, annotationNumber)}`, row));
      childRows.forEach(child => renderYamlRow(context, lines, child, indentCount + (listItem ? 4 : 2)));
      return;
    }

    lines.push(yamlLine(`${prefix}${fieldName}: <${yamlValueParts(row, true).join("; ")}>`, row));
  }

  function renderYamlAnnotations(context, annotationIdPrefix) {
    if (!context.annotations.length) return "";
    return `
      <ol class="schema-yaml-annotations">
        ${context.annotations.map(annotation => `
          <li id="${escapeAttr(`${annotationIdPrefix}-annotation-${annotation.number}`)}">
            <div class="schema-yaml-annotation-title">Default Value</div>
            <pre class="schema-yaml-block schema-yaml-annotation-block"><code>${yamlHighlightBlock(annotation.content)}</code></pre>
          </li>`).join("")}
      </ol>`;
  }

  const topRows = sourceRows.filter(row => !row.parent_path || !rowsByPath.has(`${row.module}:${row.parent_path}`));
  const groupedRows = new Map();
  for (const row of topRows) {
    const groupId = schemaGroupId(row, module);
    if (!groupedRows.has(groupId)) {
      groupedRows.set(groupId, { root: rootSegment(row.key_path), module: rowModule(row, module), rows: [] });
    }
    groupedRows.get(groupId).rows.push(row);
  }

  const selectedRow = sourceRows.find(row => schemaRowId(row, module) === state.currentRowId) || null;
  const selectedGroupId = selectedRow ? schemaGroupId(selectedRow, module) : "";
  const idPrefix = `y${++_schemaRenderSeq}`;
  const groupsHtml = [...groupedRows.entries()].sort(([, a], [, b]) => `${a.module}:${a.root}`.localeCompare(`${b.module}:${b.root}`)).map(([groupId, group], idx) => {
    const lines = [];
    const context = { annotations: [] };
    group.rows.forEach(row => renderYamlRow(context, lines, row, 0));
    const id = `${idPrefix}-group-${idx}`;
    const isSelectedGroup = groupId === selectedGroupId;
    const yamlHtml = lines.length ? lines.map(line => yamlLineHtml(line, id)).join("\n") : yamlHighlightLine("# No YAML fields match.", id);
    const groupModuleBadge = module === "all" ? `<span class="badge ${group.module === "eos_designs" ? "bg-primary" : "bg-success"} ms-1" style="font-size: 0.6rem;">${escapeHtml(SCHEMA_MODULES[group.module]?.name || group.module)}</span>` : "";
    return `
      <div class="schema-group" data-group-id="${id}" data-schema-group-id="${escapeAttr(groupId)}">
        <div class="schema-group-header" data-bs-toggle="collapse" data-bs-target="#${id}" aria-expanded="${isSelectedGroup ? "true" : "false"}" aria-controls="${id}">
          <i class="bi ${isSelectedGroup ? "bi-chevron-down" : "bi-chevron-right"} collapse-icon"></i>
          <code class="schema-key-code schema-yaml-group-key">${escapeHtml(group.root)}</code>
          ${groupModuleBadge}
        </div>
        <div class="collapse${isSelectedGroup ? " show" : ""}" id="${id}">
          <pre class="schema-yaml-block"><code>${yamlHtml}</code></pre>
          ${renderYamlAnnotations(context, id)}
        </div>
      </div>`;
  }).join("");

  target.innerHTML = `
    <div class="schema-results-scroll">
      ${groupsHtml}
    </div>`;

  function rememberYamlLine(line) {
    if (!line?.dataset.yamlRowId) return;
    state.currentRowId = line.dataset.yamlRowId;
    state.referenceSelectedId = state.currentRowId;
    target.querySelectorAll(".schema-yaml-line.active").forEach(item => item.classList.remove("active"));
    line.classList.add("active");
  }

  const activeLine = target.querySelector(".schema-yaml-line.active");
  activeLine?.scrollIntoView({ block: "center" });
  target.querySelector(".schema-results-scroll")?.addEventListener("click", event => {
    rememberYamlLine(event.target.closest("[data-yaml-row-id]"));
  });

  const rememberYamlScroll = debounce(block => {
    const blockTop = block.getBoundingClientRect().top;
    const visibleLine = [...block.querySelectorAll("[data-yaml-row-id]")].find(line => line.getBoundingClientRect().bottom >= blockTop);
    rememberYamlLine(visibleLine);
  }, 80);
  target.querySelectorAll(".schema-yaml-block").forEach(block => {
    block.addEventListener("scroll", () => rememberYamlScroll(block));
  });
}

// ── embed mounting ──────────────────────────────────────────────────────────
//
// Renders a scoped schema explorer inside any <schema-explorer> element on the page.
// The element is treated like a sealed component: docs author drops the tag,
// the SPA fills it in.
//
// Supported data attributes:
//   module   — "eos_designs" | "eos_cli_config_gen" | "all" (default: "eos_designs")
//   root     — key_path prefix; only show that subtree (e.g. "router_bgp"). Optional.
//   view     — "reference" | "yaml" (default: "reference")
//   height   — CSS max-height for the scroll container (default: "600px")
//   chrome   — "compact" | "none" (default: "compact").

function _embedAttr(el, name, fallback) {
  return el.getAttribute(`data-${name}`) || el.getAttribute(name) || fallback;
}

function failEmbed(el, msg) {
  el.innerHTML = `<div class="alert alert-danger m-2 small"><i class="bi bi-exclamation-triangle me-1"></i>${escapeHtml(msg)}</div>`;
}

async function mountEmbed(el) {
  const module  = _embedAttr(el, "module", "eos_designs");
  const root    = _embedAttr(el, "root", "");
  const view    = _embedAttr(el, "view", "reference");
  if (!["reference", "yaml"].includes(view)) throw new Error("Unsupported schema explorer view: " + view);
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

  const db = await getDb();
  const rootOptions = getRootOptions(db, module);
  const defaultRootStateValue = defaultRootState(rootOptions, root, module);
  const defaultRootSelection = defaultRootStateValue.selection;
  const rootOptionsHtml = rootOptions.map(row => {
    const value = rootOptionValue(row, module);
    const label = module === "all" ? `${SCHEMA_MODULES[row.module]?.name || row.module}: ${displayPath(row.key_path)}` : displayPath(row.key_path);
    return `<option value="${escapeAttr(value)}"${value === defaultRootSelection ? " selected" : ""}>${escapeHtml(label)}</option>`;
  }).join("");
  const hasDefaultRootOption = !defaultRootSelection || rootOptions.some(row => rootOptionValue(row, module) === defaultRootSelection);
  const rootFallbackOption = hasDefaultRootOption ? "" : `<option value="${escapeAttr(defaultRootSelection)}" selected>${escapeHtml(displayPath(defaultRootStateValue.root))}</option>`;
  const idPrefix = `embed-${++_schemaRenderSeq}`;

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
    docTable: "",
    searchScope: "both",
    view,
    target: el.querySelector(".schema-embed-results"),
    embedCompact: true,
  };

  function renderEmbedResults() {
    renderResults(db, module, state);
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
