---
tags: [aurora, concept, deep-learning, interview]
aliases: [Backpropagation, 反向传播, backprop, back-prop, BP, backward pass, backward]
domain: deep-learning
whiteboard: ★★★★★
first_seen: L54
mastered: L56
---

# Backpropagation · 反向传播（Backpropagation, BP）

[[_lifecycle|← 生命周期总表]] · [[../domains/deep-learning|← Deep Learning 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：把梯度想成从输出口往回灌的水——每个节点收到上游水量，乘上自己这段管子的本地斜率，再往下游分；一趟走完，每个参数的梯度就都填好了。

---

## 📖 定义
反向传播是**在计算图上高效计算"损失对每个参数的偏导"的算法**。它把计算图按**逆拓扑序**遍历：从输出 `L.grad = 1` 出发（dL/dL=1），每个节点用链式法则把梯度分发给它的输入（`上游流量 × 本地导数`），沿有向无环图（DAG）从后往前一层层传递。代价与一次前向相当，复用了前向已算好的中间值。

## 🤔 为什么工程师要发明它（Layer 9）
> 复用自 L56「为什么工程师要发明它？」：

- **不用它会怎样？** 一个百万参数的网络，你得为每个参数手写一条偏导公式再逐点求值——写不完，也调不动。
- **它解决了什么真实问题？** 反向传播把"求所有参数的梯度"变成**一次图遍历**：复用前向已算好的中间值，一趟 `for` 循环就把 `dL/d参数` 全部填好，代价和一次前向差不多。
- **后面哪里还会再用到？** L57 MLP 整网反向、L58 训练循环的 `w -= lr·w.grad`、L60 PyTorch 的 `.backward()`——全是这套机制的放大版。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
种子         L24  链式法则：反向传播的数学内核
第一次露面   L54  Value 类记录算子，为反向铺地基
拆解原理     L55  每个算子封装一段 _backward 闭包（局部导数）
真正掌握     L56  ★ 手写 Value.backward()：拓扑排序 × 链式法则，逆序传梯度
再次使用     L57  MLP 整网一键反向
真正应用     L58  训练循环 forward→loss→backward→update→zero_grad
对答案       L60  与 PyTorch autograd 数值比对，确认等价
最终应用     L83/L84  Transformer / LoRA 训练靠它回传梯度
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学反向传播之前你得先会
```
Backpropagation
 ├─ 需要 → [[Chain-Rule|链式法则]]        (L24, 数学内核)
 ├─ 需要 → [[Gradient|梯度]]              (L23)
 ├─ 需要 → 拓扑排序 / DAG                 (L56)
 └─ 需要 → [[Autograd|计算图]]            (L54)
被谁依赖 → [[Gradient-Descent|梯度下降]] → [[Training-Loop|训练循环]] → 所有神经网络
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **梯度下降（GD）** | 拿梯度**更新**参数 | backprop 只负责**算**梯度，GD 才更新 |
| **链式法则** | 数学规则 | backprop = 链式法则 + 计算图 + 逆拓扑序 |
| **"神秘学习算法"** | ❌ | backprop 不含学习、无魔法；学习发生在后续 GD |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★★（最高）** — 深度学习白板第一题，闭卷必推：
- ✅ 讲清"逆拓扑序 + `L.grad=1` 起点 + 逐节点 `_backward()`"三步
- ✅ 手推 `L = a*b + c` 的反向，解释为何梯度要 `+=` 累积（节点复用）
- ✅ 用水管比喻讲"上游流量 × 本地导数 → 下游"，并连回链式法则

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#Meta` `#OpenAI` `#DeepMind` `#NVIDIA` `#Anthropic` `#DL-Core`
> 每年被问烂但仍必考——从零推导 + 讲清"只是链式法则"。

## 🌍 现实系统里它在哪发挥作用
PyTorch/TensorFlow/JAX 的 autograd · 所有神经网络训练 · LLM 预训练与微调 · Whisper/LoRA · 可微渲染

## 📚 出现于（反查）
[[../lessons/L24]] · [[../lessons/L54]] · [[../lessons/L55]] · **[[../lessons/L56]]** · [[../lessons/L57]] · [[../lessons/L58]] · [[../lessons/L60]] · [[../lessons/L83]]
