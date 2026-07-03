---
tags: [aurora, concept, music, interview]
aliases: [Beat Tracking, 节拍追踪, onset detection, onset包络, 自相关, autocorrelation, BPM, tempo]
domain: music
whiteboard: ★★★★
first_seen: L77
mastered: L78
---

# Beat-Tracking · 节拍追踪（Beat Tracking / Onset + Autocorrelation）

[[_lifecycle|← 生命周期总表]] · [[../domains/music|← Music 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：先找出音乐里"每个音符敲下去"的时刻（onset），再用自相关看这些敲击隔多久重复一次——就能估出节拍周期和 BPM，让 AI 跟着音乐点头。

---

## 📖 定义
节拍追踪是**从音频估计节拍位置与速度（BPM）的任务**。典型流水线两步：① **onset 包络** — 用**谱通量（Spectral Flux）**衡量相邻帧频谱能量的正向增量，峰值就是音符起点；② **自相关（autocorrelation）** — 把 onset 包络与自身平移相乘求和，出现峰值的时滞（lag）就是节拍周期，换算成 `BPM = 60 / 周期(秒)`。Aurora 里 L78 用纯 NumPy + `aurora.audio.stft` 从零实现，并与 `aurora.music.beat_track` 对比验证。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 想让 AI 卡点混音、给视频配节奏、做音乐推荐，都需要知道"拍子在哪、多快"，可音频本身没有节拍标签。
- **它解决了什么真实问题？** 从原始波形自动估出 tempo / beat，是音乐信息检索（MIR）的基础能力。
- Aurora 里它把前面学的 STFT / 频谱能量真正用到音乐场景，产出节拍网格用于可视化与相似度（L82）。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L77  音乐特征工程：RMS 能量 / ZCR 铺垫
拆解原理     L78  谱通量 onset 包络 + 自相关估周期
真正掌握     L78  ★ 纯 NumPy 从零估 BPM，对比 aurora.music
再次使用     L82  节拍网格可视化、色度热力图
再次使用     L79  音乐 embedding 的节奏特征
最终应用     L81  音乐推荐（节奏相似度）
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学节拍追踪之前你得先会
```
Beat-Tracking
 ├─ 需要 → [[STFT]]                          (逐帧频谱, L44)
 ├─ 需要 → 谱通量 Spectral Flux              (帧间正向能量差)
 ├─ 需要 → [[Autocorrelation|自相关]]        (找周期峰值)
 └─ 需要 → [[Dot-Product|点积]]              (自相关的本质, L10)
被谁依赖 → 音乐 embedding · 相似度 · 推荐
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **onset vs beat** | 音符起点 vs 拍点 | onset 是每个音的起始；beat 是**规律的节拍网格**，从 onset 提取周期 |
| **自相关 vs 傅里叶** | 时域周期 vs 频域 | 自相关直接在**时滞**上找节拍周期，不必换到频域 |
| **BPM vs 采样率** | 拍/分钟 vs 样本/秒 | BPM 是音乐速度，采样率是数字化密度，量纲无关 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★** — 音乐/信号岗常见，必须做到：
- ✅ 讲清两步流水线：谱通量 onset 包络 → 自相关找周期
- ✅ 写出 `BPM = 60 / lag_seconds`（lag 由自相关峰值 × hop / sr 得到）
- ✅ 说明为什么只取谱通量的**正向差**（能量上升=起音）

## 💼 面试标签（Layer 7）
`#interview` `#Spotify` `#Apple-Music` `#ByteDance` `#MIR` `#DSP`
> 音乐信息检索（MIR）岗的入门必答，考 DSP 直觉 + 自相关。

## 🌍 现实系统里它在哪发挥作用
Spotify / Apple Music 的 tempo 标注 · DJ 软件自动对拍 · 短视频卡点混剪 · 健身 App 按 BPM 选歌 · 音乐推荐

## 📚 出现于（反查）
[[../lessons/L77]] · **[[../lessons/L78]]** · [[../lessons/L79]] · [[../lessons/L81]] · [[../lessons/L82]]
