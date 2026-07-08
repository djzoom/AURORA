让我认真跟着这份课程逐个cell学习。我先完整阅读了notebook，现在作为"老陈"的角色来总结学习过程。

---

# 老陈 — L61 学习日志

## 我理解了什么

1. **nn.Module 把参数"登记"到一个管理系统**：用`nn.Parameter()`或`register_buffer()`注册的张量，会被纳入 Model 的"户口"，这样`parameters()`、`state_dict()`、`.to('cuda')`这些操作才能找到它们。散落在外面的普通张量则无人管理。

2. **nn.Sequential 省掉手工链式调用**：不用自己在`forward()`里写`x=layer1(x); x=layer2(x); ...`，直接用Sequential把各层堆成列表，他们会按顺序执行。

3. **参数数量能手算：AudioMLP(40, 64, 10) 共3274个参数**（40×64+64 + 64×10+10），与高中学过的矩阵维数规则一致。

---

## 遇到的困难和问题

### 【理解】register_buffer() 为什么要存在，什么时候用？

课程说："不需要梯度，但要跟着模型一起搬设备（.to()），还要出现在state_dict()里"。给的例子是 BatchNorm 的 running_mean。

**卡在这里**：我不知道什么叫"BatchNorm的running_mean"。之前课程没讲过BatchNorm，也没说running_mean是什么。我能读懂`register_buffer()`这段代码，但**不理解实际应用场景**。为什么有些数据无梯度但又要跟着模型移动？初学者需要一个更简单、更具体的例子（比如"模型内部的计数器"之类的）。

**希望补充**：用初学者能理解的东西举例register_buffer()，不要假设知道什么是BatchNorm。

---

### 【理解】"子模块"（submodule）这个概念没有铺垫

Cell 8 说 `named_parameters()` "递归遍历所有**子模块**，返回所有参数"。

**卡在这里**：什么叫"子模块"？我看代码里`self.fc = nn.Linear(4, 2)`，Linear是不是一个子模块？那`self.scale = nn.Parameter(...)`是不是也算一个"子模块"？"递归遍历"的意思是说，如果一个Module里套着另一个Module，参数会一层层往外找出来吗？

**希望补充**：画个示意图或举例，说明什么时候构成"子模块嵌套"的结构。

---

### 【理解】Sequential 为什么"适用于无分支、无跳连"

课程明确说了这个限制："适用条件：层之间**无分支、无跳连（skip connection）**"。

**卡在这里**："分支"是什么意思？"跳连"是什么意思？这两个词从没在前面课程出现过。我能猜测可能是说数据流的形状问题，但没学过，无法推断。

**希望补充**：解释这两个概念，最好用一个小例子说明什么情况下会有"分支"或"跳连"，以及此时为什么不能用Sequential。

---

### 【推演】为什么一定要调用 `super().__init__()`？

Cell 12 的模板写了 `super().__init__()` 在第一行。

**卡在这里**：高中没学过这个，Python课程也没强调过。`super()` 是什么意思？为什么必须调用？如果我在 `__init__` 里忘了写这一行，会发生什么？

**希望补充**：简短地解释：`super().__init__()` 的作用是"初始化父类（nn.Module）的内部结构，这样nn.Module才能帮你管理参数"，后果是"如果不写，参数管理功能全部失效"。

---

### 【推演】Linear 的 weight 为什么是 `(out_features, in_features)` 而不是反过来？

Cell 15 手算参数时写："`layers.0 (Linear 40→64): weight=40×64=2560`"。这说明weight形状是 (64, 40)。

**卡在这里**：为什么是输出维度×输入维度，而不是输入×输出？高中学过矩阵乘法 $A_{m \times n} \cdot B_{n \times p} = C_{m \times p}$，那如果输入是 (batch=8, in=40)，前向时做 `x @ weight`，是 (8, 40) @ weight = (8, 64)，那weight应该是 (40, 64) 啊？

**希望补充**：清楚地说明：PyTorch里Linear层用的公式是什么？`y = x @ W^T + b` 还是 `y = x @ W + b`？然后推导为什么weight的存储形状是(out, in)。不要说"显然"或"容易看出"。

---

### 【实践】为什么实现AudioMLP时不能把三个操作直接写在forward里？

Cell 12 给的方案是把`nn.Linear`、`nn.ReLU`都放进`self.layers = nn.Sequential(...)`，然后forward直接调用`self.layers(x)`。

**我想问**：我能不能这样写——

```python
def __init__(self):
    super().__init__()
    self.l1 = nn.Linear(40, 64)
    self.l2 = nn.Linear(64, 10)

def forward(self, x):
    x = self.l1(x)
    x = torch.nn.functional.relu(x)
    x = self.l2(x)
    return x
```

这样有什么问题吗？或者一定要用Sequential？课程的优势只是"代码短"吗？

**希望补充**：明确说明两种写法的等价性，以及选择Sequential的原因（是代码简洁，还是有功能差异？）。

---
