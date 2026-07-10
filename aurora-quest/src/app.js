// 入口与游戏机制 —— 持有唯一的 state，定义所有动作（答题 / 推进 / 静音 / 键盘），
// 渲染委托给 ui.js，存档与查询在 state.js，题库在 data/quests.js，音效在 audio.js。
//
// 单向数据流：动作改 state → render() 重画 → persist() 落盘。
// 反馈窗口（答题后 460/820ms）内 inputLocked=true，所有改状态的动作都被挡住，
// 保证延迟结算 commitAnswer 时世界没有被切章/重置/读档改变。

import { QUESTS, XP_PER_QUESTION, XP_PER_PHASE_CLEAR } from "./data/quests.js";
import { playSfx } from "./audio.js";
import {
  defaultSave,
  loadState,
  saveState,
  hasSave,
  clearSave,
  currentQuest,
  currentQuestion,
  phaseIsComplete,
  unlockedIndex,
  addLog,
  ensureInventory,
} from "./state.js";
import {
  els,
  renderApp,
  updateResumeButton,
  updateMuteButton,
  markChoiceFeedback,
  flashBoss,
  spawnFx,
} from "./ui.js";

let state = loadState() ?? defaultSave();
let inputLocked = false;

const handlers = {
  onChoice: handleChoice,
  onSelectPhase: setActivePhase,
};

function render() {
  renderApp(state, handlers);
}

function persist() {
  saveState(state);
  updateResumeButton(hasSave());
}

// ---- 章节切换 -------------------------------------------------------------

function setActivePhase(index) {
  if (inputLocked) return; // 反馈窗口内禁止切章（防止延迟结算记到别的章节）
  const unlock = unlockedIndex(state);
  if (index > unlock && index !== state.activePhaseIndex) {
    addLog(state, "系统", "这一区域还没有解锁，先打通前面的章节。");
    render();
    persist();
    return;
  }

  state.activePhaseIndex = Math.max(0, Math.min(index, QUESTS.length - 1));
  addLog(state, "系统", `进入 ${currentQuest(state).title}。`);
  render();
  persist();
}

function startAdventure() {
  setActivePhase(0);
}

function resetAdventure() {
  if (inputLocked) return; // 反馈窗口内禁止重置（防止延迟结算污染新存档）
  const muted = state.muted; // 音效偏好与进度生命周期不同，重置进度不重置静音
  clearSave();
  state = defaultSave();
  state.muted = muted;
  addLog(state, "系统", "存档已清空，新的冒险重新开始。");
  render();
  // 刻意不 persist：清空就是清空（「继续存档」随之禁用），
  // 新存档等玩家真正行动（进章/答题）时再落盘。
  updateResumeButton(hasSave());
}

function advancePhase() {
  if (inputLocked) return;
  const nextIndex = Math.min(state.activePhaseIndex + 1, QUESTS.length - 1);
  if (!phaseIsComplete(state, state.activePhaseIndex)) {
    addLog(state, "系统", "这一章还没通关，先把当前问题打完。");
    render();
    persist();
    return;
  }

  if (state.activePhaseIndex === QUESTS.length - 1) {
    state.activePhaseIndex = 0;
    addLog(state, "系统", "终章已过，重新从序章开始复盘。");
  } else {
    state.activePhaseIndex = nextIndex;
    addLog(state, "系统", `进入 ${currentQuest(state).title}。`);
  }

  render();
  persist();
}

// ---- 答题 ------------------------------------------------------------------

// 点击/键盘入口：先播放反馈（高亮 + 音效 + 打击特效），锁定短暂时间，再提交结算。
function handleChoice(choiceIndex) {
  if (inputLocked) return;
  const question = currentQuestion(state);
  if (!question) return;

  const correct = choiceIndex === question.answer;
  if (!markChoiceFeedback(choiceIndex, question.answer)) return;

  inputLocked = true;
  playSfx(correct ? "hit" : "miss", state.muted);
  flashBoss(correct ? "hit" : "block");
  spawnFx(
    correct ? `-${Math.round(100 / currentQuest(state).questions.length)}` : "MISS",
    correct ? "dmg" : "miss",
  );

  window.setTimeout(
    () => {
      inputLocked = false;
      // 双保险：若反馈期间世界仍被改变（未来代码路径），当前题对不上就放弃结算。
      if (currentQuestion(state) !== question) return;
      commitAnswer(choiceIndex, question);
    },
    correct ? 460 : 820,
  );
}

// 结算：更新存档状态并渲染。答错保留原题以便重试，答对则推进进度。
function commitAnswer(choiceIndex, question) {
  const quest = currentQuest(state);
  const progress = state.phaseProgress[state.activePhaseIndex] ?? 0;

  if (choiceIndex !== question.answer) {
    state.streak = 0;
    addLog(state, "失手", `${question.hint} 再试一次，你已经很接近了。`);
    render();
    persist();
    return;
  }

  state.phaseProgress[state.activePhaseIndex] = progress + 1;
  state.xp += XP_PER_QUESTION;
  state.streak += 1;
  addLog(state, "命中", `${question.note} +${XP_PER_QUESTION} XP。`);

  if (phaseIsComplete(state, state.activePhaseIndex)) {
    state.xp += XP_PER_PHASE_CLEAR;
    state.streak = 0;
    ensureInventory(state, quest.artifact);
    addLog(state, "通关", `你拿到了「${quest.artifact.name}」；下一章已经解锁。 +${XP_PER_PHASE_CLEAR} XP。`);
    if (state.activePhaseIndex === QUESTS.length - 1) {
      addLog(state, "终章", "整条链路已经合体。现在你可以带着这套作品去讲、去演示、去继续迭代。");
      playSfx("finale", state.muted);
    } else {
      playSfx("clear", state.muted);
    }
  } else {
    addLog(state, "进展", `继续拆解 ${quest.boss} 的下一个招式。`);
  }

  render();
  persist();
}

// ---- 静音与键盘 -------------------------------------------------------------

function toggleMute() {
  state.muted = !state.muted;
  updateMuteButton(state.muted);
  if (hasSave()) persist(); // 无存档时只改内存，避免开场按 M 就凭空造出存档
  if (!state.muted) playSfx("hit", state.muted);
}

function handleKeydown(event) {
  if (event.metaKey || event.ctrlKey || event.altKey) return;
  const tag = document.activeElement?.tagName;
  if (tag === "INPUT" || tag === "TEXTAREA") return;

  const key = event.key;
  if (key === "m" || key === "M") {
    toggleMute();
    event.preventDefault();
    return;
  }
  if (key === "Enter" || key === "n" || key === "N") {
    // Enter 在按钮/链接聚焦时应触发该控件的默认行为，不能被“下一章”劫持。
    if (key === "Enter" && (tag === "BUTTON" || tag === "A")) return;
    if (!els.nextButton?.disabled) {
      advancePhase();
      event.preventDefault();
    }
    return;
  }
  if (/^[1-9]$/.test(key)) {
    if (phaseIsComplete(state, state.activePhaseIndex)) return;
    handleChoice(Number(key) - 1);
    event.preventDefault();
  }
}

// ---- 启动 --------------------------------------------------------------------

function wireEvents() {
  els.startButton?.addEventListener("click", startAdventure);
  els.resumeButton?.addEventListener("click", () => {
    if (inputLocked) return; // 反馈窗口内禁止读档
    const saved = loadState();
    if (saved) {
      state = saved;
      addLog(state, "系统", "继续上次的存档。");
      render();
      persist();
      return;
    }
    addLog(state, "系统", "当前没有存档，先从序章开始。");
    render();
  });
  els.resetButton?.addEventListener("click", resetAdventure);
  els.muteButton?.addEventListener("click", toggleMute);
  els.nextButton?.addEventListener("click", advancePhase);
  window.addEventListener("keydown", handleKeydown);
}

function bootstrap() {
  wireEvents();
  render();
  updateResumeButton(hasSave());
}

bootstrap();
