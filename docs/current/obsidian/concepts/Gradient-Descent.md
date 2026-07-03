---
tags: [aurora, concept, calculus, interview]
aliases: [Gradient Descent, 梯度下降, gradient-descent, GD, SGD, 权重更新, 优化器]
domain: calculus
whiteboard: ★★★★
first_seen: L25
mastered: L25
---

# Gradient Descent · 梯度下降（Gradient Descent, GD）

[[_lifecycle|← 生命周期总表]] · [[../domains/calculus|← Calculus 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：蒙上眼睛下山——每一步都朝当前最陡的下坡方向（负梯度）挪一小步，反复几十次，就走到谷底（损失最小）。

---

## 📖 定义
梯度下降是最小化函数的迭代算法：`x ← x − lr · ∇f(x)`。`∇f(x)` 是当前坡度（梯度），指向上坡；取负号沿**下坡**走；`lr`（学习率）控制步长。梯度接近 0 时停下（谷底或鞍点）。这一行更新规则就是所有神经网络"学习"的动作。

## 🤔 为什么工程师要发明它（Layer 9）
> 复用自 L25「本课剧情」：

- **不用它会怎样？** 参数空间上百万维，没法暴力枚举所有权重组合去找损失最小点。
- **它解决了什么真实问题？** 只用局部坡度（梯度）就能一步步逼近极小值，不需要看全局——`optimizer.step()` 执行的正是这一行。
- 三个核心问题：为什么取**负**梯度（梯度指上坡）？lr 太大会**震荡/发散**；何时停（∇f≈0）。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L23  梯度指出方向，但还没"走"
正式动机     L25  要让损失变小，朝 −∇f 走一小步
真正掌握     L25  ★ 手写 gd_step，f=(x−3)² 从 0 收敛到 3（50 步）
再次使用     L56  反向传播算好梯度，交给它更新
真正应用     L58  训练循环第 4 步 w -= lr·w.grad，拟合双月牙
再次使用     L61  PyTorch optimizer.step() 同一行放大版
最终应用     L72/L84  Whisper 微调、LoRA 训练大模型
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学梯度下降之前你得先会
```
Gradient Descent
 ├─ 需要 → [[Gradient|梯度]]              (L23)
 ├─ 需要 → [[Chain-Rule|链式法则]]        (L24, 用来算梯度)
 └─ 需要 → learning rate 学习率           (L25)
被谁依赖 → [[Training-Loop|训练循环]] → 所有模型训练 · 优化器 (Adam/SGD)
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **反向传播（backprop）** | **算**梯度的过程 | GD 是拿到梯度后**用**它更新参数 |
| **学习率（lr）** | GD 的超参数 | lr 太大震荡、太小龟速；GD 是更新规则本身 |
| **SGD vs GD** | 用小批数据估计梯度 | SGD = 每步只用一个 batch 的 GD |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★** — 训练核心，必须做到：
- ✅ 闭卷写出 `x ← x − lr·∇f(x)`，解释为什么是负号
- ✅ 手算 f=(x−3)² 前两步（x₀=0, lr=0.1 → 0.6 → 1.08）
- ✅ 说清 lr 的收敛/震荡边界（本例 |1−2·lr|<1）

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#Meta` `#OpenAI` `#NVIDIA` `#ML-Fundamentals` `#Optimization`
> "如何训练一个神经网络" 的第一句答案。

## 🌍 现实系统里它在哪发挥作用
所有深度学习训练（SGD/Adam/AdamW）· LLM 预训练 · Whisper/LoRA 微调 · 逻辑回归 · 推荐系统

## 📚 出现于（反查）
[[../lessons/L23]] · **[[../lessons/L25]]** · [[../lessons/L56]] · [[../lessons/L58]] · [[../lessons/L61]] · [[../lessons/L72]] · [[../lessons/L84]]
