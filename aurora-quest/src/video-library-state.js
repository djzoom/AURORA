// 视频资料库打卡存档 —— localStorage 读写、默认存档、派生查询（selector）。
// 与 state.js 同一套约定：mutator（toggleWatched）只改传入的 save，不碰 DOM、
// 不自动持久化；什么时候保存、什么时候渲染由 video-library.html 决定。

export const STORAGE_KEY = "aurora-quest.video-library.v1";

export const defaultSave = () => ({
  // id → 打卡日期（本地 "YYYY-MM-DD"）。日期既是「看过」标记，也是连击的原始数据。
  watched: {},
});

const DATE_RE = /^\d{4}-\d{2}-\d{2}$/;

// 把外部输入（localStorage 可能被手改/损坏）过滤成安全形状：
// 只保留「id 仍存在于当前片单 + 日期格式合法」的记录，条目改名/下架自动清理。
export function loadSave(validIds) {
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    if (!raw) return defaultSave();
    const parsed = JSON.parse(raw);
    if (!parsed || typeof parsed !== "object") return defaultSave();
    const watched = {};
    if (parsed.watched && typeof parsed.watched === "object") {
      for (const [id, date] of Object.entries(parsed.watched)) {
        if (validIds.has(id) && typeof date === "string" && DATE_RE.test(date)) {
          watched[id] = date;
        }
      }
    }
    return { watched };
  } catch {
    return defaultSave();
  }
}

export function persist(save) {
  window.localStorage.setItem(STORAGE_KEY, JSON.stringify(save));
}

export function clearSave() {
  window.localStorage.removeItem(STORAGE_KEY);
}

export function localDateString(date = new Date()) {
  const y = date.getFullYear();
  const m = String(date.getMonth() + 1).padStart(2, "0");
  const d = String(date.getDate()).padStart(2, "0");
  return `${y}-${m}-${d}`;
}

// ---- mutator（只改 save，不持久化）---------------------------------------

export function toggleWatched(save, id) {
  if (save.watched[id]) {
    delete save.watched[id];
  } else {
    save.watched[id] = localDateString();
  }
}

// ---- 派生查询（不修改 save）----------------------------------------------

export function watchedCount(save) {
  return Object.keys(save.watched).length;
}

// 连续打卡天数：从今天往回数（今天还没打卡就从昨天起算），断一天即归零。
export function streakDays(save, today = new Date()) {
  const days = new Set(Object.values(save.watched));
  if (!days.size) return 0;
  const cursor = new Date(today);
  if (!days.has(localDateString(cursor))) cursor.setDate(cursor.getDate() - 1);
  let streak = 0;
  while (days.has(localDateString(cursor))) {
    streak += 1;
    cursor.setDate(cursor.getDate() - 1);
  }
  return streak;
}

// 里程碑奖章：total 由片单数据决定，最后一枚永远是「全通关」。
export function milestones(total) {
  return [
    { at: 10, icon: "🥉", name: "铜牌" },
    { at: 25, icon: "🥈", name: "银牌" },
    { at: 50, icon: "🥇", name: "金牌" },
    { at: 75, icon: "💎", name: "白金" },
    { at: total, icon: "👑", name: "全通关" },
  ].filter((m, i, arr) => m.at <= total && arr.findIndex((x) => x.at === m.at) === i);
}

export function nextMilestone(total, count) {
  return milestones(total).find((m) => count < m.at) ?? null;
}
