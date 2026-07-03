---
tags: [aurora, concept, calculus, interview]
aliases: [Chain Rule, 链式法则, 链式求导, chain-rule, 复合函数求导]
domain: calculus
whiteboard: ★★★★★
first_seen: L24
mastered: L24
---

# Chain Rule · 链式法则（Chain Rule）

[[_lifecycle|← 生命周期总表]] · [[../domains/calculus|← Calculus 领域]] · [[../INDEX|← Master Index]]

> **⚡ 一句话（Layer 8）**：函数套函数的求导规则——每穿过一层，就乘上那一层的斜率；一条乘法链，就是整个深度学习能训练的秘密。

---

## 📖 定义
链式法则给出**复合函数** `y = f(g(x))` 的导数：`dy/dx = f'(g(x)) · g'(x)`。直觉：内层把 x 的扰动放大 `g'(x)` 倍，外层再放大 `f'(g)` 倍，两个放大倍数**相乘**就是总放大倍数。多层复合时逐层连乘，`n` 层就有 `n` 项相乘。

## 🤔 为什么工程师要发明它（Layer 9）
> 复用自 L24「本课剧情」：

- **不用它会怎样？** 神经网络有几十层。当你调整输入一点点，最终损失会变多少？没有链式法则，你无从下手。
- **它解决了什么真实问题？** 把"输出对输入的总导数"拆成**每层局部斜率的连乘**——从最后一层的误差出发，逐层向前传递导数乘积，直到每个参数的梯度都算出。
- 反向传播（backpropagation）就是链式法则在计算图上的批量执行。它是 backprop 的**种子**。

## ⏳ 生命周期（Layer 2 / 10）——今天难，是因为以后还会出现很多次
```
第一次露面   L23  梯度里已隐含"逐层"思想
正式动机     L24  复合函数 f(g(x)) 该怎么求导
真正掌握     L24  ★ 手写 composite_derivative，y=sin(x²) 数值验证 < 1e-9
再次使用     L54  Value.backward() 把两步乘法自动化
再次使用     L55  每个算子封装一段 _backward 闭包（局部导数）
真正应用     L56  ★ 反向传播 = 链式法则沿计算图逆拓扑序展开
再次使用     L57  MLP 整网每条边连乘局部梯度
最终应用     L61  PyTorch autograd 底层就是这条乘法链
```
👉 见自动生成的完整时间线：[[_lifecycle]]

## 🔗 依赖关系（Layer 3）——学链式法则之前你得先会
```
Chain Rule
 ├─ 需要 → [[Derivative|导数]]        (L22)
 └─ 需要 → [[Gradient|梯度]]          (L23)
被谁依赖 → [[Backpropagation|反向传播]] → [[Autograd|自动微分]] → 所有深度网络
```

## ⚠️ 容易混淆（Layer 4）
| 别搞混 | 它是什么 | 一句话区分 |
|---|---|---|
| **乘法法则（product rule）** | `(uv)' = u'v+uv'` | 链式针对**函数套函数**，不是相乘 |
| **反向传播（backprop）** | 链式法则的**算法实现** | backprop = 链式法则 + 计算图 + 逆拓扑序 |
| **链式 vs "新求导法"** | ❌ | 它只是把复合函数**拆层连乘**，没有新数学 |

## 🧑‍🏫 白板要求（Layer 6）
**★★★★★（最高）** — 反向传播的根，几乎必问：
- ✅ 闭卷写出 `dy/dx = f'(g(x))·g'(x)` 并推广到 n 层连乘
- ✅ 手算 `y=sin(x²)` → `cos(x²)·2x`
- ✅ 讲清"局部斜率连乘 = 总斜率"，并连到 backprop

## 💼 面试标签（Layer 7）
`#interview` `#Google` `#Meta` `#OpenAI` `#NVIDIA` `#DeepMind` `#ML-Fundamentals`
> "推导一下反向传播" = "用链式法则沿计算图展开"，白板高频。

## 🌍 现实系统里它在哪发挥作用
每个深度学习框架的 autograd（PyTorch/TensorFlow/JAX）· 所有神经网络训练 · 物理引擎的可微仿真 · 任何 `loss.backward()`

## 📚 出现于（反查）
[[../lessons/L23]] · **[[../lessons/L24]]** · [[../lessons/L54]] · [[../lessons/L55]] · [[../lessons/L56]] · [[../lessons/L57]] · [[../lessons/L61]]
