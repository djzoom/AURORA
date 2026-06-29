# 参考实现 — L59_tensor_basics

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def mel_to_batch(mel_list):
    arr = np.stack(mel_list, axis=0)          # (B, T, n_mels)
    t   = torch.from_numpy(arr).float()       # (B, T, n_mels) float32
    return t.unsqueeze(1)                     # (B, 1, T, n_mels)
```

