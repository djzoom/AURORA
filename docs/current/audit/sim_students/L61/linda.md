# 琳达 — L61 学习日志

## 我理解了什么

理解了 `nn.Module` 把参数"登记"给 PyTorch，这样优化器能找到它们、存盘和加载；学会用 `nn.Sequential` 串联 Linear→ReLU→Linear，省掉手写 `forward()` 的麻烦；算出 AudioMLP 的参数数量（40×64+64 + 64×10+10 = 3,274）并验证了。

## 遇到的困难和问题

### 【理解】`nn.Linear` 权重为什么是 `(64, 40)` 不是 `(40, 64)`？

课程说 `layers[0].weight.shape` 应该是 `(64, 40)`——即输出维度在前、输入维度在后。这和直觉相反啊，向量从 40 维变 64 维，为什么权重矩阵要写成 64×40 而不是 40×64？代码里矩阵乘法是 `x @ weight` 吗，还是 `weight @ x`？没有推导过程，我不太能理解这个设计。

### 【理解】为什么一定要用 `nn.Parameter` 包裹，不能用普通 `torch.Tensor`？

演示代码展示了"用 Parameter 注册、普通 Tensor 不注册"的区别，但为什么这个区别这么关键？代码层面明白了（`parameters()` 能找到/找不到），但不懂**为什么优化器非得通过 `parameters()` 迭代来发现梯度**。高中数学没教过这个，是 PyTorch 的设计规则吗？

### 【实践】`register_buffer()` 那个表格，"不需要梯度但要跟着模型一起搬设备"这个需求什么时候会出现？

表格列出了三种状态（Parameter、buffer、普通张量），区别在于"梯度""出现在 state_dict"。代码提到 BatchNorm 的 running mean，但这课本身没有 BatchNorm，所以我感受不到这个需求。什么时候我会写 `register_buffer()`？能举个这课内相关的例子吗？

### 【理解】`state_dict()` 为什么只保存权重参数值，不保存"怎么用这些参数计算"的信息？

代码说 `torch.save(model.state_dict(), 'ckpt.pt')` 然后 `model.load_state_dict(torch.load('ckpt.pt'))` 就能恢复模型。但 state_dict 只有数字（权重值），没有"这是个两层 MLP"这样的信息。怎么保证加载进去的模型结构是对的？是得先定义好模型类，然后才能 load 吗？

---
