# 前导课程 · 代码优先的微积分

够用就好——目标是看懂**梯度下降**和**反向传播**，这是 Month 2 深度学习的内核。

```bash
jupyter lab    # 打开 notebooks/prep_calculus/，从 c1 开始
```

| 笔记 | 学什么 | 连到 Aurora |
|---|---|---|
| `c1_derivatives` | 导数=变化率、数值求导 | 损失对权重的敏感度 |
| `c2_gradients` | 偏导、梯度向量 | 损失=f(百万权重)，梯度指方向 |
| `c3_chain_rule` | 链式法则 | **反向传播的心脏** |
| `c4_gradient_descent` | 沿梯度下山、学习率、拟合直线 | 所有模型训练的内核 |

每课：讲解 → numpy 演示 → ✏️ 填空 → 自动判卷 → 🔗 Aurora 连接。

## 🎨 图形化分册

`v1_visual_calculus.ipynb`（由 `cviz.py` 驱动）：导数=切线斜率、一维/二维梯度下降轨迹、学习率对比。
