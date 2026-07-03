---
tags: [aurora, concept, deep-learning, interview]
aliases: [Autograd, 自动微分, automatic differentiation, 计算图, computation graph, computational graph, Value, grad_fn]
domain: deep-learning
whiteboard: ★★★★★
first_seen: L54
mastered: L56
---

# Autograd · 自动微分与计算图（Autograd / Computation Graph）

[[_lifecycle|← 生命周期总表]] · [[../domains/deep-learning|← Deep Learning 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：你只管写正向计算，系统在背后偷偷记下"每个数是怎么算出来的"，形成一张图；等你喊一声 `.backward()`，梯度就自动沿图回传。

---

## 📖 定义
自动微分（autograd）是**在运行前向代码时自动构建计算图、再沿图反向求出所有梯度**的机制。核心单元是一个节点对象（Aurora 的 `Value`）：它把"数值 + 生成它的算子 + 输入节点 + 局部 `_backward` 闭包"绑在一起。每写一次 `c = a + b` 就隐式建一个 `+` 节点，Python 对象图 = 计算图（DAG）。`.backward()` 触发反向传播沿图回传梯度。这就是 PyTorch/TensorFlow 的最小内核。

## 🤔 为什么工程师要发明它（Layer 9）
> 复用自 L54「为什么工程师要发明它？」：

- **不用它会怎样？** 每加一层网络，你就得手推一遍新的偏导公式；换个激活函数，全部重来——研究根本无法迭代。
- **它解决了什么真实问题？** 用一个 `Value` 对象把"数值 + 它是怎么算出来的"绑在一起，计算图在你写前向代码时就自动搭好，梯度之后能一键回传——这正是 PyTorch / TensorFlow 自动微分的最小内核。
- **后面哪里还会再用到？** L55 补算子、L56 实现 `backward()`、L57 搭 MLP、L60 换成 PyTorch autograd——全都站在这个 `Value` 类的肩膀上。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
种子         L24  链式法则（自动微分要自动化的那步）
第一次露面   L54  ★ 手写 Value 类：data + grad + 生成算子，点燃计算图心脏
拆解原理     L55  补 __pow__/relu/tanh/exp 算子 + _backward 闭包
真正掌握     L56  ★ 实现 backward()：拓扑排序沿图逆序传梯度
再次使用     L57  Neuron→Layer→MLP 全建在计算图上
对答案       L60  PyTorch grad_fn 计算图 vs 手写 Value，数值等价
再次使用     L61  nn.Module 参数注册在 autograd 之上
最终应用     L83/L84  Transformer/LoRA 训练全靠框架 autograd
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学自动微分之前你得先会
```
Autograd
 ├─ 需要 → [[Chain-Rule|链式法则]]        (L24)
 ├─ 需要 → [[Backpropagation|反向传播]]   (L56, 图上的反向算法)
 ├─ 需要 → DAG / 拓扑排序                 (L56)
 └─ 需要 → 闭包 (closure)                 (L55)
被谁依赖 → [[Training-Loop|训练循环]] → nn.Module → 所有深度学习框架
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **反向传播（backprop）** | 沿图求梯度的**算法** | autograd = 自动**建图** + 调用 backprop |
| **符号微分** | 推出导数公式 | autograd 是**数值**求值，不给你符号公式 |
| **数值微分** | 有限差分近似 | autograd 精确（到浮点），且只需一次反向 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★★（最高）** — 闭卷手写 micrograd 级引擎：
- ✅ 手写 `Value` 类：`data / grad / _prev / _backward` 四字段 + `__add__`/`__mul__`
- ✅ 说清"写前向 = 建图"，每个算子挂一段局部反向闭包
- ✅ 实现 `backward()`：拓扑排序 + 逆序调用，梯度 `+=` 累积

## 💼 面试标签（Layer 7）
`#interview` `#OpenAI` `#Meta` `#Google` `#Anthropic` `#NVIDIA` `#DL-Systems`
> "从零实现 autograd"（Karpathy micrograd）是系统/研究岗高频白板题。

## 🌍 现实系统里它在哪发挥作用
PyTorch autograd / `grad_fn` · TensorFlow · JAX `grad` · 所有深度学习训练 · 可微编程

## 📚 出现于（反查）
[[../lessons/L24]] · **[[../lessons/L54]]** · [[../lessons/L55]] · [[../lessons/L56]] · [[../lessons/L57]] · [[../lessons/L60]] · [[../lessons/L61]] · [[../lessons/L83]]
