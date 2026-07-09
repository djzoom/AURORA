import courseSnapshot from "./course-snapshot.generated.js";

const STORAGE_KEY = "aurora-quest.save.v1";
const XP_PER_QUESTION = 30;
const XP_PER_PHASE_CLEAR = 60;

const q = (prompt, choices, answer, hint, note) => ({
  prompt,
  choices,
  answer,
  hint,
  note,
});

const QUESTS = [
  {
    id: "prologue",
    title: "序章：欢迎来到 AURORA Quest",
    boss: "黑盒守门人",
    artifact: {
      icon: "ID",
      name: "入学徽章",
      desc: "Jupyter + 终端 + 课程地图的通行证。",
    },
    source: ["docs/current/course/LEARNING_PLAN.md", "docs/current/course/GETTING_STARTED.md"],
    narrative: [
      "欢迎大家来到这门课。这里不会把你直接扔进黑盒，而是先让你把每一块砖看明白。",
      "在这场 8-bit 远征里，课程是主线，游戏是陪练。你打通的不是分数，而是“我知道它为什么 work”的底气。",
    ],
    questions: [
      q(
        "这门课最强调的学习方式是什么？",
        ["先堆 API，再看结果", "先手写、再验证、再讲清", "只背概念", "只看演示"],
        1,
        "如果你只会调用工具，遇到陌生问题就会失去方向。",
        "这就是“no API wrappers”的精神。",
      ),
      q(
        "Jupyter 在这门课里更像什么？",
        ["交互式实验室", "静态小说阅读器", "编译器替身", "记笔记用的打印机"],
        0,
        "Notebook 的价值不只是看，更是能边写边试。",
        "Jupyter 最好的地方，就是你可以在同一页里讲、算、画、改。",
      ),
      q(
        "如果一段代码看起来能跑，但你不懂原理，课程希望你怎么做？",
        ["先跳过，等以后自然懂", "回到公式和测试，把链路补清楚", "只记住结论", "把它当成魔法"],
        1,
        "看起来能跑，不代表你以后能复现、能改、能解释。",
        "我们要的是能写、能讲、能调试。",
      ),
    ],
  },
  {
    id: "phase-1",
    title: "第 1 章：数学 + DSP 地基",
    boss: "频谱守门人",
    artifact: {
      icon: "Σ",
      name: "采样钥匙",
      desc: "把空气中的振动变成数组的第一把钥匙。",
    },
    source: ["docs/current/course/LEARNING_PLAN.md", "docs/current/course/week-01-checklist.md", "docs/current/course/week-02-checklist.md"],
    narrative: [
      "傅里叶当年是沿着热传导问题一路走进信号世界的。到了我们这里，这条路变成了声音：先采样，再看频谱，再学会把一段波形拆开、理解、重建。",
      "欧拉公式一出场，旋转这件事就有了最漂亮的写法。你会发现，FFT 不是在背公式，而是在把旋转写成代码。",
    ],
    questions: [
      q(
        "为什么采样率不能随便低？",
        ["因为电脑会发热", "因为最高频率会被误认成更低频率", "因为数组长度会变短", "因为 matplotlib 会报错"],
        1,
        "这正是 Nyquist 定理要提醒你的事情。",
        "采样率至少要覆盖两倍最高频率，才不容易混叠。",
      ),
      q(
        "欧拉公式 `e^{iθ}` 在 FFT 里最重要的直觉是什么？",
        ["它只是一个随机技巧", "它把旋转写成了复指数", "它会自动降噪", "它能直接读出歌词"],
        1,
        "你要把“旋转因子”当成平面上的转动。",
        "当旋转变得可计算，DFT 才有了漂亮的矩阵写法。",
      ),
      q(
        "窗口函数主要是在缓解什么问题？",
        ["频谱泄漏", "显存不足", "标签错误", "音量不够大"],
        0,
        "硬切一段信号，相当于给频谱制造尖锐边缘。",
        "窗口不是为了变大声，而是为了让频谱更干净。",
      ),
    ],
  },
  {
    id: "phase-2",
    title: "第 2 章：ML / 深度学习地基",
    boss: "反向传播骑士",
    artifact: {
      icon: "∇",
      name: "梯度卷轴",
      desc: "把损失往下推的那卷手抄秘籍。",
    },
    source: ["docs/current/course/LEARNING_PLAN.md", "docs/current/course/week-03-checklist.md"],
    narrative: [
      "训练并不神秘，它只是一个会不断修正误差的流程。你先让损失出现，再沿着梯度往下走，模型就会一点点把事情做对。",
      "从最早的误差传播思想，到今天的 autograd 和训练循环，背后的逻辑一直都很朴素：记录路径，再把导数倒着传回去。",
    ],
    questions: [
      q(
        "梯度下降在做什么？",
        ["沿着损失下降最快的方向更新参数", "让数据自动变大", "把梯度变成图像", "把学习率设成 0"],
        0,
        "它不是在“猜”，而是在系统地找更低的损失。",
        "模型训练的核心，就是不断沿下降方向迈步。",
      ),
      q(
        "autograd 的本质是什么？",
        ["随机数生成器", "记录计算图并把梯度反向传回", "把 Python 变慢", "把矩阵自动转成标量"],
        1,
        "前向算一次，反向把每个节点的贡献算清楚。",
        "这就是为什么我们要从计算图一步步写起。",
      ),
      q(
        "mel 特征更接近什么？",
        ["人耳对频率的感知", "随机噪声", "图片的边缘检测", "字典排序"],
        0,
        "mel 标度是把物理频率拉向感知频率。",
        "这也是音频特征和人耳直觉对齐的关键。",
      ),
    ],
  },
  {
    id: "phase-3",
    title: "第 3 章：Speech Core (ASR)",
    boss: "对齐裁判",
    artifact: {
      icon: "↔",
      name: "对齐胸章",
      desc: "把波形一步步翻成文字的准入标记。",
    },
    source: ["docs/current/course/LEARNING_PLAN.md", "docs/current/course/week-04-checklist.md"],
    narrative: [
      "从传统声学模型一路走到端到端，ASR 的历史其实就是“怎么把对齐这件事讲明白”的历史。CTC 像一座桥，让你看见对齐不是玄学，而是动态规划能解决的账。",
      "Whisper 上场以后，训练目标和解码策略都换了说法，但你真正需要抓住的，依然是：模型如何在时间轴上学会听懂人说话。",
    ],
    questions: [
      q(
        "CTC 里的 blank 主要起什么作用？",
        ["让模型更快", "允许对齐和压缩重复", "把文本变成大写", "替代声学特征"],
        1,
        "它让不同长度的路径都能映射到同一个标签序列。",
        "blank 是对齐问题里的缓冲区。",
      ),
      q(
        "Whisper 的训练目标更接近什么？",
        ["纯 CTC", "seq2seq / cross-entropy", "聚类", "线性回归"],
        1,
        "它不是沿着 CTC 那条老路走的。",
        "Whisper 更像标准的编码器-解码器范式。",
      ),
      q(
        "WER 主要衡量什么？",
        ["词错误率", "窗口函数误差", "权重更新率", "字节压缩率"],
        0,
        "它是语音识别最常见的评价指标之一。",
        "词错得越少，WER 越低。",
      ),
    ],
  },
  {
    id: "phase-4",
    title: "第 4 章：Music Core",
    boss: "旋律机灵鬼",
    artifact: {
      icon: "♫",
      name: "旋律地图",
      desc: "把歌变成向量，再把向量变成推荐。",
    },
    source: ["docs/current/course/LEARNING_PLAN.md", "src/aurora/music/README.md"],
    narrative: [
      "音乐 AI 的乐趣，在于你会开始看到“听感”如何变成可计算的结构。你不只是听到旋律，还会看到节奏、音级、相似度和向量空间。",
      "从特征工程走向 embedding，再到近邻搜索，音乐推荐背后其实是一条很工程、也很漂亮的路线。",
    ],
    questions: [
      q(
        "chroma 特征更关心什么？",
        ["音级 / 调性相关性", "波形采样抖动", "梯度方向", "说话人年龄"],
        0,
        "它会把不同八度里的同名音高压到一起看。",
        "chroma 更像在听“音高关系”而不是原始波形。",
      ),
      q(
        "embedding 的意义是什么？",
        ["把歌曲变成可比较的向量", "把音频压成文本", "把谱图转成 PDF", "把采样率提高一倍"],
        0,
        "向量化以后，推荐和检索才有了统一距离。",
        "它是“相似”这件事能被机器处理的前提。",
      ),
      q(
        "k-NN 相似搜索主要依赖什么？",
        ["距离 / 相似度", "歌词长度", "文件后缀", "是否是同一歌手"],
        0,
        "先算距离，再看谁离得最近。",
        "向量空间里的近邻，就是推荐的起点。",
      ),
    ],
  },
  {
    id: "phase-5",
    title: "第 5 章：LLM + RAG + Agent",
    boss: "检索图书馆长",
    artifact: {
      icon: "⌁",
      name: "检索芯片",
      desc: "给大模型装上一座可查可问的图书馆。",
    },
    source: ["docs/current/course/LEARNING_PLAN.md", "src/aurora/rag/README.md", "src/aurora/llm/README.md"],
    narrative: [
      "进入大模型这章，你会更清楚地看到：参数规模、上下文长度、检索、采样、量化，这些都不是孤立的点，而是一整套工程选择。",
      "从 Transformer 到 LoRA，再到给模型接上一座图书馆，问题不再只是“模型会不会答”，而是“模型能不能把答案说得又准又快，又能追溯来源”。",
    ],
    questions: [
      q(
        "LoRA 为什么受欢迎？",
        ["因为它会自动标注数据", "因为它用低秩适配减少训练参数", "因为它只能跑在手机上", "因为它能直接替代检索"],
        1,
        "关键是只动一小部分参数，也能有效适配新任务。",
        "少量可训练参数，换来更低的成本。",
      ),
      q(
        "KV cache 的作用是什么？",
        ["让模型复读一遍所有内容", "复用历史 key/value，加快推理", "把输入变成图片", "让 tokenizer 更聪明"],
        1,
        "它在自回归生成时能省掉大量重复计算。",
        "缓存的是历史上下文，不是魔法。",
      ),
      q(
        "RAG 的关键环节是什么？",
        ["检索 + 生成", "采样 + 混音", "分词 + 归一化", "窗函数 + FFT"],
        0,
        "先找资料，再让模型根据资料回答。",
        "检索把模型和知识库连起来。",
      ),
    ],
  },
  {
    id: "phase-6",
    title: "第 6 章：整合 + 1 个 Demo + MLOps",
    boss: "终局总工",
    artifact: {
      icon: "★",
      name: "终局徽章",
      desc: "把所有模块真正合体的最后奖励。",
    },
    source: ["docs/current/course/LEARNING_PLAN.md", "docs/current/course/cloud_gpu_plan.md"],
    narrative: [
      "走到完成 Phase 6 这一步，训练就不再神秘了。你会发现它其实就是一套可以手写、可以调试、也可以一点点看着收敛的流程。",
      "而接下来，我们最重要的事不是再堆新名词，而是把这整条链路讲清楚、跑稳定、交给别人也能复现。",
    ],
    questions: [
      q(
        "最终 demo 最重要的不是？",
        ["把所有缩写都塞进去", "把链路讲清并能跑通", "把页面做得最花", "把参数写得最多"],
        1,
        "面试和展示都看重“可解释 + 可复现”。",
        "一个讲得明白的端到端结果，比一堆半成品更有力量。",
      ),
      q(
        "调试训练或推理时，最有价值的证据是什么？",
        ["截图越多越好", "测试、日志、可复现输入", "感觉像是对的", "别人也卡过"],
        1,
        "证据链比印象更重要。",
        "能复现，才真正能修。",
      ),
      q(
        "通关之后，下一步最值得做的是？",
        ["把名字改得更大", "做出能讲的端到端作品", "把 notebook 全删掉", "只背概念不写代码"],
        1,
        "你已经有了零件，现在要拼出作品。",
        "能讲清楚的作品，才是你自己的资产。",
      ),
    ],
  },
];

const defaultSave = () => ({
  activePhaseIndex: 0,
  phaseProgress: QUESTS.map(() => 0),
  xp: 0,
  streak: 0,
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

let state = loadState();
if (!state) {
  state = defaultSave();
}

const els = {
  heroText: document.getElementById("hero-text"),
  startButton: document.getElementById("start-button"),
  resumeButton: document.getElementById("resume-button"),
  resetButton: document.getElementById("reset-button"),
  currentStage: document.getElementById("current-stage"),
  level: document.getElementById("player-level"),
  xp: document.getElementById("player-xp"),
  clear: document.getElementById("player-clear"),
  streak: document.getElementById("player-streak"),
  xpFill: document.getElementById("xp-fill"),
  stageTitle: document.getElementById("stage-title"),
  bossChip: document.getElementById("boss-chip"),
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
  openingLessons: document.getElementById("opening-lessons"),
  foundationTracks: document.getElementById("foundation-tracks"),
  weeklyCheckpoints: document.getElementById("weekly-checkpoints"),
};

const INTRO_COPY = courseSnapshot.subtitle;

function loadState() {
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    if (!raw) return null;
    const parsed = JSON.parse(raw);
    if (!parsed || typeof parsed !== "object") return null;
    return {
      ...defaultSave(),
      ...parsed,
      phaseProgress: normalizeProgress(parsed.phaseProgress),
      inventory: Array.isArray(parsed.inventory) ? parsed.inventory : defaultSave().inventory,
      log: Array.isArray(parsed.log) ? parsed.log.slice(0, 8) : defaultSave().log,
    };
  } catch {
    return null;
  }
}

function normalizeProgress(progress) {
  if (!Array.isArray(progress)) return QUESTS.map(() => 0);
  return QUESTS.map((_, index) => Math.max(0, Number(progress[index] ?? 0)));
}

function saveState() {
  window.localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  updateResumeButton();
}

function updateResumeButton() {
  if (!els.resumeButton) return;
  els.resumeButton.disabled = !window.localStorage.getItem(STORAGE_KEY);
}

function levelFromXp(xp) {
  return 1 + Math.floor(xp / 120);
}

function xpToNext(xp) {
  const level = levelFromXp(xp);
  const nextThreshold = level * 120;
  return Math.max(0, nextThreshold - xp);
}

function completedCount() {
  return QUESTS.reduce((count, quest, index) => count + (state.phaseProgress[index] >= quest.questions.length ? 1 : 0), 0);
}

function unlockedIndex() {
  for (let i = 0; i < QUESTS.length; i += 1) {
    if (state.phaseProgress[i] < QUESTS[i].questions.length) {
      return i;
    }
  }
  return QUESTS.length - 1;
}

function currentQuest() {
  return QUESTS[state.activePhaseIndex] ?? QUESTS[0];
}

function currentQuestion() {
  const quest = currentQuest();
  const progress = state.phaseProgress[state.activePhaseIndex] ?? 0;
  return quest.questions[progress] ?? null;
}

function phaseIsComplete(index) {
  return state.phaseProgress[index] >= QUESTS[index].questions.length;
}

function addLog(kind, text) {
  state.log.unshift({ kind, text });
  state.log = state.log.slice(0, 8);
}

function ensureInventory(item) {
  if (!item) return;
  if (state.inventory.some((entry) => entry.name === item.name)) return;
  state.inventory.unshift(item);
}

function setActivePhase(index) {
  const unlock = unlockedIndex();
  if (index > unlock && index !== state.activePhaseIndex) {
    addLog("系统", "这一区域还没有解锁，先打通前面的章节。");
    render();
    saveState();
    return;
  }

  state.activePhaseIndex = Math.max(0, Math.min(index, QUESTS.length - 1));
  addLog("系统", `进入 ${currentQuest().title}。`);
  render();
  saveState();
}

function startAdventure() {
  setActivePhase(0);
  els.heroText?.scrollIntoView({ behavior: "smooth", block: "start" });
}

function resetAdventure() {
  window.localStorage.removeItem(STORAGE_KEY);
  state = defaultSave();
  render();
  saveState();
  addLog("系统", "存档已清空，新的冒险重新开始。");
  render();
}

function answer(choiceIndex) {
  const quest = currentQuest();
  const progress = state.phaseProgress[state.activePhaseIndex] ?? 0;
  const question = currentQuestion();
  if (!question) return;

  if (choiceIndex !== question.answer) {
    state.streak = 0;
    addLog("失手", `${question.hint} 再试一次，你已经很接近了。`);
    render();
    saveState();
    return;
  }

  state.phaseProgress[state.activePhaseIndex] = progress + 1;
  state.xp += XP_PER_QUESTION;
  state.streak += 1;
  addLog("命中", `${question.note} +${XP_PER_QUESTION} XP。`);

  if (phaseIsComplete(state.activePhaseIndex)) {
    state.xp += XP_PER_PHASE_CLEAR;
    state.streak = 0;
    ensureInventory(quest.artifact);
    addLog("通关", `你拿到了「${quest.artifact.name}」；下一章已经解锁。 +${XP_PER_PHASE_CLEAR} XP。`);
    if (state.activePhaseIndex === QUESTS.length - 1) {
      addLog("终章", "整条链路已经合体。现在你可以带着这套作品去讲、去演示、去继续迭代。");
    }
  } else {
    addLog("进展", `继续拆解 ${quest.boss} 的下一个招式。`);
  }

  render();
  saveState();
}

function advancePhase() {
  const nextIndex = Math.min(state.activePhaseIndex + 1, QUESTS.length - 1);
  if (!phaseIsComplete(state.activePhaseIndex)) {
    addLog("系统", "这一章还没通关，先把当前问题打完。");
    render();
    saveState();
    return;
  }

  if (state.activePhaseIndex === QUESTS.length - 1) {
    state.activePhaseIndex = 0;
    addLog("系统", "终章已过，重新从序章开始复盘。");
  } else {
    state.activePhaseIndex = nextIndex;
    addLog("系统", `进入 ${currentQuest().title}。`);
  }

  render();
  saveState();
}

function renderNarrative(quest) {
  els.stageNarrative.innerHTML = "";
  quest.narrative.forEach((paragraph) => {
    const p = document.createElement("p");
    p.textContent = paragraph;
    els.stageNarrative.appendChild(p);
  });
}

function renderChoices(question) {
  els.choiceList.innerHTML = "";
  question.choices.forEach((choice, index) => {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = choice;
    button.addEventListener("click", () => answer(index));
    els.choiceList.appendChild(button);
  });
}

function renderCompleteState(quest) {
  els.questionCount.textContent = "本章已通关";
  els.questionHintPill.textContent = "下一章已经解锁，点右上角继续前进";
  els.questionPrompt.textContent = `你已经击败 ${quest.boss}。`;
  els.choiceList.innerHTML = `
    <div class="choice-static correct">已获得「${quest.artifact.name}」</div>
    <div class="choice-static">点击右上角继续下一章。</div>
  `;
  els.nextButton.disabled = false;
  els.nextButton.textContent = state.activePhaseIndex === QUESTS.length - 1 ? "重新复盘" : "进入下一章";
}

function renderRoadmap() {
  const unlock = unlockedIndex();
  els.roadmapList.innerHTML = "";

  const items = [
    {
      title: "序章 · 欢迎入学",
      deliverable: "先把 Jupyter、终端和课程地图打通",
      checkpoint: courseSnapshot.openingLessons[0]?.title ?? "开场五课",
      label: "L01–L05",
      isPrologue: true,
    },
    ...courseSnapshot.monthlyPhases.map((phase, index) => ({
      title: `第 ${phase.month} 章 · ${phase.title}`,
      deliverable: phase.deliverable,
      checkpoint: phase.checkpoint,
      label: `Month ${phase.month}`,
      index: index + 1,
    })),
  ];

  items.forEach((item, index) => {
    const phaseIndex = item.isPrologue ? 0 : item.index;
    const completed = phaseIsComplete(phaseIndex);
    const active = phaseIndex === state.activePhaseIndex;
    const locked = phaseIndex > unlock;

    const card = document.createElement("article");
    card.className = `roadmap-card ${completed ? "completed" : ""} ${active ? "active" : ""}`;
    card.innerHTML = `
      <div class="roadmap-meta">
        <span>${item.label}</span>
        <span>${completed ? "已通关" : locked ? "锁定" : active ? "进行中" : "可进入"}</span>
      </div>
      <h3>${item.title}</h3>
      <p><strong>产出</strong>：${item.deliverable}</p>
      <p><strong>目标</strong>：${item.checkpoint}</p>
    `;
    const button = document.createElement("button");
    button.type = "button";
    button.className = "mini";
    button.textContent = locked ? "锁定中" : completed ? "复盘这一章" : active ? "正在进行" : "进入这一章";
    button.disabled = locked || active;
    button.addEventListener("click", () => setActivePhase(phaseIndex));
    card.appendChild(button);
    els.roadmapList.appendChild(card);
  });
}

function renderInventory() {
  els.inventoryList.innerHTML = "";
  const items = state.inventory.slice(0, 8);
  items.forEach((item, index) => {
    const card = document.createElement("article");
    card.className = "inventory-card";
    card.innerHTML = `
      <div class="inventory-icon">${item.icon ?? "▣"}</div>
      <div>
        <h3>${item.name}</h3>
        <p>${item.desc}</p>
      </div>
    `;
    if (index === 0) {
      card.style.borderColor = "rgba(102, 232, 255, 0.26)";
    }
    els.inventoryList.appendChild(card);
  });
}

function renderCurriculum() {
  els.openingLessons.innerHTML = "";
  courseSnapshot.openingLessons.forEach((lesson) => {
    const chip = document.createElement("span");
    chip.className = "chip";
    chip.innerHTML = `<strong>${lesson.code}</strong>${lesson.title}`;
    els.openingLessons.appendChild(chip);
  });

  els.foundationTracks.innerHTML = "";
  courseSnapshot.foundationTracks.forEach((track) => {
    const chip = document.createElement("span");
    chip.className = "chip";
    chip.innerHTML = `<strong>${track.range}</strong>${track.title} · ${track.service}`;
    els.foundationTracks.appendChild(chip);
  });

  els.weeklyCheckpoints.innerHTML = "";
  courseSnapshot.weeklyCheckpoints.forEach((week) => {
    const card = document.createElement("article");
    card.className = "weekly-card";
    card.innerHTML = `
      <div class="weekly-meta">
        <span>${week.range}</span>
        <span>${week.file.split("/").pop()}</span>
      </div>
      <strong>${week.title}</strong>
      <p>${week.target}</p>
    `;
    els.weeklyCheckpoints.appendChild(card);
  });
}

function renderLog() {
  els.battleLogList.innerHTML = "";
  state.log.slice(0, 5).forEach((entry) => {
    const row = document.createElement("div");
    row.className = "log-entry";
    row.innerHTML = `<strong>【${entry.kind}】</strong> ${entry.text}`;
    els.battleLogList.appendChild(row);
  });
}

function renderStats() {
  const level = levelFromXp(state.xp);
  const xpIntoLevel = state.xp - (level - 1) * 120;
  const xpPercent = Math.max(0, Math.min(100, (xpIntoLevel / 120) * 100));
  const completed = completedCount();
  const quest = currentQuest();
  const progress = state.phaseProgress[state.activePhaseIndex] ?? 0;
  const questionTotal = quest.questions.length;

  els.currentStage.textContent = `${quest.title}`;
  els.level.textContent = String(level);
  els.xp.textContent = String(state.xp);
  els.clear.textContent = `${completed}/${QUESTS.length}`;
  els.streak.textContent = String(state.streak);
  els.xpFill.style.width = `${xpPercent}%`;
  els.stageTitle.textContent = quest.title;
  els.bossChip.textContent = `${quest.boss} · HP ${phaseIsComplete(state.activePhaseIndex) ? 0 : Math.max(0, Math.round(100 - (progress / questionTotal) * 100))}`;
  els.phaseSource.textContent = `资料来源：${quest.source.join(" · ")}`;

  if (phaseIsComplete(state.activePhaseIndex)) {
    renderCompleteState(quest);
  } else {
    const question = currentQuestion();
    els.questionCount.textContent = `问题 ${progress + 1} / ${questionTotal}`;
    els.questionHintPill.textContent = "先想一想，再出手";
    els.questionPrompt.textContent = question?.prompt ?? "没有可用的问题。";
    els.nextButton.disabled = !phaseIsComplete(state.activePhaseIndex);
    els.nextButton.textContent = state.activePhaseIndex === QUESTS.length - 1 ? "重新复盘" : "进入下一章";
    if (question) {
      renderChoices(question);
    } else {
      els.choiceList.innerHTML = "";
    }
  }
}

function render() {
  renderStats();
  renderLog();
  renderInventory();
  renderRoadmap();
  renderCurriculum();
}

function wireEvents() {
  els.startButton?.addEventListener("click", startAdventure);
  els.resumeButton?.addEventListener("click", () => {
    const saved = loadState();
    if (saved) {
      state = saved;
      addLog("系统", "继续上次的存档。");
      render();
      saveState();
      return;
    }
    addLog("系统", "当前没有存档，先从序章开始。");
    render();
  });
  els.resetButton?.addEventListener("click", resetAdventure);
  els.nextButton?.addEventListener("click", advancePhase);
}

function bootstrap() {
  wireEvents();
  render();
  updateResumeButton();
  if (state.log.length === 1 && !window.localStorage.getItem(STORAGE_KEY)) {
    addLog("系统", INTRO_COPY);
    render();
  }
}

bootstrap();
