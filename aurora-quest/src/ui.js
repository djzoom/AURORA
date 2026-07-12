// 渲染层 —— 把 state 画到 DOM。只读 state；交互回调由 app.js 通过 handlers 注入，
// 本层不直接修改游戏状态、不碰 localStorage。
//
// handlers 契约：{ onChoice(index), onSelectPhase(phaseIndex) }

import courseSnapshot from "./course-snapshot.generated.js";
import { QUESTS, XP_PER_LEVEL } from "./data/quests.js";
import { MAP_ZONES } from "./data/worldmap.js";
import { drawSprite, SPRITE_BY_QUEST } from "./sprites.js";
import {
  levelFromXp,
  completedCount,
  unlockedIndex,
  currentQuest,
  currentQuestion,
  phaseIsComplete,
} from "./state.js";

export const els = {
  startButton: document.getElementById("start-button"),
  resumeButton: document.getElementById("resume-button"),
  resetButton: document.getElementById("reset-button"),
  muteButton: document.getElementById("mute-button"),
  level: document.getElementById("player-level"),
  xp: document.getElementById("player-xp"),
  clear: document.getElementById("player-clear"),
  streak: document.getElementById("player-streak"),
  xpFill: document.getElementById("xp-fill"),
  stageTitle: document.getElementById("stage-title"),
  bossZone: document.getElementById("boss-zone"),
  bossCanvas: document.getElementById("boss-canvas"),
  bossName: document.getElementById("boss-name"),
  bossHp: document.getElementById("boss-hp"),
  fxLayer: document.getElementById("fx-layer"),
  stageNarrative: document.getElementById("stage-narrative"),
  phaseSource: document.getElementById("phase-source"),
  questionCount: document.getElementById("question-count"),
  questionHintPill: document.getElementById("question-hint-pill"),
  questionPrompt: document.getElementById("question-prompt"),
  choiceList: document.getElementById("choice-list"),
  battleLogList: document.getElementById("battle-log-list"),
  nextButton: document.getElementById("next-button"),
  inventoryList: document.getElementById("inventory-list"),
  roadmapList: document.getElementById("roadmap-list"),
  mapCaption: document.getElementById("map-caption"),
};

const HP_CELLS = 10;

// ---- 战斗区 -----------------------------------------------------------------

function renderBoss(state) {
  const quest = currentQuest(state);
  const progress = state.phaseProgress[state.activePhaseIndex] ?? 0;
  const total = quest.questions.length;
  const complete = phaseIsComplete(state, state.activePhaseIndex);
  const hpRatio = complete ? 0 : 1 - progress / total;

  drawSprite(els.bossCanvas, SPRITE_BY_QUEST[quest.id]);
  els.bossZone.classList.toggle("defeated", complete);
  els.bossName.textContent = complete ? `${quest.boss} · 已击败` : quest.boss;

  els.bossHp.innerHTML = "";
  els.bossHp.classList.toggle("low", hpRatio > 0 && hpRatio <= 0.34);
  const filled = Math.round(hpRatio * HP_CELLS);
  els.bossHp.setAttribute("aria-label", `BOSS 血量 ${filled}/${HP_CELLS}`);
  for (let i = 0; i < HP_CELLS; i += 1) {
    const cell = document.createElement("span");
    cell.className = i < filled ? "hp-cell filled" : "hp-cell";
    els.bossHp.appendChild(cell);
  }
}

// 打击特效：boss 被命中闪白抖动 / 格挡闪红。反馈窗口(460/820ms)结束后随重渲染消失。
export function flashBoss(kind) {
  if (!els.bossZone) return;
  els.bossZone.classList.add(kind);
  window.setTimeout(() => els.bossZone.classList.remove(kind), 420);
}

// 伤害飘字：-33 / MISS 从 boss 区域向上飘出淡出。
export function spawnFx(text, kind) {
  if (!els.fxLayer) return;
  const el = document.createElement("span");
  el.className = `fx-float ${kind}`;
  el.textContent = text;
  els.fxLayer.appendChild(el);
  window.setTimeout(() => el.remove?.(), 900);
}

function renderNarrative(quest) {
  els.stageNarrative.innerHTML = "";
  quest.narrative.forEach((paragraph) => {
    const p = document.createElement("p");
    p.textContent = paragraph;
    els.stageNarrative.appendChild(p);
  });
}

function renderChoices(question, onChoice) {
  els.choiceList.classList.remove("locked");
  els.choiceList.innerHTML = "";
  question.choices.forEach((choice, index) => {
    const button = document.createElement("button");
    button.type = "button";
    const key = document.createElement("span");
    key.className = "choice-key";
    key.textContent = String(index + 1);
    button.appendChild(key);
    button.appendChild(document.createTextNode(choice));
    button.addEventListener("click", () => onChoice(index));
    els.choiceList.appendChild(button);
  });
}

// 答题反馈：高亮正确项，答错项标红并锁定列表。
// 返回 false 表示索引越界（调用方应忽略本次输入）。
export function markChoiceFeedback(chosenIndex, answerIndex) {
  const buttons = [...els.choiceList.querySelectorAll("button")];
  if (chosenIndex < 0 || chosenIndex >= buttons.length) return false;
  els.choiceList.classList.add("locked");
  buttons.forEach((btn, i) => {
    if (i === answerIndex) btn.classList.add("correct");
    if (i === chosenIndex && chosenIndex !== answerIndex) btn.classList.add("wrong");
  });
  return true;
}

function renderCompleteState(state, quest) {
  els.questionCount.textContent = "本章已通关";
  els.questionHintPill.textContent = "下一章已解锁";
  els.questionPrompt.textContent = `你击败了 ${quest.boss}！`;
  els.choiceList.innerHTML = `
    <div class="choice-static correct">获得「${quest.artifact.icon} ${quest.artifact.name}」</div>
    <div class="choice-static">按 Enter 或点击「${state.activePhaseIndex === QUESTS.length - 1 ? "重新复盘" : "进入下一章"}」。</div>
  `;
  els.nextButton.disabled = false;
  els.nextButton.textContent =
    state.activePhaseIndex === QUESTS.length - 1 ? "重新复盘" : "进入下一章";
}

// ---- 冒险地图（像素世界地图：Boss 城门 + 11 个课程地形区 + 99 块课程石砖）-------

// 缩放只是视觉状态，不进存档；控件是静态 DOM，模块加载时接线一次。
let mapZoom = 1;
const MAP_ZOOM_MIN = 0.6;
const MAP_ZOOM_MAX = 2.2;
const MAP_ZOOM_STEP = 0.2;

function applyMapZoom() {
  els.roadmapList?.style.setProperty("--map-zoom", String(mapZoom));
  const readout = document.getElementById("map-zoom-val");
  if (readout) readout.textContent = `${Math.round(mapZoom * 100)}%`;
}

function nudgeMapZoom(direction) {
  const next = mapZoom + direction * MAP_ZOOM_STEP;
  mapZoom = Math.min(MAP_ZOOM_MAX, Math.max(MAP_ZOOM_MIN, Number(next.toFixed(2))));
  applyMapZoom();
}

document.getElementById("map-zoom-in")?.addEventListener("click", () => nudgeMapZoom(1));
document.getElementById("map-zoom-out")?.addEventListener("click", () => nudgeMapZoom(-1));

const lessonCode = (n) => `L${String(n).padStart(2, "0")}`;

function renderLevelMap(state, onSelectPhase) {
  const unlock = unlockedIndex(state);
  els.roadmapList.innerHTML = "";
  QUESTS.forEach((quest, index) => {
    const completed = phaseIsComplete(state, index);
    const active = index === state.activePhaseIndex;
    const locked = index > unlock;
    const stateCls = `${completed ? " completed" : ""}${active ? " active" : ""}${locked ? " locked" : ""}`;

    // Boss 城门：保留原节点交互（点击切章、锁定禁用）
    const gate = document.createElement("button");
    gate.type = "button";
    gate.className = `map-gate chapter-${index}${stateCls}`;
    gate.title = locked ? "锁定中" : quest.title;
    gate.setAttribute("aria-label", quest.title);
    gate.disabled = locked || active;
    const gateIcon = document.createElement("span");
    gateIcon.className = "gate-icon";
    gateIcon.textContent = completed ? "🏰" : locked ? "🔒" : "⚔️";
    const gateName = document.createElement("span");
    gateName.className = "gate-name";
    gateName.textContent = index === 0 ? quest.title : `${quest.title}｜${quest.boss}`;
    gate.append(gateIcon, gateName);
    gate.addEventListener("click", () => onSelectPhase(index));
    els.roadmapList.appendChild(gate);

    // 该章覆盖的课程地形区：区名 + 课号范围 + 每课一块石砖（放大可读 L##）
    MAP_ZONES.filter((zone) => zone.questIndex === index).forEach((zone) => {
      const biome = document.createElement("section");
      biome.className = `biome chapter-${index}${stateCls}`;
      const head = document.createElement("h3");
      head.className = "zone-head";
      head.textContent = `${zone.icon} ${zone.name}`;
      const rangeTag = document.createElement("small");
      rangeTag.textContent = `${lessonCode(zone.range[0])}–${lessonCode(zone.range[1])}`;
      head.appendChild(rangeTag);
      const tiles = document.createElement("div");
      tiles.className = "tiles";
      for (let n = zone.range[0]; n <= zone.range[1]; n += 1) {
        const tile = document.createElement("span");
        tile.className = "tile";
        tile.textContent = lessonCode(n);
        tiles.appendChild(tile);
      }
      biome.append(head, tiles);
      els.roadmapList.appendChild(biome);
    });
  });
  applyMapZoom();

  // 地图说明：当前章节 + 对应课程里程碑（来自 LEARNING_PLAN 生成的快照——改课程，地图会变）
  const quest = currentQuest(state);
  const idx = state.activePhaseIndex;
  const milestone =
    idx === 0
      ? `开场五课 ${courseSnapshot.openingLessons.map((l) => l.code).join(" · ")}`
      : courseSnapshot.monthlyPhases[idx - 1]?.deliverable ?? "";
  els.mapCaption.textContent = milestone ? `${quest.title} ｜ ${milestone}` : quest.title;
}

// inventory/log 的字符串来自存档（localStorage 可被手改），
// 一律用 textContent 组装，绝不进 innerHTML —— 防本地篡改型注入。
function renderInventory(state) {
  els.inventoryList.innerHTML = "";
  state.inventory.slice(0, 8).forEach((item) => {
    const card = document.createElement("article");
    card.className = "loot-card";
    const icon = document.createElement("div");
    icon.className = "loot-icon";
    icon.textContent = String(item.icon ?? "▣");
    const body = document.createElement("div");
    body.className = "loot-body";
    const name = document.createElement("h3");
    name.textContent = item.name;
    const desc = document.createElement("p");
    desc.textContent = item.desc;
    body.appendChild(name);
    body.appendChild(desc);
    card.appendChild(icon);
    card.appendChild(body);
    els.inventoryList.appendChild(card);
  });
}

function renderLog(state) {
  els.battleLogList.innerHTML = "";
  state.log.slice(0, 3).forEach((entry) => {
    const row = document.createElement("div");
    row.className = "log-entry";
    const tag = document.createElement("strong");
    tag.textContent = `【${entry.kind}】`;
    row.appendChild(tag);
    row.appendChild(document.createTextNode(` ${entry.text}`));
    els.battleLogList.appendChild(row);
  });
}

function renderStats(state, handlers) {
  const level = levelFromXp(state.xp);
  const xpIntoLevel = state.xp - (level - 1) * XP_PER_LEVEL;
  const xpPercent = Math.max(0, Math.min(100, (xpIntoLevel / XP_PER_LEVEL) * 100));
  const quest = currentQuest(state);
  const progress = state.phaseProgress[state.activePhaseIndex] ?? 0;
  const questionTotal = quest.questions.length;
  const complete = phaseIsComplete(state, state.activePhaseIndex);

  els.level.textContent = String(level);
  els.xp.textContent = String(state.xp);
  els.clear.textContent = `${completedCount(state)}/${QUESTS.length}`;
  els.streak.textContent = String(state.streak);
  els.xpFill.style.width = `${xpPercent}%`;
  els.stageTitle.textContent = quest.title;
  els.phaseSource.textContent = `资料来源：${quest.source.join(" · ")}`;

  if (complete) {
    renderCompleteState(state, quest);
  } else {
    const question = currentQuestion(state);
    els.questionCount.textContent = `问题 ${progress + 1} / ${questionTotal}`;
    els.questionHintPill.textContent = "先想一想，再出手 · 键盘 1–4 作答";
    els.questionPrompt.textContent = question?.prompt ?? "没有可用的问题。";
    els.nextButton.disabled = true; // 未通关不可跳章
    els.nextButton.textContent =
      state.activePhaseIndex === QUESTS.length - 1 ? "重新复盘" : "进入下一章";
    if (question) {
      renderChoices(question, handlers.onChoice);
    } else {
      els.choiceList.innerHTML = "";
    }
  }
}

export function updateResumeButton(saveExists) {
  if (!els.resumeButton) return;
  els.resumeButton.disabled = !saveExists;
}

export function updateMuteButton(muted) {
  if (!els.muteButton) return;
  els.muteButton.textContent = muted ? "音效：关" : "音效：开";
  els.muteButton.setAttribute("aria-pressed", String(!muted));
}

export function renderApp(state, handlers) {
  renderStats(state, handlers);
  renderBoss(state);
  renderNarrative(currentQuest(state));
  renderLog(state);
  renderLevelMap(state, handlers.onSelectPhase);
  renderInventory(state);
  updateMuteButton(state.muted);
}
