# 参考实现 — L36_windows

> ⚠️ 请先独立完成练习，再查看参考实现。

## 参考实现 1

```python
def describe_window(name, w):
    first = w[0]
    last = w[-1]
    peak = w.max()
    peak_idx = int(np.argmax(w))
    print(f'{name}: len={len(w)}, first={first:.4f}, last={last:.4f}, peak={peak:.4f} @ idx={peak_idx}')
    return (first, last, peak, peak_idx)
```

