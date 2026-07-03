# 参考实现 — L79_music_embed

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def triplet_loss(anchor, positive, negative, margin=0.2):
    """
    Triplet loss for contrastive learning.
    Args:
        anchor, positive, negative: torch.Tensor, shape (B, d)
        margin: float, safety margin
    Returns:
        scalar Tensor
    """
    d_pos = torch.norm(anchor - positive, dim=-1)       # (B,) 锚点↔正样本距离
    d_neg = torch.norm(anchor - negative, dim=-1)       # (B,) 锚点↔负样本距离
    loss = torch.clamp(d_pos - d_neg + margin, min=0.0).mean()
    return loss
```
