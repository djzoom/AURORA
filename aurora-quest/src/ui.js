// 渲染层 —— 把 state 画到 DOM。只读 state；交互回调由 app.js 通过 handlers 注入，
// 本层不直接修改游戏状态、不碰 localStorage。
//
// handlers 契约：{ onChoice(index), onSelectPhase(phaseIndex) }

import courseSnapshot from "./course-snapshot.generated.js";
import { QUESTS, XP_PER_LEVEL } from "./data/quests.js";
import { MAP_CANVAS, MAP_EDGES, MAP_NODES } from "./data/worldmap.js";
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
const SVG_NS = "http://www.w3.org/2000/svg";
const MAP_NODE_BY_ID = new Map(MAP_NODES.map((node) => [node.id, node]));
const MAP_STEP_COUNT_BY_QUEST = QUESTS.map((_, questIndex) =>
  Math.max(
    1,
    ...MAP_NODES
      .filter((node) => node.questIndex === questIndex)
      .map((node) => node.step + 1),
  ),
);

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
// 初始比例 = 大陆视图（far LOD）：先看 Phase 拓扑全貌，放大才进入街道级细节。
let mapZoom = window.matchMedia("(max-width: 760px)").matches ? 0.6 : 0.7;
const MAP_ZOOM_MIN = 0.6;
const MAP_ZOOM_MAX = 2.2;
const MAP_ZOOM_STEP = 0.2;

function applyMapZoom() {
  els.roadmapList?.style.setProperty("--map-zoom", String(mapZoom));
  // LOD（制图学细节分级）：比例就是层级切换——
  // far = 大陆视图（只看 Phase 拓扑：城门 + 地形轮廓 + 依赖走向）
  // mid = 地区视图（区名 / 课号域 / ◀承接 路标可读）
  // near = 街道视图（每块 Lesson 石砖的 L## 与风物志清晰）
  const lod = mapZoom < 0.75 ? "far" : mapZoom < 1.3 ? "mid" : "near";
  els.roadmapList?.setAttribute("data-lod", lod);
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

function createSvgElement(tagName) {
  return document.createElementNS(SVG_NS, tagName);
}

function questProgressStep(state, questIndex) {
  const quest = QUESTS[questIndex];
  const progress = state.phaseProgress[questIndex] ?? 0;
  const total = Math.max(1, quest?.questions.length ?? 1);
  const stepCount = MAP_STEP_COUNT_BY_QUEST[questIndex] ?? 1;
  if (progress >= total) return stepCount;
  return Math.min(stepCount - 1, Math.floor((progress / total) * stepCount));
}

function mapNodeStatus(state, mapNode, unlock) {
  if (mapNode.questIndex > unlock) return "locked";
  if (phaseIsComplete(state, mapNode.questIndex)) return "completed";

  const progressStep = questProgressStep(state, mapNode.questIndex);
  if (progressStep > mapNode.step) return "completed";
  if (state.activePhaseIndex === mapNode.questIndex && progressStep === mapNode.step) {
    return "active";
  }
  return "available";
}

function mapEdgeStatus(fromStatus, toStatus) {
  if (toStatus === "locked") return "locked";
  if (fromStatus === "completed" && toStatus === "completed") return "completed";
  if (fromStatus === "active" || toStatus === "active") return "active";
  return "available";
}

function mapEdgePath(edge) {
  const from = MAP_NODE_BY_ID.get(edge.from);
  const to = MAP_NODE_BY_ID.get(edge.to);
  if (!from || !to) return "";

  const dy = to.y - from.y;
  if (edge.style === "main") {
    const midY = from.y + dy / 2;
    return `M ${from.x} ${from.y} C ${from.x} ${midY} ${to.x} ${midY} ${to.x} ${to.y}`;
  }

  const bend = edge.style === "merge" ? 0.38 : 0.28;
  return `M ${from.x} ${from.y} C ${from.x} ${from.y + dy * bend} ${to.x} ${
    to.y - dy * bend
  } ${to.x} ${to.y}`;
}

function renderMapRoutes(svg, nodeStatuses) {
  MAP_EDGES.forEach((edge) => {
    const path = mapEdgePath(edge);
    const status = mapEdgeStatus(nodeStatuses.get(edge.from), nodeStatuses.get(edge.to));
    const classes = `${edge.style} ${status}`;

    const glow = createSvgElement("path");
    glow.setAttribute("class", `quest-route-glow ${classes}`);
    glow.setAttribute("d", path);
    svg.appendChild(glow);

    const route = createSvgElement("path");
    route.setAttribute("class", `quest-route ${classes}`);
    route.setAttribute("d", path);
    svg.appendChild(route);
  });
}

function renderMapNodes(layer, state, onSelectPhase, nodeStatuses) {
  MAP_NODES.forEach((mapNode) => {
    const status = nodeStatuses.get(mapNode.id);
    const quest = QUESTS[mapNode.questIndex];
    const button = document.createElement("button");
    button.type = "button";
    button.className = `quest-map-node kind-${mapNode.kind} chapter-${mapNode.questIndex} ${status}`;
    button.style.left = `${(mapNode.x / MAP_CANVAS.width) * 100}%`;
    button.style.top = `${(mapNode.y / MAP_CANVAS.height) * 100}%`;
    button.title =
      status === "locked"
        ? "锁定中"
        : `${mapNode.label}｜${mapNode.subtitle}${mapNode.summary ? `｜${mapNode.summary}` : ""}`;
    button.setAttribute(
      "aria-label",
      `${mapNode.label}，${mapNode.subtitle}，${quest.title}`,
    );
    button.disabled = status === "locked" || status === "active";
    button.addEventListener("click", () => onSelectPhase(mapNode.questIndex));

    const sprite = document.createElement("span");
    sprite.className = "quest-map-sprite";
    sprite.setAttribute("aria-hidden", "true");
    sprite.textContent = mapNode.sigil;

    const label = document.createElement("span");
    label.className = "quest-map-label";
    label.textContent = `${mapNode.icon} ${mapNode.label}`;

    const subtitle = document.createElement("span");
    subtitle.className = "quest-map-subtitle";
    subtitle.textContent = mapNode.subtitle;

    const copy = document.createElement("span");
    copy.className = "quest-map-copy";
    copy.append(label, subtitle);

    button.append(sprite, copy);
    layer.appendChild(button);
  });
}

function activeMapLabel(state) {
  const progressStep = questProgressStep(state, state.activePhaseIndex);
  const step = Math.min(
    progressStep,
    (MAP_STEP_COUNT_BY_QUEST[state.activePhaseIndex] ?? 1) - 1,
  );
  const activeNodes = MAP_NODES.filter(
    (node) => node.questIndex === state.activePhaseIndex && node.step === step,
  );
  if (!activeNodes.length) return currentQuest(state).title;
  return activeNodes
    .map((node) => `${node.label}${node.subtitle ? ` ${node.subtitle}` : ""}`)
    .join(" / ");
}

function renderLevelMap(state, onSelectPhase) {
  const unlock = unlockedIndex(state);
  const nodeStatuses = new Map(
    MAP_NODES.map((mapNode) => [mapNode.id, mapNodeStatus(state, mapNode, unlock)]),
  );

  els.roadmapList.innerHTML = "";

  const svg = createSvgElement("svg");
  svg.classList.add("quest-map-routes");
  svg.setAttribute("viewBox", `0 0 ${MAP_CANVAS.width} ${MAP_CANVAS.height}`);
  svg.setAttribute("preserveAspectRatio", "none");
  svg.setAttribute("aria-hidden", "true");
  renderMapRoutes(svg, nodeStatuses);

  const nodeLayer = document.createElement("div");
  nodeLayer.className = "quest-map-nodes";
  renderMapNodes(nodeLayer, state, onSelectPhase, nodeStatuses);

  els.roadmapList.append(svg, nodeLayer);
  applyMapZoom();

  // 地图说明：当前地图节点 + 对应课程里程碑（来自 LEARNING_PLAN 生成的快照）。
  const idx = state.activePhaseIndex;
  const milestone =
    idx === 0
      ? `开场五课 ${courseSnapshot.openingLessons.map((l) => l.code).join(" · ")}`
      : courseSnapshot.monthlyPhases[idx - 1]?.deliverable ?? "";
  const place = activeMapLabel(state);
  els.mapCaption.textContent = milestone ? `${place} ｜ ${milestone}` : place;
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
