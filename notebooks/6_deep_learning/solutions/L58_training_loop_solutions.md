# L58 参考实现 — 训练循环（training loop）

本文件提供 `train()` 函数的完整参考实现，供完成练习后对照。

---

## `train()` 完整实现

```python
def train(model, xs, ys, lr=0.05, epochs=100):
    """训练 model，返回每轮的 loss 值列表。"""
    loss_history = []
    for epoch in range(epochs):
        # 1. forward — 对所有样本计算预测
        ypred = [model(x) for x in xs]

        # 2. 计算每个样本的 hinge loss = max(0, 1 - y*pred)
        losses = [(Value(1.0) - Value(y) * p).relu() for p, y in zip(ypred, ys)]

        # 3. 取均值得到标量 loss
        loss = sum(losses) * (1.0 / len(losses))

        # 4. 反向传播
        loss.backward()

        # 5. 参数更新（梯度下降）
        for p in model.parameters():
            p.data -= lr * p.grad

        # 6. 清零梯度，防止下轮累积
        for p in model.parameters():
            p.grad = 0.0

        loss_history.append(loss.data)
        if (epoch + 1) % 20 == 0:
            print(f'epoch {epoch+1:3d}  loss={loss.data:.4f}')
    return loss_history
```

---

## 关键设计说明

### 为什么输出层不用 ReLU？

隐层使用 ReLU 是为了引入非线性、帮助网络学习复杂边界。但输出层的任务是输出一个无界的实数分数（score），供 hinge loss 用 `y * score` 计算 margin：

- 若输出层也施加 ReLU，则 `score >= 0` 恒成立
- 负类（`y = -1`）的损失变为 `max(0, 1 + score) >= 1`，永远非零
- 分类器永远预测正类，准确率卡在 50%

正确做法（`nonlin=False`）允许分数为负，网络才能区分正负类。

### zero_grad 时机

zero_grad 放在参数更新之后、下一轮 forward 之前均可。关键是每轮 `backward` 前必须清零，否则梯度会跨 epoch 累积。

### 验收断言含义

```python
assert history[-1] < history[0]   # 损失总体下降
assert acc > 0.85                  # 月牙形数据集 100 轮后精度应超过 85%
assert len(history) == epochs      # 返回列表长度等于训练轮数
```
