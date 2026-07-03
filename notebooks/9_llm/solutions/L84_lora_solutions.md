# 参考实现 — L84_lora

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
class LoRALinear(nn.Module):
    def __init__(self, in_features, out_features, rank=8, alpha=1.0):
        super().__init__()
        # 1. 冻结的预训练基座（Frozen Base）：bias=False，权重不参与梯度
        self.base = nn.Linear(in_features, out_features, bias=False)
        self.base.weight.requires_grad = False
        # 2. 低秩因子（Low-Rank Factors）：A 随机小高斯，B 零初始化
        self.lora_A = nn.Parameter(torch.randn(rank, in_features) * 0.01)
        self.lora_B = nn.Parameter(torch.zeros(out_features, rank))
        # 3. 缩放因子（Scaling Factor）scale = alpha / rank
        self.scale = alpha / rank

    def forward(self, x):
        base_out = self.base(x)                       # 冻结主路径
        lora_out = (x @ self.lora_A.T) @ self.lora_B.T  # 低秩旁路 ΔW·x = B(Ax)
        return base_out + self.scale * lora_out
```

**要点**：

- `base.weight.requires_grad = False` 冻结预训练权重，可训练参数只剩 `lora_A` + `lora_B`，
  合计 `rank * in_features + out_features * rank`（cell 12 检查 1：`2×64×4 = 512`）。
- `lora_B` 零初始化保证训练起点 `ΔW = B·A = 0`，输出与预训练完全一致（无扰动启动）。
- `(x @ lora_A.T) @ lora_B.T` 先降维到 `rank` 再升回 `out_features`，对 2D `(batch, d)`
  和 3D `(batch, seq, d)` 输入都通过广播自动兼容（cell 12 检查 2/4）。
- `scale = alpha / rank`；当 `alpha=8, rank=4` 时 `scale=2.0`（cell 12 检查 5）。
