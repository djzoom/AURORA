---
tags: [aurora, concept, audio-dsp, interview]
aliases: [aliasing, 混叠, Nyquist, 奈奎斯特, 奈奎斯特定理, Nyquist theorem, 采样定理, anti-aliasing]
domain: audio-dsp
whiteboard: ★★★★
first_seen: L33
mastered: L34
---

# Aliasing · 混叠与 Nyquist 定理（Aliasing / Nyquist）

[[_lifecycle|← 生命周期总表]] · [[../domains/audio-dsp|← Audio DSP 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：采样太稀疏时，高频会"伪装"成低频——6 kHz 的音被 8 kHz 采样后听起来像 2 kHz。

---

## 📖 定义
**Nyquist 定理**：要不失真地采样频率为 `f` 的信号，采样率必须满足 `sr > 2f`；`sr/2` 是能如实表示的最高频率（Nyquist 频率）。超过它，高频会"折叠"成一个假的低频——即**混叠（aliasing）**。折叠公式：

$$\text{alias}(f, f_s) = \left|\,f - f_s\cdot\text{round}\!\left(\tfrac{f}{f_s}\right)\right|$$

原理：超过 Nyquist 的频率与其镜像频率在每个采样点上产生完全相同的数值，离散域无法区分。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 若不懂这条极限，随手选个采样率录音，高频成分会折叠成虚假的低频，永久污染后续所有 [[Mel]] / [[MFCC]] 特征——而且无法事后修复。
- **它解决了什么真实问题？** CD 选 44100 Hz 不是巧合：人耳上限约 20 kHz，`sr > 2×20000` 才能无损。理解 Nyquist 就知道该用多高的采样率、以及录音前为什么要加**抗混叠滤波器（anti-aliasing filter）**先砍掉高频。
- **Aurora 里：** 16 kHz 管道只处理 0–8 kHz，录音前把 8 kHz 以上截断，防止折叠进 mel 谱。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L02  数字化声音时初提采样率
预习         L33  正弦波在 Nyquist 频率处只剩两点/周期
真正掌握     L34  ★ 手写 predict_alias_freq，6kHz→2kHz 折叠实证
再次使用     L45  声谱图里观察高频折叠伪影
再次使用     L51  真实音频重采样时守住 Nyquist
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学混叠之前你得先会
```
Aliasing
 ├─ 需要 → 采样率 / 正弦波              (L33)
 ├─ 需要 → 周期 / 相位                  (L04)
 └─ 关联 → 抗混叠滤波器                 (L34)
被谁依赖 → [[STFT]] / [[Mel]] / [[MFCC]] 的采样前提
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **混叠 vs 频谱泄漏** | 采样问题 vs 截断问题 | 混叠靠**提高采样率/抗混叠滤波**解决；泄漏靠[[Windowing|加窗]]解决 |
| **Nyquist 频率 vs Nyquist 率** | sr/2 vs 2f | 频率是"能表示的上限"，率是"需要的最低采样率" |
| **欠采样 undersampling** | 故意 vs 事故 | 混叠通常是事故；有意的带通欠采样是另一回事 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★** — 必须做到：
- ✅ 写出 `sr > 2f` 与折叠公式，手算 sr=8k/f=6k → 2 kHz
- ✅ 解释"为什么两个频率产生相同采样点"（镜像不可分）
- ✅ 说清 CD 44.1 kHz 的来历与抗混叠滤波器作用

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#Apple-Audio` `#ElevenLabs` `#NVIDIA` `#DSP`
> "为什么采样率要大于最高频率两倍"是信号处理入门必答题。

## 🌍 现实系统里它在哪发挥作用
所有 ADC / 录音设备的抗混叠滤波 · CD 44.1 kHz / 语音 16 kHz 的采样率选择 · 图像下采样的摩尔纹 · 重采样库。

## 📚 出现于（反查）
[[../lessons/L02]] · [[../lessons/L33]] · **[[../lessons/L34]]** · [[../lessons/L45]] · [[../lessons/L51]]
