import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import test from "node:test";
import vm from "node:vm";

const here = dirname(fileURLToPath(import.meta.url));
const sanitizePath = join(here, "..", "static", "js", "sanitize.js");

function loadSanitize() {
  const context = { globalThis: {} };
  context.globalThis = context;
  vm.createContext(context);
  vm.runInContext(readFileSync(sanitizePath, "utf8"), context);
  return context.SchemaExplorerSanitize;
}

test("escapeHtml neutralizes HTML metacharacters", () => {
  const { escapeHtml } = loadSanitize();
  assert.equal(escapeHtml(`<img src=x onerror=alert(1)>"'&`), "&lt;img src=x onerror=alert(1)&gt;&quot;&#39;&amp;");
});

test("escapeAttr escapes quotes for attribute contexts", () => {
  const { escapeAttr } = loadSanitize();
  assert.equal(escapeAttr(`"><script`), "&quot;&gt;&lt;script");
});

test("renderCrossRefRow builds encoded hash links and escapes labels", () => {
  const { renderCrossRefRow } = loadSanitize();
  const modules = { eos_cli_config_gen: {}, eos_designs: {} };
  const row = renderCrossRefRow('eos_cli_config_gen#/keys/router_bgp/keys/neighbors', modules);
  assert.match(row, /href="#\/eos_cli_config_gen\/router_bgp\.neighbors"/);
  assert.match(row, /<code>eos_cli_config_gen<\/code>/);
  assert.doesNotMatch(row, /<script/);
});

test("renderCrossRefRow rejects unknown modules and javascript: refs", () => {
  const { renderCrossRefRow } = loadSanitize();
  assert.equal(renderCrossRefRow("evil_module#/keys/foo", { eos_designs: {} }), "");
  assert.equal(renderCrossRefRow('javascript:alert(1)#/', { eos_designs: {} }), "");
});

test("sanitize.js passes node syntax check", () => {
  const result = spawnSync("node", ["--check", sanitizePath], { encoding: "utf8" });
  assert.equal(result.status, 0, result.stderr || result.stdout);
});
