# 参考实现 — L63_kws_model

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
class KeywordCNN(nn.Module):
    def __init__(self, n_mels=40, n_classes=10):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=(n_mels, 5), padding=(0, 2))
        self.conv2 = nn.Conv2d(32, 64, kernel_size=(1, 5), padding=(0, 2))
        self.pool  = nn.AdaptiveAvgPool2d((1, 1))   # Global Average Pool → 变长 T 通吃
        self.fc    = nn.Linear(64, n_classes)

    def forward(self, x):
        # x: (B, 1, n_mels, T)
        x = torch.relu(self.conv1(x))   # (B, 32, 1, T)  ← 频率维压成 1
        x = torch.relu(self.conv2(x))   # (B, 64, 1, T)  ← 时间轴 1D 卷积
        x = self.pool(x)                # (B, 64, 1, 1)  ← GAP，与 T 无关
        x = x.view(x.size(0), -1)       # (B, 64)
        return self.fc(x)               # (B, n_classes)
        # 参数量：conv1 6432 + conv2 10304 + fc 650 = 17,386
```

