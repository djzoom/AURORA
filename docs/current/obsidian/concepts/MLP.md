---
tags: [aurora, concept, deep-learning, interview]
aliases: [MLP, 多层感知机, Multi-Layer Perceptron, 全连接网络, 前馈网络]
domain: deep-learning
whiteboard: ★★★★
first_seen: L54
mastered: L57
---

# MLP · 多层感知机（Multi-Layer Perceptron）

[[_lifecycle|← 生命周期总表]] · [[../domains/deep-learning|← Deep Learning 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：把一堆"加权求和 + 非线性"的神经元一层层叠起来，就能拟合任意复杂的函数——这就是最基础的神经网络。

---

## 📖 定义
多层感知机是**由全连接层堆叠而成的前馈网络**。每个神经元先做一次线性变换 `z = w·x + b`，再套一个非线性激活（relu / tanh）；把多个神经元并成一层，再把多层串起来，中间夹激活函数。因为有非线性，它能表达线性模型学不到的曲面（万能逼近定理）。前向算 `y = f(W₂·f(W₁·x))`，反向靠 [[Backpropagation|反向传播]] 求每个 `w, b` 的梯度。

## 🤔 为什么工程师要发明它（Layer 9）
- **不用它会怎样？** 单个线性层（`w·x + b`）只能画直线/平面，连"双月牙"这种弯曲边界都分不开。
- **它解决了什么真实问题？** 叠加"线性 + 非线性"后，网络能拟合任意连续函数——这是所有深度学习模型（CNN / Transformer）的原型骨架。
- Aurora 里它是第一个能真正"学会"的模型：L58 亲眼看到 loss 下降、拟合出双月牙分类边界。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L54  Value 类点燃 autograd，神经元的"零件"
正式动机     L55  前向传播：单个 Neuron 的 relu/tanh 算子
拆解原理     L56  反向传播：拓扑排序 × 链式法则求梯度
真正掌握     L57  ★ 手写 Neuron→Layer→MLP，数清 13 个参数
再次使用     L58  训练循环拟合双月牙
再次使用     L61  nn.Module / Sequential 重写同一个 MLP
再次使用     L63  KWS CNN 的分类头就是一个 MLP
最终应用     L83  Transformer 里的 FFN（逐位置 MLP）
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学 MLP 之前你得先会
```
MLP
 ├─ 需要 → [[Dot-Product|点积]]              (L10, 神经元线性部分)
 ├─ 需要 → [[Activation|激活函数]]           (L55, relu/tanh)
 ├─ 需要 → [[Backpropagation|反向传播]]      (L56, 求梯度)
 └─ 需要 → [[Gradient-Descent|梯度下降]]     (L25/L58, 更新参数)
被谁依赖 → [[CNN]] · [[Transformer]] · [[Whisper]]（都以 MLP 为子模块）
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **单个感知机** | 一层线性 + 阶跃 | MLP = **多层**，且激活可导才能反传 |
| **CNN** | 带卷积/权重共享 | MLP 每个输入独立连边；[[CNN]] **共享卷积核**、利用局部性 |
| **线性回归** | 无隐藏层 | 去掉非线性激活，MLP 就退化成线性模型 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★** — 面试高频，必须做到：
- ✅ 闭卷手写 `Neuron.forward` / `Layer` / `MLP` 的结构
- ✅ 数清参数量：`MLP(2,[3,1])` = 3×(2+1)+1×(3+1) = 13
- ✅ 讲清"为什么要非线性激活"（否则多层塌缩成一层）

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#Meta` `#OpenAI` `#NVIDIA` `#DeepLearning`
> 深度学习岗的"Hello World"，常与反向传播一起考。

## 🌍 现实系统里它在哪发挥作用
Transformer 的 FFN 层 · 各类分类/回归头 · 推荐系统的 embedding MLP · Whisper/GPT 每个 block 里都藏着它

## 📚 出现于（反查）
[[../lessons/L54]] · [[../lessons/L55]] · [[../lessons/L56]] · **[[../lessons/L57]]** · [[../lessons/L58]] · [[../lessons/L61]] · [[../lessons/L63]] · [[../lessons/L83]]
