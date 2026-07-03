# 参考实现 — L65_visual_training

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

`early_stopping()`：追踪历史最优验证损失与“连续未改善”计数器。
一旦连续 `patience` 个 epoch 未刷新最优值，立即返回当前最优 epoch；
若序列走完仍未触发，则返回验证损失最小的 epoch。

```python
def early_stopping(val_losses: list, patience: int) -> int:
    best_epoch = 1
    best_loss  = float('inf')
    no_improve = 0
    for epoch, loss in enumerate(val_losses, start=1):
        if loss < best_loss:
            best_loss  = loss
            best_epoch = epoch
            no_improve = 0          # 刷新最优 → 计数器清零
        else:
            no_improve += 1
            if no_improve >= patience:
                return best_epoch    # 连续 patience 次无改善 → 早停
    return best_epoch
```
