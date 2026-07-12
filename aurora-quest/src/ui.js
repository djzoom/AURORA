// 渲染层 —— 把 state 画到 DOM。只读 state；交互回调由 app.js 通过 handlers 注入，
// 本层不直接修改游戏状态、不碰 localStorage。
//
// handlers 契约：{ onChoice(index), onSelectPhase(phaseIndex) }

import { QUESTS, XP_PER_LEVEL } from "./data/quests.js";
import { COURSE_INTRO, COURSE_PHASES } from "./data/worldmap.js";
import { drawSprite, SPRITE_BY_QUEST } from "./sprites.js";
import {
  levelFromXp,
  completedCount,
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

// ---- 课程介绍（L01–L99 折叠目录）-------------------------------------------

function phaseIsInCurrentQuestRange(index, state) {
  const coursePerQuest = Math.ceil(COURSE_PHASES.length / QUESTS.length);
  return Math.floor(index / coursePerQuest) === state.activePhaseIndex;
}

function renderCourseLessons(phase) {
  const table = document.createElement("table");
  table.className = "course-lessons";

  const thead = document.createElement("thead");
  const headRow = document.createElement("tr");
  ["课号", "课程标题"].forEach((text) => {
    const th = document.createElement("th");
    th.scope = "col";
    th.textContent = text;
    headRow.appendChild(th);
  });
  thead.appendChild(headRow);

  const tbody = document.createElement("tbody");
  phase.lessons.forEach(([code, title]) => {
    const row = document.createElement("tr");
    const codeCell = document.createElement("td");
    codeCell.className = "lesson-code";
    codeCell.textContent = code;
    const titleCell = document.createElement("td");
    titleCell.textContent = title;
    row.append(codeCell, titleCell);
    tbody.appendChild(row);
  });

  table.append(thead, tbody);
  return table;
}

function renderCourseKeyIdeas(phase) {
  const ideas = phase.keyIdeas ?? [];
  if (!ideas.length) return null;

  const block = document.createElement("section");
  block.className = "course-keyideas";
  block.setAttribute("aria-label", "关键知识");

  const title = document.createElement("h4");
  title.textContent = "关键知识";

  const list = document.createElement("ul");
  ideas.forEach((idea) => {
    const item = document.createElement("li");
    item.textContent = idea;
    list.appendChild(item);
  });

  block.append(title, list);
  return block;
}

function renderCoursePhase(phase, index, state) {
  const detail = document.createElement("details");
  detail.className = "course-phase";
  detail.open = index === 0 || phaseIsInCurrentQuestRange(index, state);

  const summary = document.createElement("summary");
  summary.className = "course-phase-summary";

  const badge = document.createElement("span");
  badge.className = "course-phase-icon";
  badge.setAttribute("aria-hidden", "true");
  badge.textContent = phase.icon;

  const title = document.createElement("span");
  title.className = "course-phase-title";
  title.textContent = `${phase.phase} · ${phase.title}`;

  const meta = document.createElement("span");
  meta.className = "course-phase-meta";
  meta.textContent = `${phase.folder} ${phase.range}`;

  summary.append(badge, title, meta);

  const body = document.createElement("div");
  body.className = "course-phase-body";

  const lead = document.createElement("p");
  lead.className = "course-copy";
  lead.textContent = phase.lead;

  const summaryCopy = document.createElement("p");
  summaryCopy.className = "course-copy course-summary";
  summaryCopy.textContent = phase.summary;

  const keyIdeas = renderCourseKeyIdeas(phase);
  body.append(lead);
  if (keyIdeas) body.appendChild(keyIdeas);
  body.append(renderCourseLessons(phase), summaryCopy);
  detail.append(summary, body);
  return detail;
}

function renderLevelMap(state) {
  els.roadmapList.innerHTML = "";

  const intro = document.createElement("article");
  intro.className = "course-intro";

  const eyebrow = document.createElement("p");
  eyebrow.className = "course-eyebrow";
  eyebrow.textContent = COURSE_INTRO.range;

  const heading = document.createElement("h3");
  heading.textContent = COURSE_INTRO.title;

  const lead = document.createElement("p");
  lead.className = "course-copy";
  lead.textContent = COURSE_INTRO.lead;

  const thesis = document.createElement("p");
  thesis.className = "course-thesis";
  thesis.textContent = COURSE_INTRO.thesis;

  intro.append(eyebrow, heading, lead, thesis);
  els.roadmapList.appendChild(intro);

  COURSE_PHASES.forEach((phase, index) => {
    els.roadmapList.appendChild(renderCoursePhase(phase, index, state));
  });

  els.mapCaption.textContent = "L01 → L99 · 点击每个 Phase 展开课程表和简介。";
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
