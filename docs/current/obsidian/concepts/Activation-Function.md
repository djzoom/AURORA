---
tags: [aurora, concept, deep-learning, interview]
aliases: [Activation Function, 激活函数, activation, 非线性, nonlinearity, ReLU, tanh, sigmoid, GELU]
domain: deep-learning
whiteboard: ★★★★
first_seen: L55
mastered: L55
---

# Activation Function · 激活函数（Activation Function）

[[_lifecycle|← 生命周期总表]] · [[../domains/deep-learning|← Deep Learning 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：在每层线性变换后加一个"弯一下"的非线性函数——没有它，叠再多层也只等于一层直线，网络学不会复杂形状。

---

## 📖 定义
激活函数是**加在线性层（`w·x+b`）之后的非线性函数**，给网络引入"弯曲"能力。常见几种及其导数（反向传播要用）：

| 激活 | 前向 | 导数 |
|---|---|---|
| `ReLU(x)` | `max(0,x)` | `1 if x>0 else 0`（次梯度）|
| `tanh(x)` | `(e²ˣ−1)/(e²ˣ+1)` | `1 − tanh²(x)`（用前向输出直接算）|
| `sigmoid(x)` | `1/(1+e⁻ˣ)` | `σ(x)(1−σ(x))` |
| `GELU(x)` | `x·Φ(x)` | 平滑近似 ReLU（Transformer 常用）|

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 若只堆线性层，`W₂(W₁x) = (W₂W₁)x` 还是线性——叠一百层等于一层直线，连"异或"这种弯曲边界都学不出来。
- **它解决了什么真实问题？** 在每层后插一个非线性"关节"，网络才能逼近任意复杂函数（万能逼近）；同时它得**可导**，梯度才能反传（tanh 的导数还能用前向输出直接算，省一次计算）。
- ReLU 因为导数简单（0 或 1）、不饱和、训练快，成了现代默认选择。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L54  tanh 出现在示例损失 L=tanh(a*b+b²)
真正掌握     L55  ★ 手写 relu/tanh/exp 算子 + 各自 _backward 导数
再次使用     L57  MLP 每层 Linear→激活→Linear，非线性堆叠
再次使用     L61  PyTorch nn.ReLU 复现 L57 结构
再次使用     L63  KWS 模型卷积层后接激活
再次使用     L64/L65  训练/可视化里观察激活影响
最终应用     L83  Transformer FFN 用 GELU/ReLU
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学激活函数之前你得先会
```
Activation Function
 ├─ 需要 → [[Derivative|导数]]            (L22, 要能求各自导数)
 ├─ 需要 → 线性层 w·x+b                   (L21/L57)
 └─ 需要 → [[Chain-Rule|链式法则]]        (L24, 反传要用导数)
被谁依赖 → [[Backpropagation|反向传播]] (需要激活导数) → MLP → Transformer FFN
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **Softmax** | 输出层归一化 | 激活是**逐元素**弯曲；softmax 是**整排**归一化 |
| **激活 vs 线性层** | 线性做变换 | 没有激活，多层线性 = 单层线性，白叠 |
| **ReLU vs sigmoid** | 都是激活 | ReLU 不饱和、梯度不消失，深网默认；sigmoid 易梯度消失 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★** — 必问导数与"为何需要非线性"：
- ✅ 默写 ReLU / tanh / sigmoid 的前向与导数（尤其 `tanh'=1−tanh²`、`σ'=σ(1−σ)`）
- ✅ 一句话论证"无非线性 → 多层塌缩成单层"
- ✅ 说清 ReLU 为何成默认（不饱和、计算省、缓解梯度消失）

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#Meta` `#OpenAI` `#NVIDIA` `#ElevenLabs` `#DL-Core`
> "为什么需要激活函数""ReLU 和 sigmoid 区别" 是基础必考。

## 🌍 现实系统里它在哪发挥作用
所有神经网络的隐藏层 · Transformer FFN（GELU）· CNN（ReLU）· KWS/ASR/LLM 各层之间

## 📚 出现于（反查）
[[../lessons/L54]] · **[[../lessons/L55]]** · [[../lessons/L57]] · [[../lessons/L61]] · [[../lessons/L63]] · [[../lessons/L64]] · [[../lessons/L65]] · [[../lessons/L83]]
