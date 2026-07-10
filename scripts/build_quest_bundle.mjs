// scripts/build_quest_bundle.mjs — bundle Aurora Quest into a single self-contained HTML file.
//
// The playable app under aurora-quest/ is a multi-file ES-module site (index.html +
// styles.css + src/*.js modules). ES modules require an HTTP server, so a double-clicked
// file:// copy will not run. This script concatenates the modules in dependency order,
// strips the module syntax, and inlines everything (CSS + JS) into ONE HTML file that
// runs from file:// with no server — handy for sharing, archiving, or publishing as a
// hosted artifact.
//
// Constraint this relies on: modules use named imports/exports only (no `import * as ns`,
// no `export { ... }` lists, no re-exports), and top-level identifiers are unique across
// all modules — so strip-and-concatenate inside one IIFE is semantically equivalent to
// the module graph. The stripper handles multi-line `import { a, b } from "..."` blocks.
//
// It emits two files:
//   aurora-quest/dist/aurora-quest.html      — full standalone document (double-click to play)
//   aurora-quest/dist/aurora-quest.body.html — body-only fragment (for embedding hosts that
//                                              supply their own <head>/<body> skeleton)
//
// Usage:  node scripts/build_quest_bundle.mjs
import { promises as fs } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, "..");
const questDir = path.join(repoRoot, "aurora-quest");
const distDir = path.join(questDir, "dist");

// Dependency order: leaves first, entry last.
const MODULE_ORDER = [
  "src/course-snapshot.generated.js",
  "src/data/quests.js",
  "src/sprites.js",
  "src/audio.js",
  "src/state.js",
  "src/ui.js",
  "src/app.js",
];

function stripModuleSyntax(code) {
  return code
    // drop imports, incl. multi-line `import { a,\n b } from "...";`
    // ([^;] cannot cross the terminating semicolon, so each match is one statement)
    .replace(/^import[^;]*from\s*["'][^"']+["'];/gm, "")
    .replace(/^export default .*$/gm, "") // drop default re-exports
    .replace(/^export (const|let|var|function|class) /gm, "$1 "); // unwrap named exports
}

async function main() {
  const [indexHtml, css] = await Promise.all([
    fs.readFile(path.join(questDir, "index.html"), "utf8"),
    fs.readFile(path.join(questDir, "styles.css"), "utf8"),
  ]);

  const modules = await Promise.all(
    MODULE_ORDER.map(async (rel) => {
      const code = await fs.readFile(path.join(questDir, rel), "utf8");
      const stripped = stripModuleSyntax(code).trim();
      if (/^\s*(import|export)\b/m.test(stripped) || stripped.includes('from "./')) {
        throw new Error(`unstripped module syntax remains in ${rel}`);
      }
      return `// ---- ${rel} ----\n${stripped}`;
    }),
  );

  const bundledScript = `(() => {\n"use strict";\n${modules.join("\n\n")}\n})();`;

  // Extract the <body> inner markup from index.html and drop the external <script> tag.
  const bodyMatch = indexHtml.match(/<body>([\s\S]*?)<\/body>/i);
  if (!bodyMatch) throw new Error("could not find <body> in index.html");
  const bodyInner = bodyMatch[1]
    .replace(/\s*<script type="module"[^>]*><\/script>/i, "")
    .trim();

  const styleTag = `<style>\n${css.trim()}\n</style>`;
  const scriptTag = `<script>\n${bundledScript}\n</script>`;

  const bodyFragment = `${styleTag}\n${bodyInner}\n${scriptTag}\n`;

  const standalone = `<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
    <meta name="description" content="Aurora Quest — AURORA 课程的 8-bit 辅助教学 RPG。单文件离线版，双击即玩。" />
    <meta name="theme-color" content="#08111f" />
    <title>Aurora Quest | AURORA 辅助课程 RPG</title>
    ${styleTag}
  </head>
  <body>
    ${bodyInner}
    ${scriptTag}
  </body>
</html>
`;

  await fs.mkdir(distDir, { recursive: true });
  await fs.writeFile(path.join(distDir, "aurora-quest.html"), standalone, "utf8");
  await fs.writeFile(path.join(distDir, "aurora-quest.body.html"), bodyFragment, "utf8");

  const kb = (s) => `${(Buffer.byteLength(s, "utf8") / 1024).toFixed(1)} KB`;
  console.log(`wrote aurora-quest/dist/aurora-quest.html       (${kb(standalone)})`);
  console.log(`wrote aurora-quest/dist/aurora-quest.body.html  (${kb(bodyFragment)})`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
