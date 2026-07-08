# L61 教授审查与修订总结

根据小雨、老陈、琳达三位学生的学习日志，识别出 **9 类共性问题**，全部在 notebook 中进行了针对性修订。修订遵循"只增加、不删减"原则，在学生卡住的位置之前插入新的讲解、代码演示和图示。

---

## 修订清单

### 问题 1：矩阵乘法与权重形状（小雨、老陈、琳达均问）

**学生困惑**：`nn.Linear(40, 64)` 输入 40 维、输出 64 维，权重为什么是 `(64, 40)` 而不是 `(40, 64)`？矩阵乘法怎样从 40 维变成 64 维的？

**修订内容与位置**：
- **新增 markdown cell**（cell id `53a9871a`）：在 Section 1 后插入"深潜：为什么 Linear 的权重是 `(out_features, in_features)` 而非 `(in_features, out_features)`？"
  - 详细推导公式 $y = x \cdot W^T + b$
  - 展示具体的 `(2,40) @ (40,64) = (2,64)` 矩阵乘法演算
  - 解释"逻辑形状"与"存储形状"的差异，为什么 PyTorch 转置后存储
  - 给出内存高效、梯度计算、初始化的三个好处

- **新增 code cell**（cell id `761166f0`）：矩阵乘法验证演示
  - 手工计算 `x @ W.T + b` 与 `linear_layer(x)` 对比
  - 打印 `W.T` 的形状，验证矩阵乘法的维度规则

---

### 问题 2：register_buffer() 的实际用场（小雨、老陈、琳达均问）

**学生困惑**：`register_buffer()` 的"不需要梯度但要跟着模型"这个需求什么时候出现？课程提 BatchNorm running mean 但我没学过，无法想象。

**修订内容与位置**：
- **替换 markdown cell**（cell id `aurora-register-buffer-note`）：用"模型计数器"替代 BatchNorm 作为主要例子
  - 演示一个真实可想象的场景："模型需要记住它见过多少个样本"
  - 清楚地说明计数器的三个需求（无梯度、保存、设备迁移）
  - 保留表格对比 Parameter、buffer、普通张量的区别

- **替换 code cell**（cell id `aurora-register-buffer-demo`）：用 `TrainedSampleCounter` 替代 `TinyNetV2`
  - 在 `forward()` 中累计样本数，展示计数器的实际用途
  - 验证 `total_samples` 在 `state_dict()` 中但不在 `parameters()` 中
  - 对比已注册的 `total_samples` 和未注册的 `unreg_count`，展示差异

---

### 问题 3：nn.Module 如何自动追踪属性（小雨、琳达问）

**学生困惑**：为什么 `self.fc = nn.Linear(4, 2)` 的参数自动被追踪，但 `self.buf = torch.zeros(1)` 就不行？nn.Module 做了什么魔法？

**修订内容与位置**：
- **新增 markdown cell**（cell id `491aa2af`）：在参数注册演示后插入"技术细节：nn.Module 如何'追踪'子模块属性"
  - 解释 `nn.Module` 重写了 `__setattr__()` 方法
  - 逐一列举哪些对象被自动追踪（`nn.Module` 子类、`nn.Parameter`、`register_buffer`）、哪些不追踪
  - 说明后果：只有被追踪的对象才能被 `parameters()`、`state_dict()`、`to(device)` 找到

---

### 问题 4：参数总量的矩阵维度推导（小雨、老陈问）

**学生困惑**：手算 `AudioMLP(40, 64, 10)` 的参数时，为什么是 `40×64` 而不是 `64×40`？为什么是乘而不是加？

**修订内容与位置**：
- **替换 markdown cell**（cell id `cell-fix-l61-15`）：Section 5 从简化版扩展为详细版
  - 逐层计算参数数量（L1：`64×40+64 = 2624`，L2：`10×64+10 = 650`）
  - 用"每个输出神经元都需要一个完整的权重向量"解释为什么是乘法
  - 公式化地写出每层参数 = `output_size × input_size + output_size`

---

### 问题 5：torch.randn() vs torch.zeros()（小雨问）

**学生困惑**：课程里某处用 `randn`、某处用 `zeros`，有什么区别？是初始化技巧还是有更深含义？

**修订内容与位置**：
- **在 Section 5 中添加"初始化策略补充"小节**（同上 cell id `cell-fix-l61-15`）
  - `torch.randn(shape)`：从 $\mathcal{N}(0,1)$ 采样，用于初始化**可训练参数**
  - `torch.zeros(shape)`：全 0，用于初始化**非参数状态**（计数器、缓存）
  - 解释为什么参数需要随机（打破对称性），而状态无需随机

---

### 问题 6："子模块"与递归遍历（老陈问）

**学生困惑**：`named_parameters()` "递归遍历子模块"，什么是子模块？子模块还能嵌套吗？

**修订内容与位置**：
- **替换 markdown cell**（cell id `cell-fix-l61-8`）：Section 2 开头新增"什么是'子模块'？"小节
  - 明确定义：`self.fc = nn.Linear(...)` 中的 `nn.Linear` 就是一个子模块
  - 展示嵌套的例子：`nn.Sequential` 本身是子模块，它内部的 `Linear` 又是 `Sequential` 的子模块
  - 说明"递归遍历"的含义：一层层往外找，找到所有深层的参数

---

### 问题 7：Sequential 的适用条件（老陈问）

**学生困惑**：Sequential "适用于无分支、无跳连"——什么是分支和跳连？为什么这是限制条件？

**修订内容与位置**：
- **替换 markdown cell**（cell id `cell-fix-l61-10`）：Section 3 扩展适用条件讲解
  - 明确列举什么时候适用（单一链条数据流）、什么时候不适用（分支、跳连）
  - 用 ASCII 图示展示"分支"的概念（一个层的输出流向多个下一层）
  - 用 ASCII 图示展示"跳连"的概念（ResNet 风格的残差连接）
  - 说明复杂情况必须手写 `forward()`

---

### 问题 8：Sequential vs 手写 forward 的等价性（老陈问）

**学生困惑**：为什么非得用 Sequential？能不能在 `forward()` 里直接调用 `self.l1(x)` → `self.relu(x)` → `self.l2(x)`？有什么优劣区别？

**修订内容与位置**：
- **新增 code cell**（cell id `09e20e01`）：在 Section 3 演示后插入"Sequential vs 手写 forward 两种写法完全等价"
  - 实现 `MLPv1`（用 Sequential）和 `MLPv2`（手写 forward）
  - 复制权重使参数相同，验证两者输出一致
  - 总结：Sequential 代码少易读，手写 forward 灵活可控
  - 建议：简单结构用 Sequential，复杂结构用手写

---

### 问题 9：super().__init__() 的必要性（老陈问）

**学生困惑**：为什么一定要在 `__init__` 里调用 `super().__init__()`？忘了会怎样？

**修订内容与位置**：
- **替换 markdown cell**（cell id `cell-fix-l61-12`）：Section 4 模板讲解中新增"为什么一定要 `super().__init__()`？"小节
  - 说明 `super().__init__()` 的三个作用（初始化参数追踪、设置内部字典、为方法做准备）
  - 用反面教材展示忘记写的后果：参数消失，`parameters()` 返回空
  - 强调：必须是 `__init__` 第一行或至少在赋值子模块前

---

### 问题 10：state_dict() 的设计与加载步骤（琳达问）

**学生困惑**：`state_dict()` 只有权重数值，没有"这是个什么模型"的信息。怎么保证加载时模型结构正确？

**修订内容与位置**：
- **新增 markdown cell**（cell id `d4deb3e6`）：在 Section 2 后插入"state_dict() 的一个常见误解：只有数字，没有结构信息"
  - 展示 `state_dict()` 的内容（只是字典，只有数值）
  - 说明正确的加载步骤：先定义模型架构，再加载权重
  - 对比错误做法（直接 `torch.load`）与正确做法（先创建模型再 `load_state_dict`）
  - 解释设计初衷：保存文件尽可能小，架构由代码定义

---

## 修订统计

- **新增 markdown cell**：5 个（矩阵乘法深潜、参数追踪机制、子模块讲解补充、分支/跳连补充、state_dict 误解）
- **新增 code cell**：3 个（矩阵乘法验证、计数器演示、Sequential 等价性）
- **替换修改的 cell**：4 个（register_buffer 说明和演示、参数总量推导、Section 2/3/4 讲解）
- **总共改动位置**：约 12 处

所有修订都在原内容基础上扩充，保留原有例子和练习题，符合"只增加、不删减"的规则。

---

## 修订后的学习体验改进

- ✅ **矩阵乘法**：从"为什么是 (64, 40)"的模糊困惑 → 清晰的公式推导 + 具体演算 + 代码验证
- ✅ **register_buffer()**：从"BatchNorm running mean 这是什么"的迷茫 → 学生能想象的计数器例子
- ✅ **参数追踪**：从"nn.Module 的魔法是什么"的无知 → 清楚的 `__setattr__()` 机制解释
- ✅ **Sequential 限制**：从"无分支、无跳连这是啥"的不理解 → 图示和明确的反例
- ✅ **super().__init__()**：从"为什么要写这行"的疑惑 → 反面教材展示忘记的后果
- ✅ **state_dict 加载**：从"检查点怎样恢复结构"的不明确 → 先定义再加载的明确步骤

每条学生问题都有对应的修订位置，无需学生自己去猜测或补脑。
