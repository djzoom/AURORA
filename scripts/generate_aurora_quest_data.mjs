import { promises as fs } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const repoRoot = path.resolve(__dirname, "..");
const courseDir = path.join(repoRoot, "docs", "current", "course");
const sourcePath = path.join(courseDir, "LEARNING_PLAN.md");
const outputPath = path.join(repoRoot, "aurora-quest", "src", "course-snapshot.generated.js");

function cleanText(value) {
  return value.replace(/\s+/g, " ").replace(/\s*([：:，,。！？;；])\s*/g, "$1").trim();
}

function stripMarkdown(value) {
  return cleanText(value.replace(/[`*]/g, ""));
}

function sectionBetween(text, startMarker, endMarker) {
  const start = text.indexOf(startMarker);
  if (start === -1) return "";
  const end = endMarker ? text.indexOf(endMarker, start + startMarker.length) : -1;
  return text.slice(start, end === -1 ? undefined : end);
}

function parseOpeningLessons(block) {
  const rows = [];
  for (const line of block.split(/\r?\n/)) {
    const match = line.match(/^\|\s+`([^`]+)`\s+\|\s+(.+?)\s+\|$/);
    if (!match) continue;
    const title = stripMarkdown(match[2]);
    rows.push({
      code: match[1].match(/(L\d+)/)?.[1] ?? match[1],
      path: match[1],
      title,
    });
  }
  return rows;
}

function parseFoundationTracks(block) {
  const rows = [];
  for (const line of block.split(/\r?\n/)) {
    const match = line.match(/^\|\s+`([^`]+)`\s+([^\|]+?)\s+\|\s+([^|]+?)\s+\|\s+([^|]+?)\s+\|$/);
    if (!match) continue;
    rows.push({
      path: cleanText(match[1]),
      range: cleanText(match[2]),
      title: cleanText(match[3]),
      service: cleanText(match[4]),
    });
  }
  return rows;
}

function parseMonthlyPhases(block) {
  const rows = [];
  for (const line of block.split(/\r?\n/)) {
    const match = line.match(/^\|\s+\*\*(\d+)\*\*\s+\|\s+([^|]+?)\s+\|\s+\*?([^|*]+?)\*?\s+\|\s+([^|]+?)\s+\|$/);
    if (!match) continue;
    rows.push({
      month: Number(match[1]),
      title: cleanText(match[2]),
      deliverable: cleanText(match[3]),
      checkpoint: cleanText(match[4]),
    });
  }
  return rows;
}

function parseWeeklyChecklists() {
  return fs.readdir(courseDir).then(async (entries) => {
    const files = entries.filter((entry) => /^week-\d+-checklist\.md$/.test(entry)).sort();
    const output = [];
    for (const file of files) {
      const fullPath = path.join(courseDir, file);
      const text = await fs.readFile(fullPath, "utf8");
      const heading = text.split(/\r?\n/).find((line) => line.startsWith("# ")) ?? file;
      const headingMatch = heading.match(/^#\s+(L\d+[–-]L?\d+)\s+.*?[—-]\s+(.+)$/u);
      const targetLines = [];
      let collectingTarget = false;
      for (const line of text.split(/\r?\n/)) {
        if (!collectingTarget && /^>\s*目标[:：]/.test(line)) {
          collectingTarget = true;
          targetLines.push(line.replace(/^>\s*目标[:：]\s*/, ""));
          continue;
        }
        if (collectingTarget) {
          if (/^>\s+/.test(line)) {
            targetLines.push(line.replace(/^>\s+/, ""));
            continue;
          }
          break;
        }
      }
      const target = cleanText(targetLines.join(" "));
      const lessonMatches = [...text.matchAll(/^##\s+(L[\d–-]+)\s+[—-]\s+(.+)$/gmu)];
      output.push({
        file: `docs/current/course/${file}`,
        heading: cleanText(heading.replace(/^#\s+/, "")),
        range: headingMatch?.[1] ?? lessonMatches[0]?.[1] ?? file,
        title: headingMatch?.[2] ?? cleanText(heading.replace(/^#\s+/, "")),
        target,
        lessons: lessonMatches.map((match) => ({
          range: match[1],
          title: cleanText(match[2]),
        })),
      });
    }
    return output;
  });
}

async function main() {
  const learningPlan = await fs.readFile(sourcePath, "utf8");
  const courseTitle = learningPlan.match(/^#\s+(.+)$/m)?.[1]?.trim() ?? "Aurora 学习计划";
  const subtitle =
    "一条从开场五课走向 FFT、Whisper、RAG 和终局整合的实战路线。";

  const openingLessons = parseOpeningLessons(
    sectionBetween(learningPlan, "**⓪ 开场五课**", "**① 数学地基**"),
  );
  const foundationTracks = parseFoundationTracks(
    sectionBetween(learningPlan, "**① 数学地基**", "## 4."),
  );
  const monthlyPhases = parseMonthlyPhases(
    sectionBetween(
      learningPlan,
      "## 3. 6 个月重排（深度优先）",
      "## 3.5 前导课程（代码优先）",
    ),
  );
  const weeklyCheckpoints = await parseWeeklyChecklists();

  const sourceFiles = [
    "docs/current/course/LEARNING_PLAN.md",
    "docs/current/course/GETTING_STARTED.md",
    ...weeklyCheckpoints.map((entry) => entry.file),
  ];

  const data = {
    title: courseTitle,
    subtitle,
    openingLessons,
    foundationTracks,
    monthlyPhases,
    weeklyCheckpoints,
    sourceFiles,
  };

  const code = `export const courseSnapshot = ${JSON.stringify(data, null, 2)};\n\nexport default courseSnapshot;\n`;
  await fs.writeFile(outputPath, code, "utf8");
  console.log(`wrote ${path.relative(repoRoot, outputPath)}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
