# 参考实现 — L63_kws_model

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
class KeywordCNN(nn.Module):
    def __init__(self, n_mels=40, n_classes=10):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=(n_mels, 5), padding=(0, 2))
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.pool  = nn.MaxPool2d(kernel_size=(1, 2))
        self.fc    = nn.Linear(64, n_classes)

    def forward(self, x):
        # x: (B, 1, n_mels, T)
        x = torch.relu(self.conv1(x))   # (B, 32, 1, T)
        x = torch.relu(self.conv2(x))   # (B, 64, 1, T)
        x = self.pool(x)                # (B, 64, 1, T//2)
        x = x.mean(dim=-1).squeeze(dim=-1)  # (B, 64)
        return self.fc(x)               # (B, n_classes)
```

