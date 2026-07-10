// 存档与状态查询 —— localStorage 读写、默认存档、所有派生查询（selector）。
// 约定：mutator（addLog / ensureInventory）只改传入的 state，不碰 DOM、不自动持久化；
// 什么时候保存、什么时候渲染由 app.js 决定。

import { QUESTS, XP_PER_LEVEL } from "./data/quests.js";

export const STORAGE_KEY = "aurora-quest.save.v1";

export const defaultSave = () => ({
  activePhaseIndex: 0,
  phaseProgress: QUESTS.map(() => 0),
  xp: 0,
  streak: 0,
  muted: false,
  inventory: [
    {
      icon: "PK",
      name: "课程通行证",
      desc: "你已经进入 AURORA 的起点。",
    },
  ],
  log: [
    {
      kind: "系统",
      text: "存档已就绪。点击“开始冒险”就能进入序章。",
    },
  ],
});

// 把外部输入（localStorage 可能被手改/损坏）钳制成安全整数。
function clampInt(value, min, max, fallback = 0) {
  const n = Number(value);
  if (!Number.isFinite(n)) return fallback;
  return Math.max(min, Math.min(Math.floor(n), max));
}

function normalizeProgress(progress) {
  if (!Array.isArray(progress)) return QUESTS.map(() => 0);
  return QUESTS.map((quest, index) =>
    clampInt(progress[index], 0, quest.questions.length),
  );
}

// 数组元素也要消毒：inventory/log 里混入 null/数字会让渲染层读属性时砖机。
function sanitizeInventory(list, fallback) {
  if (!Array.isArray(list)) return fallback;
  const clean = list.filter(
    (item) =>
      item &&
      typeof item === "object" &&
      typeof item.name === "string" &&
      typeof item.desc === "string",
  );
  return clean.length ? clean : fallback;
}

function sanitizeLog(list, fallback) {
  if (!Array.isArray(list)) return fallback;
  const clean = list
    .filter(
      (entry) =>
        entry &&
        typeof entry === "object" &&
        typeof entry.kind === "string" &&
        typeof entry.text === "string",
    )
    .slice(0, 8);
  return clean.length ? clean : fallback;
}

export function loadState() {
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    if (!raw) return null;
    const parsed = JSON.parse(raw);
    if (!parsed || typeof parsed !== "object") return null;
    return {
      ...defaultSave(),
      ...parsed,
      // 逐字段消毒：越界的 activePhaseIndex 会让 phaseIsComplete 索引越界砖机，
      // 字符串 xp 会让 += 变成字符串拼接。
      activePhaseIndex: clampInt(parsed.activePhaseIndex, 0, QUESTS.length - 1),
      xp: clampInt(parsed.xp, 0, Number.MAX_SAFE_INTEGER),
      streak: clampInt(parsed.streak, 0, Number.MAX_SAFE_INTEGER),
      muted: Boolean(parsed.muted),
      phaseProgress: normalizeProgress(parsed.phaseProgress),
      inventory: sanitizeInventory(parsed.inventory, defaultSave().inventory),
      log: sanitizeLog(parsed.log, defaultSave().log),
    };
  } catch {
    return null;
  }
}

export function saveState(state) {
  window.localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
}

export function hasSave() {
  return Boolean(window.localStorage.getItem(STORAGE_KEY));
}

export function clearSave() {
  window.localStorage.removeItem(STORAGE_KEY);
}

// ---- 派生查询（不修改 state）--------------------------------------------

export function levelFromXp(xp) {
  return 1 + Math.floor(xp / XP_PER_LEVEL);
}

export function completedCount(state) {
  return QUESTS.reduce(
    (count, quest, index) =>
      count + (state.phaseProgress[index] >= quest.questions.length ? 1 : 0),
    0,
  );
}

export function unlockedIndex(state) {
  for (let i = 0; i < QUESTS.length; i += 1) {
    if (state.phaseProgress[i] < QUESTS[i].questions.length) {
      return i;
    }
  }
  return QUESTS.length - 1;
}

export function currentQuest(state) {
  return QUESTS[state.activePhaseIndex] ?? QUESTS[0];
}

export function currentQuestion(state) {
  const quest = currentQuest(state);
  const progress = state.phaseProgress[state.activePhaseIndex] ?? 0;
  return quest.questions[progress] ?? null;
}

export function phaseIsComplete(state, index) {
  return state.phaseProgress[index] >= QUESTS[index].questions.length;
}

// ---- mutator（只改 state，不持久化）--------------------------------------

export function addLog(state, kind, text) {
  state.log.unshift({ kind, text });
  state.log = state.log.slice(0, 8);
}

export function ensureInventory(state, item) {
  if (!item) return;
  if (state.inventory.some((entry) => entry.name === item.name)) return;
  state.inventory.unshift(item);
}
