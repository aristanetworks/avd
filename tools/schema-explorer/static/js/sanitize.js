/* Schema Explorer HTML escaping and cross-schema link helpers.
 *
 * Loaded before app.js in the standalone SPA and via MkDocs extra_javascript.
 * Keep free of DOM or sql.js dependencies so node --check and fixture tests stay simple.
 */
(function (global) {
  "use strict";

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, (character) => ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#39;",
    }[character]));
  }

  function escapeAttr(value) {
    return escapeHtml(value).replace(/"/g, "&quot;");
  }

  /** Convert a schema $ref into a hash-routed table row with escaped text and href. */
  function renderCrossRefRow(ref, allowedModules) {
    const [target, jsonPointer] = String(ref).split("#", 2);
    if (!target || !jsonPointer) return "";
    if (!allowedModules || !Object.prototype.hasOwnProperty.call(allowedModules, target)) return "";
    const segments = jsonPointer.split("/").filter(Boolean);
    const parts = [];
    for (let index = 0; index < segments.length; index += 1) {
      const segment = segments[index];
      if (segment === "keys") {
        // skip — next segment is the key name
      } else if (segment === "items") {
        if (parts.length) parts[parts.length - 1] += "[]";
      } else {
        parts.push(segment);
      }
    }
    const keyPath = parts.join(".");
    const encodedTarget = encodeURIComponent(target);
    const encodedKeyPath = keyPath.split("/").map(encodeURIComponent).join("/");
    const link = keyPath ? `#/${encodedTarget}/${encodedKeyPath}` : `#/${encodedTarget}`;
    return `<tr><td class="px-3 fw-semibold small text-muted">Cross-schema</td><td><a href="${escapeAttr(link)}" class="link-brand"><code>${escapeHtml(target)}</code> → <code>${escapeHtml(keyPath || "(root)")}</code></a></td></tr>`;
  }

  global.SchemaExplorerSanitize = {
    escapeHtml,
    escapeAttr,
    renderCrossRefRow,
  };
  global.escapeHtml = escapeHtml;
  global.escapeAttr = escapeAttr;
})(typeof globalThis !== "undefined" ? globalThis : this);
