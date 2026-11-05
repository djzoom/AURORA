// 进度卡 —— 把视频资料库的打卡进度画到 1080×1350 的画布上（小红书 / Instagram 故事比例），
// 像素风，带仓库名与二维码，下载成 PNG。纯 Canvas 2D，不引任何外部资源。

import { GROWTH } from "./growth.js";

const W = 1080;
const H = 1350;

const C = {
  bgTop: "#050814",
  bgMid: "#081223",
  bgBot: "#04070e",
  panel: "#0b1428",
  panelDeep: "#070d1d",
  line: "rgba(140, 197, 255, 0.35)",
  ink: "#04070e",
  text: "#edf7ff",
  muted: "#9fb4cb",
  cyan: "#66e8ff",
  cyanStrong: "#b8fbff",
  amber: "#ffc85e",
  green: "#8ff3a5",
  magenta: "#ff6f91",
};

const MONO = '"IBM Plex Mono", "SFMono-Regular", Consolas, "Liberation Mono", monospace';
const SANS = '"PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans SC", system-ui, sans-serif';

function loadImage(src) {
  return new Promise((resolve) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = () => resolve(null);
    img.src = src;
  });
}

function pixelPanel(ctx, x, y, w, h) {
  ctx.fillStyle = "rgba(0,0,0,0.45)";
  ctx.fillRect(x + 10, y + 10, w, h);
  ctx.fillStyle = C.ink;
  ctx.fillRect(x - 4, y - 4, w + 8, h + 8);
  ctx.fillStyle = C.panel;
  ctx.fillRect(x, y, w, h);
  ctx.strokeStyle = C.line;
  ctx.lineWidth = 4;
  ctx.strokeRect(x + 2, y + 2, w - 4, h - 4);
}

function shadowText(ctx, text, x, y, { font, color, shadow = C.ink, offset = 4, align = "left" }) {
  ctx.font = font;
  ctx.textAlign = align;
  ctx.textBaseline = "alphabetic";
  ctx.fillStyle = shadow;
  ctx.fillText(text, x + offset, y + offset);
  ctx.fillStyle = color;
  ctx.fillText(text, x, y);
}

function todayLabel() {
  const d = new Date();
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
}

// progress: { count, total, streak, phasesDone, phasesTotal, medals: [{icon,name,unlocked}],
//             cells: boolean[] (按片单顺序，true = 已刷), nextHint }
export async function renderProgressCard(progress) {
  const canvas = document.createElement("canvas");
  canvas.width = W;
  canvas.height = H;
  const ctx = canvas.getContext("2d");

  // 背景：深空渐变 + CRT 扫描线
  const bg = ctx.createLinearGradient(0, 0, 0, H);
  bg.addColorStop(0, C.bgTop);
  bg.addColorStop(0.52, C.bgMid);
  bg.addColorStop(1, C.bgBot);
  ctx.fillStyle = bg;
  ctx.fillRect(0, 0, W, H);
  const glow = ctx.createRadialGradient(260, 160, 0, 260, 160, 520);
  glow.addColorStop(0, "rgba(102, 232, 255, 0.16)");
  glow.addColorStop(1, "rgba(102, 232, 255, 0)");
  ctx.fillStyle = glow;
  ctx.fillRect(0, 0, W, H);
  ctx.fillStyle = "rgba(255,255,255,0.035)";
  for (let y = 0; y < H; y += 6) ctx.fillRect(0, y, W, 2);

  // 顶部：标题
  shadowText(ctx, "AURORA  VIDEO  LIBRARY", 72, 112, {
    font: `700 30px ${MONO}`,
    color: C.cyan,
    offset: 4,
  });
  shadowText(ctx, "我的刷课进度", 72, 196, {
    font: `700 68px ${SANS}`,
    color: C.text,
    offset: 6,
  });
  shadowText(ctx, `从正弦波刷到 Whisper · ${progress.total} 条名师课对齐 L01–L99`, 72, 244, {
    font: `26px ${SANS}`,
    color: C.muted,
    offset: 3,
  });

  // 主数字面板
  pixelPanel(ctx, 72, 290, 936, 250);
  const pct = progress.total ? Math.round((progress.count / progress.total) * 100) : 0;
  shadowText(ctx, String(progress.count), 104, 430, {
    font: `700 150px ${MONO}`,
    color: C.cyanStrong,
    offset: 8,
  });
  ctx.font = `700 150px ${MONO}`;
  const numW = ctx.measureText(String(progress.count)).width;
  shadowText(ctx, `/ ${progress.total} 已刷`, 104 + numW + 24, 430, {
    font: `700 44px ${SANS}`,
    color: C.muted,
    offset: 4,
  });
  // 进度条
  const barX = 104;
  const barY = 462;
  const barW = 872;
  const barH = 34;
  ctx.fillStyle = C.panelDeep;
  ctx.fillRect(barX, barY, barW, barH);
  ctx.strokeStyle = C.line;
  ctx.lineWidth = 4;
  ctx.strokeRect(barX, barY, barW, barH);
  const fill = ctx.createLinearGradient(barX, 0, barX + barW, 0);
  fill.addColorStop(0, C.cyan);
  fill.addColorStop(1, C.amber);
  ctx.fillStyle = fill;
  const fillW = Math.round(((barW - 12) * pct) / 100);
  ctx.fillRect(barX + 6, barY + 6, fillW, barH - 12);
  ctx.fillStyle = "rgba(4,7,14,0.55)";
  for (let x = barX + 6; x < barX + 6 + fillW; x += 16) ctx.fillRect(x + 10, barY + 6, 4, barH - 12);
  shadowText(ctx, `${pct}%`, barX + barW, 528, {
    font: `700 26px ${MONO}`,
    color: C.amber,
    offset: 3,
    align: "right",
  });

  // 三格状态：连续天数 / 阶段通关 / 奖章
  const statY = 576;
  const statW = 296;
  const gap = 24;
  const stats = [
    { label: "连续打卡", value: `${progress.streak} 天` },
    { label: "阶段通关", value: `${progress.phasesDone}/${progress.phasesTotal}` },
    {
      label: "奖章",
      value: progress.medals.filter((m) => m.unlocked).map((m) => m.icon).join(" ") || "—",
    },
  ];
  stats.forEach((s, i) => {
    const x = 72 + i * (statW + gap);
    pixelPanel(ctx, x, statY, statW, 150);
    shadowText(ctx, s.label, x + 24, statY + 50, { font: `22px ${MONO}`, color: C.muted, offset: 3 });
    shadowText(ctx, s.value, x + 24, statY + 116, {
      font: `700 48px ${s.label === "奖章" ? SANS : MONO}`,
      color: s.label === "阶段通关" ? C.green : C.amber,
      offset: 4,
    });
  });

  // 92 格通关地图
  pixelPanel(ctx, 72, 764, 936, 300);
  shadowText(ctx, "通关地图 · 每格一条视频", 104, 812, { font: `22px ${MONO}`, color: C.muted, offset: 3 });
  const cells = progress.cells;
  const cols = 23;
  const cellSize = 30;
  const cellGap = 8;
  const gridX = 104;
  const gridY = 840;
  cells.forEach((done, i) => {
    const cx = gridX + (i % cols) * (cellSize + cellGap);
    const cy = gridY + Math.floor(i / cols) * (cellSize + cellGap);
    ctx.fillStyle = C.ink;
    ctx.fillRect(cx + 3, cy + 3, cellSize, cellSize);
    ctx.fillStyle = done ? C.green : C.panelDeep;
    ctx.fillRect(cx, cy, cellSize, cellSize);
    ctx.strokeStyle = done ? C.green : C.line;
    ctx.lineWidth = 2;
    ctx.strokeRect(cx + 1, cy + 1, cellSize - 2, cellSize - 2);
  });
  shadowText(ctx, progress.nextHint, 104, 1036, { font: `22px ${SANS}`, color: C.muted, offset: 3 });

  // 底部：仓库名 + 二维码
  pixelPanel(ctx, 72, 1090, 936, 196);
  shadowText(ctx, "99 课音频 AI 课程 · 免费 · MIT 开源", 104, 1142, {
    font: `700 30px ${SANS}`,
    color: C.text,
    offset: 3,
  });
  shadowText(ctx, "GitHub 搜 djzoom/AURORA", 104, 1194, {
    font: `700 34px ${MONO}`,
    color: C.amber,
    offset: 4,
  });
  shadowText(ctx, GROWTH.pages.videos.url.replace(/^https?:\/\//, ""), 104, 1238, {
    font: `22px ${MONO}`,
    color: C.cyan,
    offset: 3,
  });
  shadowText(ctx, todayLabel(), 104, 1272, { font: `20px ${MONO}`, color: C.muted, offset: 2 });

  const qr = await loadImage(GROWTH.pages.videos.qr);
  const qrSize = 156;
  const qrX = 72 + 936 - qrSize - 20;
  const qrY = 1090 + 20;
  ctx.fillStyle = "#fff";
  ctx.fillRect(qrX - 8, qrY - 8, qrSize + 16, qrSize + 16);
  if (qr) {
    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(qr, qrX, qrY, qrSize, qrSize);
  } else {
    ctx.fillStyle = C.ink;
    ctx.font = `18px ${MONO}`;
    ctx.textAlign = "center";
    ctx.fillText("QR", qrX + qrSize / 2, qrY + qrSize / 2 + 6);
  }

  return canvas;
}

export async function downloadProgressCard(progress, filename = "aurora-progress.png") {
  const canvas = await renderProgressCard(progress);
  const dataUrl = canvas.toDataURL("image/png");
  const a = document.createElement("a");
  a.href = dataUrl;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  a.remove();
  return dataUrl;
}
