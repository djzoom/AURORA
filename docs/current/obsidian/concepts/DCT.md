---
tags: [aurora, concept, audio-dsp, interview]
aliases: [DCT, DCT-II, 离散余弦变换, Discrete Cosine Transform, 去相关]
domain: audio-dsp
whiteboard: ★★★★★
first_seen: L49
mastered: L49
---

# DCT · 离散余弦变换（Discrete Cosine Transform, DCT-II）

[[_lifecycle|← 生命周期总表]] · [[../domains/audio-dsp|← Audio DSP 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：用一组固定的余弦波把一堆"你说了两遍"的相关数字重新洗牌，把有用信息挤到前几个、后面几乎归零——像不用训练的 PCA。

---

## 📖 定义
DCT-II 把长度 N 的实数序列 `x[n]` 投影到一组余弦基上，输出实数系数：

$$X[k] = \sum_{n=0}^{N-1} x[n]\cos\!\left[\frac{\pi}{N}\left(n+\tfrac12\right)k\right]$$

它是 [[DFT]] 的"纯实数余弦"表亲：只用余弦（无虚部），且用固定基向量集中能量、去除相关性（decorrelation），前几维就装下了大部分信息。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 直接用 40 维 log-Mel，相邻维度相关系数高达 0.9+，等于反复告诉模型同一件事，浪费容量、拖慢优化；GMM / 欧氏距离这类"假设特征独立"的模型甚至会失效。
- **它解决了什么真实问题？** 用一组**固定的**余弦基，把相关信息旋转、集中到前几维（像不用训练的 PCA），后面维度接近 0，可以安全截断 → 既降维又去噪。
- **后面哪里还会再用到？** L50 MFCC 流水线的最后一步就是它；截到前 13 维即经典的 MFCC-13。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L46  Mel 讲完后预告：相邻 Mel 高度相关，需要去相关
正式动机     L49  40 维 log-Mel 塞满重复信息，直接喂模型是添乱
真正掌握     L49  ★ 手写 dct_ii()，验证去相关与能量集中
再次使用     L50  MFCC 最后一步，截前 13 维得 MFCC-13
再次使用     L53  MFCC 可视化，观察高阶系数近零
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学 DCT 之前你得先会
```
DCT
 ├─ 需要 → 余弦 / [[Euler formula|欧拉公式]]   (L06)
 ├─ 需要 → [[Dot Product|点积]] / 正交基        (L10)
 └─ 需要 → [[Mel]] log 谱作为输入               (L47)
被谁依赖 → [[MFCC]]（第五步）
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **[[DFT]]** | 复指数变换 | DFT 用 e^{-iθ}（含虚部）；DCT 只用余弦、输出实数 |
| **PCA** | 数据驱动的去相关 | DCT 用**固定**余弦基、无需训练；PCA 要看数据学基 |
| **[[FFT]]** | 快速算法 | FFT 加速的是 DFT；DCT 是另一种变换（可借 FFT 实现） |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★★（最高，L49 闭卷推导课）** — 必须做到：
- ✅ 闭卷写出 DCT-II 求和公式
- ✅ 讲清"去相关 + 能量集中 = 不用训练的 PCA"这层动机
- ✅ 手写 `dct_ii()`，解释为什么截断前几维安全

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#Meta` `#Apple-Audio` `#NVIDIA` `#DSP` `#ASR`
> 常与 JPEG / MFCC 一起被问："DCT 为什么能压缩/去相关？"

## 🌍 现实系统里它在哪发挥作用
MFCC 语音特征 · JPEG / MPEG 图像视频压缩 · 音频编解码器（AAC/MP3）· 任何"能量集中到低频系数"的降维场景。

## 📚 出现于（反查）
[[../lessons/L46]] · **[[../lessons/L49]]** · [[../lessons/L50]] · [[../lessons/L53]]
