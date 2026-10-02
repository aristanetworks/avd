import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";
import vm from "node:vm";

const here = dirname(fileURLToPath(import.meta.url));
const appPath = join(here, "..", "static", "js", "app.js");
const HELPERS_START = "// sanitize-helpers-start";
const HELPERS_END = "// sanitize-helpers-end";

function loadSanitizeHelpers() {
  const source = readFileSync(appPath, "utf8");
  const start = source.indexOf(HELPERS_START);
  const end = source.indexOf(HELPERS_END);
  assert.notEqual(start, -1, "sanitize helper block start marker missing from app.js");
  assert.notEqual(end, -1, "sanitize helper block end marker missing from app.js");
  assert.ok(end > start, "sanitize helper markers out of order in app.js");
  const helperSource = source.slice(start + HELPERS_START.length, end);
  const context = { globalThis: {} };
  context.globalThis = context;
  vm.createContext(context);
  vm.runInContext(
    `${helperSource}\n;globalThis.SchemaExplorerSanitize = { escapeHtml, escapeAttr, renderCrossRefRow };`,
    context,
  );
  return context.SchemaExplorerSanitize;
}

test("escapeHtml neutralizes HTML metacharacters", () => {
  const { escapeHtml } = loadSanitizeHelpers();
  assert.equal(escapeHtml(`<img src=x onerror=alert(1)>"'&`), "&lt;img src=x onerror=alert(1)&gt;&quot;&#39;&amp;");
});

test("escapeAttr escapes quotes for attribute contexts", () => {
  const { escapeAttr } = loadSanitizeHelpers();
  assert.equal(escapeAttr(`"><script`), "&quot;&gt;&lt;script");
});

test("renderCrossRefRow builds encoded hash links and escapes labels", () => {
  const { renderCrossRefRow } = loadSanitizeHelpers();
  const modules = { eos_cli_config_gen: {}, eos_designs: {} };
  const row = renderCrossRefRow("eos_cli_config_gen#/keys/router_bgp/keys/neighbors", modules);
  assert.match(row, /href="#\/eos_cli_config_gen\/router_bgp\.neighbors"/);
  assert.match(row, /<code>eos_cli_config_gen<\/code>/);
  assert.doesNotMatch(row, /<script/);
});

test("renderCrossRefRow rejects unknown modules and javascript: refs", () => {
  const { renderCrossRefRow } = loadSanitizeHelpers();
  assert.equal(renderCrossRefRow("evil_module#/keys/foo", { eos_designs: {} }), "");
  assert.equal(renderCrossRefRow("javascript:alert(1)#/", { eos_designs: {} }), "");
});
