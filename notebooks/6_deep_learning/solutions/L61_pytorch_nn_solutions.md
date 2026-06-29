# 参考实现 — L61_pytorch_nn

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
class AudioMLP(nn.Module):
    def __init__(self, in_features, hidden, out_features):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(in_features, hidden),
            nn.ReLU(),
            nn.Linear(hidden, out_features),
        )

    def forward(self, x):
        return self.layers(x)
```

