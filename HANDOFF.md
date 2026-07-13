# Aurora 接手指南 · Handoff Guide

> 面向下一位接手 Aurora 的开发者。目标：**5 分钟看懂现状，10 分钟找到该做的下一步。**
> 本文由一次全仓库并行审计（6 个子系统深读）综合而成，日期 2026-07-10。
> 权威事实以代码 / `docs/current/audit/INDEX.md` 为准；历史叙事见未跟踪的
> `DEV_SUMMARY_2026-07-03.md`（本地日志，勿提交）。

---

## 0. 一句话现状

Aurora 是一套「从零手写、no API wrappers」的音频 AI 教学 + 研究系统。
**课程侧已完整交付并三轮独立复审，DSP 核心是真材实料；但整条「证据链」目前还
没有任何一个训练出来的模型或上线的**推理** Demo（课程门户/游戏已上线,不算数）
——这就是接手要补的核心缺口。**

| 门禁 | 状态 | 命令 |
|---|---|---|
| 单元测试 | ✅ 82 passed (~4s) | `make test` / `python -m pytest` |
| Notebook 验收门 | ✅ PASSED all checks（99 本） | `python scripts/validate_pipeline.py` |
| Lint | ✅ ruff（src/tests） | `make lint` |
| Format | black 88 列 | `make format` |
| Pages 部署 | ✅ https://djzoom.github.io/AURORA/ | push main 自动（aurora-quest-pages.yml） |

工作树干净；2026-07-12/13 会话的增量（视频资料库、全面开源、移动端与世界地图）
见 §7 与本地日志 `DEV_SUMMARY_2026-07-13.md`。

---

## 1. 仓库地图

```
src/aurora/           核心库（一个成熟核 audio + 三个较年轻核 llm/music/speech + 6 个占位核）
tests/                镜像 src 树（audio/llm/music 有测试；speech 无测试目录）
notebooks/            99 本课程 L01–L99，11 个阶段；README.md 是课程标题的唯一真源
scripts/              验收门 + 维护工具 + 6 个一次性历史迁移脚本
docs/current/         权威文档（audit 681 文件 · obsidian 知识图谱 159 文件 · course · blog）
docs/archive/         历史文档（读 current/，除非刻意查历史）
aurora-quest/         配套 8-bit 教学 RPG + 交互版视频资料库（纯静态，Pages 在线）
.github/workflows/    ci.yml · aurora-quest-pages.yml
ROADMAP.md            六个月路线图 + 未完成项（真正的 backlog）
CLAUDE.md / AGENTS.md / CONTRIBUTING.md   工作约定
```

---

## 2. 子系统状态盘点

### 2.1 核心库 `src/aurora/`
- **audio（皇冠）**：FFT/STFT/mel/DCT/MFCC/WAV 全手写、纯 NumPy，逐一 pin 到
  `numpy.fft`/参考公式，误差 <1e-10。**src 内零 librosa/scipy 依赖**——铁律真正落地。
- **llm**：`kvcache` / `retrieve`(TF-IDF) / `sample`(top-k/top-p) 均实现且有测试。
- **music**：`features`(chroma/onset/beat) / `similarity`(k-NN) 有测试；`embed`(torch
  MusicEncoder + triplet/NT-Xent) **无测试**。
- **speech**：`metrics.py`(edit_distance/WER) 是**真代码但伪装成 stub**——
  `speech/__init__.py` 仍是 "planned" 一行、不 re-export，`from aurora.speech import wer` 会失败。**且无 `tests/speech/`**。
- **占位核（仅 `__init__` docstring）**：`mlops` `multimodal` `rag` `realtime`
  `research` `tts`。README 架构表用 ✅/▷/▢ 如实标注，没有过度承诺。
- **viz 层**：`aviz`/`laviz`/`_plot_theme` 未测试；`aviz` 用 `np.fft.rfft` + 内联
  mel/window，**故意不吃自己的核**（改核不会改图，反之亦然）。`_plot_theme` 会
  进程级 monkeypatch matplotlib（有幂等 guard）。

**已知代码级瑕疵（非阻塞，接手可择机修）**：
- `llm/retrieve.cosine_retrieve` 查询向量是 raw-TF，文档是 TF-IDF——不对称，非教科书写法。
- `io.py` docstring 说自己解析 RIFF，实际用 stdlib `wave`——事实性口误。
- `rfft` 先算全复 FFT 再切一半（~2x 冗余，教学可接受）。

### 2.2 课程 `notebooks/`（99 本）
- 11 阶段全部完成、三轮独立复审（Opus 4.8 执行态 → Fable 5 静态 → Grok prose），
  全部过 `validate_pipeline.py`。
- **统一模板**：H1 标题 → nav 格(tag `['nav']`) → 科普 intro → demo → ✏️TODO
  (`raise NotImplementedError`+`...`) → 白板/闭卷推导 + 对答案格 → 自评 `l##_review={..:None}` 门。
- **两态机制是「带外」的**：学生态 notebook 永远含占位符，答案在
  `solutions/L##_*_solutions.md`；检查格吞掉 `NotImplementedError/TypeError` 打 ⬜。
  **⚠️ 门禁全绿 ≠ 习题已做完。** 绝不要把答案粘进 notebook 格。
- 13 本 🎨 视觉复盘课（多为 `L##_visual_*`，例外 `L21_aurora_matrices`）。
- 小瑕疵：4 本视觉课缺自评门（L42/L48/L53/L82）；少量散落文件与 13 个提交进源目录的 PNG。

### 2.3 工具与门禁 `scripts/` + CI
- `validate_pipeline.py` = 验收门（5 查：JSON / 语法 / 音频流水线 / 多核冒烟 / 结构一致）。
- **🔴 最大结构缺口：验收门没进 CI。** `ci.yml` 只跑 ruff + pytest。有人改坏
  notebook / 流水线 / 结构约定，CI 仍绿——门禁目前是「本地手动仪式」。
- 可复用工具：`audit_drift` `add_nav_cells` `build_knowledge_graph` `build_docs`
  `demo_audio` `sim_students_audit`(多智能体审课，烧 API 额度) `generate_aurora_quest_data`。
- **6 个 `apply_*.py` 是一次性历史迁移**（7-01 已应用，非幂等，勿盲目重跑）。
- 工具依赖未声明进 extras：`rich`/`pandoc`/`xhtml2pdf`/`wandb`/Node——`make install` 装不上。
- `log_ci_metrics.py` 是**孤儿**：其 docstring 描述的 W&B CI 步骤在任何 workflow 里都不存在。

### 2.4 文档 `docs/current/`
- audit 是皇冠（6 轮复审 + 99 本逐课修复记录 + 模拟学生法）；`INDEX.md` 是审计状态的唯一真源
  （成绩 A-×79 / B+×13 / B×7）——`00/01/02` 是**过时快照**，别引用它们的数字。
- obsidian 是真知识图谱（~462 词/9 域），但 concept 页只建了 42/462（其余 v2 backlog）。
- **🔴 blog 是最显眼的内容缺口**：只有 `0001-fft-from-scratch.md` 且仍是草稿；
  ROADMAP 有 2 个未勾的 blog TODO。
- 分区/部分完成：`prose_polish/` 空目录；`sim_students/` 只到 L73；week-checklist 只到第 4 周；video 只有 L01。

### 2.5 开放模式
- 本仓库 public、MIT、L01–L99 全部开放，开放原则见 `docs/current/OPENNESS.md`。

### 2.6 配套游戏 Aurora Quest（已上线 Pages，7-10 精修见 §6，7-12/13 增量见 §7）
- 在线地址 https://djzoom.github.io/AURORA/ ；移动端为 App 式固定视口
  （战斗一屏 + 底部 Tab 分页：战斗/地图/战利品/更多）。
- 冒险地图 = 像素世界地图（`src/data/worldmap.js` 数据驱动）：Phase→地形区、
  Lesson→铺路石、依赖→汇流/三岔流线 + ◀承接路标、缩放=LOD 层级切换。
- 视频资料库 `video-library.html`：92 条名师课（源 `docs/current/course/VIDEO_LIBRARY.md`
  → `scripts/generate_video_library_data.mjs` 生成数据），支持筛选/搜索/打卡
  （localStorage，`src/video-library-state.js` 沿用 state.js 存档约定）。

---

## 3. 接手该做什么（优先级 backlog）

> 全部未完成项来自 `ROADMAP.md`。核心判断：**课程已收尾，缺的是「训练出来的模型 +
> 上线的 Demo」这条证据链。** 下面按「投入产出比」排序。

### 🥇 如果只做三件事
1. **训练 KWS 分类器**（Speech Commands，Colab 免费 T4，~10 分钟，~¥0.02）——
   Phase 2「第一个训练出来的模型」里程碑，最高信噪比、最低成本，让证据链从「只有
   notebook」变成「有真模型」。
2. **把验收门接进 CI**（`ci.yml` 加一步 `python scripts/validate_pipeline.py`）——
   否则项目自己的头号质量门根本不保护 main。
3. **在真实 LibriSpeech 上跑 MFCC 并与 librosa 对拍**——Phase 1 唯一剩项，
   证明从零音频核在真语音上匹配 ground truth（librosa 仅作校验参照，不入 src）。

### 本地可做（无需 GPU）
| 任务 | 为什么 | 量级 |
|---|---|---|
| 修 ROADMAP 漂移：FFT blog 已存在 → 勾上；`cloud_gpu_plan` 标注未执行 | 零成本纠错，避免后继者误判 | S |
| 加 `tests/speech/test_metrics.py` + 从 `speech/__init__` re-export WER | 补齐已知约定违规（无 tests/speech） | S |
| 验收门进 CI + 归档 6 个 `apply_*.py` 到 `scripts/archive/` + 声明工具 extras | 保护 main、清理 scripts/ | S–M |
| MFCC vs LibriSpeech 对拍（脚本/notebook，非 src） | Phase 1 收尾 | M |
| 写第二篇 blog「从线性回归到反向传播」+ 定稿 FFT blog | blog 是显式交付物 | M |
| 把 `cloud_gpu_plan.md` 真正落进 L93/L64/L72 | 解锁并降险后续两次云训练 | M |
| 给 `music/embed` 补测试（MusicEncoder 形状 + triplet/NT-Xent） | 音乐核的面试门面目前零验证 | M |

### 需要云 GPU
| 任务 | 环境 | 量级 |
|---|---|---|
| 训练 KWS CNN（Speech Commands）+ 存 checkpoint + W&B run | Colab T4 ~10min | M |
| Whisper-small LoRA 微调（LibriSpeech 子集）+ 报 WER + 存 checkpoint | A100 ~2–4h（RunPod/Lambda，用计划里的 checkpoint/resume） | L |
| 部署 Aurora v1（mic → ASR → LLM）+ 上线 Demo URL + Docker/CI | 云/部署 | L |

### 拉伸（最低优先级，前面四个核心产物稳了再碰）
- 建实占位核：`rag`（在现有 TF-IDF 上做编排）、`realtime`、`tts`。
- 流式 ASR（因果注意力分块）、MusicGen 微调。

---

## 4. 铁律与约定（务必遵守）

- **Git 身份**：**作者**恒为 `djzoom <djwangzhong@gmail.com>`（全历史单作者身份，
  仅 `djzoom` / `0xGarfield` 两个别名同邮箱）。**只允许 djzoom 一个署名**：
  不加 `Co-Authored-By: Claude …` trailer、不留 claude.ai 会话链接
  （历史上曾有过的 7 处已于 2026-07-12 filter-branch 清除）。贡献只在 **main** 计数。
- **No API wrappers**：核心能力从零写算法。Audio Core 里 numpy 只当数组容器/逐元素运算，
  **src 内禁 librosa / scipy.signal**；librosa/torch/transformers 只能作校验参照或
  云训练脚本/notebook 里、且藏在按核的 optional-dependency extras 后。
- **提交前**：`make format` + `make lint` + `make test`（应 82 passed）+
  `python scripts/validate_pipeline.py`（应 PASSED all checks）。
- **评审哲学**：按结构 / 概念 / 习题打分，**不纠 atol、import 风格等代码细枝末节**。
- **写作风格（课程 markdown/notebook）**：科普风，先问题/类比/故事、后公式；术语双语标注「中文（English）」。
  （本 HANDOFF、DEV_SUMMARY 等**内部工程文档**不受此约束，用技术文档风即可。）
- **Notebook 改法**：就地字符串替换 + `json.dumps(indent=1, ensure_ascii=False)` + 保留尾换行，
  零 format churn；保住两态门（学生态停在每个 TODO，答案态 `exit 0`；guard 抓 `(NotImplementedError, TypeError)`）。
- **生成物勿手改**：`course-snapshot.generated.js`（`node scripts/generate_aurora_quest_data.mjs`）、
  `video-library.generated.js`（`node scripts/generate_video_library_data.mjs`）、
  nav 格（`make nav-cells`）、obsidian 派生层（`build_knowledge_graph.py`）。
- **改标题**：先改 `notebooks/README.md` 表，再跑 `make nav-cells`（它从 README 解析 prev/next）。

---

## 5. 已知陷阱

- `fft()` 只收 2 的幂长度（否则 ValueError）；`stft()` 补零到 next_power_of_two；`dft()` 是任意长度回退。
- 验收门结构检查**硬编码 15 本推导课**必须含「闭卷推导/推导检查」格：
  {L38,L44,L47,L49,L50,L54,L56,L67,L69,L70,L83,L84,L85,L86,L89}——删了会挂门。
- 本地 `make install` 装 `.[dev,notebooks]`，CI 只装 `.[dev]`——加了需 nbformat/matplotlib 的测试会本地过、CI 挂。
- `sim_students_audit.py` 烧真实 API 额度、持 fcntl 锁，单实例；用 `sim_students_tui.py` 监控，别开第二个。
- main 曾被 filter-branch + 强推并与并行 Codex 会话冲突丢过 4 个 commit——任何未来强推都要小心。
- 主源码里 `np.fft` 只出现在 `aviz.py` 和 docstring/测试（作参照）——别往核心模块加 `np.fft`，会破铁律。

---

## 6. 本次对配套游戏 Aurora Quest 的精修与重构

`aurora-quest/` 是一个纯静态、无依赖的 8-bit 教学 RPG（序章 + 6 章，每章 3 道选择题，
XP/等级/连击/战利品，localStorage 存档，课程地图从 `LEARNING_PLAN.md` 生成的快照渲染）。

**第一轮：精细修订**（保留既有设计，只做精准增强）：
- **答题视觉反馈**：接上 CSS 里早已定义却从未使用的 `.correct/.wrong` 高亮——答对/答错即时高亮，
  答错时揭示正确项并轻微抖动（尊重 `prefers-reduced-motion`）。
- **从零手写 8-bit 音效**（Web Audio 振荡器，无音频文件、无库——呼应 no-API-wrappers 且这是门音频课）：
  命中 / 失手 / 通关 / 终章四种音效，带可持久化的静音开关。
- **键盘操作**：`1–4` 选择、`Enter/N` 进入下一章、`M` 静音；选项带序号徽章自解释。
- **答题锁定**：反馈期间锁输入，防连点。

**第二轮：模块化重构**（行为不变，端到端冒烟做回归安全网）：

```
aurora-quest/src/
  app.js            入口 + 游戏机制（持有唯一 state；动作→render→persist 单向流）
  ui.js             渲染层（只读 state，交互回调经 handlers 注入）
  state.js          存档 + 派生查询（selector 与 mutator 分离，不碰 DOM）
  audio.js          8-bit 音效引擎（muted 由调用方传入，不持游戏状态）
  sprites.js        Boss 像素精灵（16×16 字符矩阵 + Canvas 逐像素渲染）
  data/quests.js    题库纯数据（改文案只动这里）+ XP 数值平衡常量
  course-snapshot.generated.js   生成物（node scripts/generate_aurora_quest_data.mjs）
```

- 重构中修复一个**真 bug**：`renderNarrative()` 原是死代码——每章剧情文字写好了却从未渲染
  （`#stage-narrative` 容器永远为空），现已接入渲染流程；顺带删除死函数 `xpToNext`。
- 重构中发现并修复 **`.gitignore` 陷阱**：根规则裸 `data/` 会吞掉任意深度的 data 目录
  （包括 `src/data/quests.js`），已收窄为根级 `/data/`、`/datasets/`。
- `scripts/build_quest_bundle.mjs`：按依赖序拼接模块、剥离 import/export（支持多行 import），
  产出**单文件** `aurora-quest/dist/aurora-quest.html`（`file://` 双击即玩）。
  约束：模块只用命名导入/导出、顶层标识符全局唯一（脚本有残留检测兜底）。

**第三轮：8-bit 游戏化改版 + 对抗审查修复**（应用户要求「简化界面、提升趣味、像 8-bit 游戏」）：
- **像素 Boss 战**：7 个 Boss 全部用 16×16 字符矩阵手绘（`sprites.js`），Canvas 逐像素渲染 +
  `image-rendering: pixelated`——零图片文件，呼应 no-API-wrappers。答对 Boss 闪白抖动 + 伤害
  飘字「-33」；答错 Boss 格挡红闪 + 「MISS」；通关 Boss 灰化倒下。
- **分格 HP 血条**（10 格，低血量红色闪烁）、**横向像素关卡地图**（节点连线，完成绿/当前琥珀脉冲/
  锁定灰），地图说明仍与 `LEARNING_PLAN.md` 快照同步（改课程→地图变）。
- **简化**：砍掉「课程同步」三大板块与大段文案，布局收敛为 HUD 状态栏 + 战斗屏 + 地图/战利品。
- **修复第一轮对抗审查抓到的全部问题**（2 major + 2 minor + 1 nit）：
  ① 结算竞态——反馈窗口(460/820ms)内切章/重置/读档会把答题记到错误章节、可无限刷 XP：
  现 `inputLocked` 守卫所有改状态动作 + 结算前题目同一性校验；
  ② Enter 劫持——全局 Enter 抢走聚焦按钮/链接的默认激活：现 BUTTON/A 聚焦时让行；
  ③ 幻影存档——开场按 M 就凭空落盘：现无存档时只改内存；
  ④ 重置误清静音偏好：现跨重置保留；
  ⑤ 损坏存档砖机——`activePhaseIndex` 越界/字符串 xp/数组混入 null：`loadState` 现逐字段
  钳制消毒（含 inventory/log 元素级过滤）。

- **第二轮复核修复**（改版后再审出 8 个 minor/nit，全部修掉）：当前地图节点被 `button:disabled`
  误调暗；HP 血量对辅助技术不可见（现动态 aria-label）；`.hint-pill` 死选择器；XP 条 aria 修正
  （纯装饰 + 文本 stat 供值）；「清空进度」凭空重建存档 + 确认日志不落盘（现真清空，新档等真实
  动作再落盘）；存档字符串直接进 innerHTML 的本地篡改型 XSS（inventory/log/选项现全部 textContent
  组装）。

**验证**：模块 `node --check` 全过；精灵矩阵 7×16×16 逐行校验；DOM/WebAudio/timer stub
端到端冒烟 **49/49 通过**（含全部两轮 bug 修复的回归断言 + XSS 注入断言），且**同一套断言对
模块版和打包产物各跑一遍**（证明拼接语义与模块图等价）；两轮多智能体对抗审查（第一轮：行为对齐/
打包完整性/运行时 UX，3 agent；第二轮：接线/修复复核，2 agent），全部发现均已修复并有回归测试。

### 🔗 链接（可直接点开）
- **托管可玩版（推荐，立即可分享）**：<https://claude.ai/code/artifact/0d83de66-5121-455a-b358-f1d99341b1e7>
- 本地多文件版（ES module，需服务器）：
  `python -m http.server -d aurora-quest 8080` → <http://localhost:8080>
- 本地单文件版（双击即玩）：`node scripts/build_quest_bundle.mjs` → 打开 `aurora-quest/dist/aurora-quest.html`
- GitHub Pages：`aurora-quest-pages.yml` 已就绪，但部署门 `if repository_visibility == public`——
  **仓库转公开 + 开 Pages 后**才会上线到 `https://djzoom.github.io/AURORA/`（届时自动）。

---

*本文件为接手快照，随仓库演进请更新或替换。*

---

## 7. 2026-07-12/13 会话增量摘要

> 叙事细节见本地日志 `DEV_SUMMARY_2026-07-13.md`（未跟踪，勿提交）。

- **视频资料库**：92 条名师名校 YouTube 教程逐条对齐 L01–L99
  （`docs/current/course/VIDEO_LIBRARY.md` 单一数据源）+ 交互版页面
  （筛选/搜索/打卡/里程碑奖章）；README·notebooks·LEARNING_PLAN 均有入口。
- **全面开源**：仓库转 public（MIT，L01–L99 全部开放）；OPENNESS.md
  重写为全面开源宣言。
- **Git 身份**：全史 Co-Authored-By trailer 与会话链接清除,仅存 djzoom 署名
  （见 §4 铁律）。
- **Aurora Quest**：Pages 上线；移动端 App 式一屏布局 + 底部 Tab；像素世界地图
  （比喻映射 + 依赖拓扑 + LOD 缩放）；「更多」页 = 关于/作者(@DJWZ)/链接/分享。
- **注意**：`aurora-quest/dist/` 单文件 bundle 未随本轮重构重建
  （`scripts/build_quest_bundle.mjs`），需要离线版时先重跑并验证。
