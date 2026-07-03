# AURORA

**Audio Understanding, Reasoning and Orchestration Research Architecture**

A from-scratch audio-AI research system spanning DSP, speech recognition,
speech synthesis, music intelligence, LLMs, retrieval, agents, realtime
inference, and MLOps.

> **Guiding principle — no API wrappers.** Aurora is not "Whisper API + OpenAI
> API + ElevenLabs + Next.js." Every core is built to demonstrate
> first-principles understanding: the DSP layer is hand-written, the speech and
> music models are trained, the inference is run locally. The goal isn't a résumé
> that says *API integrator* — it's to become a **builder** with solid fundamentals
> who genuinely understands how things work, all the way down.

---

## What it does

A user uploads **speech, music, video, or a podcast**, and Aurora can:

> understand · analyze · transcribe · summarize · retrieve · generate · converse · recommend · synthesize

It is, in spirit, a fusion of **OpenAI Voice + Spotify + NotebookLM Audio +
Suno + Apple Siri**.

## Why this project

It spans the entire stack you need to *actually understand* audio/voice/music AI
end to end: **DSP · ML · Speech · Music · LLM · RAG · Agents · System Design ·
Cloud · Research** — the real thing, not a wrapper over someone else's model.

---

## System architecture

```
Aurora
├── aurora.audio      FFT / STFT / Mel / MFCC / WAV — fully implemented ✅
├── aurora.llm        KV-Cache / sampling / TF-IDF / RAG — implemented  ✅
├── aurora.music      features / similarity / embed — implemented        ✅
├── aurora.speech     metrics (WER) — partial; ASR training planned      ▷
├── aurora.realtime   mic → ASR → LLM → TTS pipeline — planned          ▢
└── aurora.mlops      Docker / W&B / CI — planned                       ▢
```

See [`ROADMAP.md`](ROADMAP.md) for the full six-month plan.

---

## Audio Core (implemented)

The foundation. Everything is written from first principles and validated
against reference implementations — **no librosa, no SciPy DSP.**

| Primitive | Module | Notes |
|---|---|---|
| DFT / FFT / IFFT | `aurora.audio.transforms` | iterative radix-2 Cooley-Tukey, validated against `numpy.fft` |
| Windows | `aurora.audio.windows` | Hann / Hamming / Blackman, periodic & symmetric |
| STFT & spectrograms | `aurora.audio.stft` | framing, magnitude & power |
| Mel scale & filterbank | `aurora.audio.mel` | HTK mel, triangular filters, log-mel (dB) |
| MFCC & DCT-II | `aurora.audio.mfcc` | orthonormal DCT from scratch |
| WAV I/O & generators | `aurora.audio.io` | PCM WAV read/write, sine/chirp |

### Quick start

```bash
pip install -e ".[dev]"
pytest                      # 82 tests, FFT validated against numpy
python scripts/demo_audio.py
```

```python
from aurora.audio import sine, mfcc, mel_spectrogram

x = sine(440.0, duration=1.0, sample_rate=16000)
M = mel_spectrogram(x, sample_rate=16000, n_mels=80)   # (frames, 80)
C = mfcc(x, sample_rate=16000, n_mfcc=13)              # (frames, 13)
```

---

## Learning track — 99 lessons, from a sine wave to Whisper

**A from-scratch, bilingual (中/英) course.** 99 lessons over ~6 months take you from
generating a single sine wave to the internals of Whisper — every algorithm **hand-written
in NumPy** (FFT · STFT · Mel · MFCC · backprop · attention · CTC · KV-Cache · RAG),
validated to `< 1e-10` against reference implementations. **No API wrappers, no black boxes.**

- **Verified twice** — every lesson passes a two-state gate (student state stops only at the
  exercise; answer state runs to `exit 0`), across two independent review rounds (Opus 4.8 + Fable 5).
- **Teaching-first** — question → analogy → story, *then* the formula; every term glossed 中文（English）.
- **You genuinely understand it** — because you've *written* it. So when you need to show that — to a teammate, in an interview, or just to yourself — the derivation is already in your hands.

**Start here:** beginners → [`GETTING_STARTED`](docs/current/course/GETTING_STARTED.md) ·
course map → [`notebooks/README.md`](notebooks/README.md) ·
knowledge graph → [`docs/current/obsidian/INDEX.md`](docs/current/obsidian/INDEX.md).

```bash
pip install -e ".[dev,notebooks]" && jupyter lab   # then open notebooks/0_foundation/L01_motivation.ipynb
```

<details>
<summary><b>🇨🇳 中文完整邀请（点开展开 · full Chinese invitation）</b></summary>

### 先问你一个问题

你写过 `import whisper`，一行 `model.transcribe()`，几秒就把语音变成了文字。
**它到底是怎么做到的？** 声音怎么变成数字？为什么要做傅里叶变换（Fourier transform）？
注意力机制（attention）凭什么"看得懂"一句话？

如果这些问题让你心里一紧——这门课就是为你写的。

### 这是什么

**Aurora 学习轨道**是一套从零开始的音频 AI 课程：**99 节课、6 个月、一条主线**——
从你亲手生成的第一条正弦波（sine wave），一路走到能听懂 99 种语言的 Whisper，
再到会检索、会对话的 RAG 系统。它只有一条铁律，写在每一页上：**拒绝黑盒（no black boxes）。**
FFT、STFT、梅尔滤波器（mel filterbank）、MFCC、CTC、多头注意力（multi-head attention）、
KV-Cache、RAG——**全部用 NumPy 手写**，再与 `numpy.fft`／参考公式逐点比对，误差压到 `< 1e-10`。

### 这趟旅程

每节课都有一个会让你想点开的名字，因为每一步都在解决一个真实的困惑：

- 🧮 **数学地基**：「每一帧声音都是一支箭」——向量、矩阵、特征值、梯度，全落到音频语境；"你的耳机每秒都在做矩阵乘法"。
- 🌊 **音频 DSP**：「一个频率一个频率地审问信号」→「把 N² 折成 N log N」，亲手重写 1965 年改变世界的 FFT，最后「搭出 Whisper 的耳朵」。
- 🧠 **深度学习**：「亲手点燃自动微分」→「让梯度逆流而上」手推反向传播 →「从一个神经元到一张网」，训出你自己的关键词识别模型。
- 🎙️ **语音识别**：「100 帧如何吐出 5 个字」（CTC）→「只动 0.5% 的参数，教会 Whisper 你的方言」（LoRA）。
- 🎵 **音乐 AI**：「教 AI 跟着音乐点头」→「一亿首歌里找知音」——从零实现节拍追踪与音乐嵌入。
- 🤖 **大模型**：「一个公式撑起大模型时代」（Transformer）→「ChatGPT 为什么越答越快」（KV-Cache）→「给 LLM 一座图书馆」（RAG）。
- 🚀 **整合收官**：「六个月的模块第一次合体」→ 亲手把它讲清楚 →「终点亦是起点」。

### 它为什么不一样

- **每一课都能跑，而且验证过两次。** 每节课都过"两态执行门"：学生态只在你该动手处停下，答案态从头到尾 `exit 0`——不是"看起来对"，是**真的能跑通**。
- **科普风讲解。** 问题先行、类比先行、故事先行，公式随后；数学不是拿来吓人的，是拿来"啊，原来如此"的。
- **中英双语术语。** 每个专业名词第一次出现都带上英文（和缩写），既读懂中文直觉，又无缝对接英文论文与技术交流。
- **真懂的底气。** 当你需要向别人——或向自己——证明你真的懂原理时（比如在白板上推导 FFT、解释 CTC），你不会慌，因为你**亲手写过**。

### 一起学吧

一个人啃 99 节硬核课容易半途而废；但如果有人和你一起在同一条正弦波上出发、在同一个蝶形图前卡住、
又在同一个"啊原来如此"的瞬间会心一笑——这条路会好走得多，也有意思得多。

> 🔰 **完全零基础？**（没装过 Python、没用过终端也没关系）先看
> [**新手上路指南**](docs/current/course/GETTING_STARTED.md)——从装 Python、开终端，
> 到跑通第一课、看懂 notebook 的 ✏️TODO / ✅检查格，手把手约 30 分钟。

```bash
pip install -e ".[dev,notebooks]" && jupyter lab
# 从第 1 课开始：notebooks/0_foundation/L01_motivation.ipynb
#   「拒绝黑盒——从一条正弦波亲手造出 Whisper 的 6 个月远征」
```

完整课程地图见 [`notebooks/README.md`](notebooks/README.md)；周计划见
[`docs/current/course/LEARNING_PLAN.md`](docs/current/course/LEARNING_PLAN.md)。
全部 99 课通过 `python scripts/validate_pipeline.py`（JSON 完整性 + Python 语法 +
音频流水线形状断言），并经 2026-07 两轮独立复审（Opus 4.8 + Fable 5）逐课两态执行验证。

> 📚 **术语与知识图谱**：[`docs/current/obsidian/INDEX.md`](docs/current/obsidian/INDEX.md)
> —— 中英双语词汇表 + 每个术语的「生命周期 / 依赖 / 易混淆 / 白板要求」概念页 +
> [面试冲刺图](docs/current/obsidian/interview/Audio-AI.md)。用 Obsidian 打开即见知识网。

带上好奇心就够了。我们白板见。 🎧

</details>

## Repository layout

```
src/aurora/              # the package, one sub-package per core
tests/                   # pytest suite (DSP validated against numpy)
notebooks/               # 99-lesson interactive course (L01–L99)
docs/current/            # active audit, standards, course materials
docs/current/audit/      # per-lesson audit + professor review
docs/current/obsidian/   # bilingual glossary + knowledge graph (concepts/lessons/interview)
docs/current/course/     # learning plan, getting-started, checklists
docs/archive/            # historical snapshots
scripts/                 # runnable demos and validation tools
.github/workflows/       # CI
```

## Development

```bash
make install                        # editable install with dev deps
make test                           # run pytest
make lint                           # ruff
make format                         # black
python scripts/validate_pipeline.py # notebook acceptance gate (JSON + syntax + pipeline)
```

## License

MIT — see [`LICENSE`](LICENSE).
