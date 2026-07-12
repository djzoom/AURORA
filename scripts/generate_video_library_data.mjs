// 把 docs/current/course/VIDEO_LIBRARY.md（视频资料库，单一数据源）解析成
// aurora-quest/src/video-library.generated.js，供 aurora-quest/video-library.html
// 渲染可搜索、可筛选的片单。与 generate_aurora_quest_data.mjs 同一套路：
// Markdown 是标准答案，这里只做机械转换，不做内容加工。
import { promises as fs } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const repoRoot = path.resolve(__dirname, "..");
const sourcePath = path.join(repoRoot, "docs", "current", "course", "VIDEO_LIBRARY.md");
const outputPath = path.join(repoRoot, "aurora-quest", "src", "video-library.generated.js");

// 只有这些 ## 章节里的 ### 才是资源条目（导读章节没有 ###，但显式判定更稳）。
const PHASE_HEADING = /^## (Phase .+|aurora\.tts .+)$/;

const FIELD_KEYS = {
  "讲师/机构": "instructor",
  链接: "links",
  类型: "type",
  难度: "difficulty",
  语言: "language",
  时长: "duration",
  覆盖: "covers",
  "对齐 Aurora": "align",
  为何契合: "why",
};

function cleanText(value) {
  return value.replace(/\s+/g, " ").trim();
}

// 字段值里去掉粗体/行内代码等 Markdown 记号（页面按纯文本渲染）。
function stripMarkdown(value) {
  return cleanText(value.replace(/\*\*|[`]/g, ""));
}

// 一行 bullet 可能包含多个 `**字段**: 值`（用 ` · ` 连接的紧凑写法），逐段拆开。
function parseFieldLine(line, entry) {
  const body = line.replace(/^-\s*/, "");
  const segments = body.split(/\s·\s(?=\*\*)/);
  for (const segment of segments) {
    const match = segment.match(/^\*\*(.+?)\*\*[:：]\s*(.*)$/s);
    if (!match) continue;
    const key = FIELD_KEYS[cleanText(match[1])];
    if (key) entry[key] = key === "links" ? cleanText(match[2]) : stripMarkdown(match[2]);
  }
}

function extractUrls(text) {
  return [...new Set(text.match(/https?:\/\/[^\s()<>）｜|]+/g) ?? [])].map((url) =>
    url.replace(/[.,;:：。）」』]+$/, "")
  );
}

function urlLabel(url) {
  if (/[?&]list=/.test(url)) return "播放列表";
  if (/youtube\.com\/(watch|shorts)|youtu\.be\//.test(url)) return "视频";
  if (/youtube\.com\/(@|c\/|channel\/|user\/)/.test(url)) return "频道";
  if (/github\.com/.test(url)) return "代码";
  if (/bilibili\.com/.test(url)) return "B站";
  try {
    return new URL(url).hostname.replace(/^www\./, "");
  } catch {
    return "链接";
  }
}

function parseLibrary(markdown) {
  const phases = [];
  const items = [];
  let currentPhase = null;
  let entry = null;

  const flush = () => {
    if (!entry) return;
    const searchable = [
      entry.title,
      entry.instructor,
      entry.covers,
      entry.align,
      entry.why,
      entry.type,
    ]
      .filter(Boolean)
      .join(" ")
      .toLowerCase();
    const difficulty = entry.difficulty ?? "";
    const language = entry.language ?? "";
    items.push({
      ...entry,
      urls: extractUrls(entry.links ?? "").map((url) => ({ url, label: urlLabel(url) })),
      topPick: entry.topPick,
      unverified: /⚠️/.test(Object.values(entry).join(" ")),
      diffLevels: ["入门", "进阶", "高级"].filter((level) => difficulty.includes(level)),
      langTags: [
        /中文|中英/.test(language) ? "中文" : null,
        /英文|中英/.test(language) ? "英文" : null,
      ].filter(Boolean),
      searchable,
    });
    entry = null;
  };

  for (const rawLine of markdown.split(/\r?\n/)) {
    const line = rawLine.trimEnd();
    const phaseMatch = line.match(PHASE_HEADING);
    if (line.startsWith("## ")) {
      flush();
      currentPhase = phaseMatch ? cleanText(phaseMatch[1]) : null;
      if (currentPhase && !phases.includes(currentPhase)) phases.push(currentPhase);
      continue;
    }
    if (line.startsWith("### ") && currentPhase) {
      flush();
      const rawTitle = cleanText(line.slice(4));
      entry = {
        title: cleanText(rawTitle.replace(/🥇/g, "")),
        topPick: rawTitle.includes("🥇"),
        phase: currentPhase,
      };
      continue;
    }
    if (entry && line.startsWith("- **")) parseFieldLine(line, entry);
  }
  flush();
  return { phases, items };
}

async function main() {
  const markdown = await fs.readFile(sourcePath, "utf8");
  const { phases, items } = parseLibrary(markdown);
  if (items.length < 50) {
    throw new Error(`条目数异常（${items.length} < 50）——VIDEO_LIBRARY.md 结构可能变了`);
  }
  const payload = {
    source: "docs/current/course/VIDEO_LIBRARY.md",
    count: items.length,
    phases,
    items,
  };
  const banner =
    "// 自动生成：node scripts/generate_video_library_data.mjs（勿手改，改 VIDEO_LIBRARY.md）\n";
  await fs.writeFile(
    outputPath,
    `${banner}export const videoLibrary = ${JSON.stringify(payload, null, 2)};\n`,
    "utf8"
  );
  console.log(`✅ ${items.length} 条资源（${phases.length} 个阶段）→ ${path.relative(repoRoot, outputPath)}`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
